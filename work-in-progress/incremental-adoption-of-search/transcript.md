# Incremental adoption of AI in e-commerce (Turnbull Maven)

[00:00:00] ~~​ AI is a lot more accessible than classic ML that means that improving agentic search is going to be more intuitive. It's not about retraining models. It's not about finding the perfect model that's a good fit. It's not about, data cl-cleaning and stuff like that. If you view it as a pipeline, then you can just read the traces, think about how your new AI intern i-is itself thinking through the problem space, and you can help it get better at its job.~~

[00:00:00] ~~That's how you improve agentic search.~~

[00:00:00] ~~If this is promising right now, then think about the speed at which things are changing. It mean that a reasonably capable agentic search right now is only going to get better~~

[00:00:00] today we're going to talk about the future of agentic search. 2024, that's when retrieval-augmented generation came on the scene, and it kind of revolutionized everything with search.

[00:00:11] But it wasn't always a smooth path. Uh, there was issues with very complicated ingestion pipelines, opaque semantic and vector search that when it broke, you didn't really know why.

[00:00:22] And sometimes the models summarizing the documents would just lie and hallucinate.

[00:00:27] Fortunately, the models have gotten a lot better And our techniques have improved as well. And along the way, there have been some surprises. For example, you don't necessarily need cutting-edge vector search capabilities in order to have good agent search. Instead, you might just try giving your agent simple tools, traditional search, or even grip.

[00:00:48] And what's more, when you watch these agents work through the search documents, it's kind of like watching a human rummage through documents, and this makes it much more [00:01:00] transparent, much easier to reason about and improve.

[00:01:03] The following is a lightning lesson that I did with Doug Turnbull about incrementally adopting agentic search into your company. I clarify what agentic search is, and guess what? It's not a black box.

[00:01:16] It's actually a transparent pipeline that you can easily work with and improve. I talk about how you can start adopting agentic search cheaply, incrementally, and safely. And then once you're in the mix of it, you can start extending it to all sorts of interesting new opportunities, including full assisted agentic search.

[00:01:37] So let's dig in.

[00:01:38] we're gonna cover three main topics today. The first one is just what is RAG? Everyone's g- got their own definition, but RAG, agentic AI, all this stuff demystified.

[00:01:47] That by itself doesn't have to be as hard as we've made it for the past several years. Also, AI we're in a weird place where AI might be your search team. There's there are very specialized tasks that [00:02:00] a frontier search team has had to do, but AI is getting so smart that it can search like a human and in some cases maybe be a good option for jumping to the head of the line and spending a little bit less.

[00:02:13] Adopting AI in the e-commerce user experience. Rather than revamping your whole site I'm gonna show by example a way that you can adopt agentic search gradually, introduce it i- in a way that doesn't surprise your users. So why this matters adopting AI for e-commerce is actually going to be a pretty easy thing to try.

[00:02:35] You can see if it works really quick, and if it does work, it will save your enterprise lots of money. So here we go. First off, I am Jon Berryman. I got started in aerospace engineering. Quickly found out that it was the math and software that I liked, so I ended up getting into search. And there, there's the book that Doug and I wrote together.

[00:02:55] Another couple hops and I was at GitHub. I was a first... I was [00:03:00] an early, not first anything, but I was an early production engineer on GitHub Copilot, if you still remember what that was. And I got a chance to write a- another book with one of my colleagues there, Alex Ziegler, who was o- one of the original three that actually introduced that, that research at GitHub.

[00:03:18] Finally I am Arcturus Labs independent consultants. Check me out. I do blog and if you like this, then you might like some of the other content I've got on my site as well. All right, so RAG and agentic AI demystified. In two thousand twenty-four everyone had their own R-RAG framework. LangChain, LlamaIndex, Haystack, they were just coming out of the woodworks.

[00:03:43] And unfortunately, huge problem in my opinion, coming from both a search and AI background, is they were just black box. They said, "Here's the thing. Turn it on, pip install modify whatever configuration so that it points to the right documents," and you get, you got some other [00:04:00] things to tweak.

[00:04:00] Turn it on and pray that it works. If it doesn't work, then a lot of these things were pretty opaque. Like, where exactly do you go to, to change all the nitty-gritty details? And I think that's unfortunate because really when you get down, down to it the pieces are transparent, and once you know what all the pieces are, it's a lot easier to think through RAG agentic RAG and actually solving any problems that you have in production.

[00:04:29] So let's go through a bit of the evolution from search to RAG to agentic RAG to even assistant RAG, I'll call it. So in the beginning, there was the search and pre-twenty twenty-two, right? Before every, all the fireworks started. User makes a request to the search application. The search application is itself...

[00:04:50] it, I guess it could be thick, but out of the box it's pretty thin layer. It says, "The user said this thing in the little box on the screen, so we're gonna [00:05:00] convert that into a search across a certain number of fields. We're gonna weight the fields differently." It basically wrote the search that goes into the search system, whatever that might be.

[00:05:11] So I, I am very, I'm thinking very much in a lexical mindset, but this is how things worked in twenty twenty-two. The search engine returns all the documents, and those are, cleaned up, augmented by whatever you need them to be augmented with and returned back to the user. Done.

