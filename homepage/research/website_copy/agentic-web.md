# Agentic Web — copy draft

Status: for review, not approved or implemented in HTML. This document supersedes the earlier conversational outline. Source background: [research brief](../content_research/agentic-web.md).

## Latest graphics direction

See [agentic-web-graphics.md](agentic-web-graphics.md) for John's detailed scene instructions and all eight reference screenshots in `supporting_images/`. That brief supersedes the provisional graphic directions below, especially the first two problem scenes and the solution-1 asset/discovery emphasis. References are unsanitized private working material, not publication-ready assets.

## Presentation instructions (not visible copy)

- Separate problem and solution scroll-through sections. Bold numbered headings below form each section's stable left outline.
- Each “Moment” is a separate right-side text/illustration state, advanced by scrolling. These are not visible bullet lists. Keep the relevant left heading highlighted across all its moments.
- Source numbers are small, clickable superscript links to original sources, not HTML comments or a mandatory separate footnote section. Retain source/methodology notes here for implementation.
- Graphic directions are provisional, not requests for final illustration work yet.
- Hero headline remains open. Current HTML's “The web is going dark.” needs a clearer replacement; do not treat it as approved.

## The problem

### 1. Customers are finding answers without finding you.

**Moment 1 — visible copy**

In Pew’s study, people clicked a traditional search result **8% of the time when an AI summary appeared**, versus **15% without one**.<sup>[1](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)</sup> **Nearly half the click-through rate.**

*Graphic direction:* two simple flows from search to a website, making the 8% versus 15% comparison legible. Don't depict an actual client's traffic or “visitors: 0.”

*Source guardrail:* Pew tracked 900 US adults during March 2025. Observational comparison, not proof that AI caused a given company's traffic to halve. Preserve the distinction between click-through rate and total traffic. The removed introductory sentence (“AI can answer the question...”) should not return.

### 2. You get the transaction, but lose the conversation.

**Moment 1 — visible copy**

You receive the order without understanding what the customer explored, considered, or needed.

> “The retailer loses so much context because it's outside of their realm.”<sup>[2](https://www.retaildive.com/news/retails-ai-bet-risks-data-market-share/810202/)</sup>
>
> — Nikki Baird, Aptos

*Graphic direction:* a discovery/conversation path inside an external assistant; only the order reaches the business. Show the missing context, not just missing visits.

**Moment 2 — visible copy**

> “You're giving away the customer interactions, the brand experience, all of that, and then you become like a fulfillment company.”<sup>[3](https://www.retaildive.com/news/retails-ai-bet-risks-data-market-share/810202/)</sup>
>
> — Kartik Hosanagar, Wharton

*Graphic direction:* keep the customer conversation on one side and the company reduced to order fulfillment on the other. Give the quote room to land.

*Source guardrail:* these are attributed assessments of a risk, not measured universal outcomes. Check exact wording against Retail Dive before publishing. For the Nikki quote, the surrounding passage specifically concerns missing information leading to discovery, decision, and delivery.

### 3. Your product and their assistant are isolated.

**Moment 1 — visible copy**

Their assistant has their preferences, work context, and past conversations. Your website makes them start over—with buttons and forms, or a built-in chatbot that needs everything explained again.

*Graphic direction:* an assistant with accumulated personal context separated from the product interface and its fresh chatbot. Show the person bridging the gap.

*Content guardrail:* this is the problem we propose to solve, not a universal claim about every assistant or website. Do not imply that agents literally know everything about users or that lack of personal context is the proven cause of irrelevant recommendations. Avoid anthropomorphizing the product as “knowing what it can do.”

## The solution

### 1. Make your product discoverable to agents.

**Moment 1 — visible copy**

Make your product easy for agents to find and understand—with accessible content, clear documentation, and discoverable integrations and skills.

*Graphic direction:* assistant discovers a product through readable content and clearly described capabilities. Distinguish discovery assets from the actual experience of using them in the next step.

