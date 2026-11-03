"""MkDocs hook: fill the homepage "recent posts" list with the five newest blog posts.

docs/index.html contains <!-- recent-posts:start --> ... <!-- recent-posts:end -->.
After the build, we scan site/blog/YYYY/MM/DD/<slug>/index.html (skipping redirect stubs),
take the five newest, and replace the content between the markers in site/index.html.
"""
import datetime
import html
import re
from pathlib import Path

COUNT = 5
START, END = "<!-- recent-posts:start -->", "<!-- recent-posts:end -->"
POST_RE = re.compile(r"blog/(\d{4})/(\d{2})/(\d{2})/([^/]+)/index\.html$")


def _blurb(description: str, limit: int = 130) -> str:
    description = " ".join(description.split())
    first = re.split(r"(?<=[.!?])\s", description, maxsplit=1)[0]
    if len(first) <= limit:
        return first
    cut = first[:limit].rsplit(" ", 1)[0].rstrip(",;:–-")
    return cut + "…"


def _posts(site: Path):
    found = []
    for path in site.glob("blog/*/*/*/*/index.html"):
        m = POST_RE.search(path.relative_to(site).as_posix())
        if not m:
            continue
        text = path.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in text:
            continue
        title = re.search(r"<title>(.*?)</title>", text, re.S)
        if not title:
            continue
        title = html.unescape(title.group(1)).rsplit(" - ", 1)[0].strip()
        desc = re.search(r'<meta name="description" content="(.*?)"', text, re.S)
        y, mo, d, slug = m.groups()
        found.append((datetime.date(int(y), int(mo), int(d)), f"/blog/{y}/{mo}/{d}/{slug}/", title,
                      html.unescape(desc.group(1)) if desc else ""))
    found.sort(key=lambda p: (p[0], p[1]), reverse=True)
    return found[:COUNT]


def on_post_build(config, **kwargs):
    site = Path(config["site_dir"])
    index = site / "index.html"
    text = index.read_text(encoding="utf-8")
    if START not in text or END not in text:
        return
    items = []
    for date, url, title, desc in _posts(site):
        pretty = f"{date.strftime('%B')} {date.day}, {date.year}"
        blurb = f'<span class="blurb">{html.escape(_blurb(desc))}</span>' if desc else ""
        items.append(
            f'        <li><a href="{url}"><time datetime="{date.isoformat()}">{pretty}</time>'
            f'<span><strong>{html.escape(title)}</strong>{blurb}</span></a></li>'
        )
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    index.write_text(head + START + "\n" + "\n".join(items) + "\n    " + END + tail, encoding="utf-8")
