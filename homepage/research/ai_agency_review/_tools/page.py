"""Show a few crawled pages compactly. usage: python3 -I page.py <crawl.json> <path-substring>..."""
import sys, json, urllib.parse
d = json.load(open(sys.argv[1]))["pages"]
for want in sys.argv[2:]:
    for v in d.values():
        if "links" not in v: continue
        p = urllib.parse.urlsplit(v["url"]).path
        if p.rstrip("/") == want.rstrip("/"):
            ctas = []; s = set()
            for l in v["links"]:
                if l["region"] in ("nav", "header", "footer") or not l["text"] or l["abs"] in s: continue
                s.add(l["abs"]); ctas.append(f"[{l['text'][:28]}]->{urllib.parse.urlsplit(l['abs']).path if l['internal'] else 'EXT '+urllib.parse.urlsplit(l['abs']).netloc}")
            print(f"## {p}  h1={v['h1'][:80]!r} {v['words']}w forms={v['forms']}\n   {v['excerpt'][:260]!r}\n   goes to: {'; '.join(ctas[:7])}")
