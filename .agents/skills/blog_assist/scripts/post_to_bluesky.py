#!/usr/bin/env python3
"""Post to Bluesky from a validated JSON blob."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

URL_RE = re.compile(r"https?://[^\s]+")
BLUESKY_TEXT_LIMIT = 300


class BlueskyPost(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str
    image_path: str | None = None
    image_url: str | None = None
    image_alt: str = "Blog post hero image"
    langs: list[str] | None = None
    createdAt: str | None = None

    @model_validator(mode="after")
    def validate_image_source(self) -> "BlueskyPost":
        if bool(self.image_path) == bool(self.image_url):
            raise ValueError("Exactly one of image_path or image_url is required")
        if len(self.text) > BLUESKY_TEXT_LIMIT:
            raise ValueError(
                f"Bluesky text too long: {len(self.text)} chars (max {BLUESKY_TEXT_LIMIT})"
            )
        return self


class BlueskyPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    posts: list[BlueskyPost] = Field(min_length=1)


def require_env(key: str) -> str:
    value = os.environ.get(key, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value


def request_json(
    url: str,
    *,
    data: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    method: str = "POST",
) -> dict[str, Any]:
    payload = None
    merged_headers = {"Content-Type": "application/json"}
    if headers:
        merged_headers.update(headers)
    if data is not None:
        payload = json.dumps(data).encode("utf-8")

    request = urllib.request.Request(url, data=payload, headers=merged_headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from Bluesky: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Bluesky: {exc}") from exc


def create_session() -> tuple[dict[str, Any], str, str]:
    handle = require_env("BLUESKY_HANDLE")
    app_password = require_env("BLUESKY_APP_PASSWORD")
    host = require_env("BLUESKY_PDS_HOST").rstrip("/")
    if not host.startswith("https://"):
        raise RuntimeError("BLUESKY_PDS_HOST must start with https://")

    session = request_json(
        f"{host}/xrpc/com.atproto.server.createSession",
        data={"identifier": handle, "password": app_password},
    )
    if "accessJwt" not in session:
        raise RuntimeError(f"Bluesky createSession response missing accessJwt: {session}")
    return session, host, handle


def build_link_facets(text: str) -> list[dict[str, Any]]:
    facets: list[dict[str, Any]] = []
    encoded = text.encode("utf-8")
    for match in URL_RE.finditer(text):
        url = match.group(0).rstrip(".,!?:;)")
        if not url:
            continue
        prefix = text[: match.start()].encode("utf-8")
        uri_bytes = text[match.start() : match.start() + len(url)].encode("utf-8")
        byte_start = len(prefix)
        byte_end = byte_start + len(uri_bytes)
        if byte_start < 0 or byte_end > len(encoded) or byte_end <= byte_start:
            continue
        facets.append(
            {
                "index": {"byteStart": byte_start, "byteEnd": byte_end},
                "features": [{"$type": "app.bsky.richtext.facet#link", "uri": url}],
            }
        )
    return facets


def load_image(post: BlueskyPost) -> tuple[bytes, str]:
    if post.image_path:
        path = Path(post.image_path)
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.exists():
            raise RuntimeError(f"image_path does not exist: {path}")
        data = path.read_bytes()
        mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        return data, mime

    assert post.image_url
    try:
        with urllib.request.urlopen(post.image_url, timeout=30) as response:
            data = response.read()
            mime = response.headers.get_content_type() or mimetypes.guess_type(post.image_url)[0] or "application/octet-stream"
            return data, mime
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"Failed to fetch image_url ({exc.code}): {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to fetch image_url: {exc}") from exc


def upload_blob(image_bytes: bytes, mime_type: str, access_token: str, host: str) -> dict[str, Any]:
    if len(image_bytes) > 1_000_000:
        raise RuntimeError(f"Image too large: {len(image_bytes)} bytes (max 1000000)")
    if not mime_type.startswith("image/"):
        raise RuntimeError(f"Unsupported image mime type: {mime_type}")

    request = urllib.request.Request(
        f"{host}/xrpc/com.atproto.repo.uploadBlob",
        data=image_bytes,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": mime_type,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from Bluesky uploadBlob: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Bluesky uploadBlob: {exc}") from exc

    blob = payload.get("blob")
    if not isinstance(blob, dict):
        raise RuntimeError(f"uploadBlob response missing blob: {payload}")
    return blob


def submit_post(post: BlueskyPost, session: dict[str, Any], host: str) -> dict[str, Any]:
    image_bytes, mime_type = load_image(post)
    blob = upload_blob(image_bytes, mime_type, session["accessJwt"], host)
    record: dict[str, Any] = {
        "$type": "app.bsky.feed.post",
        "text": post.text,
        "createdAt": post.createdAt or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "embed": {
            "$type": "app.bsky.embed.images",
            "images": [{"alt": post.image_alt, "image": blob}],
        },
    }
    facets = build_link_facets(post.text)
    if facets:
        record["facets"] = facets
    if post.langs:
        record["langs"] = post.langs

    return request_json(
        f"{host}/xrpc/com.atproto.repo.createRecord",
        data={
            "repo": session.get("did"),
            "collection": "app.bsky.feed.post",
            "record": record,
        },
        headers={"Authorization": f"Bearer {session['accessJwt']}"},
    )


def to_web_url(at_uri: str, handle: str) -> str:
    parts = at_uri.split("/")
    if len(parts) >= 5 and parts[-2] == "app.bsky.feed.post":
        return f"https://bsky.app/profile/{handle}/post/{parts[-1]}"
    return at_uri


def parse_payload(json_blob: str) -> BlueskyPayload:
    try:
        return BlueskyPayload.model_validate_json(json_blob)
    except ValidationError as exc:
        raise RuntimeError(f"Invalid Bluesky payload JSON:\\n{exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Post to Bluesky from a JSON blob.")
    parser.add_argument("json_blob", help="JSON string matching BlueskyPayload schema")
    args = parser.parse_args()

    load_dotenv()
    payload = parse_payload(args.json_blob)
    session, host, handle = create_session()
    for post in payload.posts:
        result = submit_post(post, session, host)
        print(f"Posted Bluesky: {to_web_url(str(result.get('uri', '')), handle)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
