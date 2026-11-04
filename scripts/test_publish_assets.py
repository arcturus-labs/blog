"""Regression checks for cache-safe homepage publishing."""
import hashlib
from pathlib import Path
import re
import tempfile
import unittest

from publish_home import version_local_assets, ROOT, PAGES


class AssetVersions(unittest.TestCase):
    def test_urls_follow_contents_not_previous_versions(self):
        with tempfile.TemporaryDirectory() as folder:
            src = Path(folder)
            (src / 'styles.css').write_text('old CSS')
            (src / 'story.js').write_text('JS')
            html = '<link href="styles.css"><script src="story.js?v=stale"></script>'
            before = version_local_assets(html, src)
            self.assertEqual(before, version_local_assets(html, src))
            css = hashlib.sha256(b'old CSS').hexdigest()[:12]
            self.assertIn(f'home/styles.css?v={css}', before)
            self.assertNotIn('stale', before)
            (src / 'styles.css').write_text('new grouped CSS')
            after = version_local_assets(html, src)
            self.assertNotEqual(before, after)
            self.assertEqual(re.findall(r'src="([^"]+)"', before), re.findall(r'src="([^"]+)"', after))
            self.assertEqual(after.count('?v='), 2)

    def test_external_and_image_urls_are_untouched(self):
        html = '<script src="https://example.com/a.js"></script><img src="assets/image.webp"><a href="#top">Top</a>'
        self.assertEqual(version_local_assets(html, Path('/nonexistent')), html)

    def test_all_published_assets_are_versioned_and_match_actual_bytes(self):
        for page in PAGES:
            html = (ROOT / 'docs' / page).read_text()
            refs = re.findall(r'(?:href|src)="(home/[\w-]+\.(?:css|js))([^\"]*)"', html)
            self.assertTrue(refs, page)
            for filename, query in refs:
                expected = hashlib.sha256((ROOT / 'docs' / filename).read_bytes()).hexdigest()[:12]
                self.assertEqual(query, f'?v={expected}', (page, filename))


if __name__ == '__main__':
    unittest.main()