[00:05:28] Now, when RAG was introduced, it changed the equation a little bit. Effectively, instead of a... The user request initially often went, still went through this application step and got the search documents out. But instead of just passing them back directly to the user, we make sure to represent the docs to the large language model agent and generate a response.

[00:05:52] And then typically these applications were providing answers more so than documents back to the [00:06:00] users. Very useful. It, it has been doing its own revolution, like twenty twenty-four was the awesome year of RAG. But- let's dig further. With agentic RAG, we change this up a little bit.

[00:06:13] So instead of circumventing the agent we give the agent the ability to make its own judgments about the user's request. Whatever the user types in the little box at the top of the screen the agent now is doing an extra task of interpreting that intent, and that allows it to make its own query against a search tool that hits Elasticsearch or whatever search endpoint that you have.

[00:06:42] Now, you can make that even more powerful by adding an inner loop. And I labeled it research, but basically it just gives the agent the ability to not only make one search, but you can, write in your system message, "Please do a a narrow search first, and [00:07:00] then maybe expand it to some parallel searches and then gather the best content back."

[00:07:05] If you want to make it, in some ways, depending on your application, even better, then think about building out the user experience as more like an assistant, and this implies adding just one more loop that includes the user in that loop. So basically, rather than... I- in, in this case, rather than the user typing in something in a text box and it goes into this inner loop, this little research loop the...

[00:07:33] it's more like a conversation. The user asks for something, and oftentimes that ask itself carries more content than just whatever would come into the text box. That's already good. But if the agent makes a bad response, then the user can offer some correction. So by having an assistant-type user experience, you get to gain a richer and richer context, which will [00:08:00] make intent interpretation way better.

[00:08:05] Better understanding means better answers.

[00:08:12] All right. So the beef that I had with RAG as a black box is what on earth do you do when it breaks? It's it's just a thing, and since it's atomic, it's can't be broken down. What do you do? It's easy when you can look through the black box and see all the pieces that are in motion. In this case, me coming from a search background and a large language model background, I just see two chunks here.

[00:08:41] And I can think about them independently. You have the LLM agent- It takes in information, it has access to tools, it's got a system message, all that stuff. And you have the search engine, and we've been doing search for forever. So think about it like a pipeline. Any of these things, y- [00:09:00] if RAG is broken, it means that you're getting unexpected results.

[00:09:04] The input leads to an output that is unusual. But when you can break it down and see it for its its candidate parts, you can see that maybe the breakdown happens maybe it's at the ETL. When you're trying to index things, maybe you indexed it in a way that it makes it hard to search. Maybe it's the search relevance its- itself.

[00:09:25] The documents are all there, but we're weighting something incorrectly, we're not incorporating popularity. There's any number of things, but you can think about that in isolation. That problem has been dealt with forever. Or maybe it is some, some of these line items here that the agent is responsible for.

[00:09:44] Maybe when the user says something, the way we're presenting it to the agent makes it hard to understand for the agent. Maybe the documents don't have all the information that they need, and they need to be augmented. Maybe Howard's generating a response that's hallucinating, and it needs some [00:10:00] extra guardrails to prevent that.

[00:10:02] So once you think about RAG as a pipeline, it becomes so much easier to deal with it to bisect the problem until you find where the problem is, and then fix it.

[00:10:17] So we're entering into a, an unusual place where maybe an AI agent can act i- in place of an ML search team. Now, there's gonna be all sorts of caveats to this. We're at the very beginning of this, but I... there, there are huge glimmers of hope around this. So imagine that it's back in 2022, which I think of as the beginning times for the revolution.

[00:10:47] And you're running a small to mid-size e-commerce site. It's super important for your success to have search returns relevant results, and [00:11:00] the steps involved when getting your search site set up is, okay you need to adopt search to begin with. So OpenSearch Elasticsearch, they were the biggest players, back then.

[00:11:10] But Shopify I imagine, I guess Doug could tell me has its own API that is probably an easy thing to start with. I don't know. If you get a little bit more sophisticated, it's time to improve your search. So you actually start doing the right things with data. Log into search, figure out what are the popular queries are hand-tuning things relevance parameters.

[00:11:33] And then the next step is get awesomer, like click tracking, judgment lists, semantic hybrid search, some of the newer things that were being introduced at that time and have actually themselves have become even more interesting and powerful since then. So those are still all on the table.

[00:11:49] Now, if you're a small to mid-size e-commerce site, adopting search is going to be pretty easy for you. You need your developer to, just read the tutorial, [00:12:00] and you're gonna get, I don't know, 70% of the way there. It's something. Improving search it's a little bit more tricky for sure.

[00:12:07] You have to start setting up special processes to, to figure out what the important queries are and start tuning that the parameters in your search to optimize not just the page that you're looking at right now, but all of them. Things do get tricky, but it's doable.

