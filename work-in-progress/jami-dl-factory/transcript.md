# Conversation on Software Factories and AI Enablement

[00:00:00] **John Berryman:** All right. The thing I wanted to get started with was how did we get here? I am John Berryman. I am an independent consultant at Archers Labs and I focus on AI product engineering. I really I'm like equal parts product and engineer.

[00:00:15] **John Berryman:** I really love making the system, but also using this crazy new tool that we've got. It's the first tool that humans have made that we can speak to, and it speaks back. Can't do that with a hammer. But as a consultant, I've been kinda locked away for a while. I do my own thing. I help clients out, but it's, as an individual, it's in series and I miss being on a team. it occurred to me there's all these videos on YouTube about claw code and how to write code as an individual. And it occurred to me that I'm actually missing out on the cool developments and the team experience and what is happening to the companies right now. So I tossed out a question on LinkedIn that was actually got a lot of good conversation going where it's basically [00:01:00] what do people do now?

[00:01:01] **John Berryman:** What are the new, processes that are being developed so that you can actually plan the product and build a thing so that you don't have a bunch of developers stepping on each other's toes and building the same thing twice. So you don't have like anarchy so that you can review the code.

[00:01:17] **John Berryman:** Like some people are like, no, it's humans. Read every line. But my gosh, there's a lot of lines right now. What are the tools, the skills, the disciplines that are evolving? And like how are the roles shaping up like the engineer is? I always knew it dark ages 2022 and earlier. That didn't quite exist anymore.

[00:01:35] **John Berryman:** That's quickly going out of outta existence. But I think something more interesting is coming to replace it. all these questions in mind it occurred to me rather than being sad, I'm poor me, I'm a consultant and I'm just locked up in one project after another. It's like I, I'm supposed to be doing content anyways. So why not just start interviewing people and get the experience from everybody about what's changing? Figure out the pain points, figure out what's working and what's [00:02:00] not and learn, everyone learn together. Today I'm welcoming Jamie Couch and Dave Lane from Twin son. Greetings fellas. Maybe start off why don't you guys tell us about yourselves in individually but also about, your role in twin son and what twin son does. Jamie, would you like to go first?

[00:02:19] **Jami:** Yeah, a little bit about me individually. So I've been at Twin son for eight years now which is, Feels like a very long time when I say it, but it hasn't felt like that there. I actually grew up in Franklin, Tennessee in the area. And I got a PhD in Biochemistry from vanderbilt back in 2014. And then decided to take a different path than that would normally lead to ended up at a software development agency here in town working for Dave actually. And then, you know, several years later joined Twin Sun [00:03:00] and have been kind of rolling there. So I've been the CTO, going from a. You know, for four person, partner only business, all the way to you know, we've got a, a full team now. So I'm not generally developing on client projects anymore, but more facilitating, you know, making sure the team is has what they need to be successful investigating, you know, how should we be incorporating this AI thing that's going on that sort of thing.

[00:03:30] **Jami:** So, you know, that that also does lead me some time though to be able to experiment with new things and, you know come up with ideas and go, Hey guys, look at this thing, you know, maybe this would work. That sort of thing. So for me, I think seeing the AI tools develop is, very exciting because as someone who's not, doesn't always have their hands on the keyboard anyway. you're saying, it's a tool that you can speak to and it speaks back, but it also [00:04:00] makes things for you when you speak to it, which is cool.

[00:04:03] **John Berryman:** Yeah, were both really early on in, in playing with this stuff too. I, I do AI tinkerers Nashville and both you guys had some really cool demos for the earlier meetings. I think Jamie, yours, yours was actually chatting, this was way back, this was a year ago which is way back these days. But 

[00:04:21] **Jami:** ancient times.

[00:04:22] **John Berryman:** on Slack, you chatted on Slack and had the Slack bot talk to, I guess it was claw code, an early claw

[00:04:30] **Jami:** Mm-hmm.

[00:04:30] **John Berryman:** and rewrite the Slack bot itself and

[00:04:33] **Jami:** Yeah.

[00:04:33] **John Berryman:** itself to do something silly. I forget it was, but it actually worked in like a three minute demo. It's 

[00:04:38] **Jami:** yeah. That was like. That was like the first time. So we, Dave and I have a joke that anything we're working on Anthropic is like a month away from releasing a better version of it. And so that was probably the first instance of that. It's like, oh, this cool thing. And then a few months later, anthropic comes out with, here's the, you know, Claude GitHub app you just do at [00:05:00] Claude and it will run CLO code in a sandbox instance and send you a pull request.

[00:05:06] **John Berryman:** This is why this year I'm dedicating myself to get content out quicker because every once in a while, like it's oh, that's a great idea. I'll write it when I have time. And then it's like I'm following.

[00:05:16] **Dave Lane:** Well Jamie kinda left out. We actually met in college and he instantly, I was like, this is the brightest guy I've ever met. Like, just a genius. And so then he was like, I'm not going to keep doing computer science, and went off and got his PH or PhD and, and all that, but, i, I went to school at Tennessee Tech for computer science.

[00:05:40] **Dave Lane:** Quickly got a job during the Blackberry era. So dating myself a bit there. And I would still kill for one of those keyboards. But I worked for the agency where Jamie eventually joined us, but I got in I think I was the eighth employee. And we grew that team to 150 people. 130 engineers reported up [00:06:00] through the engineering organization with us.

[00:06:02] **Dave Lane:** So I moved up from, you know, ground floor developer to CTO. And I recall, you know, being fascinated with automation that far back. And one day I had a company talk where I was like. Here's where I think we should go. We should generate the interfaces the libraries that we use on client side applications from our web apps.

[00:06:24] **Dave Lane:** Just automatically. I was like, there's so much we could do just right away on every project if we just you know, built our own tools around generating this code. And this was like 2014 or something. And I remember one of the developers sheepishly raised their hand and was like, you're talking about automating our jobs?

[00:06:42] **Dave Lane:** And I was like, no. Like I'm not. And that's been something interesting just seeing with industry lately and all the layoff excuses around, oh, well ai, you know, we can be more efficient. It's like, you could also just grow your capabilities with this stuff. And that's really what I wanted all this time.

[00:06:57] **Dave Lane:** And then finally, you know, we get this new class of [00:07:00] tooling a, a few years ago and it's fantastic, but yeah. Now I'm CEO of Twin Sun. We're a software development agency here in Nashville. We pride ourselves on being the best. We own it. So of course we think we're the best. But you know, we're our tagline is we're fast, fearless and fully US based.

[00:07:17] **Dave Lane:** So we take these decades of software development experience. We've got apply it to prioritizing goals for software projects and get stuff in people's hands quickly and let them see a working system that improves every day. We've done all kinds of stuff. Speaking to Fearless. We've deployed custom Android kernels to submarines.

[00:07:37] **Dave Lane:** Not that submarine, not the one you're thinking about. But also deployed firmware to satellites and everything in between. We've done, you know, hundreds of projects over our careers and so the appeal of software factories was immediate for us. You know, we saw a lot of opportunity to get a lot more done and saw general applicability of this stuff.

[00:07:58] **Dave Lane:** So that's kinda [00:08:00] where we're at today. And I, I know we're gonna talk about that a bit, but it's really, I think, come down to having discipline and having all those best practices that software developers been talking about for years has enabled us to adopt agents in general and also a software factory.

[00:08:18] **Dave Lane:** I don't think without that discipline, you can do it well, and we need to do it well.

