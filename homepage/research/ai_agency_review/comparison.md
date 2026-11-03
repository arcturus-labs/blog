# Website review: comparison (2026-10-29)

Eight sites, desktop view only (1280px). Mobile, deeper inner pages, and blogs were mostly not reviewed. Page-to-page flow is in `navigation.md`. Per-site details are in each folder (`notes.md`; `text.md` is raw page text and optional; `screenshots/`). The agent-readiness results are summarized in the table below; the raw probes were deleted and can be regenerated with `_tools/probe.sh <site-url>`.
Caveat: probes on `ai.intellectronica.net` / `agentic-ventures.com` return 200 HTML for every path, so only robots.txt and sitemap.xml there are real files.

## At a glance

| Site | Type | Above-the-fold message | Offer packaging | Proof | Conversion |
|---|---|---|---|---|---|
| **Matt Webb** (Acts Not Facts) | Design/invention studio | 3 labeled circles + "for hire" | None | Work list, talks | Almost none (email buried in 2 project pages) |
| **Rachel Woods** (AI Exchange) | Training company | "Future of work runs on AI playbooks." | One $3,000 certification + free template | Press logos, 20+ reviews (no roles) | Strong: 3 email captures |
| **Allie K. Miller** | Celebrity advisor/speaker | Name + "AI Business Leader and International Speaker" | Speaking, advising (vague), courses, free email course | Best credential stack (Time 100, Fortune 500 clients, logos) | Contact button + free course |
| **Dave Ebbelaar** (Datalumina) | Productized dev shop | "Blazing fast builds for AI-forward companies" | 2-week MVP sprint, 2 clients/month | Named roles, 38%/43% results | **Strongest**: one repeated CTA |
| **Kavita Ganesan** | Executive AI advisor/author | "Strategic AI Integration to Corporations and the Boardroom" | "Four ways to work together" | Employers, awards; one quote | Newsletter + contact page |
| **Eleanor Berger** (Agentic Ventures) | Course storefront | Brand name + subscribe | 5 course cards | Almost none | Email subscribe |
| **Drew Breunig** | Writer / company CEO | Photo + one-sentence intro | None | The writing itself | Email box + contact form |
| **Jason Liu** | Ex-consultant, now OpenAI | Current job + topics | Closed | Past client names, Instructor, archives | Newsletter |

## Patterns that seem to work

1. **One clear action, repeated.** Datalumina asks for one thing (submit a project request) in the nav, hero, and closing block. Rachel Woods repeats an email capture three times. Sites without a visible action (Matt Webb) leave interested visitors with nowhere to go.
2. **Say who it's for in the first screen.** Datalumina ("AI-forward companies") and Kavita ("Corporations and the Boardroom") do; Matt Webb, Drew Breunig, and Agentic Ventures don't.
3. **Time-boxed, productized offers** (2-week sprint, $3,000 certification, "Four ways to work together") are easier to understand than "I help with AI."
4. **Testimonials with name, role, and company** (Datalumina: "Founder, Crypto Insiders"; "CTO, Telnet srl") land harder than first-name-and-initial reviews (AI Exchange).
5. **Numbers help.** Datalumina's 38% support-cost savings, 2M+ visitors, and 43% cost reduction are the most concrete proof across all eight sites.
6. **Pain vs. promise.** Datalumina's "You don't have to... / Instead you could..." contrast box is a concrete model for your "fear" framing.
7. **Named methods/vocabulary** (CRAFT, playbooks, "Prompt Debt," "Context Inertia") make the brand memorable.
8. **A free lead magnet** (playbook template, 5-day email course) drives the email list for Rachel Woods and Allie Miller.
9. **Credentials in a stack, not a wall.** Allie's and Kavita's About sections are long walls of awards; skimmable logos or numbers would serve them better.
10. **Writing is the proof for the quiet sites** (Drew Breunig, Jason Liu). This is the Simon-Willison-style pattern you ruled out as a primary strategy.

## Weaknesses to avoid

- No visible contact or next step (Matt Webb; his email appears only inside two project pages).
- Pitch with no audience and no problem (several).
- Advising described in one vague paragraph with no format, price, or first step (Allie).
- Brand scattered across three domains (Kavita: personal, company, book).
- Generic dark, glowing "AI" look (Datalumina). It is clear, but it is the look you want to avoid.

## Visual styles seen

- Neo-brutalist yellow with thick black boxes (Agentic Ventures)
- Soft pastel with a mascot (AI Exchange)
- Dark navy glow (Datalumina)
- Full-bleed speaker photo (Allie)
- Maroon/cream editorial (Kavita)
- Serif text on white, photo hero (Drew)
- Docs-site default (Jason)
- Plain cyan diagram (Matt Webb)

Only Matt Webb uses diagram/figure imagery as the hero, which is the nearest to your "top-down worldview" idea.

## Agent-readiness scoreboard

| Site | llms.txt | sitemap | Markdown mirrors | JSON-LD | Notes |
|---|---|---|---|---|---|
| Drew Breunig | **Yes (rich)** | Yes | **Yes (.md per post)** | Yes | Best example |
| Dave Ebbelaar (personal) | **Yes** | Yes | No | Not checked | RSS and llms.txt linked in footer |
| Kavita Ganesan | No | Yes | No | Yes | |
| Allie K. Miller | No | Yes | No | Not checked | Squarespace robots lists AI crawlers |
| Datalumina | No | Yes | No | Not checked | |
| Jason Liu | No | Yes | No | No | |
| Matt Webb | No | No | No | No | Cloudflare content-signals robots |
| Rachel Woods | No | No | No | No | |
| Agentic Ventures | not real | Yes | No | No | |

None of the eight has `.well-known` agent skills/MCP files, and none showed WebMCP tools. An Arcturus site that does would stand out immediately.

## Implications for the Arcturus site (for discussion, not decisions)

- **Offer clarity + one repeated action** (Datalumina) combined with **named-role testimonials and numbers**.
- A **"Four ways to work together"**-style engagement menu is accepted and easy to scan (Kavita).
- A **free lead magnet** appears on both sites with the biggest lists. Worth deciding what yours is.
- **Top-down worldview hero** is uncommon; Matt Webb's circles show the idea but not the interaction or explanation.
- **Agent-readiness is a real differentiator**, and Drew Breunig's markdown-mirror approach is a concrete model.
- These are mostly **single-path** sites. A "pick your problem" homepage with three storylines would be unusual.

## Not yet done

- Mobile layouts, scroll-animation behavior, hover/interactive states.
- Inner pages (services, case studies, speaking pages) for most sites.
- Rachel Woods' bootcamp page syllabus, Datalumina Academy, Cmpnd (Drew's company), opinosis-analytics.com (Kavita's company site).
- Their blogs and newsletters.
- Quiet, referral-driven consultants with good sites (the people search engines don't surface).
