# Agentic Web: evidence for pains and competing solutions

Research recorded: 2026-10-29. For content review of `../draft_site/agentic-web.html`, not approved website copy. This brief combines the initial pain-point research with a follow-up on solutions. Sources are linked below so another agent can check them without conversation history.

## Question and working hypothesis

John's vision: a person's own assistant carries preferences, goals, and prior context into a website or application. The environment supplies relevant state, tools, and instructions; the person and assistant work together in the product, with the person controlling actions and disclosure.

The business concern is not merely lost page views: companies may lose influence over product discovery, customer relationships, and the experience they designed. The proposed participatory solution is a hypothesis, not an established remedy.

**Bottom line:** external evidence supports reduced click-through from AI answers, retailer concerns about intermediation, demand for useful product-discovery assistance, and user concerns about privacy/control. It does not yet prove that customers want portable personal agents inside websites, or that this design preserves loyalty or improves conversion. Most evidence here concerns retail and publishing, not every B2B application.

## Evidence rules

- Separate observed behavior, self-reported preferences, executive forecasts, vendor outcome claims, technical feasibility, and our inference.
- A shipped feature is evidence of investment, not automatically demand or success. A preview announcement is weaker still.
- Preserve denominators, dates, populations, and limitations when using numbers. Associations are not causal uplift.
- Distinguish ownership of orders/support/customer records from control over discovery and the visible interface. A merchant can retain the former while an AI platform controls the latter.
- Product availability changes quickly. Recheck current documentation before publishing implementation claims. The Shopify documentation below already differs from OpenAI's original checkout announcement.

## 1. Evidence for pain points

### A. Answers can replace visits — observed, bounded evidence

**Source:** [Pew Research, July 22, 2025](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/). Full article retrieved in initial research.

- Browsing data from **900 US adults**, March 1–31, 2025.
- Traditional-result clicks occurred on **8% of visits to search pages with an AI summary**, versus **15% without one**.
- Users clicked a link within the AI summary on **1% of visits to pages containing a summary**.
- Searches differ in their likelihood of triggering summaries. This was not a randomized experiment. Researchers reconstructed search results; see the source methodology before quoting details.

Supports: users can get answers without opening a source website.
Does not support: all websites are losing customers; personal agents already replace entire product experiences; AI summaries caused a particular company's revenue decline.

**Copy implication:** say that AI is changing discovery and can reduce visits, not that "nobody visits your site."

### B. Losing control of discovery and customer context — documented concern

