# Arcturus Labs website: brainstorming dump

Dumping ground for everything discussed so far. John's curated checklist lives in `john_notes.md`.
Status: ideas only; nothing decided as final. Nothing built.

## 1. Purpose and goals

- Rebuild site around **community, content, and John's vision for AI products** (Strategy 2026-09-25 milestone)
- Primary conversions:
  - **Contact John**
  - **Subscribe** (email)
- Wider aims: grow community, support consulting, show credibility
- Old site problem: "I don't know what the heck he sells" (menu confusion)
- Contact form got lots of spam
  - Open question: plain email vs. form
  - Options: `mailto:` (scraped by bots, needs mail client) vs. form with honeypot or Cloudflare Turnstile
  - Idea: form with guiding fields ("What are you working on?", which topic)
- Subscribe side: vault has a Kit (ConvertKit) note to check later

## 2. John's three threads

Core Competencies note gives three main areas, plus a supporting one. John's priority order (most to least):

1. **Agentic web / AI UX**: most interested; wants to draw people here
   - Personal agents joining products and environments; people + agents working together
   - Environment-aware, environment-capable agents
   - Beyond websites: native apps, mobile, physical places, events, devices/IoT, people
   - Techniques: agent-friendly docs, llms.txt, discoverable skills, WebMCP, MCP
   - Learning gaps: agent SEO, WebMCP limits, chat-engine experiences, MCP discovery
2. **Business workflows / virtuous cycle**: also interesting
   - Capture expert knowledge, reduce toil, expert review, evals, earned autonomy
   - "Brain transfer" framing from the website note
3. **Software factories**: can help, but *not core expertise*
   - Knows several companies' approaches, can help those companies
   - Learning gaps: team-level operating model, CI/CD and QA, independent verification
- *Agent internals and portability*: supporting context, not a main offer

### Pain points (visitor's fear)

- **Agentic web:** web "goes dark"; agents answer, nobody visits. How do companies pull people into their curated experience? How to stay engaging when plain pages feel boring?
- **Workflows:** experts burn hours on tasks AI clearly can do; need it done dependably and efficiently
- **Software factories:** every company invents its own approach; quality and coordination suffer

### Steps per capability (from Core Competencies)

- Each path has its own steps; steps could be the story's scenes
- Agentic web: make product legible to agents, publish skills/tools, give assistant page context, keep person in control
- Workflows: find the work, interview the expert, review output, turn corrections into evals, earn autonomy
- Software factories: experiment, encode what works, decompose/delegate, verify, evolve as a team
- Aim for 4-5 steps each, written as outcomes for the visitor ("expert's judgment written down so AI can use it")
- **Same step structure on every page**, so pages feel like siblings

## 3. Site structure

- One homepage, three storylines, each with its **own URL** (e.g. `/agentic-web`, `/workflows`, `/software-factories`)
  - Reasons: blog/talk/social links point to the right story; clear topic for search and agents; tailored page per prospect; separate `llms.txt` entries later
- **Default** landing story: Agentic Web
- **Fixed shell** shared across all pages:
  - Header, visual identity, proof, ways to work together, subscribe/contact
- **Balance matters.** John rejected "unequal weight"
  - All three paths get the same structure, length, and treatment
  - Build Agentic Web **first** as the working template, then reuse for the others
- **One unifying statement:** "What does John Berryman do?" as one thing, manifested in three paths
  - Write after the competitor survey
  - Core Competencies progression may help: understand agents, build with them, dependable workflows, rethink how people use products
- Avoid looking scattered: shared shell, one umbrella sentence, matching structure

## 4. Homepage interaction idea

- Top of page asks a **question**, visitor answers by choosing a problem
  - Candidate: "What's making your week harder?" / "Why are you here?" / "Why are you having a bad day?"
  - Candidate answers:
    - Customers asking AI instead of visiting our product
    - Experts buried in work AI could do; don't trust it yet
    - Shipping with agents; process is a mess
    - (maybe) "Just show me what you're working on" for non-buyers
- A row of labels is not enough; must be obvious how to switch
- Visual form (undecided):
  - **Not tabs**; not sure about buttons or cards
  - Maybe **images floating in space**, organic
  - Challenge: must still *look clickable* (mental note)
  - Each choice has an image of its fear