[00:08:21] **John Berryman:** Outstanding. Yeah, I think so. I think that's a good segue. To get into the meat of it then, like you guys have seen my questions, I reiterated some of them at the beginning. Like I'm interested in how things are changing, hopefully, so I can provide people some advice provide companies advice and navigating those changes. And you guys are interested in a piece of this that is gaining a lot of attention right now. The factory or the dark factory, or the somewhat translucent factory, depending on, I guess how much you get into it. Tell me what this factory pattern is. And break it down for me.

[00:08:56] **John Berryman:** What are the salient pieces of it? What's working what's not?

[00:08:59] **Dave Lane:** [00:09:00] You wanna take a shot, Jamie, or Yeah.

[00:09:05] **Jami:** So as you know, recently strong dm, published their, this Dark, the idea of this dark factory. You know, they had I think, kind of two rules, which were humans should not write code and humans should not read code. And then, you know, tokens are kind of the thing that makes this happen. Which is a really interesting idea. I think. I think this was probably around, you know maybe a month or so after Claude 4.5 Opus dropped. Because I think that was kind of the, seems to be the turning point where letting it rip autonomously kind of starts working a little bit better. 

[00:09:45] **John Berryman:** Seem to notice that is like last November, December

[00:09:48] **Jami:** right.

[00:09:48] **Jami:** Yeah. Something like that. It's pretty really recent, really, you know, it's like within the last six months and it's like old news, when are we getting the next release? You know? But yeah, so [00:10:00] that idea, you know, they've since, since published more things about kind of they publish this attractor pattern just kind of like a statement of how they expect the factory to work in terms of you know an a cyclic graph.

[00:10:15] **Jami:** And I forget which, know. Graph representation, language they use. But I think for us of the big unlocks, you know, in terms of being able to potentially make this successful is, like Dave mentioned, having a strong process in place, having strong disciplines for the, you know, for Opus or cloud code to follow. That way you're not, Kind of, you give it a framework, in other words, to build upon rather than kind of letting it choose. And it does it haphazardly and maybe the decisions all don't always make sense, you know, with each other as it makes them independently. And then you get, you know, kind of the vibe [00:11:00] coded mess that everyone warns about. So the, the way to avoid that, I mean, we, we could talk a lot about this, but the way to avoid that is with that strong process, discipline and having really good guardrails in place for it. But it's been really interesting. I think the way we've kind of gone about it is, and I think what the way to have success in a world where things are moving so quickly and you know, the next model turn, who knows what it's gonna bring, it might make everything you've built completely obsolete is really, I think, focusing on. a thing well. So, you know, for us, we don't have to build factory that's like so general purpose that anyone could use it. just need one that builds things the way we want them to be built. And that's, that's a way, you know, that's the, the twin Sun way for lack of a better term. You know, we don't need to do it you know, the, [00:12:00] this company's way or that company's way or whatever.

[00:12:02] **Jami:** We just need to do it our way and then it works for us and we can get good results about it and kind of get ahead of the curve a little bit maybe. 

[00:12:09] **Dave Lane:** I think one really good example of of iterating on that one thing well is our pull request process.

[00:12:17] **Jami:** yes.

[00:12:18] **Dave Lane:** so Jamie o over a year ago, I think introduced what we call twin sum dev, our PR bot and it's pod code behind the scenes, you know, running prompt that he's iterated on over the time. The team has given feedback too, but pull requests are in, in the agency world are a little difficult at times.

[00:12:37] **Dave Lane:** We work on a lot of projects concurrently. We have a lot of small teams, you know, one or two person dev teams. So outside of the coding conventions we have and the frameworks we typically use. Most people on our team don't have a lot of context about everyone else's applications. So when you think about what's the goal of a PR review for us, it's one, we wanna know [00:13:00] where we're following sane coding conventions, and it's comprehensible.

[00:13:03] **Dave Lane:** But two, we also wanna ensure we're implementing the thing that was specified. Like, is the work implemented properly? Does it make sense in this business domain? And what we started recognizing as we rolled out this automated PR reviewer is based on the task specification and the information it could pull about a project.

[00:13:22] **Dave Lane:** It often had better context than most of the team about what a, what a poll request was for. So over time it started feeling like the human review was just a distraction and taking time away from folks. When. Twin son death could do a lot of the work. And that was driven largely by their feedback and iterating and saying, you know, it, it, it does this.

[00:13:44] **Dave Lane:** We don't really do things that way, or it hallucinated this. We need to figure out something around that. But over time it went from this optional review step you could add in to prs, to now I, I think within a week of allowing it to, [00:14:00] to approve poll requests on its own,

[00:14:02] **John Berryman:** Bye.

[00:14:02] **Dave Lane:** Something like 70%, I think Jimmy of poll requests were approved by twin sum Dev.

[00:14:08] **Dave Lane:** And now most projects that is the PR process. And so that fell right into place in a workflow step in our factory. But it's that openness and iteration and, and trying to enhance a thing over time that really became the powerful unlock for us in, in code reviews and changing how we look at PRS now.

[00:14:28] **Dave Lane:** So, yeah.

[00:14:29] **John Berryman:** I definitely wanna dig in into this in a little bit because there's different, everyone's trying everything at once, so there's obviously different camps. Some people are like, it doesn't ship unless a human's laid eyes on code, which like, my logical inclusion is like I know what your humans are doing all day long. That's not very motivating either. But before we dig in into that I wanna dig into the prs. I wanna dig into all pieces. I wanna dig into the opinions that you were talking about, Jamie, 'cause that's important in making it work really well. But [00:15:00] I'm gonna feign ignorance and actually demonstrate ignorance.

[00:15:03] **John Berryman:** That's valid and true. Yeah. Help me understand at at a more basic level what the factory is. What are the components of the factory what are the nodes and like decision blocks, what comes outta the factory? I pretty much know, but put that into words. 'cause that'll be pieces that we can hang later conversation on too.

[00:15:24] **Dave Lane:** I, I think like the easiest analogy I have is like, if you're a software developer, you're familiar with like a Kanban board or a Jira board and having, you know concrete steps in a workflow. So you specify a task, it gets prioritized, and then you have, you know, maybe a development stage or design stage, let's say design.

[00:15:44] **Dave Lane:** Then you go through development of the task. Then you have review steps. It might be a pull request, it could be internal team review of a feature. It could be a client or stakeholder review of a feature, and then you have a promotion to production. So all [00:16:00] those workflow stages require certain tasks to be performed.

[00:16:04] **Dave Lane:** And traditionally a lot of those have been human tasks, or it may be your CI CD environment where GitHub actions trigger workflows that run tests, and then it does a deployment if the test pass. So a software factory is basically our attempt at automating many of the tasks and steps in that workflow.

[00:16:26] **Dave Lane:** So basically our factory as it stands today starts with the task specification. We enter tasks like you would enter them in tickets and Jira. We actually use Jira still. And then the workers.

[00:16:39] **John Berryman:** To.

[00:16:40] **Dave Lane:** Yes. Now we, we do use like the Atlassian MCP and things like that to help with you know specking some things on mass and things.

[00:16:50] **Dave Lane:** But yeah, we use Jira and Type, and Jamie tied that into the factory to look at what work is available. Then we have work delegated to runners that are running [00:17:00] cloud code agents. And they review the plan, implement the task, and then it goes through our workflow of, you know, PR review ci.

[00:17:08] **Dave Lane:** So we have automated tests a practice again, we've, we've had for years security checks, accessibility checks and all that feedback gets returned to the developer agent if things don't pass muster. So the agent gets that context. Built a new plan for finishing the implementation, goes back through review and testing and all that, and ultimately gets merged into the main code line.

