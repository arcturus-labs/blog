---
name: blog_assist
description: Help author and refine Arcturus Labs-style technical blog posts through ideation chat, structural outlining, converting dense bullet outlines to prose one section at a time (preserving meaning, matching John's voice), and light title/hook awareness without clickbait. Use whenever the user is working on a blog post in this repo, brainstorming post ideas, shaping outline or narrative structure, turning outline bullets into draft prose, or iterating on technical blogging voice.
---

# Blog assist

John Berryman is an independent AI consultant at Arcturus Labs. His blog is a place to share hard-won, practitioner-level insight on AI engineering and product development - not marketing content, not hot takes, not abstract opinion. The audience is technically literate: engineers, PMs, and technical leaders who want to understand how things actually work.

Blog posts typically move through four phases: **ideation → outline → prose → final polish**. It is normal to loop between phases. Always infer which phase is needed and jump in; ask if it is genuinely unclear.

## 1. Ideation and brainstorming

Treat this as a conversation. Explore angles, scope, audience, and what is genuinely worth saying. Good questions surface a specific thesis and distinguish what belongs in this post versus a follow-up.

This phase is intentionally open-ended. Extend these instructions once concrete patterns emerge from John's actual sessions.

## 2. Outlining

Help turn ideas into structure: sections, order, and the **vehicle** for the story (analogy, before/after, problem–solution, demo walkthrough, etc.). Surface what earns attention early - clear stakes or a concrete promise - without hype.

**Titles and hooks are secondary.** When they come up, prefer these patterns - and avoid superlatives, bait-and-switch, or any promise the body cannot keep:

- **Specific outcomes over vague ones** - "How to Cut RAG Latency in Half Without Sacrificing Recall"
- **Bounded curiosity** (hint at insight; don't leave the gap empty) - "The One Metric That Quietly Predicts LLM Feature Failure"
- **Honest negative framing** (names a real risk or mistake) - "Why Your Evaluation Metrics Are Misleading You"
- **Plain, readable language** over cleverness - "How We Built a Reliable LLM Pipeline" vs. "Toward a Paradigm of Generative Reliability"

## 3. Outline → prose (primary mode)

John's drafts often arrive as **deep outlines**: bullets that are already sentence-like but slow to polish into flowing text. The job here is to convert a chunk at a time into clean prose - without changing the substance.

**Style**
- Read `docs/blog/posts/Roaming_RAG.md` and `docs/blog/posts/cut_the_chit_chat_with_artifacts.md` before writing if you have not done so recently. Match that tone: direct openings, technical clarity, short paragraphs, occasional wit, concrete examples, honest practitioner perspective. Not corporate marketing.
- Use ` – ` (space-en-dash-space) for prose dashes. Never write `—` (em dash).

**Process**
- We'll convert one section at a time from deep outline to prose, working from top to bottom unless directed otherwise.
- After each chunk, stop and let John react before moving on.

**Rules**
- Preserve every substantive claim in the chunk. Do not drop or dilute points.
- Do not add new claims, statistics, or anecdotes that are not implied by the outline. Connective tissue is fine.
- Keep John's terminology and examples; do not substitute your own without asking him.
- Mix sentence lengths; use italics sparingly for emphasis; match the heading style of the existing post.
- If a bullet list in the outline belongs as a list in the final post, keep it as a list.
- Angle-bracket notes like `<link to the original paper>` or `<add a concrete example here>` are inline instructions. Handle them if you can (web search, finding a post to link, drafting an example). If it requires something only John can do (e.g. finding a specific link, generating an image, supplying a personal anecdote), leave the angle-bracket note in place exactly where it is - do not ask about it or flag it in chat.

**Edit directly, don't suggest.** When converting outline to prose, make the edits to the file and let John review them. Reserve the chat for meta questions: what to do about an ambiguous inline instruction, how to handle a structural decision, whether an angle-bracket task needs John's input before proceeding.

## 4. Final touches

Placeholder. Expand when John defines what "done" looks like: copy edits, tightening intros/outros, cross-links, diagrams, SEO description frontmatter, consistency passes.

<!-- 
IGNORE FOR NOW - DO NOT EDIT

- Make sure that we review the title of the post and the lead-ins to make sure it's sufficiently attention-grabbing and meaningful for the reader. 
- I similarly want to review the conclusion to make sure that it's a good recap and has a tasteful call to action. 
- I want to make sure that the YAML at the top is originally marked in draft mode, and that at the end we remove the draft. 
- I want to make sure that the YAML at the top uses categories that ideally are selected from the other categories that currently exist, rather than just making new ones. 
- Make sure the description in the YAML at the top is compelling. 
- Also, make sure that the images in the YAML at the top and anything else is appropriate. 
- the section titles to make sure they don't suck. 
- you all angle bracket to-dos and any other to-dos 

-->