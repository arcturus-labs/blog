# Fourth draft – Agentic Web

Open **`agentic-web.html`**. Drafts 1–3 are preserved. The approved copy plus this round's requested revisions are in **`copy.md`**.

HTTP preview (serve the website working directory):

```sh
python3 -m http.server 8001 --bind 127.0.0.1
# http://127.0.0.1:8001/draft_site_4/agentic-web.html
```

## Python builder source of truth

Run from this directory:

```sh
python3 -I tools/build_agentic_web.py
python3 -I tools/build_home.py
python3 -I tests/builders.py
```

Agentic Web is generated from `tools/templates/agentic-web.html` plus the canonical `tools/templates/story-tail.html` (proof, contact and footer). Edit those maintained inputs, not generated HTML. `tools/story_page.py` supplies composition to Agentic and the sibling builders; homepage consumes the same shared-tail source and retains its existing homepage-only transformations. No builder reads generated `agentic-web.html` as input. The initial migration preserved Agentic byte-for-byte. All four current pages now share `tools/proof_component.py` and `compact-proof.css` (no duplicate homepage-only proof CSS): inline attributions, both Laura credentials, tighter spacing and authorship below the right book, with unchanged quote text/font sizes. All story builders apply `tools/page_chrome.py` and `story-chrome.css` for the fixed booking tab, corrected homepage links, YouTube footer link and dark footer, using the homepage sky behavior. The video carousel has not yet been ported.

`tests/builders.py` verifies construction with no existing output, exact approved output bytes and repeatability. Browser validation also passed Agentic smoke, all 27 story configurations and all 9 homepage configurations. Before/after screenshots at 1280, 1440, 1840, 390 and 320 widths were captured under `/tmp/agentic-{before,after}-<width>-{hero,problem,proof}.png`; rendered main text compares exactly. Agentic's compact proof now fits desktop viewports; narrow screens retain natural scrolling without clipping.

Sibling rebuilds remain `python3 -I tools/build_workflows.py` and `python3 -I tools/build_software_factories.py`. Workflow artwork now uses `tools/constellation_assets.py` to preserve variable alpha and cache responsive exports; factory scenes retain their original chroma-key exporter. Do not rebuild unrelated pages for an Agentic-only markup edit. Homepage videos are maintained in `tools/home-videos.json`. See project skill reference 07 for the full asset/test workflow.

## Changes in this iteration

- Hero: “Are your customers / moving to chat?”; existing action and supporting text retained.
- Picture and supporting copy are now measured as one **vertically centered group**. The copy uses the picture's actual displayed width, so its left edge no longer starts far left of the image. A common reserved copy height keeps the image stationary across a step's multiple moments. This works with different image aspect ratios and longer paragraphs.
- Removed “Barely half the click-through rate.” The factual Pew comparison and linked source remain.
- Problem 3 is one paragraph: first sentence white; “Coming to your website means starting the conversation over and switching context.” gold.
- The transition has its **own full-screen slide with one viewport of native sticky dwell** on desktop. No scroll interception; reduced-motion, short-screen and narrow-screen versions stay in ordinary reading flow.
- Solution 1 says **platform**, not product, in heading and body. Five supporting technologies: WebMCP, Agent Skills, llms.txt, MCP, Claude / ChatGPT integration. SEO and OpenAPI removed.
- Solution 2 is **one moment**, with the new second sentence in gold. Former invitation moment removed. Three problem + five solution moments, eight total.
- Solution 3 context sentence drops “work”; “Don't make them leave it at the door.” is gold. Final paragraph uses the shorter wording supplied by John. No extra headings or numbers on the right.
- Removed the extra proof-introduction sentence, retaining “Product direction. AI behavior. Agentic engineering.” **The original spacious proof layout is restored**: normal heading size, larger books, original quote-column proportions/spacing, and 15.2px quote text. Heading, books, all four testimonials (including Arin Sime) and authorship remain one scene. Desktop pauses for one viewport of scrolling without squeezing the layout. Tall scenes enter normally and pause once their bottom is visible; every part remains reachable. No compact slide-specific styling.
- Follow-up copy refinements: “has been taken over by chat”; capabilities/customer-assistant heading revised; statistic comparison and discovery-assets clause gold; “into an experience you own.” italicized.
- Email field and button form one rounded group. Focus outlines the entire group, rather than an oversized rectangular outline around only the input. Keyboard focus remains visible.
- Footer includes copyright with current year set at runtime. Footer links match the Arcturus Labs text's font, size, weight and color.

