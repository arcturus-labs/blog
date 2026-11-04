---
name: build_homepage
description: Use when editing, researching, rebuilding, testing or publishing the Arcturus Labs homepage and its three story pages (agentic web, business workflows, software factories) in the blog repo. Covers copy, evidence research, imagery, the Python builders, tests, and publishing into the MkDocs site.
---

# Develop evidence-led website stories

Help an owner discover what the website should communicate—not merely turn their initial notes into HTML. Move between business intent, actual audience concerns, external evidence, and visual storytelling. Collaborate in small rounds: propose, hear criticism, revise, and preserve decisions so the next agent can continue without the conversation.

This skill lives in the blog repo (`.agents/skills/build_homepage`). Paths below are relative to the blog repo root unless noted. Source of truth for the homepage is `homepage/`; `docs/` holds generated output.

## Working principles

- The owner's mental model is valuable input, not market validation. Research can strengthen, qualify, or contradict it.
- Lead with the buyer's recognized problem, not a compressed version of the owner's sophisticated solution. The page earns the reveal as visitors scroll.
- The output is a compelling story, not an exhaustive competency list or a literature review.
- Few stable outline headings; richer explanatory moments can unfold through scrolling. Graphics and copy should reinforce one another.
- Most visitors simply scroll. Interaction must not be required to understand the offer.
- Keep visible language confident and concise without changing the meaning of evidence.
- Do not confuse an attractive mockup, a vendor announcement, or a proposed experience with a demonstrated outcome.
- Preserve the owner's voice and explicit preferences. Start from their wording when requested; bank alternatives, lock exact approvals, and distinguish copy approval from implementation and testing.
- Treat a layout, scroll pause, and copy as separate decisions. Adding dwell must not silently shrink the books, change column proportions, or rewrite approved text.
- Reference-led image editing is iterative: keep the original scene, pass approved style/branding samples, and verify semantic details such as arrow direction and endpoints.
- Build visitor-facing copy as a final-site candidate. Keep implementation caveats in project docs, not scattered preview warnings; never fake a functioning conversion or a shipped result.
- Work on the requested phase/page. Writing notes is not permission to change HTML; image planning is not permission to generate; generation is not permission to publish.

## Workflow and references

Read the reference for the current phase; revisit earlier phases when evidence or feedback changes the story.

1. **Recover context and clarify the job.** Read curated notes and linked competency/talk material; identify audience, offer, conversion, constraints, and what remains a hypothesis. [01 — Context and positioning](references/01-context-and-positioning.md)
2. **Research websites for the right reasons.** Separate offer/navigation research from visual interaction research; inspect live behavior and synthesize patterns, not copies. [02 — Site and interaction research](references/02-site-and-interaction-research.md)
3. **Make a rough straw man, then capture critique.** Use enough structure to provoke useful feedback; separate shared changes, per-page work, and deferred work. [03 — Architecture, prototypes, and feedback](references/03-architecture-and-feedback.md)
4. **Research pains and competing solutions.** Look for outside data, buyer language, counterevidence, and actual approaches on the market. Map findings back to the owner's model without confirmation bias. [04 — Evidence and market mapping](references/04-evidence-and-market-mapping.md)
5. **Write a directional scroll story.** Develop a small problem/solution outline, then short right-side moments, quotations, and graphics together. [05 — Copy and story development](references/05-copy-and-story.md)
6. **Brief and generate coherent imagery.** Collect references, protect privacy, define exact compositions and text, verify current model choices, and generate directly from descriptive prompts and image inputs. [06 — Graphics and generation](references/06-graphics-and-generation.md)
7. **Assemble, test, and hand off.** Use the Python builders and maintained templates, not generated HTML as input. Preserve approved copy with exact-output regression tests; validate source links, responsive presentation, imagery, and conversions before publishing. [07 — Assembly and validation](references/07-assembly-and-validation.md)

## Layout

