# AI compute costs force architecture choices that will define the next 12 months

[Google](https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/) just committed $11 billion annually to SpaceX for compute capacity they can't get anywhere else.

The era of 'tokenmaxxing and go fast' is ending because the bills came due. Builders now face a binary choice: architect explicit local-vs-cloud routing or watch unit economics kill their products. Teams that nail cost routing win; teams that don't disappear.

**Key takeaways:**
- Google's $920M monthly SpaceX commitment signals traditional cloud supply chains have completely broken under AI demand
- The industry conversation shifted from 'go fast' to 'we need guardrails' on token costs, forcing architectural changes at every AI company
- Local AI now handles 78% of real workloads, proving hybrid routing architectures are operational reality, not theoretical optimization
- Chinese open weights models may stop shipping if costs rise, threatening the entire bootstrapped AI builder ecosystem

### When Google pays SpaceX $920M monthly, cloud scarcity becomes real

Google signed the largest compute deal in tech history. $920 million per month to SpaceX. That's $11 billion annually for satellite-based compute capacity.

This isn't emergency procurement. This is Google admitting that AWS, Azure, and their own cloud can't scale fast enough to meet AI training demand. When the company that runs one of the world's three largest clouds goes to a rocket company for compute, the constraint is real.

The mechanism here is supply chain failure at infrastructure scale. Traditional data centers take 24 months to build and require massive upfront capital. AI demand doubled every quarter through 2025. The math broke. SpaceX can launch compute capacity in weeks, not years.

What I keep coming back to is the location problem this creates. Satellite compute means latency, power constraints, and thermal management issues that ground-based clouds don't face. Every packet of data travels 22,236 miles up to geosynchronous orbit and 22,236 miles back down. That's 44,472 miles round-trip for every API call. Even at the speed of light, that adds 250-500 milliseconds of latency compared to terrestrial data centers.

The thermal constraints are even more severe. Satellites can't dissipate heat through air convection like ground-based servers. They rely on radiative cooling, which limits processing power and requires careful thermal management. This means satellite compute works best for batch processing jobs that can tolerate latency and don't require sustained high-performance computing.

Google chose these tradeoffs over waiting for terrestrial capacity. That tells you everything about how desperate the supply situation has become.

The causal chain from here runs straight through every AI builder's architecture. More hyperscaler-to-satellite deals are coming. Microsoft will follow Google to space-based compute within six months. Amazon will have to choose between spinning up their own satellite constellation or falling behind on AI infrastructure commitments.

This forces a new calculus for everyone building AI products. Compute location becomes a strategic decision, not an operational detail. Latency-sensitive workloads stay on ground. Batch training jobs go to space. Teams that understand this split win contracts. Teams that don't lose customers to competitors who architect around the new reality.

The founders building AI startups today face the same supply constraints as Google. The difference is Google has $11 billion to solve the problem. Bootstrapped teams don't. That makes routing decisions survival choices, not optimization opportunities.

### The 'tokenmaxxing' era officially ends as bills hit real budgets

The conversation changed overnight. [Rebecca Bellan at TechCrunch](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/) captured it perfectly: "The whole conversation shifted from tokenmaxxing and 'go fast' to 'we need guardrails, how do we control this?'"

That shift wasn't gradual. It happened when Q1 bills hit finance teams. Companies that spent six months optimizing for AI output quality suddenly had CFOs asking why their cloud bills tripled. The experimental budget became a real line item.

I saw this coming in March when Uber burned through their entire annual AI tooling budget in four months. That forced immediate caps on employee AI usage across large enterprises. What seemed like an edge case became the standard enterprise experience.

The mechanism driving this is visibility. Finance teams now have granular data on AI costs per employee, per project, per output. They can see exactly which teams burn through tokens fastest and which use cases deliver measurable ROI. That granular visibility creates granular pressure.

Teams optimizing for cost per output beat teams optimizing for output quality. The market proved this in two quarters. Companies building cost-aware AI products win enterprise deals. Companies building capability-first products lose budget conversations.

This creates three immediate effects. First, tiered model selection becomes standard architecture. GPT-4 for complex reasoning, GPT-3.5 for simple tasks, local models for bulk processing. Second, output caching and result reuse become core competencies, not nice-to-haves. Third, "cheap enough" models win market share over "best possible" models.

The teams that built explicit cost routing six months ago now have sustainable unit economics. The teams that optimized for capability without considering cost are retrofitting their entire architecture or running out of money.

### Local routing isn't theoretical anymore, it's 78% of real workloads