*Research/implementation note:* agent discoverability overlaps with SEO, crawler access, and platform-specific catalogs/documentation. Do not promise rankings from llms.txt or imply a magic “agentic SEO” file is required. [Google says established SEO practices remain relevant and no special optimization is required for its AI search features](https://developers.google.com/search/docs/appearance/ai-features). [OpenAI distinguishes its crawler purposes and access controls](https://developers.openai.com/api/docs/bots). These links were located in official search extracts during this pass; verify full current documentation before publishing detailed guidance. Agentic SEO remains John's learning area, not an advertised specialty. The visible paragraph is an approach, not a measured outcome claim.

### 2. Make the experience useful wherever customers start.

**Moment 1 — visible copy**

Build tools, skills, and chat integrations that help customers explore your offering and get things done—not just read another answer.

*Graphic direction:* an interactive product experience inside a chat harness, not merely a text response.

*Optional graphic annotation, visible if used:* Zillow brings home listings and an interactive map into ChatGPT.<sup>[4](https://openai.com/index/introducing-apps-in-chatgpt/)</sup>

**Moment 2 — visible copy**

Give those integrations a clear path into your website, carrying the conversation into an experience you own.

*Graphic direction:* a deliberate handoff from chat into the relevant product view, preserving intent. The actual context-transfer mechanism and permission boundary must be designed; don't imply it is automatic or universally supported.

*Editorial decision:* this absorbs the former standalone “Bring customers into an experience you own.” It is a second moment, not another numbered heading. Keep confident language; no visible qualification about “if the website is better.” Direct to the useful product destination, not necessarily the homepage.

### 3. Build one experience for the person and their assistant.

**Moment 1 — visible copy**

Bring their trusted assistant into your product—with their preferences, work context, and past conversations. They choose what to share, without starting from scratch.

*Graphic direction:* the user's assistant and permitted personal context enter the product alongside the person. Private context remains visibly under the user's control.

**Moment 2 — visible copy**

One shared surface. The person clicks, filters, and explores. Their assistant sees those changes, acts through the same experience, and talks through what happens next.

*Graphic direction:* a shared home-search interface: a manual filter change updates results; a conversational request changes the same map/list. Make mutual visibility and the common state unmistakable, rather than two disconnected interfaces.

**Moment 3 — visible copy**

The assistant can work behind the scenes, too—searching, comparing, and bringing useful options back into view. Conversation and direct interaction become one continuous experience, on your platform.

*Graphic direction:* background searches/comparisons feed the shared visible surface; the person reviews and steers consequential actions.

*Implementation guardrail:* this is the intended experience, not a claim that all browsers already provide it. WebMCP is an enabling tool interface, not by itself personal memory, complete environment awareness, shared state synchronization, or permission management. Rook can remain unnamed; don't publicly advertise it without John's approval.

## After the story — unresolved copy

- Clear, substantial alternate-path invitations, not the current cryptic inline “Not this one?” treatment. Wording pending.
- Proof heading along the lines of “Arcturus Labs can help”; final heading pending.
- Existing books and quotes with corrected attribution, publisher-only captions, and one shared coauthorship explanation; use shared requirements in `../to-dos.md`. No new proof text drafted here.
- No related-post section or videos on story pages for now; both deferred until sufficiently relevant material exists.
- Simple booking CTA and real email subscription input; final supporting copy pending. Current booking destination remains a placeholder.

## Citation implementation

Render each `<sup>[n](URL)</sup>` notation as an actual superscript anchor in HTML, e.g. `<sup><a href="SOURCE_URL" aria-label="Source 1: Pew Research">1</a></sup>`. The Markdown link syntax inside `<sup>` may not render in every Markdown viewer; the HTML implementation must produce a working link. Numbers 2 and 3 intentionally point to the same reporting source but identify separate quotations. Do not rely on comments for attribution.
