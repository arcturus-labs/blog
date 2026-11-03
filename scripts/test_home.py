"""Run after `mkdocs build`: python3 scripts/test_home.py.

Checks post selection (including escaping/redirects), published asset references,
metadata and canonical URLs. Does not contact Kit or require network access.
"""
import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("recent_posts", ROOT / "hooks/recent_posts.py")
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class HomeTests(unittest.TestCase):
    def test_post_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp)
            (site / "index.html").write_text(hook.START + "fallback" + hook.END)
            for i in range(1, 8):
                p = site / f"blog/2026/01/{i:02}/post-{i}/index.html"
                p.parent.mkdir(parents=True)
                p.write_text(f'<title>Post {i} &amp; AI - Arcturus Labs</title>'
                             '<meta name="description" content="&lt;script&gt; &amp; more.">')
            p = site / "blog/2027/01/01/redirect/index.html"
            p.parent.mkdir(parents=True)
            p.write_text('<meta http-equiv="refresh" content="0"><title>Redirect</title>')
            self.assertEqual([x[0].day for x in hook._posts(site)], [7, 6, 5, 4, 3])
            hook.on_post_build({"site_dir": site})
            rendered = (site / "index.html").read_text()
            self.assertEqual(rendered.count("<li>"), 5)
            self.assertIn("Post 7 &amp; AI", rendered)
            self.assertIn("&lt;script&gt;", rendered)
            self.assertNotIn("<script>", rendered)
            hook.on_post_build({"site_dir": site})
            self.assertEqual(rendered, (site / "index.html").read_text())
            # Removing a post promotes the next newest item on the next build.
            (site / "blog/2026/01/07/post-7/index.html").unlink()
            hook.on_post_build({"site_dir": site})
            self.assertNotIn("Post 7", (site / "index.html").read_text())
            self.assertIn("Post 2", (site / "index.html").read_text())

    def test_built_pages(self):
        for page in ("index.html", "agentic-web.html", "workflows.html", "software-factories.html"):
            text = (ROOT / "site" / page).read_text()
            self.assertEqual(text.count("gtag('config', 'G-9ZGCYE3982')"), 1)
            canonical = "https://arcturus-labs.com/" + ("" if page == "index.html" else page)
            self.assertIn(f'<link rel="canonical" href="{canonical}">', text)
            for tag in ("og:type", "og:site_name", "og:url", "og:title", "og:description", "og:image", "twitter:card", "twitter:title", "twitter:description", "twitter:image"):
                self.assertEqual(text.count(f'="{tag}"'), 1, (page, tag))
            for ref in re.findall(r'(?:href|src)="([^"]+)"', text):
                if ref.startswith(("http", "#", "mailto:")):
                    continue
                p = ROOT / "site" / ref.lstrip("/")
                self.assertTrue(p.exists(), (page, ref))
            for asset in re.findall(r'home/assets/([\w.\-]+)', text):
                self.assertTrue((ROOT / "site/home/assets" / asset).is_file(), asset)
            self.assertIn('href="/blog/"', text)
            self.assertIn('action="https://app.convertkit.com/forms/7337584/subscriptions"', text)
        index = (ROOT / "site/index.html").read_text()
        items = index.split(hook.START)[1].split(hook.END)[0]
        self.assertEqual(items.count("<li>"), 5)
        self.assertEqual(items.count("<time "), 5)
        for url in re.findall('href="([^"]+)"', items):
            self.assertTrue((ROOT / "site" / url.lstrip("/") / "index.html").is_file())


if __name__ == "__main__":
    unittest.main()
