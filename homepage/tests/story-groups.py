"""Moments that share a picture are one group: a single picture, one copy per moment.

Run with python3 -I homepage/tests/story-groups.py
"""
from pathlib import Path
import re
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import story_page as sp

PAGES = Path(__file__).resolve().parents[1]


def moment(id, step, prefix, heading='Heading', **extra):
    return dict(id=id, step=step, heading=heading, prefix=prefix, alt='alt', size=(10, 5), copy=f'<p>{id}</p>', **extra)


class GroupingTests(unittest.TestCase):
    def test_consecutive_moments_sharing_step_and_picture_form_one_group(self):
        items = [moment('a', 0, 'one'), moment('b', 0, 'one', heading=None), moment('c', 0, 'one', heading=None),
                 moment('d', 1, 'two'), moment('e', 2, 'two')]
        groups = sp._groups(items)
        self.assertEqual([[m['id'] for m in g] for g in groups], [['a', 'b', 'c'], ['d'], ['e']])

    def test_same_step_but_different_pictures_stay_separate(self):
        groups = sp._groups([moment('a', 1, 'blueprint'), moment('b', 1, 'verify')])
        self.assertEqual([[m['id'] for m in g] for g in groups], [['a'], ['b']])

    def test_markup_draws_the_picture_once_and_keeps_every_copy(self):
        html = sp._moments([moment('p1', 0, 'toil', class_name='quote-overlay'),
                            moment('p1-more', 0, 'toil', class_name='quote-overlay'),
                            moment('p2', 1, 'compare')])
        self.assertEqual(html.count('<figure class="scene">'), 2)
        self.assertEqual(html.count('<img '), 2)
        self.assertEqual(html.count('class="moment"'), 3)
        # The group takes the first moment's id (what the outline links to); later moments keep theirs.
        self.assertIn('<div class="moment-group quote-overlay" id="p1" data-step="0">', html)
        self.assertEqual(re.findall(r'<article class="moment"( id="[^"]+")?>', html), ['', ' id="p1-more"', ''])
        self.assertEqual(html.count('mobile-heading'), 2, 'one heading per group, not per moment')
        self.assertNotIn('data-step="0">\n            <article', html, 'step lives on the group only')
        self.assertIn('<p>p1</p>', html)
        self.assertIn('<p>p1-more</p>', html)

    def test_priority_loading_only_for_the_first_picture(self):
        html = sp._moments([moment('a', 0, 'one'), moment('b', 0, 'one'), moment('c', 1, 'two')], first_page=True)
        self.assertEqual(html.count('fetchpriority="high"'), 1)
        self.assertEqual(html.count('loading="lazy"'), 1)

    def test_a_group_cannot_mix_overlay_and_plain_moments(self):
        with self.assertRaises(AssertionError):
            sp._groups([moment('a', 0, 'one', class_name='quote-overlay'), moment('b', 0, 'one')])


class BuiltPageTests(unittest.TestCase):
    """The generated pages draw each repeated picture once."""

    def groups(self, name):
        html = (PAGES / name).read_text()
        return html, re.findall(r'<div class="moment-group[^"]*" id="([^"]+)" data-step="(\d)">', html)

    def test_agentic_web_solution_three_is_one_picture_and_three_moments(self):
        html, groups = self.groups('agentic-web.html')
        self.assertEqual(len(groups), 6)
        block = html.split('<div class="moment-group" id="s3"')[1].split('</section>')[0]
        self.assertEqual(block.count('<img '), 1)
        self.assertEqual(block.count('class="moment"'), 3)
        self.assertIn('id="s3-shared"', block)
        self.assertIn('id="s3-aware"', block)

    def test_workflows_evidence_is_one_picture_and_three_moments(self):
        html, groups = self.groups('workflows.html')
        self.assertEqual(len(groups), 7)
        block = html.split('id="p1" data-step="0">')[1].split('<div class="moment-group"')[0]
        self.assertEqual(block.count('<img '), 1)
        self.assertEqual(block.count('class="moment"'), 3)
        self.assertEqual(block.count('mobile-heading'), 1)

    def test_every_page_has_one_picture_per_group_and_no_repeats_in_a_row(self):
        for name, pictures in (('agentic-web.html', 6), ('workflows.html', 7), ('software-factories.html', 7)):
            html, groups = self.groups(name)
            sources = re.findall(r'<figure class="scene"><img [^>]* src="([^"]+)"', html)
            self.assertEqual(len(sources), pictures, name)
            self.assertEqual(len(groups), pictures, name)
            self.assertFalse([s for i, s in enumerate(sources) if i and s == sources[i - 1]], name)


if __name__ == '__main__':
    unittest.main()
