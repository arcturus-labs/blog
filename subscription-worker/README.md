# Subscription Worker

Cloudflare Worker that verifies Kit (ConvertKit) newsletter subscribers for gated links on [arcturus-labs.com](https://arcturus-labs.com).

**Live endpoint:** `https://kit.arcturus-labs.com/verify_subscription`

The browser never sees Kit credentials. The blog frontend (`docs/assets/scripts/custom.js`) POSTs `{ email }` here; this worker calls the Kit v3 API and returns whether to grant access.

Worker logic mirrors `stateful-objects-of-discourse/backend/app/routes/subscription/routes.py`.

## How verification works

1. `GET /v3/subscribers?email_address=...` with `CONVERTKIT_API_SECRET`
2. If `total_subscribers > 0` → `{ subscribed: true }`
3. Otherwise `POST /v3/forms/7337584/subscribe` with `CONVERTKIT_API_KEY`
4. On successful signup → `{ subscribed: false, pending: true, message: "..." }` (user must confirm email)

On success, the blog sets cookies on `arcturus-labs.com`:

| Cookie | Purpose |
|--------|---------|
| `subscription_email` | Email entered in the modal |
| `subscription_authorized` | `"true"` after Kit confirms subscription |

Cookies last 1 year, `SameSite=Strict`. Private/incognito windows have no cookies, so users go through the modal again.

Test bypass: add `?bypass-subscription` to any blog URL.

## Setup

**Prerequisites:** Cloudflare account with `arcturus-labs.com` in the zone, Node.js, Kit API Secret + API Key (Kit dashboard → Settings → Advanced).

```bash
cd subscription-worker
npm install
npx wrangler login
npx wrangler secret put CONVERTKIT_API_SECRET   # use same values as stateful-objects-of-discourse
npx wrangler secret put CONVERTKIT_API_KEY
npm run deploy
```

Wrangler creates the custom domain `kit.arcturus-labs.com` automatically (`custom_domain: true` in `wrangler.jsonc`).

## Local development

Create `.dev.vars` (gitignored):

```
CONVERTKIT_API_SECRET=...
CONVERTKIT_API_KEY=...
```

```bash
npm run dev   # http://localhost:8787
```

Point `WORKER_URL` in `docs/assets/scripts/custom.js` at `http://localhost:8787/verify_subscription` for end-to-end testing with `mkdocs serve`.

Sanity-check credentials against Kit directly:

```bash
node scripts/test-convertkit.mjs your@email.com
```

## Operations

```bash
npm run deploy          # deploy code/config changes
npx wrangler tail       # live logs (useful for Kit API errors)
npx wrangler rollback   # revert to previous version
npx wrangler secret list
```

## Cost

Workers **Free** plan only — no KV, D1, Queues, or observability bindings. 100k requests/day is plenty for this use case. Do not enable **Workers Paid** ($5/mo) unless you intentionally want it.

## Troubleshooting

| Symptom | Likely cause |
|---------|----------------|
| Works in normal browser, modal in private mode | Expected — no `subscription_authorized` cookie yet |
| "Verification service unavailable" | Bad `CONVERTKIT_API_SECRET` — re-sync from `stateful-objects-of-discourse/.env` |
| "Subscription failed" | Bad `CONVERTKIT_API_KEY` or invalid form ID |
| Subscribed email still shows pending | Email not **active** in Kit yet, or wrong address entered |
| `kit.arcturus-labs.com` unreachable | DNS still propagating — check Cloudflare dashboard → Workers → custom domains |

## Adding gated links (blog)

No worker changes needed. Tag any link in a post:

```html
<a href="https://github.com/arcturus-labs/some-repo" data-gated>this repo</a>
```

Modal styling lives in `docs/assets/stylesheets/custom.css`.

## Kit API reference

| Call | Endpoint | Auth |
|------|----------|------|
| Check subscriber | `GET /v3/subscribers?email_address=...` | `CONVERTKIT_API_SECRET` |
| Subscribe to form | `POST /v3/forms/7337584/subscribe` | `CONVERTKIT_API_KEY` |
