---
date: 2025-12-07
authors:
  - john-berryman
categories:
  - Agentic AI
  - Development Methodology
  - Automation
  - Vibe Coding
  - Coding Patterns
description: I built a Cursor command that creates hierarchical explanations and posts them to GitHub issues. But the real story here isn't the tool—it's that I'm literally programming in English. The markdown file is the code, and the LLM agent is its runtime.
title: Programming in English
---

# Programming in English using Cursor Commands

I had a fun little experiment over the weekend. I needed to understand a codebase quickly, so I started interrogating it using Cursor. Around the same time, I discovered cursor commands and realized: "I need this capability often, let's formalize it." But it morphed into something bigger.

![Programming in English](./assets/programming_in_english/top_image.jpg){ align=left width=100% }

<!-- more -->

!!! note "Rather watch than read?"

    Here's a quick video where I walk through everything in this post.

    <figure markdown="span">
      <iframe width="70%" src="https://www.youtube.com/embed/COnNLwOSgms" title="Programming in English" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </figure>

## What I Built

I wanted a general hierarchical way to understand different questions about codebases. Not just "what does this file do" but also potehtially other things:
- "Tell me about this repo"
- "How does data flow through the system"
- "Explain how the codebase is modularize – and the interfaces are between the modules"
- Anything relating to the codebase

I wanted something hierarchical: a quick overview first, easy to click through to see the code, and easy to drill down for further details.

## How It Works: The Explain-in-Issue Command

The command follows a few simple steps:

**Step 0**: Understand the request. Verify context, research if needed.

**Step 1**: Create hierarchical markdown structure. The command generates:
- A main README with an overview
- Separate detail files for each section
- Extensive code links to GitHub (with line numbers)
- Inline links to the details files linked as `([details](./file.md))`
- Inline links to online references linked as `([ref](url))`

**Step 2**: Create GitHub issue. The README becomes the issue description, and each detail file becomes a comment. The command captures all the comment URLs.

**Step 3**: Link everything together. Replace file links with GitHub comment URLs and update the issue description with the final links.

The output is a single link to the explanation issue which is really easy to share with others and really easy to navigate by just clicking around on the links. See the video above for a demonstration of this in action. You can also see the actual output, an [example issue explaining a toy chatbot repo that I built](https://github.com/arcturus-labs/llm_playground/issues/5).

## The Big Idea: Programming in English

Here's what's really cool about this: I created a natural language markdown file that executes as a program. Heck, the "program" itself was vibe-coded—meta-programming in natural language. This is literally programming in English.

The command is just a specification document that gets executed step-by-step. This represents a new paradigm: natural language specifications as executable workflows.

It's super flexible—it can even do research outside of software. Check out this [Japanese-US economic relations example](https://github.com/arcturus-labs/llm_playground/issues/4) where it researched the web and provided justified references with links. As best I can tell, Cursor is quickly becoming the "anything agent" — and I wonder if they have even noticed this at this point (... we should talk Aman, Sualeh).

## Conclusion

Simple idea, powerful results. If you want to try it yourself, here's the [cursor command gist](https://gist.github.com/JnBrymn/ca8b82ebd87b7fda0218b3bc90cfd878). Stick it in your Cursor today — I think it'll be useful to you, too.

What I'm strarting to see is even more than [natural language as spec](../blog/spec-driven-development-breaks-at-scale-and-how-to-fix-it.md) — this is the English spec being run _as code_, and the large language model agent being its runtime. It's a brave new world, folks!

---

### _Building something cool with AI?_

If you're experimenting with programming in English, vibe-coding your way to automation, or building your own "anything agent," I'd love to hear about it. [Drop me a line](/#contact-blog) — I'm always curious what others are discovering in this space.

And if you want to stay in the loop on more posts like this, [subscribe here](/#contact-blog) and you'll be the first to know when new content lands.