[00:17:34] **Dave Lane:** If all that passes and can fire off deployments,

[00:17:38] **John Berryman:** It and is the merging and deployment that's all automated to, at this point.

[00:17:43] **Dave Lane:** we, we do have it configurable per project. So there are somewhere like, okay, we can let it rip. There are some, you know, untested applications we bring in. Like they, they need a lot of love before we can really let it loose. But yeah. Jamie, you were about to talk, I think on that point.

[00:17:59] **Jami:** Yeah, I was [00:18:00] gonna say so one, before we leave the code review thing entirely, I wanna give of props to the team. They've been, they've actually been the ones driving that I kind of had an idea initially. And then Justin on our team has done, I think most of the implementation of that kind of stuff.

[00:18:15] **Jami:** And and Jack as well been working together to kind of, you know, revise it over time and make it into something that's, yeah, it went from being advisory all the way to now. Not only is it, you know, the only approver on most of our pull requests but it also will it also enforces some of, some of our conventions.

[00:18:33] **Jami:** So. One of the things we've really been pushing for lately is our our like rails and backend generally our testing has always been excellent. That's something that's always been part of our culture. Our front ends you know, a little less sometimes you know, things are moving fast there. We use Flutter, which has dart, which is a strongly typed language. So you already have kind of the type safety there a lot of times. So that, you know, catches a lot of the [00:19:00] bugs that you would catch with testing in like a, a Rails app with like interface mismatch kinds of things. But, you know, we wanted to improve our testing and so now it's at the point where if there's a pull request that it looks at and it's like, that should have tests, will tell you, reject it. Like, no, you gotta add tests.

[00:19:18] **John Berryman:** That's cool. And there's a separation of concerns too. It, because it sounds like the node, the agent that is responsible for actually building the code better be writing the test because

[00:19:30] **Jami:** Yes.

[00:19:31] **John Berryman:** bot is very specialized at judging the code, but not

[00:19:36] **Jami:** Right,

[00:19:36] **John Berryman:** stuff.

[00:19:37] **Jami:** right. Yeah. It doesn't fix anything. It just goes, this is good or bad. And so that I think was kind of the, the fundamental starting point for the factory, which is, you know, I can code locally with cloud code, get good results, have the fact have this code reviewer review it, you know, even use the GitHub CLI to say, okay, Claude, get the feedback off of here and address it.

[00:19:57] **Jami:** You know? It's like, okay, let's encode [00:20:00] that into a factory now. And so. To Dave's point, you know, the, this is, this is in its early days. So I've spent a lot of time with it because we call our factory scarif, which we can go into why that name for historical reasons in a minute if we want.

[00:20:15] **Jami:** But it has essentially built itself after just a little bit of bootstrapping locally, you know, to get to the point where it, it has the, you know, this worker agent and a way to, you know, do just basic stuff going through the pipeline and then, you know, built itself up from there. Now it, it still requires someone to specify things.

[00:20:37] **Jami:** So my, my typical workflow is. You know, Claude code and I have a conversation about what our priorities should be. You know, I have this idea, what do you think? Or go look at all of the, you know, stages that have run in the past couple of days and see what you think. What could be more efficient, what could be better, what are we missing, you know, all that kind of stuff. produce a plan from that and [00:21:00] then use, you know, break that into stories. Like, all right, now break this down into, you know, discreet stories. Which by the way, I'm getting some kind of warning about my browser storage being low. So if I freeze or something, I apologize here in a minute, but I don't know.

[00:21:14] **Jami:** I have space free on my hard drives. I don't know what that's about. Anyway, we'll see, see what's about to happen in 80 megabytes. But get a plan, break it into stories, you know, put it into Jira and then queue up all of those stories into scarf and then scarfs gonna run them through. And kind of to Dave's point. It's gonna start with nowadays it actually starts with a planning stage. So it's gonna take the ticket, break it into its own plan, make sure it understands generally how it's gonna implement things. You know, it's looking at the code what its acceptance criteria are, that sort of thing. Feed that forward into an implement step and it's gonna implement. and then separately, you know, it's gonna do a code review which is very closely based on that initial code review agent. And then from [00:22:00] there it's going to actually separately evaluate the review, go, okay, based on this, these findings, here was our initial plan with acceptance criteria. know, do we need, is this good do we need to go back and revise it? And so one of the, one of the important things about this is it's not an acyclic graph. So there are some, you know, there's like a cycle counter, so it's like, all right, once you get to like five cycles, probably need a human to look at this. But so we'll go back and do it again and come through, you know, all those stages, implement review, and then evaluate again.

[00:22:31] **Jami:** Then once, once the evaluator signs off, then it goes into verify, which is basically make sure the CI checks pass. And from there there's kind of the, to Dave's point, the decision point of, you know, I run this thing, I, I don't have time to look at all this code it's generating. So I just let it go and if something's broken, we'll log more tasks to fix it. But I think the, we've had. A couple of teams use this a little bit. And you know, [00:23:00] they're not quite, so, you know, they're the ones, they have a thing they have to like go show their clients at the end, so they're not quite ready for the just, you know, fully autonomous things all the way to volatile that, you know, they haven't looked at yet kind of stuff. So there is a decision point there where it can, once it's verified, it can just wait for a human review, you know, to say, okay, good merge. Versus I should do that on camera, I guess. Versus automatically merging and moving on to the next thing. So there, there is kind of a, you know, nod to the, the developer sensibilities as we're kind of moving up the automation chain here. The, what I will say is code review is something that Claude is, is very good at. And especially in a context like this, where if it needs to, it can kind of run the app and, you know, those sorts of things. It can, there's a test suite that it can run, you know, all of that. And we can get into this.

[00:23:55] **Jami:** I, I forget what the original question was, so I apologize for rambling. But the design, [00:24:00] design review and implementation has been kind of an interesting challenge. 

[00:24:03] **John Berryman:** The big the big question that I really wanted to make sure we had, drawn on the board behind me is here is how the whole system works. And let me see if I've got this straight. and you can correct me if I don't. So it Scarif is one unified system that has different skill sets. and I'm gonna get a little bit of this wrong, but if I get it like blatantly wrong, let's jump in. We'll edit it out. at the start is the ideation process. This is where, and I'm interested in where humans touch that's part of this too. Ideation. My client has a concern. I'm like a product engineer, like hybrid right now. And so I say okay I know it's feasible with technology. I'm gonna converse with this with an maybe with scarf. Does, is scarf helping with the ideation? Is

[00:24:54] **Jami:** Not yet. I think that's, that's probably gonna be in the long-term plan. But it's, yeah, it's not, [00:25:00] it's not doing that just yet. It's still after the ideation phase. Yeah.

[00:25:05] **John Berryman:** might be interesting to see if you when, if I was to come in and ideate, I bet the plan I came up with would have a very different flavor from like in the engineer sitting next to me. So that might

[00:25:15] **Jami:** Right.

[00:25:15] **John Berryman:** interesting

[00:25:16] **Jami:** Yep, for sure.

[00:25:16] **John Berryman:** do that and then tell me about it. 'cause that's cool.

[00:25:18] **John Berryman:** But anyway ideation happens. The engineer gets a plan that he or she deems sufficiently rich. And that is the input. And I think the input like the, you're using infrastructure that you already have working like Jira is kinda like the holding place for this. where Scare F is okay I see a new task.

[00:25:36] **John Berryman:** Or probably an engineer says, Hey. Scarf, get to work, and then scarf goes to a planning phase on its own, which, and it's clawed code but it goes to a planning phase. It builds it out according to certain foundational opinions that you guys have started with. Let's definitely touch into