[00:12:24] And as a matter of fact there is a book written on the subject that you should check out. I think it's still relevant. And finally, if it's time for your small to mid e- size e-commerce sh- site to get even better, then you're looking into sometimes really sophisticated things. And for a lot of for a lot of the smaller players I'm certain that this is a roadblock.

[00:12:48] They got... they're successful enough, but not successful enough to maybe hire a dedicated ML team that, that is really going to do the right thing with search relevance. So [00:13:00] 2026, we have a new option that is becoming a really attractive possibility a- and that's agentic search.

[00:13:09] So AI is a lot more accessible than classic ML. Everyone understands language, and now we've got this weird API that speaks language to us. We can talk human. There's no need for linear algebra or gradient descent, anything like that. It's just something that we can look at how the agent is reasoning through stuff, and we can understand it as if we were working with a person.

[00:13:40] So that means that improving agentic search is going to be more intuitive. It's not about retraining models. It's not about finding the perfect model that's a good fit. It's not about, The same type of data cl-cleaning and stuff like that. And if you view it as a pipeline, then you can just read the traces, think about [00:14:00] how your new AI intern i-is itself thinking through the problem space, and you can help it get better at its job.

[00:14:08] That's how you improve agentic search. And also if this is promising right now, then think about the speed at which things are changing. It is scary, it is weird, but it does mean that a reasonably capable agentic search right now is only going to get better as we understand how to deal with this crazy new technology, and as the technology itself is getting better.

[00:14:34] So all sorts of neat things that make agentic search a very attractive possibility.

[00:14:43] So let's show I've al- I've already explained how search is related to RAG, is related to agentic RAG, agentic search and then to, this more conversational version of search experience. So let's look at where the magic lives and what makes this so [00:15:00] appealing. The first thing is that search, let's go from the inner loop, and then let's progress to the outer loop. At the core of this is an individual search request made by the LLM agent to the traditional lexical search, for example. Now, large language models have been trained on everything that we've ever written that's in the public domain, and even some stuff that, that's in the private domain as well.

[00:15:31] Some things slip past. And that means that they have a really good an increasingly good understanding of just common sense topics. Whenever your user makes a mistake, a misspelling, they say Reebok shoes instead of Reebok shoes, there's supposed to be an extra E in there. The agent's "Okay I could copy-paste that, but that'd be stupid.

[00:15:54] I know I'm dealing with shoes, and this is obviously a misspelling. I know the inventory well enough, I can just fix [00:16:00] that." And you get an autocorrect that you didn't even ask for. Synonyms. If the agent sees a search for pumps then it knows, okay, heels, high heels, these are all things that are the same.

[00:16:12] So if you coach the agent to, to think about that and to broaden their search, the agent should be able to make, certain types of synonyms if it's a domain that the large language model has had plenty of access to, which is a lot of the domains. Filtering. If a user searches for something like red Nike size eight, internally, if you have lexical search, for example, if you have some sort of search where it's easy to filter on things, then each one of these words is not really a search that you want to go to just the title of, your inventory or the the content, the description of a product in your inventory.

[00:16:53] These are different facets, different fields inside the structured document that [00:17:00] outlines your product. Red is a color. Nike is a brand. Size, search eight. And so if you give the agent the ability to understand how this schema is set up and what types of fields it what values it expects to see in these fields, then the agent is gonna be able to figure out how to slice and dice that query up.

[00:17:23] This natural language text can get turned to a very surgical subset of the index that returns exactly what the user had in mind, whereas content search for this is gonna be very subpar. All right. Dress shoes. That's something that has tripped me up during my entire search career.

[00:17:43] Doug, this is the reason that I don't do search anymore and I do AI. In natural language, English I'm sure this is true of any language, has these gotchas. A dress shoe is not a dress, it's a specific type of shoe. We can imagine in our [00:18:00] minds exactly what that looks like. And if a user just types that in and we're using a traditional search application in front of the the se- search engine, then we have to do all sorts of acrobatics to figure out what are all the types of things that might fall under this category.

[00:18:17] Are we in one of those categories now? If we are, special handling. But the agent can say, "Okay, I know what a dress shoe is. I understand from the instructions, from my system message, that this requires special handling, and so I'm gonna put it into to quotes, and that's gonna make sure that it really targets only things that are the match for the concept of dress shoes."

[00:18:39] So effectively, one of the things that we're starting to get out of here is, The agent is starting to fake semantic search. It's not the cool... it's still not the cool vector search where it's like you can type in the idea and it matches anything with the idea, just searching an idea space. It's totally a cool topic but when the [00:19:00] agent can start using synonyms and repairing searches like this, then it is getting at something that is going to be more semantic than just copy and pasting what other users said into the Elasticsearch query fields.

[00:19:17] Let's bump it up to the inner loop. All right. So at this point, you get the tightest inner loop is just one query. At this level of the inner loop we can also provide the agent with some understanding about the strategy that it needs to take to, to move through the index. In our instructions, we can say "The user's going to ask you a question.

[00:19:42] You need to do a quick broad search to get an idea of the index in the neighborhood. And then once you have a broad search figured out then, brainstorm to yourself, do a little chain of thought reasoning, do a little thinking and figure [00:20:00] out, what are the synonyms to look at, what, should we make use of any of the facets, the filter fields," all the stuff above.

