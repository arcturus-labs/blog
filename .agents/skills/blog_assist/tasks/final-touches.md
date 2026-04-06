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

**If the title changes**, also update:
- The post filename — it should be a kebab-case slug of the title (e.g. `the-ai-product-era-youre-building-for-might-already-be-over.md`)
- The assets directory — `docs/blog/posts/assets/<slug>/` should match the post slug
- All image references inside the post that point to that assets directory

## 7. Social sharing meta tags

The `overrides/main.html` template generates `og:image` and `twitter:image` from `page.meta.image`. Add an `image:` field to the frontmatter pointing to the hero image:

```yaml
image: /blog/posts/assets/<post-slug>/hero.jpg
```

The path must be absolute from the site root (starts with `/`). The template prepends `site_url` to build the full URL.

Verify it works by serving the site and checking the meta tags:

```bash
curl -s http://127.0.0.1:8000/blog/YYYY/MM/DD/<post-slug>/ | grep -E 'og:image|twitter:image'
```

Both tags should contain the full URL to the image, not an empty string.

The `title` and `description` frontmatter fields are already used for `og:title`/`twitter:title` and `og:description`/`twitter:description` respectively — no extra fields needed for those.

## 8. Deploy
Remind John to remove the draft tag in the yaml, to commit and push, to review the blog online.
