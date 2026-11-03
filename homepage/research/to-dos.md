# Website to-dos

John's feedback and outstanding work for the prototypes. **Newest Agentic Web build: `draft_site_4/agentic-web.html`; latest copy: `draft_site_4/copy.md`.** Drafts 1–3 are preserved.
This is a handoff document: these are requests to implement or questions to discuss, not a description of everything already implemented. Latest feedback takes precedence over earlier brainstorming. Do not silently choose final copy where brainstorming is requested.

**Next iteration: content first.** Work through the wording with John before polishing graphics, animation, or interaction. Keep the three story pages visually balanced, even though John's interest is Agentic Web first, workflows second, factories third.

## Shared across all pages

- [ ] **Wrap-up – John’s original-source audit:** Trace every quote and number across all pages to its original source. Assemble direct links and relevant passages so John can personally reread them and check for hallucinations, misquoting, missing context and incorrect figures before publication.

- [x] Migrate Agentic Web to a reproducible Python builder without copy/layout changes. Maintained story and shared-tail templates replace generated-page extraction; homepage and sibling builders consume the same canonical tail. Exact pre-migration bytes, clean-output construction and idempotency verified; existing browser suites passed. Optional compact proof and video-bar unification remains deferred to the consistency pass below.

- [ ] **Deferred – cross-page consistency pass:** Make all current pages consistent, including the video bar/carousel and proof slide. Carry approved shared content, styling, and behavior across the homepage and story pages. Record only for now; do not implement during the current constellation exploration.

### Positioning and tone
- [ ] Promote **Arcturus Labs as an entity**, not merely John as a solo consultant. John's experience and authorship establish credibility, but a personal introduction need not be the opener.
- [ ] Write concise, motivating website copy, not a literal transcription of John's explanation. Show things where possible instead of labeling everything explicitly.
- [ ] Decide headline punctuation case by case. John asks whether website headlines typically need periods; discuss this during copy review rather than applying a blanket rule. He specifically likes the period in "You're here for a reason."

### External evidence for content (all four pages)
- [ ] Support important pain points—and solutions where evidence exists—with external numbers, studies, customer research, and concrete market examples, not only John's hypotheses.
- [ ] For each claim, preserve source URL, date, population/denominator, evidence type, and limitations. Distinguish behavior from stated preferences, executive forecasts, vendor claims, and our inference. Never turn correlation into causal uplift.
- [x] In **draft 3**, externally sourced claims link to original material through visible attribution text (Pew, Hosanagar, book titles). Apply the same approach when rebuilding other pages. Every externally sourced quote, fact, or figure displayed on the website must link to the original material. **Revised 2026-11-01 (supersedes the superscript-number approach): no superscript numbers anywhere on any page.** Instead, link the visible source text itself (e.g. the attribution line under a quote, or the study description under a statistic; for books, link the titles). Keep methodology details in research/copy notes; HTML comments are not a substitute for working source links. *(Removed from `draft_site_3`; draft 2 remains historical.)*
- [ ] Use `website_copy/` for one copy document per page. `agentic-web.md` has the current review draft; `index.md`, `workflows.md`, and `software-factories.md` are placeholders. Distinguish visible text from scroll/graphic directions.
- [ ] Research competing responses as well as approaches matching John's vision; record counterevidence. A product launch demonstrates investment/feasibility, not proven demand or outcomes.
- [ ] Use `content_research/` for research briefs. Keep unresolved hypotheses explicit and recheck sources before publishing numerical claims.