[00:20:07] And the agent can parallelize several different queries and get to much more relevant results. So this is, again, a sort of way of faking out semantic search by just asking, for all the synonyms and stuff like that. But you're not limited to what I just said right then. You could have the agent do anything you want at that point.

[00:20:27] An- another... It would take longer, but another cool thing that you could do, depending on your user space, is to have the agent be more like a researcher. This is really important to get the right thing, so we're gonna introduce the search tool, we're gonna introduce instructions about how to iterate until you get all the information that covers the field that the user's looking at.

[00:20:49] And may- maybe you can have other tools around there, like other tools so that the agent can introspect about, what types of fields are inside these filters, it's a color field, but [00:21:00] what colors do I have options for? You can have other tools for the agent to collect the ideas and make sure that it says, "Okay, this group of products covers this aspect of the request."

[00:21:13] You can do anything you want to. And for some fields, it's super important. One of my early search projects was with the United States Patent Office, and- When an e-commerce user goes and looks for shoes, they wanna find a bunch of products, and they're gonna pick out the first one. Or they're gonna make a very specific request, 'cause they have the thing in mind they want, and they're gonna see it on the page or not, and either click it or just abandon.

[00:21:42] With patent search, it was... working with these people was crazy. It was like working with AI agents there. Because they want every single thing that matches any aspect of this, and they want it very tightly cataloged because it becomes their [00:22:00] palette of work a- as they're figuring out if this new idea matches anything that exists in the the patents that currently exist.

[00:22:09] They need to know all the information. So on the inner loop, you can do whatever you want. It's there for the the agent, you just have to train it. And if you are fortunate enough to have a conversation experience, I really like this, and I really hope that we drive more of our user experiences towards a more conversational experience.

[00:22:35] I think we probably had a little bit of burnout early, earlier on in this whole revolution because everything was conversation for a while. But done well, I think it has some really neat qualities to it. For one thing, think about today's typical user experience. You go to a website, you have your text box there, you're clicky around, typing in a text box, clicking on [00:23:00] little glowing boxes on the screen.

[00:23:01] The whole idea of clicking on glowing boxes on a screen, that whole user experience has only existed for 30 years tops. Conversation as a user experience has existed for about 50,000 years. So it's a, it's there's a little bit more heft behind this as actually being useful. And the reason that it's so useful i- in an agentic search experience is because, what I alluded to earlier, you are allowing the user to participate with the agent.

[00:23:33] They don't just fire off a request, look at the results, and then take them or leave them, which is pretty much what you're doing if you only have the inner loop. But they're looking at the results. They're dis- they're clarifying their intent with the agent, and the agent having access to the full conversation as it progresses, the agent is going to have a very rich understanding of what the user has in mind, and that's [00:24:00] gonna just make it a lot better for them to search the corpus and get back the information that the user wants.

[00:24:10] All right. Any questions so far? Oh, I am actually going a little bit faster than expected. We will have time for questions at the end. Douglas has a question: How do you deal with non-deterministic nature of your LLM agent? Yep, that's the nice thing about traditional search, because you search for XYZ and it returns the same thing every single time.

[00:24:33] The way the way you deal with the stochastic, non-deterministic nature of an LLM is you view it as a good thing rather than a bad thing. It is going to give you different answers for the same request. You could turn the temperature down and maybe it'll be a little bit more constrained, but still it's going to act like a human.

[00:24:58] Basically, you've [00:25:00] hired a very forgetful but tireless AI intern, and they're gonna have their own opinions and depending on what their internal temperature is and their internal state, it will lead to different results. But the idea, the hope, is that overall, it's going to be much better than the out-of-the-box I've opened Elasticsearch and I've hand-tuned the query a little bit.

[00:25:29] Because it has all this intuition about, common sense, misspellings all this stuff right here. It, it has that.

[00:25:36] Yeah, and there's a lot of stuff, I don't know if you'll get to, about just... And I definitely talk about this in my course, it's like a major theme, like wrapping a lot of these agentic loops in really good harnesses that are giving feedbacks to agents to say, "No, you're..." An LLM judge or something saying, "No, you're giving the wrong answer," or something, some model that's [00:26:00] helping guide the agent towards the right answer.

[00:26:03] And that's, yeah, so that, that's an interesting topic in and of itself. When I started building AI applications for customers, my idea in this space was let's build something like a workflow, where there's a node in the workflow that is do basic search, and there's another node in the workflow that's like the guardrails.

[00:26:23] Is this, is there anything that that we've messed up on and we should cut out? Is there have we covered the user's intent? And then maybe a literal go back, arc in the, in that diagram to the search again so we can cover our bases. What I'm seeing things heavily tilt toward right now in the AI product design is very interesting.

[00:26:44] A- an agent has almost become synonymous with an LLM called in a loop with access to tools, and so a lot of what I used to do with hard-coded guardrail nodes get finished with this node [00:27:00] and go to the next node, you can almost program in English. I think we're getting there. The models are getting better and better at reading the way you want the search request to go and just doing the right thing.

