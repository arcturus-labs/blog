---
date: 2025-03-31
categories:
  - Classification
title: Supercharging LLM Classifications with Logprobs
description: Turn your LLM into a precision instrument for classification – no fine-tuning required. This post shows how to go beyond simple "yes/no" answers and unlock soft classification using logprobs. You'll learn how to extract class probabilities in a single call, tune your classifier for optimal performance, and make your LLM behave more like a proper ML model. Perfect for anyone building smarter, more flexible AI applications.
image: blog/assets/superpower_llm_classifications_with_logprobs/top_image.png
---

I was just reading the classification chapter of Jay Alammar and Maarten Grootendorst's excellent book [Hands-On Large Language Models](https://amzn.to/4lfynRy). I felt inspired to extend their work and show yet another cool trick you can do with LLM-based text classification. In their work they demonstrated how an LLM can be used as a "hard classifier" to determine the sentiment of movie reviews. By "hard" I mean that it gives a concrete answer, "positive" or "negative". However, we can do one better! Using _"this one simple trick"_™ we can make a "soft" classifier that returns the probabilities of each class rather than a concrete single choice. This makes it possible to _tune_ the classifier – you can set a threshold in the probabilities so that classifications are optimally aligned with a training set.

![Soft Classification](./assets/superpower_llm_classifications_with_logprobs/top_image.png){ align=left width=100% }

<!-- more -->

## Building the "Hard" LLM Classifier
To quickly repeat/paraphrase the work of Hands-On Large Language Models, here's how to build a sentiment classifier using an LLM.

1. Create a prompt that explains the task: "Find the sentiment of this movie review."
2. Add in the text to be classified.
3. Explain the output format for the classification: "Please say only 'positive' or 'negative' and no other words or explanations."

Here's how we could couch this inside of a function:

```python
def get_sentiment(text, model):
    messages = [{   
        "role": "user",
        "content": f"""Read the following text and tell me if the sentiment is positive or negative: 
        
        > {text}
        
        Just say 'positive' or 'negative' (lowercase - no other text - no quotes no words besides positive or negative)""",
    }]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1,
        temperature=0.7,
    )

    return response.choices[0].message.content
```

Let's use it a couple of times:

```python
>>> get_sentiment("this sucks", "gpt-4o-mini") 
negative

>>> get_sentiment("it's awesome", "gpt-4o-mini")
positive
```

Perfect.

Let's try one more time:

```python
>>> get_sentiment("this sucks, it's awesome", "gpt-4o-mini")
positive
```

Positive? Really? I mean, surely there's some nuance to that, right? Let's try it again a few more times – click, click, click – and we get another 2 positives and a negative. So there _is_ nuance. But how can we understand what the nuance is? How can we take advantage of this?


## Turning a "Hard" Classifier into a "Soft" Classifier
The solution is obvious, right? If you run the classifier several times, then the ratio would eventually converge to the true value, and we would have our soft classifier. But the problem with this solution is just as obvious – how many times do you have to run the classifier before it converges on the correct solution? The answer... lots. And I ain't got that kind of time or money.

But would you believe that you can get the _exact_ probabilities in a single LLM completion request? You can, but first you need to read cool info box about logprobs.

!!! note "Cool Info Box About Logprobs (or "The Lies We Tell Ourselves")"

    When an LLM makes a completion, it doesn't just magically come back with the text all at once. That's a lie. Instead, it looks at the prompt and generates a single token, and then this token gets appended to the prompt and the calculation happens all over again. And one token at a time, the completion is calculated.

    But this is _also_ a lie. Because the LLM doesn't really come up with the next token. It's actually a 2-step process. First the LLM looks at the prompt, and rather than predicting the next token it _actually_ comes up with a long list of probabilities for every possible next token. For instance, gpt-4o has roughly 100K next tokens – if you prompt it with "Today's weather is" then every possible next token is associated with a probability. Among them will be "sunny", "cloudy", "hot", "cold", "rainy", all with reasonably high probabilities. But there will also be all the other tokens "pickle", "manly", "dance", "even" most with infinitesimally small probabilities. And if you summed up all the probabilities, they would add up to 1.0 – that is, there's a 100% chance that one of these tokens will be the next token - nothing less, nothing more.

    There is one more complexity to cover. (Yes, this was another lie.) Each token is actually associated with a "logprob" rather than a probability - that is, the logarithm of the probability rather than the actual probability. Why? It's just easier computationally. It's also no big deal – you can convert from logprobs to probabilities by taking the exponent of the logprob.

    Oh... yeah, and all of that was a lie too. If you _really_ want to know what's happening inside the LLM, I recommend you again to [Hands-On Large Language Models](https://amzn.to/4lfynRy) – in particular, chapter 3. But my explanation here is sufficient for now.

With that knowledge in hand, here is how to extend the hard classifier above to make our soft classifier. First you have to follow the exact same steps above to make the hard classifier. But for the request, you ask for the logprobs to be returned. You don't want the probabilities of all ~100K tokens, but 10 or so should be enough. Then, when you get the completion back, you extract the logprob for each of the possible next tokens and convert them into probabilities.

