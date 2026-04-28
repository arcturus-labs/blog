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

Once John is happy with the social copy, also append the final LinkedIn and Twitter/X drafts to the bottom of the blog post inside a hidden HTML/XML comment. This keeps the launch copy next to the post without rendering on the site.

## Reddit

Also prepare Reddit promotion:

- Identify the newest post by frontmatter `date`, not file modification time.
- Recommend subreddits that match the post's real topic and likely audience.
- Read or search subreddit rules before recommending an actual post.
- Draft subreddit-specific posts. Prefer discussion-first text posts; use link posts only where normal for the subreddit.
- Ask John if the Reddit drafts are good before posting.
- Do not submit anything until John explicitly approves.

Approved Reddit drafts can be posted with `scripts/post_to_reddit.py`. Create a JSON file like:

```json
{
  "posts": [
    {
      "subreddit": "AI_Agents",
      "kind": "self",
      "title": "Are agent harnesses just the next app runtime?",
      "selftext": "Discussion-first post body here...\n\nLink: https://arcturus-labs.com/blog/YYYY/MM/DD/slug/"
    }
  ]
}
```

Preview first:

```bash
python .agents/skills/blog_assist/scripts/post_to_reddit.py reddit-drafts.json
```

Post only after approval:

```bash
python .agents/skills/blog_assist/scripts/post_to_reddit.py reddit-drafts.json --post
```

After posting:

- Share each submitted Reddit URL in chat so John has direct links.
- Remind John that Reddit AI/AutoModerator filtering can remove or throttle posts, so he should manually verify each submission.

If Reddit credentials fail or are missing, explain setup again:

1. Create a script app at `https://www.reddit.com/prefs/apps`.
2. Add `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`, `REDDIT_PASSWORD`, `REDDIT_USER_AGENT`, and `REDDIT_REDIRECT_URI` to `.env`.
3. Keep `.env` gitignored.
4. Dry-run before posting.

## Reminder: push to Slack

After drafting the social posts, remind John to also share the post in his Slack communities.