[00:27:14] It's not perfect. We're getting better. But I think that's the direction we're heading towards. So English or whatever language you want is a programming language now, for better or for worse.

[00:27:29] All right. Probably getting back at what our previous questioner said a bit here's all the opportunity. There's, here's where the magic lives. This is the good picture, but is the magic enough? So even though I think this is a really interesting space that we're getting into it's emergent right now.

[00:27:50] It's something that we're trying to fig- to wrap our minds around and see, how far it really can go and there are challenges. One challenge, a- [00:28:00] and Doug and I have both done a lot of playing around with little toy problems in this space, is is making your agent aware of the index can be challenging.

[00:28:09] Like the in- the agent can see a very well-described search tool, can understand the fields but how does it know really which field it search, should focus its search on, name or title? Or should it use the brand field? Or maybe there's like categorization field and there's 4,000 different possible categories for your giant index.

[00:28:31] How do you describe this stuff to the agent in a way that it can make use of it? Some of that maybe you can stick into the system message, but maybe not all of it. Making the agent search just like a human, so going to the outer loop is still hard. One way that you can guarantee that it shape it searches exactly like what you have in mind is to do a workflow.

[00:28:53] You've got a bunch of nodes, and you say, "Once you do the main search, you go here and check other results," and, if-then stuff. [00:29:00] But like I said a lot of applications seem to be headed towards program in English. Tell the model what it sh- should do. But it's not quite there yet. The agent has- sometimes takes leeway that you don't want it to.

[00:29:14] I think ultimately we're gonna get to a point where programming in English it's going to obey it better and the leeway that it does take we'll be able to look at it and say, "Ah, as a human, I understand, why you made an exception in this diagram I had in my head that I've tried to encode in English."

[00:29:34] But it's still talking English to an AI intern. Latency and cost. This can be a big shock, especially to old-school search engineers like, like I was. Everything back in, in the day when I was building search was make latency as low as possible so that the user can search again because it's the user, it's upon the [00:30:00] user to clarify their own search and navigate the index and find the product.

[00:30:05] If we get to a point where agentic search just delivers the right products, then the user is going to be super fine with seconds return time instead of milliseconds return, return time because the effort on their part is just so much lower. And the business is also gonna be fine with a cost increase because we're getting much less abandonment.

[00:30:29] We're directing the customers to the products that they're going to purchase. But as you are trying this out, latency and cost are both things that you definitely need to keep in mind. There are results there are resolutions to all of these on the horizon. And in s- in several spaces, I bet the re- resolutions are here.

[00:30:50] Prompt engineering. Make sure you write good detailed system message that covers how to make the individual searches, that covers how to make the higher level [00:31:00] research behavior. Make sure that you provide sub tools if your agent needs more accessibility to understand what is in the index.

[00:31:11] One of the really cool things about lexical search is when you issue a query- Not only does it return the search results, but it has a set of counts across all the other fields for all the products left in the inventory. So I search for Nike shoes and lexical search can also return okay, what size is that?

[00:31:36] We have, 20 products in size nine, we have 30 products in size 10, we have... it can return all that information. What colors do we have? We have, 100 products that are white, 20 products that are red, and you can feed this back into the the search agent as well and allow it to gain a better understanding for what is actually in the index.

[00:31:59] You probably [00:32:00] also want to provide thorough exam- thorough examples. If the user searches for this, here's an example strategy that, that you can use. Great... A, a great way that you can do this is to focus on the very typical, like the top, 10% queries, which is usually a really small number of queries that covers a lot of the queries that are being issued.

[00:32:22] And make sure the agent has rock solid understanding about how to deal with those things and it'll return better behavior. You can also... it starts including more specialized experience but you can also do fine-tuning of these large language models. It's not so bad as finding your own...

[00:32:43] building your own neural network architecture and doing the training in the raw. But there are a lot of APIs now that allow you to say, "Okay, given this input, here's a great output," and it's text to text. And so training is actually on the table as a very feasible thing, but that does imply more [00:33:00] complexity.

[00:33:01] And the last thing that you can always do these days I- I s- I don't th- I don't think AI is getting... is slowing down. We're at least linear- linearly growing, maybe even exponentially growing. You can wait a month and that might be what you need to get over some of the problems the challenges above.

[00:33:22] All right. With that in mind I'll pause, take a sip of water. Ask me a question, and then we'll get into a final portion of the presentation where I will talk about how you can incorporate agentic search into user experience without starting over from scratch. We have two questions, one from Debra Bratta.

[00:33:43] How the... how does the feedback loop work? How does it penalize inaccurate results in iterations to reach at the final result with the desired confidence? You might wanna unmute and clarify in case I get this wrong. But there's [00:34:00] two places where you might talk about regulating the results that come back and making sure that they're up to par.

[00:34:07] One thing is institute, like in the model in the agent when it's making the request you, you can instruct it "Here is how to know that this is a good result. If you don't have good results, go back to the well, get another bucket and, try some more." But you also need to think more bigger picture, how do you yourself know when the agent is doing the right thing or the wrong thing?

