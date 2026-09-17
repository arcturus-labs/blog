---
date: 2026-09-16
authors:
  - john-berryman
categories:
  - Agentic AI
  - AI Product
  - Automation
description: TypeSafe's Jev skips text generation entirely, answering structured questions with calibrated probabilities in milliseconds. Here's how the API works, what might be under the hood, and why it could matter for robotics and real-time AI.
image: /blog/assets/typesafe_jev_trades_text_generation_for_instant_calibrated_decisions/hero.jpg
---

# TypeSafe's Jev Trades Text Generation for Instant, Calibrated Decisions

TypeSafe just announced [System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), and it's an interesting new take on transformer-based language models that could be _really_ useful.

The basic idea: you send the model a `state` (all the text or JSON data you want it to consider) plus a list of `questions` you want answered. But instead of responding with more text predicted one token at a time, Jev responds with calibrated, consistent, numerical `answers` to those questions, almost instantaneously.

![Calibrated decisions](./assets/typesafe_jev_trades_text_generation_for_instant_calibrated_decisions/hero.jpg){ align=center width=100% }

The answers come in three flavors – `choice`, `noul`, and `score` – which I'll describe below.

The utility of this model comes from its speed and the accuracy with which it makes its numerical predictions. Conventional LLMs are orders of magnitude slower, and if you ask how confident they are, they'll give you a number that often has little bearing on reality.

The demos for Jev are super impressive. In their Doom demo, they send 7 requests per second, having Jev predict which button should be pressed in real time. Jev can easily navigate the Doom map and blow away the baddies. ... Try that with an LLM.

<!-- more -->

## The API in brief

A request has a `state` and a `questions` map. The `state` is like the prompt in a conventional LLM: all the text or JSON data you want the model to consider. Each named question in `questions` has a type, instructions, and sometimes a set of allowed answers or a rubric.

Here are the three question types:

- `choice`: picks one item from a fixed list. It returns `{choice, probabilities, confidence}`.
- `score`: picks a position on an ordered rubric. It returns `{score, legend, probabilities, confidence}`.
- `noul`: asks whether something is true. It returns `{noul}`, which is the probability from zero to one that the answer is yes. No separate confidence field on this one.

## Example: handicapping a horse race

For example, the input for a horse race could look like this:

```json
{
  "model": "jev-latest",
  "state": {
    "race_details": {"distance_m": 1600, "track": "muddy"},
    "horse_details": {
      "thunderhoof": "Won 2 of last 3 races; strong in mud.",
      "saddleflash": "Won last race; prefers dry tracks.",
      "gallopjack": "Second in last 2 races; untested in mud."
    }
  },
  "questions": {
    "winner": {
      "type": "choice",
      "instructions": "Predict the winner of this horse race using horse ability, recent form, and fit for the course conditions. Select the horse most likely to win, not merely the favorite.",
      "criteria": {
        "thunderhoof": "Thunderhoof wins the race.",
        "saddleflash": "Saddleflash wins the race.",
        "gallopjack": "Gallopjack wins the race."
      }
    },
    "thunderhoof_handles_mud": {
      "type": "noul",
      "instructions": "Does Thunderhoof appear likely to perform well on the current track condition?"
    },
    "race_competitiveness": {
      "type": "score",
      "instructions": "How competitive is this race?",
      "criteria": [
        "One horse is clearly favored.",
        "A few horses have plausible winning chances.",
        "Many horses have similarly plausible winning chances."
      ]
    }
  }
}
```

And the answers would come back under those named questions (illustrative response – I made up these numbers):

```json
{
  "answers": {
    "winner": {
      "type": "choice",
      "choice": "thunderhoof",
      "probabilities": {
        "thunderhoof": 0.48,
        "saddleflash": 0.27,
        "gallopjack": 0.25
      },
      "confidence": 0.71
    },
    "thunderhoof_handles_mud": {
      "type": "noul",
      "noul": 0.82
    },
    "race_competitiveness": {
      "type": "score",
      "score": 1.61,
      "legend": {
        "0": "One horse is clearly favored.",
        "1": "A few horses have plausible winning chances.",
        "2": "Many horses have similarly plausible winning chances."
      },
      "probabilities": {
        "0": 0.04,
        "1": 0.31,
        "2": 0.65
      },
      "confidence": 0.63
    }
  }
}
```

