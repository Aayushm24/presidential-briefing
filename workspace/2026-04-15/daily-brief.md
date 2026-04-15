# Daily Brief — 2026-04-15

**Lead:** The next evolution of the Agents SDK

# The agent stack just got its concrete pour

Notion rebuilt their agent system five times before it worked.

That single detail tells you where the AI agent market actually is right now. Not in the "agents are coming" phase. Not in the demo phase. In the painful, expensive, production-hardening phase where the platforms that survive will define how software works for the next decade. Today, OpenAI shipped sandbox execution and long-running support in their Agents SDK, Adobe launched cross-app AI agents across its entire Creative Cloud suite, Notion's cofounder revealed the brutal engineering cost of making agents real, and a startup called Gitar raised $9 million to secure all the AI-generated code that agents are now producing. The pattern is unmistakable: **agent infrastructure is graduating from prototype to production, and it's happening across every layer of the stack simultaneously.**

**Key takeaways:**
- OpenAI's Agents SDK now supports native sandboxed execution and persistent, long-running agents, giving builders the primitives they've been hacking around for months
- Adobe's Firefly AI Assistant works across Photoshop, Premiere, Illustrator, Lightroom, and more, turning creative workflows into multi-app agent orchestration
- Notion rebuilt their custom agents four or five times, used 100+ tools, and still had to solve MCP vs CLI tradeoffs, setting an honest cost benchmark for anyone building agent products
- Gitar's $9M raise targets the security debt created by vibe-coded AI-generated code, a second-order market that only exists because agents are shipping real output
- Builders investing now in agentic architectures, multi-step, multi-tool, sandboxed execution, will have a structural advantage as tooling stabilizes; waiting for v2 means ceding ground


### OpenAI gives agents a real runtime

The biggest bottleneck for production agents has never been the model. It's been the runtime. Agents that need to execute code, call APIs, read files, and maintain state across long tasks have been duct-taped together with custom orchestration layers. OpenAI's updated Agents SDK addresses this directly.

The SDK now ships with **native sandbox execution**, meaning agents can run code in isolated environments without builders spinning up their own container infrastructure. It also supports **long-running agents**, the kind that don't just answer a question and disappear but persist across multi-step workflows that might take minutes or hours.

This matters because it collapses a layer of infrastructure that every serious agent builder has been maintaining themselves. If you've been using LangGraph, CrewAI, or custom orchestration to manage agent state and tool execution, OpenAI just made the "build vs. buy" calculus shift hard toward buy. The primitives, sandboxing, persistence, tool calling, are now first-party.

The timing is deliberate. Microsoft has been shipping its own agent frameworks aggressively. Google's agent tooling is maturing. The platform war for agent developers is real, and OpenAI is making the case that their SDK should be the default foundation layer. For builders, the practical implication is clear: **the cost of getting a multi-step agent into production just dropped significantly**, but so did the defensibility of custom orchestration as a product.


### Adobe turns creative suites into agent playgrounds

Adobe's Firefly AI Assistant, previously teased as "Project Moonlight" last October, is entering public beta. It's not another image generator. It's a **cross-application agent** that can take a natural language instruction and execute tasks across Photoshop, Premiere, Lightroom, Illustrator, Express, and other Creative Cloud apps.

> The assistant can work across apps like Firefly, Photoshop, Premiere, Lightroom, Express, Illustrator, and its other apps to do tasks for you.

This is the enterprise creative workflow version of what OpenAI is doing at the infrastructure layer. Adobe isn't just adding AI features to individual apps. They're building an agent that understands the relationships between apps and can orchestrate work across them. Need to color-correct footage in Premiere, export stills, retouch them in Photoshop, and resize for social in Express? Describe it once.

The competitive signal here is loud. Adobe has **700 million+ Creative Cloud users** and deep enterprise penetration. When they ship agents that automate multi-app workflows, they're not experimenting. They're setting the expectation that creative professionals will interact with software through agents, not menus. Every creative tool startup that doesn't have an agent story is now playing defense.

Pricing details are still unclear, and Adobe hasn't said whether the assistant will live inside existing Firefly credit-based tiers or cost extra. That ambiguity is worth watching. The value of a cross-app agent is categorically different from a per-image generation credit, and Adobe's pricing decision will signal how they think about agent economics.


### Notion's five rebuilds reveal the real cost of agent products

The most honest data point today comes from Notion. On the Latent Space podcast, cofounder Simon Last and head of AI Sarah Sachs described what it actually took to ship Custom Agents, the feature teased at Notion's last Make conference.

**Five rebuilds.** Over 100 tools. Years of iteration starting from failed tool-calling experiments in 2022, before there was even a standard for how models should interact with external tools.

> Early agent attempts failed: no tool-calling standard, short context windows...

This is the part of the agent story that doesn't make it into launch blog posts. Notion is a decacorn with deep engineering talent, and they still burned through multiple architectural approaches before landing on something production-worthy. They had to solve progressive tool disclosure (how do you give an agent access to 100+ tools without overwhelming it?), evaluate MCP vs CLI-based approaches, figure out how meeting notes could serve as structured data capture for agents, and design an eval system that could actually measure agent quality.

The framework they arrived at, turning Notion into an "agent-native system of record for enterprise work," is ambitious. But the path there was brutal. For any founder or product leader planning an agent initiative, Notion's experience sets a **concrete benchmark**: expect multiple full rebuilds, expect the tooling landscape to shift under you, and expect the hardest problems to be in orchestration and tool management, not in the model itself.

