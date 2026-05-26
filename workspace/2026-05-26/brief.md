# AI agents replace hundreds at ClickUp as workforce substitution accelerates

[ClickUp replaced hundreds of employees with thousands of AI agents](https://techcrunch.com/2026/05/25/what-clickups-mass-layoff-tells-us-about-the-future-of-work/) in what may be the first explicit workforce substitution at a funded startup.

The nine-year-old startup's mass layoffs signal that agent-workforce substitution has moved from theory to practice at venture-backed companies. When enterprise buyers ask hard questions about headcount implications, builders need architectural answers, not just product features. The coordination cost collapse is happening faster than most founders anticipated.

**Key takeaways:**
- ClickUp replaced hundreds of employees with thousands of AI agents, making the agent-workforce substitution thesis concrete at funded startups
- Felix Rieseberg shows practical Claude workflows that replace specialized roles: 3D house plans from floor plans, automated promise tracking, $20 hardware integration
- Simon Willison advocates red/green TDD for agent-generated code as regression protection when agents ship code faster than humans can review
- Google outpaces OpenAI 9-to-1 on hard math benchmarks while 7B open models match GPT-3.5-turbo, reshuffling model provider decisions for cost-sensitive builders
- The Vatican's AI encyclical targets concentrated tech power rather than AI itself, previewing regulatory pressure on platform consolidation

### ClickUp's workforce substitution experiment proves the agent employment thesis

[ClickUp explicitly replaced hundreds of employees with thousands of AI agents](https://techcrunch.com/2026/05/25/what-clickups-mass-layoff-tells-us-about-the-future-of-work/) this week. The productivity platform, founded in 2017 and valued at $4 billion, made the trade explicit in their announcement: human headcount down, agent workforce up.

This breaks new ground for venture-backed companies. Previous layoffs cited market conditions, cost reduction, or strategic pivots. ClickUp cited AI capability as the replacement mechanism. They're treating agent capacity like hired labor, not like software features.

What makes this particularly significant is the scale and directness. We're not talking about "AI-assisted productivity improvements" or "workflow automation." ClickUp hired thousands of agents to do jobs that hundreds of humans were doing yesterday. They're running the first large-scale experiment in explicit workforce substitution at a funded startup.

The mechanism matters as much as the outcome. ClickUp didn't phase in gradual automation or deploy AI as an assist tool. They made a sharp substitution: terminate human contracts, activate agent capacity, maintain output levels. This approach treats agents as direct labor replacements, not productivity multipliers.

Why now? The cost of coordination has finally dropped below the cost of human management for specific workflows. Managing hundreds of specialists requires layers of communication, alignment meetings, performance reviews, and HR overhead. Managing thousands of agents requires prompts, monitoring dashboards, and version control. The coordination complexity inverts at scale.

The causal chain forward is predictable. Enterprise buyers will start asking hard questions before signing AI contracts. "If we deploy your platform across 500 knowledge workers, how many will we need in 18 months?" Vendors who can't answer this question with specifics will lose deals to vendors who can. The conversation shifts from "what can your AI do?" to "how many people can your AI replace?"

I keep coming back to the procurement implications. When a funded startup publicly trades hundreds of humans for thousands of agents, every enterprise buyer has to model this scenario for their own organization. The ClickUp precedent makes agent-workforce substitution a board-level discussion, not a product team experiment.

The timing advantage goes to founders who design for this transition now. Teams that build agent-first workflows from day one skip the migration pain that comes from retrofitting human-designed processes for agent execution. Small teams with well-designed agent workflows beat larger teams with manual processes.

### Felix Rieseberg's workflows show what agent-augmented roles actually look like

[Felix Rieseberg, the Anthropic engineer behind Claude Cowork, demonstrates](https://www.lennysnewsletter.com/p/how-the-engineer-behind-claude-cowork) exactly what professional work looks like when agents handle specialized tasks. His workflows redefine professional roles completely.

His 3D house walkthrough workflow transforms floor plans into navigable 3D spaces. Not conceptual renderings or architectural sketches. Actual walkthrough experiences that let clients move through spaces before construction. He feeds Claude a floor plan image and gets back a complete 3D model with realistic lighting, furniture placement, and camera paths.

Real estate professionals now need this capability. What was previously locked behind specialist 3D modeling teams, expensive software licenses, and week-long project timelines is now essential. Felix compressed that entire specialist workflow into a single Claude conversation.

His promise tracking system automatically monitors commitments across email threads, Slack conversations, and meeting transcripts. When someone says "I'll send you the contract by Friday," the system logs it, tracks the deadline, and surfaces broken promises without human oversight. The system doesn't just track explicit commitments. It infers implicit promises from conversational context.

The $20 hardware "buddy" integration shows how agent workflows extend beyond software. Felix built a physical device that listens to conversations, processes them through Claude, and provides contextual responses through a simple LED interface. The hardware cost is negligible. The agent processing creates value that justifies dedicated devices for specific workflows.

These examples matter because they show agent-augmented roles, not agent-replaced roles. Felix didn't eliminate the need for real estate professionals, project managers, or hardware engineers. He created hybrid roles that combine human judgment with agent execution capability. Professionals who master these workflows become irreplaceable in ways that pure human expertise or pure automation cannot match.

The pattern extends across every knowledge work category. Marketing professionals who master agent-assisted content creation don't just work faster. They work at scales that pure human effort cannot achieve. Engineering managers who use agents for code review and documentation work at quality levels that manual processes cannot sustain.

What separates winners from losers is workflow design, not tool access. Most founders treat Claude Code like an IDE plugin instead of an agent runtime. They use it for coding assistance when they should use it as the execution layer for their entire company: documentation, customer research, competitive analysis, investor updates.

The compound advantage builds over time. Professionals who design agent workflows early establish patterns that scale. Teams that treat agents as enhanced search engines miss the coordination collapse that comes from well-designed agent-human collaboration.

### The engineering discipline gap as agents ship code faster than humans can review

[Simon Willison advocates for red/green TDD](https://x.com/simonw/status/2058992972734341445) when working with coding agents specifically because agents generate code faster than humans can thoroughly review it. The discipline gap creates regression debt that compounds as agent-generated code volume scales.

His argument is precise: [write failing tests first, let the agent generate code that passes them, then write more tests for edge cases](https://x.com/simonw/status/2058992461381562382). The test-driven workflow forces explicit requirement definition before code generation and creates automated protection against feature regression when making future changes.

The speed differential is the core problem. Human developers read through code line-by-line, mentally trace execution paths, and catch subtle bugs through experience pattern-matching. Agents generate hundreds of lines of functional code in seconds. Human review speed doesn't scale to match agent generation speed.

Traditional code review processes break down when one agent can output more code in an hour than a human reviewer can thoroughly evaluate in a day. Teams that skip systematic testing discipline accumulate hidden regression debt. Features work correctly when first generated but break unexpectedly when modified later.

Red/green TDD creates automated safeguards that scale with agent productivity. Failing tests define success criteria before code generation. Passing tests validate that generated code meets requirements. Comprehensive test suites protect existing functionality when agents generate modifications.

This matters beyond code quality. Teams shipping agent-generated code without systematic testing discipline create maintenance nightmares. Bug fixes break existing features. Feature additions introduce subtle regressions. Technical debt compounds faster than human debugging can resolve it.

The competitive advantage goes to teams that establish testing discipline early. Well-tested agent-generated code compounds into reliable systems. Poorly tested agent-generated code compounds into maintenance overhead that eventually forces complete rewrites.

I think the deeper principle is that memory and testing architecture matters more than model capabilities. Teams optimizing for the latest model releases while ignoring systematic testing and state persistence are building on unstable foundations. The infrastructure choices determine whether agent productivity creates compounding advantages or compounding technical debt.

---

### Model provider landscape shifts as Google outpaces OpenAI and open models make inference cheap

[Google's models now outperform OpenAI 9-to-1 on hard math benchmarks](https://www.therundown.ai/p/google-tops-openai-math-breakthrough-9-to-1), marking a decisive capability shift that matters for builders choosing model providers for reasoning-heavy applications. This represents a decisive capability shift. The gap is large enough to change vendor selection decisions.

The math benchmark performance signals broader reasoning capability differences that extend beyond mathematical problem-solving. Complex logical reasoning, multi-step analysis, and systematic problem decomposition all benefit from the same underlying capabilities that drive math performance. Applications that depend on precise reasoning now have a clear provider hierarchy.

Simultaneously, [Qwen2.5-7B matches GPT-3.5-turbo performance](https://x.com/garrytan/status/2059007262182785432) while running on dramatically cheaper infrastructure. A 7B parameter model that delivers GPT-3.5-turbo quality inference means cost models for high-volume AI products change fundamentally. Startups paying OpenAI API fees for GPT-3.5-turbo level capability can now run equivalent models on their own infrastructure at fraction of the cost.

The convergence creates a two-tier market structure. Frontier reasoning tasks require Google's advanced models despite higher costs. High-volume, standard-quality tasks can run on open-weight models at commodity pricing. The architectural decision becomes cost-performance optimization across different workload categories.

AI product builders need to audit their current model usage patterns against these performance and cost shifts. Applications using GPT-4 for tasks that Qwen2.5-7B can handle are burning money on unnecessarily expensive inference. Applications using GPT-4 for complex math or reasoning tasks that Google's models handle better are limiting their product capability.

The lock-in risk compounds over time. Model provider switching costs increase as applications accumulate prompt engineering, fine-tuning data, and integration complexity. Teams that optimize for their current provider without monitoring competitive landscape changes build technical debt into their product architecture.

The strategic implication is provider diversification rather than provider consolidation. top AI products will use Google models for complex reasoning, open-weight models for high-volume standard tasks, and specialized models for domain-specific applications. The winners architect for multi-provider workflows from the beginning.

---

### The Vatican enters AI governance as institutional pressure builds on concentrated tech power

[Pope Leo XIV's AI encyclical](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) doesn't actually target AI technology. It targets concentrated tech power using AI as the lens for diagnosing older problems: eroding democracy, platform consolidation, and tech elites shaping society to their own advantage.

[The TechCrunch analysis](https://techcrunch.com/2026/05/25/the-popes-ai-encyclical-isnt-really-about-ai/) frames this correctly: the encyclical uses AI as a vehicle for broader critiques of big tech concentration. The Vatican focuses on artificial intelligence control, not the technology itself. Who decides how AI systems behave? Who profits from AI deployment? Who bears the costs of AI externalities?

This matters for AI founders because it previews the regulatory and public pressure that concentrated AI platforms will face. The Vatican's institutional authority legitimizes anti-concentration narratives that will shape policy environments. Consumer AI products that visibly distribute capability rather than consolidate it will navigate regulatory scrutiny more easily.

The encyclical establishes religious authority backing for AI governance frameworks focused on democratic participation and equitable benefit distribution. When major religious institutions enter technology policy discussions, they bring moral authority that secular policy arguments cannot match. The Vatican's position becomes a reference point for global AI regulation debates.

For practical purposes, this means consumer AI founders should consider how their products appear to regulatory bodies concerned about tech concentration. Products that enable user control, data ownership, and distributed capability deployment align with the institutional pressures building around AI governance. Products that consolidate user data, limit user control, or concentrate AI capability face headwinds.

The timing suggests broader institutional coordination around AI governance. When the Vatican publishes detailed AI encyclicals, other major institutions are likely developing similar positions. Consumer AI founders should expect coordinated pressure from religious, educational, and civic institutions concerned about democratic participation in AI development and deployment.

The strategic response is product architecture that visibly distributes rather than consolidates AI capability. Tools that help users run their own models, control their own data, and modify their own AI behaviors align with institutional pressure for democratic AI governance. Platforms that lock users into centralized systems face institutional resistance.

---

### What to do this week

**Audit your agent-generated code for TDD coverage** (30 minutes). List every piece of code that agents generated in your codebase over the past month. Check which pieces have comprehensive test coverage and which don't. For code without tests, write failing tests first, then verify the agent code passes them. This creates regression protection as you generate more agent code.

**Test Felix Rieseberg's 3D house plan workflow** (15 minutes). Find a floor plan image online or sketch one yourself. Ask Claude to generate a 3D walkthrough description, focusing on room layouts, lighting, and navigation paths. Even if you're not in real estate, the workflow demonstrates how agents can replace specialized technical roles across industries.

**Evaluate your model provider lock-in given Google's math performance advantage** (45 minutes). Document which tasks in your application require complex reasoning versus standard language processing. Test Google's models on your hardest reasoning tasks. Calculate cost differences between your current provider and Qwen2.5-7B for high-volume standard tasks. Build a multi-provider architecture plan that optimizes cost and capability across different workload types.
