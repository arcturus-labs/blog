# Workflow success cases and virtuous-cycle evidence

Follow-up research, 2026-11-02. Discussion material, not approved website copy. Builds on [workflows.md](workflows.md). No website changes made. Goal: replace a failure-statistic-led pitch with credible examples of useful expert-guided workflows. Distinguish AI assistance, agentic deployments, customer reports and independent research.

## 1. Johnson Stokes & Master: expert-reviewed legal first drafts

Primary customer account published by Microsoft, June 2026. Full article retrieved:
https://news.microsoft.com/source/asia/features/from-legacy-to-ai-frontier-how-johnson-stokes-master-built-a-governance-first-copilot-model-for-regulated-legal-services/

The Employment Legal Advice Copilot Agent organizes matter context, identifies issues and prepares structured first-pass drafts covering risks, options and next steps. Lawyers review, refine and finalize before clients see advice. The initial application supports high-volume employment advisory work for Microsoft, with plans to replicate for other clients.

Reported outcomes for standard employment queries:
- 40–60% less time preparing first-pass advice.
- 25–35% less substantive rework during supervisory review.
- Average one to two hours saved per matter.

Exact quote, Joe Choy, Partner and Co-Head of Employment and Benefits:
> “The output provides a genuinely strong starting point, allowing our lawyers to spend more time on the strategic judgement and client counsel that matter most.”

Evidence: company-reported results in a vendor-published story. No sample size, comparison protocol or measurement window given in article. Not independently audited and not a general productivity guarantee. Explicit controls: no autonomous legal advice, no self-learning from client data, no bypassing professional review. Supports expert leverage and useful first drafts, NOT self-improving agents or autonomous professional accountability.

Initially suggested website candidate: attributed 40–60% first-draft preparation time reduction. Re-read in full during copy round 2: the smaller 25–35% finding measures substantive rework during supervisory review, not overall advice preparation time. No whole-process percentage is reported. Current draft instead states 25–35% less substantive rework and one to two hours saved per matter, with a visible Microsoft News link. Do not relabel the smaller figure as a percentage time saving for the entire matter.

## 2. Nubank: evaluation-driven customer-support agents

Primary technical paper, June 2026, full HTML retrieved:
https://arxiv.org/html/2606.08867
Title: Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework.

Five production deployments: card delivery, debt management, credit-limit support, card management and product explanation. Combines structured context, human-in-the-loop prompt iteration, LLM judges checked for agreement and optimized using GEPA, offline simulation and production experiments. Small progressive rollouts (1–5%) and escalation on out-of-routine cases are described.

Abstract reports the card-delivery A/B test achieved:
- +37 percentage points in AI transactional Net Promoter Score.
- +29 percentage points in self-service rate, relative to prior agent variants.

Evidence: authors' technical preprint describing their own production deployments, including A/B tests; not an independent replication or assumed peer-reviewed publication. These are percentage-POINT improvements, NOT percentages. The denominator is the evaluated card-delivery support experience, NOT all 100m+ customers; company customer count is context, not experiment sample size. The abstract and rollout methodology were reviewed; detailed sample sizes, tables and variant comparators still need closer extraction before website use.

Supports the virtuous cycle more directly than generic productivity research: expert feedback → structured evaluation → iteration → online validation. Does not establish that plain-English skills alone cause the gains, or that all task types should become autonomous. Strong research/process example; public metric pending deeper table review.

## 3. Morgan Stanley: SMEs and repeatable regression tests

First-person interview with Kaitlin Elliott, Executive Director leading Firmwide Generative AI Solutions; full transcript retrieved:
https://scale.com/blog/hitl-ep13-ai-evals-in-practice

They first asked subject-matter experts and end users to try the system because technically plausible answers were not enough. The team created a regression suite of 500 questions, reran it on changes, and developed an error taxonomy. Uses both human and AI-assisted annotation.

