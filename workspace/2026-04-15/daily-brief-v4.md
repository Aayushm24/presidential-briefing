# The agent knowledge moat is evaporating

Notion rebuilt their agent system five times.

The knowledge required to build production AI agents went from locked inside a few teams' heads to publicly accessible in the last 24 hours. Frameworks, case studies, post-training courses. The remaining differentiator isn't knowledge. It's how fast you iterate.

**Key takeaways:**
- Most teams can't even compare their agent ideas. A $500/month chatbot and a six-figure voice assistant both get called "agents" and ranked on the same spreadsheet. Categorize before you prioritize, or burn months on the wrong thing first.
- Notion's cofounder went on record: 5 rebuilds, 100+ tools, years of work. Budget for at least three rebuilds.
- A free RLHF course lowers post-training knowledge from "$400K hire" to "a few weeks of focused learning."
- Open source models match frontier performance for most production tasks. Default to open source, benchmark the rest.


### Most teams can't even compare their agent ideas

Hamza Farooq and Jaya Rajwani published a framework on Lenny's Newsletter that cuts to the core problem. They've had the same conversation "at least 30 times" with AI leaders.

Someone shows up with 5-10 agent initiatives on a roadmap. They try to prioritize using a standard impact-vs-effort matrix. It fails immediately.

The items aren't comparable.

A customer support chatbot built with n8n that costs $500/month is not the same category of project as a voice-enabled shopping assistant that requires dedicated ML engineering and generates six-figure annual LLM bills. Putting them on the same spreadsheet is, as the authors put it:

> "Comparing apples, oranges, and jet engines."

Their framework groups agent initiatives into **three tiers based on architectural complexity**. This determines everything: team composition, timeline, infrastructure, cost. They built it working with enterprise teams at Jack in the Box, Tripadvisor, and The Home Depot. These aren't theoretical categories. They emerged from watching real organizations try and fail to ship agents, then figuring out what the successful ones had in common.

The generic horizontal agents are getting commoditized fast. Microsoft's OpenClaw-style efforts, Google's Gemini integrations, Salesforce Agentforce. Domain-specific agents with real operational ownership in verticals like retail, finance, and healthcare are where defensible value gets built. But most teams don't even have the vocabulary to distinguish between these categories when staring at their own roadmap.

**Categorization must come before prioritization.** If you skip the step of asking "what type of agent is this actually proposing," your effort estimates will be off by 10x.


### Notion's five rebuilds: what production agents actually cost

Simon Last (Notion's cofounder) and Sarah Sachs (head of AI) went deep on the Latent Space podcast about shipping Custom Agents.

**5 rebuilds. 100+ tools. Years of work.**

Notion has been building AI features since before ChatGPT launched. They've shipped Q&A (2023), unified AI (2024), Meeting Notes (2025), and now Custom Agents as part of Notion 3.0. A decacorn valuation. A world-class team grinding on this problem for years.

They still rebuilt the agent system five times.

The reasons are instructive. No tool-calling standard existed. Context windows were too short. The agent harness architecture wasn't mature enough. These aren't exotic problems. They're the exact same walls every team building agents hits. The difference is that Notion is now talking openly about the specific decisions: evals, pricing, progressive tool disclosure, org design, the choice between MCP and CLIs.

The genuinely new part is their **"software factory" framing**. Notion is positioning itself not just as a productivity tool but as an agent-native system of record. Meeting notes become structured data capture for agents. Custom agents get scoped access to specific workspaces. The product becomes the platform.

> "We started building AI tooling before ChatGPT launched. Our first agent attempts failed because there was no tool-calling standard."
> — Simon Last, Notion cofounder

**Budget for multiple rebuilds.** If Notion needed five, you probably need at least three. The fact that they're sharing the specific lessons means other teams can potentially skip rebuilds two through four.


### Free RLHF course makes post-training accessible

A free course on RLHF (reinforcement learning from human feedback) launched with lectures covering the overview, instruction fine-tuning, reward models, RL math, and implementation.

Post-training, the process of taking a base model and aligning it to be actually useful, has been **one of the most gatekept areas of AI knowledge**. The people who understand it well are expensive to hire and in short supply. Most AI teams building agents rely entirely on API-served models and never touch post-training. That's fine for many use cases. But it means they're completely dependent on model providers for the behavior characteristics of their agents.

As open source models reach frontier performance, the ability to do your own post-training becomes a real competitive lever. Fine-tune behavior for your specific domain. Adjust the reward model to match your users' actual preferences. Reduce dependence on closed-model pricing.

A free, structured course lowers the barrier from "hire a $400K ML researcher" to "dedicate an engineer for a few weeks of focused learning."

Each of these stories independently makes it easier for a competent team to ship real agents. Together they represent something bigger: agent-building is maturing from a craft practiced by a small number of well-resourced teams into a discipline with frameworks, case studies, and training infrastructure anyone serious can access.

If your competitive advantage was "we figured out how to build agents and our competitors haven't," that advantage has a shorter shelf life than you think. The frameworks are published. The case studies are public. The training is free.

Notion rebuilt five times. The teams that treat their first architecture as precious will lose to teams that treat it as a draft.

---

### #2 Open source models have reached frontier levels

Lindy, the AI agent platform, shared a breakdown that crystallizes something important. For most production use cases, open source models now perform at or near frontier levels. And inference cost is their dominant expense, more than payroll.

Their framework: if an open source model gets you 90-95% of the capability at 30-50% of the cost, the math is obvious for most applications.

The nuance matters. "Most use cases" is doing real work in that sentence. For the hardest reasoning tasks, complex multi-step agent workflows, and cutting-edge code generation, closed frontier models still have an edge. But **the set of tasks where that edge actually matters keeps shrinking**.

Default to open source. Benchmark against closed models on your specific tasks. Only pay the premium when you can measure a meaningful difference that your users actually care about.

---

### #3 Security is becoming a token budget

Simon Willison highlighted a sharp framing from Drew Breunig about the UK AI Safety Institute's evaluation of Claude Mythos Preview's cybersecurity capabilities.

The key finding: **the more tokens you throw at security review, the more exploits the model finds**. There's no obvious plateau.

This reduces security to a brutally simple equation: to harden a system, you need to spend more tokens discovering exploits than attackers will spend exploiting them. Security becomes proof of work.

The second-order insight is more interesting. This makes open source libraries *more* valuable, not less. Tokens spent securing an open source library get amortized across every user. A company that vibe-codes a replacement to save integration time takes on the full cost of securing that code themselves.

> At a time when AI makes both attacking and defending cheaper, the shared defense economics of open source become a genuine strategic advantage.

This directly pushes back on the "vibe coding makes open source obsolete" narrative. It's easy to generate code. It's expensive to secure it. Open source pools the investment. If you're building anything touching sensitive data, your security budget is about to become a token budget.
