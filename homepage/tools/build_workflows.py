"""Build the workflow story from maintained copy and selected constellation art.
Run: python3 -I tools/build_workflows.py. Originals are never overwritten.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import story_page as sp
from constellation_assets import export

S = sp.SCENES / 'workflow-constellations'
assets = sp.DRAFT / 'assets'
names = {
    'p1': (sp.SCENES / 'constellation-experiments/choice-expert/transparent.png', 'wf-constellation-toil', True),
    'p2': (S / 'problem-2-compare-v2/image-01.png', 'wf-constellation-compare', False),
    'p3': (S / 'problem-3-stairs-v4/image-01.png', 'wf-constellation-advance', False),
    's1': (S / 'solution-1-fruit/image-01.png', 'wf-constellation-fruit', False),
    's2': (S / 'solution-2-handoff-v6/image-01.png', 'wf-constellation-handoff', False),
    's3': (S / 'solution-3-promote-v4/image-01.png', 'wf-constellation-promote', False),
    's4': (S / 'solution-4-stair-handoff-v4/image-01.png', 'wf-constellation-improve', False),
}
sizes = {key: export(image, assets, prefix, transparent) for key, (image, prefix, transparent) in names.items()}

SLACK = 'https://slack.com/blog/news/new-slack-research-shows-accelerating-ai-use-at-work'
ASANA = 'https://investors.asana.com/news-releases/news-release-details/asana-anatomy-work-global-index-2023-smart-collaboration-and'
MCKINSEY = 'https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier'
MORGAN = 'https://scale.com/blog/hitl-ep13-ai-evals-in-practice'


def moment(id, step, heading, art, alt, copy, overlay=False):
    result = dict(id=id, step=step, heading=heading, prefix=names[art][1], size=sizes[art], alt=alt, copy=copy)
    if overlay:
        result['class_name'] = 'quote-overlay'
    return result


def source(url, label):
    return f'<p class="source-context"><a href="{url}">{label}</a></p>'


P1 = 'Your experts are wasting time on routine tasks.'
P2 = 'How can you trust an AI workflow to produce good work?'
P3 = 'How do you build dependable workflows in a world of fast-paced change?'
S2 = 'Augment your expert staff.'
TOIL_ALT = 'An expert with arms raised in despair among towering stacks of paperwork; a brilliant central star represents their expertise.'
HANDOFF_ALT = 'A short, adult-proportioned office robot reaches up to hand paperwork to a taller human, who looks down toward its sensor visor.'
problems = [
    moment('p1', 0, P1, 'p1', TOIL_ALT,
           '<p class="evidence-number">41% <span>of the working day</span></p><p>Desk workers in Slack’s survey said that 41% of their working day went to tasks that were “low value, repetitive or lack meaningful contribution to their core job functions.”</p>' + source(SLACK, 'Slack Workforce Lab · 10,281 desk workers · January 2024'), True),
    moment('p1-processes', 0, P1, 'p1', TOIL_ALT,
           '<p class="evidence-number">4.9 hours <span>per week.</span></p><p>Knowledge workers estimated better processes could save them 4.9 hours per week. Asana’s survey found <span class="gold">58% of time went to “work about work.”</span></p>' + source(ASANA, 'Asana Anatomy of Work · 9,615 knowledge workers · 2023'), True),
    moment('p1-potential', 0, P1, 'p1', TOIL_ALT,
           '<p class="evidence-number">60–70% <span>of employee time</span></p><p>McKinsey estimated that generative AI and other technologies could automate activities occupying 60–70% of employees’ time.</p>' + source(MCKINSEY, 'McKinsey Global Institute · technical automation potential · 2023'), True),
    moment('p2', 1, P2, 'p2',
           'A tense professional seen from behind looks directly at paper B in his right hand, wearing a neatly tucked shirt and well-fitting trousers.',
           '<blockquote><p>“The answer looked good to me, but I wasn\'t a financial advisor, so I didn\'t actually know if it was useful.”</p><cite><a href="' + MORGAN + '">Kaitlin Elliott, Morgan Stanley · Human in the Loop interview</a></cite></blockquote>'),
    moment('p3', 2, P3, 'p3',
           'Three practical office-assistant robots with sensor-visor heads march up a staircase ascending toward the upper right.',
           '<p>Models, tools, and approaches change. <span class="gold">How do you keep your workflows up to date while assuring they remain dependable?</span></p>'),
]
solutions = [
    moment('s1', 0, 'Start with the most impactful tasks.', 's1',
           'A fruit tree with clearly visible low-hanging fruit on its lower branches.',
           '<p>Look for valuable, repeatable tasks with outcomes your experts can check. Watch how employees already use AI, then <span class="gold">capture the most promising processes as agent skills.</span></p>'),
    moment('s2', 1, S2, 's2', HANDOFF_ALT,
           '<p>Let agents perform research, make the easy decisions, and prepare drafts. <span class="gold">Give experts the sources, findings, and open questions they need to review the work instead of doing it all from scratch.</span></p>'),
    moment('s3', 2, 'Promote what proves reliable.', 's3',
           'A relaxed, confident human expert reviews a document on the left while a practical office-assistant robot handles business work at a desk on the right.',
           '<p>Capture expert corrections, classify and catalogue tasks, and <span class="gold">fully automate tasks that are determined to be low-risk and highly dependable.</span></p>'),
    moment('s4', 3, 'Maintain and continuously improve workflows.', 's4',
           'Office-assistant robots ascend a staircase; the robot on the lowest step hands paperwork to the one just above.',
           '<p>Extract evaluation benchmarks from your experts’ daily work. When models, tools, or approaches change, <span class="gold">rerun the benchmarks to ensure workflow quality stays on track.</span></p>'),
]

if __name__ == '__main__':
    print(sp.build(dict(
        file='workflows.html', title='Are your experts buried in work?',
        description='Turn your experts’ processes into AI-assisted workflows. Graduate dependable tasks to full automation. Iterate and continuously improve.',
        eyebrow='Business workflows', h1='Are your experts<br>buried in work?',
        turn='Scale their expertise,<br>not their workload.',
        sub='Turn your experts’ processes into AI-assisted workflows.<br>Graduate dependable tasks to full automation. Iterate and continuously improve.',
        bridge_a='Augment your experts on day one.<br>Keep humans in charge.', bridge_b='Automate tasks dependably.',
        stylesheet='workflows.css', solution_label='The solution',
        problems=problems, solutions=solutions,
        testimonial_order=['Corey Griggs', 'Laura Murray', 'Shantanu Dhaka', 'Arin Sime'],
    )))
