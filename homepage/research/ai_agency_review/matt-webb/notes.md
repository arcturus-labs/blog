# Matt Webb / Acts Not Facts: review notes

Reviewed 2026-10-29. Pages examined: home, /made, /made/archetype, /made/large-language-models, /made/speaking. Desktop only (1280x720); mobile not tested.
Files: `text.md` (raw page text; optional), `screenshots/01-home-fullpage-t0.png`, `screenshots/02-made-fullpage.png`.

## Above the fold (home)
- The whole homepage is one screen, no scroll. Full-bleed cyan background; white outlined Venn diagram of three circles: **AI, Embodiment, Multiplayer**. Caption in italic serif: "Fig. 1: Current interests (together and separately)."
- Bottom-left: big serif "Acts Not Facts" plus one sentence: "A vehicle for product invention via exploring and making. For hire and for collabs, big and small. From Matt Webb."
- Reads like a personal studio and a figure in a paper. It states no problem, audience, or outcome, and says only "for hire." The interests are shown, not explained.
- The circles are static. I couldn't confirm any interactivity, because the labels block pointer events on the circles (untested).

## Navigation and structure
- No menu or header nav on the homepage. Two exits: "some things we've made" (/made) and "Matt Webb" (his blog, interconnected.org).
- Hierarchy: Home -> Made (flat list of 16 projects, each with year and tags like APP, WORK, TALK, HARDWARE) -> project pages -> Speaking.
- Tiny site: about five page types. Every page links back to the home via "~ Acts Not Facts ~".

## How the offer is packaged
- There is no packaged offer. No services, process, pricing, or engagement types. "Big and small" collaboration is all it says.
- The work list is the offer: strategy talk, launch-video props for a client, apps, a hardware product.
- The strongest "service-like" text is on the BMJ page: a strategic-pathfinding approach and "happy to give it again" to leadership groups.

## Proof
- Proof is **the work itself**: 16 projects with dates, plus a long speaking history (about 35 talks/podcasts since 2022, highlights back to 2004), YouTube links, a "1M+ views" mention.
- Client names appear inside case pages (Archetype AI, BMJ, Google, Stripe, PA Consulting), often labeled "Internal." No testimonials, logos, or numbers found.
- Case pages are written in first person as short stories (problem, what I did, process) with images.

## Conversion
- **No contact path from the home page or the project list.** A crawl later found his email (`matt@interconnected.org`) only inside two project pages (`/made/yesterday`, `/made/galactic-compass`). There is no form, calendar, or newsletter signup. The main route out is his blog, interconnected.org (not reviewed).
- Implication: the site relies on reputation and inbound referral. Visitors who don't already know him have no obvious step to take.

## Voice and tone
- Quiet, confident, wry. Dry captions ("Fig. 1"), short declarative sentences ("Communicating new technology is hard."), plain first person on case pages. Little marketing language.

## Agent-readiness
- Server: Cloudflare. robots.txt exists but only contains Cloudflare's content-signals preamble (no actual rules, as far as I could tell).
- 404 for: sitemap.xml, llms.txt, llms-full.txt, /.well-known/agent-skills/index.json, /.well-known/mcp.json, /.well-known/ai-plugin.json.
- No JSON-LD on /made. Open Graph and Twitter-card tags are present, including a generated image endpoint (/api/og).
- Built as a server-rendered JS app (Tanstack-style): the fetch tool judged the home page incomplete, but the content is in the HTML. Page text is mostly readable by agents.

## Freshness
- Mixed: footer says (c) 2024, but "Yesterday (2026)" is on the list and speaking history includes Sep 2026 upcoming and Jul 2026 past. Content is current; the footer is stale.

## Takeaways relevant to Arcturus
- Strong example of **personality-first minimalism**: proof through work and talks, almost no marketing copy.
- It trades conversion for taste. The lack of a contact path would be a mistake for our goals.
- The Venn-of-interests idea echoes our three-paths structure, but nothing is clickable or explained there.
- Case pages as short stories with images are a model for our proof.
- Untested: mobile layout, circle interactivity, `/made/yesterday` and other project pages, his blog.
