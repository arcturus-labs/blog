---
date: 2025-10-17
categories:
  - Prompt Engineering
  - User Experience
description: Explore the challenge of functionality flicker in spec-driven AI development - when different AI agents produce completely different implementations from the same specification. Discover why natural language specs are inherently ambiguous and learn practical strategies for building more consistent AI-driven development workflows.
image: /blog/assets/functionality_flicker/top_image.png
draft: true
---
# Addressing the Problem of Functionality Flicker in Spec-Driven AI Development
<!-- TODO! 
- make better description above

-->

There's a problem with spec-driven development – functionality flicker.



As context, it's important to know what I mean by spec-driven development, because it means something different to every person you ask. One definition – prior to every meaningful implementation change, you create a specification document for that change and then use the spec as a guide for the AI to make changes. It helps it see the big picture. Once the implementation is complete, you throw away the spec because it's served it's purpose. –– This is a good idea! But it's not what I'm talking about.



I'm talking about a bigger notion of the spec. I'm talking about an ideal world where we keep track of the global product specification, and then we allow the agent to build code based upon that.



But if you take a global product spec and you have two agents attempt to write code for that spec, the resulting codebase will be completely different! This is "functionality flicker". Why is this? It is _not_ because the agents aren't smart enough yet. Rather, it's because natural language is inadequate for the task! English is far too ambiguous and imprecise.



So what's the solution? One thing you could do is to specify away the uncertainty! Find everything that is ambiguous in the specification and add subsections (and sub-subsections) to clarify exactly what you mean. But what you'll find is that in order to make natural language precise you have to write so much content that you lose any benefit - the spec has become a formalized language and you might as well use a different formalized language –– code.



But as humans, we do pretty well with natural language. How do we do such a reasonable job with software development?



For starters, we have a shared understanding of the world right around us. An AI has read every bit of text and code in the public domain – so it has a great idea of how things _generally_ work. But it has no idea how things typically work at your company and in this codebase. And every request it receives can only carry a small portion of the context it really needs. You, on the other hand, have accrued an understanding of your immediate environment through trial and error. You implemented your first code change, and in PR review you learned a LOT about "the way we do things here". And you learned more with every interaction you've made at the company both with the code and with the humans. What you've learned can not easily be put into a giant document and shared with the agent as context (...though it's a great idea to try...).



Next, use humans _clarify_. When statements are made, we identify ambiguities and we have conversations to disambiguate the possibilities. What's more, we're really efficient at only dealing with the ambiguities that matter. We lean back upon the shared context (last paragraph) and we don't ask they things that "everyone is supposed to know," we don't ask about which libraries to us



chat - dually implement and ask

code as shadow spec.


respond in https://www.linkedin.com/feed/update/urn:li:activity:7384664250830606336?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7384664250830606336%2C7384887548021534720%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287384887548021534720%2Curn%3Ali%3Aactivity%3A7384664250830606336%29