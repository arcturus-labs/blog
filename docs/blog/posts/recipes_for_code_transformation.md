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


I did a thing. A very silly, very meta thing. I vibe-coded a CLI tool that summarizes YouTube videos, _recorded myself making the tool_, and then used the tool to summarize the video of me making the tool. And now, dear reader, you are reading a blog post that was largely generated from that summary. If you're not dizzy yet, you will be by the end of this post.

But the real star of the show isn't the tool, or the video, it's the **Recipe Pattern** – a way to encapsulate repetitive coding work into a one-off, reusable doc.


![Recipe Bot](./assets/recipes_for_code_transformation/bot.jpg){ align=left width=100% }


<!-- more -->

## What's a "Recipe"?

Let's say you've written a CLI tool you're proud of. You like the way it's structured, the coding pattern it uses, and the way it installs. Now you want to reuse the same patterns again, but for a different project. Do you:

- A) Copy-paste a bunch of files and hope for the best?
- B) Spend 2 hours refactoring and then forget what you were doing?
- C) Write a Recipe – a doc that instructs Cursor (or whatever vibe-coding platform you're using) exactly how to repeat the magic, step by step?

Sorry, the answer is D - none of the above. But C is close. The only thing is that rather than _you_ writing a recipe, you have Cursor itself write the recipe for you. A Recipe is a markdown file that describes how to perform a coding task that you only perform occasionally. In this case I'm making a recipe that takes a rough piece of code and converts it to a well-formed and easy-to-install CLI tool.

Recipes are perfect for:
- Converting code snippets into CLI tools (the example task of this post)
- Bootstrapping new project structures (think LLM-powered cookiecutter)
- Auto-generating dashboards from your ORM
- Creating a migration script for converting from any framework/pattern/language to any other
- Reading a codebase and creating a standard README
- Converting a run script into a minimal Dockerfile that bakes in your own preferences
- Automating any complex coding task you'll need to do occasionally, but you don't want to memorize

## What's the Difference Between Recipes and Cursor Rules

Mmmm... not much. As a matter of fact, when you have a recipe, you can save it as a Cursor rule. Just make sure it requires manual inclusion so that it's not automatically applied in every conversation. I guess the main difference is that the recipe is not something you'd want to use all the time, so it might be annoying to have a cursor rule that is rarely used (though useful when you need it!). 

The other neat thing I'm pointing out about recipes here (especially if you watch the video below) is that you don't have to write them yourself, you can point Cursor at a repo and tell it to extract a recipe based upon the pattern it sees in this repo.

## The Video: Extracting and Applying the CLI Recipe

Now... back to that video. If you watch it, it shows the process of extracting a reusable CLI recipe from an existing repo that had a well-structured pattern for CLI tools. I then applied this recipe to another repo that originally just had a Jupyter notebook for summarizing YouTube videos, turning it into a proper CLI tool. The cool part is how straightforward it was to extract the recipe, and how it can now be used to quickly convert future repos or code snippets into fully functional CLI tools.

So without further adieu, here is the video. As usual - no cuts, no edits. See me in all my glory.
<figure markdown="span" style="width: 100%; max-width: 1200px; margin: 0 auto;">
    <iframe width="100%" height="500" src="https://www.youtube.com/embed/jqV4AhjhIfY" title="Vibe coding the Recipe pattern and then applying it." frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

- [Here's the repo with the final tool implementation](https://github.com/arcturus-labs/summarize-youtube)
- [Here's the recipe that created the CLI tool, packaging, and install scripts](https://github.com/arcturus-labs/summarize-youtube/blob/main/RECIPE.md)


<details>
<summary>Here is the summary of the YouTube video generated using the CLI tool created in the YouTube video</code></summary>

```
- Tool introduction and purpose  
  Summary: Introduces a tool converting URLs to markdown and a new similar tool for YouTube video summaries.  
  First occurrence: 2.32 - "I've got a tool that I created called"  
  Most important: 51.84 - "grabs a YouTube video, grabs its transcript, and then uh turns it into a summary with like timestamps and stuff"

- Goal of the experiment  
  Summary: Plans to extract a reusable recipe for creating command line tools and apply it to the YouTube summary tool.  
  First occurrence: 69.28 - "is super meta. Basically, I want to extract the pattern I used here to create uh an uh create a um command line application."  
  Most important: 92.72 - "the recipe effectively to do that and then apply the recipe today to the uh YouTube summary command that I want."

- Review of existing tool structure  
  Summary: Examines the current project structure, focusing on essential files for CLI tools.  
  First occurrence: 196.08 - "I'm going to create a recipe that will generate command line tools which look similar in organization to the command line tool of this directory."  
  Most important: 296.32 - "I think the init is important, the main's important, the CLI is important."

- Adjustments to the recipe and project structure preferences  
  Summary: Specifies which parts of the structure and dependencies matter or don't for the recipe.  
  First occurrence: 346.08 - "So, here's some changes to make with the above ideas that you've extracted."  
  Most important: 373.759 - "I do care about the project structure. Uh it should look roughly like what you have there."

- Writing the README and installation instructions  
  Summary: Creates a README explaining how to convert code into globally available CLI tools.  
  First occurrence: 495.919 - "create a readme file that explains how to take a repo or a folder that has a CLI file inside of it."  
  Most important: 686.24 - "This is how you install it in that virtual environment. That's what I actually care about."

- Testing the recipe with the YouTube summary tool  
  Summary: Attempts to apply the recipe to the YouTube summary code and test the resulting CLI tool.  
  First occurrence: 768.0 - "Now see if it works. All right, I'm go to Scratch. I'm going go to summarize YouTube."  
  Most important: 1194.96 - "It's taking a while. It's a chance it might actually work."

- Final reflections and success confirmation  
  Summary: Confirms the CLI tool works and reflects on extracting a reusable recipe for making CLI tools.  
  First occurrence: 1240.88 - "That appeared to work. Cool."  
  Most important: 1251.36 - "what I did was extracted a cool pattern for taking whatever code I felt like making today and turning it into a command line tool that installs globally."
```

</details>

## What's Next? A CLI Tool That Writes Blog Posts

Now I've got a recipe for converting scraps of code into well-organized CLI tools.

If you thought this was the end of the recursion, think again. As an experiment, I wrote the first draft of this post by prompting Cursor with the text of the YouTube summary (above) and some general guidance about what I wanted. So the next obvious thing to do is to copy the Cursor conversation into a notebook, make a half-assed prompt for writing blog posts, and then apply my new recipe to convert the notebook into a CLI tool that can write a blog post from piped in text. Maybe I'll use that tool to write a blog post about how it wrote itself.

---

### Hey, and if you liked this post, then maybe we should be friends!

- I just wrote a book about Prompt Engineering for LLM Applications. [Maybe you'd be interested in reading it.](/#about)
- Are you stumped on a problem with your own LLM application? [Let me hear about it.](/#contact-blog)
- I'm going to write lots more posts. [Subscribe and you'll be the first to know](/#contact-blog).
