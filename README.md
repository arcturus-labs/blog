# Arcturus Labs Blog

Source for [arcturus-labs.com](https://arcturus-labs.com). Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Development

```bash
mkdocs serve   # live-reload dev server at localhost:8000
mkdocs build   # build to site/
```

## Subscription Gating

Links in blog posts can be gated behind a Kit (ConvertKit) subscription check. Tag any `<a>` with `data-gated`:

```html
<a href="https://github.com/arcturus-labs/some-repo" data-gated>this repo</a>
```

The gate is handled by a Cloudflare Worker at `kit.arcturus-labs.com/verify_subscription` (source in `subscription-worker/`). Existing subscribers get through immediately; new visitors are subscribed to the newsletter and must confirm their email first.

This uses the **Workers Free** plan only (no KV, D1, Queues, etc.). Do not enable **Workers Paid** ($5/mo) in the Cloudflare dashboard unless you intentionally want it.

See [subscription-worker/README.md](subscription-worker/README.md) for setup, deploy, and troubleshooting.

## Homepage

The homepage (`docs/index.html`) and its three story pages (`agentic-web.html`, `workflows.html`, `software-factories.html`) are generated from the draft site in `content-production/2026.10.29--Arcturus-Labs-Website/draft_site_4`. After editing the draft, re-run:

```bash
python3 -I scripts/publish_home.py   # copies pages to docs/, CSS/JS to docs/home/, images to docs/home/assets/; injects GA, canonical, Open Graph, Twitter tags
```

Do not hand-edit those four HTML files or `docs/home/`; changes are overwritten.

The "recent posts" list is filled at build time by `hooks/recent_posts.py` (five newest posts, no manual upkeep).

Tests (after `mkdocs build`): `python3 scripts/test_home.py`, and with `mkdocs serve` running, `node scripts/test_home_browser.cjs` (needs Playwright; Kit calls are mocked, no subscribers are created).