[00:25:52] **Jami:** Yep.

[00:25:53] **John Berryman:** And once it feels like it's done, it goes to a review stage, which is actually that's fairly dark for [00:26:00] you guys. Dark factory. You don't have humans looking at lines of code. So I wanna get in a little bit. I wanna get into like how we're confident that blah, blah, blah. All things that we should be confident about. But it's apparently pretty good. it says yes, then it goes on to emerging deployment, which can be automated, depends. And if it's bad, it kicks it back to the previous step. Have I missed any, like big, obvious things I.

[00:26:22] **Jami:** I think you got it. I mean, the, the only thing to say about the architecture is it's, you know, the scarf itself, kind of the, there's a backend to it, which is, you know, living in the cloud rails app running in AWS, and then there's. Kind of similar to GitHub actions in a way. There's worker notes, you know, that have there's basically a harness around cloud code to, you know, claim work from the system and work at, you know, report completion, that sort of thing. yeah, and, and the choice of keeping things tied to Jira was a deliberate one, just because that [00:27:00] currently is how our human engineers work, you know, and how clients expect to see progress in the system. Is Jira tickets moving? And so the idea is, you know, maybe not every ticket is suitable for scarf to work on. You know, for example, one that has a lot of configuration to it, you know, it's like, okay, well someone besides scarf is gonna have to go click around in Google Cloud console to get. OAuth set up, you know, that sort of thing.

[00:27:29] **John Berryman:** Yeah.

[00:27:30] **Jami:** And so if those are both in the same system, we can track all of the work together, you know, it all can kind of move together.

[00:27:36] **Jami:** We have scarf will dump things out into our, you know essentially what a master our internal review column. So that's saying, you know, someone internally needs to look at this. So normally for our human process, a developer implements something and then we want someone other than them to go look at it and make sure, okay, based on this story, this is what I see deployed [00:28:00] good or not. And then, then it goes to a client, you know, after that it's okay. Now the client needs to go, all right, go look at volatile you know, make sure that this is what you meant. This is what we thought you meant, you know that sort of thing. So there's still, you know, we haven't automated the, the full lifecycle yet for a, a client project.

[00:28:18] **Jami:** There's still like. We still need eyes on it. It's just in a different way. It's like a, a verification of, you know, the output in a way. Like, did this,

[00:28:28] **Dave Lane:** I think your,

[00:28:29] **Jami:** what we thought it would?

[00:28:30] **Dave Lane:** your, your mention of the design review I, I think is worth revisiting too because like functionally you know, we can get well tested features out of what we've got and they work, but as a user you're like, oh my God. Like nothing is styled in this section for some reason. And you know, so there are,

[00:28:51] **Jami:** same as everything else.

[00:28:52] **Dave Lane:** yeah.

[00:28:53] **Dave Lane:** Yeah. So there, you know, there is a lot of that we have to deal with too. Yeah. And I, I think a key part of this is just [00:29:00] we've. A part of the reason that we have integrated with the tool chain we already had is, you know, our mentality around what the factory is doing is it's like a teammate. It is not as good as a human developer.

[00:29:16] **Dave Lane:** It, again, it can't go get the context that people can get as easily. It can't you know lean on the memory it has. I feel like memory in general is, is still a,

[00:29:26] **John Berryman:** Yeah,

[00:29:26] **Dave Lane:** know, a work in progress. Yeah. But in general, like it, it's like having an intern or a junior developer where you can offload some set of tasks and then you probably still want that senior person with experience and knowledge to, to go give it a real look and make sure things are good.

[00:29:43] **Dave Lane:** Yeah.

[00:29:43] **John Berryman:** Absolutely. I love that framing too. That's one thing that's come up a lot for me in building AI products with my clients is what is the intuition that you can have about this thing? And the best intuition I can communicate is to intentionally anthropomorphize the freaking thing to say, it's like our nice [00:30:00] AI intern really smart, forgetful. But that's implies exactly what you're talking about. What would a person on their first day of the job to have in front of them so that they can reasonably do their jobs. So tools should they have? and this poor fellow, he's gonna wake up tomorrow and he's not gonna remember anything so we won't. get into memory later if you'd like to. I think that's also a fascinating topic in a place where, until Mil Jovi Jovovich released her repo

[00:30:29] **Jami:** Yeah, I saw that that was released. I haven't had a chance to look at it yet. That's, that'll be interesting.

[00:30:34] **John Berryman:** I don't know what that is,

[00:30:35] **Jami:** Yeah.

[00:30:36] **John Berryman:** but it's not real. That's personal opinion. all, all so let's back to factors.

[00:30:42] **John Berryman:** Let's dig into this a little bit. when implementing this thing, so I know that the nodes are basically claw code, but are you programming the knowledge of all these things as skills? Are these all like skills or [00:31:00] how are you encoding each one of these steps into something that works?

[00:31:05] **Jami:** Yeah. So okay. There's probably like three moving parts here to talk about. so one kind of to get back to you, you know, treating it like a teammate and, and using the tools that our team uses. We actually have a. Twin Sun Cloud code plugin that we use internally which has, you know, a bunch of skills and agents around you know, development debugging, reviewing, you know, those sorts of things.

[00:31:33] **Jami:** So the cloud co, the worker notes have have that installed. So they have all of those available. And you see it leaning on those sometimes. And then the second part of that is kind of related but there's, in, in that plugin we actually have a kind of a, a setup task for repo where it's like, you wanna set up this task to use, use the plugin well to use ai well and what it does is it [00:32:00] will add. These AI rule sets that we developed. The impetus for this was the Flutter team actually released something similar to this, which became a seed where they, you know, it's just a, a long markdown file of, know, if you're using an AI agent with Flutter, you know, here's like all of the best practices to tell it, to have it in context, you know? And so I took that and then was like, okay, well we don't do flutter exactly the same way everyone else does. So, hey, Claude, look at some of, you know, look at our base apps, look at our, you know, some of our recent work and come up with, you know, use this as the base and then add like a twin sun specific section at the bottom that's like, okay, now. There are the general rules. Now here are the specifics of how we like to do things, you know? So a good example is there's a very common pattern in flood development called Block for the Business Logic components. And we do it somewhat differently than [00:33:00] the more popular packages for out there, do it. You know, we don't, it's not super important to get into the details of that right now, but what's important is it is different. And so if you, you know, come into a project and know that we're doing block know that we're doing Twin Sunblock, you know, produces different results, then if you just said, Hey, Claude, do block. It's probably gonna pull a block package off of pub.dev and, you know, set that up and, and whatever, rather than just follow our existing pattern that's here. and so then okay, so we have that for Flutter. Okay, great. Now let's do one for Rails. You know do a little research find, you know, on both in our, our base app and you know, the, the internet at large for best practices and things like that come up.

[00:33:43] **Jami:** You know, here's the, here's the flutter one, make it like this, but for Rails, you know, make it like this, but for Node, make it like this. But for what's the other PHP, I guess Lable other one I did. so those are kind of the, the more common technologies that we use. And so then this cloud [00:34:00] code plugin has a setup task that it's like, okay, figure out which platforms we're using.

[00:34:05] **Jami:** Pull in the right rule sets, add them to the cloud.md. That way. We always have those. And so that, that kind of provides some of that baseline context for, you know, when you're implementing or planning or whatever, you should be looking at these files that tell you generally how to do things and then from there.

[00:34:26] **John Berryman:** Okay, so claw code, and you guys are stretching claw code more

[00:34:30] **Jami:** Yes.

