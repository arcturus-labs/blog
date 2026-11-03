# Software factories – second draft

Second implemented draft for John's review. Based on the owner-directed copy review and workflow imagery references. This file is the maintained copy source read by `tools/build_software_factories.py`; rebuild to apply edits. The superseded first implementation is preserved locally in `IGNORED/software-factory-draft-1/`.

The three problem themes are approved; the wording below is proposed. Keep this page simpler than the other stories: three problems, one transition, three solutions. One supporting moment per problem; solution 2 has two short moments to distinguish guidance from verification. Graphic directions are proposals, not visible copy or generation instructions. `{gold: …}` marks proposed gold emphasis.

## Hero

Software factories

# Competitors are shipping<br>at the speed of AI
# Getting started is<br>easier than you think

Bring agents into your software development life cycle.<br>
Start with what you have. Increase autonomy as confidence grows.

## The problem

### 1. A faster way to build software is taking shape.

> “Within weeks, hundreds of engineers were shipping at a pace that would have seemed impossible a year ago.”

[Intercom · firsthand account of adopting agent-first engineering](https://ideas.fin.ai/p/we-gave-claude-code-to-everyone-at)

*Approved replacement for the entire right-hand paragraph. Quote stands alone with linked attribution. Self-reported experience, not an independently measured productivity result.*

*Graphic direction: a simple constellation scene matching the workflow page's blue, softly glowing robots, bright white stars, and connecting lines. Three robots face the viewer from behind a single assembly line, each adding a part to a widget at its station. Show the SAME recognizable widget at three unmistakably different stages from left to right: a bare chassis at the first station; the same chassis with a prominent new component at the second; that chassis retaining the component and gaining another prominent part at the third. Parts accumulate, rather than being swapped. Avoid three nearly identical closed boxes. Minimal props, no labels, no competing delivery line. Reuse the workflow robots' design and proportions.*

### 2. But an AI software factory is worthless if the process is not dependable.

Poor code design can turn early speed into a standstill as agents struggle with mounting complexity. {gold:When agents ignore the product invariants, inconsistent behavior erodes customer trust.}

*Graphic direction: one constellation robot stalled at an assembly station, looking down at a widget tangled in a few oversized, knotted cables. Two visibly mismatched widgets sit beside it. Simple silhouette and few props: the tangle suggests accumulated complexity; the mismatched outputs suggest inconsistent behavior. No code, labels, warning icons, or elaborate factory background.*

### 3. How do you build a process that stays relevant as technology changes?

Models, frameworks, and agent harnesses keep changing. {gold:Will your software factory be out of date as soon as you've put it in place?}

*Graphic direction: a constellation robot holds a large clean, well-made cogwheel beside a sleek electronic machine on a minimal workbench. The machine has a smooth sealed housing and a small electronic connector, with no exposed gears or place to fit the cog. The robot looks between them, unsure where the component could go. Mechanical versus electronic shapes communicate a good component whose surrounding technology has moved on. Same blue constellation style throughout; no rust, text, labels, cables or extra props. Selected render: `p3-gear-electronics/image-01.png`; the earlier plug/socket candidate is preserved.*

## Turn into the solution

# Start with hands-on collaboration
# Build toward hands-off automation

*One full-screen transition. First line white, second gold. No additional explanation on this slide. Rework and visually verify the layout with this longer wording; John flagged the previous rendered layout as wonky.*

## The solution

### 1. Develop the process together. Automate what proves reliable.

Break your software development lifecycle into tasks and work through them alongside an agent. Correct mistakes as they happen and refine the process together. {gold:As individual tasks prove dependable, promote them to more hands-off automation.}

*Graphic direction: a human and one constellation robot work side by side at a single assembly bench. The robot fits one part onto a widget while the human handles the neighboring task. Equal partners in an existing workspace, with minimal tools and no sprawling production line.*

### 2. Build to your standards. Verify the results.

**Moment 1 – Shared understanding**

Define your coding conventions, architecture, and product invariants. {gold:Clarify each task together before agents begin implementation.}

*Graphic direction: a human and a constellation robot lean over the same large blueprint on a table. The human points to a simple widget outline while the robot follows the gesture. One shared plan, no readable text, directory names, floating documents, or complex architecture diagram.*

**Moment 2 – Meaningful verification**

Build tests, review, and hands-on QA into your delivery process. {gold:Check the running software against agreed expectations – not the agent’s claim that it’s done.}

*Graphic direction: a human uses a simple physical gauge to check a finished widget while a constellation robot watches from across the bench. Reuse the widget from the assembly scenes. Show an actual measurement against a standard, not a thumbs-up, green check, or robot declaring its own work complete.*

### 3. Future-proof your software factory.

Stable patterns are emerging: plain-English skills, shared project context, and established build and delivery checks. {gold:Build around portable practices, so your software factory can adapt as technology changes.}

*Graphic direction: a human hands an open instruction manual across a workbench to a constellation robot; a second robot stands beside it, also looking at the same manual. Different recipients, one shared set of instructions. Use a few simple diagram marks rather than readable text. No vendor logos, orbiting tools, or migration arrows.*

## Proof, contact, and footer

Reuse the existing shared proof and conversion components from the other story pages, without inventing software-factory client outcomes or changing testimonial wording.

From possibility to product

## Arcturus Labs can help

Product direction. AI behavior. Agentic engineering.

*[Existing shared books, testimonials, and coauthorship line.]*

# Build what comes next

[Book a 15-minute call ↗](https://calendly.com/jfberryman/15min)

### Subscribe to the Arcturus Labs blog

*[Existing subscription form and shared footer.]*

## Editorial notes – not page copy

- Shared graphic style: match the workflow page's softly glowing blue constellation figures, white star points and connecting lines, robot design, and transparent background. Keep each scene readable at a glance, with one main action and minimal props. These are symbolic illustrations, not literal software-system diagrams.
- Artwork uses `gpt-image-2.5-sunburst`. Selected assembly revision: `software-factory-constellations/p1-assembly-v2/image-01.png`; problem 3 now uses `software-factory-constellations/p3-gear-electronics/image-01.png`, with the other five scenes retaining their first-draft selections. Prompts, settings and originals are preserved outside this repo under `content-production/2026.10.29--Arcturus-Labs-Website/website_copy/supporting_images/`. Responsive alpha WebPs are the shipped assets.

- The approved fears are falling behind, unreliable automation, and investing in tools or processes that become obsolete. There is no separate product-strategy problem.
- Product context belongs in the solution as practical guidance: what the software must do and what changes must not break.
- Plain-English skills are an intentional portability argument, not a claim of permanent compatibility. Readable instructions can survive particular frameworks while still needing maintenance, harness adaptations, executable tools, and verification.
- Incremental adoption answers all three fears: gain useful capability now, earn confidence before increasing autonomy, and avoid a wholesale stack replacement.
- The existing skill informs the guidance and QA ideas. It does not establish a mature large-team organizational or CI/CD design; references to existing delivery practices are a proposed direction, not a claim that the template already implements those integrations.
- Problem 1 uses Intercom's own account of agent-first engineering, not an independently measured before/after result or a claim about all competitors. Original source: https://ideas.fin.ai/p/we-gave-claude-code-to-everyone-at . Quote: “Within weeks, hundreds of engineers were shipping at a pace that would have seemed impossible a year ago.”
