---
draft: true
date: 2026-03-22
authors:
  - john-berryman
categories:
  - Agentic AI
  - AI History
  - Product Development
description: From document completion to agentic runtimes — a tour through every epoch of AI product development, and what it means for what you should build next.
title: The Shifting Sands of AI Product Development
---

# instructions to AI
The following is a really rough outline - it's part outline part prose - it lists all the ideas I want to write about (unless explicitly stated otherwise). I will ask you to start converting stuff to prose. Try to be mindful of some of my ideosyncracities (like quotes and parens usage) - refer to other blog posts for other samples. I'll have some commands for you in the text like this <do this thing> - so do it when we're dealing w/ that part of text

# Lead in
- at  the end of 2022 ChatGPT was released, immediately set records for fast rising consumer product of all time, and gave us a glimpse of an alien technology - Humans are special, in that we make tools. But for the first time ever, we made a tool that could speak back.
- Since then we have seen several waves growth, ideas and approaches have come and fallen as we have worked to understand how to use this technology
- But we are currently at the beginning of a new wave of interruption and this one is going to make the others look like child's play
- In this post we will cover the past epochs, the present revolution, and what we might have in store in the future
- If you are building AI products, it will be critical to understand this so that you won't be left behind - you'll need to understand this so that you can build products in a way that won't be immediately disrupted (and you have to build them again), and you'll need to know this so that you can build products that will work well into the future, you need to know this so taht you can build products taht take advantage of the technology to the max
- (Image - evolving AI - like old monkey drawing of evolution)

# The epochs of AI history:

## 2022 – Document Completion and the age of Prompt Engineering
<missing from this section is a discussion of Copilot as the epitome of completion epoch>

- In the beginning was the Prompt. (as quoted "big text"?)
- I was an early product engineer for GitHub Copilot - you remember... it completed the text in front of your cursor?
- At that point there were only "instruct models" - they were simple - basically they were the that silly middle button on your iPhone that autocompletes a single word at a time. Given the top half of a document, the would find the statistically most like next word, then next, then next - if you do it enough, then you complete the document.
- <insert image of a severed document>
- A big difference between LLMs (**large** language models) and the iPhone text complete – LLMs were "pre-trained" on all publically available text and it served as a REALLY splendid statistical model of text. In particular, there was a lot of code in the training set, and since code is simpler than human speech, it was surprisingly good at completing code documents
- But these models were clumbsy, and we had to devise a bunch of tips and tricks to geet them to make useful outputs. These tricks were collectively called "Prompt Engineering". Early tricks:
  - Few shot examples - LLMs are pattern matchers - if you jsut asked "What is the capital of Belarus?" in the prompt, then the completion to that document would likely be several more questions elaborating on this pattern: "what is the capital of Spain? What's the capital of Italy? What's the capital of Germany?" etc. - So you have to show it a pattern of examples and then it would complete from these: "what is the capital of Spain? Madrid. What's the capital of Italy? Rome. What's the capital of Germany? Berlin" and then you could ask your actual question and it would complete the pattern "What is the capital of Belarus?" --> "Minsk!"
  - chain-of-thought reasoning - If the models reasoned in text about an answer, then the answer was likely better, so we ended the first part ofthe document with "Let's think step by step" <link out to this paper from arxiv> and the model would churn out a string of reasoning and ultimately figure out better answers
  - reAct - we figured out that you could tell the model that it had access to tools that could be used for accessing data or manipulating the environment and ... it worked enough to make gimicky demos. But they also did some fine tuning around tool usage examples and it got pretty good <link to this paper form arvxi>
  - chat - amusingly - silly little trick - you could make a document that at the top said "this is a transcript between a very smart assistant and a user" and then you would give it the fake transcript - messages like "assistant: how can I help you toayd?\nuser: What is 42*14?\nassistant:" and the model would complete the fake transcript document as "The answer is 824" (models weren't too good at math, you see).
  
- I remember building these things in 2022! As a matter of fact, I wrote a really awesome interview coding challenge at GitHub to try and build a working chat assistant using only document completion. It rocked <ask for the link, I have it>.
- Heck - I even wrote a book about ALL of this stuff with Albert zeiler, one of the OG researchers on Copilot and current Xbow cheif of stuff <get his real title> ... which you can buy now for the low low price of <get price and get amazon link to book>
- LangChain was the first to realize that you could "chain" together the output of one prompt with the next and achieve interesting and complicated work. What a cool idea... (ominous foreshadowing)
  
## 2023 – The Chat and Tool-Calling Revolution
- In late 2022 the pattern was set into motion where all the cool ideas of previous epochs were aggressively trained into the models and incorporated into APIs
- In Nov 2022 ChatGPT landed, formalizing the transcript trick from completion epoch - the result was a MUCH more useful model - it wasn't just answering questions, it was engaging in conversation and staying on track - much easier to direct
- In May of 2023 OpenAI fine-tuned models to interact with tools (slurping up the reAct trick) - it wasn't particularly accurate at first but it gave the models eyes so that they could see and hands so that it could manipulate data outside of the document being completed (internally, it really is still a document completion model - it's just that the document is expected to have weird context tool calling and role switching)
  - <link out to my post on how cool tool calling is - ask John>