## Reference-led image edits

Sources and prompts: `../website_copy/supporting_images/willow-scenes-v4/`.

First generated **`annotation-style/image-01.png`**, a white sample sheet of large red handwritten labels, clean curved arrows, oval and underline. Passed that image alongside each prior scene and the brand sheet for the related edits.

- **Problem 1, image-01:** unchanged screenshot words; large diagonal handwritten “Your website, below the fold” with hand-drawn arrow and circling line around the clipped result.
- **Problem 2, image-01:** blue property links/prices retained; gray URLs and “Explore them on Willow” removed. No visible Willow name. Red annotation: “By the time they find your page, you've missed the conversation.”
- **Solution 1, image-01:** five supporting tiles around Willow, including the combined integration tile.
- **Solution 3, image-03:** handwritten red “the assistant updates the page” and “and sees customer interactions.” Top arrow has a plain tail at the matching-homes assistant message and one arrowhead into the map generally, not at a property. Return arrow starts at selected Maple Lane and points into the assistant's selection message. Earlier image-01's double-headed arrow is superseded; image-02 corrected the head count, image-03 corrected its destination.
- Problem 3 and solution 2 retain draft 3's illustrations.

Greenscreen originals and transparent derivatives are retained. Shipped images are trimmed alpha WebP files in `assets/`. Keying removes border-connected green plus near-pure-green islands trapped by red circles, without deleting normal foliage or map greens.

## Kit and remaining launch work

The working connection from draft 3 is retained unchanged: public Kit form **7337584**, native hosted-form fallback (including file previews and port 8001), and inline worker enhancement on its existing approved origins. No client credentials. See `../draft_site_3/README.md` for endpoint details and verification boundaries.

Arin Sime's exact training quote and CEO/Founder at AgilityFeat attribution are now included, supplied by John. Still open: general testimonial publication permissions; final Calendly destination; an authorized real mailbox signup/confirmation test; Safari/iOS and assistive-technology review. No visible draft disclaimers or fake success states were added to the page.

## Verification

`tests/smoke.cjs` uses Playwright; run with Playwright installed/on `NODE_PATH` and the working directory served at port 8001. Tests never send a real subscription; Kit responses are intercepted.

Checked 1840×1000, 1440×900, 1280×720, 1024×668, 820×1180, 390×844, 320×568; also reduced motion and no JavaScript. All eight moments fit without horizontal overflow or clipping. Repeated-step pictures have identical bounds; image and copy left edges/widths agree within 1px; picture+copy groups are centered. Tested transition dwell, outline navigation, cue fade/return, focus styling, footer typography/year, removal of the extra slide/labels, and all inherited mocked form states. Desktop/phone screenshots visually inspected.

Drafts 3–4 and their image sets were checkpointed and pushed in `d3c1491`. The follow-up restores the original proof layout while retaining dwell and adds Arin's supplied quote; it is saved in a subsequent commit.

## Other story pages (added after the Agentic Web iteration)

`workflows.html` and `software-factories.html` use the same layout, scripts, sky, proof scene, closing and Kit form as `agentic-web.html`. **`agentic-web.html`, `styles.css`, `story.js`, `sky.js` and `subscribe.js` were not modified** (checksums compared before and after).

