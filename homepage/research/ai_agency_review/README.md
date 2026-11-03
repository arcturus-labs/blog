# AI agency review

A review of eight visible AI consulting, training, and advisory sites, done on 2026-10-29 to learn what works on them (above the fold, navigation, how the offer is packaged, proof, conversion, voice, agent-readiness, freshness) before designing the Arcturus Labs site. Desktop only (1280px); mostly home pages plus a link crawl.

Scope decision from John: base the site on **visible brands**; referral-driven consultants with quiet sites are deliberately out of scope for now. Simon Willison was excluded because his authority comes from blogging volume, not from a website.

## Where to look (in this order)

1. **`comparison.md`**: one table across all eight sites, patterns that seem to work, weaknesses to avoid, visual styles, an agent-readiness scoreboard. Start here. About 6 KB.
2. **`vs-brainstorming.md`**: the sites compared with the Arcturus brainstorming (`../brainstorming.md`), section by section, marked supports / challenges / no precedent. About 11 KB; read when you need the link to Arcturus decisions.
3. **`navigation.md`**: how visitors move between pages on each site (hubs, funnels, where people get stranded). About 7 KB.
4. **`<site>/notes.md`**: one page per site (2-4 KB), same headings every time. Read only the sites that matter to your question.
5. **`<site>/screenshots/`**: look at `*above-fold*` images first. Open images selectively.

Sites: `allie-k-miller`, `dave-ebbelaar` (personal site and Datalumina), `drew-breunig`, `eleanor-berger` (Agentic Ventures), `jason-liu`, `kavita-ganesan`, `matt-webb`, `rachel-woods`.

## What not to read

- **`<site>/text.md`**: raw captured page text. Optional. Open only to quote a site's actual copy or check its voice.
- **`_tools/`**: scripts, not content (see below).
- Screenshots named `*fullpage*` are downscaled long pages (small text); prefer the above-the-fold shots. (`rachel-woods` has only the full-page one, and `matt-webb` has short pages.)

## Deleted on purpose (to keep agents from wasting context)

Raw crawl JSON (about 2.6 MB), a raw HTML copy, raw agent-readiness probe output, a copied `llms.txt`, and several very tall screenshots. Their findings are already summarized in the files above. They can be regenerated with the scripts in `_tools/`. This folder was never committed to git before the deletions, so the originals are gone.

## `_tools/` (regenerate evidence)

- `crawl.py <start-url> <out.json> [max-pages] [extra-hosts]`: breadth-first link crawler (no JavaScript executed). Run as `python3 -I`.
- `summarize.py <crawl.json>`: short summary: sections, global menu, most-linked pages, where the main buttons lead. Use this instead of reading crawl JSON.
- `page.py <crawl.json> <path>...`: compact view of specific crawled pages.
- `probe.sh <site-url>`: checks robots.txt, sitemap, llms.txt, `.well-known` agent files, feeds, server headers, and mailto links.

## Known caveats

- `ai.intellectronica.net/eleanor` redirects to `agentic-ventures.com`, a course storefront, so it says little about her advisory work.
- Jason Liu has closed his consulting practice (he now works at OpenAI); his site is useful for lessons, not as a live consulting site.
- Kavita Ganesan's consulting site is `opinosis-analytics.com`; the home page reviewed is her personal-brand site. Her company site was seen only through the crawl.
- Matt Webb's contact email appears only inside two project pages, so earlier notes saying "no contact" were corrected.
- Counts from the crawl are samples (the crawler was capped per site).
- Not covered: mobile layouts, animation and hover behavior, inner pages beyond the sampled crawl, and the sites' blogs and newsletters. For interactivity and scroll behavior see `../engaging_websites/`.
