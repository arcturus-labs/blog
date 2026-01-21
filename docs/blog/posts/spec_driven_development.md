---
date: 2025-10-17
authors:
  - john-berryman
categories:
  - Agentic AI
  - Development Methodology
description: Natural language specs are inherently ambiguous, and AI agents lack the nuanced context that human developers have. This leads to codebases becoming patchwork quilts and product decisions getting trampled over. I'll explore why current spec-driven development fails at scale and how we might build conversational, living specifications that evolve with our codebases instead of being thrown away.
image: /blog/assets/spec_driven_development/main.jpg
title: Why Spec-Driven Development Breaks at Scale (And How to Fix It)
---

When GitHub Copilot launched in 2021, AI code completion took the development world by storm. But after a mere year or two, code completion was completely eclipsed by vibe-coding, allowing much larger tasks to be accomplished with much less effort. Vibe-coding is great, but it has some problems that limit its utility. Agents tend to work with the code as if they are over-ambitious interns; they often do more damage than good if you're not guiding them at every step.

The most recent trend is spec-driven development. This term is still ill-defined, but the basic idea is that prior to tackling a meaningful code change, you first create a specification document for that change and then use the specification as a guide for the AI to make changes. This helps the agent to better understand the big picture. Once the implementation is complete, you throw away the spec because it has served its purpose.

This form of spec-driven dev is a good idea\! *But I want more\!* In this post I'll talk about a bigger notion of spec-driven development. I'm talking about an ideal world where we keep track of the global product specification, and then we allow the agent to build code based upon that.

![Spec-Driven Development](./assets/spec_driven_development/main.jpg){ align=left width=100% }

<!-- more -->

## The Challenge of Global Product Specification

Imagine that you set out to perform a truly extreme form of spec-driven development: You write your full product specification and then deploy an agent to execute upon the plan. It's going to build your whole website from scratch and return to you the finished product. But there's a problem. 2 days later when the agent finally returns you realize that the generated product is not quite what you wanted. It's not a problem with the agent, let's assume that the agent's work is perfectly consistent with the specification doc – it's just that your specification was *ambiguous*. That's the problem with these big specs – they are written in natural language and natural language is imprecise and ambiguous.

So what's the solution? One thing you could do is to specify away the uncertainty\! Find everything that is ambiguous in the specification, and add subsections (and sub-subsections) to clarify exactly what you mean. But what you'll find is that in order to make natural language sufficiently precise, you will have to write so much content that you lose any benefit of writing the spec in the first place. The spec has become a formalized language and you might as well use a different formalized language for this task – code.

## How Humans Succeed Where AI Fails

In contrast, as humans, we do pretty well with natural language. How is it possible that we do such a reasonable job with large-scale software development when AIs fall flat?

### Shared Context and World Understanding

For starters, we have a shared understanding of the world that exists *right* around us. An AI, on the other hand, has read every bit of text and code in the public domain – so it has a great idea of how things *generally* work. But it has no idea how things typically work at your company and in this codebase, and the context that we provide these agents can't possibly capture the nuance for understanding this.

*You*, on the other hand, have accrued an understanding of your immediate environment through trial and error. When you started working at your company, you implemented your first code change, and in the PR review you learned a LOT about "the way we do things here". And you learned more with every interaction you've made at the company both with the code and with the humans in meetings and through hallway conversations. What you've learned can not easily be put into a giant document and shared with the agent as context.

### The Power of Clarification

Next, humans seek *clarification*. When statements are made, we identify ambiguities, and we engage in conversations to disambiguate the possibilities. What's more, we're quite efficient at only dealing with the ambiguities that *really matter*. We lean back upon the shared context (last paragraph) and we don't ask about the things that "everyone is supposed to know." We don't ask about which libraries to use, and we don't ask about tiny implementation details. We *do* ask about things that confuse us or things that are unclear. Models are only now starting to get good at this, and even so, to become *really good* at clarification, AI agents need the nuanced contextual understanding I present in the last paragraph – which doesn't exist for them.

## Building Better AI Development Workflows

So how do we address the challenge of specification ambiguity in large-scale spec-driven development? Let's hit the above points in reverse order and talk about both *clarification* and *world view*.

### Enabling Clarification Through Conversation