[00:34:33] Like if I was to approach an e-commerce client and just make up some rules for how to define what is a good result or a bad result, I'd have no clue, and they wouldn't either, even though they're experts in this space. Probably, what you wanna do is go back to the notion of large language model evaluation and optimization.

[00:34:53] Look up Hamel Hussein, he's got, and Shreya, forgotten her last name. They've got incredible [00:35:00] content on this, but it involves basically, finding logging all the behavior you can. Allow your users to use the search, finding the ones that are problematic and start cataloging, read the traces, read how the agent thought through things, and start cataloging the types of errors that you're seeing the agent make.

[00:35:20] And then based on that, you can create little tests modify the system message and try to optimize how they're performing on these tests that are now aligned with your observed understanding of how the agent should be asking and how it's failing. Does that make sense?

[00:35:41] I think so. Did that make sense to you, though? Yeah. Kevin wants to know, does vector search still help if you've got tool calls or search loops? So I guess, yeah. Does a vector search tool- That's actually really interesting. One thing that I've wanted to [00:36:00] do, and I just haven't found a good apples to apples comparison, is can you build a agentic search backed by lexical search engine that beats vector search at its own game?

[00:36:20] Can you use the notion of synonyms in broadening search and searching through an index like a human would and actually get better results than one-shotting a vector search? I haven't found a good way of making a comparison that makes any sense, unfortunately, but that right by itself is a very interesting space.

[00:36:38] Now, a different way of interpreting your question is okay, but I still wanna do agentic search, but rather than lexical search, I want to use semantic search, vector search internally. Is that still useful? There, there are interesting things you can do. Lex- agentic search backed solely by [00:37:00] lexical search, I get a feeling that it takes away from some of the utility of it.

[00:37:07] Because if you search for synonyms against nothing but lexical search, you're just gonna get something that's in the same portion of the embedding space, and it's just not really gonna help you that much, I bet. But hybrid search is still totally in play because you can tell this, you can have certain fields that are really important to match on term-wise like title.

[00:37:31] I want to have an exact title match. Product names, people's names, these things are garbage in lexical search. The... anything that's new terminology... Sorry, these things are garbage in semantic search. The vector search doesn't really do a good job about mapping that to a sensible portion of the em- embedding domain.

[00:37:50] So you could have hybrid search, and you can tell your AI assistant, "Hey, if the user seems to be looking for something that's like a title match, [00:38:00] use this tool. If the user is looking for something that's like an idea, use the lexical search." And that might be that might trump everything I've talked about right now because it uses the best tool at the best time.

[00:38:13] So good idea if that's where you're headed at.

[00:38:20] All right. And then Alexandra wants to know- Yep ... are relevance measures like nDCG still... Do they still make sense with agents? I'll just say I- Oh, sure ... I think they do. But yeah. I don't know, John, if you have a perspective on that. Yeah. What Doug hasn't told you is that Doug and I are going to be doing a workshop for someone else's...

[00:38:41] for Hugo's course later today. And we're going to kinda test that out. Definitely nDCG, Normalized Discounted Cumulative Gain, that's the worst acronym in the world that's definitely s- still- A valid way of testing the [00:39:00] results of agentic search. Nothing really changes in the formulation of that equation.

[00:39:06] And so it's a good way to compare. When you try this yourself, if you happen to have a solid judgment list, that's a really great way to see if you're there yet, if this is worth actually doubling down on. So yes. Barely yes. All right. So the last portion of our talk today is practical UI/UX stuff.

[00:39:32] I've always been a deep backend engineer. But when Doug and I wrote the book on relevant search, I drew the short sto- straw, and I wrote the UX chapter, and I was like, "I have no idea." But it was a great chapter 'cause I got to I got to really think through the problems and the product understanding.

[00:39:49] It's it's been a neat part of my career, it turned out. And so this is... So this is my little help pad. This, on the screen right now, [00:40:00] is a example of a traditional search application. You can type your stuff in... Let's see. I'll do this one. You can type stuff in this field and click Search, and it does the right thing.

[00:40:14] You get facets on the side. You can click the facets and filter down on stuff, and it shows you the subset. It's a nice way of slicing and dicing. You get relevance sorting, or you can sort by other things newest or high to low price. This, so this is very traditional search. Now, imagine you are at this company and you wanna try out AI ag- agentic search.

[00:40:47] You might be tempted to say, "Let's just throw everything away, and we're gonna pop open a conversation box over here, and it's just gonna be a completely new experience." That would be a terrible idea, [00:41:00] because your users are going to be so disturbed by the new experience that they're going to mass exodus.

[00:41:05] That, that's just not a great idea at all. Instead, I'm gonna show you a three-step process where you can gradually introduce agentic search in a way that s- does not disturb the user experience at all initially. It actually augments it from right out of the box. And as you get proof from your data that users like the experience, then you can start increasing and going to more and more agentic-type workflows.

[00:41:36] All right. So the first stage of adopting agentic search is what I'm calling the beginner stage, and let me just- Here's what, why I created these little tools. Let's say let's say we search for new listing downcount- downtown condo. So in this iteration, the search app has changed nothing at all.[00:42:00] 

