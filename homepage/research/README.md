# Arcturus Labs website

Started: 2026-10-29. **Status: working static prototypes and content review.** Homepage and all three story pages exist; wording, graphics, and integrations remain provisional. Nothing here should be mistaken for a launch-ready site.

## Start here

1. [john_notes.md](john_notes.md) — John's curated direction and decisions. Preserve his edits; add only when asked.
2. [to-dos.md](to-dos.md) — current actionable feedback: shared changes, homepage, shared story structure, each story page, Future Work, and launch checks. Latest explicit feedback supersedes earlier ideas.
3. [draft_site_4/README.md](draft_site_4/README.md) — newest Agentic Web iteration: centered image/copy groups, handwritten red annotations, full-screen transition dwell, streamlined copy and five-technology graphic, rounded form focus and improved footer. Open `draft_site_4/agentic-web.html`; annotate `draft_site_4/copy.md`. Draft 3 remains preserved at `draft_site_3/`.
4. [draft_site_2/README.md](draft_site_2/README.md) — preserved previous Agentic Web build, for comparison.
5. [draft_site/README.md](draft_site/README.md) — original four-page prototype; homepage and the other two paths still live here.
6. [content_research/agentic-web.md](content_research/agentic-web.md) — external evidence for Agentic Web pain points and competing solutions. Read before revising that story's claims.

## Current direction

- Homepage helps visitors choose among **Agentic Web**, **business workflows**, and **software factories**; each has a dedicated problem/solution story page.
- Primary conversion: book a conversation. Blog subscription is secondary. No public prices.
- Arcturus Labs is the brand; John's early GitHub Copilot experience, coauthored books, testimonials, and talks provide credibility. Do not inflate aspirations into proven delivery claims.
- Visual direction: whole-page night sky, four-pointed stars, subdued dawn at the bottom, optional interaction. Real content stays accessible HTML; decorative canvas sits behind it.
- Agentic Web copy is approved and implemented with the latest requested revisions in `draft_site_4`; the other pages still need content review. Support claims with external evidence; distinguish measured findings, executive concerns, vendor claims, and John's hypotheses.
- `to-dos.md` records what is implemented in drafts 3–4 versus still outstanding. Arin Sime's supplied training testimonial is included in draft 4; authorized live Kit confirmation-email testing and launch checks remain open.

## Complete document guide

### Root documents

| Document | Purpose |
| --- | --- |
| `README.md` | This directory guide and current project context. |
| `john_notes.md` | John's curated notes and checklist; protected from unsolicited rewriting. |
| `brainstorming.md` | Broader idea dump: goals, offers, audience paths, structure, branding, proof, interactions, and open questions. Historical options, not all approved requirements. |
| `to-dos.md` | Implementation and content-review backlog, organized by page; includes deferred work and launch checks. |

### `skill/` — repeatable collaborative website-development process

- **`SKILL.md`** — overview and entry point for repeating this process on the remaining pages; project-local, not installed globally.
- **`references/01-context-and-positioning.md`** — recover decisions, read competency/talk notes, clarify audience and conversion.
- **`references/02-site-and-interaction-research.md`** — comparable-site research and live interaction inspection.
- **`references/03-architecture-and-feedback.md`** — straw men, review passes, and actionable per-page feedback.
- **`references/04-evidence-and-market-mapping.md`** — pains, competing solutions, source quality, and counterevidence.
- **`references/05-copy-and-story.md`** — concise outline headings, scroll moments, proof, and citations.
- **`references/06-graphics-and-generation.md`** — reference-led image briefing, privacy, current models, and descriptive generation-first prompts (not handcrafted fake HTML).
- **`references/07-assembly-and-validation.md`** — planned implementation, browser checks, accessibility, and release/handoff discipline.

### `website_copy/` — page-by-page copy review