- `homepage/` — source: `tools/` (builders, `templates/`, `home-videos.json`), `tests/`, shared CSS/JS, `assets/` (committed WebP exports), `*-copy.md` (annotatable copy), `README.md`.
- `homepage/research/` — notes, backlog (`to-dos.md`, `john_notes.md` is owner-curated: never rewrite unasked), `content_research/` evidence briefs, `website_copy/` briefs, competitor/interaction research.
- `scripts/publish_home.py` — copies `homepage/` pages, CSS/JS and used images into `docs/` (`docs/home/`), injecting Google Analytics, canonical, Open Graph and Twitter tags. Never hand-edit `docs/index.html`, the three story pages or `docs/home/`.
- `hooks/recent_posts.py` — MkDocs hook that fills the homepage "recent posts" with the five newest posts at build time (markers `<!-- recent-posts:start/end -->`).
- The raw generated-image originals (~200 MB) were deleted along with the old `content-production/2026.10.29--Arcturus-Labs-Website/` project (and expunged from that repo's history on 2026-11-04). `homepage/assets/` holds the only copies of the shipped artwork: 76 committed WebP/JPG exports. Do not delete them. Ordinary rebuilds reuse them via `cached_scene()` and need no originals. `--assets`/`HOMEPAGE_REBUILD_ASSETS=1` only works if originals are supplied again via `HOMEPAGE_SCENES`; if new artwork is needed, generate it fresh and export it into `homepage/assets/`.

## Workflow commands (run from blog repo root)

Shortcut: `python3 scripts/build_homepage.py [home|agentic-web|workflows|software-factories ...]` runs the builders then `publish_home.py`. Add `--assets --scenes <supporting_images path>` to re-export artwork. The steps below are the same thing spelled out.

```sh
# 1. edit copy/templates/config under homepage/tools (never generated HTML)
cd homepage
python3 -I tools/build_agentic_web.py
python3 -I tools/build_home.py
python3 -I tools/build_workflows.py
python3 -I tools/build_software_factories.py
python3 -I tests/builders.py            # exact-bytes Agentic guard; update baseline only after deliberate approved change
cd ..
# 2. publish into docs/
python3 -I scripts/publish_home.py
# 3. preview + verify
.venv/bin/mkdocs serve                  # http://127.0.0.1:8000
.venv/bin/mkdocs build && python3 scripts/test_home.py
NODE_PATH=/Users/johnberryman/.npm/_npx/e41f203b7505f1fb/node_modules node scripts/test_home_browser.cjs   # needs mkdocs serve running; Kit mocked
# homepage-only browser tests: python3 -m http.server 8001 -d homepage, then node homepage/tests/{smoke,home,story-pages}.cjs
```

Builders need Pillow, NumPy, SciPy (system python3 has them). Publishing = commit to `main` and push (GitHub Actions deploys). Commit locally freely; **ask John to review before pushing**. Kit signup tests are always mocked; a real signup test needs his authorized mailbox.

Homepage videos: edit `homepage/tools/home-videos.json`. Homepage choices: `PICKS` in `build_home.py`. The `POSTS` list there is only a fallback for the standalone preview; the live list comes from the hook.

## Research help

When John asks for research, copy ideas, or new pages: follow phases 1–5 above, write evidence into `homepage/research/content_research/<page>.md` (link sources, sample sizes, counterevidence, vendor vs. measured), and proposed text into the page's `*-copy.md`. Only after approval change builders/templates. Record open review items in `homepage/research/to-dos.md`.

## Resuming

Read `homepage/README.md`, `homepage/research/to-dos.md`, then the relevant `*-copy.md`. `homepage/research/website_copy/<page>.md` may be an older brief. Recent explicit feedback overrides older notes. Drafts 1–3 of the original project are gone (the old content-production folder was deleted and its history rewritten); this repo is now the only copy. Chromium checks do not cover Safari/iOS or assistive tech; open launch items (Calendly URL, testimonial permissions, real Kit mailbox test) are in the backlog.