[00:42:00] It's still actually directly going to the s- the traditional search app, traditional Elixir search, all these things hit the screen immediately. But the one change that we have introduced is for the price of, what's this? Like 20, 50, 60 pixels here, we have an area on the screen where it say- the agent says, "I think you might have meant this."

[00:42:24] Property type, condo. Search terms, downtown. Sort by newest. And you give the users a chance to say, "You know what? I like that. I wanna see if that does lead to better results." So as soon as they click Search the little box collapses down. You don't need it anymore, and you start seeing the sort by used to be relevant search, which was not what I wanted.

[00:42:47] I did want new condos. W- we have appropriately selected the filters here. And whatever doesn't fit in a filter goes into the search box. So this en- ends up being a really [00:43:00] nice way of filtering of directing the user to a better interpretation of the search, costing them no time and latency.

[00:43:08] And it provides a really good way to figure out how often they are clicking this little box here. This is good. I want it. So you can look at your data and see if it's time to progress to progress to step two, intermediate search. With intermediate search, we s- we have seen so many people wait for this and immediately click on the search box that we've just decided to make this the default experience.

[00:43:38] And so right now, instead of going directly to the search app, we are going to the agent that then itself is in charge of the tool and getting the results out. You do forego some latency here. If your agent, does three sets of parallel queries, it's gonna, it's gonna take more time. But [00:44:00] if the user is getting to the results they want faster, your users will not care.

[00:44:05] They will appreciate the work that the agent is doing on their behalf. We've still kept this bar right here so that the users don't get too confused. I'm sure there's probably better UX for this. But basically, we say, here is how we've interpreted your query." There probably should be an escape door, hatch here so that you can get back to no, I just want dumb search.

[00:44:26] And then you can see how much people are searching on it going back. The other thing here, though, is while this is while the search results load, we've introduced another element on the page. You don't have to do this, but think about the possibilities. It's taken a little bit longer to load the properties, but once they're loaded, the agent has access to all of this content in its context, and it can start editorializing this on behalf of your customers.

[00:44:54] It can explain a summary so the user doesn't have to look through here, and maybe, [00:45:00] if presented correctly, the users can look at a really quick summary and understand, "Oh, this is not quite what I want," or, "Oh, I need to include these other terms," something to give them a little bit faster response time.

[00:45:13] And additionally, we can keep the users engaged. We can say, "Okay, based on your search, you might also be interested in three-bedroom houses under 100,000 in Oakland and Berkeley." And so it does the same thing again, and then you get the generated search re- results again. It's just another way of having your users exposed to a traditional-like search application but it's slowly adopting AI.

[00:45:42] If the experience is still positive, users like it you're getting more purchases, less abandonment, then that's where we go on to advanced search, and that's where we have actually done the thing the concerning thing, we have gotten rid of the user experience. Maybe you want to [00:46:00] introduce both of these at the same time.

[00:46:01] I don't know. But what we have introduced here is a new chat experience, and what you're gonna find out is users right off the bat are going to behave differently when they're using the metaphor of conversation as opposed to the metaphor of, 2020 version of Google. Type, text in a box and have Google be psychic for you.

[00:46:26] And so let's let's try it out. What if I was to... I don't know exactly what I want, but I'll text-to-speech this. I want a big-ass house. There we go. A very broad query. I just... What does the agent do with that? Let's see if the agent, having common sense about what this might mean, can make, can infer what might actually fit in the cat- in this catalog.

[00:46:55] How cool. It figures out that I want a house, don't want a townhouse or [00:47:00] condo. It figures out- That four or five bedrooms probably qualifies as big ass. And it, it says we can also look at the square footage and make sure that's as high as possible. But remember, this is a conversation.

[00:47:15] It gains context about stuff. I don't know. What's a good way of asking this? I can ask not only about the search page results, but I can also say things that take into account aggregate information. I can say things like "I'm really looking for something that's below a million dollars.

[00:47:36] How many items are on the market below a million dol- dollars?" And so it might change the search, I don't know, or it might just look at what it has access to, because it can see the facets it well- as well, and it can see other stuff that we don't necessarily display on this page. Or it might just never return.

[00:47:57] That's a fun possibility, too. [00:48:00] All right. You'd like to know how many four or five bedroom houses at least blah, blah, blah, blah. Based on your current filters, there are eight, and it actually did update the filters for me since I wanted below a million dollars. That's cool. So it's working together.

[00:48:16] I can interact with it, make the changes in the traditional way. The agent sees the changes that I make, and it's like having your own search assistant guiding you through the inventory. So a really cool experience that is surprisingly available to not terribly specialized search teams. We're all learning how this works right now, and AI product is getting easier and easier to build.

[00:48:42] So I think that's... Oh, wait. I do have the final slide. So what have... stuff we learned. I copied and pasted those original things again. We learned them. And if you guys still have a little time, we're a little bit over, but I will stick around to the bottom of the hour for questions.[00:49:00] 

