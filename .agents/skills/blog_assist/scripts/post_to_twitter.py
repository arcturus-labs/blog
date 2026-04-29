#!/usr/bin/env python3
"""Post to X/Twitter from a validated JSON blob."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator
from requests_oauthlib import OAuth1Session

API_BASE = "https://api.x.com"
V2_TWEETS_ENDPOINT = f"{API_BASE}/2/tweets"
V2_POSTS_ENDPOINT = f"{API_BASE}/2/posts"
V2_MEDIA_ENDPOINT = f"{API_BASE}/2/media/upload"
V1_MEDIA_ENDPOINT = "https://upload.twitter.com/1.1/media/upload.json"
MAX_POST_CHARS = 4000
DEFAULT_MAX_IMAGE_BYTES = 5 * 1024 * 1024


class TwitterPost(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str
    image_path: str | None = None
    image_url: str | None = None

    @model_validator(mode="after")
    def validate_image_source(self) -> "TwitterPost":
        if self.image_path and self.image_url:
            raise ValueError("Provide only one of image_path or image_url")
        return self


class TwitterPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    posts: list[TwitterPost] = Field(min_length=1)


def require_env(key: str) -> str:
    value = os.environ.get(key, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value


def oauth_session() -> OAuth1Session:
    return OAuth1Session(
        client_key=require_env("X_CONSUMER_KEY"),
        client_secret=require_env("X_SECRET_KEY"),
        resource_owner_key=require_env("X_ACCESS_TOKEN"),
        resource_owner_secret=require_env("X_ACCESS_TOKEN_SECRET"),
    )


def parse_payload(json_blob: str) -> TwitterPayload:
    try:
        return TwitterPayload.model_validate_json(json_blob)
    except ValidationError as exc:
        raise RuntimeError(f"Invalid X payload JSON:\n{exc}") from exc


def load_image(post: TwitterPost) -> tuple[bytes, str]:
    if post.image_path:
        path = Path(post.image_path)
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.exists():
            raise RuntimeError(f"image_path does not exist: {path}")
        data = path.read_bytes()
        mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        return data, mime

    if post.image_url:
        try:
            response = requests.get(post.image_url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise RuntimeError(f"Failed to fetch image_url: {exc}") from exc
        mime = response.headers.get("Content-Type", "").split(";")[0].strip() or mimetypes.guess_type(post.image_url)[0] or "application/octet-stream"
        return response.content, mime

    raise RuntimeError("No image provided. Include image_path or image_url.")


def validate_text_length(text: str) -> None:
    limit = MAX_POST_CHARS
    count = len(text)
    if count > limit:
        raise RuntimeError(f"Post text too long: {count} chars (max {limit})")


def upload_media(session: OAuth1Session, image_bytes: bytes, mime_type: str) -> str:
    if not mime_type.startswith("image/"):
        raise RuntimeError(f"Unsupported image mime type: {mime_type}")
    if len(image_bytes) > DEFAULT_MAX_IMAGE_BYTES:
        raise RuntimeError(f"Image too large: {len(image_bytes)} bytes (max {DEFAULT_MAX_IMAGE_BYTES})")

    # Try v2 media upload first.
    try:
        response = session.post(
            V2_MEDIA_ENDPOINT,
            files={"media": ("image", image_bytes, mime_type)},
            timeout=30,
        )
        if response.ok:
            payload = response.json()
            media_id = payload.get("data", {}).get("id") or payload.get("media_id_string") or payload.get("media_id")
            if media_id:
                return str(media_id)
    except requests.RequestException:
        pass

    # Fallback to v1.1 upload endpoint for broad compatibility.
    try:
        response = session.post(
            V1_MEDIA_ENDPOINT,
            files={"media": ("image", image_bytes, mime_type)},
            timeout=30,
        )
    except requests.RequestException as exc:
        raise RuntimeError(f"Media upload failed: {exc}") from exc
    if not response.ok:
        raise RuntimeError(f"Media upload failed ({response.status_code}): {response.text}")
    payload = response.json()
    media_id = payload.get("media_id_string") or payload.get("media_id")
    if not media_id:
        raise RuntimeError(f"Media upload returned no media_id: {payload}")
    return str(media_id)


def create_post(session: OAuth1Session, text: str, media_id: str | None) -> str:
    body: dict[str, object] = {"text": text}
    if media_id:
        body["media"] = {"media_ids": [media_id]}

    # Try v2 tweets endpoint first.
    for endpoint in (V2_TWEETS_ENDPOINT, V2_POSTS_ENDPOINT):
        try:
            response = session.post(endpoint, json=body, timeout=30)
        except requests.RequestException as exc:
            raise RuntimeError(f"Create post request failed: {exc}") from exc

        if response.ok:
            payload = response.json()
            post_id = payload.get("data", {}).get("id")
            if post_id:
                return str(post_id)
            raise RuntimeError(f"Create post succeeded but no id returned: {payload}")

        # If endpoint isn't available, try the next one.
        if response.status_code in (404, 410):
            continue

        # Permission and auth help.
        if response.status_code in (401, 403):
            raise RuntimeError(
                f"Create post unauthorized ({response.status_code}): {response.text}\n"
                "Ensure app permission is Read and write, then regenerate Access Token and Secret."
            )
        raise RuntimeError(f"Create post failed ({response.status_code}): {response.text}")

    raise RuntimeError("No supported create-post endpoint was available.")


def build_post_url(post_id: str) -> str:
    username = require_env("X_USERNAME")
    return f"https://x.com/{username}/status/{post_id}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Post to X/Twitter from a JSON blob.")
    parser.add_argument("json_blob", help="JSON string matching TwitterPayload schema")
    args = parser.parse_args()

    load_dotenv()
    payload = parse_payload(args.json_blob)
    session = oauth_session()

    for post in payload.posts:
        validate_text_length(post.text)
        media_id = None
        if post.image_path or post.image_url:
            image_bytes, mime_type = load_image(post)
            media_id = upload_media(session, image_bytes, mime_type)
        post_id = create_post(session, post.text, media_id)
        print(f"Posted X: {build_post_url(post_id)}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
