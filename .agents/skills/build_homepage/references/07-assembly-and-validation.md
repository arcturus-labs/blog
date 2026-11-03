# 07 – Assemble, validate, and hand off

This phase has now been exercised through `draft_site_3/` and `homepage/`. The latter is the current working example; its `README.md`, `copy.md`, `story.js`, `styles.css`, `subscribe.js` and `tests/smoke.cjs` provide implementation evidence, not an immutable design specification.

## Assemble the requested version

Read the active copy, graphics selections and latest backlog. A later instruction can supersede an older “final” phrase. Make a new draft directory only when asked; otherwise update the current one. Preserve earlier drafts for comparisons. Don't silently update the homepage/other stories when the request concerns only Agentic Web.

Keep narrative, headings, quotations, sources, links and forms as semantic HTML. Canvas is decorative and cannot own the meaning or intercept interaction. Image alt text should convey its contribution, not transcribe every tiny UI control. Keep important narrative in adjacent HTML.

Use progressive enhancement: normal reading flow without JavaScript; natural layouts on narrow/short screens and with reduced motion; pinned stages only where useful. No wheel hijacking or horizontal scrolling driven by vertical input. Deep links, back/forward and keyboard outline navigation must still work.

## Layout details that materially improved the page

### Center the actual composition

- A capped-width hero needs explicit centering (`width:100%; max-width:…; margin-inline:auto`) or a large right margin appears on wide screens.
- Center the **image plus its copy as one group**. Anchoring all images at the top of the viewport made the right side feel too high.
- Match copy width/left edge to the **actual displayed illustration**, not a wider grid column. A full-width `img` with `object-fit:contain` can have narrower visible content, leaving its caption seemingly far to the left.
- Measure natural image ratios, available column width and text height after fonts/images load. Reserve a common maximum copy height for moments sharing one step so the same picture cannot move when a paragraph changes.
- Test real image and copy bounds, not just “no overflow”. Keep all moments readable without enlargement controls.

### Make active state and timing obvious

Opaque white active outline items with dark text were clearer than a tiny star and subtle text-color change. Remove unnecessary progress lines and tiny labels instead of introducing a new UI vocabulary for every section.

A delayed scroll cue should fade **continuously with scroll offset** and return when scrolling back up. Separate its entrance animation and scroll-opacity layer (e.g. child animation + parent opacity) so animation fill does not override scroll updates. Make fully invisible controls inert rather than leaving ghost click/tab targets.

### Dwell must preserve the design

“Give this scene a slide pause” is a behavior request, not permission to compact typography, shrink covers, widen the quote column or split a heading away from its content. Ask what constitutes the scene if unclear. For proof, it means **heading + books + all testimonials + authorship**, not a title-only slide.

The final proof restores the original spacious layout. On desktop, allow its natural-height stage to enter; when taller than the viewport, it can pause with the bottom visible. One native sticky implementation is:

- stage height = `max(viewportHeight, naturalStageHeight)`;
- sticky top = `min(0, viewportHeight - stageHeight)`;
- section height = `stageHeight + desiredDwellDistance`.

With a one-viewport dwell distance, the entire scene remains one composition without permanently clipping content or shrinking it. Short/narrow/reduced-motion layouts use ordinary flow. This is different from requiring every long testimonial to fit simultaneously at 720px height.

## Styling and accessibility details

- Apply emphasis exactly where requested. Let nested `strong` inherit gold inside a gold clause; otherwise a generic white-strong rule silently defeats the styling.
- Use a single rounded email+button group. Focus the group with `:focus-within`; suppress the mismatched input-only rectangle **only while preserving a visible keyboard focus indication**. Keep the email label accessible even if visually hidden.
- Footer links need readable contrast and the intended brand typography, not tiny muted afterthought text. Set copyright year at runtime with a sensible static fallback.
- Keep the sky behind the content, not over it. Bound DPR/star counts and animation rate, suspend when hidden, and honor reduced motion. Current sky has continuous stars and perceptible scroll parallax, with dawn near the bottom, not a starless problem phase.

## Connect real conversions safely

Inspect the existing site's actual form and backend before inventing a replacement. In this project, the live blog already supplies:
- public Kit form `7337584`, native POST field `email_address`;
- a credential-protected worker for inline submission;
- an explicit allowed-origin list.