- Poor LangChain... the chat model introduced a useful pattern of recursively calling models and appending user and assistant messages and tool calling as the conversation got longer - LangChain's API split into two cohabitating APIs one for doc completion models, one for chat... it got weird

## 2024 - Workflows get real work done
- 2024 was the advent of workflows. Rather than just directly pipe the output of one LLM request into another LLM call (e.g. "chaining" them together), it was actually a great idea to think of each LLM request as node in a connected graph, where each node took an input and provided an output.
- This was important, because if you just started calling an LLM in a loop and gave it access to tools, then it would quickly diverge from the task you wanted to work on and start making crap up
- Workflows kept the task on rails and made it possible to achieve real results for complex things.
- LangGraph was introduced! What a smart idea. ... Except maybe they hadn't learned that naming things so specifically came with consequences (ominous foreshadowing).

- <keep this short - it's really a sidenote in this post> (Although not the focus of this post, another dominant theme for 2024 was RAG... but since I am a combination of search engineer and AI engineer I never understood the fuss. RAG is just the use of LLMs with at tool that calls search. If search breaks, lean on 30 years of industry usage and fix it (buy my first book). If LLMs aren't doing what you want, fix it (buy my second book). There's no reason to pretend RAG is a black box.)

# 2025 – The advent of agents
- In Feb of 2025 at the AI Engineering conference, Grace Isford (Lux Capital) declared that [this woudl be the year of the agents](https://www.youtube.com/watch?v=HS5a8VIKsvA).
- But what the hell was an AI agent? Just defining this term would be the real success of 2025.
  - Some were just calling LLMs, or chained LLMs in order to process a single data points, and callign _that_ an agent (for instance to extract structured content from a website).
  - Some said that workflows were a form of agency (something I sadly did in my book).
  - But the word "agency" actually has a simple definition: "the ability to make decisions and act independently" so we should go with that as a bare minimum requirement. Single LLM requests, chains, or workflows aren't making directional decisions about what they want to do – they are typically just doing the task and letting the framework make algorithmic decisions.
- The winning paradigm for agency is simple: it's a for loop with call outs to the LLM and tools. You give it an input, and _it decides_ what direction to take to make use of the tools and accumulate reasoning in order to address the task. Philosophical quibble aside about whether or not LLMs can actually have a Will, this does meet the definition of agency. 
  - If you want to make your agent an assistant, then add another for loop around the outside and keep appending user messages to the context.

- One thing that I feel drove us to a definitive conclusion was the advent of reasoning models which OpenAI introduced in late 2024, just to have DeepSeek-R1 steal the show in Jan 2025 with exceptional reasoning for an opensource model at a fraction of the price.
- Throughout 2025, reasoning got better. The early loop-agents couldn't be trusted to stay on track very well at all. (Agents were rather useless TBH.) But by the end of 2025 this had changed significantly with several prominent sourced independantly citing a step change improvement toward the end of 2025
  - <ask me about creating a call-out box with several example citations>

- By the end of 2025, agentic frameworks appear to be converging on what the main primitives are in terms of agent instructions, tools, memory, etc.
  - There are still fine points to be worked out on subagents (like context management between them and stomping on one anothers' work) - but a good first order approximation is to think of them as just tools called by the main agent - tools that happen to utilize LLMs internally, but that is an implementation detail that the main agent doesn't have to worry about
- Finally - rather than fine-grained prompt engineering approaches, the focus in 2025 was clearly at a higher level of abstraction – context management.
- P.S. LangSmith is a really nice way of recording and interrogating traces. ... Though I'm hearing less about LangGraph these days.


## 2026 - The Agentic Runtime
- It's being called a "harness" – all the pieces and parts that surround your agents and run them when you're getting work done. The pieces are things like, the agentic loop, tools handling, session management, context management (including compaction and memory), sandboxing work, and subagent orchestration.
- The reference to "harness" is primarily in the field of software development, where the harness is Claude Code, Codex, Cursor, OpenCode, etc. Increasingly though, we'll see the harness around getting any type of work done, even outside of code -  Claude Cowork and OpenClaw being very prominent examples.
- The name harness won't stick, because it's so much more than a harness. What we are seeing is the emergence of a new _agentic runtime_. This has a close analog to pre-AI code interpreter, but in this case the code is English (or whatever language you prefer), and the runtime interprets the English and uses available tools to accomplish real work.
- Importantly, whereas code interpreters could only read structured programming languages, and do only exactly what the code encode, the agentic runtime will be much more flexible. It will "understand what you're getting at" (almost like a human) and be able to do wild things like write its own tools to make it's work more easy and repeatable. It can even fire off other agents to divvy up the work.

- Besides just finally putting all these ingredients together and demonstrating that they work for the first time, the key new development in my opinion are the agent skills introduced by Anthropic <link to the official documentation> introduced in october of 2025.
- On one hand, skills is a ridiculously simple idea – have a folder with a SKILL.md that acts as a README for how to do a specialized task, and then have arbitrary subdirectories, explanatory markdown files discussing specifics as needed, and even having some runnable scripts, and then just tell the coding agent/harness/runtime to "use these skills as needed".
- But it's really deeper than that. Anthropic realized that it's models (and all the frontier models as a matter of fact) have gotten really good at using an operating system, interacting at the command line, and navigating a filesystem. So using these familiar constructs that have been trained into the models, the agents have a leg up in navigating their world, especially as compared to arbitrary tools for which it has no ingrained intuition. (This is why MCPs are on the way out.)
- If English is the new programming language, and the agentic runtime is the new interpreter, then the agent skill is the program itself. I've already written powerful programs with skill, like my post on writing a simple OpenClaw clone in 15 minutes <I haven't actually writen this, I just want to see if people are interested in this - so create a placeholder post for that and link to it - make the placeholder say "coming soon">. Similarly, there are several places online where you can download skills as if they are libraries that you can use in your work - that's because that's basically what they are, and we're seeing new package management systems come into place to handle them.


- We're still in the early days of the agentic runtime. And like all epoch's before, you'll see the good ideas get slurped up and fine-tuned into the models, added to the agent APIs, and formalized into standards. Here are some of my guesses for what's coming next.
  - context management will become completely standardized – the frontier labs will discover more and more efficient automatic ways to do memory extraction and context compaction, and progressive disclosure of skills instructions; this will become trained into models so that they just do the right thing
  - similarly, it will become clearer how to build tools that do their own version of progressive disclosure
  - we'll start to see skills packaged up as stand-alone products which can be run in your agentic runtime of choice (are you an Anthropic man, Stan?)
    - they will be opensource by default (because it's hard to close source English), but they might not be free - so we'll have to figure out what to do to protect IP
    - all skills will also be modifiable by default - I can easily imagine a skill editing skill that allows you to understand the functioning of existing skills and update them to match your preferences... what's that going to do to IP ownership?
  - Orchestration will continue to morph. Remember, originally it was us creating workflows. And now we write the workflow state machine inside of loose English prose in skills and let the main agent determine if it wants to use subagents. Soon, higher-level workflows will form that are effectively at the level of the business. They will be composed of decoupled agents each with their own roles, goals, instructions, and tools. And they will communicate by loosely constructed message passing interfaces - and if I had to make a bet, this loose interface will be good ol' SMTP email (after all, there's plenty of that in training data). And you know who will be one of the agents in this network? You! You will be an agent working with a mix of AI and human colleagues 


# Conclusion: Building for success
- ?Albert and I told O'Reilly that the important abstraction was document completion... but we weren't right for nearly as long as we thought. In the past 4 years several epochs have passed, each burying the document completion abstraction in another layer....
- The Agentic Runtime isn't the last abstraction either.
  - With world models and robotics, we're getting all the pieces in place for embodied cognition
  - We are also working hard on making it so that models can perform continously learning. This will make agents much more than the instructions in their skills files because they will be able to learn the nuances of their jobs by making mistakes and learning from them.

- It's challenging to give general advice when I don't know what you're working on, but through all the changes a key intuition has been empathy - It's always been weird that I find myself delivering this message, because my wife tells me I'm kinda like a lizard emotionally. But I actually don't mean the touchy feely type of emotional empathy - I mean cognitive empathy – can you put yourself in the shoe of the agent and of the user and make sure they have what they need to get the job done?
  - agent – context engineering, tool descriptions, skills, instructions - does your intern have what they need and can they understand it? If the answer is "yes" then increasingly the agents will deliver success
  - user – users intereacting with the AI system need to understand what the agents are doing, the conversation about work needs to be separated from the objects of work, the agent's reasoning needs to be auditable and explainable. Critically, the user needs to be able to redirect the agent.
- The other piece of advice is to try to see the trajectory, not just a snapshot in time.
  - Whatever we're interested in right now in this current news cycle isn't the be-all-end-all, but looking back we can see the trajectory - attempt to project that trajectory forward - you'll be _wrong_ but the exercise is useful.
  - English will be a runnable software language - it already is
  - The technology is still on a more-or-less exponential upswing. Agents that are laughable today will be awesome in no time at all. Everyone will have a personal agent... which is actually a legion of agents at your bidding.
  - The internet for humans will go away and be replaced with an internet for agents and highly personalized apps for humans - humans will work with agents to make the personalized apps
  
- It's a brave new world. Make the most of it.



Don't forget:
- Make skill for how to write blog posts from an outline
- I need to say early on in the intro that there has been a pattern of slurping up good ideas and training them into the models and incorporating them into APIs and formalized into standards, so that the dominant abstraction in any epoch sets on top of those from the last
- Aggressively cut the fat - make copies of old outlines
    - in 2024, shrink RAG and highlight workflows - they are closer to the agentic story I want to tell
- What ideas of come and fallen? DSPy?
- Label these as epochs - and have a fixed number and name for each
- To make sure covered
  - The RLs involved at each step (chat, )
- Make it a little more terse than my normal posts
- Check situations
- Don't shit on LangChain too much - praise LangSmith
- Add images for every section
  - insert plot of time-length of task that are getting done and how it's on an exponential?

Follow-up
- Make myself a speaker on this topic everywhere
- Notify these people and get them to repost
  - Grace Isford
  - swyx
  - LangChain
- add TODO to write participatory UX post