Exact short quote, Kaitlin Elliott:
> “The answer looked good to me, but I wasn't a financial advisor, so I didn't actually know if it was useful.”

Another exact excerpt:
> “What we started to do was create a regression suite of testing, where we picked 500 questions and used that as a base. We leveraged that every time we wanted to make a change to our solutions.”

Evidence: practitioner interview hosted by evaluation vendor Scale. Firsthand process account, not controlled outcome research. Core example is a knowledge-management assistant, not proof of an autonomous multistep agent workflow. Strong support for capturing expert quality judgments and testing changes.

OpenAI customer story https://openai.com/index/morgan-stanley/ returned 403. Search extracts report over 98% advisor-team adoption and evaluation datasets for Debrief. Do not use those as fully fetched/verified metrics. Morgan Stanley's Debrief press-release fetch also failed. Avoid quoting unsupported 30-minute meeting savings from secondary summaries here.

## 4. Generative AI at Work: stronger independent productivity evidence

Published in Quarterly Journal of Economics (2025). Current publication summary retrieved:
https://www.gsb.stanford.edu/faculty-research/publications/generative-ai-work
Paper DOI: https://doi.org/10.1093/qje/qjae044
Current abstract: https://arxiv.org/abs/2304.11771

Study of staggered AI-assistant introduction among 5,172 customer-support agents; 15% average improvement in issues resolved per hour, with heterogeneous effects, larger gains among less-experienced/lower-skill workers. Suggestive evidence of diffusion of stronger workers' practices.

Important version distinction: https://www.nber.org/papers/w31161 still displays the older 2023 working-paper abstract with 5,179 workers and 14% average gain. Do not mix sample sizes or metrics across versions. Use 15% with 5,172 and the published-version source.

Evidence: independent academic study of real workplace rollout, published; NOT a randomized trial merely because rollout is staggered. Measures AI assistance, not autonomous agentic workflows. Skilled workers benefited less, so this supports spreading expertise rather than claiming experts themselves save 15% of their time.

## 5. Production-agent survey: bounded systems are normal

Full preprint HTML retrieved:
https://arxiv.org/html/2512.04123v1
Title: Measuring Agents in Production.

Survey of 306 practitioners, 20 in-depth case studies across 26 domains. Abstract reports 68% of agents execute at most ten steps before requiring human intervention; 74% depend primarily on human evaluation; reliability remains the top development challenge.

Evidence: sampled practitioner survey/interviews, not representative census, causal trial or ROI proof. Helpful counterweight to fully autonomous-agent hype. Shows expert guidance is compatible with actual production practice. Use exact sample framing if cited.

## Story implications (proposals, not approved copy)

Pain need not map one-to-one to solution. Candidate pain facets:
1. Routine preparation consumes expert capacity.
2. A generic assistant does not know what good means for this business.
3. Output that needs redoing is not useful automation.

Solution: introduce John's virtuous cycle as a connected process:
1. Capture expertise in a reviewable process and examples.
2. Let AI produce a sourced, inspectable first pass; experts review.
3. Turn corrections into explicit improvements and regression cases; repeat.
4. Extend automation only where performance has been demonstrated; retain expert review elsewhere.

No claim of automatic online learning, guaranteed savings or inevitable autonomy. Human corrections do not magically update a model: the team updates instructions/tools/examples and verifies them. Error analysis and measured iteration are the through-line.

Owner's gold-headline candidate: “Capture their expertise in reliable workflows.” Not approved. Strength: names expertise and reliability. Weakness: describes the mechanism more than the relief; evidence supports expert leverage and reliable first passes, not a reliability guarantee for every workflow. Alternatives to discuss, not implement: “Turn their expertise into dependable workflows”; “Scale their expertise, not their workload.”

Best research-led framing: successful organizations use AI to do more preparation while experts retain quality judgment; explicit review and evaluation make improvement deliberate. Avoid equating all cited tools with autonomous agents or presenting individual gains as universal.
