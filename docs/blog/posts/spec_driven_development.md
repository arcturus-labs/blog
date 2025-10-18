---
date: 2025-10-17
categories:
  - Agentic AI
  - Development Methodology
description: Transform spec-driven development from a small-scale experiment into a robust enterprise practice. Learn why natural language specifications fail at scale and discover practical solutions including hierarchical specs, conversational clarification, and living documentation that evolves with your codebase. Perfect for teams ready to scale AI-driven development beyond simple tasks.
image: /blog/assets/functionality_flicker/top_image.png
draft: true
---


<!-- TODO! 
- get  image
- make better description above
- make title more broad - just spec driven development
- remove "frunctionality flicker" from the first parrespond in https://www.linkedin.com/feed/update/
urn:li:activity:7384664250830606336?
commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7384664250830606336%2C738488754802153
4720%29&
dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287384887548021534720%2Curn%3Ali%3Aactivity%3A7384664250830606336%29
-->
# Making Spec-Driven Development work at the Largest Scale

When GitHub Copilot launched in 2021, AI code completion took the development world by storm. But after a mere year or two, code completion was completely eclipsed by vibe-coding, allowing much larger tasks to be accomplished with much less effort. Vibe-coding is great, but it has some problems that limit its utility. Agents tend to work with the code as if they are over-ambitious interns so that they often do more damage than good if you're not guiding them at every step.

The most recent trend is spec-driven development. This term is still ill-defined, but the basic idea is that prior to tackling a meaningful code change, you first create a specification document for that change and then use the specification as a guide for the AI to make changes. This helps the agent to better understand the big picture. Once the implementation is complete, you throw away the spec because it has served its purpose.

This form of spec-driven dev is a good idea! _But I want more!_ In this post I'll talk about a bigger notion of the spec-driven development. I'm talking about an ideal world where we keep track of the global product specification, and then we allow the agent to build code based upon that.

## The Challenge of Global Product Specification

Imagine that you set out to perform a truly extreme form of spec-driven development. You write your full product specification and then deploy an agent to execute upon the plan. It's going to build your whole website from scratch and return to you the finished product. But there's a problem. 2 days later when the agent finally returns it's not quite what you wanted. It's not a problem with the agent. In this fictional future example (which will probably be reality in 2 months), the agent's work is perfectly consistent with the specification doc – it's just that your specification was ambiguous. That's the problem with natural language – it's imprecise and ambiguous.

So what's the solution? One thing you could do is to specify away the uncertainty! Find everything that is ambiguous in the specification, and add subsections (and sub-subsections) to clarify exactly what you mean. But what you'll find is that in order to make natural language sufficiently precise, you will have to write so much content that you lose any benefit of writing the spec in the first place. The spec has become a formalized language and you might as well use a different formalized language for this task: code.

## How Humans Succeed Where AI Fails

In contrast, as humans, we do pretty well with natural language. How is it possible that we do such a reasonable job with large-scale software development when AIs fall flat?


### Shared Context and World Understanding

For starters, we have a shared understanding of the world that exists _right_ around us. An AI, on the other hand, has read every bit of text and code in the public domain – so it has a great idea of how things _generally_ work. But it has no idea how things typically work at your company and in this codebase, and every request it receives can only carry a small portion of the context it really needs. You, on the other hand, have accrued an understanding of your immediate environment through trial and error. When you started working at your company, you implemented your first code change, and in PR review you learned a LOT about "the way we do things here". And you learned more with every interaction you've made at the company both with the code and with the humans in meetings and through hallway conversations. What you've learned can not easily be put into a giant document and shared with the agent as context (...though it's a great idea to try this... but that's for another blog post).

### The Power of Clarification

Next, us humans _clarify_. When statements are made, we identify ambiguities, and we engage in conversations to disambiguate the possibilities. What's more, we're quite efficient at only dealing with the ambiguities that _really matter_. We lean back upon the shared context (last paragraph) and we don't ask they things that "everyone is supposed to know." We don't ask about which libraries to use, and we don't ask about tiny implementation details. We _do_ ask about things that confuse us or things that are unclear. Models are only now starting to get good at this.

## Building Better AI Development Workflows

So how do we address the challenge of specification ambiguity in large-scale spec-driven development? Let's hit the above points in reverse order and talk about both _clarification_ and _world view_.

### Enabling Clarification Through Conversation