This aligns with what we've seen across the industry. The teams succeeding with agents are the ones treating them as product engineering problems, not AI research problems. Bounded tasks, clear success metrics, iterative architecture. Notion's five rebuilds aren't a failure story. They're the normal cost of building something real.


### Vibe coding's security bill comes due

Gitar emerged from stealth with **$9 million** led by Venrock, and their thesis is elegant in its circularity: AI agents are generating mountains of code, that code has quality and security problems, so you need AI agents to review it.

> AI agents have unleashed a deluge of code onto companies that many are now struggling to manage. This sudden inundation has been called "code overload."

Founded by Ali-Reza Adl-Tabatabai, who spent time at Intel Labs, Google, and Uber, Gitar sells subscription access to a platform that deploys agents for code-quality operations. The target customer is any engineering org drowning in AI-generated pull requests that senior engineers don't have time to review manually.

This is a **second-order market** that only exists because the first-order trend, AI code generation, is working. Cursor, Copilot, Windsurf, and dozens of other tools have made it trivially easy to generate code. But generating code and shipping safe code are different problems. Reports consistently show AI-generated code introduces bugs, security vulnerabilities, and architectural debt that compounds over time.

$9 million is a modest raise, but the timing and the investor signal (Venrock, Sierra Ventures) suggest conviction that this market will grow proportionally with AI code generation itself. If agents write 50% of production code within two years, the security review market isn't a niche. It's infrastructure.


### The stack is filling in from both ends

What makes today unusual isn't any single announcement. It's the simultaneity. OpenAI is hardening the foundation layer with sandboxed execution and persistent agents. Adobe is building the application layer with cross-app creative agents. Notion is revealing what the middle layer, the product engineering of agents, actually costs. And Gitar is building the cleanup layer for agent output.

This is what infrastructure maturation looks like. Not one company shipping a breakthrough, but an entire stack filling in at once. The agent primitives (tool calling, sandboxing, state management) are becoming commodities. The application patterns (multi-app orchestration, progressive tool disclosure, domain-specific agents) are being proven in production. And the second-order markets (security, quality, governance of agent output) are attracting real capital.

The builders who will have a structural advantage in 12 months are the ones investing now, not in building custom orchestration that OpenAI will ship next quarter, but in the domain-specific agent logic that sits on top of these platforms. The retail agents, the creative workflow agents, the code security agents. The picks-and-shovels layer is consolidating fast. The value is moving up the stack, into agents that know something about a specific domain and can operate with real autonomy within it.

Waiting for the tooling to "stabilize" is a trap. The tooling is stabilizing right now, and the teams learning through their own five-rebuild journeys are building knowledge that can't be bought later.

---

### #2 Allbirds sells its shoes, buys GPUs, and calls itself NewBird AI

A shoe company becoming a GPU cloud provider sounds like satire. It's not.

Allbirds sold its footwear brand and assets last month for **$39 million**, then announced a pivot to AI infrastructure under the new name **NewBird AI**. The rebranded company calls itself a "fully integrated GPU-as-a-Service and AI-native cloud solutions provider" and secured **$50 million in convertible financing** from an undisclosed institutional investor.

> It's objectively pretty funny that Allbirds is becoming an AI company, not because it's unusual for companies to pivot, but because of how extreme this pivot is.

The math is worth examining. Allbirds sold its entire reason for existing for $39 million, then raised $50 million to enter one of the most capital-intensive, commoditized segments of the AI market. GPU-as-a-Service is a business where you compete with AWS, Azure, GCP, CoreWeave, Lambda, and a dozen other well-funded players. The margins are thin, the capex is enormous, and the competitive moats are measured in data center leases and NVIDIA allocation agreements.

This isn't an AI story. It's a capital markets story. A public company shell with a depressed valuation attaches the letters "AI" to its name and attracts $50 million in financing that Allbirds-the-shoe-company could never have raised. For founders and investors, it's a **useful signal about how frothy the AI capital environment remains**, even as the underlying technology matures. When a wool sneaker brand can rebrand as GPU infrastructure and raise a $50 million round, the market is telling you something about how indiscriminate some AI capital allocation still is.

---

### What to do this week

**1. Test OpenAI's updated Agents SDK against your current orchestration stack.** If you're running LangGraph, CrewAI, or custom agent orchestration, spend 2-3 hours this week porting one simple multi-step agent to the new SDK. Specifically test the sandbox execution and long-running agent support. The docs are at [openai.com/index/the-next-evolution-of-the-agents-sdk](https://openai.com/index/the-next-evolution-of-the-agents-sdk). If the first-party primitives cover 80% of what your custom layer does, that's a signal to stop maintaining your own infrastructure and build on top of theirs instead.

**2. Audit your AI-generated code exposure.** If your team uses Copilot, Cursor, or any AI coding tool, ask your engineering lead one question: what percentage of merged PRs in the last 30 days were primarily AI-generated, and how many of those got a meaningful human security review? If the answer is "we don't track that," you've found a gap. Tools like Gitar ([gitar.co](https://gitar.co)) and Snyk's AI code scanning are worth evaluating now, before the security debt compounds further.

**3. Use Notion's rebuild count as your planning benchmark.** If you're scoping an agent product initiative, listen to the first 30 minutes of the [Latent Space episode with Notion's team](https://www.latent.space/p/notion). Then take your current timeline estimate and multiply it by 2-3x. Not because your team is worse, but because the honest industry benchmark for production agent products, from a well-resourced decacorn, is five architectural rebuilds. Plan your budget and team patience accordingly.