## What's under the hood?

How do they do this? My initial guess was that this might be a new take on BERT – Take a transformer encoder, pull in all the text and process it like a normal, and replaced the output head with something that has a bunch of "slots" of these different types. The API's `questions` are associated with slots that select among a set of choices, score a rubric, or produce the probability that a statement is true.

Then, internally this gets turned into a prompt that dumps in the request structure (`state` and `questions`) but replaces the actual variable names with slot names so that the model knows where to stick the output data. Then, once the answer comes back, the API translates the slot names back to variable names.

[This X post](https://x.com/harshagundal/status/2100044305536889015) provides an even simpler possibility. This person (Harsha Gundala) has apparently replicated some of the success of Jev by fine tuning a conventional LLM. Rather than having a special output head, they just make the LLM generate the next token and then they use the logprobs to populate the probability numbers. For instance, if the `question` is boolean, then they look at the tokens `true` and `false`; if the `question` is over a set of enumerated choices, then they look at the logprobs of the tokens `A`, `B`, `C`, `D`, etc. Makes perfect sense.

Dang it... it makes perfect sense. I even [wrote about a similar idea a year and a half ago](./superpower_llm_classifications_with_logprobs.md). Shame I didn't follow that to its logical conclusion, found a company, and pull in millions of dollars in venture capital! Oh well. At least I don't have to think hard about the hero image for this blog post. I'll borrow the one from my old blog post.

In any case, the secret sauce to make the outputs make sense is in training the model. Starting with a pre-trained model, they would likely follow up with supervised fine-tuning. The data set they use would be really interesting because they need to collect outcomes for events that happened in real life and make up random questions like these with known answers.

The weird challenge is coming up with good confidence or probability values for each training example. For instance, if you know Thunderhoof did win, you have a clean answer for the Choice question or the Noul question. But you don't automatically have a clean answer for whether this particular input should have caused the model to be 51% confident or 95% confident.

Perhaps that's where the reinforcement learning comes in – what TypeSafe is calling "Reinforcement Learning for Calibrated Decisions". SFT would push the model to mimic the training data (where confidence is poorly defined), whereas reinforcement learning would allow the model to "introspect" into its own knowledge state and learn confidence/probability values that aren't just wild guesses. For this, you would definitely need to collect data that was outside of the original pre-training and SFT set.

Another place where RL can be useful is in a domain like the Doom demo. Given some "environment" (which could be real-world 3D like in the Doom video, or it could be a board game, or anything), you can have the model make predictions about what will happen next and how to interact in the world. Then you can let that play out in simulated worlds and use the results for policy updates.

Finally, these models aren't doing any reasoning. Reasoning requires token generation, which is _much_ slower than processing input tokens and would slow these models down tremendously. And like I said, these are probably encoders only, so they wouldn't be able to produce tokens in any case. Though I do wonder if they have some generic "thinking" placeholder tokens. There's precedent for this. In [Think before you speak: Training Language Models With Pause Tokens](https://arxiv.org/abs/2310.02226), they trained models with repeated `<pause>` tokens before the answer, giving them extra computational workspace without adding any new information. Something like that could be going on here.

## What can you do with this?

I've been wondering how LLMs might be used for embodied AI. My concern has been that any conventional LLM that cranks out one token at a time is going to be way too slow to interact with the world and make decisions in real time. So, perhaps these embodied AI agents will use LLMs for high-level decision making and then use dynamic models of real-world systems that can be called as tools. For example, the LLM could say "catch the ball that the boy is throwing at you" and then call the `catch_ball` tool, which internally uses visual input and a kinematic/dynamic model of the robot to actually reach out and catch the thing.

But this feels awkward. The `catch_ball` tool is incredibly bespoke. You'd have to make a buzillion little tools like this, and even then it wouldn't be great. How would you fold laundry? Instead, you'd want lower-level functions that generalize to any task, like `move_left_hand_to_coordinates(x,y,z)`, but an LLM is going to take way too long to generate the tool call and won't have the correct `x,y,z` values anyway.

This is where Jev might come in handy as an intermediate layer. [Go watch that Doom demo again](https://typesafe.ai/blog/introducing-system-one-models-and-jev) for a hint about how this might work. The high-level, abstract, navigational thinking could be performed by a conventional LLM, while the low-level motion of robotic limbs could be handled by conventional kinematic/dynamic models. In between, Jev could be watching streaming video from the robot's camera and estimating the ball's trajectory parameters to figure out the `x,y,z` location where the robot should place its hand to catch it.

(Update: The current model does not actually take visual inputs. Apparently, they're feeding it text telemetry from the Doom environment. But since this is a transformer model there's no reason that future models wouldn't be able to process image inputs.)

What's more – and it blows my mind to think about the possibilities – the high-level LLM can specify requests to Jev on the fly, as needed. The LLM, using Jev as a tool, can call on it to make arbitrary predictions about salient things in its environment. This is very generalizable!

There are plenty of other things you can do with a model like this. Think about sticking it into smart glasses and quickly classifying all the things around you and their location. Or think about quickly batch processing very general classification tasks. Rather than having a traditional LLM slowly and expensively reason through a stack of resumes to determine if a person is right for the job, you could send them all to Jev and blow through the stack quickly and cheaply.

But... the key thing yet to be proven is how accurate it is in general real-world tasks. It might be the case that Jev – a general model – is not terribly accurate on your specific domain and the better approach is to just use their approach to fine tune a model for your own domain.

## But what I really want

What I really want next is a fine-tuning API for Jev where I can dump in a big blob of text and data, have TypeSafe convert all of that into good training data with example states, questions, and outputs, and then fine-tune the model for me. If TypeSafe offers anything like that, then I'm going to gather up all the horse racing data I can find and head to the tracks. 😆

!--
POST_URL: https://arcturus-labs.com/blog/2026/09/16/typesafes-jev-trades-text-generation-for-instant-calibrated-decisions/
HERO_IMAGE: https://arcturus-labs.com/blog/assets/typesafe_jev_trades_text_generation_for_instant_calibrated_decisions/hero.jpg
=== LINKEDIN ===
What if an LLM never generated a single token?
TypeSafe's Jev points toward a different interface: ask structured questions about a state and get calibrated decisions back in milliseconds. I dug into the API, what might be under the hood, and where this kind of model could fit between a high-level LLM and a real-time system.
Where would you put a model like this first - robotics, games, or something else?
https://arcturus-labs.com/blog/2026/09/16/typesafes-jev-trades-text-generation-for-instant-calibrated-decisions/
=== TWITTER/X ===
What if an LLM never generated a single token?
TypeSafe's Jev returns calibrated decisions instead. I dug into the API and what this suggests for real-time agents.
https://arcturus-labs.com/blog/2026/09/16/typesafes-jev-trades-text-generation-for-instant-calibrated-decisions/
=== BLUESKY (276 chars) ===
What if an LLM never generated a single token? TypeSafe's Jev returns calibrated decisions instead. I dug into the API and what this suggests for real-time agents. https://arcturus-labs.com/blog/2026/09/16/typesafes-jev-trades-text-generation-for-instant-calibrated-decisions/
=== REDDIT: r/AI_Agents (text post) ===
TITLE: What happens when an LLM stops generating text and just makes decisions?
TypeSafe's Jev takes a different approach to an LLM interface: send it state plus named questions, and get back choices, scores, or probabilities instead of a generated response.
I wrote up my read of the API and the architectural question it raises. A conventional LLM is good at open-ended, high-level planning, but token-by-token generation is a strange fit for decisions that need to happen repeatedly and quickly. Jev looks like a possible middle layer for that gap.
The post explores what might be under the hood, including whether a fine-tuned conventional model plus logprobs could reproduce some of the behavior, and what calibrated decisions could mean for real-time agents.
Full disclosure: this is my own blog post, not affiliated with TypeSafe: https://arcturus-labs.com/blog/2026/09/16/typesafes-jev-trades-text-generation-for-instant-calibrated-decisions/
Where would you use this interface first - as a policy layer, classifier, evaluator, or something else?
-->