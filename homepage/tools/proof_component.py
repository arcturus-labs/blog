"""Approved compact proof markup, shared by homepage and Agentic Web builders."""
import re

CAPTIONS = {
    'Shantanu Dhaka': 'Chief Product Officer, Perch Insights',
    'Laura Murray': 'Founder, CETA Global; Head of Global Mental Health at Google',
    'Corey Griggs': 'Chief Technology Officer, Peer Supply',
    'Arin Sime': 'CEO/Founder at AgilityFeat',
}

def compact_proof(proof):
    def caption(match):
        name = re.search(r'<strong>(.*?)</strong>', match.group(0)).group(1)
        return f'<figcaption><strong>{name}</strong>, <span>{CAPTIONS[name]}</span></figcaption>'
    proof, count = re.subn(r'<figcaption>.*?</figcaption>', caption, proof, flags=re.S)
    assert count == 4, count
    author = re.search(r'\s*<p class="authorship">.*?</p>', proof, re.S)
    author_html = author.group(0).strip()
    proof = proof.replace(author.group(0), '')
    anchor = 'alt="Prompt Engineering for LLMs, coauthored by John Berryman" width="762" height="1000" loading="lazy"></a>'
    assert anchor in proof
    proof = proof.replace(anchor, anchor + '\n      ' + author_html, 1)
    return proof
