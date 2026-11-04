"""Build homepage/index.html (the homepage) and its assets.

Reuses the maintained proof, contact and footer template so the
homepage stays consistent with the story pages, then applies homepage-only changes.
Does not modify any shared file. Run: python3 -I tools/build_home.py (needs Pillow, NumPy, SciPy).

EDIT THE LISTS BELOW to change the homepage's videos, posts and choices.
"""
import re
import sys
import json
from html import escape
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent))
import story_page as sp
from proof_component import compact_proof
from page_chrome import sky_script_url

DRAFT = sp.DRAFT
H = sp.SCENES / 'home-scenes'

# ---------------------------------------------------------------------------
# VIDEOS (carousel order = list order). To add one: append a dict, then put its
# 16:9 thumbnail at assets/<thumb>.jpg (or set "thumb_url" and the build downloads it).
# To remove or reorder: delete or move the dict. Captions are plain text; use &amp; for &.
# ---------------------------------------------------------------------------
# Owner-selected videos in a saved shuffled order; rebuilds do not reshuffle.
# Edit home-videos.json to reorder videos or update their publishing-channel metadata.
VIDEOS = json.loads((Path(__file__).parent / 'home-videos.json').read_text())

POSTS = [  # (iso date, label, title, url, one-line summary written for this page)
    ('2026-10-15', 'October 15, 2026', 'My Software Factory', 'https://arcturus-labs.com/blog/2026/10/15/my-software-factory/', 'How I’m building my own software factory, mistakes and all.'),
    ('2026-09-21', 'September 21, 2026', 'Will OpenAI Eat Jev’s Lunch?', 'https://arcturus-labs.com/blog/2026/09/21/will-openai-eat-jevs-lunch/', 'A fast new kind of model took off. What happens when the big labs notice?'),
    ('2026-09-16', 'September 16, 2026', 'TypeSafe’s Jev Trades Text Generation for Instant, Calibrated Decisions', 'https://arcturus-labs.com/blog/2026/09/16/typesafes-jev-trades-text-generation-for-instant-calibrated-decisions/', 'A model that answers questions with calibrated numbers almost instantly.'),
]

PICKS = [  # (art key, story page, statement, invitation, picture alt text)
    ('agentic', 'agentic-web.html', 'We’re losing our website traffic to chat.', 'Reclaim the user experience',
     'An awestruck woman in flowing garments and a confident office-assistant robot with a sensor-visor head reach toward an embrace while conversing.'),
    ('workflows', 'workflows.html', 'Our expert staff is toiling away on tasks that should be automated.', 'Build dependable automation',
     'An expert with arms raised in despair amid towering stacks of paperwork, marked by a brilliant central star.'),
    ('factories', 'software-factories.html', 'Competitors ship at the speed of AI. We’re stuck in the stone age.', 'Build a software factory you can trust',
     'A craftsperson laboriously carving a stone wheel using a hammer and chisel.'),
]

# ---------------------------------------------------------------------------
def export_constellation(scene, prefix):
    """Resize the existing variable-alpha art without chroma keying it again."""
    size = sp.cached_scene(DRAFT / 'assets', prefix)
    if size:
        return size
    source = sp.SCENES / 'constellation-experiments' / scene / 'transparent.png'
    image = Image.open(source).convert('RGBA')
    image = image.crop(image.getbbox())
    size = image.size
    for width in (960, 1536):
        resized = image.copy()
        resized.thumbnail((width, 1400))
        resized.save(DRAFT / 'assets' / f'{prefix}-{width}.webp', quality=92, method=6)
        if width == 1536:
            size = resized.size
    return size

picks_art = {
    'agentic': export_constellation('choice-customer-robot-v5', 'home-agentic'),
    'workflows': export_constellation('choice-expert', 'home-workflows'),
    'factories': export_constellation('choice-stone-wheel', 'home-factories'),
}

cards = []
for v in VIDEOS:
    asset = DRAFT / 'assets' / f'{v["thumb"]}.jpg'
    if not asset.exists():
        import urllib.request
        tmp = asset.with_suffix('.src')
        urllib.request.urlretrieve(v['thumb_url'], tmp)
        im = Image.open(tmp).convert('RGB')
        w, h = im.size
        target = round(w * 9 / 16); top = (h - target) // 2
        im = im.crop((0, top, w, top + target)); im.thumbnail((960, 540)); im.save(asset, quality=86); tmp.unlink()
    w, h = Image.open(asset).size
    cards.append(f'<a class="talk" draggable="false" href="{v["url"]}"><img class="talk-thumbnail" src="assets/{v["thumb"]}.jpg" alt="" width="{w}" height="{h}" loading="lazy"><span class="cap">{escape(v["caption"]).replace("—", " – ")}</span><span class="talk-channel"><img class="channel-icon" src="assets/{v["channel_icon"]}" alt="" width="32" height="32" loading="lazy"><span>{escape(v["channel"])}</span></span></a>')