Regarding clarification – there is no way that the agent can get to a better understanding if you *allow* them to ask about the ambiguous or ill-defined portions of the spec. That is, I think if spec-driven dev is to work, it necessarily *requires* some back-and-forth to identify and nail-down all the ambiguities. This is probably implemented as some sort of chat experience. Another thing you can do for smaller chunks of work is to have the AI implement the spec multiple times so that the different implementations reveal points of ambiguity. The agent can then compare the different implementations and use what it learns to converse with the developer about which direction it should go.

### Building Agent World View Through Hierarchical Specifications

The goal of clarification is ultimately to correct and flesh out the agent's world view. They need to know how things typically work at *this* company and in *this* codebase. There are a couple of options here. First, recall the idea above about adding subsections and sub-subsections to the spec? This would require a great deal of effort for a developer, but this might be time well spent for an AI agent. I don't recommend literally adding all these subsections to the spec because it would be huge. Instead, there is probably some hierarchical approach that can be used to allow so that the global spec can link out to sub-specification documents. (As a matter of fact, in [an earlier post](http:///blog/2024/11/21/roaming-rag--make-_the-model_-find-the-answers/) I showed that AI Agents are pretty good at navigating links like this \- so it's a natural fit.)

It's not clear what the best organization of the hierarchy is though – you could put one spec in every file, and then in every directory have a rolled up version of that directory's contents – all the way to the top. In this case, the specification would be rigidly attached to aspects of the code, so a better approach might be something more like a free-form wiki – but that can get out of hand for other reasons.

### Code as the Most Granular form of Specification

At some point, the best way to encode the low-level assumptions of the code is to just use the code itself, because, while there is ambiguity in natural language, there is no ambiguity in the code. This does imply a philosophical change though. Some people are in the camp that a well-defined spec should lead to functionally equivalent generations every time. I disagree with this, basically because I believe it to be infeasible – natural language just isn't up to the challenge. Relying upon the code itself as the leaf-level spec removes the problem of specification ambiguity because code changes are grounded in the code that already exists. And you never expect to globally regenerate the code from the master product spec.

## Living Specifications: Usage and Evolution

The above discussion addresses how the specification comes into existence. The next interesting question is how the spec is used and changed over time. If done correctly, the specification will be of great use for both the humans and the AI agents that are working in the codebase.

If the AI agents are aware of the spec and understand how to navigate it, then they will be grounded not only by the code \- but the product specification itself. This is actually quite an improvement over the way we humans used to do things: as developers we rarely have access to the product specification, and we often end up trammeling over product decision that have been lost to the past. This is the reason that aging codebases look like inconsistent patchwork quilts – we did the best we could with the very small context we had at hand – most of which was extracted by reading code rather than talking with product managers or reading documentation.

This is precisely where global, hierarchical specifications will be of their best service. No, developers should be expected to actually read those specifications, but it should be easy for them to have a *conversation* with the AI agent and suss out the information that is relevant to our work at hand. As the developer scopes out a code change with the agent, the agent will navigate the global spec and call out any places where the implementation is inconsistent with the spec.

### Specification Evolution Through Code Changes

The last thing to cover is how specifications change with time. Like I said in the intro, we tend to think about specification-driven development like so: you write the spec, break it up into steps, have an AI help implement all the steps, and then you throw away the spec and submit your PR. I think we got it backwards – I think changes in code should lead to changes in the specification itself. Whenever code changes, it needs to be compared with the existing product specification. If this introduces anything that is inconsistent to the written specification, then the global specification will be edited and submitted in the same PR as the code change.

This leads to a richer working experience for everyone on the team. For the engineer, it becomes easier to understand how their code changes are affecting the global specification. The product manager can also become more involved in pull requests because they can read the actual text of the specification change and jump into the conversation if they see anything surprising.

A global spec will also give product managers and even executives more insight into the evolution of the product. In the olden days – say, 5 years ago – few people *actually* read documentation because it was difficult to find and rarely up-to-date. In the world we're entering, the global specification will be kept up-to-date automatically. The product manager and the executive *still* won't read the docs, but they *will* talk to their AI assistant and get answers about the current state of the product and about how it has evolved over time.

## The Future of Spec-Driven Development

The path forward for large-scale spec-driven development isn't about perfecting natural language specifications — it's about building systems that can navigate ambiguity through conversation and context. By combining hierarchical specifications with conversational clarification, and by grounding agents in existing code, we can create AI development workflows that are both powerful and consistent.

The real breakthrough will come when specifications become living documents that evolve with our codebases, maintained by the same AI agents that implement them. This creates a feedback loop where product decisions are preserved, context is maintained, and the gap between specification and implementation disappears.  