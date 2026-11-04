"""Run with python3 -I tests/builders.py. Does not modify tracked outputs/assets."""
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import story_page as sp
import build_agentic_web
from page_chrome import apply_story_chrome
from proof_component import compact_proof
import re

# Approved pre-migration page: this asserts every byte, including all story copy.
APPROVED_AGENTIC_SHA256 = '8c684a86dc771f66eaf01e0391736e0583e060232aa52e4723296afc12660a9f'


class AgenticWebBuilderTests(unittest.TestCase):
    def test_compact_proof_preserves_story_and_quotes(self):
        original = sp.DRAFT
        try:
            with tempfile.TemporaryDirectory() as folder:
                sp.DRAFT = Path(folder)
                baseline = sp.build_preserved_story('agentic-web.html', 'baseline.html').read_text()
                output = build_agentic_web.build().read_text()
                story = output.split('  <section class="proof-intro"')[0].replace('\n  <link rel="stylesheet" href="compact-proof.css">', '')
                self.assertEqual(story, apply_story_chrome(baseline).split('  <section class="proof-intro"')[0])
                self.assertEqual(re.findall(r'<blockquote>.*?</blockquote>', output, re.S), re.findall(r'<blockquote>.*?</blockquote>', baseline, re.S))
                self.assertIn('Founder, CETA Global; Head of Global Mental Health at Google', output)
                self.assertIn('class="authorship"', output.split('book-right')[1])
                self.assertEqual(output, build_agentic_web.build().read_text())
        finally:
            sp.DRAFT = original

    def test_clean_output_directory_and_repeatability(self):
        original = sp.DRAFT
        try:
            with tempfile.TemporaryDirectory() as folder:
                sp.DRAFT = Path(folder)
                # No generated Agentic page exists here: templates alone must suffice.
                destination = sp.build_preserved_story('agentic-web.html', 'agentic-web.html')
                first = destination.read_bytes()
                self.assertEqual(hashlib.sha256(first).hexdigest(), APPROVED_AGENTIC_SHA256)
                sp.build_preserved_story('agentic-web.html', 'agentic-web.html')
                self.assertEqual(first, destination.read_bytes())
                tail = sp.shared_tail()
                split = tail.index('  <section class="contact')
                expected = compact_proof(tail[:split]) + tail[split:]
                self.assertEqual(sp._tail(), expected.replace('../draft_site/index.html', 'index.html'))
        finally:
            sp.DRAFT = original


if __name__ == '__main__':
    unittest.main()