Let's take a look at the implementation:

```python

def get_sentiment(text, model):
    messages = [{   
        "role": "user",
        "content": f"""Read the following text and tell me if the sentiment is positive or negative: 
        
        > {text}
        
        Just say 'positive' or 'negative' (lowercase - no other text - no quotes no words besides positive or negative)""",
    }]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1,
        temperature=0.7,
        logprobs=True, # this instructs the model to return the logprobs for each token returned
        top_logprobs=10, # this further instructs the model to return the top 10 logprobs, not just the one selected
    )

    # Extract top logprobs and convert to probabilities
    logprobs_list = response.choices[0].logprobs.content[0].top_logprobs # we only care about the first token in the completion
    token_probs = {
        # item.token is the text of the token - "positive", "negative", or something else
        # math.exp(item.logprob) is the probability of that token
        item.token: math.exp(item.logprob)
        for item in logprobs_list
    }

    # for the sentiment classification, I only care about the probability of 'positive' and 'negative'
    # but I'm lumping the probability for all other possible tokens into "other"
    pos_prob = token_probs.get('positive', 0)
    neg_prob = token_probs.get('negative', 0)
    other_prob = 1 - (pos_prob + neg_prob)

    return {'positive': pos_prob, 'negative': neg_prob, 'other': other_prob}
```

To see how it works, let's run this sentiment classifier with the problematic example from above:

```python
>>> get_sentiment("this sucks - it's awesome", "gpt-4o-mini")
{
    'positive': 0.5621647747752282,
    'negative': 0.4378143668101077,
    'other': 2.085841466414884e-05,
}
```

There's our nuance! Before, we ran the hard classifier 4 times and found that it was positive 75% of the time and negative 25% of the time. But with the hard classifier it would be impossible to have an accurate estimate without running the classification many, many times. But if you have access to the underlying probabilities (and we do!) then you don't have to run the classifier multiple times. You can just look and immediately see what tiny fraction of the time the model would have classified the sentiment as positive vs. negative.

What's more, you can set a threshold for the probability of the classifier and tune its performance to maximize your desired criteria. For example, it would be naive to assume that if the value associated with `positive` is greater than `negative`, this implies that the sentiment is positive. There might be some bias in the classifier – but you can tune for it! You can run the soft classifier on a labeled sample of your dataset and adjust the cutoff threshold so that accuracy for your sample is optimized. This might mean that any value for `positive` that is above, say, 0.47 is counted as being positive.


## Making Your Own Classifier

If you want to make a similar classifier, then here are some ideas and tips to consider:

- Sentiment analysis only has 2 options "positive" or "negative", but your implementation could have many more. For instance, you could make a tech support classifier that classifies emails into the portion of the product that is being discussed.
- Sentiment analysis requires almost no explanation, but your classifier could incorporate a prompt with considerable explanation and some examples. Maybe you could even employ chain-of-thought or reasoning prior to declaring its final answer.
- Notice that in the above implementation I was keeping track of the probability associated with "other" tokens besides "positive" and "negative", this is because ambiguous text can make the classifier jump to a token besides "positive" and "negative", such as "ambiguous". A better classifier would take this into account. There are several options here:
    1. You can normalize the probabilities so that prob("positive") and prob("negative") sum to 1.0 and ignore the other tokens.
    2. You can listen to what the LLM is trying to tell you – catalog the other tokens being referred to and incorporate them into new classifier with more options.
    3. Add an explicit "none of the above" option.
- Whenever you implement a "soft" classifier make sure that each of the classes you select are single tokens. For instance, "positive" and "negative" are tokens, but if "positive" was two tokens "pos" and "itive", then this technique wouldn't work - at least not without some extra considerations. One easy way to get around this is to use numbered options for your classes.


## Conclusion
There are a lot of fun things you can do with logprobs. For instance, when we were working at GitHub, the coauthor on my book, Albert Ziegler, was experimenting with a way to pack the optimum number of few shot examples into a prompt. He did this by measuring the "perplexity" of the text of the Nth example, which is derived from the logprobs of that text.

Unfortunately, not to many frontier models these days actually surface logprobs – to my knowledge, only OpenAI. And I can see why not – full access to logprobs makes it much easier to distill the knowledge of a teacher model into a student model. So even OpenAI has limited access to only output tokens (which means that, you can't do Albert's trick any more!). But if you're using OpenAI or hosting your own open-weights model then building a classifier like this is still a neat tool to have in your belt.

Oh! Shout-out to Jay Alammar and Maarten Grootendorst. If you really want to grok how things work inside the model and learn some neat approaches for using them, then make sure to grab a [copy of their book](https://amzn.to/4lfynRy). It's fantastic!

--- 

### Hey, and if you liked this post, then maybe we should be friends!

- I just wrote a book about Prompt Engineering for LLM Applications. [Maybe you'd be interested in reading it.](/#about)
- Are you stumped on a problem with your own LLM application? [Let me hear about it.](/#contact-blog)
- I'm going to write lots more posts. [Subscribe and you'll be the first to know](/#contact-blog).
