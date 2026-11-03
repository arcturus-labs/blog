# Software factories: evidence for pains and competing solutions

Research recorded 2026-11-01 for `../draft_site_4/software-factories.html`. Not approved copy; the visible text lives in `../draft_site_4/software-factories-copy.md`.

## John's model (from the vault)

Sources read: `Arcturus Core Competencies` (Software factories), `The Software Factory – From Coding with Agents to Coordinating Them`, `Building the Future of AI Products` workshop description, the to-do `Software Factory with "Strong opinions lightly held"`, and notes on the Twin Sun "dark factory" conversation. His view:

1. Start with interactive experimentation; turn what works into explicit skills.
2. Establish product intent, architecture, constraints and code patterns **before** delegating.
3. Write inspectable processes with clear inputs, outputs and completion criteria; decompose work into tasks with explicit dependencies.
4. Isolate concurrent changes (worktrees); add orchestrators that prioritize unblocked work, coordinate workers and verify results.
5. Keep people responsible for product decisions, architectural tradeoffs and the evidence needed to accept work. At every level of delegation ask: what evidence lets us trust the result?
6. Adopt incrementally; "take what you need", fitted to the company and team.

**Boundaries to respect.** His own notes say experience centers on his *personal* software factory. Team-level operating model, CI/CD and QA for rapid change, independent verification and evolving a factory as a team are **learning gaps**. The copy therefore describes an approach and what to ask, not a track record of team deliveries.

## Evidence for the pains

### A. More code does not mean more shipped product

**Source:** [Faros AI, *The AI Productivity Paradox* (AI Engineering Report 2025)](https://www.faros.ai/ai-productivity-paradox). The page was fetched, but its body is mostly navigation. It confirms the sample (**telemetry and workflow data from about 10,000 developers across 1,255 enterprise engineering teams**) and "completing twice as many code changes, but company metrics remain flat." The specific figures below come from the page's own search-result summary, not the fetched body.

- Teams with high AI adoption merged about **98% more pull requests** while **review time rose about 91%**.
- A separate academic paper quotes the same Faros study with larger pull requests and more bugs; not independently checked here.

Caveats: vendor research (Faros sells engineering analytics); observational telemetry, not an experiment; "company metrics remain flat" is the vendor's wording. Use the 98% and 91% figures, attributed, with the sample size.

### B. AI amplifies the organization it lands in

**Source:** [DORA, *State of AI-assisted Software Development 2025*](https://dora.dev/dora-report-2025/). Page fetched. "The report reveals AI's primary role is as an **amplifier**, magnifying an organization's existing strengths and weaknesses. The greatest returns on AI investment come not from the tools themselves, but from a strategic focus on the underlying organizational system." Research basis per Google's announcement: 100+ hours of qualitative data and a survey of nearly 5,000 technology professionals (June–July 2025).

Strong match for shared intent, process and verification. A secondary summary also says AI raises throughput and instability, but that was not verified against the report.

### C. Perceived speed and measured speed can disagree

**Source:** [METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Full page read.

- Randomized trial: **16 experienced developers, 246 real issues** in repositories they knew well, AI allowed or disallowed at random.
- With AI allowed, issues took **19% longer**. Developers had expected a 24% speedup and, **afterward, still believed AI had sped them up by 20%**.

Caveats METR states itself: it does **not** show that AI fails to speed up most developers or that future tools won't; it covers early-2025 tools in mature open-source repositories. Use only to make the narrow point that confidence and measurement diverge, and name the tools' vintage. Do not write "AI slows developers down."

## What others reach for, and how it differs

| Approach | What it is | Overlap with John | Difference / tradeoff |
| --- | --- | --- | --- |
| Individual AI coding assistants | Autocomplete and chat in each developer's editor | Low barrier; where most teams start | No shared intent or process; the pain above shows up as review bottleneck |
| AI code-review tooling | Automated review of pull requests | Targets the review bottleneck directly | Reviews output against what? Without shared intent and acceptance criteria it can only check generic quality |
| Spec-driven development | Write detailed specs before agents implement | Same instinct: intent before delegation | John's blog notes it can break at scale; he emphasizes living product and architecture context, not one-off specs |
| Fully autonomous "dark factories" | Agents run the whole pipeline | Same ambition of repeatable agent-driven delivery | Twin Sun's approach was discussed on John's show; evidence of outcomes beyond the company's own account was not reviewed here |
| Platform and CI/CD investment | Stronger pipelines, tests and release safety | Directly supports verification | Necessary but not sufficient: it does not decide what to build or coordinate concurrent agents |
| Do nothing / ad hoc | Let each developer improvise | Zero cost today | DORA's amplifier finding suggests weak systems get weaker |

## How the pieces fit

- **Strong overlap:** all three pains (review bottleneck, amplification of weak systems, unreliable self-assessment of speed) support John's emphasis on shared intent, a repeatable process and evidence-based acceptance.
- **Not independently supported:** that his specific factory design (skills, worktrees, orchestrators) improves delivery results for a team. It is an approach with a personal track record, not a validated team outcome.
- **John's differentiator:** treating the factory as something grown incrementally with the team and carrying the same question ("what evidence lets us trust this?") through every layer of delegation.
- **Gaps already acknowledged:** team-scale coordination, CI/CD and QA for rapid change, independent verification (such as a holdout suite agents cannot edit), and cultural/technical evolution of the shared factory. Keep these out of capability claims.

## Copy guardrails

- Attribute Faros as vendor research; cite sample sizes; never imply causation or that a client's numbers look like these.
- Quote DORA's "amplifier" language accurately and link the report page.
- Present METR as one early-2025 study; do not generalize.
- No client results. The testimonials shown are the existing ones and concern other work; **do not imply that Peer Supply or CETA or Perch used a software factory.**
- Describe the approach as "start small, encode what works", consistent with John's notes, not as an off-the-shelf product.

## Next validation

Fetch the Faros report PDF and DORA full report for exact wording; interview teams about where review time goes; test whether shared intent files actually reduce conflicting agent changes in a team setting before claiming it.
