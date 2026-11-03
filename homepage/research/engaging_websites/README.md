# Engaging websites

Research on websites with engaging, scroll-based, or interactive behavior, to inform the Arcturus Labs site. Findings come from inspecting live pages (measuring hover and scroll behavior, reading their CSS and JavaScript), not from screenshots alone.

John's favorites are the two Ponder patterns (pinned steps with scenes that play as you scroll; accordion cards with a "Try..." reveal). They are covered first in `patterns.md`.

## Where to look (in this order)
1. **`patterns.md`**: the synthesis. Start here (about 8 KB): constraints John set, the two Ponder patterns, other patterns, cross-cutting techniques, risks, a suggested mapping to the Arcturus plan, open items.
2. **`cases/`**: one measured write-up per site or section (1-4 KB each). Read the one you need.
   - `ponder-pinned-steps.md`, `ponder-accordion-cards.md` (John's favorites)
   - `elespacio-button-hover.md`, `stash-index-list.md`, `mamuso-cartridge-chooser.md`, `andrei-moise-scroll-journey.md`
3. **`method.md`**: how to interrogate a page's hover and scroll behavior (what to measure, with what scripts). Read before analyzing a new site.
4. **`sources.md`**: what was inspected, what John has asked for next, candidates, and rejected examples.

## Screenshots
`screenshots/ponder-how-it-works/` (2 frames) and `screenshots/andrei-moise/` (19 frames named by scroll position, e.g. `y3960.png`). The andrei-moise case file has a table that maps each scroll position to what appears, so you rarely need to open all the frames. Open images selectively.

## Related
- `../ai_agency_review/`: review of eight AI consulting sites (content, navigation, offers, conversion). Different question; see its README.
- `../brainstorming.md` and `../john_notes.md`: the plan these patterns are meant to serve.

## Status (2026-10-29)
Five sites inspected. Next, per John: analyze `decimals.co` and sites he finds on a1.gallery, then possibly a broader analysis of scroll-driven pages. Nothing here has been checked on phones, with reduced motion, or for load time.