No secrets belong in browser code. A native hosted-form POST provides a real file-preview/no-JS/unsupported-origin fallback. Do not send inline requests from an origin the worker won't allow: the server might perform the signup while CORS hides the response, encouraging duplicate retries.

Validate email, prevent duplicate in-flight submission, restore controls after errors, use an accessible live status, and distinguish pending confirmation from an existing list entry. Inspect HTTP-200 error payloads, unknown shapes, malformed JSON, network failures and timeouts. Never infer confirmed subscription merely from “email found” or set an authorization cookie on an unverified request. Do not fake success because the form looks finished.

Keep status empty before use, not “preview only”. Real operational feedback is not placeholder clutter. If credentials/configuration or a consented test address is missing, record the blocker internally and report it. Don't silently leave a dead form or subscribe a guessed address.

## Browser verification

Exercise all moments, entry/release and each multi-moment step. Check:
- correct active outline/moment, stable left layout and fixed repeated-media bounds;
- image/copy widths and left edges, vertical group centering, equal hero margins;
- readable illustration text, decoded lazy images, no clipping/overflow;
- whole-scene dwell and access to all tall content, not just the title's sticky position;
- deep links/history, keyboard focus, cue fade and return;
- removed captions, superscripts, disclaimers, duplicate moments and unwanted em dashes;
- footer typography/year, booking destination and accessible form labels/status;
- console errors and failed requests.

The project matrix includes wide desktop, laptop, small laptop, tablet, 390px and 320px phones, reduced motion and JavaScript disabled. Compare screenshots at the same viewport. After scroll, wait for lazy images/fonts before diagnosing a blank illustration. Do not read screenshots concurrently with the command that is still generating them.

Use intercepted Kit responses for pending/existing/error, malformed/unknown data, network failures, validation and control recovery. Intercept a native form POST to verify field names and destination without registering anyone. Live preflight and empty-email validation establish reachability, **not a successful signup or delivered confirmation email**. A real end-to-end test requires the owner's authorized address. Chromium mocks do not establish Safari/iOS or assistive-technology coverage.

## Handoff and release

- Update the active draft's copy/README with actual behavior, selected image versions, checks run and remaining limits. Keep the root document map current; leave owner-curated notes alone unless asked.
- Reconcile checked tasks with reality and scope. Separate copy approval, implemented code, browser verification, live-service validation and publication permission. Don't call all shared pages done because one draft changed.
- Keep known incomplete work honest: Arin's text/name/title became resolved when John supplied them; general quote permissions, final booking URL and authorized Kit mailbox testing are separate issues.
- Inspect git status and staged paths. Exclude secrets, private raw references and unrelated work. Commit/push only when authorized; if asked to checkpoint first, do that before the next experiment. Push only the intended branch, not backup tags or rewritten history.
- Don't leave “uncommitted/not pushed” hardcoded in documentation after release. Use accurate checkpoint references or direct future readers to git status.
- Keep the closing report short: active path, changes, meaningful test coverage, blockers, commit/push status. If asked to open a preview or announce completion with `say`, do so once the work is actually ready.

## Replicating the page for other topics

Once one story page is approved, build siblings without editing it:

- Checksum the finished page and its shared CSS/JS before starting; verify they are unchanged at the end.
- Assemble each new page from a content configuration (hero, three problems, bridge, three solutions, image mapping, proof order) using the Python builders and canonical `tools/templates/story-tail.html` component (not generated page extraction). This kept three pages consistent without duplicating logic. Keep per-page copy and image names in a separate build file; commit the generated HTML.
- Give images topic-specific prefixes so exports cannot overwrite another page's assets.
- Reuse one parameterized browser test across pages. It should check every moment's layout and alignment, equal hero margins, stable repeated images, transition dwell, removal rules, failed requests and page errors in the whole viewport matrix. A generic test caught nothing new here only because the template was already proven; keep it anyway.
- Inspect every generated scene before building. A scene can satisfy its prompt yet fail its job: one first render showed three identical agent plans under a headline about three different products. Fix it with a targeted edit of the existing image plus the style sample.
- Keep external evidence honest per page: link sources, state sample sizes, and note when a figure came from a search extract or vendor summary rather than the fetched document. Prefer a narrower accurate claim to a viral headline number (for example, do not write that AI slows developers down from one early-2025 trial).
- Do not let proof imply relevance it lacks: existing testimonials may be reordered for fit, but must not be presented as evidence for a different offer.
- Record per-page review items in the backlog (what the owner should judge) and note that the page was built without their input.