[00:34:30] **John Berryman:** I have. I've been a cursor fanboy. And they're still good. I like them. But

[00:34:35] **Jami:** Yeah.

[00:34:35] **John Berryman:** claw code is got all the light right now. So claw code wakes up and it's already got these packages installed. Plugins I'm sorry installed.

[00:34:44] **John Berryman:** Let's say, describe certain types of agents, I guess certain types of did you say the word skills? Are you using

[00:34:50] **Jami:** So yeah, there, there are skills in that, in that plugin. And the, the third piece is the actual. Prompt, you know, that's in scarf. That scarf will build for [00:35:00] whatever various stage it's doing. And there's a little bit of variation depending on what technology you're using, you know, what MCPS are available, that sort of thing.

[00:35:07] **Jami:** But yeah, for Mo, most purposes, it's a roughly a static prompt.

[00:35:13] **John Berryman:** got it. So cloud code wakes up, whenever it receives the

[00:35:17] **Jami:** Mm-hmm.

[00:35:18] **John Berryman:** that's here's the plan, here's the thing you're do

[00:35:20] **Jami:** Yep,

[00:35:20] **John Berryman:** of the set, set up script is okay, I got it, but also, what kind of repo is this? And let's start just downloading documents, I guess about if you're doing rails, here's the rules of the road.

[00:35:31] **John Berryman:** If you're doing node, here's the rules of the road.

[00:35:33] **Jami:** yep.

[00:35:34] **John Berryman:** And I'm not familiar with BLC, but it's just is this like the programming paradigm where it's like you have an API layer service layer, a re repository layer, something like that. It's

[00:35:43] **Jami:** Yeah. Very, very similar to that. Just, you know, flutter specific jargon, basically.

[00:35:48] **John Berryman:** Okay. Okay. That's cool. And and by giving it these opinions you keep it on much easier confined rails, you know where it's going to go. [00:36:00] it gets, I presume it gets better results, 

[00:36:02] **Jami:** yeah, right. sure.

[00:36:04] **Dave Lane:** I will say one thing. That we benefit from on most of our projects is our base app templates. Like we do a lot of greenfield work, a lot of new projects. And those templates have been in the works for years and have one, you know, given us starting point implementations for a lot of things like organization and user management, access controls stripe payment integration, push notifications, like all kinds of crazy stuff, dashboards, reporting.

[00:36:35] **Dave Lane:** And the side effect of having that as your starting point is Claude has tons of good examples for design design patterns the architecture we use, the infrastructure we deploy. You know, so that base template is just. Loads, dozens and dozens of feature examples. So when it goes to implement a new service class, it's looking at what are the [00:37:00] service classes already in this project and it follows our convention.

[00:37:04] **Dave Lane:** It's just kind of organically from that alone, which we do see a much better result from that just inherent context of what is in the app already. Then we'd get from just a brand new app that hasn't had that benefit of all those learnings over the years.

[00:37:19] **John Berryman:** That's huge. That makes a lot of sense. So effectively you get the one two punch. You have the instructions that say here's what you should do, but also to like harken back to prompt engineering when it was thing. You've got the few shot examples and the few shot examples is your whole repo.

[00:37:34] **John Berryman:** You've got all these

[00:37:35] **Jami:** Right.

[00:37:35] **John Berryman:** about what I mean when I say do this exact thing and that I'm sure that helps it stay on the rails much better. Here's a question that I've been wondering about in my own work developing prototypes and stuff. It's tempting just to say, Hey, build the product, build the thing.

[00:37:51] **John Berryman:** And I'll have a little bit too much of just like my user, my product hat on, how would a user use this? And I think about like an interface. And [00:38:00] then I get into a situation where I like hem myself in and I've built something that technically satisfies the user interface, but the. the backend code, the server code is garbage. I've obviously learned to be a little more deliberate about no, we want to have an API layer and here's a reasonable interface. If I can define that. Then the other stuff plugs into it. Here's a service layer. It controls the business logic itself. I don't want, I want the database to be pluggable. So like I might have a repository labor that layer that, that you can just replace this thing and you get, a different database or different data model even. But I have to be very intentional about that in the work that I've done lately. Maybe it's because I'm not using like a good, skill that says, here's what you should do and here's like a good example. But when your developers are working through these things, how much guidance are they providing scarf about the less visible. things that, that they're working on and that are important to extensibility [00:39:00] and modularity and stuff like that.

[00:39:01] **Dave Lane:** I think part of it comes down to comfort level with the project and, and just this new class of tooling too. So one project I know recently Jamie asked the team first. Task level specification on everything in, in the product we were gonna build. It was a small fixed price effort. And he ran it all through scara.

[00:39:23] **Dave Lane:** And going back to that configurability, the team needed to PR review that because it was the entire application. And so a lot of their time, you know, went to, you know, does this match what we expected to build. And it was kind of funny, the first pass of this the team came back and said, Hey, we're rejecting most of the PRS scarf made because it did what we specified and we specified the wrong thing.

[00:39:50] **Dave Lane:** And so we, we do have a lot of learning around that of like, how important is that and what is the cost of iterating on it? Things like that. And I, I think like [00:40:00] the realization we keep coming to, as we've iterated on these ideas and as we've prototype is. Just how you know, cheap code is in this new paradigm where you know, on on scarf itself.

[00:40:15] **Dave Lane:** Jamie, I, I think has a, a fantastic ability and discerning eye for like, looking at a system and understanding it or designing a system. And I don't have that. I have the, like, I'm gonna try a bunch of crazy ideas. And so our initial attempt at a factory was, I built this, to your point, really cool ui, it doesn't really work.

[00:40:39] **Dave Lane:** What, what might you learn from that? And so in extreme programming, you know, there's this notion of tracer bullets where maybe you're firing a machine gun in the dark, you can't see where you're shooting. So tracer bullets light up and you see kind of the direction of things. And I think, I like to pretend at least that prototyping and iterating on that was valuable to Jamie and he's like, ah, I actually see where we should [00:41:00] go.

[00:41:00] **Dave Lane:** Because he, he definitely has a keen eye for that and, and built the right thing. But I think that's something in general, across all of our projects where we're saying, you know, for a lot of these, especially in tech stacks, we're not familiar with or not using a lot we do still have to have that kind of trace or mentality of, we're probably gonna have to take a few hits at this.

[00:41:20] **Dave Lane:** But I think the thing you know, LLMs afford us is experiments are cheap and easy now, and we can do more and do it quickly. So it's not even necessarily the, the end goal is not, oh, we're just going to complete stuff automatically and, and never look at it. It's more we're going to stretch time and budgets more by increasing what we can accomplish in the same amount of time or with the same amount of money.

[00:41:45] **Dave Lane:** So we're still. Kind of working through that on a lot of projects.

[00:41:48] **John Berryman:** Very interesting stuff. Ah, there, there was something that, that I was going to say to you, and now all I can think about is I can't think about the thing I was trying to say.

[00:41:59] **Jami:** Think [00:42:00] about anything else? yeah, well that, that initial, yeah, I think your prototyping was really useful, Dave. Because I think while you

[00:42:08] **Dave Lane:** Thanks for telling me that.

[00:42:09] **Jami:** on I made a I. A another Discord bot. 'cause why not Discord bots, but it's kind of like, okay, are we ready to be like truly self-modifying yet kind of thing.

