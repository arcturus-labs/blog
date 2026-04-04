---
draft: true
date: 2026-03-22
authors:
  - john-berryman
categories:
  - Agentic AI
  - AI History
  - Product Development
description: From document completion to agentic runtimes - a tour through every era of AI product development, and what it means for what you should build next.
title: The Shifting Sands of AI Product Development
---

At the end of 2022, ChatGPT launched and immediately set records as the fastest-rising consumer product of all time. It gave us a glimpse of something genuinely alien. Humans are special - we make tools. But for the first time ever, we made a tool that could speak back.

Since then, we've seen several eras of growth. Ideas and approaches have come and gone as we've tried to figure out how to actually use this thing. With every era, the good ideas of the last are trained into the models, incorporated into their APIs, encoded as best practices, and often obscured by a new layer of abstraction.

We are now at the beginning of a new era - and this one is going to make the earlier ones look like a warm-up act.

In this post I'll walk through the history of AI product development, the present revolution, and what might be coming next. If you're building AI products, you need to understand this trajectory: to avoid building things that get immediately disrupted, to build things that hold up over time, and to take full advantage of what the technology can actually do.

<!-- Image: evolving AI - like the classic march-of-progress monkey drawing -->

# The eras of AI history:

## 2022 – Document Completion and the Age of Prompt Engineering

In the beginning was the Prompt.

I was an early product engineer for GitHub Copilot - you remember it, right? You'd start typing in your editor and it would complete whatever was in front of your cursor. Copilot was the purest expression of what the underlying technology actually was at that point: a document completion engine.

Think of the early models as being similar to the autocomplete on your iPhone when you're composing a text message – it reads your text so far and suggests the next word. Large language models of this era did the same thing except that they were trained on a vastly larger corpus – essentially all publicly available text on the internet, and therefore much more accurate. Given a scrap of text, they would find the statistically most likely next word, then the next, then the next. Do that enough times and you've completed the document.

<!-- Image: a document cut in half - the model filling in the bottom half -->

Because the training data included enormous amounts of code, and because code is more structured and predictable than human speech, these models turned out to be fantastic for code completion. Copilot was the first killer app of the AI era, and it was built on this simple trick.

But the models were clumsy. Getting them to produce anything reliably useful required a collection of workarounds – tricks really. These tricks were collectively called *prompt engineering*.

**Few-shot examples.** The GPT-3 paper, ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)), was the landmark that put this on everyone's radar. LLMs are pattern matchers. If you asked the model "What is the capital of Belarus?" then rather than just telling you the answer, the model would see a pattern - questions about capitals – and it would continue:

```
What is the capital of France?
What is the capital of Japan?
What is the capital of Australia?
What is the capital of Canada?
What is the capital of Egypt?
What is the capital of Brazil?
What is the capital of Sweden?
```

The fix was to prime it with a few examples first and _then_ ask the question that you really wanted answered:

```
What is the capital of Spain? Madrid.
What is the capital of Italy? Rome.
What is the capital of Germany? Berlin.
What is the capital of Belarus?
```

"Minsk!"