### Background, scrolling, and layout
- [x] The stars should tell a story across **the whole page**, not just a blue hero band. Do not retain the old live site's dated blue-sky/content-band proportions. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Keep the Arcturus logo and four-pointed stars. A full-screen, fixed background canvas is the likely approach: imagery and behavior change with scroll position, while content remains ordinary HTML readable by agents. Make this work with different page layouts. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Continue the night-to-morning gradient idea: not bright daylight, but morning approaching; sun peeking over the horizon at the bottom as a symbol of hope. Prototype exists; fine visual work comes later. *(implemented in `draft_site_2`: darker problem, stars return in solution, dawn at contact)*
- [x] Replace the static, left-aligned "Scroll" label with a cue that appears **a few seconds after loading**, bottom center just above the fold, with a downward arrow underneath. Applies to home and story-page openings. Exact delay still open. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] **Remove the "Pause motion" button and its manual pause functionality entirely.** This supersedes earlier suggestions to include a pause control. Reduced-motion accessibility preferences are a separate consideration, not an instruction to remove those safeguards. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Use **responsive layouts**: intelligently adapt to very narrow screens ("fluid layout" was John's question; responsive is the broader term). Possibly simplify the background for mobile performance. Do not overengineer mobile background variants; if complicated, defer them. *(done for the Agentic Web page; tested 320px–1440px; background only simplified by using fewer stars on phones)*

### Books, quotes, and authorship
- [x] Book covers are present, chronological left-to-right: *Relevant Search* (Manning), then *Prompt Engineering for LLMs* (O'Reilly).
- [x] **Keep the current book/quote layout, book hover effect, and Amazon links.** John likes these. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] ~~Under each cover, show only the publisher.~~ **Superseded 2026-11-01:** remove the lone “Manning” and “O'Reilly” captions entirely; the covers and the authorship line carry the information. *(Removed in draft 3; draft 2 stays unchanged.)*
- [x] Replace `[role]` and first-name-only attributions with the facts John supplied: *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
  - **Shantanu Dhaka — Chief Product Officer, Perch Insights.**
  - **Laura Murray — Founder, CETA Global; current Head of Global Mental Health at Google.** Distinguish the CETA engagement from her current Google role; do not imply Google commissioned or endorses the work.
  - **Corey Griggs — former Chief Technology Officer, Peer Supply.** Preserve the past-tense role.
- [x] **Add Arin Sime's training testimonial in draft 4**. John supplied the exact text and attribution, **CEO/Founder at AgilityFeat**: “If you have the chance to bring him in for a training with your team then I would definitely recommend it and I know my colleagues would too.” Added after Corey, verbatim, in HTML and `draft_site_4/copy.md`. Public training-video breadcrumb: https://www.youtube.com/watch?v=pqzj94_pZa8. Earlier spelling “Simes” is superseded by John's “Sime”. Carry this testimonial into the other pages when rebuilding them; historical drafts are unchanged.
- [ ] Quote-publication permission is still an outstanding check from the first draft. Don't assume it has been verified merely because attribution details are now available.
- [x] Explain **what the books represent** (implemented in draft 3): John coauthored them. Covers alone do not make the authorship connection sufficiently obvious. *(Revised 2026-11-01: line under the quotes becomes “Arcturus Labs founder John Berryman is a coauthor of Relevant Search and Prompt Engineering for LLMs,” with each title linked to its Amazon page and no superscript numbers.)*
  - Open wording/placement question: how to connect John's authorship to Arcturus Labs without reverting to a single-person-shop pitch?
  - Avoid repeating an authorship line under both books. Could put one line underneath the quotes. Brainstorm before implementing final wording.
- [x] The dated trusted-by logo board is removed from the revised pages.
- [ ] If useful, find logos for **Perch Insights, CETA Global, and Peer Supply** instead. Don't automatically restore the old employer/client logo strip.

### Booking, subscription, and publishing mechanics
- [x] Keep the simple bottom-of-page treatment. John likes it. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] **"Book a 15-minute call"** is clear enough by itself. Avoid redundant "Let's talk" and "Fifteen minutes..." prose or the uncertain "we'll see if I can help." *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [ ] Booking currently uses the approved **placeholder** https://calendly.com/jfberryman/15min; confirm the final destination before launch.
- [x] Restore an **email input for blog subscription** (enabled and connected in draft 3) alongside the subscribe button. Latest feedback supersedes the earlier button-only suggestion. Keep the copy concise; no repeated "get new posts by email" explanation is needed. *(Draft 3 uses the existing Kit form; original draft 2 stays disabled.)*
- [ ] **Connect the subscription form to Kit (ConvertKit).** The email field and Subscribe button must work, not remain disabled. Find the correct existing Arcturus Labs Kit form/embed; starting breadcrumb: vault note `Subscription Gating with Kit (ConvertKit).md`. Verify required settings, email validation, submission, success/error states, and any confirmation flow. Do not expose secret API keys in browser code or claim success without a real accepted submission. **Connected in draft 3** to public form `7337584` and the existing worker. Native Kit fallback for file previews and non-allowed origins. Worker preflight/empty-email validation checked live; pending/existing/error client flows tested with intercepted responses. **Still open: end-to-end confirmation-email test using John's authorized test address.** No unsolicited subscriptions.
- [ ] Blog lists are hand-selected/static; decide how they update (manual, feed, or build-time).

## `index.html` — homepage
**Rebuilt in `draft_site_4/index.html`** (earlier drafts untouched). Copy in `draft_site_4/index-copy.md`. Built without John in the loop; every wording choice below is a proposal. Checked boxes mean implemented in draft 4, not approved.

- [x] Content evidence pass: the homepage makes **no statistical claims**. The three choices are first-person pain statements and each links to a story page that carries its own sourced evidence. The "47 waiting" and "63 open" in the pictures are scenario details.
- [ ] John to confirm the headline and the three pain statements below.