- **Business workflows (current owner-directed rewrite):** “Are your experts buried in work? / Scale their expertise, not their workload.” Three pain headings cover expert toil, quality judgment and fast-changing technology. A three-line solution lead-in on its own paused slide (“Augment your experts on day one. / Keep humans in charge. / Automate tasks dependably.”, centered), then four steps: start with the most impactful tasks, augment expert staff, promote reliable work, maintain and continuously improve workflows. Every robot on the site (workflows and homepage) uses one practical office-assistant design with a sensor-visor head and no human face. Nine scroll moments (five problem, four solution) keep the evidence readable without adding outline bullets. The first three share the same dimmed paperwork constellation with real HTML statistics overlaid; the remaining scenes use six new reference-guided transparent constellations. Sources: Slack/Asana/McKinsey, Morgan Stanley interview, published Generative AI at Work study, JSM customer account. Copy: `workflows-copy.md`; old copy: `copy-history/workflows-before-virtuous-cycle.md`. Research limitations and John's source audit remain open.
- **Software factories:** "Writing more code than you can ship? / Build a factory you can trust." Problems: faster code but slower shipping (Faros telemetry), AI amplifies the existing process (DORA 2025), measured and perceived speed can differ (METR). Solutions: shared product intent, a repeatable process of skills and isolated worktrees, evidence-based verification. Copy: `software-factories-copy.md`. Evidence and limits: `../content_research/software-factories.md`.
- Each page has three problems and three solutions, all with one moment per step, red handwritten annotations on the problem scenes and on one solution scene each, the shared white outline highlight, centered picture-and-copy groups, and the same transition and proof dwell.
- Testimonials appear in a page-appropriate order (workflows leads with Corey Griggs, software factories with Laura Murray). **No testimonial is presented as evidence of a software factory.** Quotes, roles and permissions are unchanged and still need the general publication-permission check.
- Scenes use fictional products ("Meridian Supply" clinical supply team; "Tallybook" invoicing app) with invented names. Illustrative counts such as "47 waiting" and "63 open" are scenario details, not evidence or client results, and are never cited as such in the copy.
- Images were generated with `gpt-image-2.5-sunburst` from descriptive prompts plus the shared handwriting sample, then keyed and exported as alpha WebP. Prompts and originals: `../website_copy/supporting_images/workflow-scenes/` and `factory-scenes/`. The first factory problem-2 render showed identical plans in all three agents; `image-02` (differing assumptions) is the shipped version.

### Rebuilding the pages

`tools/story_page.py` assembles a page from a content configuration and the maintained `tools/templates/story-tail.html` proof/contact/footer source, never extracting generated Agentic HTML. `tools/build_workflows.py` and `tools/build_software_factories.py` hold each page's copy and image mapping. Run with `python3 -I tools/build_<page>.py` from this directory (needs Pillow, NumPy, SciPy). Re-keying is deterministic. The generated HTML is committed; these scripts are the editing source for the two new pages. Do not use them to modify the Agentic Web page.

### Verification

`tests/story-pages.cjs` runs the story-page checks (set `PAGES`): all nine moments' layout and alignment, equal hero margins, repeated-image stability, transition dwell, outline navigation, removal rules, no failed requests, no page errors, for 1840, 1440, 1280, 1024, 820, 390 and 320 px widths, reduced motion and JavaScript disabled. Both new pages passed all 18 runs. Phone/desktop screenshots were inspected. The Kit form markup is identical to the Agentic Web page; mocked submission flows were exercised only on that page.

Not tested: Safari/iOS and assistive technology; real subscriber confirmation; final Calendly URL; permissions for external quotations and the testimonials. Statistics were linked to their sources, but the MIT NANDA PDF, McKinsey page and the Faros report body could not be fetched directly in this session, so some figures rest on search extracts or secondary summaries (see each research brief). Re-verify before launch.

## Homepage (`index.html`)

