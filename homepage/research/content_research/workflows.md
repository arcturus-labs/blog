# Business workflows: evidence for pains and competing solutions

Research recorded 2026-11-01 for `../draft_site_4/workflows.html`. Not approved copy; the page's visible text lives in `../draft_site_4/workflows-copy.md`.

## John's model (from the vault)

Sources read: `Arcturus Core Competencies` (Business workflows and the virtuous cycle), `The Virtuous Cycle – Building AI Workflows You Can Trust`, `English is the Programming Language of AI Software`, and the `Building the Future of AI Products` workshop description. His view:

1. Find research, analysis and review work with high toil and checkable output.
2. Interview the expert to capture their mental flow: steps, branches, exceptions, escalation.
3. Implement with an agent, tools, and a plain-English skill the expert can read and fix. No state machine or DAG.
4. Start with expert review: the agent produces work artifacts; experts approve, reject or repair them, with sources, intermediate results and open questions visible.
5. Capture corrections as evaluation cases; improve skills, tools and models; rerun the dataset after every change.
6. Classify tasks by demonstrated reliability: automatic, needs review, not yet. Autonomy is earned per task.

Those are hypotheses about what works, grounded in his practice and client work. His notes also record a learning gap in current evaluation and observability practice: refresh evaluation fundamentals, catch up on tooling, and build the full improvement loop.

## Evidence for the pains

### A. Experts spend a large share of time gathering information

**Source:** [McKinsey Global Institute, *The economic potential of generative AI*](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier). Extract reviewed in search results; the full page timed out when fetched.

- The report recalls MGI's **2012** estimate that knowledge workers spend about **a fifth of their time, roughly a day a week, searching for and gathering information**.
- That is a 2012 estimate, and it concerns information gathering in general, not review of AI output or any one business.

Use: supports the "experts' time goes to work AI could start" pain. Label it as an estimate and give its year. Do not present it as the owner's client data.

### B. Generic AI pilots stall because they do not learn the business

**Source:** [Fortune summary of MIT NANDA, *The GenAI Divide: State of AI in Business 2025*](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/). Full Fortune article retrieved. The underlying PDF timed out, so only Fortune's reading of it was verified.

- Study basis: **150 leader interviews, a survey of 350 employees, and analysis of 300 public deployments**.
- About **95%** of the pilots in the dataset showed **no measurable P&L impact**; about 5% achieved rapid revenue acceleration.
- The lead author attributes the gap to a **"learning gap"**: generic tools do not learn from or adapt to workflows, rather than model quality.
- The same article says purchased specialist tools and partnerships succeeded about 67% of the time, versus about a third as often for internal builds. Back-office automation showed the strongest ROI, while over half of budgets went to sales and marketing.

Caveats: the 95% figure has been widely repeated and disputed, comes from a non-peer-reviewed report, covers pilots chosen for the study, and measures revenue and P&L impact over a short window. Quote it only as MIT NANDA's finding, with the Fortune summary as the source. The success-rate contrast favours buying over building and is **not** support for any Arcturus offer; avoid it in copy.

### C. Unchecked AI output moves work onto colleagues

