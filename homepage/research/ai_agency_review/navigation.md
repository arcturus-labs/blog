# Navigation and page-to-page flow (2026-10-29)

How visitors move through each site, from a link crawl (no JavaScript executed) of up to 30-60 pages per site, plus a few inner pages read directly. The raw crawl data (several MB of JSON) was deleted to keep this folder light; to regenerate it, run `python3 -I _tools/crawl.py <start-url> <out.json> [max-pages]`, then `_tools/summarize.py <out.json>` for a short summary or `_tools/page.py <out.json> /some/path` for one page.
Crawler limits: some sites were capped (Kavita 59 pages of ~565 found; Drew 39 of ~190; Jason 40 of ~110; Datalumina 30 of ~70), so counts are samples.

## Summary: the funnel each site builds

| Site | Shape | Where the main call to action leads | Hand-offs to other places |
|---|---|---|---|
| **Matt Webb** | Home -> /made list -> project case pages -> /speaking | Nowhere obvious. Email `matt@interconnected.org` appears only inside 2 project pages. | His blog (interconnected.org) is the main link out (26 links) |
| **Rachel Woods** | Home -> bootcamp page (2 pages) | Home "Get Certified" -> bootcamp page -> "Enroll Now" on an external community platform (circle.so) | Enrollment leaves the site |
| **Allie Miller** | Hub with nav: Services, Courses, Resources, Contact | "Contact" -> /request-to-talk (short page); courses -> Maven, LinkedIn Learning, MasterClass (external); free course -> /the-ai-fast-track; /resources has ~8 free downloads | Heavy outbound to course platforms and her newsletter (beehiiv) |
| **Datalumina** (sales site) | Almost one page | Every button -> external Typeform project request | Academy sub-site (separate) |
| **Datalumina Academy** | Home -> programs (Python, Accelerator, Launchpad, Freelance) + Blog, Reviews, About | Each program page -> checkout (`/checkout/...`) or "Book My Call"; free /proposals download as lead magnet | Freelance page has 3 case studies |
| **Kavita Ganesan** (personal) | Short brand page | Newsletter -> hosted subscribe page; book -> Amazon; consulting -> her company site | Hands off to opinosis-analytics.com and aibusinesscasebook.com |
| **Kavita's company site** (Opinosis) | Large service-page tree (see below) | Nearly every service page ends in a "contact" button or form | Newsletter and book links in the footer (~115 each) |
| **Eleanor Berger** (Agentic Ventures) | Home -> 5 course pages | Each course page -> "Join the Course" on Maven (external) | Links to her personal site and Hugo's |
| **Drew Breunig** | Home -> essays -> tag pages; About; Contact | Contact is a 2-field form; email box on pages | Essays link out heavily (Wikipedia, arXiv, DSPy) |
| **Jason Liu** | Home -> Writing (34 of the sampled pages) with hub pages | None active (consulting closed); newsletter on a separate host | Investments, Books, Resume pages |

## What the crawl shows

### 1. Hub pages and "start here" lists carry the writing-led sites
- **Jason Liu:** the home page offers four "Start Here" links; the most-linked content pages are series/index pages (e.g. a context-engineering index linked from 11 pages, plus category pages such as applied-ai, personal, RAG). Readers move from one essay to related ones through series hubs.
- **Drew Breunig:** every essay links to tag pages (`/tags/ai.html` is linked from 23 pages), and every page has About and Contact in the footer. Navigation is tags and chronology, not sales.

### 2. The sales-led sites are shallow, with one exit
- **Datalumina:** the sales page is essentially a single scroll that sends every button to one Typeform.
- **Rachel Woods:** two pages, and the paid step happens elsewhere.
- **Eleanor Berger:** a catalog, each page ending in an external enrollment button.
These funnels are fast to follow but give a visitor no other route (for instance "learn more about the person").

### 3. Kavita's company site is a large SEO-style service tree
The Opinosis site's global menu lists ~20 destinations, grouped as:
- **Services:** AI Transformation Strategy, AI Readiness Assessment, AI Opportunity Discovery & Assessment, Custom AI Software Development, Data Science Consulting, Custom NLP Solutions, Private Leadership Training.
- **By industry:** healthcare, government, manufacturing.
- **By company size:** mid-sized companies, small business.
- **Resources, Publications, About Our Founder, "BOOK A 20-MINUTE C[ONSULTATION]".**
Each service page (about 1,200-3,000 words) ends in a short action: "Get an early assessment" / "Speak to an expert" / "Book a consultation" -> `/contact/`. Services cross-link to each other ("Learn more").
Observations:
- The pattern is one page per problem/service/segment. This could map onto your three storylines, but at much larger scale.
- The personal site and company site feel like two layers: personal brand on top, service catalog behind it.

### 4. Lead-magnet paths
- **Allie Miller:** `/resources` has about eight free downloads, each ending at a download page; a 5-day email course; an "Are You AI-First?" quiz (linked from the footer ~30 times).
- **Datalumina Academy:** `/proposals`, a free "proposal framework" download, is linked from the Freelance page. This is the lead magnet that feeds its paid programs.
- **Kavita:** newsletter on every page via a hosted subscribe page.
- **Rachel Woods:** free playbook template on the home page.

### 5. Where visitors get stranded or lose context
- **Matt Webb:** contact info is buried in two project pages; nothing links to it from the home page or the case pages' footers.
- **Allie Miller:** `/request-to-talk` is a ~120-word page that leads to an agency booking (CAA); advising has no page of its own.
- **Kavita:** the personal site's "Get Expert Advice" button routes to the company site's home page, which is a roundabout path.
- **Datalumina:** the single exit means a visitor who isn't ready to submit a project has nowhere else to go (aside from Academy).

### 6. Navigation size
- Tiny (0-3 items): Matt Webb, Rachel Woods, Drew Breunig, Eleanor Berger, Dave's personal site.
- Medium (5-7): Allie Miller, Kavita (personal site), Datalumina Academy.
- Large (20+ in a mega-menu): Kavita's company site.

## Ideas this raises for Arcturus (for discussion)
- Kavita's company site shows how **problem-specific service pages** each end in one action. Your three storylines could be three of these pages, with the same action at the end.
- Jason Liu's **"Start Here" list** and series hub pages are a lightweight way to guide a new reader into blog content.
- Datalumina Academy's **free proposal framework** is a good model for a lead magnet that serves buyers, not general readers.
- A site with several paths needs a **consistent exit** on every page (a subscribe or contact action) so no path strands a visitor.

## Not yet examined
- Whether menus change on mobile; what each site does on its 404 page; how deep the Opinosis case studies and blog funnels go; the inbound paths from blogs and newsletters.