**Chain-of-thought reasoning.** If you ended the setup portion of your prompt with "Let's think step by step," ([Wei et al., 2022](https://arxiv.org/abs/2201.11903)) the model would work through its reasoning before answering - and the answer was usually better for it.

Without chain-of-thought:
```
Q: If you have one bucket that holds 2 gallons and another bucket that holds 5 gallons, how many buckets do you have?
A:
```

"There are 7 buckets!"

With "Let's think step by step":
```
Q: If you have one bucket that holds 2 gallons and another bucket that holds 5 gallons, how many buckets do you have?
A: Let's think step by step.
```

The model would then think out loud which effectively provided more context to reason over and the result would often be a better answer. In this case the continuation might read "The question is asking how many buckets there are, not how many gallons they hold. There is one bucket plus another bucket. Therefore, the answer is 2."

**ReAct.** Researchers figured out you could describe hypothetical tools in the prompt - search engines, calculators, etc. - and the model would attempt to "call" them ([Yao et al., 2022](https://arxiv.org/abs/2210.03629)).

```
User: Which city is warmer right now, Boston or Miami?

Thought: I should check the current weather for both cities.
Action: get_weather("Boston")
Observation: 48 F
Action: get_weather("Miami")
Observation: 81 F

Answer: Miami is warmer right now.
```

**Chat.** Possibly the silliest trick: you can craft a document that opens with "The following is a transcript between a brilliant assistant and a user," provide a few fake exchanges, and the model would keep the transcript going. If the end of the document had the text "assistant: " then the model would be oblidged to complete the text of the assistant. You would just need to make sure that you stopped the completion if you saw the text "user: " because that would be the model fabricating the entire rest of the conversation. You could then show the real human user the assistant response, allow the human to make their own reply, and incorporate that into the growing transcript – thus chat was born.

```
The following is a transcript between a brilliant assistant and a user.

assistant: How can I help you today?
user: Write a polite reply declining a meeting because I'm traveling.
assistant:
```

The model would simply continue the transcript with something like:

```
Of course - here's a polite reply:

"Thanks for the invitation. I'll be traveling that day and won't be able to make it, but I'd be glad to reconnect afterward."
```

I was playing with all of these things in 2022. I even wrote an interview coding challenge at GitHub that asked engineers to build a working chat assistant using only document completion - [here's it is](https://gist.github.com/JnBrymn/bcd0e1edcc6d8c310b889d0cd0e43565) if you want to try it.

Albert Ziegler (a founding research engineer on Copilot) and I documented this era's hard-won tricks in our O'Reilly book, [*Prompt Engineering for LLMs*](https://amzn.to/4gChsFf).

## 2023 – The Chat and Tool-Calling Revolution

This is also where the defining meta-pattern of AI development first became clear: whatever the prompt engineers figure out in one era gets aggressively fine-tuned into the models and folded into the APIs of the next.

ChatGPT launched in November 2022 and institutionalized the transcript trick. The jump in usefulness was immediate. Rather than coaxing answers out of a completion engine, you could hold a real conversation – the model stayed on topic, remembered what was said, responded to corrections. Much easier to direct.

Then in May 2023 OpenAI fine-tuned models to interact with tools, baking in the ReAct pattern. Accuracy was shaky at first, but the move was huge: the models now had eyes to read data outside the prompt, and hands to act on the world. Under the hood it was still document completion – the document just grew to accommodate tool calls and their responses.

## 2024 – Workflows Put LLMs on Rails

By now you could string LLM calls together and hand a model a set of tools. The temptation was to just let it run in a loop. The problem: given that much freedom, models would wander off task and start making things up.

The answer was workflows – treating each LLM call as a node in a directed graph, with defined inputs and outputs. Rather than one long improvised session, you broke complex jobs into discrete steps. Workflows kept the work on the rails and made it possible to get real results on hard tasks.

RAG was also a dominant theme in 2024, but I'll admit I never quite understood the fuss. RAG is just LLMs combined with a search tool. If retrieval is broken, there are 30 years of industry knowledge on how to fix it (buy [*Relevant Search*](https://amzn.to/3TXmDHk)). If the LLM isn't behaving, fix that too (buy [*Prompt Engineering for LLMs*](https://amzn.to/4gChsFf)). There's no reason to treat RAG as a black box – it's a pipeline.

# 2025 – The Year We Figured Out What "Agent" Means

In February 2025, at the AI Engineering conference, Grace Isford of Lux Capital [declared that this would be the year of agents](https://www.youtube.com/watch?v=HS5a8VIKsvA). She was right - but the real accomplishment of 2025 was just agreeing on what an agent actually was.

The term was a mess. Some teams were making a single LLM request to extract structured data from a webpage and calling that an agent. Some said workflows were a form of agency - I'll admit I made that mistake in my own book. But "agency" has a straightforward definition in the dictionary: _the ability to make decisions and act independently_. A single LLM call, a chain, or a workflow isn't acting under its own agents, it's just doing what it's told, with the decision points happening algorithmically.

The winning paradigm turned out to be simple: a for loop, with callouts to the LLM and tools. You give it a task, and _it decides_ how to proceed - which tools to call, what to do with the results, when it's done. Whether or not LLMs have a genuine _will_ is a philosophical quibble, but this at least meets the functional definition of agency. And if you want your agent to behave like an assistant, you just add another loop around the outside and keep appending the user's messages to the context.

One thing that pushed the field toward a clear answer was the arrival of reasoning models. OpenAI introduced them in late 2024, then DeepSeek-R1 showed up in January 2025 and stole the show - comparable reasoning quality at a tiny fraction of the cost. For loop-based agents, which need a model that can stay oriented over many steps, this mattered a lot.

That said, the early agents were pretty useless. Keeping a loop on task was hard, and the models weren't reliable enough to be trusted with anything consequential. But reasoning steadily improved throughout the year, and by late 2025 several observers independently called out a step-change improvement in agent capability.

!!! note "The November 2025 inflection point"

    Several prominent observers independently called out the same moment.

    **[Andrej Karpathy](https://twitter.com/karpathy/status/2026731645169185220):** "Coding agents basically didn't work before December and basically work since - the models have significantly higher quality, long-term coherence and tenacity and they can power through large and long tasks."

    **[Simon Willison](https://simonwillison.net/2026/Jan/4/inflection/):** "GPT-5.2 and Opus 4.5 in November represent an inflection point - one of those moments where the models get incrementally better in a way that tips across an invisible capability line where suddenly a whole bunch of much harder coding problems open up."

    **[Paul Ford, NYT](https://www.nytimes.com/2026/02/18/opinion/ai-software.html):** "[Claude Code] was always a helpful coding assistant, but in November it suddenly got much better, and ever since I've been knocking off side projects that had sat in folders for a decade or longer."

    **[Max Woolf](https://minimaxir.com/2026/02/ai-agent-coding/):** "It's impossible to publicly say [the models] are an order of magnitude better than coding LLMs released just months before without sounding like an AI hype booster clickbaiting, but it's the counterintuitive truth."

By the end of 2025, the agentic frameworks were also converging. The main ingredients - agent instructions, tools, memory - had settled into recognizable patterns across the major platforms. Subagents were still a rough edge: coordinating context between them without stomping on each other's work was fiddly. But a good first-order approximation is to just treat a subagent as a tool that happens to use an LLM internally - the main agent doesn't need to know or care. (Context management for subagents has also been getting easier; a March 2026 leak of Claude Code's internals revealed that subagents receive the full context of the parent agent, which is both information-rich and cache-friendly.)

The big shift in focus from earlier eras: rather than fine-grained prompt engineering tricks, the dominant abstraction in 2025 was context management. What does the agent need to know, when does it need to know it, and how do you keep the context window useful rather than bloated?

## 2026 – The Agentic Runtime

Right now people in the software development world are calling it a "harness" – all the scaffolding that surrounds your agents and runs them: the agentic loop, tool handling, session and context management (compaction, skills, memory), sandboxing, subagent orchestration. Some prominent examples are Claude Code, Codex, Cursor, and OpenCode.

But the harness metaphor is too narrow. We're already seeing it extend beyond code. Claude Cowork and OpenClaw are the most obvious examples – they're essentially coding agent harnesses with more flexible input and output (voice, email, whatever) and less rigid expectations about the work being done. The name "harness" won't stick (I hope).

What we're really seeing is the emergence of an _agentic runtime_. Think of it like a code interpreter – The Python interpreter takes structured source code and executes it. The agentic runtime takes English (or whatever language you prefer) and executes _that_, using available tools to get real work done. The difference is that a code interpreter does exactly what the code says. The agentic runtime understands what you're getting at, and can be creative in addressing your problem – including wild things like writing its own tools to make work easier and more repeatable, or spinning off subagents to parallelize the load.

The key new development that makes this click – in my opinion – is [agent skills](https://docs.anthropic.com/en/docs/claude-code/skills), introduced by Anthropic in October 2025. On the surface, skills are a ridiculously simple idea: a folder with a `SKILL.md` that acts as a README for a specialized task, with optional subdirectories, explanatory markdown, and runnable scripts. You tell the runtime to use skills as needed, and it does.

But it's deeper than that. Anthropic realized its models – and the frontier models generally – have become very good at navigating a filesystem, working at a command line, and using an operating system. Skills allow these agentic runtimes to leverage constructs the models already know intimately, which gives agents a natural leg up compared to arbitrary tool APIs for which the model has no trained-in intuition.

If English is the new programming language and the agentic runtime is the new interpreter, then the agent skill is the program itself. I've already written powerful programs with agent skills – including [building a simple OpenClaw clone in 15 minutes](openclaw_clone_in_15_minutes.md). And there are now places online where you can download skills like software libraries, because that's basically what they are – with package management systems starting to appear to manage them.


- We're still in the early days of the agentic runtime. And like all eras before, you'll see the good ideas get slurped up and fine-tuned into the models, added to the agent APIs, and formalized into standards. Here are some of my guesses for what's coming next.
  - context management will become completely standardized – the frontier labs will discover more and more efficient automatic ways to do memory extraction and context compaction, and progressive disclosure of skills instructions; this will become trained into models so that they just do the right thing – for my hint on how this might work, see my post on infinite compaction <this is another fake post that I want to see if anyone is clicking on it  so create a placeholder post for that and link to it - make the placeholder say "coming soon" - make sure it doesn't show up in the mkdocs Material blog page>
  - we'll start to see skills packaged up as stand-alone products which can be run in your agentic runtime of choice (are you an Anthropic man, Stan?)
    - they will be opensource by default (because it's hard to close source English), but they might not be free - so we'll have to figure out what to do to protect IP
    - all skills will also be modifiable by default - I can easily imagine a skill editing skill that allows you to understand the functioning of existing skills and update them to match your preferences... what's that going to do to IP ownership?
  - Orchestration will continue to morph. Remember, originally it was us creating workflows. And now we write the workflow state machine inside of loose English prose in skills and let the main agent determine if it wants to use subagents. Soon, higher-level workflows will form that are effectively at the level of the business. They will be composed of decoupled agents each with their own roles, goals, instructions, and tools. And they will communicate by loosely constructed message passing interfaces - and if I had to make a bet, this loose interface will be good ol' email (after all, there's plenty of email in training data). And you know who will be one of the agents in this network? You! You will be an agent working with a mix of AI and human colleagues - strange but true

- Agents will be the building block for everything in the future. The agents will all run on this agentic runtime, and "programming" the agents will be as simple as providing them with the english-written skills they need and specialized tools (that they might very well just build themselves).


# Conclusion: Building for success
- Albert and I told O'Reilly that the important abstraction was document completion... but we weren't right for nearly as long as we thought. In the past 4 years several eras have passed, each burying the document completion abstraction in another layer....
- The Agentic Runtime isn't the last abstraction either.
  - With world models and robotics, we're getting all the pieces in place for embodied cognition
  - We are also working hard on making it so that models can perform continously learning. This will make agents much more than their instructions because they will be able to learn the nuances of their jobs through trial and error and correction – just like us meat computers.

- It's challenging to give general advice when I don't know what you're working on, but through all the changes a key intuition has been empathy - It's always been weird that I find myself delivering this message, because my wife tells me I'm kinda like a lizard emotionally. But I actually don't mean the touchy feely type of emotional empathy - I mean cognitive empathy – can you put yourself in the shoes of the agent and of the user and make sure they have what they need to get the job done?
  - agent – context engineering, tool descriptions, skills, instructions - does your intern have what they need and can they understand it? If the answer is "yes" then increasingly the agents will deliver success
  - user – users intereacting with the AI system need to understand what the agents are doing, the conversation about work needs to be separated from the objects of work, the agent's reasoning needs to be visible, auditable, and explainable. The user needs to be able to _see_ what the agent is doing and redirect it and _teach_ it when it gets off course.
  - lean into things that are familiar to the models – these days it is the notion of a filesysetem and a command line
- The other piece of advice is to try to see the trajectory, not just a snapshot in time.
  - Whatever we're interested in right now in this current news cycle isn't the be-all-end-all, but looking back we can see the trajectory - attempt to project that trajectory forward - you'll be _wrong_ but the exercise is useful.
  - English will be a runnable software language - it already is
  - Agents are the worst that they will ever be going forward becuase the technology is still on a more-or-less exponential upswing. Agents that are laughable today will be awesome in no time at all. Everyone will have a personal agent... which is actually a legion of agents at your bidding.
  - The internet for humans will go away and be replaced with an internet for agents and highly personalized apps for humans - humans will work with agents to make the personalized apps
  
- It's a brave new world. Make the most of it.



# Don't forget:
- [ ] Label these as eras better - and have a fixed number and name for each
- [ ] Make it a little more terse than my normal posts
- [ ] Add images for every section
  - [ ] insert plot of time-length of task that are getting done and how it's on an exponential?
- [ ] Make sure this is not a draft but also not listed in the "blogs" list [building a simple OpenClaw clone in 15 minutes](openclaw_clone_in_15_minutes.md)

Follow-up
- [ ] Make myself a speaker on this topic everywhere
- [ ] Notify these people and get them to repost
  - [ ] Grace Isford
  - [ ] swyx
- [ ] add TODO to write participatory UX post
- [ ] advertise with shock - "AI Product Developers - in a couple of months you will never need to build another AI agent"