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
