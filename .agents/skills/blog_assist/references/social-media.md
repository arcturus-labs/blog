# Social promotion

Once the post is published (or nearly so), draft social posts for LinkedIn, Twitter/X, and Reddit.

## General principles

The audience is technically literate. They can smell a marketing post in two words and will scroll past. The goal is to surface the genuine insight from the post in a way that makes someone stop and think "wait, I want to read that."

John's voice is casual, direct, and practitioner-level. He shows people how to do neat things with AI. He is pragmatic and humble - not a hype fighter, not a thought leader selling a brand.

- No emoji parade. One or two max, only if they genuinely add something.
- No salesy language ("groundbreaking," "game-changing," "thrilled to share," "way easier than the hype suggests").
- Don't frame posts as debunking or fighting hype - that itself reads as hype.
- Casual and specific beats polished and vague.
- The first line or two must work as a standalone hook - that's what shows before the fold on both platforms.
- The hook should be specific, not vague. Name the thing. Name the tension. Don't lead with an abstract observation.

## Post structure

```
[Short, punchy hook - 1-2 lines max. Something that names a real tension or surprising fact.]

[1-3 short paragraphs of substance: the core insight, what makes this post worth reading,
maybe a specific detail or concrete example that teases without giving everything away.]

[Link to post]
```

The body paragraphs can briefly describe what the post covers and what the reader will get out of it. Two or three sentences is plenty. Don't summarize the whole post - leave something to discover. The goal is to make someone curious enough to click, not to give them a reason not to.

Use ` - ` (space-hyphen-space) for prose dashes. Never em dashes.

If it fits naturally, end the post with a short question that invites reader commentary. Make it personal and practical - ask about their situation, not a hypothetical about "most teams" or "the industry." Bad: "What level do you think most teams get stuck at?" Good: "Where does your stack sit today - and what's the next step you'd actually take?"

## Draft in chat

Generate LinkedIn and Twitter/X posts directly in the conversation for John to review and edit. Twitter will naturally compress to a tighter version of the same structure; LinkedIn can breathe a little more.

**REQUIRED: append all drafts to the blog post file.**
After showing drafts in chat, immediately append them to the bottom of the corresponding blog post inside a hidden HTML comment. Do this before asking for approval – John reviews and edits the drafts in-file, not just in chat. Do this for every platform (LinkedIn, Twitter/X, Reddit, Bluesky). Keep the comment block updated as drafts evolve.

Format:
```
<!--
POST_URL: https://arcturus-labs.com/blog/...
HERO_IMAGE: https://arcturus-labs.com/blog/assets/.../hero.jpg

=== LINKEDIN ===
...

=== TWITTER/X ===
...

=== BLUESKY (N chars) ===
...

=== REDDIT: r/subreddit (text post) ===
TITLE: ...
...
-->
```

## Reddit

Also prepare Reddit promotion:

- Identify the newest post by frontmatter `date`, not file modification time.
- Recommend subreddits that match the post's real topic and likely audience.
- Read or search subreddit rules before recommending an actual post.
- Draft subreddit-specific posts. Prefer discussion-first text posts; use link posts only where normal for the subreddit.
- Titles: say what the thing is, succinctly. No "wrote up", no "here's a...", no listicle framing. Sound like a person describing something, not a marketer naming a content piece. Bad: "Wrote up how to add agentic AI to search". Bad: "A 4-level path to agentic search - here's what I learned". Good: "Incrementally adding agentic AI to an existing keyword search app".
- Body: lead with substance. Sound like a person sharing something they built or learned. Don't open with "I wrote a blog post about..." - Reddit can smell promotion instantly.
- Ask John if the Reddit drafts are good before posting.
- Do not submit anything until John explicitly approves.

Before submitting, check whether the target subreddit requires post flair:

```bash
python .agents/skills/blog_assist/scripts/post_to_reddit.py --list-flairs SUBREDDIT
```

If flair is required, pick the most appropriate one and include `flair_id` in the post JSON.

Approved Reddit posts are submitted with a JSON blob argument:

```bash
python .agents/skills/blog_assist/scripts/post_to_reddit.py '{"posts":[{"subreddit":"AI_Agents","kind":"self","title":"...","selftext":"...","flair_id":"optional-flair-uuid"}]}'
```

After posting:

- Share each submitted Reddit URL in chat so John has direct links.
- Remind John that Reddit AI/AutoModerator filtering can remove or throttle posts, so he should manually verify each submission.

If Reddit credentials fail or are missing, explain setup again:

1. Create a script app at `https://www.reddit.com/prefs/apps`.
2. Add `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`, `REDDIT_PASSWORD`, `REDDIT_USER_AGENT`, and `REDDIT_REDIRECT_URI` to `.env`.
3. Keep `.env` gitignored.
4. Use user-context credentials from the same app/session and retry.

## Bluesky

Bluesky posts are submitted with a JSON blob argument and should include text, link, and hero image:

```bash
python .agents/skills/blog_assist/scripts/post_to_bluesky.py '{"posts":[{"text":"... https://arcturus-labs.com/...","image_url":"https://arcturus-labs.com/blog/assets/.../hero.jpg","image_alt":"..."}]}'
```

Notes:

- The script enforces a 300 character max and errors if too long.
- The script auto-adds link facets for URLs.
- The script always embeds one image and errors if image is missing or too large.

## Twitter/X

Twitter/X posts are submitted with a JSON blob argument and can include an image:

```bash
python .agents/skills/blog_assist/scripts/post_to_twitter.py '{"posts":[{"text":"... https://arcturus-labs.com/...","image_url":"https://arcturus-labs.com/blog/assets/.../hero.jpg"}]}'
```

Required `.env` variables:

- `X_CONSUMER_KEY`
- `X_SECRET_KEY`
- `X_ACCESS_TOKEN`
- `X_ACCESS_TOKEN_SECRET`
- `X_USERNAME`

Notes:

- This uses OAuth1 user-context tokens and requires app `Read and write` permissions.
- All four X credentials must come from the same app.
- The script enforces a max text length and returns a clear error if too long.
- Link + image posting should be preferred for blog promotion.

After posting to Bluesky or X:

- Share each submitted URL in chat so John has direct links.
- Remind John to manually verify post rendering and visibility.

## Reminder: manual community shares

After drafting the social posts, remind John to manually share in these communities (copy-paste the LinkedIn copy, lightly adapted if needed):

**Slack**
- [Search Relevance — #blogs-papers-books](https://relevancy.slack.com/archives/CA7U4PTGS)
- [Tribe AI — #be-shameless](https://tribeai.slack.com/archives/C0390USJVC2)
- [Nashville Developer — #ai](https://nashdev.slack.com/archives/C04H3UX5A8J)

**Discord**
- [Build with AI — #look-what-i-built](https://discord.com/channels/1324240687641657484/1468425992992460911)
- [AGI Ventures Canada — #promote-your-work](https://discord.com/channels/1167423028553056268/1193518490464821258)

## Reminder: individual outreach

After the community shares, remind John to think about specific people who might find the post genuinely useful - collaborators, past colleagues, anyone mentioned in or relevant to the post - and reach out to them directly with a personal note and link.