[00:42:19] **Jami:** And so it was a discord bot that, you know, I would chat to it and we could have a conversation, you know, going back and forth and then it could make a pull request, whatever, improve it, let's have more conversations, all that. So that was kind of a fun early, that was my first kind of foray into that while Dave was kind of building his factories and he kind of went top down you know, a little more generic. And so based on, you know, kind of his frustrations and my experience with this, you know, very narrowly tailored kind of discord bot, it's like, okay, maybe if we start smaller and build our way up, know, it'll be a little more successful than trying to come at it, you know, build the whole [00:43:00] thing all at once.

[00:43:00] **Dave Lane:** Yeah.

[00:43:01] **John Berryman:** a really cool so it's maybe Dave you had in mind like, okay, you, we've got the, it's a cyclic graph. Graph and you just like we know we gotta build the code and we know we gotta review the code and we gotta deploy the code. And so you can build all these boxes, but if you keep them completely generic, then you're basically given the claw code enough rope to hang itself with.

[00:43:21] **John Berryman:** And what you guys found out by trying stuff, your XP tracer bullets is okay, obviously it's not good enough yet. But from patterns that you guys had already seen, it's if you keep it on a, if you take the entire world of possibilities and narrow it down to just a much smaller space, then it's okay it's less likely to be creative

[00:43:42] **Dave Lane:** Yeah.

[00:43:42] **John Berryman:** the wrong way.

[00:43:43] **Dave Lane:** And that is precisely like, I think a core lesson. I learned from seeing Jamie's implementation versus, you know, all my iterations because I was doing a dag directed a cyclic graph. Then I had to introduce Cycle because it wasn't doing a great job. And you know, [00:44:00] Jamie's approach was, I don't need all that.

[00:44:01] **Dave Lane:** Like, our workflow is very straightforward. Here are the steps. Yeah, we've got conditional stuff for languages or frameworks. But he was like, you're, you're just, yeah. Very much giving it too much rope. So I started with and wanted iteration a planning step where, you know, it was a YAML based configuration and Claude would do the planning step, which would generate YAML for execution.

[00:44:24] **Dave Lane:** And it always did a worse job than the standard execution steps Tammy had. And so I, I eventually gave up on that one, but, it's very much he, he saw the field and refined it down to what we really needed. And that opinionated approach definitely has made it easier, I think, to, to make real progress on getting this thing running. 

[00:44:48] **John Berryman:** Maybe just take a pause for a second. I've got plenty of things that I want to ask, but I wanna make sure you guys are the ones building thing, what's working and, the pain points too. Top of [00:45:00] mind for you guys that it's gonna be important for us to nail in this conversation?

[00:45:04] **Dave Lane:** Well, if you wanna go, I, I have something too, but.

[00:45:07] **Jami:** was gonna say pain point wise, the design review thing is we should touch on, 'cause I think that's probably a big pain point that a lot of people feel, with this stuff is, you know, Claude doesn't see the way we see. Right? If you give it a picture of your design that looks great and its implementation that looks. Kind of like what, kind of like what we put in, you know? It, it, sometimes it can pick out what was wrong, maybe, or some of it, you know, it doesn't, it doesn't do a great job if it's looking at this like large image, especially just static images, you know, whatever.

[00:45:47] **John Berryman:** Interesting.

[00:45:48] **Jami:** so that, that design, you know, but that's very important for us because, you know, our product development process, you know, a client comes in, they work with our designer, [00:46:00] they spend a lot of time, you know, working with her refining, like, what should this look like visually?

[00:46:05] **Jami:** How should it feel? How should it work? Those sorts of things. We can't have claw just spit out, you know, something that's like, nah. And be like, ah, this is good, right? This is what you want. So that, that was kind of an interesting, like almost research project in terms of like, okay, know. People, everyone's trying to do this.

[00:46:23] **Jami:** Like, what are, what can we do here? You know, that sort of thing. And so it's more time consuming and results in more cycles. But we get a much better result with you know, this design review stage we've got now, which it's kind of like two pieces to it. There's one, there's kind of like the, the code up kind of piece that's going, okay, let me pull down all of like the design tokens from Figma and Zeppelin, you know, so we know, okay, what colors are we supposed to be using?

[00:46:54] **Jami:** You know, what's the border radius supposed to be? What is the spacing supposed to be? You know, all that stuff. [00:47:00] And then go look at the code. You know, like in our tailwind configuration, make sure we've, that matches the designs. You know, look at start running it. Use playwright to pull out like the computed CSS on elements and make sure those are matching, you know, we're using. The design tokens in the right places, all that kind of stuff. And then the other side is kind of like a visual review, but instead of going, okay, compare this image to that image, it's like, okay, you know, look at, look at the implementation of a screen, divide it into like regions that you can compare independently.

[00:47:35] **Jami:** And then within those regions, divide it into components and then start looking at, okay, here's the components and how do they match up? You know, have we used the right ones? Have we put them in other places? That sort of thing. And it's still not a hundred percent perfect. I don't wanna give that impression, but it is a much better result at the end of that than just a, you know, doing, doing nothing certainly.

[00:47:56] **Jami:** Or even just doing like, you know, screenshot to design kind [00:48:00] of one-to-one comparison.

[00:48:01] **John Berryman:** So very much. Right now we're talking about just the graphical design of things, 

[00:48:07] **Jami:** mm-hmm.

[00:48:08] **John Berryman:** pain

[00:48:08] **Jami:** Yep.

[00:48:09] **John Berryman:** because of the guard rails. You put it on the, like code design, all that stuff that's doing pretty well.

[00:48:13] **Jami:** Yeah.

[00:48:14] **John Berryman:** but when you're looking at the design. And the cloud code doesn't see the way humans see when you break it down into like pieces.

[00:48:24] **John Berryman:** Do you, is that still at least visual? Do you say take a screenshot of these three components on the screen and compare it with the designs? 

[00:48:33] **Jami:** Yeah, it's,

[00:48:34] **John Berryman:** making it more accurate? That seems like a really challenging problem.

[00:48:37] **Jami:** yeah, I mean, ultimately it's kind of, you know, to go back to your prompt engineering, it's like a prompt engineering thing. There's some scripts for how to like, pull out, you know, design tokens and things. But largely it's just a big prompt that's like, do these two things go, you know, look at. The design tokens from Figma and Zeppelin. Compare them to the code, make sure, [00:49:00] you know, compare them to the computed CSS, all of that kind of stuff. And then visually doing these breakdowns. And it is still, you know, it's it's running the application. You know, that in itself is kind of an interesting pain point that had to be solved.

[00:49:14] **Jami:** 'Cause it doesn't do a great job of cleaning up after itself all the times. It's like, okay, now a pre warming step where the, the scaffolding, a round clock code scans for a block of like 10 ports that are open together, you know, above 3000. Then we inject that into the prop. Like, okay, run the app when you do it, use, you know, ports 30 10 through 30 20 kind of thing. You can pick whatever you want in there. Just, 'cause I try to, you know, we've got like multiple nodes running on the same machine kind of stuff.

[00:49:44] **John Berryman:** That's a very,

[00:49:46] **Jami:** they conflict and they'll kill each other sometimes. Like Claude is, can be very persistent about it. So like I've, I've seen them kill each other's cloud processes to try to like free up ports so they can run things, like stop [00:50:00] doing that.

[00:50:00] **John Berryman:** wild.

[00:50:02] **Jami:** But yeah,

[00:50:03] **John Berryman:** But yeah, obviously that would be a, like this design looks nothing like the design that you asked me

[00:50:08] **Jami:** it's just like this error page of like an old Rails app that was running, you know? But now the temp directory has been cleaned up, you know, it's like, it's not, it doesn't look anything like it, of course. 

[00:50:19] **John Berryman:** Is that okay?