[Tomasz Tunguz](https://x.com/ttunguz/status/2062903809626755256) ran the numbers and found something remarkable. His laptop now handles 78% of his daily AI work. The cloud only gets "the hard fifth."

This isn't a cost-cutting experiment. This is mature architecture design where routing decisions happen at the request level. Simple queries go local. Complex reasoning goes to frontier models. Document processing stays on device. Creative writing gets sent to Claude.

The routing logic is explicit. Tunguz built decision trees that evaluate task complexity, privacy requirements, and latency needs before picking local versus cloud. The decision matrix includes specific thresholds: tasks requiring less than 1000 tokens and no external API calls go local first. Tasks needing multi-step reasoning or creative output route to cloud models. Privacy-sensitive data processing stays on device regardless of complexity.

This routing happens at the infrastructure layer, not the application layer. The system evaluates each request against predefined criteria and routes automatically. Developers don't make routing decisions manually for every AI call. The architecture makes those decisions based on task characteristics and current system constraints. That's systems thinking, not optimization theater.

What changed is hardware capability crossed a threshold. Consumer GPUs can now run 35B parameter models that match GPT-4 performance on domain-specific tasks. This wasn't possible 12 months ago. The quality gap closed just as the tooling layer simplified deployment for non-technical users.

The implications cascade through every part of the AI stack. Local-first becomes the default architecture pattern. Cloud becomes a premium tier for hard problems only. Teams building hybrid routing from day one ship products with predictable costs and zero API dependency risk.

This proves the small team advantage I've been tracking. A 3-person team with explicit local-cloud routing can build products with better unit economics than 50-person orgs that default to cloud APIs for everything. The coordination overhead disappears when the architecture makes cost decisions automatic.

The builders who understand this ship products that work offline, handle sensitive data locally, and scale costs with real usage instead of API calls. The builders who don't get surprised by their next bill.

---

### Chinese open weights dependency becomes strategic risk

[Ethan Mollick](https://x.com/emollick/status/2062746121055695077) identified the weak point in the local AI story. "A lot depends on Chinese labs continuing to ship open weights models. If they stop, the frontier falls further and further behind to those who want to use local/fine-tuned models."

The 78% local routing that Tunguz demonstrated only works if capable models exist to download. Right now, that means DeepSeek, Qwen, and other Chinese labs releasing frontier-quality weights for free.

But Mollick's economic argument is sound. "Open weights may not be a good business model as costs rise." Training runs that cost $100 million don't sustain themselves on goodwill and research prestige. If Chinese labs stop releasing models, the local AI ecosystem breaks.

This creates a strategic dependency problem for every team building on open weights. The cost advantage of local models depends on continued access to capable weights. If access disappears, teams face a brutal choice: pay frontier API prices or accept dramatically worse model quality.

The bootstrapped builder problem becomes existential. Teams with enterprise budgets can afford GPT-4 API calls. Teams without those budgets get locked out of AI capabilities entirely. The gap between frontier-access haves and have-nots widens from cost optimization to capability access.

What I'm watching for is defensive open weights infrastructure. US labs building sustainable business models around open weights. Enterprise customers paying for local deployment support. Government funding for open weight research as strategic capability.

The teams building products that depend on free Chinese models need backup plans. That means architectural flexibility to switch between local and cloud models. It means building customer value that justifies higher costs if necessary. It means treating current open weights access as a temporary competitive advantage, not a permanent architecture assumption.

---

### Agentic architecture gets real tradeoff frameworks

[Anthropic's framework](https://x.com/emollick/status/2063073955968123062) for agentic architectures finally gives builders explicit guidance on power versus token cost tradeoffs. Agent teams and workflows deliver more capability but consume dramatically more tokens than single-agent approaches.

The framework matters because it makes architectural decisions explicit. Single agent for simple tasks. Agent workflows for complex multi-step processes. Agent teams for problems requiring diverse capabilities. Each choice has predictable cost implications.

This connects directly to the cost routing theme. Agentic architectures become the expensive tier in a hybrid system. You use single agents for 80% of tasks and reserve agent teams for the 20% that justify the token cost.

The practical decision tree is clear. If the task can be solved by one model call, use one model call. If it requires multiple steps but follows a predictable pattern, use a workflow. If it requires different types of reasoning or tool use, use a team. The cost scales with architectural complexity.

What Ethan Mollick observed is crucial: "A lot of the decisions about which approach to use is from the AI itself & it often uses them in combination." The models are getting better at self-routing to the right architectural pattern for each task.

This means the teams building agentic systems need to think like platform architects. Design clear cost boundaries between architectural tiers. Build monitoring that tracks token usage by architectural pattern. Create routing logic that defaults to simpler approaches unless complex patterns are required.

The alternative is building agent teams for every task and burning through token budgets on problems that single agents solve fine. That's the architectural equivalent of using GPT-4 for math that a calculator handles better.

---

### What to do this week

Start with an AI cost audit. Track every API call your team made in the last month. Categorize by task type: simple queries, complex reasoning, document processing, creative work. Calculate cost per task category. Most teams discover 70% of their AI budget goes to tasks that local models handle fine.

Build explicit routing logic while you have the data. Set up decision trees that evaluate task complexity before picking local versus cloud. Simple pattern: if the task needs creativity or complex reasoning, send to frontier models. If it's classification, summarization, or structured data processing, route to local models first.

Download capable local models this week while Chinese open weights are still available. Test Qwen 2.5, DeepSeek V2, or Llama 3.1 on your actual use cases. Measure quality differences on tasks that matter to your product. Build local inference capability as insurance against future access restrictions.

Set up cost monitoring with actual budget alerts, not just usage dashboards. Most teams track tokens consumed but don't connect consumption to monthly budget burn rate. Build alerts that trigger when you're on track to exceed monthly budget by week 3, not day 31. This gives you time to adjust routing decisions before costs spiral.

The teams that nail cost routing in the next 60 days will ship products with sustainable unit economics. The teams that keep optimizing for capability without considering cost will run out of budget or get priced out of their market completely.
