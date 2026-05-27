# Brainstorming — Tim Kellogg Interview

## 1. Shared Nothing Architecture Applied to Software Teams
- Distributed systems principle (partition, eliminate shared state) maps to AI-driven dev teams
- Keep modules small and independent → AI commits collide less → scales horizontally
- Monorepos become increasingly painful as AI-generated change volume grows
- Complexity scales ~N² with team/module size; staying small keeps it manageable

## 2. The 10% vs 90% Problem with Generic Agents
- Dropping in a generic agent (e.g. Microsoft Copilot) captures ~10% of potential value
- Remaining 90% requires encoding company-specific domain knowledge into the agent
- Agents must learn workflows over time — not just assist with individual tasks
- Business processes need to become codified in how the agent behaves

## 3. You Can't Just Sell an Agent
- SaaS companies treat agents as a new feature/SKU rather than a workflow transformation
- Real value comes from transforming the workflow, not layering an agent on top of it
- Parallel: giving someone a new tool doesn't help if they don't change how they work
- True AI adoption requires organization-wide participation in identifying automation opportunities

## 4. End-to-End Vertical Teams + AI
- AI agents are general purpose — why stop at engineering? Extend to QA, DevOps, sales, marketing
- Future org structure: vertical generalist teams own a product slice end-to-end; horizontal specialists (AI/domain experts) build the shared agent infrastructure
- Engineers evolve from "people who write code" → "people who build systems that build software"
- VPs/managers already think this way; individual engineers are experiencing burnout from the shift

## 5. The Future of SaaS
- IT shops building bespoke internal tools is accelerating (vs. buying SaaS)
- Lower-tier SaaS players will be displaced; 1–2 category leaders may survive
- Alternative path for SaaS: make your product extremely agent-accessible (open APIs, installable skills, agent-specific login/tracking) rather than bolting on an "AI feature"
- The internet may shift from human-facing destinations → machine-addressable APIs

## 6. AI Model Preferences & Enterprise Constraints
- Personal/team AI preferences are strong and growing (Claude vs. GPT vs. Gemini)
- Enterprises have IT-driven constraints: minimum supported tools, vendor lock-in concerns
- Selling an agent tied to one model creates downstream sales friction ("we're a Google shop")
- Better strategy: expose clean APIs and let customers bring their own model/harness

## 7. OpenStrix & Stateful Agent Design
- Tim's open-source stateful agent harness (comparable to OpenClaude/Codex)
- Not a coding agent — a minimal event-driven harness you plug skills into
- Event-oriented: only invokes LLM when real events occur (GitHub issues, Jira comments, etc.)
- Meta-agent: constantly brainstorms ways to improve its own use of the harness

## 8. Memory Management — Small Sliding Window vs. Compaction
- Long-running agents eventually exhaust context; you must have a strategy
- Compaction (infrequent, catastrophic) is risky: untested code path + large information loss + shapes all future behavior based on what survives
- Alternative: small fixed sliding window — always rebuild context from files/memory blocks
- Keeps memory management visible and testable; failures are obvious and immediately corrected
- Cheaper in tokens for long-running agents (avg context ~10–15K vs. 500K+)

## 9. Plain-Text Memory > Weight-Based Continual Learning
- Current stateful agents use files + memory blocks (key-value chunks in the system prompt) — all plain text
- "Learnable system prompt": memory blocks shape persona, guidelines, working style
- Files = data/knowledge; skills = hybrid of prompt representation + files
- Plain text is debuggable (read it, check Git history); weight-encoded memory is opaque
- Tim's prediction: plain-text memory will remain the dominant pattern for a long time

## 10. The Workflow Engineer Role
- Emerging job title: someone who understands agent systems AND deep domain expertise
- Can integrate agents into manufacturing, legal, sales — not just software
- Tacit/undocumented domain knowledge (e.g. Nitinol metallurgy) is AI's current hard boundary
- But domain experts + agents together can gradually encode that knowledge over time
