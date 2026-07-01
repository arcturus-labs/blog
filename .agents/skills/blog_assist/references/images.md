# Images

For blog image generation, read and follow the Gemini image generation skill:

```
.agents/skills/gemini-image-gen/SKILL.md
```

That skill covers model selection, the CLI, output directories, reference-image iteration, and how to run generation in the background.

## Placing the hero image in a post

Once the hero image is chosen:

1. Copy it to `docs/blog/posts/assets/<post-slug>/hero.jpg`.
2. Set the frontmatter `image:` field to `/blog/assets/<post-slug>/hero.jpg`.
3. Embed it inline in the post body right after the opening paragraph:

```markdown
![Alt text describing the image](./assets/<post-slug>/hero.jpg){ align=center width=100% }
```
