# Editing Notes — Tim Kellogg

Tim is a principal AI architect at a law tech company, former Amazon/AWS IoT, GitHub-adjacent background. He writes at timkellogg.me and a Substack (linked from his site).

---

## Summary

- **Intros** — John frames the podcast around AI-driven software development lifecycle; Tim's background in ML/AI since 2018, startups, law tech.
- **Shared Nothing Engineering** — treating a software team like a distributed system; keep things small; scale horizontally by partitioning work.
- **Mythical Man Month tangent** — N-squared communication cost, same applies to software complexity; argument for staying small.
- **Can't Sell an Agent** — dropping in Claude Code doesn't work; real value requires transforming workflows; companies hit ~10% of potential; everyone has to participate.
- **SaaS disruption** — IT shops building their own software is already accelerating; internal teams becoming the primary competitor to mid-tier SaaS vendors.
- **End-to-end vertical teams** — why stop at engineering? Agents could extend across QA, DevOps, sales, marketing; specialists become "vertical generalists."
- **Workflow engineer role** — new job title: someone with both domain expertise and AI/systems thinking.
- **OpenStrix intro** — Tim's open-source stateful agent harness; event-driven, minimal LLM invocation, runs parallel jobs.
- **Agent memory philosophy** — keep context small and always-on rather than waiting for rare compaction events; plain-text files are inspectable; continual learning in weights is opaque.
- **Memory architecture deep-dive** — memory blocks (learnable system prompt), files (nested directories), skills; sliding window vs. accumulating context.
- **Calls to action / wrap** — timkellogg.me, Bluesky, Substack.
- **Post-recording chat** — consulting ambitions, Lily (marketing ops co-conspirator), social platform banter.

---

## Key Points

### Software Teams as Distributed Systems
- Engineers used to think of themselves as coders; now they're building systems that build software.
- VPs of engineering already get this; individual engineers often feel burned out by the shift.
- Treating a codebase like a distributed system: partition change requests the way a database partitions traffic → horizontal scaling.
- Software complexity grows N-squared (Mythical Man Month); keeping things small is the single best lever.

### Can't Sell an Agent
- Dropping a generic agent into a company doesn't transform it — it's just a new tool people have to learn.
- Real transformation = rewiring workflows to take advantage of AI; that requires whole-company participation.
- SaaS vendors bolt on agents as a new SKU; that fits their business model but doesn't change customer workflows.
- Better SaaS strategy: make your product extremely accessible via API/skills so *any* agent can use it, rather than bundling your own agent.

### SaaS Disruption
- IT shops building bespoke internal software is already visibly accelerating (Tim has private data; public reports exist).
- Pattern: 1–2 top SaaS players in each category still growing; mid/lower players shrinking; "build it yourself" category accelerating.
- The Venn diagram that matters: people who know the domain deeply *and* know AI — they can build exactly what's needed, not a general solution.
- Future internet: "internet for machines only" — your agent is the UI, SaaS survives by being agent-addressable.

### End-to-End Vertical Teams
- If agents are general-purpose, why stop at engineering? A single vertical slice could span product → engineering → QA → DevOps → sales → marketing.
- Org structure shift: horizontal specialists (domain experts) sit on a meta team building the agent framework; vertical teams own their slice end-to-end.
- "Workflow engineer" — new role that combines domain expertise with systems/agent thinking.

### OpenStrix
- Minimal, stateful agent harness (think: Claude Code / OpenHands, but bare-bones).
- Event-driven: polling scripts emit JSONL events; LLM is only invoked when something real happens.
- Runs multiple parallel jobs (tests, coding agents, etc.) simultaneously.
- The agent teaches itself — constantly brainstorming ways to improve its own harness/skills.
- Uses Playwright to scrape sites without open APIs (e.g., LinkedIn).

### Agent Memory Philosophy
- **Core insight:** what you remember shapes everything that follows — compaction at 1M tokens is a big, risky, infrequent event; it's better to keep context perpetually small.
- Infrequent events don't get tested well; small context means memory hygiene is always exercised.
- Anthropomorphize the agent: "AI intern with anterograde amnesia" — it has to write things down or it forgets.
- **Plain text wins:** files and memory blocks are inspectable; you can git-blame the agent's memory. Continual learning in weights is opaque and undebuggable.
- Memory blocks = learnable system prompt (key-value chunks always prepended); files = nested markdown directories for data/context; skills = hybrid.
- Context rebuilding (sliding window, ~10–15K tokens/message) vs. accumulating context (avg ~500K tokens/message at 1M max) — cost math often favors rebuilding.

### Cold-Open Fodder
- `[00:04:30]` *"We are now building systems that build software."*
- `[00:12:31]` *"You can't just simply drop in Claude Code and make it work."*
- `[00:27:12]` *"Internal IT shops are the primary competitor now."*
- `[00:35:33]` *"It's like the agent has anterograde amnesia — it's constantly making tattoos on itself."*
- `[00:31:16]` *"What you end up remembering matters a lot, because it carries forward."*