[00:50:19] **Jami:** but yeah, you know, when it runs things correctly, it will go in, you know, take a screenshot, divide it up you know, even section that into images and compare like, okay, did we get this button right?

[00:50:30] **Jami:** You know, did we get this this card? Right. You know, that kind of stuff.

[00:50:35] **Dave Lane:** I do think, like just in prompting to say, you know, check the computed styles and the rendered dom for this page and ensure it matches your expectations and is consistent with the rest of the design, like that does a lot in itself. But yeah, Jamie's taken it very far on the, the visual analysis aspect too.

[00:50:58] **Dave Lane:** But [00:51:00] that alone, just check the structure. Checkout actually rendered oftentimes cleans up a lot of obvious visual defects.

[00:51:07] **Jami:** I think, I think this is one of those things where it's like, you know, Pareto principle kind of things. Like you get 80% of the result with the easy prompt, and then if you get to do a lot of hard stuff to kind of get, you know, like the next nine kind of thing, you know?

[00:51:23] **Dave Lane:** A random cloud update on Tuesday will replace it all, so,

[00:51:27] **Jami:** Yeah.

[00:51:27] **Dave Lane:** yeah.

[00:51:28] **Jami:** Yeah.

[00:51:28] **John Berryman:** Yeah,

[00:51:29] **Jami:** come out with their visual design implementer, you know, in a couple weeks and just make it all. Yeah.

[00:51:37] **John Berryman:** yeah, if you want it sooner, then I better publish this sooner so that

[00:51:40] **Jami:** Right.

[00:51:41] **John Berryman:** agents listening to podcast and be like, oh, that's a good idea. We'll just

[00:51:44] **Jami:** Yeah. Yeah.

[00:51:46] **Dave Lane:** Yeah. Well, I, I think we, I, we don't have to hit it right now, but I have thought you know, we're talking a lot about the technical implementation of a factory, but I'm sure in your line of work, John you probably hit this too. There's also the adoption aspect [00:52:00] and the comfort level people have.

[00:52:01] **Dave Lane:** Right. Which has been interesting in general with AI for us as a development agency. But, you know, going into like the disciplined culture aspect of you know, we needed a discipline across the organization to, to give us the ability to do what we've done so far. And part of that is in hiring and having the team.

[00:52:22] **Dave Lane:** We have most of our team they're second career developers. They've already had. A significant change in, in their profession. Bartenders, musicians, teachers, a law librarian. Again, Jamie had a PhD in biochemistry, you know a very diverse group of people. But they all came from different fields and have already made the jump once into technology.

[00:52:46] **Dave Lane:** You know, they learn programming, they learn to do it the traditional way, and then all of a sudden, you know, a couple years in AI comes out and can spit out, you know, thousands of lines of code in, in the time they can do a [00:53:00] dozen, so I think having those people on board has you know, been, been a big deal for us.

[00:53:05] **Dave Lane:** They're open and receptive to, you know, a changing field because they've been through it. They're willing to adapt and they're willing to try and see like, is there something here that can make this work well for us? So I've personally known a lot of first career developers. You know, several friends of mine even that feel completely differently about all this technology and have had a different result.

[00:53:27] **Dave Lane:** And, you know, we like Jamie, and I think of it as they're too focused on watching the sausage get made. And I've been compelled, you know, as, you know, an experienced developer too, to say, wait a minute, Claude, stop. Don't do that. Don't do that. Do it this other way. But oftentimes when you let it go and just let it run for a bit it, it can reassess and correct those problems eventually without you touching it at all.

[00:53:51] **Dave Lane:** And especially, you know, with the workflow we have with PR reviewer, design review, CI feedback you know, that, that, that's been a big [00:54:00] differentiator too. But just being open and trying new things is a big deal for the team. You know that's really driven adoption. Mm-hmm.

[00:54:08] **John Berryman:** Very interesting. So the, this, it's the second time I've heard this spoken in the last two days that for some reason the people that come from unusual backgrounds to be more receptive and even potentially capable. And that, that's interesting. I guess may maybe it's, it is exactly what you said.

[00:54:27] **John Berryman:** And I'm one of those myself. Just the fact that there has been a big leap in the past to be like, okay, this is just another big leap. done one of those before. Very interesting. As, as far. So much to, to talk about on this one and figure out where you want. You wanna take this conversation, Dave and Jamie, but the morale of not seeing code and just everything changing.

[00:54:51] **John Berryman:** Who moved my cheese, but it's a really big block of cheese this time. What roles are on the chopping block versus what roles are emerging? [00:55:00] Especially in the olden days we had dedicated engineers, dedicated product managers, which didn't know much about code. And sometimes struggle to get people listen to their good ideas. Project managers that are like wiring stuff together. That might have a very different role at this point. People, managers and even up in the higher level. Yeah. So where do you wanna take this conversation? 'cause I think this is, adopting the technology is very important.

[00:55:26] **Dave Lane:** I, I think like when, when we, you know, ask what roles are being replaced on the chopping block? You know, I, I still think of it at a task level. I think where you know, we've seen some success so far in there is a third, a certain threshold of task or a type of task where you don't have to write that code.

[00:55:47] **Dave Lane:** And. I think we kind of benefit again, in, in how we've selected the people that are on our team. That's the expectation from day one is not, we don't care, like we care about code [00:56:00] quality, but we don't necessarily care about the code over the outcome or the business impact. And

[00:56:07] **John Berryman:** Yeah.

[00:56:08] **Dave Lane:** unfortunately there, I think there is definitely a morale hit for a lot of people where they enjoy programming.

[00:56:14] **Dave Lane:** It, it turns out developers like to develop. But I, I've also had to take that development has kind of taken a, a narrower and narrower definition than I think it should have. I mean, especially if you look at like the Agile manifesto it's about communication and collaboration. It's about achieving those outcomes.

[00:56:34] **Dave Lane:** You know, it's. Very much not focused on, we write great code, it is quality code. Most of our time is code. It's really what are we trying to achieve and what tooling helps us achieve that. And so I feel generally like the folks we have have accepted that if not embraced it, I think most have embraced it.

[00:56:54] **Dave Lane:** And I think it's really almost empowering a lot of time when you can say, I've [00:57:00] got this really hairy task I need to go implement and. I'm just gonna be typing for three hours. If you look at it at a high level, like that's not a very exciting thing. You want the accomplishment at the end. But the task of typing out the syntax is, is really honestly I think one of the least valuable things our team does.

[00:57:17] **Dave Lane:** They, they are great thinkers. They look at projects globally. They, they try to think strategically about, you know, what's really the right thing to do for my client here?

[00:57:28] **Dave Lane:** So I think we do benefit uniquely in the way we've hired with that.

[00:57:32] **John Berryman:** Hire people that are focused on outcomes and that, when you say it out loud, it seems obvious, but but yeah, but I like, yeah. I'm a developer too. I've done down like the bite level coding in the past,

[00:57:45] **Dave Lane:** Yeah.

[00:57:45] **John Berryman:** stuff Honest puzzle. There is,

[00:57:48] **Dave Lane:** I, yeah, I mean, and that's the thing, like I don't think people, I, I think there will always be a place for programming and you know, people knit sweaters. It, it's not the cheapest or most efficient way to [00:58:00] get a sweater, but it's still really cool. But I think there's also just meta programming around, you know, these factories.

[00:58:06] **Dave Lane:** Like yeah, you can you know, bootstrap them like Jamie has described, and, and they can build a lot themselves. But there are some decisions where you probably do want to get your hands dirty and make sure things are exacting and specific. And I think that will just always exist. So I think it's programming on a different level that, you know, that will continue for quite some time.

