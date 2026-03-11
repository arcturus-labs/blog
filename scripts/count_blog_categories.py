#!/usr/bin/env python3
"""Extract categories from all blog posts and print counts."""

import re
from pathlib import Path
from collections import Counter

BLOG_POSTS_DIR = Path(__file__).resolve().parent.parent / "docs" / "blog" / "posts"


def extract_frontmatter(content: str) -> str | None:
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1].strip()


def extract_categories(frontmatter: str) -> list[str]:
    categories = []
    in_categories = False
    for line in frontmatter.splitlines():
        if line.strip() == "categories:":
            in_categories = True
            continue
        if in_categories:
            m = re.match(r"^\s*-\s+(.+)$", line)
            if m:
                categories.append(m.group(1).strip())
            elif line.strip() and not line.startswith(" "):
                break
            elif not line.strip():
                continue
            else:
                break
    return categories


def main() -> None:
    counter: Counter[str] = Counter()
    for path in sorted(BLOG_POSTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(text)
        if fm:
            for cat in extract_categories(fm):
                counter[cat] += 1

    for cat, count in counter.most_common():
        print(f"{count:3}  {cat}")


if __name__ == "__main__":
    main()
