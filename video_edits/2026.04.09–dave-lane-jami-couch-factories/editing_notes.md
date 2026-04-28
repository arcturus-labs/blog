# key points

- building from templates (like cookie cutter)
  - key points
    - 12ish Jami "the factory works well for us because we don't have to build anything, we need only build the types of things that we build the way we build it"
    - 15ish John "help me understand what the full factory is" Dave talks about it immediately - good clip
    - 17:30ish Dave Lane "pass muster" - he's talking about how the feedback loop closes - important
    - 18:30 "it went from being advisory to" - important - they matured it from just providing advice and as they understood its behavior they started to just let it do the work
    - 35ish discussion about how they keep it on rails w/ these architectural templates and rules
    - 36ish dave lane talks about how the coding agent pulls in samples from their codebases which serve as great patterns - this is the few shot pattern!
    - 44:06 " And that opinionated approach definitely has made it easier, I think, to, to make real progress on getting this thing running." great quote - keep it

- structure of the factory    
    - 20:44 starting from " So my, my typical workflow is. " there is a good conersation about every step of the factory
      - He also talks about the importance of feedback and also the importance of limiting the number of cycles that it might cross
    - 23:48 I try to reiterate full factory
    - 26:09 " thing to say about the architecture " - he talks about the infrastructure that supports the factory
    - 26:41 " choice of keeping things tied to Jira " - important to make the work visible and ledgible to both humans and agents - key!
    - 30:28 " Let's dig into this a little bit. " I start asking them about how individual agent components are built
      - skills for various task
      - but also "rules for how we do things" -And they created it by copying flutter's rules but saying we need to adopt this for our code base and then showing it their own code base to make it adopt those rules – it sets up the general code structure so all generated code looks the same and is easily navigable - and they have ensured that it always works well (if they kept it completely generic, then they couldn't tune the way this is working)
      - all of this goes GREAT in the templates section too
    - It's triggered by prompts created by their factory Scarif that are text templates
    - 48 specific infrastructure issue " 'Cause it doesn't do a great job of cleaning up after itself all the times. "
  

- incremental adoption
  - there are other good incremental adoptions points in the rest of this doc
  - 41ish " the end goal is not, oh, we're just going to complete stuff automatically and, and never look at it. It's more we're going to stretch time and budgets more by increasing what we can accomplish in the same amount of time or with the same amount of money."
  - 59 "How would you recommend that a company that has an established development practice incrementally move to something that's like a factory?" - good starting point for that conversation
  - 1:01 " And I think one quick win for people that are critical of introducing these tools to like their core tasks could be saying, Hey, you know you need to make sure you're doing security scans every night. " and following - start adopting AI factory only for the taskss that people don't want to do but that claude is quite good at anyway (this also goes under the "cultural issues" section)

- design reviews
  -  28:16 - design reviews are still hard 
  -  39ish Hey, we're rejecting most of the  PRS scarf made because it did what we specified and we specified the wrong thing. 
  - 44:37 " the design review thing " - it was a bad pain point - this is how they addressed it

- code reviews
  - key points
    - 13ish the pr agent has better ability to pull context from code than the humans
    - 19:58 " I can code locally with cloud code, get good results, have the fact have this code  reviewer review it, you know, even use the GitHub  CLI to say, okay, Claude, get the feedback off of here and address it. You know? It's like, okay, let's encode that into a factory now. " - again, as you feel confident then you promote things to be handled in the factory instead of locally
  - questions/notes
    - what about the human context - like the product desire?

- cultural issues 
  - 51:30 Dave starts talking avout getting employees to adopt AI
    - having people who have already made huge career jumps means they're adaptive
  - 54ish roles are changing
  - 54:50 Dave " when we, you know, ask what roles are being replaced on the chopping block?" starting here he talks about moral as things shift -- when peope are focused on outcomes instead of just writing code, then the moral stays high

- non-code factories
  - 1:04 " So like even in our marketing I think Jamie had the idea of, you know, we have all this built up knowledge about all these projects, all these clients we've worked with, and we've never written any of it down." and after

# Cold-open fodder
Jami, ~11:40 “We don’t have to build a factory that’s so general purpose that anyone could use it. We just need one that builds things the way we want them to be built.”

Dave, ~41:10 “The end goal is not, ‘we’re just going to complete stuff automatically and never look at it.’ It’s more that we’re going to stretch time and budgets by increasing what we can accomplish.”


# todo
- [ ] Make cold-open and intro
- [ ] Make a topical highlight reel from all the topics above
- [ ] Make a several key point reels from the above