### Opening headline and supporting line
- [x] Replaced "AI people actually trust." with **"Building the future of AI products"** (one of John's own directions) and a gold action line **"Start with the problem you're facing"** that leads into the chooser. Banked alternatives (from John's list): "Building AI products that build our future", "Building the AI that builds our future", "Building engaging AI experiences".
- [x] Removed "From GitHub Copilot's early days to two books on search and AI." The supporting line is **"Strategy, training, and hands-on engineering for teams building with AI agents."** and describes what the company does rather than a biography. Credentials live in the proof scene.
- [ ] John to judge whether the supporting line should name workflows/products explicitly, or whether "AI agents" is too narrow.

### Reason chooser
- [x] Kept **"You're here for a reason."** with its period; scroll-driven entrance.
- [x] **Extra scroll dwell** after the choices complete: the pinned scene holds for about the last third of its scroll length with everything in view.
- [x] Visceral, plain pain statements in the visitor's voice: "Our customers are asking AI instead of visiting us." / "Our best people are buried in work AI could start." / "We're shipping with agents, and the process is a mess."
- [x] Replaced "See how →" with each story's approved action line plus the arrow in gold: "Reclaim the user experience →", "Put their judgment to work →", "Build a factory you can trust →". These signal that the answer is on the next page. John to confirm that is the signal he wants.
- [x] Graphics pass done: the connected constellation is gone. Each choice is a star that **resolves into a simple picture** of its problem (a ChatGPT home search, a queue of 47 waiting research requests, 63 open agent pull requests). No fixed rectangular cards.
- [ ] Review whether the picture style (small desktop windows) is the "imaginative, modern" treatment John wants, or whether the pictures should be larger or more distinctive.

### Transition into the blog
- [x] Replaced "No reason at all? Even better." with the positive full-screen beat **"Just looking around? / See what Arcturus Labs is building"**. Alternative from John's notes still open: "See what Arcturus Labs is doing for X, Y, and Z".
- [x] Blog section kept, with the three newest posts (hand-copied 2026-11-01, with short summaries written for the page) and an "All posts" link.
- [ ] Decide how the post list is fed (by hand, from the blog feed, or at build time). Blurbs are my summaries, not the blog's own text.

### Proof and videos
- [x] Book/quote presentation reused from the story pages (publisher captions gone, linked-title authorship line, four testimonials with full roles).
- [x] **Real horizontal carousel:** slow automatic bounce, draggable with the mouse, native touch swipe, keyboard scrollable, pauses on hover/focus/interaction, off with reduced motion, **never driven by vertical scrolling**, clickable thumbnails.
- [x] Five videos: the three earlier talks, "Zero to Agent in 30 Minutes" (O'Reilly), and the AgilityFeat training video (thumbnails cropped to 16:9).
- [ ] **John to supply more videos** and confirm labels and order (Hugo Bowne-Anderson, Hamel Husain, Doug Turnbull, O'Reilly and others as applicable). The captions for the last two are my wording. Edit `draft_site_4/tools/build_home.py` to add more.
- [ ] Add a lead magnet / subscription variation later (see Future Work).

## Shared story-page updates
Applies to `agentic-web.html`, `workflows.html`, and `software-factories.html` unless John later says otherwise. Detailed content review of the stories is still pending; this feedback mainly concerns structure and presentation.

### Problem and solution as separate sequences
- [x] Keep two major sections: **problem**, then **solution**. They **do not need to be visible together**. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Replace the current single outline containing all six steps with **one scroll-through sequence for problem bullets**, followed by **another for solution bullets**. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Within each sequence, keep the **left outline fixed**, with the highlight indicating which bullet is being covered. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Move the active bullet's explanatory subtext to the **right side with the corresponding imagery**. Currently expanding subtext in the left outline makes it jump around as the user scrolls; this is distracting. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Keep all meaningful text in readable HTML, not just in the canvas or pictures. *(done; text inside illustrations is duplicated in adjacent HTML)*

### Alternate paths — removal supersedes previous directions
- [x] **Remove the entire “A different challenge?” section** (done in draft 3), including its heading, copy, other-path links, icons, and layout. John finds it a distraction from the conversation; no replacement is needed. This supersedes the earlier requests for clearer/larger alternate-path call-outs. Keep the three-path chooser on the homepage.

### What follows the story now
- [ ] **Remove the related blog-post section from all three story pages for now.** John doesn't yet have sufficiently specialized posts for each path. Restore later under Future Work. *(removed from `draft_site_2` Agentic Web; the other two story pages in `draft_site/` still have it)*
- [x] Flow from story into **proof (books and quotes)**, rather than into the provisional blog list. Alternate-path placement should not obscure this main flow. *(done in `draft_site_2/agentic-web.html` only; not yet other pages)*
- [x] Add a useful proof-section heading along the lines of **"Arcturus Labs can help"**. Exact wording open; this is not a request to restore the overly literal old homepage heading. *(draft: "Arcturus Labs can help"; John to confirm)*
- [ ] Apply shared book authorship and testimonial-attribution fixes. *(Agentic Web only)*
- [ ] **Remove videos from all three story pages for now.** They are nice proof, but not topical enough and may distract. Keep them on the homepage; restore targeted ones later under Future Work. *(removed from `draft_site_2` Agentic Web; the other two story pages in `draft_site/` still have them)*
- [ ] End in the same simple booking/subscription treatment as the homepage. *(Agentic Web only; subscription disabled)*

## `agentic-web.html` — Agentic Web
- [x] Initial external pain-point and competing-solutions research captured in `content_research/agentic-web.md`.
- [x] Likely include Kartik Hosanagar's quote about giving away customer interactions/brand experience and becoming a fulfillment company (Retail Dive; source in research brief). John particularly likes it. Verify exact wording/attribution and appropriate quotation length before publishing. *(included with source link)*
- [x] Consider Nikki Baird's lost-discovery-context quote (Retail Dive). John sees reclaiming discovery/decision context—potentially richer through voluntary personal-agent context—as central. Keep these quotations available during copy review. *(included with source link)*
- [x] Explore the complementary off-site path: useful MCPs and agent-discoverable skills that improve chat experiences and direct people to the website when its interactive experience adds value. Don't frame WebMCP/on-site participation as the only approach. *(covered by solution steps 1 and 2 in `draft_site_2`)*
- [ ] Explain the potential match between website capabilities and a personal assistant's preferences/context. Missing personal context as the cause of irrelevant recommendations remains a hypothesis, not a finding of the Nosto survey; avoid asserting it as proven.
- [ ] Address the counterevidence constructively: assistants can refer valuable visitors, not just displace visits. Agentic SEO/discoverability is an internal learning area; do not advertise it as an established Arcturus specialty.
- [ ] Use that brief in content review; select and verify publishable numbers. The pain has evidence, but portable personal agents inside products remain a proposed response, not a proven cure.
- [x] Replace “The web is going dark” and finalize the Agentic Web hero wording. **Latest approved version:** “Customers moving / to chat?” → “Reclaim the / user experience” (the shorter question supersedes the earlier statement). Supporting text, verbatim: “Engage customers when the conversation starts.” / “Bring them to a new experience that you shape and own.” Implemented in `draft_site_2/agentic-web.html` and `copy.md`; earlier candidates banked in `brainstorming.md`.
  - [x] Keep the formula: **“The agentic web” eyebrow → fear (white) → resolution (gold) → short clarifying text**. No periods on the headline pair. The body, not the hero, unfolds the personal-agent vision.
  - [x] Review the alignment experiment now on the page (John subsequently said the hero looks fine; preserved in draft 3): centered hero block with equal margins; white headline left-aligned, gold “Reclaim the user experience” right-aligned, supporting text centered. Line breaks tried: “Customers moving / to chat?” and “Reclaim the / user experience.”
  - [x] **Question form accepted in the copy review:** “Customers moving to chat?” with a break before “to chat?”. It is preserved in draft 3. Alternatives remain banked in `brainstorming.md`.
  - [x] Scroll cue (“Scroll to explore ↓”) now fades continuously with scroll offset instead of disappearing suddenly.
- [x] Opening punctuation settled: question mark after “to chat?”; no period on “Reclaim the user experience”.
- [x] Apply shared story-page changes and John's approved body copy in **draft 3**. All current copy is locked; historical draft 2 remains unchanged. Integration/launch checks remain below.

## `agentic-web.html` — round-2 feedback (John, 2026-11-01)

**Status: implemented in `draft_site_3/agentic-web.html` and `draft_site_3/copy.md`.** John requested a new folder for this iteration; draft 2 stays unchanged. Checked boxes in this section mean implemented in draft 3 only, not all pages. The locked copy supersedes the rough phrasing retained below. Kit is connected; the real confirmation-email test remains open. Arin's later-supplied quote is now included in draft 4.

### Copy review decisions – locked and implemented in draft 3

- [x] John approved the current hero and problem 1, chose problem 2 “Your customer experience is being taken over by chat.”, and approved problem 3's capabilities/full-story heading and revised body.
- [x] John approved the transition “Chat is where the conversation starts / Make your platform where it continues” (supersedes “Don’t leave the conversation outside / Make it part of your product”).
- [x] John approved solution 1 and solution 2's revised headings/bodies, including the website invitation moment unchanged.
- [x] John approved solution 3's heading and all three right-side paragraphs: context/preferences/past conversations; ability to guide/adapt/research; awareness and interaction on the shared surface. Confirmed that “can't interact with the UI” was a slip for “can”. No numbers or headings on the right.
- [x] John approved the proof introduction: “Product direction. AI behavior. Agentic engineering.” / “Meet customers in conversation. Bring them into an engaging experience on your platform.” Also approved the linked book-title authorship line, “Build what comes next” closing, booking CTA, and “Subscribe to the Arcturus Labs blog” as the single subscription invitation. Recorded and implemented in `draft_site_3/copy.md` and HTML.
- [x] **Implement the locked copy in `draft_site_3/`**, including the image, layout, background, citation, and proof revisions below. Draft 2 remains unchanged.

### Rules that apply across the whole page
- [x] **No superscript numbers anywhere.** Link the visible source text instead: the attribution under each quote (e.g. “Nikki Baird · Aptos”, “Kartik Hosanagar · Wharton”) and the description under the Pew statistic. Remove the superscript links on the Zillow example (the line itself is also being removed) and on the authorship line.
- [x] **Replace every em dash with a spaced en dash** (` – ` instead of `—`) in all visible copy, `copy.md`, and anywhere on the page.
- [x] **Remove every “View larger ↗” link** and the script that adds it. Images must stand on their own at the size they are shown, so any text inside an illustration has to be legible at that size (shrink or drop nonessential UI instead).
- [x] **Keep the illustration fixed in place and the same size** when the right-hand text changes within one step. Problem step 2's second moment shows the image at a different size (John prefers the size used in the first moment). Solution step 2's second moment shifts the image slightly. Fix by giving every moment in a step the identical image box.
- [x] **Image generation workflow for tweaks:** when John asks for small changes, pass the *original generated image* as an input together with a detailed text list of the changes, plus any relevant reference samples (such as the ChatGPT desktop-app screenshot below). Do not regenerate from scratch.
- [x] Use one terminology on the right-hand text: **assistant** (not agent) for the personal AI.

### Story chrome and outline
- [x] **Remove the thin horizontal progress bar** under the problem and solution sections (`.story-meter`).
- [x] Section labels: change “01 / The problem” and “02 / The solution” to just **“The problem”** and **“The solution”**.
- [x] Keep the left-outline look, but make the **active item more obvious**. Remove the small star marker. Try one of: (a) place the active item in a box; (b) give it an opaque white background with recolored (dark) text so it stays readable. Show John both if unsure.
- [x] Remove the link **“There’s another way ↓”** under the problem outline.
- [x] Remove the link **“Build it with Arcturus Labs ↓”** under the solution outline.

### Background (whole page)
- [x] Give the **whole page stars, except at the very bottom** (dawn/horizon).
- [x] **Return to the sky approach of `draft_site/index.html` (`draft_site/sky.js`) for now**; John will redesign the background storytelling later. The problem section currently goes nearly starless and dark; undo that.
- [x] The new sky lost the old one's **parallax**: stars should drift with scroll so it feels like scrolling down through space. Restore it.

### Transition between problem and solution
- [x] Style the transition exactly like the hero, using the later approved text: **“Chat is where the conversation starts / Make your platform where it continues.”** Same fonts and sizing strategy; white left, gold right. Earlier “Don’t leave…” text is superseded.

### Problem 1 — “Customers are finding answers without finding you.” (keep heading)
- [x] Image is close. **Move the “Your website, below the fold” annotation into the image** and make it prominently point at the partly hidden Willow link.
- [x] Delete the caption “Illustrative search · Willow is a fictional property platform” (obvious).
- [x] Change “Nearly half the click-through rate.” to **“Barely half the click-through rate.”**
- [x] Source link: link the study description under the statistic (e.g. “US browsing study, March 2025 · 900 adults”) to the Pew article; drop the superscript.

### Problem 2 — heading and content need rethinking
- [x] “You get the transaction, but lose the conversation.” does not work: “you get the transaction” is not obvious from the pictures, and the real problem is worse. Getting the transaction would be fine. The idea to convey: **the chat platform now owns the user experience.** Brainstorm a new heading with John.
- [x] **New image: text-only back-and-forth in the ChatGPT desktop application** (not a browser window). Sequence: user asks for 3-bedroom homes under $600K; ChatGPT asks a clarifying question; user clarifies; ChatGPT recommends and includes a couple of **links into Willow's website**. Keep the conversation short.
  - Reference: `/Users/johnberryman/Library/Application Support/Tortie/gmux/dropped-images/1793563385282-903663dd-image.png` (macOS app window with a left icon rail, centered conversation title, rounded user bubbles, composer at the bottom). Use as a **layout sample only**.
  - Change Hermitage to the fictional place used elsewhere (Brookfield). Remove the “Full access” indicator. Replace John's avatar with a different, generic person. The sample is Codex (“Work with Codex”, “Worked for…”); render ChatGPT branding and remove all personal details, history, timestamps, and model names.
  - Browser-style windows (as in the current generated images) are not wanted for any ChatGPT image.
- [x] **Keep only the second right-hand quote** (Hosanagar: “You're giving away the customer interactions, the brand experience, all of that, and then you become like a fulfillment company.”). Remove the first (Nikki Baird) quote and its moment; keep it banked in `content_research/agentic-web.md`.
- [x] Keep the image at the size shown in the first moment (see the fixed-image rule above).

### Problem 3 — rewrite heading and body
- [x] “Your product and their assistant are isolated.” introduces the assistant before the reader has met it. John's direction: something like **“Your platform has the capabilities they need, but their AI assistant has their full story”** (or “full context”). Final wording open.
- [x] Body, John's rough version: “Their assistant has their preferences, work context, and past conversations. Coming to your website means starting the conversation over, and having to learn a new UI by themselves.” Use the **white / gold contrast colors** to show the two sides of the contrast.

### Solution 1
- [x] Heading → **“Make your products discoverable and addressable by agents”** (John's wording).
- [x] Body stays a single text block.
- [x] Image: keep **Willow clearly in the center**, but make the **technology badges smaller** (they are currently the same size as Willow).
- [x] **Add a few more technologies (MCP and OpenAPI added).** John asked for recommendations. Candidates to discuss (verify each before including; do not imply certification): MCP server, OpenAPI / documented APIs, schema.org structured data, sitemap and crawler policy (robots.txt), agent cards / A2A. Existing badges: WebMCP, Agent Skills, llms.txt, SEO.

### Solution 2
- [x] Heading → **“Be present for your customers when the conversation begins.”**
- [x] Body, John's draft: “When users start their journey in chat, meet them there with useful tools, skills, and integrations to help them on their journey.” John wants different wording than the repeated “journey”, e.g. help them **get things done** or **accomplish their goals more efficiently**.
- [x] Image: show the **ChatGPT desktop application**, not a browser window (same app-window reference as problem 2). Use the original image as input plus the tweak list.
- [x] **Delete** “Already taking shape: Zillow brings listings and an interactive map into ChatGPT.” (and its source link).
- [x] Second moment (“Give those integrations a clear path into your website…”): keep the image **fixed in place** while the text changes.

### Solution 3
- [x] Heading → **“Build an engaging experience that brings the user and their AI assistant back to your platform.”** (John: “this is close”.) The reader does not need the assistant introduced in detail; the right-hand text clarifies it.
- [x] **Remove the small gold labels** (“Their context comes with them”, “One shared surface”): a new, tiny, fiddly visual element not used anywhere else. Keep the **three steps**, as body text only.
- [x] Core ideas to land concisely, without adding new ideas (John's “bring your own agent” staples): the assistant arrives **with the user's context**; once in the environment it becomes **capable** of acting there; and it has **awareness/observability** of the environment.
- [x] Step 1 (close to the current text): in the future everyone will have a personal AI assistant that carries their context, preferences, and past conversations. Users shouldn't have to leave it at the door because it carries important, useful information. Keep it brief.
- [x] Step 2, John's rough meaning: on your platform the user can work with the UI, and the assistant can also usher them through the experience, add insights from background research, and make interesting modifications to the experience. **Confirmed with John:** “can't” was a slip for “can”. Use the approved paragraph in `draft_site_3/copy.md`.
- [x] Step 3: the assistant can **see the environment and respond to the user's interactions**: what the user is looking at, what they have highlighted, and changes happening behind the scenes (new deals and the like).
- [x] Image (shared-surface scene): the editorial arrow **tails should attach to the specific chat messages**. Arrow from the assistant message (“I've shown matching homes in Willow”) points toward the Willow page; the “Sees your selection” arrow starts at the **selected listing** on the right and ends at the assistant's message. Change the assistant's message to **“I see you've selected the Maple Lane property.”** Use the original image as input.

### Proof and authorship
- [x] Subheading: “Product direction. AI behavior. Agentic engineering.” (was “…Engineering.”)
- [x] Second line, John's draft: **“Meet customers in conversation and bring them to engagement on your platform”** (“close”; polish the wording).
- [x] Remove the lone **“Manning”** and **“O'Reilly”** captions.
- [x] Authorship line → “Arcturus Labs founder John Berryman is a coauthor of *Relevant Search* and *Prompt Engineering for LLMs*” with the titles linked to their Amazon pages; no superscripts.
- [x] Keep: “From possibility to product” and “Arcturus Labs can help” (John approved both).

### Closing section, subscription, and footer — latest additions
- [x] **Remove the full alternate-path section** (“A different challenge?” and everything in it). See superseding shared requirement above. Preserve the direct story → proof → contact flow.
- [x] **Replace the closing three-line headline** “Your platform. / Their trusted assistant. / A better way forward.” with a large **“Build what comes next”**. Promote that phrase from its current small eyebrow to the main heading; do not repeat it at both sizes. John likes it as the closing line.
- [x] **Delete visible draft/disclaimer clutter**, specifically “Preview only · email subscription isn’t connected yet.” and “Illustrative interfaces, not live product demos. Google and ChatGPT belong to their respective owners. Willow is fictional.” Treat the implementation as a final-site candidate; do not sprinkle subtle placeholder explanations across the rendered page. Keep development limitations in project docs, not visitor-facing copy. Still provide honest operational success/error feedback for the actual form, and do not misrepresent mock illustrations as shipped client work.
- [x] **Simplify the subscription invitation to one statement.** Replace the compound “Follow the work / New posts from Arcturus Labs” with one concise invitation, plus email input and Subscribe button. Brainstorm the final line with John in conversation. Keep an accessible input label even if it is visually hidden; no redundant headings.
- [ ] **Kit connection implemented in draft 3; real confirmation-email test still open.** Make the email box actually work through Kit, not just appear functional. Remove disabled attributes as part of real integration; see shared Kit task for setup, validation, success/error handling, and end-to-end verification. Do not silently enable a form that has no working destination.
- [x] After the copy review, apply the changes to **`draft_site_3/agentic-web.html` and `draft_site_3/copy.md`**, preserving draft 2 at John's request.

## `draft_site_4/` – latest Agentic Web iteration

**Implemented in draft 4 only.** This section supersedes conflicting older wording/layout directions above. Earlier drafts remain intact.

- [x] Hero question → **“Are your customers moving to chat?”** (break before “to chat?”).
- [x] Vertically center each right-side image+copy group; no longer anchor images close to the top. Give supporting copy the picture's actual width and left edge. Reserve common copy height within multi-moment steps so their images do not move.
- [x] Problem 1: large diagonal red **handwritten** “Your website, below the fold” annotation with hand-drawn arrow/circle. Keep screenshot words unchanged. Remove the separate “Barely half the click-through rate.” sentence from HTML/copy.
- [x] Problem 2 image only: keep blue property links and labels/prices; delete gray URLs and “Explore them on Willow”. Red handwritten note chosen for preview: **“By the time they find your page, you've missed the conversation.”** No visible Willow name in that scene.
- [x] Problem 3: **“Their assistant already holds your customer's preferences, work context, and past conversations. Coming to your website means starting the conversation over and switching context.”** One paragraph, first sentence white, second gold.
- [x] Give the transition a full-screen slide of its own with native sticky dwell on desktop; no wheel interception. Reduced motion/mobile use normal flow.
- [x] Solution 1 heading/body use **platform**, not product. Image has five supporting tiles: WebMCP, Agent Skills, llms.txt, MCP, **Claude / ChatGPT integration**. Remove SEO/OpenAPI from the image.
- [x] Solution 2 becomes **one slide**: “When users start their journey in chat, meet them there with useful tools, skills, and integrations that help them accomplish their goals. When possible, carry the conversation into your website – into an experience you own.” Second sentence gold; remove the former invitation-only slide.
- [x] Generate a consistent red handwritten text/arrow/circling-line sample first, then supply it alongside the original renders for image edits. Style sample and prompts are in `website_copy/supporting_images/willow-scenes-v4/`.
- [x] Solution 3 image: two red handwritten annotations **“the assistant updates the page”** and **“and sees customer interactions”**, with clean hand-drawn arrows. Follow-up correction applied: top arrow has a **plain tail at the matching-homes assistant message**, a single head into the page generally (not a property); bottom arrow starts at selected Maple Lane and points to the assistant's selection message. **Use `image-03`, not the earlier double-headed `image-01`.**
- [x] Solution 3 step 1: remove only “work” from “preferences, work context,” → **“preferences, context,”**; keep rest identical; **“Don't make them leave it at the door.”** gold.
- [x] Solution 3 last text → **“The assistant observes the customer interact with the page, works alongside them, and brings relevant information into view.”**
- [x] Remove proof line **“Meet customers in conversation. Bring them into an engaging experience on your platform.”** Retain the agentic-engineering line.
- [x] Fix email focus/hitbox appearance: combined field/button is one rounded 8px group with shared focus outline; no oversized rectangular input-only outline. Preserve visible keyboard focus and working Kit behavior.
- [x] Add copyright with runtime current year. Make footer Blog/LinkedIn/Back-to-top links match the Arcturus Labs footer brand's font, size, weight and color.
- [x] Update `draft_site_4/copy.md`, README and main directory guide. Verify desktop/phone, small screens, reduced motion/no JS, all eight moments, centered/aligned media and copy, stationary repeated images, transition dwell, form focus, footer typography/year, and inherited mocked Kit states.

**Unchanged open launch work:** general quote-publication permissions (Arin's text/attribution are now supplied and included), final Calendly URL, authorized real Kit confirmation-email test, Safari/iOS and assistive-technology review. No new visible placeholder/disclaimer copy added.

### Draft 4 follow-up refinements (same directory)

- [x] Hero break is between “customers” and “moving”: “Are your customers / moving to chat?”.
- [x] Statistic: “versus 15% without one.” gold, including the bold portion.
- [x] Problem 2: **“Your customer experience has been taken over by chat.”** In outline and mobile heading.
- [x] Problem 3: **“Your platform has the capabilities, but the customer's AI assistant knows the full story.”** In outline and mobile heading.
- [x] Solution 1: “with accessible content, clear documentation, and discoverable integrations and skills.” gold.
- [x] Solution 2: **“into an experience you own.”** italic, retaining the gold sentence.
- [x] **Restore the original proof layout with a good slide pause**, per John's follow-up. Remove compact proof-only type/spacing/book-size/grid overrides. Heading, two book covers, all **four** testimonials (including Arin Sime) and authorship remain one scene. Native desktop dwell lasts one viewport; tall content scrolls into view normally before pausing with its bottom visible, rather than shrinking the layout or clipping content permanently. Mobile/reduced motion stays in natural flow. Both the introduction-only slide and compact proof treatment are superseded.

## `workflows.html` — Business workflows

### Current virtuous-cycle rewrite (supersedes the earlier outline below)
- [x] Round 4: lead-in third line is “Automate tasks dependably.” and all three lines are centered; the Joe Choy / JSM quote slide was removed from solution 2 so it cannot be mistaken for Arcturus’s own result (the page now carries no JSM material).
- [x] Round 3: three-line one-slide solution lead-in with scroll pause; solution 2 reduced to the copy plus the Joe Choy quote (the 15% study and JSM figures removed from the page but retained in research notes); solution 3 and 4 wording updated (“ensure”, not “insure”).
- [x] One office-assistant robot design (sensor-visor head, no face, adult proportions, subdued carapace) applied to every robot image: workflow stairs, desk and handoff scenes and the homepage chooser. Handoff robot is about 4′8″ beside a taller human. Prior variants preserved.
- [ ] John to confirm the visor-head robot also suits the homepage “lure” image, where the confident/alluring expression now comes only from posture.
- [x] Round 2: shorter routine-task headline (provisional wording), updated hero and four solution steps, quote-only quality problem, separate 15% evidence moment with requested emphasis, and simpler maintenance copy.
- [x] Re-read JSM original story: use 25–35% less substantive rework during supervisory review plus one to two hours saved per matter; do not imply a whole-process percentage. Attribution now Microsoft News.
- [x] Update all active constellation robot figures to expressive non-human mechanical faceplates (homepage and four workflow scenes); preserve previous variants. Comparison figure now looks at B with tidier clothing.
- [x] All four current pages share the compact-proof formatter and stylesheet, verified to fit the tested 1280×720, 1440×900 and 1840×1000 viewports. Smaller viewports retain natural scrolling.
- [x] Preserve pre-rewrite copy in `draft_site_4/copy-history/workflows-before-virtuous-cycle.md`; checkpoint preceding builder/proof/research work in commit `17e965c` before implementation.
- [x] Draft and implement three pain headings and four solution headings; latest annotation document is `draft_site_4/workflows-copy.md`.
- [x] Reuse the homepage paperwork constellation, dim it behind linked HTML figures; keep repeated artwork stationary across Slack, Asana and McKinsey moments.
- [x] Generate six constellation scenes using all three selected homepage images as references: A/B comparison, ascending agents, low-hanging fruit, draft handoff, peaceful expert with working agent, evaluation handoff between agent generations. Preserve original PNGs and prompts; export variable-alpha assets.
- [x] Include Morgan Stanley quality quote, 15% AI-assisted support productivity finding and JSM first-draft savings/quote in their relevant moments. Sources linked visibly.
- [ ] John to refine all draft copy, review imagery and the longer augmentation sequence. No claim of final copy approval.
- [ ] Complete John's original-source audit, especially Asana/McKinsey sources previously retrieved only as search excerpts, and confirm source quotation/publication permissions as needed.

**Built in `draft_site_4/workflows.html`** (not yet in earlier drafts; the homepage in `draft_site/` still links to the old stub). Unattended build, not yet reviewed by John.
- [x] Research external evidence for workflow pains and solution outcomes; brief in `content_research/workflows.md`, including alternatives, counterevidence and caveats.
- [x] Apply shared story-page structure (separate problem/solution sequences, stable outline, right-side moments, proof, closing, no related posts/videos). Copy in `draft_site_4/workflows-copy.md`.
- [ ] **John's content review.** Headline, bullets, evidence choices and scenes were written without his input. Specific things to judge: the hero question/action, whether the McKinsey 2012 estimate and MIT 95% figure are strong enough to show, and the fictional clinical-supply scenario.
- [ ] Re-verify linked statistics against their original documents before launch (MIT NANDA PDF and McKinsey page could not be fetched directly).
- [ ] Add workflow-specific quotes/examples if John has them; the existing testimonials are reused as-is.

## `software-factories.html` — Software factories
**Built in `draft_site_4/software-factories.html`.** Unattended build, not yet reviewed by John.
- [x] Research external evidence and alternatives; brief in `content_research/software-factories.md`.
- [x] Apply shared story-page structure. Copy in `draft_site_4/software-factories-copy.md`.
- [x] Keep claims proportionate: copy describes an approach and the questions to ask, not team-delivery results. Learning gaps (team-level operating model, CI/CD and QA at speed, independent verification) stay out of capability claims. No testimonial is presented as factory evidence.
- [ ] **John's content review**, especially: whether the three outside findings (Faros telemetry, DORA's amplifier finding, METR trial) are the right pains; whether "Build trust into the factory" overstates; and the fictional Tallybook scenario.
- [ ] Re-verify the Faros figures (98% more pull requests, 91% longer review) against the full report; they came from the vendor page's summary.
- [ ] Decide whether Twin Sun's "dark factory" conversation, or John's own factory, should appear as a concrete example later.

## Future Work
These items are intentionally **not part of the next content-focused pass**.
- [ ] **Story-page related posts:** restore a blog section promoting genuinely relevant posts for each path once the content exists. Future examples will probably be blog pages linking to live demonstrations.
- [ ] **Story-page relevant videos:** restore curated, topical videos on the three story pages once suitable material is available.
- [ ] **Concrete Agentic Web examples:** add demonstrations to make the problem and solution felt. They are coming later; the page must communicate without them for now.
- [ ] **Alternative contact form:** try a prettier version of the current live site's contact form, connected to **the same existing backend**. Keep the simple booking approach available while exploring it.
- [ ] **Graphics/interaction polish:** three problem images, possible constellation-to-image transitions, richer story scenes, restrained mouse/scroll interactions. Content first.
- [ ] **Optional mobile background simplification:** investigate only if needed and straightforward; avoid making this a large engineering task.

## Outstanding launch checks
- [ ] Confirm testimonial publication permission, final assets and links, and real examples versus illustrative placeholders.
- [ ] Replace placeholder scenes with final imagery where needed; no fictional metrics should read as client results.
- [ ] Test mobile/narrow layouts, keyboard navigation, assistive technology, reduced-motion behavior, and background performance.
- [ ] Ensure the booking link and actual subscription flow work before publishing. No prices are to be posted; the goal is a conversation.


## Approved homepage revision – implemented

- [x] Larger products-and-workflows hero; approved three pain statements/actions; preserve current chooser images and staging.
- [x] Integrate “Just looking around?” into blog heading, remove separate transition dwell.
- [x] Homepage-only compact proof: same quote size, inline titles, both Laura credentials, coauthorship beneath right book; fit checked at 1280×720, 1440×900, 1840×1000.
- [x] Seven-video endless forward strip (two chosen channel videos first); accessible hidden clones, native/reduced-motion fallbacks, drag/keyboard/vertical-wheel regression checks.
- [x] Homepage-only raised dark ground/footer, YouTube link, fixed right booking tab/mobile pill.
- [x] Homepage, sibling stories, Agentic smoke and protected-file checksums pass; copy and build documentation updated.
- [ ] Owner review of screenshots; final video selection remains separate.
- [ ] Constellation concepts and factory story alignment deferred; no story/shared files changed in this revision.