[00:58:26] **John Berryman:** And there's always this weird side market for Artisanally created code, right?

[00:58:31] **Dave Lane:** Yeah, free range, organic software. Let's do it.

[00:58:34] **John Berryman:** Touch the keyboard with my hands. Have you guys got the problem that I've got right now where it's you used to rub off the s and the D and the space bar and the like shift and now I'm like rubbing off the option character. Why? I just push it down and start yelling at my key, my computer.

[00:58:48] **Dave Lane:** My, my bigger problem is I open a terminal window and I start typing in English. I'm like, I'm in quad. Right? 

[00:58:59] **John Berryman:** [00:59:00] Okay. So I don't wanna leave this topic too quickly 'cause there's another aspect of it and let's aim to wrap up the main conversation here in just a few minutes and then we'll close down recording. So one, before we leave this topic, one thing that I wanted to make sure we get to, that's gonna be especially important to all the companies out there that are trying to figure out how to navigate this is. Not just how you implement this culturally, but also like technologically, you came from a starting point. technology is moving. I it's moving so fast that you can't like, like aim for where the puck is right now. You've gotta aim ahead, you start from a particular starting point. How would you recommend that a company that has an established development practice incrementally move to something that's like a factory? 

[00:59:52] **Jami:** I think it's, yeah, we'll, we'll hit on some of the same themes. You know, what allowed us to do it is the, do [01:00:00] you have the solid process, discipline in place? You know, so if you've got a good development process, that works for your human developers. You know, and you're, you start with automating the pieces.

[01:00:14] **Jami:** You know, you can, so you start with automated code reviews. Once you're confident in those, you know, now you don't need to do the human reviews or not in every case, you know, and then you start moving up the chain. You know, you've got if you're, if you're automated, testing is going well, you know, you can be confident in the code, your shipping. and so. You know, then, all right, now we can, maybe we can take our hands back a little bit. Let Claude Claude go loose. You know, start automating the easy tasks. You know, okay, we got good results from those. Now we can move a little harder. You know, we need to, design review piece is gonna be a, you know, that's gonna be a pain point. So those UI tasks that are, [01:01:00] you know, build out a whole screen exactly to these visual requirements you know, that'll be a little bit of challenge. That's probably the hurdle hurdle to get over to really start making it able to do more. You know, 'cause most tasks involve some level of UI work. 

[01:01:18] **Dave Lane:** I think another thing,

[01:01:19] **Jami:** what I see as, yeah, that, that process discipline, and then using that to allow you to start automating pieces of it confidently.

[01:01:27] **Dave Lane:** like one thing I've been thinking a lot about lately, John, is one of the first things we discussed when we first met. I don't know if you remember this, but I was kind of whining about how no one does evals and just kind of like throws. Random prompts at the wall and assumes it's gonna work in production.

[01:01:43] **Dave Lane:** And, and you told me no one wants to eat their vegetables. And,

[01:01:48] **John Berryman:** Yeah, I

[01:01:48] **John Berryman:** Phrase.

[01:01:49] **Dave Lane:** and I, I think that's a wonderful description of software development in general. Like, no one wants to eat their vegetables. Like, are you doing, you know, security checks that you [01:02:00] should be doing every night, or are you looking at accessibility?

[01:02:03] **Dave Lane:** And I think one quick win for people that are critical of introducing these tools to like their core tasks could be saying, Hey, you know you need to make sure you're doing security scans every night. And depend, abott is kind of annoying. Claude is way better at handling these minor upgrades for you.

[01:02:22] **Dave Lane:** And you can have a nice PR in the morning that says, Hey, this CVE came out. It's already addressed. Here you go. Test pass. This is work you wouldn't have done this quarter if you didn't have this. I think that could be a nice low barrier to entry too. Maybe not the, i, I guess the low hanging fruit that otherwise people just aren't going to worry about or prioritize.

[01:02:43] **Dave Lane:** Just take care of it and show like there is value here for a subset of tasks. And then it's easy to ask, well, okay, if it can do that, what else could it do for us?

[01:02:50] **John Berryman:** Interesting. So it is you guys are saying something similar, but it's like from a starting point, you have a bunch of tasks at your work that you [01:03:00] do and you need to start probably as like a priority queue of this one sucks for us, but it is doable.

[01:03:08] **Dave Lane:** Mm-hmm.

[01:03:09] **John Berryman:** And then, yeah, and then like when you have something that's drudgery, like doing upgrades that claw code is really good at, and no one really feels like doing and working out the little minor bugs that pop up, then you can just start, you know what I think about I there. When I was a young lad, I asked my financial advisor for I, I was like, I'm an entrepreneur. I've always been a wannabe. And he's you should read this book Michael Gerber's E-Myth. Have you ever heard of that?

[01:03:39] **Dave Lane:** Yeah. Richer king. Yeah.

[01:03:43] **John Berryman:** It's not really about startups, but it's about like franchise restaurants and it's I don't wanna own a McDonald's, but it's talking about the same thing you're talking about.

[01:03:52] **John Berryman:** It's it just came to me right now is the whole idea of that book is you go to your business, you lay out the [01:04:00] tasks at hand and you write like a binder for here's the employee binder. Here's what you do when you get in this task and we've completely out outlined a role.

[01:04:08] **John Berryman:** You fire yourself from that role and go do more important high utilization stuff ahead of that. So I.

[01:04:15] **Dave Lane:** Yeah.

[01:04:16] **John Berryman:** So weirdly, it's like running a franchise hamburger joint.

[01:04:20] **Dave Lane:** That, that does open up. One final thought I I've had that we haven't touched on at all, which is we're talking software factories, and I think that's definitely the sweet spot for LLMs right now. Like we, we are in the best field for, you know, automation with AI right now, I think. But there's a whole other class of factories people are doing.

[01:04:41] **Dave Lane:** I, I, I'm not a fan of this one. I saw someone making a book factory where they're just generating books. I'm like, I please don't. But but, but there are other use cases. So like even in our marketing I think Jamie had the idea of, you know, we have all this built up knowledge about all these projects, all these clients we've worked with, and we've never written [01:05:00] any of it down.

[01:05:00] **Dave Lane:** He's like, I'm just gonna task everyone with audio interviews. I have a list of questions. Talk about your project and he turned those into a case study and blog post drafts that are grounded in real knowledge about projects we otherwise wouldn't write about. We just wouldn't take the time. And so now we have a nice draft to start from where we're just going to tweak 'em a bit and make it, you know, sound like our language, our words because it, which is already closed 'cause it's translating from our audio.

[01:05:28] **Dave Lane:** But you know, it's essentially a mini factory for case studies and, and deep dives. So I think there's a lot of new opportunity out there for a lot of fields, but we just get the benefit of it's really good at software. So everyone's talking about that right now.

[01:05:44] **John Berryman:** Yeah. Yeah. Who knows what is going to happen. This is the part where we could talk about the dystopia utopia, but we promise not to get into that. I always gravitate towards the darker side. I. All let's close [01:06:00] it up, guys. Thank you guys so much for being on the first ever podcast of whatever I'm gonna call this. Thank you for being good conversational partners and teaching me and the five people that listen to this a lot about how to implement the factory pattern.

[01:06:17] **Dave Lane:** Well, I told my wife she has to listen, so it's gonna be at least six. So

[01:06:21] **John Berryman:** I'll make my wife listen too.

[01:06:23] **Dave Lane:** thank you so much, John. This has been fun.

[01:06:27] **Jami:** Yeah. Thanks for having us. It's, it was a lot of fun.

