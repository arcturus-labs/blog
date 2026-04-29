#!/usr/bin/env python3
"""Post to Reddit from a validated JSON blob."""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator


class RedditPost(BaseModel):
    model_config = ConfigDict(extra="forbid")

    subreddit: str
    title: str
    kind: Literal["self", "link"] = "self"
    selftext: str | None = None
    url: str | None = None
    first_comment: str | None = None
    sendreplies: bool = True
    resubmit: bool = True
    flair_id: str | None = None
    flair_text: str | None = None

    @model_validator(mode="after")
    def validate_kind_fields(self) -> "RedditPost":
        if self.kind == "self" and not self.selftext:
            raise ValueError("selftext is required when kind is 'self'")
        if self.kind == "link" and not self.url:
            raise ValueError("url is required when kind is 'link'")
        return self


class RedditPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    posts: list[RedditPost] = Field(min_length=1)


def require_env(key: str) -> str:
    value = os.environ.get(key, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return value


def request_form(url: str, data: dict[str, str], headers: dict[str, str]) -> dict:
    encoded = urllib.parse.urlencode(data).encode()
    request = urllib.request.Request(url, data=encoded, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from Reddit: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Reddit: {exc}") from exc


def get_access_token() -> tuple[str, str]:
    client_id = require_env("REDDIT_CLIENT_ID")
    client_secret = require_env("REDDIT_CLIENT_SECRET")
    username = require_env("REDDIT_USERNAME")
    password = require_env("REDDIT_PASSWORD")
    user_agent = require_env("REDDIT_USER_AGENT")

    basic = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    response = request_form(
        "https://www.reddit.com/api/v1/access_token",
        {
            "grant_type": "password",
            "username": username,
            "password": password,
            "scope": "submit",
        },
        {
            "Authorization": f"Basic {basic}",
            "User-Agent": user_agent,
        },
    )
    token = response.get("access_token")
    if not token:
        raise RuntimeError(f"Reddit token response missing access_token: {response}")
    return token, user_agent


def submit_post(post: RedditPost, token: str, user_agent: str) -> dict:
    body = {
        "api_type": "json",
        "sr": post.subreddit,
        "title": post.title,
        "kind": post.kind,
        "sendreplies": str(post.sendreplies).lower(),
        "resubmit": str(post.resubmit).lower(),
    }
    if post.flair_id:
        body["flair_id"] = post.flair_id
    if post.flair_text:
        body["flair_text"] = post.flair_text
    if post.kind == "self":
        body["text"] = post.selftext or ""
    else:
        body["url"] = post.url or ""

    response = request_form(
        "https://oauth.reddit.com/api/submit",
        body,
        {
            "Authorization": f"Bearer {token}",
            "User-Agent": user_agent,
        },
    )
    errors = response.get("json", {}).get("errors", [])
    if errors:
        raise RuntimeError(f"Reddit rejected r/{post.subreddit} post: {errors}")
    return response


def submit_comment(thing_id: str, text: str, token: str, user_agent: str) -> None:
    response = request_form(
        "https://oauth.reddit.com/api/comment",
        {
            "api_type": "json",
            "thing_id": thing_id,
            "text": text,
        },
        {
            "Authorization": f"Bearer {token}",
            "User-Agent": user_agent,
        },
    )
    errors = response.get("json", {}).get("errors", [])
    if errors:
        raise RuntimeError(f"Reddit rejected follow-up comment: {errors}")


def parse_payload(json_blob: str) -> RedditPayload:
    try:
        return RedditPayload.model_validate_json(json_blob)
    except ValidationError as exc:
        raise RuntimeError(f"Invalid Reddit payload JSON:\\n{exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Post to Reddit from a JSON blob.")
    parser.add_argument("json_blob", help="JSON string matching RedditPayload schema")
    args = parser.parse_args()

    load_dotenv()
    payload = parse_payload(args.json_blob)
    token, user_agent = get_access_token()
    for post in payload.posts:
        result = submit_post(post, token, user_agent)
        submitted = result.get("json", {}).get("data", {})
        thing_id = submitted.get("name")
        print(f"Posted r/{post.subreddit}: {submitted.get('url', submitted)}")
        if thing_id and post.first_comment:
            submit_comment(thing_id, post.first_comment, token, user_agent)
            print(f"Commented on r/{post.subreddit} submission.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
