# Brainstorming
(use - [ ] for bullets so we can mark them off)

## notes
- important docs 
  - "Arcturus Core Competencies" - in Arcturus Labs vault
  - "Arcturus Labs Strategy 2026-09-25" - in Arcturus Labs vault
  - "Make a website for Arcturus Labs" - in Arcturus Labs vault
- possible website resources
  - Inspiration (from the website note): https://twotimespi.dev/ (simple, beautiful); https://meet.ameliechatelain.com/ ("explore the CV" idea, different format)
  - Andrei Moise's tips (Discord DM): prompt asking for a "very very visually pleasing and alive and creative" page, "animated page that transforms worlds as you scroll down," plus 1-2 example sites; run with Opus 5.5 at xhigh
    - Andreimoise.ai (his example site)
    - https://impeccable.style/ (design vocabulary/skills for agents)
    - https://www.ui-skills.com/skills (420 UI skills)
    - https://mobbin.com/ (UI/UX screenshot inspiration)
    - https://x.com/DesignArena/status/2111884406868808191/photo/1 (each model's default site style; what to avoid)
    - Claude design
- I might like simple story telling like "pain" (which is a short story of what is going wrong) and then "solution" (which is a short story of how it can be fixed) and "proof" (where we mention my books and peoples statements about me) and then "call to action" (which is is like an invitation to call me or fill out a form)
  - I don't know how to draw people into my blog
  - I don't know how to draw people to my future examples (which will probably be blog pages that link to the examples)
- Maybe the home page is just "you're here for a reason" and clicking on one of the 3 reasons pulls you to the dedicated page. This would scale well as we add more.
  - The homepage could also link to components like proof. Could have a proof section even if they haven't; they don't know what they want yet. It could have a contact form and it could prominently feature recent blog posts.
  - If they click on to one of the reasons you're here, then that could send them to a better storytelling page that still also ends in proof and the call to action.
- I really like "How Ponder works / From raw footage to a finished video in four steps." on https://ponder.ai/ : the left side of the page shows a set of steps, and as you scroll the imagery on the right updates and the matching step on the left is highlighted. The text stays fixed while the imagery animates as that step is being told, then scrolls past and the next step highlights. This is great for storytelling.
- **Possibility: one full-screen canvas as the background for the whole site.** The stars, the night-to-morning gradient (sun peeking over the horizon at the very bottom), and any reaction to scroll or the mouse would all be drawn on one canvas, so we can do absolutely anything visually. The text and content layered on top stay simple HTML, which is easier for agents to read and deal with. Not decided; things to check include readability over a moving background, performance and phones, a still fallback, and reduced motion.

## Decisions
(Add to this as we decide. Open questions stay in the notes above.)

- **Home page narrows down what the visitor is interested in.** It asks "you're here for a reason" and offers the three reasons; choosing one takes them to a dedicated page for that path. For visitors who don't pick one, a light-hearted rebuttal ("Or maybe you're not here for a reason...", wording still to be chosen) leads into the rest of the page: recent blog posts, a short proof section, and a call to action (call or form). Risk to manage: this can get crowded, so each band must stay short (to be handled when we design it).
- **Each path page (Agentic Web and the other two) is a walked-through story**, in the spirit of the "How Ponder works" section on ponder.ai but our own take. It looks like an animated slide presentation, though not literal slides: a text outline that walks the visitor through the story, with imagery that corresponds to it. It does not have to be a list on one side and imagery on the other.
- **The story's big sections are problem, then solution.** Each section has a very small number of steps. After the story: filtered blog posts for that path, proof, and the call to action. The path pages skip the "you're here for a reason" part and go straight into the story.
- **Starting wording for the home page (draft, easy to change):** top line "I help teams build AI products people can trust and actually use."; the three cards read "Customers are asking AI instead of visiting our product.", "Our experts are buried in work AI could do, and we don't trust it yet.", and "We're shipping with agents and the process is a mess."
- **Booking:** the main call to action is booking a call. Use https://calendly.com/jfberryman/15min as a placeholder for now.
- **Visual motif:** incorporate the Arcturus logo and the four-pointed stars from the current arcturus-labs.com. The current site's look is not quite what John wants, so the stars and logo carry over, not the whole style.
- **Draft site:** a basic static draft of the home page lives in `draft_site/` (placeholders marked TODO); it will become more engaging later.

## todo-ish (or maybe reminders we need to check on)  
- [ ] Survey similar indie consulting websites and learn what works for them (before design starts).
- [ ] Figure out branding. Arcturus = "keeper of the bear" (the bear is a formidable problem; the keeper is strength); star, navigation, and pathfinder imagery fit. Logo and color scheme live at https://arcturus-labs.com/assets/images/ (not yet viewed).
- [ ] Incorporate John's bio: emphasize deep AI product-engineering experience, early production engineering on GitHub Copilot, and coauthorship of *Prompt Engineering for LLMs*; support with the earlier search/recommendations work at Eventbrite and *Relevant Search*.
- [ ] Incorporate client quotes, including the unused testimonials from Perch Insights, CETA, and Peer Supply recorded in the vault's `Make a website for Arcturus Labs` note. (Make sure to mention the role of the person that has the quote. It's good to see that it's CEO or CTO.)
- [ ] Incorporate speaking gigs, especially Hugo, Hamel, Doug, O'Reilly (others?)
- [ ] Incorporate YouTube (John has a channel, but the audience is small, so use it as supporting content and don't lean on it as proof of reach).
- [ ] Primary conversion goals: get visitors to contact John or subscribe with their email. The previous contact form attracted a lot of spam, so decide between a form and a plain email address (undecided).
- [ ] Look into WebMCP: expose page tools so a visitor's own agent can guide them through the site (worth investigating, not urgent).
- [ ] Decide on a lead magnet: something useful to give away in exchange for an email (the sites with the biggest lists all do).
- [ ] Add concrete examples of the agentic web to make the problem felt (examples are coming soon; until then the site has to communicate without them).
- [ ] Get rid of the header bar - when the page loads have text that directly overlays the starry night sky and as we scroll down, the text fades to transparent (and unclickable)
- [ ] The whole background, which will probably be like a canvas controlled by JavaScript or something, we can animate this like a play almost where we go a little bit grayscale and dark and starless during the problem area and make the stars come out during the solution area and make The sun starts to peek over the horizon with sunbeams that looks realistic as we get into the contact section./