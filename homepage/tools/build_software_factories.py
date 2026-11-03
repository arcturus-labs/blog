"""Build homepage/software-factories.html (and its assets) from the shared template."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import story_page as sp

S = sp.SCENES / 'factory-scenes'
names = {
    'p1': ('problem-1-review-queue', 'sf-problem-1-review-queue'),
    'p2': ('problem-2-three-agents', 'sf-problem-2-three-agents'),
    'p3': ('problem-3-green-checks', 'sf-problem-3-green-checks'),
    's1': ('solution-1-intent', 'sf-solution-1-intent'),
    's2': ('solution-2-process', 'sf-solution-2-process'),
    's3': ('solution-3-evidence', 'sf-solution-3-evidence'),
}
sizes = {k: sp.export_scene(S / folder, prefix) for k, (folder, prefix) in names.items()}
pfx = lambda k: names[k][1]

FAROS = 'https://www.faros.ai/ai-productivity-paradox'
DORA = 'https://dora.dev/dora-report-2025/'
METR = 'https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/'

problems = [
    dict(id='p1', step=0, heading='Writing code got faster. Shipping didn’t.', prefix=pfx('p1'), size=sizes['p1'],
         alt='A pull-request list shows 63 open agent-written changes awaiting review by two reviewers. A red handwritten note reads: More code. Same two reviewers.',
         copy=f'<p>Faros AI studied 10,000 developers on 1,255 teams. Teams with high AI adoption merged <strong>98% more pull requests</strong>, <span class="gold">but review time rose 91%.</span></p><p class="source-context"><a href="{FAROS}">Faros AI, The AI Productivity Paradox, 2025 · vendor telemetry study</a></p>'),
    dict(id='p2', step=1, heading='AI amplifies whatever your process already is.', prefix=pfx('p2'), size=sizes['p2'],
         alt='Three coding agents work in parallel on one invoicing app, each assuming something different about billing, and a banner warns that three changes touch checkout. A red handwritten note reads: Three agents. Three different products.',
         copy=f'<p>DORA’s 2025 report describes AI as an <strong>amplifier</strong> of an organization’s existing strengths and weaknesses. <span class="gold">The returns come from the underlying system, not the tools.</span></p><p class="source-context"><a href="{DORA}">DORA, State of AI-assisted Software Development 2025</a></p>'),
    dict(id='p3', step=2, heading='Without evidence, you can’t tell fast from fragile.', prefix=pfx('p3'), size=sizes['p3'],
         alt='A pull request is ready to merge with unit tests, lint, and build passing, but Product QA not run and no reviewer assigned. A red handwritten note asks: Green checks. But does it work?',
         copy=f'<p>In a randomized trial of 16 experienced open-source developers, tasks took <strong>19% longer</strong> with AI tools. <span class="gold">Afterward, they still believed AI had made them 20% faster.</span></p><p class="source-context"><a href="{METR}">METR, 246 real tasks, early-2025 tools</a></p>'),
]
solutions = [
    dict(id='s1', step=0, heading='Give every agent the same product intent', prefix=pfx('s1'), size=sizes['s1'],
         alt='An editor shows a product folder with intent, architecture, constraints, and patterns files. The open intent file lists what customers should be able to do and notes that pricing and refunds need a person’s decision, owned by the product lead.',
         copy='<p>Write down the product goals, architecture, constraints, and code patterns before work is delegated. <span class="gold">People keep ownership of the product decisions and tradeoffs.</span></p>'),
    dict(id='s2', step=1, heading='Turn what works into a repeatable process', prefix=pfx('s2'), size=sizes['s2'],
         alt='A skill file feeds three isolated worktrees with different statuses, which report to an orchestrator that coordinates the workers, verifies, and merges.',
         copy='<p>Experiment first, then encode what works as skills: clear inputs, explicit dependencies, and defined completion criteria. <span class="gold">Isolate concurrent changes and let an orchestrator coordinate the workers.</span></p>'),
    dict(id='s3', step=2, heading='Build trust into the factory', prefix=pfx('s3'), size=sizes['s3'],
         alt='A merge checklist shows tests, code review, staging integration, product QA of the checkout flow, and rollback plan all complete. A red handwritten note reads: Evidence, not hope.',
         copy='<p>At every level of delegation, ask <span class="gold">what evidence lets you trust the result?</span> Meaningful tests, review, CI/CD, and product-level QA. Then grow the factory with your team, one step at a time.</p>'),
]

path = sp.build(dict(
    file='software-factories.html',
    title='Writing more code than you can ship?',
    description='Give coding agents shared intent, a repeatable process, and evidence you can trust, grown with your team one step at a time. Software factory strategy and engineering from Arcturus Labs.',
    eyebrow='Software factories',
    h1='Writing more code<br>than you can ship?',
    turn='Build a factory<br>you can trust',
    sub='Shared intent. Repeatable processes. Evidence you can trust.<br>Grown with your team, one step at a time.',
    bridge_a='Generating code<br>is the easy part',
    bridge_b='Build the process<br>around it',
    problems=problems, solutions=solutions,
    testimonial_order=['Laura Murray', 'Corey Griggs', 'Shantanu Dhaka', 'Arin Sime'],
))
print(path)
