"""Assemble a story page that matches homepage/agentic-web.html.

Reuses the shared styles.css, story.js, sky.js and subscribe.js unchanged, and
loads maintained proof, contact and footer markup from templates/story-tail.html.
Generated pages are never used as builder input.

Usage (from a page script): build(config). See build_workflows.py.
"""
from pathlib import Path
import re
import numpy as np
from PIL import Image
from scipy import ndimage

DRAFT = Path(__file__).resolve().parent.parent
# Large generated-image originals (~200 MB) are deliberately not in this repo.
import os
SCENES = Path(os.environ.get('HOMEPAGE_SCENES', str(DRAFT / 'image_sources')))


def cached_scene(assets: Path, prefix: str):
    """Ordinary copy rebuilds use committed exports, without raw-image dependencies."""
    if os.environ.get('HOMEPAGE_REBUILD_ASSETS') == '1':
        return None
    paths = [assets / f'{prefix}-{width}.webp' for width in (960, 1536)]
    if all(p.is_file() for p in paths):
        with Image.open(paths[-1]) as image:
            return image.size
    return None


def export_scene(folder: Path, prefix: str) -> tuple[int, int]:
    """Chroma-key the newest render in folder to alpha WebP (960 and 1536 wide).

    Removes border-connected key green and near-pure-key-green islands enclosed
    by hand-drawn red circles. App interiors, map greens and foliage are kept.
    Returns the pixel size of the 1536-wide export.
    """
    size = cached_scene(DRAFT / 'assets', prefix)
    if size:
        return size
    renders = sorted(p for p in folder.glob('image-*.png') if 'transparent' not in p.stem)
    if not renders:
        raise FileNotFoundError(f'No image originals in {folder}; set HOMEPAGE_SCENES or restore committed WebP exports.')
    source = renders[-1]
    arr = np.array(Image.open(source).convert('RGBA'))
    r, g, b = [arr[:, :, k].astype(float) for k in range(3)]
    mask = (g > 140) & (g - r > 65) & (g - b > 65)
    seed = np.zeros(mask.shape, bool)
    seed[0, :], seed[-1, :], seed[:, 0], seed[:, -1] = mask[0, :], mask[-1, :], mask[:, 0], mask[:, -1]
    bg = ndimage.binary_propagation(seed, mask=mask)
    bg |= (g > 210) & (r < 65) & (b < 65)
    arr[bg] = 0
    edge = ndimage.binary_dilation(bg, iterations=2) & ~bg
    spill = edge & (g > r + 25) & (g > b + 25)
    arr[:, :, 3][spill] = np.clip(255 - (g - np.maximum(r, b)), 0, 255)[spill].astype('uint8')
    arr[:, :, 1][spill] = np.minimum(g[spill], np.maximum(r, b)[spill] + 10).astype('uint8')
    image = Image.fromarray(arr)
    image.save(source.with_name(source.stem + '-transparent.png'))
    image = image.crop(image.getbbox())
    size = (0, 0)
    for width in (960, 1536):
        small = image.copy()
        small.thumbnail((width, 1400))
        small.save(DRAFT / 'assets' / f'{prefix}-{width}.webp', quality=92, method=4)
        if width == 1536:
            size = small.size
    return size


def _img(prefix, alt, size, first=False):
    w, h = size
    loading = 'fetchpriority="high"' if first else 'loading="lazy"'
    return (f'<figure class="scene"><img width="{w}" height="{h}" '
            f'srcset="assets/{prefix}-960.webp 960w, assets/{prefix}-1536.webp 1536w" '
            f'sizes="(max-width: 900px) 90vw, 65vw" src="assets/{prefix}-1536.webp" '
            f'alt="{alt}" {loading}></figure>')


def _moments(items, first_page=False):
    """items: list of dict(id, step, heading|None, prefix, alt, copy)."""
    out = []
    for n, m in enumerate(items):
        heading = f'          <h2 class="mobile-heading">{m["heading"]}</h2>\n' if m.get('heading') else ''
        out.append(
            f'        <article class="moment{(" " + m["class_name"]) if m.get("class_name") else ""}" id="{m["id"]}" data-step="{m["step"]}">\n{heading}'
            f'          {_img(m["prefix"], m["alt"], m["size"], first=first_page and n == 0)}\n'
            f'          <div class="moment-copy">{m["copy"]}</div>\n        </article>')
    return '\n'.join(out)


