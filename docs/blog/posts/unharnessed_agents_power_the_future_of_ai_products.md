---
date: 2026-04-24
authors:
  - john-berryman
categories:
  - Agentic AI
  - AI Product
description: The next era of AI products will not be built around individual chatbots or coding assistants. It will be built around agents that carry context, tools, skills, and interfaces across every part of digital work. To get there, we need to stop treating the "agent harness" as a coding-product wrapper and start treating the agent as the product runtime itself.
title: Unharnessed Agents Power the Future of AI Products
image: /blog/assets/unharnessed_agents_power_the_future_of_ai_products/hero.jpg
---

# Unharnessed Agents Power the Future of AI Products

This post follows on from [The AI Product Era You're Building For Might Already Be Over](./the-ai-product-era-youre-building-for-might-already-be-over.md). There I argued that AI product development is moving toward agentic runtimes. Here I want to sharpen that claim: the future will be composed of agents, but the term "agent harness" is already limiting how we think about what those agents can become.

We should _unharness_ our agent harnesses and call them what they are: _agents!_ And in the future they won't just be coding assistants. They will be personal assistants, interface builders, workflow operators, and collaborators in almost every part of digital life.

![A robotic bronco labeled AGENT bucks off a software developer as a saddle labeled HARNESS breaks free](./assets/unharnessed_agents_power_the_future_of_ai_products/hero.jpg){ align=center width=100% }
<!-- more -->
## Agents and Agent Harnesses

In 2025 we wrestled with the notion of an agent. Was it a workflow implemented in traditional software that made occasional call-outs to LLMs? Was it a `while` loop with calls to LLMs and tools? Both answers had problems.

Workflows were too rigid. The agent was not free to follow its own train of logic when handling special cases, and when the real world presented the workflow with something unexpected, it would simply break. Then you had to resort to programming those special cases back into the logic.

The `while` loop agent had the opposite problem. The model was too free, and would often get distracted and never complete its task at all.

Fortunately, by the end of 2025 the models had gotten significantly better and less likely to wander off. This solidified the `while` loop agent as the winner and opened a lot of interesting new doors for AI product development.

In parallel with this development came the confusingly named "agent harness". Agent harnesses popped up in early 2025 around code development and are basically human-in-the-loop, batteries-included versions of the `while` loop agent. While they are still just a `while` loop wrapping calls to LLMs and tools, they have much stronger opinions and mechanisms for managing context, providing filesystem and OS integration, sandboxing execution, integrating with skills and MCP servers, and more.

The agent harness originated to service code development, and the Cursor agent, Claude Code, Codex, and OpenCode are prominent examples. However, in recent months (mid 2026) agent harnesses are being used to service non-code interactions. Claude Cowork was the first attempt at this, but OpenClaw received most of the fanfare because of just how much control it ceded to the agent. It was a glimpse into our future.

## The Harness Is the Wrong Frame

The notion of the agent harness has opened a lot of interesting doors, but I find it problematic for a few reasons.

First, every provider has their own agent harness that ostensibly feels like the same thing, but they are all opinionated and opaque, and the details often matter in subtle ways. Context management differences – especially in compaction and pruning – can lead to significantly different outcomes. Ditto with memory creation and recall. You rarely control or understand what the agent harness is doing.

What we need instead is a standardized notion of the pieces used to build agents. They need to be simple and pluggable, so that building your own agent feels like snapping together Lego blocks. These blocks, and the agent as a whole, need to be transparent and easy to reason about. They should also be general enough to build agents that operate in any environment (terminal, zoom, slack, ...), communicate in any modality (text, voice, image, ...), and scale to any complexity (single turn agent, user in the loop assistant, sub agents, teams).

Second, the name is misleading. "Agent harness" implies that the _agent_ lives inside some sort of _harness_, but this isn't true. The agent is the `while` loop, the LLM calls, the tool calls, the context management, the skills and MCP integrations, and so on. The agent is the _whole composition_. The agent _is_ the "agent harness". So that's why in this post I propose we "unharness" our agent harnesses. Let's just call them what they are: they're _agents!_

Finally, and most importantly, the notion of an agent harness is far too narrow. It stifles the most exciting product possibilities because we are fixed in the mindset that the "agent harness" is for software development and lives inside of a terminal or an IDE. This shouldn't be. We can use the identical machinery – _the agent_ – to work on any task addressable via an API.

## Agents Should Leave the IDE

The agent – _my agent_ – should follow me around like it's my personal executive assistant. Sure, it should write my code. But it should also help me draft blog posts; sort, filter, and respond to emails; help me voice-navigate my phone; join my meetings and take notes; perform background lookups and answer questions; organize and augment my notes in Obsidian.

Stretch further. My agent should be able to automatically generate user interfaces for whatever data or service I want. In this future world, the internet for humans goes away. Instead, we get whatever interface we need created locally, while our agents navigate the internet, retrieve the data, and interact with services on our behalf.

![A friendly robotic agent steps out of an IDE storefront to join its user in the city](./assets/unharnessed_agents_power_the_future_of_ai_products/out-of-the-ide.png){ align=center width=100% }

## Skills Are the New Programs

Agent skills are an important part of this AI revolution. Skills are the new programs, English is the new programming language, and the agent is the new runtime. The importance of this is hard to overstate.

Skills aren't just static instructions you write once and attach to your agent. They are dynamic, composable, and self-evolving.

* **Skills can create other skills.** I've used the `create-skill` skill several times now to examine my workflows and write a new skill to capture the idea.
* **Skills can improve existing skills.** Imagine a new `improve-skill` skill that analyzes agent traces to improve some other skill `foo`. The `improve-skill` skill would identify places where the user corrected behavior caused by `foo`, then update the `foo` skill text so those problems are less likely to occur in the future.
* **Skills can retrieve and compose other skills on the fly.** Imagine a `build-anything` skill that first uses the `find-skills` skill to download the skills it is missing, then incorporates them into itself. It reminds me of Neo in *The Matrix*: "I know kung-fu!"

<p align="center">
  <img src="/blog/assets/unharnessed_agents_power_the_future_of_ai_products/i-know-kung-fu.gif" alt="Neo wakes up and says, &quot;I know kung-fu!&quot;" width="80%">
</p>

What's more, since English is the new programming language, software development is no longer limited to software developers. Non-technical users can express their intent in plain language and have their agent translate that into a skill – a program, effectively – that is perfectly legible to the non-developer. Software development for the everyman.

## How We Get There

So that's the future of AI product. I want to help us get there. Here are two practical steps.

First, everyone needs to build their own "agent harness" (ahem… _agent_). The libraries available today make this far easier than one might expect. The goal is twofold: develop a much deeper intuition for context management, memory management, skill writing, and agentic operation; and parallelize our learning.

If everyone is building agents, then we will quickly cover many more use cases and discover which patterns work, which abstractions matter, and which problems still need to be resolved. Building our own agents also immediately delivers value to the builders because their agents will be transparent, easy to reason about, and easy to extend into scenarios the current crop of agent harnesses don't reach – any environment, any modality, any complexity.

Second, as we learn lessons from building our own agents, we need to work toward a new agentic standard. We need to clearly define the modules that compose an agent – compaction, pruning, memory, tricky auth stuff, and so on. And we need a better standard for how agents connect to existing environments, so we can bring our agents anywhere we go and have them do whatever task we want – any environment, any modality, any complexity.

Once we get through this step, we won't be building our own agents from scratch. We'll be assembling exactly the agent we need from a small, well-understood set of primitives, and "programming" it by writing the appropriate agent skills.

## Let's Unharness This Together

We need to form a standards committee to tackle this problem. I have a lot of ideas, but I only have one set of experiences, and they are not yours. Let's compare notes. If we can catalog the behaviors that agents need to satisfy across real tasks, real environments, and real users, then we can outline a new standard for how agents are built and how they are expected to behave.

That is how we unlock the next level of abstraction: not just more powerful agents, but entire "agencies" – business processes run by coordinated swarms of agents that work side-by-side with humans.

---

### _Building agents beyond the IDE?_

If you're experimenting with agents, skills, or new AI product patterns, I'd love to compare notes. [Get in touch](/#contact-blog).

And if you want to follow along as this thinking develops, [subscribe here](/#contact-blog).

<!--
LinkedIn:
We are thinking too narrowly about agents.

The phrase "agent harness" is a problem here. We associate it too closely with coding only - agent harnesses are something that lives in an IDE, wraps an LLM loop, and helps software developers.

But agents are bigger than that.

They are the building blocks of what comes next: personal assistants that carry context, tools, memory, skills, and interfaces with us across whatever software we move through.

If we standardize our understanding of agents and their parts, we can stop trapping them inside coding environments. We can unharness them from the IDE and let them follow us into the rest of digital life.

That's the future of AI product I'm trying to point at in my new blog post.


https://arcturus-labs.com/blog/2026/04/24/unharnessed-agents-power-the-future-of-ai-products/

Twitter/X:
We are thinking too narrowly about agents.

Even "agent harness" makes them sound like coding tools - something trapped inside an IDE.

But agents are bigger than that. They are the building blocks of what comes next: assistants that carry context, tools, memory, skills, and interfaces across whatever software we move through.

If we standardize agents and their parts, we can unharness them from the IDE.

https://arcturus-labs.com/blog/2026/04/24/unharnessed-agents-power-the-future-of-ai-products/
-->
