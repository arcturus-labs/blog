---
date: 2026-11-03
authors:
  - john-berryman
categories:
  - Reasoning
draft: true
description: Frontier models can apparently interpret neural networks from their weights written out as text. That's a capability I wasn't expecting – and it challenges my intuition about how far learned reasoning can generalize.
title: AI Can Read Neural Network Weights. I Wasn’t Ready for That.
image: /blog/assets/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/hero.jpg
---

# AI Can Read Neural Network Weights. I Wasn’t Ready for That.

Frontier models can apparently read, reason about, and even update neural network weights directly. ([Read the report here](https://rikiyat.github.io/blog/weight-space-programming/)!) They do this not by running a training loop, but by directly reading the numbers and figuring out what to change.

My first reaction was: *Wait. How the heck does that work?*

I'm used to models surprising me with what they can do with language and code. But handing one a pile of neural network weights and asking it to make sense of the behavior encoded there? That feels like a different kind of capability.

![Robot editing its own brain](./assets/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/hero.jpg){ align=center width=100% }

<!-- more -->

## This Shouldn’t Work. Right?

Here's the analogy. Human brains are made of neurons, and so are fruit fly brains. We now have a complete connectome of the adult fruit fly brain. Shouldn't we – with our very smart brains made of the same components – be able to look at that wiring diagram and make sense of it intuitively?

Of course not! That's friggin' crazy. Our brains haven't learned to read other brains. They've learned to take in sensory data and produce behaviors – move muscles and squirt hormones.

By analogy, an LLM has learned to take in text and images and generate useful output. Its being a neural network doesn't automatically give it an understanding of what the 17th weight in some other network does. And when these weights are shown to the LLM, they aren't being plugged into the LLM in some special, native neural-weight format. They're being presented as plain text.

Consider "strawberry." The model sees pieces of words – `st`, `raw`, and `berry` – rather than a sequence of individual letters. This is why in 2025 frontier models kept swearing to us that "strawberry" had 2 r's.

So when you look at one of the prompts used in this study ([here's a prompt asking the model to identify a Pac-Man-playing neural network based solely on its architecture and weights](https://raw.githubusercontent.com/RikiyaT/lm_understand-logs/refs/heads/main/exp1_which_game/runs/pacman/prompt.txt)), the model reads numbers like `0.054 -0.026 0.014`, tokenized just like any other text input. In this case: `0`, `.`, `054`, <code>&nbsp;-</code>, `0`, `.`, `026`, <code>&nbsp;0</code>, `.`, `014`. There's no special channel that turns those numbers into a network the LLM can directly "experience." Nevertheless, it can successfully pick out relationships that suggest it's looking at a Pac-Man-playing neural network.

## Where Did This Ability Come From?

You won't find much training data available on the internet that is analogous to this. Humans train neural networks, but we don't look at specific networks and write essays describing how model weights lead to various model behaviors.

So where does a model learn to do this?

This capability is so unnatural that my first instinct was that the frontier labs are explicitly training this behavior into the models so that they can take advantage of it. Clever – and surprising that this would even work at all.

The other possibility is frankly a bit startling: models are way more intelligent than I had given them credit for.


## Maybe This Is Just What Generalization Looks Like

We already train models to trace programs and reason about their behavior. And through reinforcement learning we have trained models to be quite good at extrapolating to reading and writing programs that are well outside of their training set. Maybe we're at the point where that extrapolation really goes to an extreme that I wouldn't have expected the LLMs to handle.

If I look at code, there are several things that my feeble brain keeps track of. I see where variables are defined, I see how they are manipulated, I trace Boolean logic and control loops to understand the flow of information and reason about behavior.

But take a look at that Pac-Man prompt again. When behavior is represented as matrix multiplications, then you have _way_ more variables – simplistically, one for every row and column of each matrix. And the control code and the variable manipulations are now captured by every numerical value in each of those matrices. Even this tiny network has 569 "variables" linked by 17,184 weighted connections (and then toss in a few more bias values to boot). And if all this wasn't challenging enough, there are no nice semantic clues, like variable names and programming language keywords, to help us. I can't hold this in my head. Can you? Yet, it seems that models can now basically glance at these opaque weights and intuit relationships and behaviors.

And I do mean _glance_. After a very short amount of thinking, here is what GPT-6 Astra said with reasoning set to `minimal`.

???+ quote "GPT-6 Astra’s observations"

    **Observations:**

    - **Channel 0 — agent:** Large weights occur across both axes, but only at a structured subset of interior cells. At **(1,1)**, weights include **−3.242, 3.377, −3.734, 4.081**; at **(1,3)** they include **4.742, −3.778, 3.821, 3.890**. Row 1 has strong weights throughout columns 1–8, whereas row 2 has strong weights at columns **1, 4, 5, 8** and small, initialization-like weights at **2, 3, 6, 7**. This looks like **traversable corridors in a fixed maze**, not unrestricted movement.
    - **Channel 1 — moving objects:** Substantial weights follow the same corridor structure. At **(1,1)**, examples are **−1.619, 2.453, 1.978**; at **(1,2)**, **2.493, −3.116, 2.157, 2.413**. Other moving entities therefore appear to inhabit the maze alongside the player.
    - **Channel 2 — reward targets:** Generally weaker than agent and moving-object weights, but not unused. First-layer unit 6 receives **−1.490, −2.361, −1.905, −0.883** from targets at **(1,1)–(1,4)**. This suggests collectible targets distributed along corridors, with some locations especially influential.
    - **Channel 3 — obstacles:** Interior weights are mostly small, including at apparent blocked cells. At **(1,1)**, the obstacle row begins **0.057, 0.106, 0.006, 0.008**. Border weights show recurring structure: unit 6 receives **−0.162, −0.149, −0.130, −0.207** from the first four top-border cells. A fixed maze explains why obstacle inputs need not be strongly discriminative: its geometry can be learned through position-dependent responses, while constant wall inputs act like additional biases.
    - **Channel 4 — previous frame:** Learned structure appears along the accessible cells. At **(1,1)**, examples include **−0.739, −1.316, 0.593**; at **(1,8)**, **0.992, −2.849**. Previous positions matter, consistent with tracking moving threats and recent movement.
    - **Outputs:** All four directions have substantial, differentiated weights. Examples include **W3[17,up] = 2.144**, **W3[24,down] = 2.502**, **W3[16,left] = 2.490**, and **W3[28,right] = 2.500**. Biases are **[−0.873, 0.703, 0.712, 0.595, −0.092]**: a baseline preference for moving rather than waiting, though actual choices depend on hidden activations.

    **Reasoning:**  
    The strongest clue is the fixed corridor pattern shared by the player and other moving entities. Combined with corridor-based collectibles and useful temporal information, this fits **Pac-Man: navigating a maze, collecting pellets, and avoiding ghosts**.

    Pong, Breakout, and falling-object catching games would ordinarily confine the player to a row or column. An open-arena pursuit game would not explain the inactive interior blocks. Standard Snake would not naturally explain a fixed internal maze plus separately represented moving entities. Static maze navigation fits the geometry but not the substantial moving-object channel.

    Weights alone cannot establish the exact reward rules or whether power pellets are present.

    **Game:** A small grid-based **Pac-Man-style maze game**.

    **Description:** The agent moves through fixed corridors collecting pellets for reward while avoiding moving ghosts. The likely objective is to clear the maze without being caught.

    **Confidence:** 93%

I've run that Pac-Man prompt through Astra, Opus 5.5, and even Muse Spark 1.3. They _all_ picked up the idea of Pac-Man, though they expressed different levels of confidence.

So maybe this is where we're at now! Previously, my mental model for LLMs was not so alien to my mental model for human brains – we take in raw sensory data, and over a cascade of computations, arrive at more abstract information that we use to navigate the world; attention is a resource that is limited and there are only so many things that we – both humans and LLMs – can keep track of. I still think all of this is true. But this study just made me realize how vastly more information an LLM can hold in its working memory, how quickly it can identify the big important abstract ideas and manipulate them, and how well training is generalizing into new domains.

Maybe we're toast. Maybe I'm just jealous that I can't edit my own neural weights.

<!--
POST_URL: https://arcturus-labs.com/blog/2026/11/03/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/
HERO_IMAGE: https://arcturus-labs.com/blog/assets/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/hero.jpg

=== LINKEDIN ===
AI Can Read Neural Network Weights. I Wasn’t Ready for That.

I included the prompt and Astra’s response so you can try it yourself. What model capability last broke your intuition?

https://arcturus-labs.com/blog/2026/11/03/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/

=== TWITTER/X ===
AI can read neural network weights. I wasn’t ready for that.

Prompt + model response inside, if you want to try it yourself. What capability surprised you lately?

https://arcturus-labs.com/blog/2026/11/03/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/

=== BLUESKY ===
AI can read neural network weights. I wasn’t ready for that.

Prompt + model response inside, if you want to try it yourself. What capability surprised you lately?

https://arcturus-labs.com/blog/2026/11/03/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/

=== REDDIT: community pending rules check (text post) ===
TITLE: Identifying a game from a neural network’s weights

How much behavior can an LLM infer from a network’s architecture and weights written out as text?

This result caught me off guard. I included the original prompt and a model’s response so you can test it yourself:

https://arcturus-labs.com/blog/2026/11/03/ai-can-read-neural-network-weights-i-wasnt-ready-for-that/

What would you change about the test to distinguish weight-based reasoning from guesses based on the input and output descriptions?
-->
