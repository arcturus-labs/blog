
## Outline

* Intro – pain and potential resolution:
  * traditional search uses a deterministic algorithm to do the best it can.
    * lowest common denominator – try to match keywords across all relevant fields
    * smarter – introduce synonyms, hand tune relevance, include judgement lists
    * smartest – hybrid search, probably need to hire an ML team, prohibitively expensive
  * AI might make this easy – just wrap traditional search in AI search
    * (this doesn't mean revamping your UX – keep the search API the same, put an agent shim between API and engine; adoption is easy)
    * it understands any domain you give it
    * with proper explanation (system message) it will understand your users and your catalog
    * It knows when to make very general searches, and it knows when to tighten the searches
    * it knows synonyms in that domain "gorilla costume" "monkey suit"
    * it knows when to use quotes "dress shoes"
    * if you have lots of different fields, it can make the most of them, it can even do boosting and stuff potentially
* Experiment – Wayfair search through an agent
  * (explain data set and setup)
  * Realized after starting that it's a bit artificial. We're comparing agentic search with our naive version of Wayfair search. So it's not quite fair.
* Considerations – three things that come up (and what to do about each)
  * Teaching the agent to search
    * **Challenge**: Agent makes over-constrained queries – uses `+` (required) everywhere and empties results; applies quotes where unnecessary; searches one field (name or description) without balancing; hallucinates facet/filter values not in the index.
    * **Resolution**: Work with the model. Better prompting and field awareness. Explain your content, what users care about, and what each field contains. Title → phrase matches; description → looser matching, synonyms. Give top-level facet values. Teach behavior: start general, narrow with parallel sub-searches.
  * Latency
    * **Challenge**: Traditional search teams optimize for sub-50ms; agents are slower (e.g., one general query + several parallel queries).
    * **Resolution**: If the agent returns better results, users tolerate 5 seconds over 50ms. Real obstacle may be convincing the search engineering team.
  * Overhauling the UX
    * **Challenge**: Thinking you must redesign everything for AI.
    * **Resolution**: You don't. Keep the search API unchanged – insert an agent shim between the API and the search engine that translates user intent into queries. Your frontend and API contract stay the same; adoption is easy. See [Incremental AI Adoption for E-commerce](../blog/incremental_ai_adoption_for_ecommerce.md) for a stepwise approach.
* Conclusion
  * summarize: agent-wrapped search can outperform traditional search with careful prompting - no need for expensive ML; latency is a tradeoff; no UX overhaul needed
  * uplifting point: models are continually getting better – if there's truth to this today, it only becomes more true
  * CTA: Are you interested in upgrading your traditional search? [Perhaps I can help.](/#contact-blog) [Subscribe and you'll be the first to know](/#contact-blog) when more posts like this land.
