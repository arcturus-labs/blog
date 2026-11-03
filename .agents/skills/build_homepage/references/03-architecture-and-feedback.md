# 03 — Straw men, critique, and decision tracking

## Build enough to get useful reactions

A rough prototype makes abstract preferences discussable. Use actual navigation, short sample copy, representative proof, and deliberately provisional assets. Don't polish an unapproved message into a finished design. Track invented scenarios and technical limitations in the working docs; never let a mock metric masquerade as client evidence. Don't litter the visitor-facing page with subtle “preview only” or generic fictional-interface disclaimers that can accidentally survive publication. Required disclosures and truthful form feedback are different from placeholder clutter.

For this project:
- Home: opening → three paths → blog transition/posts → proof/videos → booking/subscription.
- Story: opening → problem sequence → solution sequence → proof → conversion. Alternate-path invitations were tried and later removed because they distracted from the argument; don't restore them automatically.
- Story-page related posts and videos were originally planned, then deferred because there wasn't sufficiently topical material. Keep them on the homepage where appropriate.

## Run separate review passes

1. Structure and basic visual direction.
2. Content and evidence, one page at a time.
3. Graphics/composition.
4. Assembly and fine interaction polish.

These overlap, but don't answer copy criticism with more animation. If asked only to capture feedback, update documents—not the site.

## Record feedback for a future agent

`to-dos.md` is the actionable backlog. Organize by:
- Shared across all pages.
- Homepage.
- Shared story-page structure.
- Each individual page.
- Future Work.
- Launch checks.

Capture exact phrases the owner likes/dislikes, alternatives that remain brainstorming, positive constraints to preserve, provided factual corrections, and what changed from earlier direction. Use checkboxes honestly; stale historical requests aren't proof that an item remains undone.

Use `homepage/research/website_copy/` for initial proposed text, `homepage/research/content_research/` for evidence, and graphics briefs for scene specifications. Once implemented, maintain a complete annotation-friendly `copy.md` inside the active draft, with source links and editorial labels distinguished from visible text. Say whether it mirrors the HTML or contains approved-but-unimplemented revisions. Link rather than duplicate full content across files. Update the main README when the document map changes. Do not create a new memo for routine conversation without a reason.

## Keep iteration and task states explicit

- Create a new `draft_site_N/` when the owner asks for a new iteration; otherwise stay in the active draft. Preserve earlier drafts rather than silently overwriting comparisons.
- Record **considered → approved → implemented → verified → committed/pushed** separately. “Lock it in” settles wording; it need not mean the site was edited. A request to capture a backlog is not a request to implement it.
- Bank liked alternatives and question variants once, then point to the current choice. Exact later wording and line breaks supersede the older “final” choice.
- Reconcile superseded tasks instead of keeping contradictory instructions active. Check off only what actually exists, scoped to the page/draft; doing one story page does not complete all shared-page tasks.
- When interrupted, inspect files and git before claiming what was or wasn't done. Finish outstanding authorized requests without repeatedly asking for permission already given.
- Keep reports concise and factual. Do not narrate internal planning or failed string-matching mechanics as if they were useful progress updates.

## Preserve these design constraints

- Semantic HTML for real content; decorative canvas can sit behind it.
- Full-page sky stays decorative. Current preference is continuous stars with depth-based scroll parallax, fading into dawn near the bottom; an earlier problem/solution-dependent darkening was rejected.
- Stable outline; multiple moments may share a highlighted heading.
- Extra dwell after homepage choices become visible; don't immediately scroll them away.
- Responsive/narrow layouts; simplified mobile background only if needed and straightforward.
- No vertical-scroll hijacking for horizontal video carousels.
- No manual “Pause motion” controls; retain reduced-motion accommodations. Fade scroll prompts continuously with scroll offset rather than abruptly hiding them.
- Pinning/dwell is a behavior, not a redesign instruction. Preserve liked type sizes, book sizes, column ratios and spacing unless the owner asks otherwise. Confirm the scope of “this whole scene”: a heading plus books/quotes is not just the heading.

## Gate

Before writing final copy or generating art, identify which structure is agreed and which parts are still deliberately rough. New feedback can supersede the prototype without requiring immediate implementation.
