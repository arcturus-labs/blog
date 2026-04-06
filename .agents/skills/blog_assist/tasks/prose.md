# Prose conversion

Convert the outline to finished prose, one section at a time, editing directly in the file.

## Setup

The target file lives at `docs/blog/posts/<post-slug>.md`. Create it if it doesn't exist yet, using the standard MkDocs frontmatter (look at an existing post for the template – e.g. `docs/blog/posts/Roaming_RAG.md`). Mark it `draft: true` until final touches.

## Style

Before writing, read `docs/blog/posts/Roaming_RAG.md` and `docs/blog/posts/cut_the_chit_chat_with_artifacts.md` if you haven't recently. Match that tone:
- Direct openings – no slow wind-up
- Technical clarity without jargon for its own sake
- Short paragraphs
- Occasional wit (usually drawn from John's dense outline), but never forced
- Concrete examples, honest practitioner perspective
- Not corporate, not marketing

Use ` – ` (space–en-dash–space) for prose dashes. Never `—` (em dash).

## Process

- Convert one section at a time, top to bottom, unless John directs otherwise.
- Edit directly in the file – don't paste into chat. Let John review the file.
- After each section, stop and wait for John to react before moving on.

## Rules

- Preserve every substantive claim. Don't drop or dilute points.
- Don't add new claims, statistics, or anecdotes not implied by the outline. Connective tissue is fine.
- Keep John's terminology and examples. Don't substitute your own without asking.
- Mix sentence lengths. Use italics sparingly for emphasis.
- If the outline has a bullet list that belongs as a list in the final post, keep it as a list.
- Angle-bracket notes like `<link to original paper>` or `<add example here>` are inline instructions to the agent. Handle them if you can (web search, finding a link, drafting an example). If they require something only John can do (a personal anecdote, a specific link, an image), ask John about it at the point when you're dealing with that text.

## Reserve chat for

Meta questions: ambiguous inline instructions, structural decisions, angle-bracket tasks that need John's input. Everything else: just edit the file.