def _outline(items):
    seen, out = set(), []
    for m in items:
        if m.get('heading') and m['step'] not in seen:
            seen.add(m['step'])
            out.append(f'          <li><a href="#{m["id"]}" data-step="{m["step"]}"><span class="number">{m["step"] + 1:02d}</span><span>{m["heading"]}</span></a></li>')
    return '\n'.join(out)


def shared_tail():
    """Canonical shared markup; never extract components from generated pages."""
    return (Path(__file__).parent / 'templates' / 'story-tail.html').read_text()


def build_preserved_story(template, destination):
    """Render an approved story verbatim without rekeying its existing assets."""
    source = (Path(__file__).parent / 'templates' / template).read_text()
    assert source.count('{{ shared_tail }}') == 1
    html = source.replace('{{ shared_tail }}\n', shared_tail())
    (DRAFT / destination).write_text(html)
    return DRAFT / destination


def _tail(testimonial_order=None):
    tail = shared_tail()
    if testimonial_order:
        block = re.search(r'<div class="testimonials">\n(.*?)\n      </div>', tail, re.S)
        figures = re.findall(r'        <figure>.*?</figure>', block.group(1), re.S)
        ordered = sorted(figures, key=lambda f: next(i for i, name in enumerate(testimonial_order) if name in f))
        tail = tail.replace(block.group(1), '\n'.join(ordered))
    from proof_component import compact_proof
    split = tail.index('  <section class="contact')
    tail = compact_proof(tail[:split]) + tail[split:]
    return tail.replace('../draft_site/index.html', 'index.html')


def build(cfg):
    head = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{cfg["description"]}">
  <title>{cfg["title"]} | Arcturus Labs</title>
  <link rel="icon" href="assets/favicon.ico">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="compact-proof.css">
  <script src="story.js" defer></script>
  <script src="sky.js" defer></script>
  <script src="subscribe.js" defer></script>
</head>
<body>
<canvas id="sky" aria-hidden="true"></canvas>
<a class="skip" href="#problem">Skip to the story</a>
<header class="opening-nav">
  <a class="brand" href="index.html"><img src="assets/logo.png" alt="" width="807" height="970"><span>Arcturus Labs</span></a>
  <nav aria-label="Main navigation"><a href="https://arcturus-labs.com/blog/">Blog</a><a class="nav-call" href="https://calendly.com/jfberryman/15min" target="_blank" rel="noopener">Book a call <span aria-hidden="true">↗</span></a></nav>
</header>
<main>
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-copy"><p class="eyebrow">{cfg["eyebrow"]}</p><h1 id="hero-title">{cfg["h1"]}<span class="hero-turn">{cfg["turn"]}</span></h1><p class="hero-sub">{cfg["sub"]}</p></div>
    <div class="scroll-cue-fade"><div class="scroll-cue" aria-hidden="true">Scroll to explore<span aria-hidden="true">↓</span></div></div>
  </section>
'''
    story = '''
  <section class="story {cls}" id="{cls}" aria-labelledby="{cls}-title" data-story>
    <div class="story-stage">
      <div class="story-outline">
        <p class="eyebrow" id="{cls}-title">The {cls}</p>
        <ol>
{outline}
        </ol>
      </div>
      <div class="moments">
{moments}
      </div>
    </div>
  </section>
'''
    transition = f'''
  <section class="turning-point" aria-labelledby="turn-title"><div class="turn-stage"><div class="hero-copy"><h2 id="turn-title">{cfg["bridge_a"]}<span class="hero-turn">{cfg["bridge_b"]}</span></h2></div></div></section>
'''
    html = head
    html += story.format(cls='problem', outline=_outline(cfg['problems']), moments=_moments(cfg['problems'], first_page=True))
    html += transition
    html += story.format(cls='solution', outline=_outline(cfg['solutions']), moments=_moments(cfg['solutions']))
    html += '\n' + _tail(cfg.get('testimonial_order'))
    if cfg.get('stylesheet'):
        html = html.replace('<link rel="stylesheet" href="styles.css">', '<link rel="stylesheet" href="styles.css">\n  <link rel="stylesheet" href="' + cfg['stylesheet'] + '">', 1)
    if cfg.get('solution_label'):
        html = html.replace('id="solution-title">The solution', 'id="solution-title">' + cfg['solution_label'], 1)
    from page_chrome import apply_story_chrome
    (DRAFT / cfg['file']).write_text(apply_story_chrome(html))
    return DRAFT / cfg['file']
