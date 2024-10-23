# Goal
Show that we can set up SPLADE in ES and use it to search documents. SPLADE is a sparse text embedding model that can be used to search documents. It works by taking a query and expanding it into a set of tokens that are then used to search for documents. In order to implement SPLADE in ES, we need to:

# Basic Steps
1. Set up a basic ES index.
2. Index a doc and search it.
3. Find a better data set.
4. Index in a reasonable manner (have a set of fields that make sense).
5. Get SPLADE working: Given a text blob, generate a set of tokens representing the expanded text.
6. Index w/ SPLADE expansions.
7. Search w/ SPLADE and demonstrate better recall.
8. Show how you can get the best of both worlds by searching over the original text, but then boost by the SPLADE text.
9. Write blog post.

# Blog ideas
- Pain points
  - Vector search is the new cool kid on the block, but it's hard to setup. ES + SPLADE is a breeze.
- Get setup
  - https://github.com/elastic/start-local
  - index documents
- Show how poorly it works with a basic query.
  - generate alternate descriptions for all heroes that state the same thing as the original description but with different words.
  - calculate the retrieval score
- Show how well it works with ESLER 
  - TBD
- Explain SPLADE
  - explanation of what it is
  - set up SPLADE
  - demo hero | description | alternate description | splade embedding | num matches that aren't in alternate description
- Show that it works better
  - index documents with SPLADE expansions
  - show that it has better recall
- Lies
  - "As Hindsight Lad would tell us"
  - SPLADE actually isn't that hard to implement - though we are ignoring the payload values for each token for now (so it's not really SPADE!)
  - caution that it might decrease precision `get_splade_embedding("marry had a little lamb, it's fleece was white as snow", num_tokens=15)`
  - If it's generating weird synonyms, you'll still need to train a better model and reindex - but at least you'll be able to see the terms that it's generating and beter diagnose the problem
- Conclusion - you have 2 options
  - ESLER has that all setup for us probably 
  - Need to figure out if vector search is better.
  
- Promote book

# don't forget
- review code - especially comments
- add https://marvel.fandom.com/wiki/Carlton_LaFroyge_(Earth-616)?file=Carlton_LaFroyge_%28Earth-616%29_from_New_Warriors_Vol_1_37_001.jpeg  https://en.wikipedia.org/wiki/Hindsight_(character)
- link out to notebook
- add another Hindsight Lad image
- add book image

# Promote
- Partners
  - Elasticsearch folks
  - Pinecone folks - prolly not because I'm saying you can do it with just basic ES stuff
  - Jason Liu
- Possible work
  - Limitless

  
