With the growing popularity of RAG methods for prompt engineering, vector-based semantic search has become a staple for many applications. And why not? It overcomes some of the historic shortcomings of keyword search. With keyword search you might type terms in the search bar and even if they mean the same thing as the document you're looking for, they won't match the doc if you're using different words. The doc says "gorilla suit" and I search "ape costume" and get no results. With semantic search, if I search for "ape costume", then this gets turned into a vector which holds the _meaning_ of my words, and if there is any document with a similar meaning (as represented by a nearby vector) then I get a match!

Semantic search is almost magic... except when it's not.

There are some gnarly pit-falls for semantic search which we are wrestling with:
- **Semantic search makes for larger indexes.** –  With keyword search, I would typically plan for the full index to be 1.5x-2x the original size of the documents I was storing. But with semantic search, the size of the index might be twice that.
- **Chunking is hard.** – You need to split up text into chunks because the quality of an embedding degrades if you stuff too much text into the chunk. Where do you split the text? Do you need to make the chunks overlap to make sure you didn't cut an important point in half? Do you need gather other important context into the chunk?
- **Semantic search is opaque.** –  With keyword search, if a query doesn't match an expected document then there are plenty of ways to debug the problem – afterall keywords search relies on human-readable tokens. You can also muck around with the query, field boosts, and phrase matches to tune the relevance. With semantic search, if the query doesn't match the expected document, then it's challenging to figure out why. Often fixing relevance problem means training a new embedding model and reindexing the entire corpus. Yikes!

It would be awesome if we could have the best of both worlds – semantic search's ability to search based upon meaning, but traditional keyword search's transparence and relative simplicity.

