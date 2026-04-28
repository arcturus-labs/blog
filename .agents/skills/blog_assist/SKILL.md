---
name: blog-assist
description: Helps author, polish, publish, promote, and send newsletters for Arcturus Labs technical blog posts. Use when John is brainstorming, outlining, reviewing, drafting prose, generating blog images, doing final touches, creating LinkedIn/Twitter/X/Reddit promotion copy, posting approved Reddit drafts, or preparing a Kit newsletter.
---

# Blog Assist

John Berryman is an independent AI consultant at Arcturus Labs. His blog shares hard-won, practitioner-level insight on AI engineering and product development – not marketing content, not hot takes, not abstract opinion. The audience is technically literate: engineers, PMs, and technical leaders who want to understand how things actually work.

## Quick Start

Infer the current phase from context. If a task is active, read the matching reference before doing the work.

- Brainstorming: read [brainstorming.md](references/brainstorming.md)
- Outlining: read [outlining.md](references/outlining.md)
- Reviewing an outline: read [reviewing-outline.md](references/reviewing-outline.md)
- Writing prose: read [prose.md](references/prose.md)
- Images: read [images.md](references/images.md)
- Final touches: read [final-touches.md](references/final-touches.md)
- Social promotion: read [social-media.md](references/social-media.md)
- Newsletter: read [send-newsletter.md](references/send-newsletter.md)

## Promotion Rule

When advertising a blog post, draft LinkedIn, Twitter/X, and Reddit copy. For Reddit:

1. Use post frontmatter dates to identify the newest post when John asks for "latest" or "most recent".
2. Recommend subreddits based on the post topic and subreddit norms.
3. Draft subreddit-specific text posts or link posts.
4. Ask John whether the drafts are good before posting.
5. Only after explicit approval, use [post_to_reddit.py](scripts/post_to_reddit.py) to submit approved drafts.
6. After submitting, report the live Reddit post links in chat.
7. After reporting links, remind John that posts can be AI/AutoModerator filtered and should be manually checked.

For all ad copy (LinkedIn, Twitter/X, Reddit), if it fits naturally, end with a short question that invites discussion and comments.

## Meta guidance

- Don't rush John between phases. Let him set the direction.
- When he seems to be wrapping up a phase, briefly surface what comes next – one sentence, not a lecture.
- It's normal to loop between phases. Roll with it.
