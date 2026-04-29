# Social promotion

Once the post is published (or nearly so), draft social posts for LinkedIn, Twitter/X, and Reddit.

## General principles

The audience is technically literate. They can smell a marketing post in two words and will scroll past. The goal is to surface the genuine insight from the post in a way that makes someone stop and think "wait, I want to read that."

- No emoji parade. One or two max, only if they genuinely add something.
- No salesy language ("groundbreaking," "game-changing," "thrilled to share").
- The first line or two must work as a standalone hook - that's what shows before the fold on both platforms.
- The hook should be specific, not vague. Name the thing. Name the tension.

## Post structure

```
[Short, punchy hook - 1-2 lines max. Something that names a real tension or surprising fact.]

[1-3 short paragraphs of substance: the core insight, what makes this post worth reading,
maybe a specific detail or concrete example that teases without giving everything away.]

[Link to post]
```

The body paragraphs can briefly describe what the post covers and what the reader will get out of it. Two or three sentences is plenty. Don't summarize the whole post - leave something to discover.

Use ` - ` (space-hyphen-space) for prose dashes. Never em dashes.

If it fits naturally, end the post with a short question that invites reader commentary.

## Draft in chat

Generate LinkedIn and Twitter/X posts directly in the conversation for John to review and edit. Twitter will naturally compress to a tighter version of the same structure; LinkedIn can breathe a little more.

As part of drafting, append the platform drafts to the bottom of the corresponding blog post inside a hidden HTML/XML comment so John can review and edit in-place. Do this for every platform being drafted (LinkedIn, Twitter/X, Reddit, Bluesky). Keep this comment block updated as drafts evolve.

## Reddit

Also prepare Reddit promotion:

- Identify the newest post by frontmatter `date`, not file modification time.
- Recommend subreddits that match the post's real topic and likely audience.
- Read or search subreddit rules before recommending an actual post.
- Draft subreddit-specific posts. Prefer discussion-first text posts; use link posts only where normal for the subreddit.
- Ask John if the Reddit drafts are good before posting.
- Do not submit anything until John explicitly approves.

Approved Reddit posts are submitted with a JSON blob argument:

```bash
python .agents/skills/blog_assist/scripts/post_to_reddit.py '{"posts":[{"subreddit":"AI_Agents","kind":"self","title":"...","selftext":"..."}]}'
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

## Reminder: push to Slack

After drafting the social posts, remind John to also share the post in his Slack communities.