## Homepage-specific implementation notes

- Put homepage-only behavior in its own CSS/JS so shared story-page files stay byte-identical; reuse the proof, closing and footer markup from the maintained shared-tail template at build time.
- A pinned "choose your problem" scene works well as one sticky stage driven by a single `--rp` (0 to 1) custom property set from scroll. CSS `clamp()` and `calc()` on that variable stagger each choice, cross-fade a star into its picture, then leave the last third of the scroll length as pure dwell. Default `--rp` to 1 so no-JavaScript, narrow, short and reduced-motion layouts simply show everything. Mark choices `inert` until they appear.
- A video strip should be a native `overflow-x` scroller (keyboard, touch and trackpad work for free) with `overflow-y: hidden` so vertical wheel input scrolls the page. Add slow automatic movement with its own fractional position (browsers round `scrollLeft`), ignore scroll events caused by the script, pause on hover/focus/interaction/off-screen/reduced motion, and suppress the click after a mouse drag. In tests, avoid `scrollIntoViewIfNeeded` on strip items: it moves the strip and pauses the auto-scroll.

## Python builders: maintained inputs and exact preservation

From `homepage/`:

```sh
python3 -I tools/build_agentic_web.py
python3 -I tools/build_home.py
python3 -I tools/build_workflows.py
python3 -I tools/build_software_factories.py
python3 -I tests/builders.py
NODE_PATH=/Users/johnberryman/.npm/_npx/e41f203b7505f1fb/node_modules node tests/smoke.cjs
PAGES=agentic-web.html,workflows.html,software-factories.html NODE_PATH=/Users/johnberryman/.npm/_npx/e41f203b7505f1fb/node_modules node tests/story-pages.cjs
NODE_PATH=/Users/johnberryman/.npm/_npx/e41f203b7505f1fb/node_modules node tests/home.cjs
```

- `tools/templates/agentic-web.html` preserves Agentic's carefully tuned hero/story/bridge markup verbatim. It has one `{{ shared_tail }}` insertion point. `build_agentic_web.py` calls `story_page.build_preserved_story`; it works with no existing generated page and never rekeys images.
- `tools/templates/story-tail.html` is the maintained proof/contact/footer source for all builders. `story_page.shared_tail()` reads it; `_tail()` handles sibling quote ordering and home-link plumbing. Homepage uses the same source but applies its existing compact attribution/authorship/footer transforms. Moving markup into this template does not authorize changing it on every page.
- `build_home.py` owns homepage configuration and transforms; `home-videos.json` owns its selected titles, publishing channels/icons and stable shuffled order. The Agentic migration deliberately preserves its original proof and does not add the optional homepage video strip. Cross-page visual unification remains separately reviewable work.
- Sibling builders retain their per-page configurations and `export_scene()` asset pipeline. That pipeline rekeys original images and writes alpha WebPs; do not run it for a markup-only Agentic change. Homepage constellation export starts from already-transparent PNGs, preserving variable alpha rather than keying again.
- Edit maintained inputs, then regenerate and commit both sources and output when authorized. Never edit generated HTML alone or use it as the next build's source. Update active copy documents only if visible wording is intentionally approved to change.
- For migration, baseline rendered text, screenshots and protected-page hashes first. `tests/builders.py` builds into an empty temporary output directory, asserts the approved full-page SHA-256 (stronger than text-only equality), then asserts a second build is byte-identical. An approved future copy change needs a deliberate baseline update after review, not automatic snapshot replacement to hide a failure.
- Rebuild twice, compare output bytes, and check protected page/assets hashes. Run browser checks across all affected pages, plus before/after screenshots at identical viewport/scroll positions. Exact HTML preservation plus unchanged CSS/JS gives a particularly strong no-redesign guarantee; still inspect screenshots and verify lazy images are decoded. Chromium checks do not substitute for Safari/iOS, assistive technology or a real consented signup.

## Success criterion

Visitors recognize the problem, discover a credible next experience, see why this business can help, and can act. They can understand it by scrolling normally, without mastering the interaction or already knowing the owner's future vision.