- Behavior when chosen:
  - Changes headline, imagery, and story; updates URL
  - **Animated transition** that hints other stories exist
  - Must feel like **one continuous space**, not a jump to a new place
- Escape route: some way to switch or go back without losing place (control not decided)
  - "Not what you're looking for?" idea; John likes the escape idea, needs more thought
- Page must work if visitor ignores the question and just scrolls
- Keep to 3-4 choices; use visitor language, not framework jargon
- Testimonials may not supply visitor language: many are from an earlier phase of John's consulting

## 5. Style and design

- Likes **scrollytelling** (scroll-driven storytelling)
  - Each section changes its visual environment
  - Idea: bifurcate scrollytelling at top, default to Agentic Web
- Everyone must understand what John does: clarity first
- **Avoid the generic AI look** (DesignArena: models have default styles; Anthropic = dark/glowy/purple, OpenAI = cream + italic serif, etc.)
  - Choose and write down a visual direction before generating
- Animation enhances real HTML text
  - All content readable without animation; respect reduced-motion
- Inspiration: twotimespi.dev ("simple beautiful"), Andrei's sites, "explore the CV" idea from ameliechatelain.com
- Andrei's method: prompt for "visually pleasing and alive and creative," animated scroll, 1-2 example sites; Opus 5.5 xhigh; tools Impeccable, UI Skills, Mobbin, Claude Design
  - John not sure he likes this approach as-is; wants to understand how it works, wants artistic input

## 6. Branding

- Arcturus = "keeper of the bear": bear = formidable problem, keeper = strength
- Imagery fits: stars, navigation, pathfinder
- Logo and color scheme at https://arcturus-labs.com/assets/images/ (not yet viewed)
- Branding still to figure out

## 7. Content and proof