- **`agentic-web.md`** — earlier problem/solution draft and rationale. The latest copy is in **`draft_site_4/copy.md`**; use that for implementation and annotation.
- **`index.md`**, **`workflows.md`**, **`software-factories.md`** — placeholders for the other three pages, with links to their review requirements.
- **`agentic-web-graphics.md`** — scene-by-scene brief and original reference manifest; later light-mode revisions are captured in generated-scene prompts.
- `supporting_images/` — supplied working references (some contain private details; not publication-ready), Willow brand sheet, and four generated scene rounds with prompts/originals/transparent versions. `willow-scenes-v4/` includes the common handwriting sample and latest annotation-led edits. **`willow-scenes-v3/`** supplies draft 3's native desktop-app scenes, internal fold callout, revised supporting-tech proportions, and corrected two-way arrows.
- Source citations now link the visible study/quote attribution text directly, **not superscript numbers**. This supersedes older citation directions.

### `content_research/` — evidence for website content

- **`workflows.md`**, **`software-factories.md`** — evidence briefs for the other two paths: what John's notes claim, what outside research supports, competing approaches, and copy guardrails.
- **`agentic-web.md`** — evidence for AI-answer click displacement, customer-relationship concerns, discovery needs, and privacy/control; limitations and counterevidence; solutions including WebMCP, retailer-owned assistants, apps in ChatGPT, external commerce channels, structured information, crawler monetization, and conventional UX. Marks what is proven versus hypothetical and what still needs verification.
- Research briefs should include alternatives to John's preferred approach, not just confirming evidence.

### `draft_site_4/` — newest Agentic Web iteration

- **`README.md`** — this round's changes, selected render versions, preview/test instructions, and remaining launch checks.
- **`copy.md`** — latest copy, including the longer hero question and merged solution-2 moment.
- `agentic-web.html`, `styles.css`, `story.js`, `sky.js`, `subscribe.js` — current page and unchanged Kit connection.
- `assets/` — transparent optimized illustrations; red notes/arrows use a shared generated handwriting reference.
- **`index.html`** (+ `index-copy.md`, `home.css`, `home.js`) — the homepage: hero, the pinned "You're here for a reason." scene, recent writing, proof, a draggable video strip, and the closing. `tests/home.cjs` checks it.
- **`workflows.html`, `software-factories.html`** (+ `workflows-copy.md`, `software-factories-copy.md`) — the other two story pages, consistent with the Agentic Web page. `tools/` rebuilds them from their copy configuration; `tests/story-pages.cjs` checks them.
- **`tests/smoke.cjs`** — eight-moment browser checks, image/copy alignment, centered groups, transition dwell, form focus/footer checks and intercepted Kit tests.
- Draft 4 now also contains a rebuilt **homepage** and the finished **Business workflows** and **Software factories** story pages, built from the same template. Drafts 1–3 preserved. Draft 4 restores the original spacious proof layout with scroll dwell and includes Arin Sime's supplied testimonial. Checkpoint `d3c1491` was pushed; subsequent proof refinements are saved separately.

### `draft_site_3/` — preserved third Agentic Web implementation

- **`README.md`** — implemented feedback, preview instructions, Kit behavior, verification, and remaining launch issues.
- **`copy.md`** — approved copy, mirrored in the page, ready for annotation.
- **`agentic-web.html`**, `styles.css`, `story.js`, `sky.js`, `subscribe.js` — complete page, revised responsive story, continuous parallax sky, and real Kit form with optional inline worker enhancement.
- `assets/` — optimized transparent illustrations and existing book/brand assets.
- **`tests/smoke.cjs`** — browser matrix and intercepted Kit-response tests. Does not register real subscribers.
- Drafts 1 and 2 are preserved. No new homepage/workflow/factory pages; those destinations still use draft 1.

### `draft_site_2/` — preserved second Agentic Web prototype

