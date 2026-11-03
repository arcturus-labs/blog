"""Build Agentic Web with preserved story copy and the approved compact proof.

Story source: templates/agentic-web.html. Shared tail: templates/story-tail.html.
Proof layout: proof_component.py and compact-proof.css. Generated HTML is never input.
Run: python3 -I tools/build_agentic_web.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import story_page as sp
from proof_component import compact_proof
from page_chrome import apply_story_chrome


def build():
    template = Path(__file__).parent / 'templates' / 'agentic-web.html'
    source = template.read_text()
    tail = sp.shared_tail()
    split = tail.index('  <section class="contact')
    tail = compact_proof(tail[:split]) + tail[split:]
    assert source.count('{{ shared_tail }}') == 1
    html = source.replace('{{ shared_tail }}\n', tail)
    html = html.replace('<link rel="stylesheet" href="styles.css">', '<link rel="stylesheet" href="styles.css">\n  <link rel="stylesheet" href="compact-proof.css">', 1)
    destination = sp.DRAFT / 'agentic-web.html'
    destination.write_text(apply_story_chrome(html))
    return destination


if __name__ == '__main__':
    print(build())