## SPLADE to the Rescue
SPLADE, Sparse Lexical and Expansion Model for First Stage Ranking, was introduced in a [July 2021 paper](https://arxiv.org/abs/2107.05720) and then quickly improved upon in [the subsequent September paper](https://arxiv.org/abs/2109.10086). The basic idea is simple – instead of asking a semantic model for a vector that carries the meaning of a document, figure out some way to ask the model for the important terms that _should be in the document_, whether or not they were actually there. For instance if I have a doc with the text "ape costume" then the semantic model might identify similar terms, such as "gorilla orangutan monkey suit clothes". These synthetic terms can then indexed in a traditional search engine, and in order to boost recall we just add this field into the search.

In the remainder of this post I will show you have to use SPLADE to augment your search. We'll create a silly document set (because what fun is it to use a realistic example?), index the documents, and demonstrate how bad search can be when you don't quite use the right terms in search. Then we'll add in SPLADE and show how it goes a long way in addressing the problem.

## Setup
What's your favorite superhero? Superman? Wolverine? Batman? ... Mine's got to be Hindsight Lad – a computer research that made a contribution to his team by critically reviewing past decisions and explaining what his team should have done instead. (Real character! Look him up!)

Inspired by Hindsight Lad, I've chosen to use superheroes for our example data set. The data set is simple, it's a list of superheroes including their names, true identity, descriptions, and superpowers. Here's an excerpt

| Name | True Identity | Description | Superpowers |
|------|---------------|-------------|-------------|
| Spider-Man | Peter Parker | A high school student bitten by a radioactive spider | Web-slinging, superhuman strength, spider-sense |
| Hindsight Lad | Carlton LaFroyge | A teenager with the ability to analyze past events and point out mistakes | Retroactive clairvoyance, tactical analysis of past events |
| Batman | Bruce Wayne | A billionaire industrialist and philanthropist | Genius-level intellect, master detective, peak human physical condition |
| Arm-Fall-Off Boy | Floyd Belkin | A superhero with the ability to detach his arms | Detachable arms, using detached arms as weapons |
| Superman | Clark Kent | An alien from the planet Krypton | Flight, super strength, heat vision, invulnerability |

In order to demonstrate the semantic mismatch problem, I've also generated a list of alternative descriptions which carry the same meaning as the description field above, but shares almost no common words.

| Name | Alternate Description |
|------|-----------------------|
| Spider-Man | An adolescent scholar affected by an irradiated arachnid |
| Hindsight Lad | A young critic gifted with retrospective wisdom |
| Batman | A wealthy entrepreneur and humanitarian |
| Arm-Fall-Off Boy | A costumed vigilante capable of limb separation |
| Superman | An extraterrestrial being from a distant celestial body |

The list of heroes I'm curated has just 50 rows, so if we query using any of the alternate descriptions, there's a decent chance that semantic search would nail it, but traditional information retrieval will fall flat.

### Indexing
Let's demonstrate this. Here is function that will index all of our documents:

```python

def index_superheroes(num_tokens=50):
    # Create the index with mappings
    index_name = "superheroes"
    mappings = {
        "mappings": {
            "dynamic": "false",
            "properties": {
                "description": {
                    "type": "text",
                    "analyzer": "english",
                },
                "splade": {
                    "type": "text",
                }
            }
        }
    }

    # delete and recreate the index
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        print(f"Index '{index_name}' deleted successfully.")
    else:
        print(f"Index '{index_name}' does not exist.")

    es.indices.create(index=index_name, body=mappings)
    print(f"Index '{index_name}' created successfully.")

    df = pd.read_csv('superheroes.csv')
    # Index the superheroes
    for i, (index, row) in enumerate(df.iterrows(), start=1):
        # Combine the index (superhero name) with the row data
        full_row = pd.concat([pd.Series({'name': index}), row])
        doc = full_row.to_dict()
        doc['splade'] = get_splade_embedding(doc['description'], num_tokens)
        es.index(index=index_name, id=i, body=doc)

    print(f"Indexed {len(df)} superheroes.")
```

This is a pretty simple script, it creates an index with two fields, the `description` field which holds the descriptions of the superheroes, and a `splade` field that holds the synthetic terms. Notice that we are generating the SPLADE content by processing the `description` text through the `get_splade_embedding`. That doesn't exist yet, so let's create it:

```python
from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch

model_id = 'naver/splade-cocondenser-ensembledistil'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id)

vocab = tokenizer.get_vocab()
id2token = {v: k for k, v in vocab.items()}

def get_splade_embedding(text, num_tokens=50):
    # get the tokens
    tokens = tokenizer(text, return_tensors='pt')

    # get the splade embedding
    output = model(**tokens)
    vec = torch.max(
        torch.log(
            1 + torch.relu(output.logits)
        ) * tokens.attention_mask.unsqueeze(-1),
    dim=1)[0].squeeze()

    # Convert vec to numpy for easier manipulation
    vec_np = vec.detach().numpy()

    # Get indices of non-zero elements
    non_zero_indices = vec_np.nonzero()[0]

    # Create a list of (token, value) pairs for non-zero elements, excluding the input tokens
    token_value_pairs = [
        (id2token[idx], vec_np[idx]) 
        for idx in non_zero_indices 
        if idx not in tokens['input_ids'][0]
    ]

    # Sort by value in descending order
    token_value_pairs.sort(key=lambda x: x[1], reverse=True)

    new_tokens = [token for token, value in token_value_pairs[:num_tokens]]
        
    return new_tokens
```

This is a bit more complicated. Fortunately, most of the thinking was done for me. The code was cribbed from Pinecone's [excellent SPLADE writeup](https://www.pinecone.io/learn/splade/#SPLADE-Embeddings), and the equations are covered in detail in [the SPLADEv2 paper](https://arxiv.org/abs/2109.10086). But effectively, we're pulling the tokens from the supplied text,and then using the SPLADE model to tell us which terms (SPLADE tokens) are important for this text. We filter out the tokens that were in the original text to begin with, converting the tokens back to readable text, and returning that to the caller.

### Searching
What good is an index that can't be searched? Let's remedy that:

```python
def search_superheroes(description, size, splade):
    # If SPLADE is enabled, we search both the description and SPLADE fields
    if splade:
        # Get SPLADE tokens for the description
        splade_tokens = get_tokens_as_text(description)
        query = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "multi_match": {
                                "query": description,
                                "fields": ["description"]
                            }
                        },
                        {
                            "multi_match": {
                                "query": splade_tokens,
                                "fields": ["splade"]
                            }
                        }
                    ]
                }
            }
        }
    # If SPLADE is not enabled, we only search the description field
    else:
        query = {
            "query": {
                "multi_match": {
                    "query": description,
                    "fields": ["description"]
                }
            }
        }
    # Set the number of results to return
    query['size'] = size
    
    # Execute the search query
    response = es.search(index="superheroes", body=query)

    # Extract the hits from the response
    hits = [hit['_source'] for hit in response['hits']['hits']]
    return hits
```

This search function finds superheroes based upon the supplied description (which will be drawn from our alternative description list). If the `splade` argument is set to true, then we search over both the `description` and the `splade` field, otherwise we only search over the `description` field.

Again we're missing one ingredient. The `get_tokens_as_text` function is used to convert the description to it's corresponding tokens. Note that we're not expanding the description to include synthetic terms, instead we're just chopping it up into SPLADE tokens. This should make it clear:

```python
def get_tokens_as_text(text):
    tokens = tokenizer(text, return_tensors='pt').input_ids[0]
    return ' '.join([id2token[i] for i in tokens.tolist()][1:-1])
```

Now we're ready to see if this all actually works!

## Demo Time
Let's take the above code out for a spin.

First we index our superheroes with `index_superheroes(num_tokens=50)`. Here we inject up to 50 SPLADE tokens for each row in our data set.

Next, SPLADE turned off, let's see if we can catch Iron Man using his alternative description:

```python
use_splade = false

hero = "Iron Man"
alt_description = hero_dict_alt[hero]
search_results = search_superheroes(alt_description, 3, use_splade)
result_heroes = [result['name'] for result in search_results]

print(result_heroes)
```

```
['Beast']
```

Nope... that's a miss! Well, after I've spent all this time writing a blog post, I hope that we can turn SPLADE back on and see Iron Man in the results.

```
['Black Panther', 'Iron Man', 'Beast']
```

Yay! I mean, I would have preferred that Iron Man was number 1 in the search results. But being in the top 3 results out of 50 for something as generic as "A brilliant innovator and corporate magnate" is not bad.

But perhaps we were lucky with this example. Let's create a new function `recall_at_3` that will run through every hero and and see if SPLADE is actually helping us improve recall.

```python
def recall_at_3(splade):
    counter = 0
    for hero in hero_dict.keys():
        alt_description = hero_dict_alt[hero]
        search_results = search_superheroes(alt_description, 3, splade)
        result_heroes = [result['name'] for result in search_results]
        # Check if the hero is in the top 3 search results
        if hero in result_heroes:
            counter += 1
    
    # Calculate and return the recall@3 score
    return counter / len(hero_dict.keys())
```

First we test without SPLADE `recall_at_3(False)` and see that the recall is 28% – as expected, not great. Now with SPLADE `recall_at_3(True)` returns (... drum roll please ...) 52%.

Alright! (Whew!) So by injecting synthetic tokens into our indexed documents we have improved recall (recall@3 to be precise) by a staggering 24%!

## Retrospective
I can feel my inner Hindsight Lad jumping up and down in my head. It's time to take a closer, more critical look at what we just accomplished. SPLADE is definitely neat, but it doesn't fix all of our problems.

We've improved recall, but in a longer blog post (which I shall never write) we would also look at how precision changes. The problem is that sometimes the synthetic tokens produced in `get_splade_embedding` can be... wonky. Take a look at this example:

```python
get_splade_embedding("mary had a little lamb, it's fleece was white as snow", 15)
```

```
['marriage',
 'married',
 'winter',
 'song',
 'wedding',
 'have',
 'sheep',
 'whites',
 'baby',
 'like',
 'color',
 'wearing',
 'film',
 'character',
 'murder']
```

There's a lot going on here. We start off with several words related to marriage and then right at the end it takes a darker turn with `murder`. You know how the rest of that song goes, and these words are clearly a miss. There's also few stop words (super common words) in there: `have`, and `like`. This will definitely increase relevance as it will match about half of the docs in the index, but this will take it's toll on precision.

Next up, my implementation of SPLADE in Elasticsearch is too simple. If you scroll back up to `get_splade_embedding` you might notice that we are pulling the non-zero elements from the `vec_np` vector – these correspond to the SPLADE tokens. But we're completely dropping the actual weight associated with the tokens. _This is useful information!_ Read the SPLADE papers, they are using the weights in order to score the match. Knowing that _murder_ was not as important to Mary as _sheep_, _song_, _baby_, and _white_ would really improve the precision problem from the previous paragraph.

Finally, one of the problems with semantic search that we were trying to avoid is the complexity of dealing with the embedding model when it doesn't quite do what you want it to do. When an embedding model doesn't match the correct documents, then your only option is to retrain the model, reindex, and hope. But with SPLADE, if it thinks that Mary likes murder, our options aren't much better. The main benefit of SPLADE in this case is that you can actually see the words produced by the model, (rather than an opaque vector). This will make it easier to debug the problem and improve it. ... Maybe SPLADE's training data had too many references to Mary I of England (you know... "Bloody Mary").

## Conclusion
SPLADE is a promising new approach that is bridging the gap between traditional keyword search and modern semantic search. And this is a good thing! In many ways, good ol' keyword search is the right tool because it's relatively simple, it's well understood, and it's easy to scale and maintain.

This post is begging for follow-up posts:
- How does my implementation of SPLADE+Elasticsearch affect precision?
- How does semantic search perform against my implementation of SPLADE+Elasticsearch?
- Can we improve SPLADE+Elasticsearch? I want to see how tough it is to get the SPLADE weights into the Elasticsearch scoring.
- Did you know that Elasticsearch offers a SPLADE-like solution called [ESLER](https://www.elastic.co/search-labs/blog/elastic-learned-sparse-encoder-elser-retrieval-performance)? I wonder how that compares with the solution presented here.





## Don't Go Yet!
It's completely un-related to this blog, but did you know that I'm writing [a book for LLM Application Development](https://amzn.to/3zKIxGG). It's slated to be out in November 2024. Every copy you purchase buys me a cup of coffee. Buy your team members a copy each, then I'll have coffee for a week. And if you are working on an LLM application of your own and need some help, then call on me jfberryman﹫gmail‧com.