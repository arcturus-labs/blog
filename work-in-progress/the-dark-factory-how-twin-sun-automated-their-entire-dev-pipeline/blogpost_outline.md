# Blog Post Outline: The Dark Factory: How Twin Sun Automated Their Entire Dev Pipeline

**Source video:** `video_edits/2026.04.09–dave-lane-jami-couch-factories/`
**Guests:** Dave Lane (CEO) and Jami Couch (CTO), Twin Sun

## Title
The Dark Factory: How Twin Sun Automated Their Entire Dev Pipeline

## Vehicle

Practitioner story used as proof of two principles. Twin Sun's experience is the narrative spine; the principles are the payoff.

---

## Outline

- **Hook — the PR bot that approves 70% of pull requests autonomously**
  - Most teams have tried a "helpful AI reviewer" that gives advice — and then ignored it
  - Twin Sun's bot doesn't give advice; it either approves or sends the PR back to be reworked — no human in the loop for 7 in 10 PRs
  - This isn't an experiment; it's production. How did they get here?

- **What is a dark factory?**
  - A software development pipeline where agents handle the full cycle: requirements → code → tests → review → merge — with minimal human intervention
  - "Dark" = running without hands on the controls (borrowed from manufacturing)
  - Twin Sun calls theirs Scarif (Star Wars reference)
  - The goal isn't to eliminate developers — it's to "stretch time and budgets by increasing what you can accomplish in the same amount of time or with the same money" (Dave's framing)

- **Inside Scarif: the full pipeline**
  - Triggered by a prompt generated from a Jira ticket (a text template Scarif creates)
  - Agent picks up the task: writes code against the existing codebase
  - Code review agent reviews the PR — checks against rules, style, architecture
  - If it passes: auto-approved and queued for merge
  - If it fails: sent back to development automatically — the loop closes without a human
  - Keeping work tied to Jira is deliberate — makes work visible and legible to both humans and agents
  - The feedback loop matters as much as the generation step

- **Principle 1: Build YOUR factory, not a factory**
  - The temptation: build a general-purpose pipeline any team could use
  - Jami's key line: *"We don't have to build a factory that's so general purpose that anyone could use it. We just need one that builds things the way we want them to be built."*
  - What makes it opinionated:
    - **Rules**: started from Flutter's coding rules, fed them the actual codebase, asked the agent to adapt those rules to their style — now all generated code looks like their code
    - **Templates**: cookie-cutter scaffolding for the types of things they build (mobile apps, web apps) — the agent starts from structure, not a blank page
    - **Few-shot from the actual codebase**: agent pulls in samples from their existing repos as patterns — essentially automated few-shot prompting
  - The opinionated approach is what makes the output dependable enough to trust

- **Principle 2: Go gradually darker**
  - The mistake: designing the full factory, then flipping it on
  - The right path: introduce one component, develop it locally first, run it manually, build confidence in its behavior, then let it run dark — then add the next component
  - The PR reviewer's history is the model example:
    - Started as an optional advisory tool (just comments, no authority)
    - As they understood its behavior, they gave it more authority
    - *"It went from being advisory to..."* — the trust graduated over time
    - Now it autonomously routes 70% of PRs without a human
  - Dave's framing: even local dev work with Claude Code can be "promoted" into the factory once you're confident — you don't have to build the factory all at once
  - Side note on infrastructure limits: the factory sometimes doesn't clean up after itself; these rough edges are tolerable because they got there incrementally and know where the edges are

- **The human side: team adoption and changing roles**
  - Not everyone is thrilled when an AI starts reviewing their PRs
  - Twin Sun's advantage: they already had a team comfortable adapting (people who'd made prior career transitions were more open)
  - Key reframe for morale: when developers are focused on outcomes rather than just writing lines of code, morale stays high — you're building something bigger
  - Dave on the "what roles are being replaced?" question: the answer that keeps morale intact is outcomes, not tasks

- **The pattern beyond code**
  - The factory pattern isn't code-specific
  - Twin Sun's accumulated project knowledge is largely undocumented — Jami's idea: apply the factory to marketing, turning that institutional knowledge into content automatically
  - The underlying principle (document a human process, systematize it, automate it) is the same wherever you apply it
  - **Callout box** — meta example: this post itself was produced by a content factory. The goal isn't to generate AI slop — it's to systematically extract value from a long-form conversation: gleaning the morsels from the video, organizing them into a coherent structure, converting that structure into prose, and pushing it through to publishing and promotion. This post started as a 70-minute interview transcript and a set of editing notes. You're looking at the output. The factory works.

- **Takeaway / close**
  - The dark factory is achievable — but not as a big-bang project
  - Two things that make it work: constrain it to your team's actual patterns, and earn trust before removing the human
  - The teams who'll succeed are the ones who resist the urge to build everything and instead go one step at a time