**Source:** [BetterUp Labs and Stanford Social Media Lab, *Workslop*](https://www.betterup.com/workslop). Page retrieved.

- Online survey of **1,150 full-time US desk workers**, September 2025.
- **40%** received "workslop" (AI-generated content that looks good but lacks substance) in the last month.
- It took about **two hours** on average to resolve each incident, which BetterUp prices at about **$186 per employee per month**, or **$9M a year for a 10,000-person company**.

Caveats: self-reported survey; the dollar figure is BetterUp's modeling assumption, not a measured cost; "workslop" concerns colleague-to-colleague output, which is related to but not the same as an expert reviewing an agent's artifact. Use only the 40% and two-hour findings, attributed.

## Evidence for the solution mechanics

### D. Plain-English skills are a recognized, open format

**Source:** [Agent Skills overview](https://agentskills.io/home): "a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows … a folder containing a SKILL.md file." Also [Anthropic's engineering post](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills). Search extracts only.

This supports the *mechanism* (an expert-readable file as the process), not the claim that experts will find it easy to maintain or that it outperforms code. That claim is John's hypothesis, based on his client work.

### E. Expert review of real outputs is standard practice in evaluation

**Source:** [Husain and Shankar, *AI Evals: Everything You Need to Know*](https://hamel.dev/blog/posts/evals-faq/). Full page retrieved and searched.

- Start with error analysis, not infrastructure: manually review **20–50 outputs** whenever there is a significant change.
- For most small and mid-sized companies, name **one domain expert** as the quality decision-maker (the "benevolent dictator").
- Surface intermediate outputs users can check, and give experts custom annotation tools. Judge outcomes, not technical steps ("Has an appointment been made?").

Strong alignment with John's "expert approves, rejects or repairs" and "expose sources and decisions". These are practitioner recommendations, not controlled studies.

### F. Use the simplest pattern that works, and verify

**Source:** [Anthropic, *Building effective agents*](https://www.anthropic.com/engineering/building-effective-agents). Extract only. Guidance: workflows give predictability for well-defined tasks; agents suit cases that need model-driven flexibility; use the simplest pattern that passes evaluation.

Overlap: John's "plain-English skill rather than bespoke orchestration". Difference: Anthropic also recommends hardcoded workflows when the path is known.

## What others reach for, and how it differs

| Approach | What it is | Overlap with John | Difference / tradeoff |
| --- | --- | --- | --- |
| Deterministic automation (RPA, Zapier, n8n-style) | Fixed steps and triggers | Auditable; good for high-volume, low-ambiguity tasks | Brittle for judgment and exceptions; secondary sources say agents earn their cost where judgment and exceptions matter |
| Bespoke agent graphs / DAGs / state machines | Model calls with coded routing | Same goal of controlled steps | Experts cannot read or fix the "code"; engineers become the bottleneck |
| Buy a specialist vendor tool | Packaged AI for a function | MIT found purchased solutions succeeded more often | Less fit to a company's own expert judgment; no capture of internal exceptions |
| Human-in-the-loop approval gates | Review before sensitive actions | Direct overlap with expert review | Often a gate on actions rather than a loop that converts corrections into tests |
| Eval and annotation platforms | Tools to label traces and score outputs | Same loop mechanics | Tooling is not the process; someone must capture expert judgment and decide when to automate |
| Generic chat assistants | Individuals prompt ChatGPT | Cheap, flexible | MIT: they do not learn from or adapt to workflows, so gains stay personal and unmeasured |

## How the pieces fit

- **Strong overlap:** the pain (expert time, stalled pilots, unchecked output), the review step, the evaluation loop, and the plain-English skill mechanism are all supported by independent practice.
- **John's differentiator:** connecting these end to end, starting at expert review, and treating autonomy as earned per task category. External sources support each part but not the combined method's results.
- **Not independently supported:** that experts can maintain skills themselves; that review saves time immediately; that autonomy can be safely extended using this loop. Present them as the approach, not as evidence.
- **Gaps John already notes:** evaluation fundamentals, observability tooling, and a connected improvement loop. Keep them out of capability claims.

## Copy guardrails

- No client metrics or fabricated numbers. Illustrative interfaces use no percentages or counts beyond the queue badge shown as a plain scenario detail.
- Cite 95%, 40% and the McKinsey estimate with the exact attributions above, linking the visible source text.
- Never say Arcturus delivered a specific time saving. Corey Griggs' testimonial already says the research agent identified substitutes "in a fraction of the time it would take staff", in his words.

## Next validation

Interview experts who review AI output about where time actually goes; test whether a domain expert can read and edit a skill unaided; fetch the MIT PDF and McKinsey page directly before launch to confirm wording.