- **Bio** (see Biographies note): lead with AI product engineering
  - Early production engineer on GitHub Copilot (completions, chat; ReAct chat agent, code-eliding)
  - Coauthor, *Prompt Engineering for LLMs* (O'Reilly)
  - Earlier: search/recommendations at Eventbrite; *Relevant Search* (Manning); US Patent Office search; GitHub code search
  - Career arc: aerospace, search, data science, prompt/AI
- **Client quotes** (unused so far; from the website note):
  - Perch Insights (Shantanu): strategic assessment, participatory experience
  - CETA (Laura): multi-agent therapist trainer
  - Peer Supply (Corey): automated workflow, research agent
  - Pending: Contentful (Maria), ISI (JC)
  - Show each person's role (CEO/CTO helps)
  - Possibly match each to a path
- **Past clients** to show as logos or names (see Accomplishments note)
- **Speaking/social proof:** Hugo, Hamel, Doug, O'Reilly, GitHub Universe, 7CTOs, podcasts (e.g., Vector, How AI is Built, TwoSetAI)
  - *The Evals that Made GitHub Copilot*; 7 Deadly Sins podcast with Hugo has ~30K views
- **Blog:** John blogs a lot; use posts as evidence per path
  - Ideas: floating subscribe link on posts; CTA at top or bottom of pages

## 8. Ways to work together

- Separate section from topics (topics = "can you help?"; engagements = "what happens if I contact you?")
- Engagements from Core Competencies:
  - Strategic assessment (stakeholder conversations, direction)
  - Advisory retainer
  - Training
  - Implementation (they own integration; John owns AI behavior)
- Existing offers in website note: 4-meeting assessment ($6,600), one-off meetings ($440/hr), retainer ($396/hr, up to 20 hrs/mo), project work (TBD)
  - Details and pricing from the older note: stale-ish, unconfirmed
- Fit signals: who benefits most (product leader, technical team with unreliable prototype, expert drowning in review work)
- Easy first step with expected outcome, not just "Contact me"
- Bridge from vision to action: e.g., prototype how customers could use a product with their agents

## 9. Agent-readiness

- Add `llms.txt`; possibly per-storyline entries
- Maybe skills or `.well-known` discovery
- Real HTML content under animations
- **WebMCP** (later, worth investigating):
  - Expose page tools so a visitor's own agent can guide them
  - Idea: agent offers curated conversation about the site (switch story, list engagements, start contact)
  - Possibly demo of John's own vision in the site
- Optional small working agent-aware demo on site; page must make sense without it

## 10. Backlog from the website note (unconfirmed, may be stale)

- Read Tim Kellogg post (domain + AI consultants replacing SaaS)
- Floating subscribe, exit-intent subscribe
- Study others: parlance-labs.com/services, gregceccarelli.com, natebjones.com, lucumr.pocoo.org/about
- Case studies from Accomplishments
- Remove friction (Jessica to help)
- Chatbot or Calendly for leads
- SEO: sitemap, robots.txt, `.well-known/agents`, `llms.txt`, Search Console review
- Move footer links to another page; link strategy review
- LinkedIn header/page updates
- Formspree already replaced (home server)

## 11. Open questions / next steps

- Survey indie consulting sites (before design)
- Branding and visual direction
- Final form of the question UI (not tabs, not buttons/cards?)
- Contact form vs email
- Unifying sentence
- Which path has the clearest "aha" visual metaphor (start with Agentic Web)
- Which companies/approaches John can speak to for software factories (watch confidentiality)
- Before-and-after results for workflows
- Which company types feel the agentic-web fear most (marketplace, publisher, SaaS, retailer)
- Whether visitor choice is remembered
- Visit Andrei's examples and tool links (not yet opened)

## 12. Agentic Web hero — candidate bank and direction

Keep the eyebrow **The agentic web**. Formula: **understandable fear (white) → confident action/resolution (gold) → short supporting text**. No periods on the two headline statements; a question retains its question mark.

Start with the buyer's recognized concern: customers move into chat, away from the company-controlled experience, reducing visibility and influence. Do not compress John's full personal-agent/shared-surface vision into the hero. Visitors do not yet have that context; the subsequent problem/solution story unfolds it. Supporting copy should invite reading, not summarize all implementation details.

Earlier “Your customers are bringing AI / Bring them in / Their trusted assistant. Your product. A better experience, together.” was rejected. “The web is going dark” was too opaque. Two-action lines (“Own the conversation / Bring them to your destination”) were explored, then a simpler fear/action pair was preferred. Repetition/context-loss is useful supporting content, not the main fear. Avoid vague “Fewer click. More ask.” or literal claims that nobody visits.

### Five candidates John liked (preserve as considered, not five approved choices)

**1 — New destination**
- Fear: **Customers are leaving your platform for chat**
- Action: **Lead them to a new destination**
- Supporting text: Meet them where the conversation starts. Draw them back to a new, modern, and more engaging experience.

**2 — New experience**
- Fear: **Customers are leaving your platform for chat**
- Action: **Lead them to a new experience**
- Supporting text: Don’t settle for supplying the answers. Shape what your customers experience next.

**3 — Take back the experience**
- Fear: **Customers are leaving your platform for chat**
- Action: **It’s time to take back the experience**
- Supporting text: Engage them in the conversation—and make your platform somewhere they want to be.

**4 — Platform as destination**
- Fear: **Your customers are moving to chat**
- Action: **Make your platform the destination**
- Supporting text: Engage customers where they are. Draw them into a new, richer experience on your platform.

**5 — Shape the experience**
- Fear: **Customers are leaving your platform for chat**
- Action: **It’s time to take back the experience**
- Supporting text: Engage with customers when the conversation starts. Bring them into an experience you shape.

### Question variants requested by John

These are additional fear/action candidates; supporting text has not been separately chosen for them.

- **Are your customers moving to chat? → It’s time to own the experience**
- **Are your customers moving to chat? → It’s time to retake the experience**
- **Are your customers moving to chat? → We can help you own the experience**

### Final hero wording — approved by John

- Eyebrow: **The agentic web**
- Fear: **Customers are moving to chat**
- Action: **Reclaim the user experience**
- Supporting text: **Engage customers when the conversation starts.**
- Supporting text: **Bring them to a new experience that you shape and own.**

Use this wording verbatim, without periods on the fear/action headlines. Implemented in `draft_site_2/agentic-web.html` and mirrored in `draft_site_2/copy.md`. John approved it after viewing desktop and skinny screenshots. Earlier candidates above stay banked as history, not active copy alternatives.

Subsequent layout experiment requested by John: keep the fear left-aligned, right-align the gold action, and center the supporting text. Wording is final; alignment is still an experiment.

Evidence caveat: these are prospect-facing problem framings, not a quantified assertion that every company has lost traffic. The body supplies bounded research and distinguishes the vision from a proven remedy.