[00:49:04] Cool. Thank you, John. I like your example query. That's gonna be my new go-to search query, big ass house. Any questions for John? I know people have asked a bunch already.

[00:49:30] Does anyone wanna unmute and say hi? D- Douglas asks, "How complex is your mapping? Any nested data?" For my toy demo, not very complex at all. The application itself is not even Elasticsearch. It is I literally vibe coded something that was a good enough search over 300 products. So it literally just searches through all the J- JSON blobs for all the products.

[00:49:58] Okay. But it was neat [00:50:00] that it didn't have to... it did a pretty good job in this particular example about figuring out which category it should filter in, what values to use there, 'cause I presented that to it. Do you have any follow-up? I saw you unmute. Yeah. Yeah, John, so even with your vibe coded example and your 300 products, but was...

[00:50:18] Like, how complex was the structure? Because that's what I see in different environments the structure will vary. Whether that data is coming from a Salesforce or or an Elastic or some other, system, when you put it together it's not flat. It's different levels. So I just wanted to understand in context of your demo, did you have to do that?

[00:50:41] In the context of the demo, no. It was flat. In the context of going into real life, the real world I th- it, it goes back to the beginning of this talk. I don't think about RAG as a thing. I think about you have an agent, and you have a tool that allows it to get information from the outside world.

[00:50:59] The [00:51:00] tool that we focused on today was implicitly lexical search only, but the tool sounds like that, that you have in mind can draw from databases. It can draw from different document types. And I can only start to imagine the complexity that you have in mind. The answer is still going to be guided by that same discussion.

[00:51:21] There's no such thing as RAG. There are these transparent agent and tools. You probably need to have a tool for Salesforce. You probably need to have a different tool for the d- other different stuff. For each tool, maybe if the agent's trying to use it and it's screws up the first time, you'll need...

[00:51:37] The error message doesn't need to be a machine error message. It needs to be, like, a pep talk to your AI interns. "Oh, looks like you're trying to use this field and this tool. Do something different." And so it's still gonna be the same thought process. But admittedly it, it could get as complex a- as you can imagine.

[00:51:56] Okay. I got one last question, [00:52:00] and I don't wanna go too deep in it. So but your agent itself is it an agent with tools? Do you have a plan, execute, reflect style approach, or how deep is that, your agent there? In the demo- We- ... and, like- In real life. Yeah, in real life, yeah. Fortunately in, in this case...

[00:52:25] Okay, let me think. In the demo, it's very simple. It's an agent with a system message that says, "You're looking at real estate search. You have access to this tool. The tool has these five fields, like house type, price, square footage." And it's gonna say for the search strategy, the first inner loop it's something simple.

[00:52:54] Do your best to satisfy the user's query. Very dumb, but obviously good enough for the simple [00:53:00] example. In more complex real-world situations, sometimes y- you actually have something equally simple as this. If you just got an, literally an e-commerce site, then see how far you can get with exactly what I just said.

[00:53:14] If you have something more complex, like what you have in mind, then I would... These days, I would take advantage of writing it in terms of a skill. I think in- increasingly, whereas two years ago, I would build a work- workflow, very bespoke, start at this node, go to this node go to this node.

[00:53:34] One year ago, I would build an agent with a loop exactly like we talk about loop and tools. I think next year the rest of this year, we're gonna see the... even that idea commoditized, where you just have the notion of the agent at Carnas, the agent at runtime, and it's going to be able to understand skills, and you program in a in agent skills.

[00:53:55] So your agent skill for finding stuff in the different domains is a different [00:54:00] skill, but the agent will be smart enough to look up the skill it needs and go get what it wants. Oh, okay. That- Yeah ... that's what I would do. Yeah. That's yeah, that's pretty good. Yeah. And thanks a lot for that.

[00:54:10] Yeah. Thanks, Douglas. Aydin has a question: Is agentic search a real possibility in terms of latency, letting the user wait? And I don't... I will say, I think in a chat context, we've all gotten used to that. I feel like we sometimes want a good answer, so we are used to it, but we are also sometimes impatient and say, "Give me an answer now."

[00:54:35] So I do think I do think there's a little bit more tolerance if people know they're getting something better especially if they th- see thinking to do something. Intr- I... It would be, I'd be curious, John, what, on your thoughts of that too. The proof's in the pudding. If you can build an- agentic search application in your domain and always get [00:55:00] the right answers to the users and it takes five seconds, they're not gonna care.

[00:55:05] They're gonna say thank you because the process of them making a search, getting, the five-millisecond response back, seeing that it's wrong, digesting this page of content e- enough to understand how to correct their own search, doing the labor of s- subselecting facets, all the stuff that they have to mentally process to get to the right s- results, that's gonna be more than five minutes...

[00:55:27] five seconds spent on their part. If you're getting better answers, they're gonna love it. If- but there's a threshold. If it's the kind of the same-ish answers and you just got a little bit of improvement then at some point it, it won't make sense anymore. It would just be expensive, latency and cost.

[00:55:45] That's it for today. I hope you enjoyed it. Uh, please check out more at arcturuslabs.com and make sure to look at my blog post

