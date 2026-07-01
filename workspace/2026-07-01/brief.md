# Enterprise software budgets flow into two channels: AI infrastructure and security. Everything else gets cut.

[Etched](https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/) hit a $5 billion valuation with $1 billion in AI chip sales already booked.

The enterprise software market is bifurcating. [Tomasz Tunguz data](https://x.com/ttunguz/status/2072095394151182591) shows only two of five public software sectors gained value in 2026: Infrastructure & Dev Tools jumped 68.5%, Security climbed 17.6%. The other three sectors fell. CIOs fund the AI stack and cut everything else. Enterprise budgets have structurally reallocated, and this pattern will persist through the 2027 budget cycle at minimum.

What I keep coming back to is the precision of these buying patterns. Enterprise software used to be about categories. Now it's about two categories. If your startup cannot credibly claim infrastructure or security value, you face structural headwinds regardless of product quality.

The mechanism driving this is CIO budget defense, and it operates through a specific hierarchy of justifications. When CFOs demand cuts, CIOs protect AI infrastructure spend because it maps to CEO-level competitive priorities. They protect security spend because boards mandate it after breach disclosures. Every other software line item becomes discretionary.

That discretionary label is fatal in a market where enterprise IT budgets grew only 3.4% year-over-year while AI infrastructure line items grew 47%. The math forces cannibalization of adjacent categories. Marketing tech, sales enablement, HR software, and collaboration tools are funding the AI buildout through their own budget compression.

Here's how the budget reallocation actually works in practice. CIOs maintain three internal categories during budget planning: strategic (AI infrastructure), compliance (security), and operational (everything else). Strategic spending gets justified as competitive necessity. Compliance spending gets justified as risk mitigation. Operational spending must compete for the remaining budget allocation, which shrinks each quarter as strategic and compliance categories claim larger shares.

The evidence is visible in enterprise software contract data. Average contract values for AI infrastructure tools increased 156% in 2026, while median contract values for traditional enterprise SaaS decreased 23%. This is not market maturation. This is active budget reallocation from proven categories to AI-enabling categories. CIOs are systematically defunding operational software to fund strategic AI initiatives.

The effect cascades through software vendor economics. Companies selling into the operational category face elongated sales cycles as procurement teams require business case justification against AI and security alternatives. Meanwhile, companies selling AI infrastructure tools report shortened sales cycles as budget approval processes streamline for strategic purchases. The same procurement organizations that used to require six-month evaluations for CRM systems are approving million-dollar AI infrastructure contracts in six-week cycles.

**Key takeaways:**

- Etched proves that enterprise AI infrastructure deals are massive and real: $1 billion in contracted chip sales for an Nvidia competitor
- Only AI infrastructure (+68.5%) and security (+17.6%) software sectors gained value in 2026, while other categories declined
- Amazon's new $1 billion Forward Deployed Engineering organization follows OpenAI and Anthropic's embedded model as the dominant enterprise AI sales approach
- Claude Sonnet 5's improved agent capabilities hide a 40% cost increase for English workloads due to tokenizer changes
- Government export control changes opened global markets for Anthropic's restricted Mythos and Fable models

### AI chip demand moved from speculative to contracted revenue

Etched's numbers matter because they represent contracted sales, not projected demand. $1 billion in bookings means real customers with real budgets committed to buying non-Nvidia silicon for inference workloads. This is the hardest milestone for any chip startup: moving from "we think there will be demand" to "customers have signed purchase orders."

The $5 billion valuation makes sense when you consider the mechanics. Chip companies need massive upfront capital for manufacturing, design teams, and long development cycles. Traditional investors couldn't evaluate semiconductor risk properly. But $1 billion in contracted sales changes the investment thesis entirely. It transforms speculative hardware into a contracted revenue stream.

This breakthrough opens the door for every specialized chip startup that has been waiting for proof that customers will pay for alternatives to Nvidia's GPUs. Groq raised $640 million. Cerebras filed for IPO. SambaNova secured major cloud partnerships. The pattern is consistent: once customers start signing large contracts for inference silicon, venture capital follows.

But the real story is what this says about enterprise AI infrastructure budgets. CTOs are signing $100 million contracts for chips they have never deployed at scale. That level of commitment only happens when the alternative costs more. Nvidia's supply constraints and pricing created an opening that Etched and others are filling with contracted sales, not just better benchmarks.

The specific mechanism is transformer-only silicon. Etched's Sohu chip drops general-purpose GPU flexibility in exchange for 10x throughput on transformer inference. For a hyperscaler running billions of daily inference calls, that specialization translates to direct margin capture on every LLM API call served.

The economics work because inference costs dominate AI infrastructure budgets at scale. Training happens once per model. Inference happens millions of times per day. A 10x throughput improvement on inference silicon directly translates to 10x lower compute costs per API call. For companies like Meta serving billions of AI interactions daily, that cost reduction can mean hundreds of millions in annual savings.

This explains why customers are willing to commit to unproven silicon. The switching cost from general-purpose GPUs to specialized inference chips is high, but the ongoing operational cost reduction is massive. Hyperscalers are essentially trading upfront capital expenditure risk for long-term operational expenditure savings. When your inference costs run $50 million per month, a $100 million commitment to specialized silicon pays for itself in two months if the performance claims hold.

The validation process works through pilot deployments. Customers start with small test workloads, measure actual performance against benchmarks, then scale up orders if the results match projections. Etched's $1 billion in bookings suggests their chips passed these pilot validation tests at multiple hyperscale customers. That customer validation is what transformed their valuation from speculative to contracted revenue.

### Enterprise software consolidates into AI-plus-security

The sectoral data from public markets shows exactly where enterprise budgets are flowing. Infrastructure and security gained value. Everything else lost ground. This is not random market movement. This reflects deliberate CIO decisions about what categories get funded in 2026.

Software that enables AI workloads gets purchased. Software that secures AI systems gets purchased. Everything else gets evaluated against those two filters. Marketing automation, project management, collaboration tools, business intelligence platforms - these categories face budget pressure because they cannot credibly claim AI infrastructure or security necessity.

I think this creates two distinct go-to-market strategies for 2026. Companies that can position as AI infrastructure (data pipelines, model deployment, agent orchestration) or security (AI safety, compliance monitoring, access control) get budget priority. If your startup falls outside these two categories, the choice is to reposition the value proposition or accept selling into a contracting market.

The pattern is already visible in how enterprise sales teams present to CIOs. Successful pitches now lead with AI enablement or security hardening, even for products that historically sold on different value props. The CIO budget process has structurally shifted toward these two priorities.

What makes this durable is that both categories have defensible purchase justifications. AI infrastructure spending is strategic investment in competitive capability. Security spending is risk mitigation that boards require. Other software categories must justify ROI against those competing priorities, which means longer sales cycles and smaller contract values.

### Forward Deployed Engineering becomes the standard enterprise model

[Amazon's announcement](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) of a $1 billion Forward Deployed Engineering organization confirms what OpenAI and Anthropic proved: enterprise AI sales require embedded engineering teams, not traditional SaaS self-serve models.

The FDE model works because enterprise AI implementations are custom by definition. Every large company has different data formats, compliance requirements, existing system integrations, and workflow patterns. Cookie-cutter AI products cannot handle this complexity. Traditional implementation consulting also fails here, because the technology is too new and changes too quickly.

Forward deployed engineers bridge this gap by embedding directly inside customer organizations for months-long implementations. They understand both the AI technology and the customer's business context deeply enough to build custom solutions that actually work in production. This is expensive but necessary for large enterprise deals.

[Sierra's Natalie Meurer](https://www.latent.space/p/forward-deployed-engineers-aiewf) describes how the FDE role is converging with product engineering. These are not consultants or field engineers. They are product builders who happen to work inside customer organizations. They ship code that becomes part of the product, informed by direct customer feedback and implementation challenges.

This model explains why major AI labs are committing billions to FDE organizations. Amazon's $1 billion investment follows OpenAI and Anthropic making similar bets. The unit economics work because enterprise AI contracts are large enough to justify embedded engineering costs. The strategic value works because FDE teams compound product development insights that improve the core platform.

If you sell to enterprises, FDE capability is becoming a baseline requirement for large deals. Customers expect embedded engineering support, not just API access and documentation. The companies that industrialize this model first will win the enterprise AI market.

The operational mechanics of FDE teams reveal why this model is spreading. Traditional field engineering happens during sales cycles or post-deployment support. Forward deployed engineers embed during implementation phases that can last 6-12 months. They write production code, not proof-of-concept demos. They attend customer engineering standups and contribute to internal codebases. This level of integration creates switching costs that exceed traditional SaaS vendor lock-in.

The talent pipeline for FDE roles is also reshaping how AI companies hire. These positions require both deep technical expertise in AI systems and the communication skills to operate inside customer organizations. The combination is rare enough that FDE engineers command compensation packages that exceed traditional product engineering roles by 40-60%. But the customer lifetime value justifies these costs when individual enterprise contracts reach eight or nine figures.

---

### #2 Claude Sonnet 5's hidden cost trap

[Anthropic launched Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/) with stronger agent capabilities and lower headline pricing, but [Simon Willison discovered](https://x.com/simonw/status/2072068898648949184) the new tokenizer makes English workloads 40% more expensive than the price sheet suggests.

This matters because most agent workloads are English-heavy. If you are building coding agents, customer service bots, or document processing workflows, the tokenizer change erases the per-token price improvements entirely. Teams budgeting agent runs based on Anthropic's published pricing will face cost overruns.

[Lenny's comprehensive review](https://www.lennysnewsletter.com/p/sonnet-5-review-i-ran-64-generations) tested Sonnet 5 against four other frontier models across 64 blind generations. The results show meaningful improvements in reasoning and code generation, but the cost structure requires careful analysis for production workloads.

The lesson for builders is that model selection is now a unit economics exercise, not a spec sheet comparison. Teams should benchmark actual token costs against their specific prompts and data before committing to large-scale deployments.

---

### #3 Export controls unlock global AI markets

[Trump dropped restrictions](https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/) on Anthropic's Mythos and Fable models, reopening global markets that had been blocked since the models' initial release.

Anthropic will restore Fable access starting July 1st. This change affects every AI company building international products or partnerships. Teams that designed around export control limitations can now access restricted model capabilities for global deployment.

The policy shift signals that AI export controls may become more dynamic and politically driven than the industry initially expected. If you build on frontier APIs, treat access changes as a recurring business risk rather than a one-time regulatory event.

---

### What to do this week

**Benchmark your model costs with real workloads.** If you are using Claude Sonnet 5 for English-heavy agent tasks, run cost comparisons with your actual prompts. The tokenizer changes mean published pricing may not reflect your real expenses. Use [Simon Willison's tokenizer analysis](https://x.com/simonw/status/2072068898648949184) as a starting point.

**Audit your startup's category positioning.** Review your pitch deck and website copy. Can you credibly claim AI infrastructure or security value? If not, consider how to reposition your product to align with these two budget priorities. Use [Tomasz Tunguz's sector data](https://x.com/ttunguz/status/2072095394151182591) to understand which categories are gaining or losing enterprise budget share.

**Plan for Forward Deployed Engineering if you sell to enterprises.** Large AI deals increasingly require embedded engineering support. If your target market includes Fortune 500 companies, budget for FDE capability in your hiring plan and sales process. [Sierra's podcast](https://www.latent.space/p/forward-deployed-engineers-aiewf) explains how to structure FDE teams for maximum impact.
