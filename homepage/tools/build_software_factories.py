"""Build the replacement Software Factories story from its maintained Markdown.

No previous generated page is read. Ordinary rebuilds use committed artwork;
HOMEPAGE_SCENES can point at supporting_images to re-export selected originals.
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import story_page as sp
from constellation_assets import export
from PIL import Image

COPY = Path(__file__).resolve().parents[1] / 'software-factories-copy.md'
SCENES = {
    'p1': ('p1-assembly-v2', 'Three robots assemble the same widget from left to right: an open chassis, the chassis with an upright gear, then the chassis retaining its gear and gaining a pipe.'),
    'p2': ('p2-tangle', 'A stalled robot examines a widget tangled in cables beside two mismatched widgets.'),
    'p3': ('p3-gear-electronics', 'A robot holds a clean mechanical cogwheel beside a sleek sealed electronic machine with no place to fit the gear.'),
    's1': ('s1-together', 'A human and robot work side by side, each assembling part of a widget.'),
    's2': ('s2-blueprint', 'A human points to a widget blueprint while a robot studies the same plan.'),
    's2-verify': ('s2-verify', 'A human measures a finished widget with a caliper while a robot watches.'),
    's3': ('s3-manual', 'A human shares one open instruction manual with two robots.'),
}


def prose(text):
    """Only explicit gold spans and hero line breaks become markup."""
    return re.sub(r'\{gold:([^}]+)\}', r'<span class="gold">\1</span>',
                  html.escape(text, quote=False).replace('&lt;br&gt;', '<br>'))


def render_copy(paragraphs):
    """Render plain copy or a standalone quotation with linked attribution."""
    if paragraphs and paragraphs[0].startswith('> '):
        if len(paragraphs) != 2:
            raise ValueError('A quotation must have exactly one linked attribution')
        link = re.fullmatch(r'\[([^\]]+)\]\((https://[^\s)]+)\)', paragraphs[1])
        if not link:
            raise ValueError('Missing HTTPS quotation attribution')
        label, url = link.groups()
        return ('<blockquote><p>' + prose(paragraphs[0][2:]) + '</p><cite><a href="' +
                html.escape(url, quote=True) + '">' + html.escape(label) +
                '</a></cite></blockquote>')
    return ''.join('<p>' + prose(p) + '</p>' for p in paragraphs)


def parse_copy(text):
    hero = text.split('## Hero\n', 1)[1].split('## The problem', 1)[0]
    headlines = re.findall(r'^# (.+)$', hero, re.M)
    sub = '\n'.join(line for line in hero.splitlines()
                    if line and not line.startswith('#') and line != 'Software factories')
    def section(start, end):
        content = text.split(start, 1)[1].split(end, 1)[0]
        result = []
        for number, heading, body in re.findall(r'^### (\d+)\. ([^\n]+)\n(.*?)(?=^### |\Z)', content, re.M | re.S):
            # Editorial navigation and graphic notes never become visible copy.
            paragraphs = [p.replace('\n', ' ').strip() for p in body.strip().split('\n\n')
                          if p.strip() and not p.lstrip().startswith(('*', '#'))]
            result.append((int(number) - 1, heading, paragraphs))
        return result
    problems = section('## The problem\n', '## Turn into the solution')
    solutions = section('## The solution\n', '## Proof, contact, and footer')
    bridge = text.split('## Turn into the solution\n', 1)[1].split('## The solution', 1)[0]
    bridge_lines = re.findall(r'^# (.+)$', bridge, re.M)
    if len(headlines) != 2 or len(bridge_lines) != 2 or len(problems) != 3 or len(solutions) != 3:
        raise ValueError('Expected two hero/bridge lines and three problem/solution headings')
    return headlines, sub, bridge_lines, problems, solutions


def art(key):
    folder, alt = SCENES[key]
    prefix = 'sf-constellation-' + folder
    assets = sp.DRAFT / 'assets'
    size = sp.cached_scene(assets, prefix)
    if not size:
        export(sp.SCENES / 'software-factory-constellations' / folder / 'image-01.png', assets, prefix)
        # Common transparent canvas keeps the two solution-2 scenes stationary.
        for width in (960, 1536):
            path = assets / f'{prefix}-{width}.webp'
            image = Image.open(path).convert('RGBA')
            canvas = Image.new('RGBA', (width, width * 2 // 3))
            image.thumbnail((int(width * .94), int(canvas.height * .94)), Image.Resampling.LANCZOS)
            canvas.alpha_composite(image, ((canvas.width - image.width) // 2, (canvas.height - image.height) // 2))
            canvas.save(path, quality=92, method=4)
        size = (1536, 1024)
    return dict(prefix=prefix, alt=alt, size=size)


def build():
    headlines, sub, bridge, problem_copy, solution_copy = parse_copy(COPY.read_text())
    def moment(key, step, heading, paragraphs):
        return dict(id=key, step=step, heading=html.escape(heading, quote=False),
                    copy=render_copy(paragraphs), **art(key))
    problems = [moment('p' + str(step + 1), step, heading, paragraphs)
                for step, heading, paragraphs in problem_copy]
    solutions = []
    for step, heading, paragraphs in solution_copy:
        if step == 1:
            if len(paragraphs) != 2:
                raise ValueError('Solution 2 requires shared-understanding and verification moments')
            solutions.extend([moment('s2', step, heading, paragraphs[:1]),
                              moment('s2-verify', step, heading, paragraphs[1:])])
        else:
            solutions.append(moment('s' + str(step + 1), step, heading, paragraphs))
    return sp.build(dict(
        file='software-factories.html', title='Build your software factory',
        description='Bring agents into your software development life cycle. Start with what you have. Increase autonomy as confidence grows.',
        eyebrow='Software factories', h1=prose(headlines[0]), turn=prose(headlines[1]),
        sub=prose(sub), bridge_a=prose(bridge[0]), bridge_b=prose(bridge[1]),
        problems=problems, solutions=solutions, stylesheet='software-factories.css',
        testimonial_order=['Laura Murray', 'Shantanu Dhaka', 'Corey Griggs', 'Arin Sime'],
    ))


if __name__ == '__main__':
    print(build())
