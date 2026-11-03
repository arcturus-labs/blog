# Engaging website patterns: what we learned (2026-10-29)

Synthesis of five sites inspected directly (measured in a browser and, where possible, by reading their CSS and JavaScript). Detail for each is in `cases/`; the way I measured is in `method.md`. Everything here is evidence about those pages, not a verdict on what Arcturus should do; the "fit for Arcturus" notes are suggestions.

## Constraints John set (these decide what counts as good)
- Most visitors arrive and just scroll down. Anything clicky must be optional and must never be needed to understand the page.
- Everyone must understand what John does and what to do next; clarity beats spectacle. "Not just showy garbage."
- Navigation should feel like one continuous space, not a jump to a new world.
- Avoid the generic AI look (dark, glowing, purple/green).
- The page should be readable by agents (real HTML text under any animation).
- John likes scrollytelling and wants clickable things to *look* clickable.

## The two Ponder patterns (John's favorites)

Both are on https://ponder.ai/. Full measurements: `cases/ponder-pinned-steps.md` and `cases/ponder-accordion-cards.md`.

### 1. Pinned steps with scenes that play as you scroll ("How Ponder works")
**What a visitor sees:** a numbered list of four steps stays fixed on the left. The right side shows one picture per step. As you scroll, the picture for the current step builds (a prompt types itself, clips fly onto a timeline, a cursor circles and strikes through something), the matching step lights up and its description opens, then the picture scrolls away and the next step takes over.
**How it works:** CSS `position: sticky` for the left column and for each scene. Each step gets a tall scroll "budget" (the scene stays pinned for 360, 720, 1,080, and 360px of scrolling at 720px screen height; the busiest step gets the most). A GSAP ScrollTrigger turns scroll position into a 0-1 number per scene, and a small function sets styles from that number. The animation runs only while you scroll (it is tied to scroll position, not a timer) and finishes at 62% of the pinned window so the finished picture holds for a moment. The active step changes exactly when the next scene's top reaches the top of the screen. Clicking a step scrolls to it. A ring around each step circle shows progress.
**Why it suits Arcturus:** it is the "pain, solution, proof" story told as scenes while the wording stays put, so someone who simply scrolls gets a guided story. Each reason page could be one of these.
**Costs and risks:** about 11 KB of custom script plus GSAP; scroll budget must be planned per step; separate layout for phones (a sticky bar showing only the active step); in the source I found a reduced-motion check only for one small animation, so what reduced-motion users see is unverified; need real text for every scene so agents can read it.

### 2. Accordion cards with a "Try..." reveal ("An editor that works the way you do")
**What a visitor sees:** four equal cards with little live demos inside. Hover one and it widens (291px to 481px in my measurement, about 0.45s) while the others narrow (to 228px). A small link ("Try a first cut", "Try exporting") fades in from below. The card's title and paragraph are always visible.
**How it works:** a flex row where the hovered card's `flex-grow` goes from 1 to 1.7 and the others to 0.8, with an ease-out transition; the demo inside rescales to fit; a veil over the demo fades out; the hidden link has opacity 0 and a 4px offset that clears on hover. Only for mouse users on screens at least 1100px wide.
**Why it suits Arcturus:** it is a natural home for "you're here for a reason": one card per reason, readable without hovering, with hover as a bonus invitation. The widening is the "this is clickable" signal without a button or tab, and the other cards stay visible (one continuous space).
**Costs and risks:** on Ponder only the small link is clickable, so for a chooser make the whole card the link; touch and narrow screens get no effect, so they need a clear static version; I did not test those.

## Other patterns observed

| Pattern | Site | One-line summary | Fit for Arcturus | File |
|---|---|---|---|---|
| Button squeeze + cursor swap | elespacio.net | Pure-CSS squash-and-spring on hover; pixel-art arrow cursor becomes a pointing hand over links; the arrow icon slides out and back | Cheap, accessible way to make every call-to-action look clickable | `cases/elespacio-button-hover.md` |
| Index list with row wipe | stash.cool | Rows are real links; hover wipes the row black and slides the text 8px; category URLs; cross-page view transitions; keyboard shortcuts and a command palette | Strong model for the blog index and per-reason filtered posts | `cases/stash-index-list.md` |
| 3D object chooser | mamuso.dev | Six 3D cartridges (one per job); hover changes the cursor; activating one spreads the stack and turns it to face you; hidden real buttons mirror each cartridge | Shows an "objects you can pick" chooser with an accessibility twin; heavy (WebGL); the hover wiggle was not reproduced | `cases/mamuso-cartridge-chooser.md` |
| Scroll-driven camera journey | andreimoise.ai | One full-screen particle scene; scrolling flies a camera through scenes that illustrate the story; blog posts shown as a labeled constellation | Constellation of posts echoes the Arcturus star idea; but long empty stretches, no stated offer, and a dark glowing look | `cases/andrei-moise-scroll-journey.md` |

## Cross-cutting techniques that made these pages work
- **Signal clickability with motion or shape, not decoration.** Cursor change (elespacio, mamuso), shape change on hover (elespacio), width change plus a revealed link (Ponder cards), full-row inversion (stash).
- **Keep the real content in HTML.** Ponder's step text, stash's rows, mamuso's hidden buttons, and andreimoise.ai's note titles are all real elements, so the page reads without the animation.
- **Make hover optional.** Elespacio and Ponder wrap their hover effects in a mouse-only media query (`hover: hover`, plus a minimum width on Ponder), so touch screens get a static version. Stash's row hover was not gated in the rules I read. Keyboard focus gets the same effect on elespacio (`:focus-visible`), and stash has its own keyboard cursor state.
- **Spend scroll in proportion to content.** Ponder's longer scene gets longer pinned time, and every scene holds after finishing.
- **One idea per screen.** Ponder pairs one sentence with one picture; andreimoise.ai uses one or two sentences per scene.
- **Give people a way out.** Stash has a "Pause all motion" button; Ponder lets you click any step.
- **Pre-render, then enhance.** Stash ships static HTML and lets JavaScript take over for filtering.
- **Cross-page continuity without a single-page app.** Stash uses the browser's `@view-transition` with a persistent header.

## Things that looked good in a screenshot but are risky
- Long stretches with no text (andreimoise.ai's tunnel is roughly 700-1,000px of scrolling).
- Text that is hard to read while it fades in or out.
- First screens that never say what is offered.
- Heavy WebGL for a page whose job is clarity; load time was not measured.
- An all-dark glowing palette.

## Possible mapping to the Arcturus plan (suggestions, not decisions)
- **Home:** "you're here for a reason" as three accordion cards (pattern 2), then recent posts as an index list (stash), a short proof strip, and the call to action.
- **Each reason page:** pain, solution, proof as pinned scenes (pattern 1), then filtered posts, then the call to action.
- **Calls to action everywhere:** elespacio-style hover feedback and a custom cursor.
- **Blog:** stash-style list with category addresses per reason.
- Keep it simple: use one or two of these patterns, not all of them.

## Not what John wanted
Dense, tabular technical explainers (Transformer Explainer at poloclub.github.io, The Anatomy of an LLM at royvanrijn.com, ciechanow.ski). They teach, but they are not engaging in the way John means.

## Open items
- `decimals.co` (pasted twice by John) has not been analyzed.
- John said some pages on a1.gallery were compelling (scroll-based, hover makes the UI move and invites a click); none from there have been picked or analyzed yet.
- Mamuso's hover wiggle needs a real mouse or a screen recording.
- Elespacio's cursor-following elements in the work slider were not inspected.
- None of this has been checked on phones, with reduced motion, or for load time.
- Sources and candidates: `sources.md`.