## Opening
- Today I'm meeting with AI Architect Tim Kellogg
- Lot of ground to cover
  - Shared-nothing architecture: the infrastructure principle of partitioning into independent groups — no shared state, more scale. The same idea applies to AI-driven software development. Instead of a monolith, keep modules small and independent so changes don't constantly collide.
  - A generic agent alone gets you maybe 10% of the value. The other 90% is your company's specific workflows and domain knowledge — and that has to be encoded intentionally. Just dropping in an agent isn't enough.
  - Tim builds his own stateful agent, OpenStrix, and has a contrarian take on memory: instead of growing a giant context and then catastrophically compacting it, keep a small sliding window always. He explains why that's actually safer and cheaper.
- Let's dive in.

## Teleprompter

Today I'm sitting down with Principal AI architect Tim Kellogg at Icertis, a Contract management software company. — and we've got a lot of ground to cover.

We're going to talk about shared-nothing architecture. It's an infrastructure principle from the 2010s where you partition your system into independent groups that share no state with each other — and the payoff is massive scale because you eliminate bottlenecks. Tim makes the case that the same thinking applies to AI-driven software development. Instead of one big monolith absorbing a flood of colliding AI commits, keep your modules small and independent so that the collisions rarely happen.

We're also going to talk about why dropping in a generic agent isn't enough. A lot of companies think that introducing something like Microsoft Copilot is going to transform the business — but a generic agent only gets you maybe 10% of the potential value. The other 90% comes from encoding your company's bespoke domain knowledge into the agent. Skip that step, and you're leaving most of the benefit on the table.

And finally, Tim builds his own stateful agent called OpenStrix, and he has a contrarian take on memory management. Instead of letting context grow indefinitely and then catastrophically compacting it, he keeps a small sliding window — always. He'll explain why that's actually the safer and cheaper approach.

Let's dive in.

## Title
The Missing 90%: Why Generic AI Agents Don't Transform Companies

## Links

**AI-SDLC**
- [Shared Nothing Engineering](https://timkellogg.me/blog/2026/04/25/hot-spots) — code is cheap and plentiful; how do you keep people from stepping on each other? Also covers fusing roles.
- [You Can't Sell an Agent](https://timkellogg1.substack.com/p/you-cant-sell-an-agent) — agents alone cover ~10% of the value (individual tasks); the other 90% is encoding company workflows and domain knowledge. Also: SaaS is dead, long live the consultant.

**AI Products**
- [OpenStrix](https://github.com/timkellogg/openstrix) *(verify URL)* — Tim's open-source stateful agent harness; event-driven memory, sliding context window.

---

## YouTube

**Title:** The Missing 90%: Why Generic AI Agents Don't Transform Companies

**Description:**

Most companies think deploying Microsoft Copilot or another off-the-shelf AI agent is going to transform their business. Tim Kellogg has seen enough to know that's only 10% of the story.

Tim is a principal AI architect at a law tech company who's spent years watching teams fail — and succeed — at AI adoption. In this conversation we dig into why shared-nothing architecture principles apply to AI-driven software teams, why a generic agent can't transform your company on its own, and how SaaS businesses need to rethink their model as internal IT shops become their biggest competitor.

We also get into Tim's open-source stateful agent, OpenStrix, and his contrarian take on agent memory: instead of growing a massive context window and catastrophically compacting it, keep a small sliding window always. The reasoning is more interesting than you'd expect.

Tim writes at timkellogg.me and his Substack (linked from his site).

Blog posts referenced:
- Shared Nothing Engineering: https://timkellogg.me/blog/2026/04/25/hot-spots
- You Can't Sell an Agent: https://timkellogg1.substack.com/p/you-cant-sell-an-agent

**Chapters** *(raw transcript timestamps — re-verify after editing):*

0:00  – Intro
1:28  – Tim's Background
2:30  – The AI-Driven SDLC Problem
3:31  – Shared Nothing Engineering
7:08  – Keep It Small
8:48  – One Agent End to End?
9:31  – Context Loss Between Teams
11:15 – Vertical Generalists vs. Horizontal Specialists
12:00 – Can't Sell an Agent
15:52 – OpenStrix: A Stateful Agent Harness
19:24 – SaaS and AI
23:56 – The Internet for Machines
26:12 – IT Shops as Your Biggest Competitor
29:05 – The Workflow Engineer
30:15 – Agent Memory Philosophy
31:16 – What You Remember Shapes Everything
35:15 – The Anterograde Amnesia Analogy
36:35 – Memory Blocks and File Architecture
38:15 – Sliding Window vs. Accumulating Context
39:52 – Calls to Action

---

## Lessons learned
- Must record on Descript - Zoom sucks
- Must have talking points if the conversation runs dry
  - Have AI summarize the main points from their recent blogs
- Must have a conversation beforehand and see if there's chemistry
- Must ask them to define things - get a list