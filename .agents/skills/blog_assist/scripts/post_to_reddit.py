#!/usr/bin/env python3
"""Post approved Reddit drafts using Reddit's OAuth API.

Dry-run is the default. Pass --post only after John has approved the drafts.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ENV_KEYS = [
    "REDDIT_CLIENT_ID",
    "REDDIT_CLIENT_SECRET",
    "REDDIT_USERNAME",
    "REDDIT_PASSWORD",
    "REDDIT_USER_AGENT",
]


def setup_instructions() -> str:
    return """Reddit setup:
1. Create a script app at https://www.reddit.com/prefs/apps
2. Add these values to .env:
   REDDIT_CLIENT_ID=<short id under app name>
   REDDIT_CLIENT_SECRET=<secret from app page>
   REDDIT_USERNAME=<reddit username>
   REDDIT_PASSWORD=<reddit password>
   REDDIT_USER_AGENT=arcturus-blog-poster by u/<reddit username>
   REDDIT_REDIRECT_URI=http://localhost:8080
3. Keep .env gitignored and never commit Reddit credentials.
4. Run this script without --post first to preview, then rerun with --post after John approves."""


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def require_env() -> dict[str, str]:
    values = {key: os.environ.get(key, "") for key in ENV_KEYS}
    missing = [key for key, value in values.items() if not value or value.startswith("TODO_")]
    if missing:
        raise RuntimeError(f"Missing Reddit env values: {', '.join(missing)}\n\n{setup_instructions()}")
    return values


def request_json(url: str, data: dict[str, str], headers: dict[str, str]) -> dict[str, Any]:
    encoded = urllib.parse.urlencode(data).encode()
    request = urllib.request.Request(url, data=encoded, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"Reddit API HTTP {exc.code}: {body}\n\n{setup_instructions()}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Reddit API: {exc}\n\n{setup_instructions()}") from exc


def get_access_token(env: dict[str, str]) -> str:
    credentials = f"{env['REDDIT_CLIENT_ID']}:{env['REDDIT_CLIENT_SECRET']}".encode()
    auth = base64.b64encode(credentials).decode()
    result = request_json(
        "https://www.reddit.com/api/v1/access_token",
        {
            "grant_type": "password",
            "username": env["REDDIT_USERNAME"],
            "password": env["REDDIT_PASSWORD"],
            "scope": "submit",
        },
        {
            "Authorization": f"Basic {auth}",
            "User-Agent": env["REDDIT_USER_AGENT"],
        },
    )
    token = result.get("access_token")
    if not token:
        raise RuntimeError(f"Reddit did not return an access token: {result}\n\n{setup_instructions()}")
    return token


def submit_post(post: dict[str, Any], token: str, user_agent: str) -> dict[str, Any]:
    kind = post.get("kind", "self")
    data = {
        "api_type": "json",
        "sr": required_post_value(post, "subreddit"),
        "title": required_post_value(post, "title"),
        "kind": kind,
        "sendreplies": str(post.get("sendreplies", post.get("send_replies", True))).lower(),
        "resubmit": str(post.get("resubmit", True)).lower(),
    }

    for optional_field in ("flair_id", "flair_text"):
        if post.get(optional_field):
            data[optional_field] = str(post[optional_field])

    if kind == "self":
        data["text"] = required_post_value(post, "selftext")
    elif kind == "link":
        data["url"] = required_post_value(post, "url")
    else:
        raise RuntimeError(f"Unsupported post kind {kind!r}; use 'self' or 'link'.")

    result = request_json(
        "https://oauth.reddit.com/api/submit",
        data,
        {
            "Authorization": f"Bearer {token}",
            "User-Agent": user_agent,
        },
    )
    errors = result.get("json", {}).get("errors", [])
    if errors:
        raise RuntimeError(f"Reddit rejected r/{data['sr']} submission: {errors}\n\n{setup_instructions()}")
    return result


def submit_comment(thing_id: str, text: str, token: str, user_agent: str) -> dict[str, Any]:
    result = request_json(
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
    errors = result.get("json", {}).get("errors", [])
    if errors:
        raise RuntimeError(f"Reddit rejected follow-up comment: {errors}\n\n{setup_instructions()}")
    return result


def required_post_value(post: dict[str, Any], key: str) -> str:
    value = post.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"Post for r/{post.get('subreddit', '?')} is missing required field: {key}")
    return value.strip()


def load_posts(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text())
    posts = payload.get("posts") if isinstance(payload, dict) else payload
    if not isinstance(posts, list):
        raise RuntimeError("Draft file must be a JSON list or an object with a 'posts' list.")
    return posts


def preview(posts: list[dict[str, Any]]) -> None:
    for post in posts:
        print(f"r/{post.get('subreddit')} [{post.get('kind', 'self')}] {post.get('title')}")
        if post.get("url"):
            print(f"  url: {post['url']}")
        if post.get("selftext"):
            print(f"  body: {post['selftext'][:220].replace(chr(10), ' ')}")
        if post.get("first_comment"):
            print(f"  first comment: {post['first_comment'][:160].replace(chr(10), ' ')}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview or submit approved Reddit drafts.")
    parser.add_argument("drafts", type=Path, help="JSON file containing Reddit post drafts")
    parser.add_argument("--env-file", type=Path, default=Path(".env"))
    parser.add_argument("--post", action="store_true", help="Actually submit to Reddit")
    args = parser.parse_args()

    load_dotenv(args.env_file)
    posts = load_posts(args.drafts)

    if not args.post:
        preview(posts)
        print("\nDry run only. After John approves, rerun with --post.")
        return 0

    env = require_env()
    token = get_access_token(env)
    for post in posts:
        result = submit_post(post, token, env["REDDIT_USER_AGENT"])
        submitted = result.get("json", {}).get("data", {})
        thing_id = submitted.get("name")
        print(f"Posted r/{post['subreddit']}: {submitted.get('url', submitted)}")
        if thing_id and post.get("first_comment"):
            submit_comment(thing_id, post["first_comment"], token, env["REDDIT_USER_AGENT"])
            print(f"Commented on r/{post['subreddit']} submission.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
