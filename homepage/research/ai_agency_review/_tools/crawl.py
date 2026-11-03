"""Small BFS crawler for site-navigation review.
usage: python3 -I crawl.py <start-url> <out-json> [max-pages] [extra-allowed-host,...]
Records per page: title, h1, word count, text excerpt, and every link with its text and region.
Does not execute JavaScript, so client-rendered sites will look thin."""
import sys, json, re, urllib.request, urllib.parse
from html.parser import HTMLParser
from collections import deque

UA = {"User-Agent": "Mozilla/5.0 (site-review crawler)"}
REGIONS = {"nav", "header", "footer", "main", "aside"}

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack = []; self.links = []; self.title = ""; self.h1 = ""; self.text = []
        self._in = None; self._a = None; self._buf = ""; self.forms = 0; self.skip = 0; self.mailto = set()
    def region(self):
        for t in reversed(self.stack):
            if t in REGIONS: return t
        return "body"
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript", "svg"): self.skip += 1
        if tag in REGIONS: self.stack.append(tag)
        if tag == "title": self._in = "title"
        if tag == "h1": self._in = "h1"
        if tag == "form": self.forms += 1
        if tag == "a" and a.get("href"):
            h = a["href"]
            if h.startswith("mailto:"): self.mailto.add(h)
            self._a = {"href": h, "text": "", "region": self.region()}
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self.skip: self.skip -= 1
        if tag in REGIONS and tag in self.stack:
            while self.stack and self.stack.pop() != tag: pass
        if tag in ("title", "h1"): self._in = None
        if tag == "a" and self._a is not None:
            self._a["text"] = re.sub(r"\s+", " ", self._a["text"]).strip(); self.links.append(self._a); self._a = None
    def handle_data(self, d):
        if self.skip: return
        if self._in == "title": self.title += d
        if self._in == "h1": self.h1 += d
        if self._a is not None: self._a["text"] += d
        self.text.append(d)

def norm(u):
    u, _ = urllib.parse.urldefrag(u)
    p = urllib.parse.urlsplit(u)
    path = p.path or "/"
    if path != "/" and path.endswith("/"): path = path[:-1]
    return urllib.parse.urlunsplit((p.scheme, p.netloc.lower().removeprefix("www."), path, "", ""))

def main():
    start, out = sys.argv[1], sys.argv[2]
    cap = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    extra = set(sys.argv[4].split(",")) if len(sys.argv) > 4 and sys.argv[4] else set()
    host = urllib.parse.urlsplit(start).netloc.lower().removeprefix("www.")
    allowed = {host} | extra
    q = deque([start]); seen = {norm(start)}; pages = {}
    skip_ext = re.compile(r"\.(png|jpe?g|gif|svg|webp|pdf|zip|mp4|mp3|css|js|ico|xml|json|txt)(\?|$)", re.I)
    while q and len(pages) < cap:
        url = q.popleft()
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=20) as r:
                if "html" not in (r.headers.get("content-type") or ""): continue
                final = r.geturl(); html = r.read().decode("utf-8", "replace")
        except Exception as e:
            pages[norm(url)] = {"url": url, "error": str(e)}; continue
        p = P(); p.feed(html)
        words = re.sub(r"\s+", " ", " ".join(p.text)).strip()
        links = []
        for l in p.links:
            h = l["href"]
            if h.startswith(("javascript:", "#", "tel:")): continue
            if h.startswith("mailto:"): links.append({**l, "abs": h, "internal": False}); continue
            absu = urllib.parse.urljoin(final, h)
            ph = urllib.parse.urlsplit(absu).netloc.lower().removeprefix("www.")
            internal = ph in allowed
            links.append({**l, "abs": absu, "internal": internal})
            if internal and not skip_ext.search(absu):
                n = norm(absu)
                if n not in seen: seen.add(n); q.append(absu)
        pages[norm(final)] = {"url": final, "title": re.sub(r"\s+", " ", p.title).strip(), "h1": re.sub(r"\s+", " ", p.h1).strip(),
            "words": len(words.split()), "excerpt": words[:600], "forms": p.forms, "mailto": sorted(p.mailto), "links": links}
    json.dump({"start": start, "pages": pages, "uncrawled_queue": len(q)}, open(out, "w"), indent=1)
    print(f"{start}: {len(pages)} pages, {len(q)} left in queue")
main()