**Source:** [Retail Dive, “Retail’s risky AI commerce bet,” reporting on early 2026](https://www.retaildive.com/news/retails-ai-bet-risks-data-market-share/810202/). Full article retrieved.

Wharton professor Kartik Hosanagar:
> “You're giving away the customer interactions, the brand experience, all of that, and then you become like a fulfillment company.”

Aptos strategy/product executive Nikki Baird describes the risk that retailers do not receive all the context leading to discovery and a decision when that activity occurs on an external platform. Retailers are nevertheless partnering with those platforms to meet customers where they are.

**Related number:** [Deloitte's 2026 Retail Industry Global Outlook](https://www.deloitte.com/us/en/insights/industry/retail-distribution/retail-distribution-industry-outlook.html) says **81% of surveyed retail executives believe generative AI will weaken brand loyalty by 2027**. This exact finding was visible in indexed primary-source results and quoted in Retail Dive; direct page extraction returned only partial content. Check the full report's sample and wording before putting it on the website.

Supports: this is a recognized buyer concern, not just John's private theory.
Does not support: measured loss of loyalty, inevitable commoditization, or the claim that merchants lose all customer data.

### C. Finding and choosing suitable products is an opportunity — survey and usability evidence

**Source:** [Nosto/Censuswide consumer research](https://www.nosto.com/blog/agentic-commerce-ai-assisstants-research/). Full article retrieved.

- Vendor-commissioned survey of a nationally representative **2,000 US/UK adults**, collected **November 13–17, 2025**.
- **34%** said they had tried shopping with a conversational AI assistant, including retailer tools or interfaces such as ChatGPT/Gemini.
- **66%** combines people who had tried it with those open to trying it. It is **not** an adoption rate.
- Among people who had tried it, **33%** chose comparing/choosing products as the area where AI could have greatest impact; **25%** chose finding products.
- Among early adopters who received irrelevant AI product suggestions, **69%** reported giving up and searching elsewhere. This is not 69% of all shoppers or observed revenue loss.

**Supporting usability source:** [Baymard, product lists/filtering research](https://baymard.com/research/ecommerce-product-lists), and [filter UI guidance](https://baymard.com/blog/ecommerce-filter-ui). Pages retrieved. Baymard documents practical difficulty with finding products through filtering and sorting. Do not infer that conversational AI solves these difficulties: better conventional interface design is also a solution.

Supports: relevance, product discovery, and decision support are real needs. A conversational interface can still fail them.
Does not support: personal agents necessarily outperform good search, filters, or retailer assistants.

### D. Privacy and control matter — stated concerns

Same Nosto/Censuswide study:
- **24%** identified concern about data handling as the reason most likely to make them stop using AI shopping.
- **21%** identified AI making decisions without their input.

Supports: make user control and disclosure explicit in the design.
Does not establish: which permission UX works best, or that customers want to share a personal agent's full context with merchants.

### E. Bringing an existing personal agent into a product — still unvalidated

We have not found direct comparative evidence that customers resent leaving a persistent personal assistant behind, or that they prefer that assistant to a site's own assistant.

Relevant but indirect: in Nosto's early-adopter subgroup, **46% preferred access through a retailer's search bar**, versus **41% through an on-site chatbot**. This is evidence about placement of assistance, not portability or continuity of an existing agent.

Treat "don't make customers choose between your product and their assistant" as a compelling proposition to test, not a documented universal complaint.

### F. Counterevidence: AI can send valuable visitors

[Adobe's March 2026 retail analysis](https://business.adobe.com/blog/ai-traffic-surge-retail-sites-not-machine-readable) reports AI-referred traffic converting **42% better than non-AI traffic**. This finding was located in primary-source search results; the article fetch timed out. Recheck the report and channel definitions before using the number publicly.

This is a comparison of visitors who arrive, not proof of incremental conversion caused by AI. Higher-intent users may self-select. It also says nothing by itself about net traffic or revenue changes.

Implication: do not tell a one-way extinction story. AI can both substitute for visits and become an acquisition channel.

## 2. What people are building or reaching for

### A. Structured tools inside the website — closest technical match

**Source:** [Chrome for Developers: WebMCP early preview, February 10, 2026](https://developer.chrome.com/blog/webmcp-epp). Full announcement retrieved.

WebMCP proposes declarative tools in HTML forms and imperative tools in JavaScript. Google's stated aim is faster, more reliable agent actions than raw DOM interaction. Examples include support tickets, ecommerce configuration/checkout, and travel search/booking.

- **Match:** websites expose capabilities to browser agents, so actions can coexist with the user's page experience.
- **Not established:** broad support, automatic transfer of personal memory, a complete environment-awareness solution, or improved customer relationships/conversion.
- **Maturity evidence:** this source announces an early preview for prototyping. Check [current documentation](https://developer.chrome.com/docs/ai/webmcp) before promising production support.
- **Outcome evidence:** no independent comparative business-outcome data located in this pass. Google's reliability claims are a design rationale, not a measured result supplied by this article.

### B. Retailer-owned assistants in existing products — partial match, different ownership

**Source:** [Amazon's Rufus product announcement](https://www.aboutamazon.com/news/retail/amazon-rufus-ai-assistant-personalized-shopping-features). Full page retrieved; 2025 announcement context corroborated by contemporaneous reporting.

Amazon reports **more than 250 million customers used Rufus that year**, and customers using it were **over 60% more likely to purchase during that shopping trip**. It describes help with broad shopping needs, comparisons, detailed product questions, and personalization inside its app/site.

- **Match:** conversational help alongside an existing shopping interface, using product knowledge and context.
- **Difference:** the retailer's assistant, not necessarily the user's portable personal agent.
- **Caveat:** vendor-reported usage and association. Do not present “60% more likely” as a causal conversion lift or assume the result transfers to smaller retailers.
- **Lesson:** helping people within a product is already a major strategy; personal-agent interoperability must show added value beyond that.

### C. Bring the product into the assistant — hybrid/competing direction

**Source:** [OpenAI's Apps SDK / apps in ChatGPT announcement](https://openai.com/index/introducing-apps-in-chatgpt/), October 2025. Primary-source search extract and independent launch coverage reviewed; direct primary page returned HTTP 403.

The announcement describes a Zillow app that shows home listings on an **interactive map inside ChatGPT**, along with apps such as Canva, Spotify, and Coursera.

- **Match:** conversation plus a rich interactive product surface. This directly challenges the false binary of “plain chat answers” versus “a rich website.”
- **Difference:** product UI enters the assistant's environment, rather than the assistant entering the company's website.
- **Evidence strength:** concrete announced integrations, not proof that this is the preferred long-term customer experience. No comparable retention/conversion results located here.
- **Implication for the home-search example:** Zillow already demonstrates another route to the same experiential goal. Explain what an owned product surface offers rather than treating all chat-hosted experiences as impoverished.

### D. Sell through external AI channels — commercially pragmatic alternative

**Sources:** [Shopify agentic storefronts documentation](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts) (full page retrieved); [OpenAI's original Instant Checkout / Agentic Commerce Protocol announcement](https://openai.com/index/buy-it-in-chatgpt/) (primary search extract; page returned HTTP 403).

Shopify describes catalogs, a business knowledge base, channel controls, attribution, and orders flowing back into Shopify. Its retrieved documentation distinguishes:
- **ChatGPT:** discovery/referral, with purchase completed on the merchant's checkout in an in-app browser or new tab.
- **Other listed channels:** direct checkout within the AI channel when activated.

The original OpenAI announcement described Instant Checkout within ChatGPT and merchants retaining merchant-of-record responsibilities. **Do not conflate the launch announcement with current channel behavior.**

- **Match:** agent-readable capabilities and discovery, customers' own AI interfaces, keeping existing merchant infrastructure.
- **Difference:** does not require the customer to visit and participate in an owned rich website.
- Shopify explicitly says merchants retain ownership of the customer relationship and post-purchase experience. Attribute that as Shopify's position; do not claim an external AI transaction necessarily eliminates the relationship.
- **Tradeoff:** transactional ownership can remain with merchants while discovery, ranking, and some interaction design move to a platform.
- **Evidence strength:** operational documentation shows an actual route, not independently demonstrated incremental revenue or preserved loyalty.

### E. Improve discoverability and data quality — complementary, not a full UX solution

Shopify's catalog and knowledge-base approach is concrete evidence of making product information, return policies, shipping details, and brand information available to assistants. Adobe's analysis also frames machine readability as an opportunity.

- **Match:** John's agent-friendly documentation and discoverable-capabilities direction.
- **Difference:** can serve off-site assistance without any person-agent collaboration in the website.
- Do not treat llms.txt, discoverable skills, or a particular discovery URL as proven drivers of ranking, traffic, or conversion. No such outcome evidence was established in this research.
- Better structured information is a plausible foundation, not a complete answer to the customer-relationship problem.

### F. Restrict or monetize AI access — materially different response

**Source:** [Cloudflare: introducing pay per crawl, July 2025](https://blog.cloudflare.com/introducing-pay-per-crawl/). Full article retrieved.

Cloudflare offers a model in which publishers can allow, charge for, or block crawler access. The announcement describes an early/beta commercial approach; current availability and terms require verification.

- **Difference:** preserve bargaining power and monetize content access rather than welcome agents into a participatory experience.
- **Fit:** more directly relevant to publishers whose content is the product than to every software company or retailer.
- **Caveat:** a vendor offering is not evidence of broad adoption, viable publisher economics, or restored customer relationships. This pass did not establish those outcomes.

### G. Better conventional UX — baseline alternative

Baymard's filtering/search guidance is an important non-agent response: improve product attributes, filtering, sorting, and product comparison. AI should compete with a good interface, not only a bad one.

A hybrid may be best: direct manipulation for some steps, conversation for others. Current research does not establish which tasks warrant which approach; usability testing is needed.

## 3. Synthesis for the story page

### Defensible statements
- AI answers can reduce clicks through to websites; cite a bounded study rather than extrapolating to all use.
- Retail leaders are concerned about brand loyalty and control of discovery; label those as concerns/expectations.
- Consumers value relevant help discovering and comparing products, while privacy and control remain important.
- Companies are experimenting with multiple approaches: website tools, owned assistants, apps inside chat, external commerce channels, and access controls.

### Hypotheses to label as such
- Persistent personal agents will be the preferred interface across many products.
- Bringing that agent into the company's environment will preserve relationships or loyalty better than chat-hosted apps or retailer-owned assistants.
- Agent-friendly documentation alone makes companies discoverable or improves commercial results.
- A particular standard will become widely supported.

### Proposed framing, not approved copy

Pain: **As customers turn to AI for discovery and decisions, companies risk losing influence over how their products are understood and experienced.**

Opportunity: **Let people and their assistants accomplish more with your product—whether that means welcoming agents into your experience or making your capabilities available where customers already work.**

Keep John's participatory vision distinct, but do not pretend it is the only credible solution. Avoid “visitors: 0,” “nobody visits,” “your website becomes irrelevant,” and implying that every API transaction is bad. Those are speculative illustrations, not established outcomes.

## 4. Next validation work

- Interview product owners about actual changes in discovery, attribution, customer insight, and conversion—not just whether they find agentic AI interesting.
- Ask customers how they currently switch between AI research and product interfaces. Look for real repeated-context problems before asserting them.
- Compare the same task using a strong conventional UI, an owned assistant, a chat-hosted product app, and a browser/personal-agent integration.
- Measure completion, time/effort, errors, permission comprehension, confidence, and willingness to return. Track causal conversion/retention effects where feasible.
- Seek independent evidence outside retail/publishing before making broad software-product claims.
- Verify report methodologies and fresh product documentation before selecting any numerical call-out for the website.

## Internal background

Read in the Arcturus Labs vault: `Arcturus Core Competencies.md` and its five linked talk notes: `The Agentic Web - A Future Beyond the Dark Web`, `Building the Future of AI Products - Agents, Factories, Workflows, and the Agentic Web`, `The Software Factory - From Coding with Agents to Coordinating Them`, `The Virtuous Cycle - Building AI Workflows You Can Trust`, and `English is the Programming Language of AI Software`. These establish John's position, not external validation.