- **`README.md`** — build guide, implemented feedback, test coverage, and unresolved content/backend issues.
- **`agentic-web.html`** — complete fresh rebuild using the current copy and light-mode Willow illustrations; independent of draft 1's code.
- `styles.css`, `story.js`, `sky.js` — new responsive layout, progressive scroll-story enhancement, and phase-aware sky.
- `assets/` — optimized alpha WebP illustrations plus brand/book assets. Original generation outputs remain under `website_copy/supporting_images/`.
- No second-draft homepage, workflow page, or factory page yet; navigation to those destinations points to the first draft. The rebuild and John's final hero wording are saved in a subsequent local commit after checkpoint `0236b10`; nothing pushed.

### `draft_site/` — inspectable HTML prototypes

- **`README.md`** — implementation/preview guide, shared behavior, known placeholders, and testing limitations.
- `index.html` — homepage chooser, blog, proof, videos, booking/subscription.
- `agentic-web.html` — participatory Agentic Web story.
- `workflows.html` — expert workflows, review, evaluation, and earned autonomy.
- `software-factories.html` — agent-driven development, intent, coordination, and verification.
- `styles.css`, `site.js`, `sky.js` — shared layout, scroll-story behavior, and decorative background.
- `assets/` — brand graphics, book covers, and talk thumbnails. `reference/` contains older visual references, not an authoritative record of the latest draft.

### `ai_agency_review/` — consulting-site positioning research

- **`README.md`** — reading guide, scope, and retained materials.
- **`comparison.md`** — cross-site comparison of positioning, offers, credibility, and conversion.
- **`navigation.md`** — navigation and visitor-path observations.
- **`vs-brainstorming.md`** — research compared with our website ideas.
- Eight subject folders: `allie-k-miller/`, `dave-ebbelaar/`, `drew-breunig/`, `eleanor-berger/`, `jason-liu/`, `kavita-ganesan/`, `matt-webb/`, and `rachel-woods/`.
  - Each **`notes.md`** contains the site's review/observations.
  - Each **`text.md`** retains extracted site text for checking wording and structure.
  - Screenshots provide visual references where retained.
- `_tools/` — research/capture scripts for regeneration, not website runtime files.

### `engaging_websites/` — interaction and visual research

- **`README.md`** — reading guide; John's preferred Ponder patterns come first.
- **`patterns.md`** — reusable interaction patterns and their relevance to this site.
- **`method.md`** — how interactions were inspected and what was actually verified.
- **`sources.md`** — source sites and research references.
- `cases/` contains six focused studies:
  - **`ponder-accordion-cards.md`** — expanding hover-card choices.
  - **`ponder-pinned-steps.md`** — sticky, scroll-driven storytelling.
  - **`andrei-moise-scroll-journey.md`** — particle journey and constellation presentation.
  - **`elespacio-button-hover.md`** — measured button motion/cursor treatment.
  - **`mamuso-cartridge-chooser.md`** — 3D chooser and verification limitations.
  - **`stash-index-list.md`** — row-hover treatment, filtering, and page transitions.
- `screenshots/` — supporting captures. These studies are inspiration, not instructions to reproduce the sites literally.

## Internal source context

The Arcturus Labs Obsidian vault provides the competency, strategy, biography, accomplishments, testimonials, and speaking background. Initial sources included `Arcturus Core Competencies.md`, `Arcturus Labs Strategy 2026-09-25.md`, and `ToDos/Make a website for Arcturus Labs.md`; additional notes were subsequently reviewed.

For the content pass, the core competencies and all five corresponding talk notes were read: Agentic Web, Building the Future of AI Products, Software Factory, Virtuous Cycle, and English is the Programming Language of AI Software. These establish John's position, **not external market validation**.

The broad vision is personal agents that carry continuity into websites, applications, physical locations, events, and devices. Consulting delivery can include assessment, advisory support, training, and bounded implementation: the client owns wider-system integration; Arcturus owns the agreed AI behavior. Keep learning areas distinct from established expertise, especially team-scale software factories.
