"""Factory-specific copy parsing and clean/repeatable builder checks."""
from pathlib import Path
import re
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import build_software_factories as factory
import story_page as sp


class SoftwareFactoryTests(unittest.TestCase):
    def test_approved_copy_and_editorial_separation(self):
        hero, sub, bridge, problems, solutions = factory.parse_copy(factory.COPY.read_text())
        self.assertEqual(hero, ['Competitors are shipping<br>at the speed of AI',
                                'Getting started is<br>easier than you think'])
        self.assertIn('software development life cycle', sub)
        self.assertEqual(bridge, ['Start with hands-on collaboration', 'Build toward hands-off automation'])
        self.assertEqual(len(problems), 3)
        self.assertEqual(len(solutions), 3)
        self.assertEqual([len(p[2]) for p in problems], [2, 1, 1])
        self.assertEqual([len(s[2]) for s in solutions], [1, 2, 1])
        self.assertEqual(solutions[2][1], 'Future-proof your software factory.')
        self.assertIn('Will your software factory be out of date', problems[2][2][0])
        self.assertIn('agent harnesses', problems[2][2][0])
        self.assertEqual(problems[0][1], 'A faster way to build software is taking shape.')
        self.assertEqual(problems[1][1], 'But an AI software factory is worthless if the process is not dependable.')
        self.assertEqual(factory.SCENES['p3'][0], 'p3-gear-electronics')
        self.assertIn('promote them to more hands-off automation', solutions[0][2][0])
        self.assertIn('Clarify each task together', solutions[1][2][0])
        self.assertIn('adapt as technology changes', solutions[2][2][0])
        quote = factory.render_copy(problems[0][2])
        self.assertIn('<blockquote>', quote)
        self.assertIn('Within weeks, hundreds of engineers', quote)
        self.assertIn('<cite><a href="https://ideas.fin.ai/', quote)
        self.assertNotIn('Competitors appear', quote)
        self.assertIn('product invariants', problems[1][2][0])
        for _, _, paragraphs in problems + solutions:
            self.assertNotIn('Graphic direction', ' '.join(paragraphs))
            self.assertNotIn('Moment 1', ' '.join(paragraphs))
        self.assertEqual(factory.prose('A & B {gold:keep <this>}'),
                         'A &amp; B <span class="gold">keep &lt;this&gt;</span>')

    def test_build_from_empty_output_and_repeat(self):
        original = sp.DRAFT
        try:
            with tempfile.TemporaryDirectory() as folder:
                sp.DRAFT = Path(folder)
                (sp.DRAFT / 'assets').symlink_to(original / 'assets', target_is_directory=True)
                first = factory.build().read_bytes()
                self.assertEqual(first, factory.build().read_bytes())
                text = first.decode()
                self.assertEqual(text.count('class="moment"'), 7)
                self.assertNotIn('Graphic direction', text)
                self.assertNotIn('Moment 1', text)
                self.assertNotIn('{gold:', text)
                self.assertIn('plain-English skills', text)
                self.assertEqual(len(re.findall(r'<span class="gold">', text)), 6)
                self.assertIn('href="software-factories.css"', text)
                self.assertIn('id="s2-verify" data-step="1"', text)
                self.assertIn('https://calendly.com/jfberryman/15min', text)
        finally:
            sp.DRAFT = original


if __name__ == '__main__':
    unittest.main()
