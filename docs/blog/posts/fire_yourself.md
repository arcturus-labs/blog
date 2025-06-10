---
date: 2025-01-17
categories:
  - Agentic AI
description: Discover how to build reliable LLM applications by applying the E-Myth's systematic approach to automation. Learn why starting with human processes and incrementally automating tasks leads to more robust LLM applications. Perfect for startup founders and teams struggling to harness the power of LLMs effectively.
image: /blog/assets/fire_yourself/top_image.png
---

# Fire Yourself First: The E-Myth Approach to Iteratively AI App Development

I've always been interested in entrepreneurship, so, early on in my career, I asked my financial advisor for book recommendations about startups. He handed me "The E-Myth" by Michael Gerber – a book about... building food service franchises? In the heat of the dot-com explosion, this wasn't exactly the startup guide I was hoping for, but its core message stuck with me and turned out to be surprisingly relevant to the problems I hear about regularly when talking to people about building reliable LLM applications.

![Fire Yourself](./assets/fire_yourself/top_image.png){ align=left width=100% }

<!-- more -->

The E-Myth's central insight is really quite simple: in any business, there are tasks to be done, and each task has steps. As a founder, you start by doing everything yourself, but that won't scale. The solution? Document and systematize those steps so that you can train others to do the work – effectively "firing yourself" from each task.

This approach actually serves as a great metaphor for how you should iteratively build and improve LLM applications! Let's dive in.

!!! note "Blog posts not your thing?"

    Text got you down? Then check out the _completely unedited_ companion YouTube video. Watch me deliver the same information as the post, and in the same time that reading would have required.

    <figure markdown="span">
      <iframe width="70%" src="https://www.youtube.com/embed/f5qWjbD-_xY" title="Fire Yourself First" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </figure>


## The Problem with Typical LLM Development

As Simon Willison astutely observes: "The key skill in getting the most out of LLMs, is learning to work with tech that is both inherently unreliable and incredibly powerful at the same time. This is a decidedly non-obvious skill to acquire!"

He's right. LLMs are remarkably capable, but they're also gullible and prone to hallucination which makes it is easy for them to get off track when reasoning through complicated tasks. This makes building complex LLM applications on the first try basically impossible. Yet many teams attempt to do exactly that – diving straight into building hordes of complex AI agents without first understanding the human processes they're trying to automate.

The solution? Take a page from the E-Myth: Start by doing the work manually, document your processes, and then systematically automate each task. Don't try to build an AI agent that can do everything – build a system where you can gradually fire yourself from specific, well-defined tasks and let the LLM take over.

## A Real-World Example: The Recruiting Startup

Let me share a recent example that serves as a great illustration for this approach. I recently spoke with a founder who was single-handedly building a startup that focused on recruiting. His platform needed to:

1. Analyze résumés and extract structured data
2. Evaluate candidate quality
3. Match candidates with job postings
4. Handle communication with candidates throughout their job search

Instead of attempting to build an all-encompassing AI solution from day one, he started with a process that was largely manual. He personally handled each step, which allowed him to understand the nuances and challenges of each task.

Then, piece by piece, he began to automate. First, he "fired himself" from data extraction – a repetitive task with clear inputs and outputs. Next came candidate quality evaluation. Since this was already somewhat subjective, transitioning to AI-generated ratings (after careful validation) made sense – he built an LLM-as-judge setup that would read resumes and rate candidates on a five point scale.

His next target? The communication workflow. But rather than haphazardly building an agent to do _all_ communication with candidates, he's taking an incremental approach by initially just automating email drafts.

From here, there are plenty of things that he can work on next, at each step letting the work itself dictate which task is most applicable for handing over to an LLM. Perhaps he'll find that the communication drafts require too much human editing, and he may introduce a more involved assistant workflow to pen those communications (for instance starting with an email outline that will be easier for the recruiter to review and update). Another possible next step is to introduce evaluation and improvements in the candidate ranking process to ensure that the LLM-as-judge generally agrees with human judges.

## Incrementally Incorporating Agency into your Application

Here are some general guidelines to help you incrementally incorporate more and more AI Agency into your application.

### 1. Identify your First Target

Create a list of tasks that might be good candidates for replacement. We're most likely looking for one of two forms:

1. Tasks that are easily described as a set of steps with well-defined inputs and outputs. <!-- FUTURE POST - chapter 8 assistant agency -->
2. Tasks that involve a human working together with an LLM assistant in order to accomplish a goal. <!-- FUTURE POST - chapter 9 workflow agency -->

For the current state-of-the-art for LLMs, it's advisable to stay away from complex, open-ended reasoning tasks – remember, these models are incredibly capable, but not incredibly reliable just yet.

Look for tasks that are expensive and timeconsuming for a human to complete, such as extracting structured data from documents or generating content. Also, look for tasks that are more amenable to occasional failure, because getting _100%_ correctness from a non-deterministic component such as an LLM is going to be really challenging.

### 2. Map the Human Process

For each module:

- Identify the inputs and outputs, and make sure they are well-defined.
- Document the steps that a human would take in accomplishing the task of the model. This needs to be something you could explain to a new employee, because you're about to onboard the AI agent _as_ your new employee. Does the agent need tools? Be able to explain them. Will the agent be assisting a human? Be able to explain the expectations of the interaction.
- Track which steps are repetitive or time-consuming, but not overly complex. This will give you an idea about where to get started when replacing yourself with an AI agent.

### 3. Fire yourself! Make the Robots do the Work

If your application is well-modularized, then ideally you can replace chunks of code with their LLM-enhanced equivalents. The idea is to keep the well-defined inputs and outputs, and keep the goals the same, but replace the human interaction part with an AI-assisted version. Naturally, this is sometimes this is easier said than done.

Nobody likes eating their veggies it seems, but it's also important to perform evaluations on your new modules to make sure they have the desired behavior. However, here too, you can be incremental in your approach. If the module is amenable to occasional failure, and if there is plenty of other lower-hanging fruit that you need to tackle, then your evaluations can be pretty superficial at first. Try 20 different inputs of varying forms, throw some curveballs and corner cases at the module, and make sure that none of the outputs would be damaging to your application or embarrassing to your company. Eventually though, you should certainly come back and perform proper evaluations (more on that in a future post.)
<!-- FUTURE POST how to evaluate llm agents -->

### 4. Iterate! Recurse!

Create a pattern of continual optimization. As soon as you fire yourself from one position and hire an AI agent, check your list for the next task that can be turned over to the agent. Keep doing this until you start running into diminishing returns. Fortunately, you're racing against a technology that is improving by leaps and bound every day. With any luck, that wall of diminishing returns will continue to be pushed in front of you.

## Conclusion
The path to reliable agentic applications isn't through ambitious, all-at-once automation. It's through systematic, incremental improvement. Start by doing the work yourself, understand it deeply, and then gradually fire yourself from each task by building focused, reliable AI agents.

This approach might seem slower at first, but it's far more likely to succeed. You'll build something that actually works, understand where the limitations are, and know exactly how to evaluate and improve each component.

--- 

### Hey, and if you liked this post, then maybe we should be friends!

- I just wrote a book about Prompt Engineering for LLM Applications. [I bet you'd be interested in reading it.](/#about)
- Is your company working on AI Agents? [I'd love to hear about it. I can help you stay ahead of the curve and make the most of AI technology.](/#contact-blog)
- I'm going to write lots more posts like this. [Subscribe, and know as soon as new content lands.](/#contact-blog).
