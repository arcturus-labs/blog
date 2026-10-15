---
date: 2026-10-15
authors:
  - john-berryman
categories:
  - Agentic AI
description: My software factory is an agent skill – harness-agnostic, modular, and evolving independently across repos.
image: /blog/assets/my_software_factory/hero.jpg
---

# My Software Factory

Everyone is experimenting with AI right now, trying to find their way as the models and tools keep changing. I'm no different.

This post is a look at how I'm building my own software factory. I'm still early in the experimentation – making my own mistakes and taking my lumps – but I think a few of the ideas are interesting enough to share.

This is by no means the One True Way™. I'd like it to be the start of a conversation. How are you building your factory? What's working, and what's not?

![Robots working along a software factory assembly line, from requirements and design through testing and deployment.](./assets/my_software_factory/hero.jpg){ align=center width=100% }

<!-- more -->


First, I avoid vendor lock-in. Since everything is progressing so quickly, why be stuck on a particular model/harness? – How? – I typically use the pi.dev harness, which gives me access to any model I feel like using. I switch between a $20/mo OpenAI account, a $20/mo Anthropic account, and nickels and dimes thrown at the open-source models. I get by pretty well. When I want to try Codex or Claude, I do!

My software-factory is written as an agent skill. (English has become the new programming language! Who knew!?) My software-factory guides me through a process: task selection, brainstorming ("grill me"), and to-do generation. Once a task is ready, a subagent creates a worktree, implements the change, QAs it, merges, and cleans up. Pretty simple.

The software-factory skill is written generically so that it doesn't require Claude-only or ChatGPT-only primitives. This is pretty easy b/c all the frontier harnesses are converging in feature set.

My software-factory skill is modular.

- I have reference files if I want specialized behavior per harness (hint... I basically don't).
- I have references describing different patterns for specific types of projects – like cookie cutters for web frontends, native apps, backends, etc.
- I have references that describe specific task management systems – I typically use a directory of Markdown docs locally, but if I'm working with others, I have a reference file for GitHub or Jira.

Finally, to improve my software-factory, I'm trying something very experimental (and fun). Each repo gets an independent copy of the software-factory skill. Each repo can make independent modifications to the skill as I chip off rough edges in the developer experience. I then have a meta-skill that knows how to periodically merge my changes together and then redeploy the revised software-factory to all the repos where it's used. Definitely fun – don't know if it's really useful yet 😅.

So, what's your approach? I want to know! Find me on [LinkedIn](https://www.linkedin.com/in/john-berryman-864b1713/) or [X.com](https://x.com/JnBrymn).