Rebuilt from the homepage requirements in `../to-dos.md`, again without changing `agentic-web.html` or the shared `styles.css`, `story.js`, `sky.js` and `subscribe.js` (checksums verified). Homepage-only behavior is in `home.css` and `home.js`; `tools/build_home.py` generates the page. Copy for annotation: `index-copy.md`. The workflows and software-factories pages now link their logo and footer to this homepage; `agentic-web.html` still links to the first draft's homepage because it was not to be modified.

- **Hero:** "Building the future / of AI products and workflows", enlarged, with “and workflows” gold. No biographical line.
- **"You're here for a reason."** keeps its period and is a pinned scene on roomy desktops. Choices enter one after another as stars with their pain statement, the stars resolve into three simple pictures (a ChatGPT home search, a queue of waiting research requests, a pile of agent pull requests), the invitations (the approved homepage actions, with the arrow) fade in, and the scene then **holds for roughly a third of its scroll length** before it releases. The old connected constellation and fixed rectangular cards are gone. Without JavaScript, on narrow or short screens, and with reduced motion, everything is simply visible as a stack. The choices are inert until they appear so keyboard users do not tab into invisible links.
- **After the choices:** "Just looking around? / See what Arcturus Labs is building" is the blog heading directly above the three posts and "All posts" link; no extra slide/dwell.
- **Proof:** the shared compact book-and-quotes scene used by all four current pages (same quote font size, inline names/titles, both Laura credentials, authorship beneath the right book), then a **real video strip**: seamless forward loop (about 22 px/s), mouse dragging, native touch swiping, keyboard scrolling, pause on hover/focus/interaction, off with reduced motion. It scrolls only sideways. A vertical wheel over it scrolls the page.
- **Closing:** the same "Build what comes next", booking button and Kit form as the story pages.

### Homepage verification

`tests/home.cjs` ran 9 view configurations (1840, 1440, 1280, 1024, 820, 390, 320 px, reduced motion, no JavaScript): no horizontal overflow, no failed requests or page errors, hero margins, the pinned scene's six scroll states (title entrance, staggered stars, stars replaced by pictures, dwell with everything in view, inert states), unpinned fallbacks, the carousel's slow auto-scroll, mouse drag without navigation, vertical wheel not moving the strip, keyboard scrolling, no auto-scroll with reduced motion, proof fit, loop wrapping, fixed booking tab, "Book a call" jump, dark footer and YouTube link, copyright year, and links to the three pages. Screenshots were inspected for desktop and phone.

Not done: Safari/iOS, assistive technology, touch-gesture testing on a real device, final Calendly URL, a live Kit signup, John's further videos.

### Approved homepage revision verification

The sixteen owner-selected videos and their stable shuffled order/channel icons are defined in `tools/home-videos.json`. Decorative clones are inert/aria-hidden; reduced motion and no JavaScript retain an ordinary strip. `home-sky.js` derives ground height from the footer and is also used by the story chrome; original sky.js remains unchanged. The fixed Calendly tab becomes a bottom-right pill under 700px.

Proof stage measurements (before compact CSS → after; CSS pixels): 1280×720: 1210 → 720 (490 saved); 1440×900: 1166 → 900 (266 saved); 1840×1000: 1157 → 1000 (157 saved). “Before” is HEAD ba4ab50, measured by routing its original HTML/home.css/home.js into Playwright without altering working files. The inherited partial HTML with new attributions but old spacing measured 1202/1159/1150px respectively. All four quotes, books, heading and engineering line fit after. Quote font size unchanged; no attribution titles abbreviated. Smaller screens retain native flow/sticky overflow fallback, not clipping.

Rerun: homepage 9 configurations, sibling stories 18 configurations, Agentic smoke 9 configurations plus mocked subscription responses passed. Protected Agentic/shared checksum baseline passed. Screenshots in `/tmp/home-{wide,desktop,laptop}-proof.png`, `/tmp/home-*-hero.png`, `/tmp/home-*-footer.png`; laptop proof/phone hero/laptop footer inspected. No live signup, commit or push. Real touch/Safari/screen-reader review remains outstanding.
