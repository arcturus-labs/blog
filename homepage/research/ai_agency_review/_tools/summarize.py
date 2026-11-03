"""Compact summary of a crawl.json: sections, global nav, and outlinks of key pages.
usage: python3 -I summarize.py <crawl.json>"""
import sys, json, re, urllib.parse
from collections import Counter
d = json.load(open(sys.argv[1])); pages = d["pages"]
ok = {k: v for k, v in pages.items() if "links" in v}
def path(u): return urllib.parse.urlsplit(u).path or "/"
def section(u):
    p = path(u).strip("/").split("/")[0]
    return "/" + p if p else "/"
print(f"crawled {len(ok)} pages (+{d['uncrawled_queue']} uncrawled)")
sec = Counter(section(v["url"]) for v in ok.values())
print("SECTIONS:", ", ".join(f"{s}({n})" for s, n in sec.most_common(10)))
# global nav: internal links in nav/header/footer appearing on >=50% of pages
cnt = Counter(); label = {}
for v in ok.values():
    seen = set()
    for l in v["links"]:
        if l["region"] in ("nav", "header", "footer") and l["internal"]:
            k = urllib.parse.urldefrag(l["abs"])[0].rstrip("/")
            if k not in seen: seen.add(k); cnt[k] += 1; label.setdefault(k, l["text"] or "(icon)")
thr = max(2, len(ok) // 2)
print("GLOBAL NAV/FOOTER:", " | ".join(f"{label[k][:28]} -> {path(k)}" for k, n in cnt.most_common() if n >= thr)[:900])
ext = Counter()
for v in ok.values():
    for l in v["links"]:
        if not l["internal"] and not l["abs"].startswith("mailto"):
            ext[urllib.parse.urlsplit(l["abs"]).netloc.removeprefix("www.")] += 1
print("TOP EXTERNAL DESTINATIONS:", ", ".join(f"{h}({n})" for h, n in ext.most_common(8)))
# inbound counts -> most-linked pages
inb = Counter()
for v in ok.values():
    for u in {urllib.parse.urldefrag(l["abs"])[0].rstrip("/") for l in v["links"] if l["internal"]}:
        inb[u] += 1
print("MOST-LINKED PAGES:", ", ".join(f"{path(u)}({n})" for u, n in inb.most_common(8)))
# key pages: home + pages linked from home main/body (not nav), cap 6; show outlinks in body/main
home = next((v for k, v in ok.items() if path(v["url"]) == "/"), None)
print("MAILTO:", sorted({m for v in ok.values() for m in v["mailto"]})[:3], "| pages with forms:", [path(v["url"]) for v in ok.values() if v["forms"]][:6])
def body_links(v, n=8):
    out = []; s = set()
    for l in v["links"]:
        if l["region"] in ("nav", "header", "footer"): continue
        k = l["abs"]
        if k in s or not l["text"]: continue
        s.add(k); out.append(f"[{l['text'][:30]}]->{'' if l['internal'] else 'EXT '}{path(k) if l['internal'] else urllib.parse.urlsplit(k).netloc}")
        if len(out) >= n: break
    return out
if home:
    print("HOME body links:", "; ".join(body_links(home, 12)))
    seen = 0
    for l in home["links"]:
        if not l["internal"] or l["region"] in ("nav", "header", "footer"): continue
        t = ok.get(urllib.parse.urldefrag(l["abs"])[0].rstrip("/").replace("://www.", "://"))
        t = t or next((v for k, v in ok.items() if v["url"].rstrip("/") == l["abs"].rstrip("/")), None)
        if t and path(t["url"]) != "/":
            print(f"  -> {path(t['url'])}: \"{(t['h1'] or t['title'])[:60]}\" ({t['words']}w) goes to: {'; '.join(body_links(t, 5))}")
            seen += 1
            if seen >= 5: break