Regarding clarification – there is no way that the agent can get to a better understanding if you _allow_ them to ask about the ambiguous or ill-defined portions of the spec. That is, I think if spec-driven dev is to work, it necessarily _requires_ some back-and-forth to identify and nail-down all the ambiguities. This is probably implemented as some sort of chat interface. Another thing you can do for smaller chunks of implementation is to have the AI implement the spec multiple times and then looking at the disparity in the results to identify the ambiguities. But again, this is probably best implemented as a conversation where the agent is walking the software through the possible interpretations of the spec.

### Building Agent World View Through Hierarchical Specifications

But the goal of clarification is ultimately to correct and flesh out the agent's world view. They need to know how things typically work at _this_ company and in _this_ codebase. I think there are a couple of options here. First, do you remember the idea above about just adding subsections to the spec... and the sub-subsections? This is a pretty bad idea for humans to do, but maybe it's not so bad for the machines to do for us. I don't recommend literally adding all these subsections to the spec because it would be huge. Instead, there is probably some hierarchical approach that can be used to allow so that the global spec can link out to sub-specification documents. (As a matter of fact, in [an earlier post](/blog/2024/11/21/roaming-rag--make-_the-model_-find-the-answers/) I showed that AI Agents are pretty good at navigating links like this - so it's probably a natural fit.)

It's not clear what the best organization of the hierarchy is though – you could put one spec in every file, and then in every directory have a rolled up version of that directory's contents – all the way to the top. In this case, the specification would be rigidly attached to aspects of the code, so a better approach might be something more like a free-form wiki – but that can get out of hand for other reasons.

### Code as the Ultimate Specification

At some point, the best way to encode the low-level assumptions of the code is to just use the code itself, because, while there is ambiguity in programming languages, there is no ambiguity in the code. This does imply a philosophical change though. Some people are in the camp that a well-defined spec should lead to functionally equivalent generations each time. I disagree with this, basically because I believe it to be infeasible – natural language just isn't up to the challenge. Relying upon the code itself as the leaf-level spec does remove the problem of specification ambiguity though, because you start a new implementation change grounded in the code that already exists. And you never expect to regenerate the code from spec.

## Living Specifications: Usage and Evolution

The above discussion addresses how the specification comes into existence. The next interesting question is how the spec is used and changed over time. If done correctly, the specification will be of great use for both the humans and the AI agents that are working in the codebase.

If the AI agents are aware of the spec and understand how to navigate it, then they will be grounded not only by the code - but the product specification itself. This is actually quite an improvement over the way we humans used to do things, because often we don't have access to the product specification, and we end up unwittingly trammeling over some product decision that really was pretty important at some point. This is the reason that aging codebases look like inconsistent patchwork quilts – we did the best we could with the very small context we had at hand – most of which was extracted by reading code rather than talking with product managers or reading documentation.

For human developers this form of spec-driven development is also a boon. It's _still_ not likely that we will actually read all the product specs when making a change, but it should be quite easy to have a _conversation_ with the AI agent and sus out the information that is relevant to our work at hand. This is also the case for product managers and, heck, executives – in the olden days (like 5 years ago), no one really liked docs because they were never up-to-date and you could never really find what you're looking for. In the world we're entering, the specification maintained by the machines. And in a quick conversation, you can find whatever you're looking for. 

### Specification Evolution Through Code Changes

The last thing to cover is how specifications change with time. At this point, we think about specification-driven development in the manner I introduced at the start of this post – you write the spec, break it up into tasks, have an AI implement all the tasks, and then you throw away the spec and submit your PR. I think we got it backwards, though – I think changes in code should lead to changes in the specification itself. Whenever code changes, by whatever means, then it needs to be compared with the existing product specification. If this introduces anything that is inconsistent to the written specification, then the spec edit needs to go into the PR along-side the code change. This leads to a richer working experience for everyone on the team. For the engineer, it makes it easy to understand any surprising side-effects that change the product plans. For the product manager, they can now look at the PRs and evaluate the higher level changes in the product and make useful commentary – this was challenging in a time when PRs only involved changes in code.  

## The Future of Spec-Driven Development

The path forward for large-scale spec-driven development isn't about perfecting natural language specifications — it's about building systems that can navigate ambiguity through conversation and context. By combining hierarchical specifications with conversational clarification, and by grounding agents in existing code, we can create AI development workflows that are both powerful and consistent.

The real breakthrough will come when specifications become living documents that evolve with our codebases, maintained by the same AI agents that implement them. This creates a feedback loop where product decisions are preserved, context is maintained, and the gap between specification and implementation disappears.