post_rows = '\n'.join(
    f'        <li><a href="{url}"><time datetime="{iso}">{label}</time><span><strong>{title}</strong><span class="blurb">{blurb}</span></span></a></li>'
    for iso, label, title, url, blurb in POSTS)

pick_items = []
for key, href, text, action, alt in PICKS:
    w, h = picks_art[key]
    pick_items.append(f'''        <li class="pick"><a href="{href}">
          <div class="pick-media">
            <img class="shot" width="{w}" height="{h}" srcset="assets/home-{key}-960.webp 960w, assets/home-{key}-1536.webp 1536w" sizes="(max-width: 900px) 90vw, 30vw" src="assets/home-{key}-1536.webp" alt="{alt}" loading="lazy"></div>
          <p class="pick-text">{text}</p>
          <span class="pick-action">{action} <span aria-hidden="true">→</span></span>
        </a></li>''')

tail = sp.shared_tail()
split = tail.index('  <section class="contact')
proof, closing = tail[:split], tail[split:]
closing = closing.replace('../draft_site/index.html', 'index.html')

proof = compact_proof(proof)

# --- footer: add YouTube between Blog and LinkedIn ---
assert '<a href="https://www.linkedin.com/in/john-berryman-864b1713/">LinkedIn</a>' in closing
closing = closing.replace('<a href="https://www.linkedin.com/in/john-berryman-864b1713/">LinkedIn</a>',
    '<a href="https://www.youtube.com/@Arcturus-Labs">YouTube</a><a href="https://www.linkedin.com/in/john-berryman-864b1713/">LinkedIn</a>', 1)

html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Arcturus Labs helps teams build AI products and workflows: agentic experiences, dependable expert automation, and software factories. Strategy, training, and hands-on engineering.">
  <title>Building the future of AI products and workflows | Arcturus Labs</title>
  <link rel="icon" href="assets/favicon.ico">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="home.css">
  <link rel="stylesheet" href="compact-proof.css">
  <script src="home.js" defer></script>
  <script src="{sky_script_url()}" defer></script>
  <script src="subscribe.js" defer></script>
</head>
<body class="home">
<canvas id="sky" aria-hidden="true"></canvas>
<a class="skip" href="#reason">Skip to the choices</a>
<header class="opening-nav">
  <a class="brand" href="index.html"><img src="assets/logo.png" alt="" width="807" height="970"><span>Arcturus Labs</span></a>
  <nav aria-label="Main navigation"><a href="https://arcturus-labs.com/blog/">Blog</a><a class="nav-call" href="#contact">Book a call <span aria-hidden="true">↗</span></a></nav>
</header>
<a class="book-tab" href="https://calendly.com/jfberryman/15min" target="_blank" rel="noopener">Book a call<span class="sr-only"> (opens in a new tab)</span></a>
<main>
  <section class="hero" aria-labelledby="hero-title">
    <div class="hero-copy"><p class="eyebrow">Arcturus Labs</p><h1 id="hero-title">Building the future<br>of AI products<br><span style="color: var(--gold)">and workflows</span></h1><p class="hero-sub">Strategy, training, and hands-on engineering<br>for teams building with AI agents.</p></div>
    <div class="scroll-cue-fade"><div class="scroll-cue" aria-hidden="true">Scroll to explore<span aria-hidden="true">↓</span></div></div>
  </section>

  <section class="reason-scene" id="reason" aria-labelledby="reason-title">
    <div class="reason-stage">
      <h2 class="reason-title" id="reason-title">You’re here for a reason.</h2>
      <ul class="picks">
{chr(10).join(pick_items)}
      </ul>
    </div>
  </section>

  <section class="glance" aria-labelledby="glance-title">
    <div class="glance-stage content-wrap">
    <h2 class="glance-title" id="glance-title">Just looking around?<span class="hero-turn">See what Arcturus Labs is building</span></h2>
    <ul class="posts">
{post_rows}
    </ul>
    <a class="all-posts" href="https://arcturus-labs.com/blog/">All posts →</a>
    </div>
  </section>

{proof}
  <section class="videos" aria-labelledby="videos-title">
    <div class="videos-heading"><h2 id="videos-title">Talks, workshops, and conversations with John Berryman.</h2></div>
    <div class="talks-strip" tabindex="0" role="region" aria-label="Talks and videos. Scrolls sideways.">
      <div class="talks-track">
        {chr(10).join(cards)}
      </div>
    </div>
  </section>

{closing}'''
(DRAFT / 'index.html').write_text(html)
print(DRAFT / 'index.html')
