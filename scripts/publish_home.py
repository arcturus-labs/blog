#!/usr/bin/env python3
"""Port the new homepage (draft_site_4) into docs/.

Copies the four pages to docs/, their CSS/JS to docs/home/, referenced images to
docs/home/assets/, rewrites paths, and injects GA, canonical, Open Graph and Twitter tags.
Re-run after editing the draft; output is deterministic.

    python3 -I scripts/publish_home.py
"""
import html
from hashlib import sha256
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SRC = ROOT / "homepage"
DOCS = ROOT / "docs"
PAGES = ["index.html", "agentic-web.html", "workflows.html", "software-factories.html"]
SITE = "https://arcturus-labs.com"
SHARE_IMAGE = f"{SITE}/assets/images/logo_with_background.png"
GA_ID = "G-9ZGCYE3982"
GA = f"""  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
  <script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
  </script>"""


def head_tags(page: str, title: str, desc: str) -> str:
    url = SITE + "/" + ("" if page == "index.html" else page)
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    return f"""  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Arcturus Labs">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:image" content="{SHARE_IMAGE}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{SHARE_IMAGE}">
{GA}
"""


def version_local_assets(text: str, src: Path) -> str:
    """Bind CSS/JS URLs to their content, avoiding mixed deploys in CDN/browser caches."""
    def replace(match):
        attribute, filename = match.groups()
        digest = sha256((src / filename).read_bytes()).hexdigest()[:12]
        return f'{attribute}home/{filename}?v={digest}"'
    return re.sub(r'((?:href|src)=")([\w\-]+\.(?:css|js))(?:\?[^"\s]*)?"', replace, text)


def main(src: Path) -> None:
    (DOCS / "home").mkdir(exist_ok=True)
    (DOCS / "home" / "assets").mkdir(exist_ok=True)
    local_files, asset_files = set(), set()
    for page in PAGES:
        text = (src / page).read_text(encoding="utf-8")
        for ref in re.findall(r'(?:href|src)="([\w\-]+\.(?:css|js))(?:\?[^"\s]*)?"', text):
            local_files.add(ref)
        for ref in re.findall(r'assets/([\w.\-]+)', text):
            asset_files.add(ref)
        title = html.unescape(re.search(r"<title>(.*?)</title>", text, re.S).group(1)).strip()
        desc = html.unescape(re.search(r'<meta name="description" content="(.*?)"', text, re.S).group(1))

        text = version_local_assets(text, src)
        text = re.sub(r'(?<![\w/\-])assets/([\w.\-]+)', r'home/assets/\1', text)
        # Keep internal navigation on this host, including during local preview.
        text = text.replace(f'href="{SITE}/blog/', 'href="/blog/')
        # Keep older blog-post CTAs pointing to the new equivalents.
        if page == "index.html":
            text = text.replace('<section class="proof-intro"', '<span id="about"></span>\n  <section class="proof-intro"', 1)
            text = text.replace('<div class="subscription">', '<div class="subscription" id="contact-blog">', 1)
        text = text.replace("</title>", "</title>\n" + head_tags(page, title, desc).rstrip("\n"), 1)
        if page == "index.html":
            text = re.sub(r'(<ul class="posts">)(.*?)(</ul>)',
                          lambda m: f'{m.group(1)}\n    <!-- recent-posts:start -->{m.group(2)}<!-- recent-posts:end -->\n    {m.group(3)}',
                          text, count=1, flags=re.S)
        (DOCS / page).write_text(text, encoding="utf-8")

    for f in sorted(local_files):
        shutil.copy2(src / f, DOCS / "home" / f)
    for f in sorted(asset_files):
        shutil.copy2(src / "assets" / f, DOCS / "home" / "assets" / f)
    print(f"pages={len(PAGES)} css/js={len(local_files)} assets={len(asset_files)}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC)
