# Final touches

Work through these in order. The post should already be in good shape — this is about tying up loose ends, not rewriting.

## 1. Categories

Remove any placeholder categories from the YAML frontmatter, then run:

```bash
python scripts/count_blog_categories.py
```

Review the output and replace the post's categories with existing ones that fit. If a new category is genuinely needed, ask John before adding it.

## 2. Description

Rewrite the `description` field in the frontmatter. It should be:
- Matter-of-fact and specific — what is this post actually about?
- Engaging enough to make a reader curious
- Not salesy, not hype-y

One or two sentences. Don't start with "In this post…"

## 3. Include a `<!-- more -->` tag
The `<!-- more -->` tag indicates where to cut off the blog post in https://arcturus-labs.com/blog/ which lists all of the posts. Typically the cut-off is after the hero image but make sure that the text above this provides a good idea of what the content of the blog will be when the reader clicks through.

## 4. TODOs

Search the post for remaining work items:
- `<!-- ... -->` HTML comments with todos or notes
- Bulleted or inline "don't forget" reminders
- Angle-bracket placeholders like `<add example here>` or `<link to paper>`

Resolve what you can. Flag what needs John.

## 5. Spelling, grammar, and clarity

Light pass — the work is mostly done. Fix obvious errors. Tighten anything awkward. Don't rewrite paragraphs that are already working.

## 6. Section titles and post title

Read through all section headings. Do they scan well? Are any vague, redundant, or boring? Check the post title one more time against the title guidance in `tasks/reviewing-outline.md`.

## 7. Deploy
Remind John to remove the draft tag in the yaml, to commit and push, to review the blog online.
