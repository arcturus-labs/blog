---
date: 2025-06-17
categories:
  - Coding Patterns
  - Automation
  - Vibe Coding
description: I vibe-coded a CLI tool that summarizes YouTube videos, then used it to summarize the video of me making the tool. But the real magic? The "Recipe" pattern – a one-off, reusable doc for automating repetitive coding tasks. It's like Cursor rules, but you only eat the cookie once.
title: Recipes – A Pattern for Common Code Transformations
image: /blog/assets/recipes_for_code_transformation/bot.jpg
---


I did a thing. A very silly, very meta thing. I vibe-coded a CLI tool that summarizes YouTube videos, _recorded myself making the tool_, and then used the tool to summarize the video of me making the tool. And now, dear reader, you are reading a blog post that was largely generated from that summary. 

But the real star of the show isn't the tool, or the video, it's the **Recipe Pattern** – a way to encapsulate repetitive coding work into a one-off, reusable doc.


![Recipe Bot](./assets/recipes_for_code_transformation/bot.jpg){ align=left width=100% }


<!-- more -->

## What's a "Recipe"?

Let's say you've written a CLI tool you're proud of. You like the way it's structured, the coding pattern it uses, and the way it installs. Now you want to reuse the same patterns again, but for a different project. Do you:

- A) Spend 2 hours manually refactoring and then forget what you were doing?
- B) Have a long conversation with Cursor to instruct it how to create the new CLI tool?
- C) Write a Recipe – a doc that instructs Cursor (or whatever vibe-coding platform you're using) exactly how to repeat the magic, step by step?

Sorry, the answer is D - none of the above. But C is close. The only thing is that rather than _you_ writing a recipe, you have Cursor itself extract the recipe from a codebase.

A recipe is a markdown file that describes how to perform a coding task that you only perform occasionally. In this case I'm making a recipe that takes a rough piece of code and converts it to a well-formed and easy-to-install CLI tool.

Recipes are perfect for:

- Converting code snippets into CLI tools (the example task of this post)
- Bootstrapping new project structures (think LLM-powered cookiecutter)
- Auto-generating dashboards from your ORM
- Creating a migration script for converting from any framework/pattern/language to any other
- Reading a codebase and creating a standardized README
- Rewriting one (small) codebase from one language into another one
- Converting a run script into a minimal Dockerfile that bakes in your preferences
- Automating any somewhat complex coding task you'll need to do occasionally, but you don't want to memorize

## What's the Difference Between Recipes and Cursor Rules

In one sense... nothing. A recipe is a blob of text that is used to inform Cursor (or whatever vibe coding tool your using) about how to proceed – which sounds like a rule. However the utility of Cursor rules is a bit different than what I'm getting at with recipes. Cursor rules are often applied in all chats – they influence the general behavior of the agent. Recipes on the other hand are useful when you need them, but they are rarely used – so you definitely don't want to apply them to most Cursor sessions, and you probably don't even want them taking up space in your Cursor rules menu.

The other neat thing I'm pointing out about recipes in this blog post (especially if you watch the video below) is that you don't have to write them yourself, you can point Cursor at a codebase and tell it to extract a recipe based upon the pattern it sees in the codebase. And then later, when you need it, you drop the recipe into the prompt as basically a runbook for transforming the code in this codebase to a form similar to that of the original codebase.

## The Video: Extracting and Applying the CLI Recipe

Now... back to that video. If you watch it, it shows the process of extracting a reusable CLI recipe from an existing codebase that had a well-structured pattern for CLI tools. I then applied this recipe to another codebase that originally just had a Jupyter notebook for summarizing YouTube videos, turning it into a proper CLI tool. The cool part is how straightforward it was to extract the recipe, and how it can now be used to quickly convert future codebase or code snippets into fully functional CLI tools.

So without further adieu, here is the video. As usual - no cuts, no edits. See me in all my glory.
<figure markdown="span" style="width: 100%; max-width: 1200px; margin: 0 auto;">
    <iframe width="100%" height="500" src="https://www.youtube.com/embed/jqV4AhjhIfY" title="Vibe coding the Recipe pattern and then applying it." frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

- [Here's the repo with the final tool implementation.](https://github.com/arcturus-labs/summarize-youtube)
- [Here's the recipe that created the CLI tool, packaging, and install scripts.](https://github.com/arcturus-labs/summarize-youtube/blob/main/RECIPE.md)
- [Here is the summary of the YouTube video generated using the CLI tool created in the YouTube video.](https://github.com/arcturus-labs/summarize-youtube/blob/main/summary_of_video.md)

## What's Next? A CLI Tool That Writes Blog Posts

Now I've got a recipe for converting scraps of code into well-organized CLI tools.

If you thought this was the end of the recursion, think again. As an experiment, I wrote the first draft of this post by prompting Cursor with the text of the YouTube summary and some general guidance about what I wanted. So the obvious thing to do next is to copy the Cursor conversation into a notebook, make a half-assed prompt for writing blog posts, and then apply my new recipe to convert the prompt into a CLI tool that can write a blog post from piped in text. Maybe I'll use that tool to write a blog post about how it wrote itself.

---

### Hey, and if you liked this post, then maybe we should be friends!

- I just wrote a book about Prompt Engineering for LLM Applications. [Maybe you'd be interested in reading it.](/#about)
- Are you stumped on a problem with your own LLM application? [Let me hear about it.](/#contact-blog)
- I'm going to write lots more posts. [Subscribe and you'll be the first to know](/#contact-blog).
