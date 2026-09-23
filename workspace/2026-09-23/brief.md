# Yesterday's triple model release reset the cost curve for AI builders

[Simon Willison](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) watched Claude Opus 5.5 at "max" thinking level spend $2.56 and 20 minutes reasoning about an SVG pelican, then hit its 128,000 token limit without producing any output.

Yesterday [OpenAI released GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna) at half the price of their predecessors, and [Anthropic responded with Opus 5.5](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/) at 20% lower prices. The simultaneous releases triggered the first major price war between frontier model providers. Every builder who locked architecture decisions around GPT-5 or Claude 3 era pricing must re-benchmark their entire model stack immediately.

**Key takeaways:**
- GPT-6 Luna hits $0.10/$0.50 per million tokens, half the price of GPT-5.6 Luna and the cheapest OpenAI model since GPT-4.1 Nano
- Claude Opus 5.5 dropped 20% in price but gained Fable 5.1-level performance, with 60% cheaper cache reads for agentic workflows
- The price war affects the tier below flagship models ($10M+ tokens), GPT-6 Astra and Claude Fable 5.1 still both cost $10/$50
- Builders optimized for GPT-5 or Claude 3 era economics now need to re-evaluate which model tier delivers the best cost/capability ratio
- The "max" thinking modes may be marketing theater, Opus 5.5 max over-thinks simple tasks to the point of failure

### OpenAI's aggressive pricing resets model economics

[GPT-6 Luna costs $0.10 per million input tokens and $0.50 per million output tokens](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/). That's exactly half the price of GPT-5.6 Luna, which charged $0.20 and $1.20 respectively. GPT-6 Sol follows the same pattern. It delivers GPT-5.6 Sol-level performance at $2 input and $10 output, compared to the previous $4 and $20.

This pricing reset happened on the same day as the model releases. GPT-5.6 has a scheduled 25% price increase for November. OpenAI just made their new models half the cost of the promotional pricing for the old ones.

The speed suggests this was planned market shift, not organic cost optimization. [OpenAI's pricing table](https://openai.com/index/introducing-gpt-6-sol-and-luna) positions GPT-6 Luna as one of the cheapest models they've ever released. Only GPT-4.1 Nano at $0.10/$0.40 in April 2025 and GPT-5 Nano at $0.05/$0.40 in August 2025 were cheaper. Both of those models were significantly weaker than Luna.

What makes this pricing aggressive is the capability floor. GPT-5.6 Luna was already Willison's "favorite model for building applications against, because it combined excellent performance with being really cheap." GPT-6 Luna delivers that same performance at half the cost. For builders running high-volume inference workloads, this is an immediate 50% cost reduction with zero performance trade-offs.

The timing forces immediate architectural decisions. Startups that committed to GPT-5.6 workflows six months ago face sudden cost pressure from competitors who can deliver the same capability at half the price. A startup processing 100 million tokens monthly just saw their AI costs drop from $32,000 to $16,000. That's $192,000 in annual savings without changing a single line of code.

Enterprise teams evaluating AI investments can now justify twice the usage volume for the same budget. A financial services company that allocated $50,000 monthly for document processing can now handle twice the volume or redirect half the budget to other initiatives. New projects will default to GPT-6 Luna unless there's a specific reason to pay more.

This creates downstream pressure on every other model provider. [Grok 4.7 launched at $2/$6](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/), positioning itself as less than half the price of GPT-5.6 Sol. xAI's marketing emphasized the cost advantage over OpenAI's premium models. Now GPT-6 Sol costs exactly $2/$10, matching Grok on input and getting closer on output. Grok's price advantage evaporated in one day.

The competitive cascade extends beyond direct competitors. Cloud providers offering managed AI services must recalculate their markup structures. A managed service charging 2x the underlying model cost needs to justify that premium when the underlying cost just dropped 50%. SaaS companies with AI-powered features can either pass savings to customers or improve margins. Either choice forces strategic decisions about competitive positioning.

The pattern suggests OpenAI is using pricing to force platform decisions while capabilities remain roughly equivalent. Teams that build on GPT-6 Luna for cost reasons will find it expensive to migrate later when the next price war hits a different tier. The cost advantage compounds into vendor lock-in as teams optimize their workflows around specific model behaviors and pricing structures.

### Anthropic responds but cannot match OpenAI's price floor

[Anthropic's counter-move was Opus 5.5](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/), released hours after OpenAI's announcement. The new model costs $4 per million input tokens and $20 per million output tokens. That's down from Opus 5.0's $5 and $25. The cache read price dropped 60%, which matters significantly for agentic conversations where most input tokens get processed at cached rates.

Anthropic positioned this as delivering "Fable 5.1-level intelligence" at a lower tier. [Thariq Shihipar described it](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) as "cheaper per token than Opus 5.0 with the intelligence of Fable 5.1." They also claimed it's "very token efficient and works across every effort level."

But the math shows Anthropic cannot compete on pure price. Opus 5.5 costs 4x more than GPT-6 Luna for input tokens and 40x more for output tokens. Even with the 60% cache discount, cached Opus tokens cost $0.20 per million compared to GPT-6 Luna's base rate of $0.10.

Anthropic's bet appears to be superior performance and cache economics for specific use cases. For teams running agentic workflows with 90%+ cached token ratios, the cache discount could offset the base price premium. A conversation where 50,000 tokens are fresh and 450,000 tokens are cached would cost $260 on Opus 5.5 versus $275 on GPT-6 Luna. The Opus advantage only appears at very high cache ratios and substantial context volumes.

This reveals different strategic approaches to the price war. OpenAI used broad price cuts to force decisions across the entire market. Anthropic targeted cache-heavy workflows where they can claim superior unit economics. The problem is that most teams don't operate at the scale where cache optimization matters more than base pricing.

What I keep coming back to is the speed of the response. Anthropic announced Opus 5.5 within hours of GPT-6's release. That suggests they were already planning price cuts but accelerated the timeline to avoid looking reactive. The cache-focused messaging feels like positioning around a pre-existing pricing strategy rather than a direct competitive response.

The immediate impact lands on enterprise procurement teams. Any RFP process that started before yesterday now includes wildly different pricing assumptions. Teams that were comparing GPT-5.6 Luna at $0.20/$1.20 against Opus 5.0 at $5/$25 are now comparing GPT-6 Luna at $0.10/$0.50 against Opus 5.5 at $4/$20. The competitive landscape shifted in one day.

This forces a fundamental re-evaluation of model selection criteria. Price per token was already a key factor, but the gaps between providers just became canyons instead of differences. A team processing 50 million tokens monthly would pay $2,500 on GPT-6 Luna versus $200,000 on Opus 5.5. That 80x price difference changes every cost-benefit analysis.

The shift also exposes the hidden costs of model switching. Teams that built complex prompt engineering around Opus's communication style can't simply swap in GPT-6 Luna and expect identical outputs. The cost savings are real, but so is the re-engineering effort required to maintain quality. Early movers who switch quickly gain cost advantages. Late movers face both higher costs and expensive migration projects.

Anthropic's strategy appears to be defending high-value use cases where performance justifies the premium. Agentic workflows with complex reasoning requirements, creative writing projects that demand specific voice characteristics, and applications where output quality matters more than unit cost. The question is whether that market segment is large enough to sustain their business model when the volume segment migrates to cheaper alternatives.

### The "max" thinking modes reveal reasoning theater

[Willison's test of Opus 5.5's "max" thinking level produced an expensive failure](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/). He asked it to "Generate an SVG of a pelican riding a bicycle", his standard benchmark for model creativity and technical execution. The model started reasoning about the task, calling it "a classic test request," then spent $2.56 and nearly 20 minutes thinking without producing any output.

The model hit its 128,000 token limit while still reasoning about pelican anatomy and bicycle mechanics. Willison tried twice and got the same result both times. The "max" mode over-thought the problem to the point of breaking. Standard reasoning modes completed the same task successfully.

This failure reveals a fundamental flaw in reasoning transparency features. The model produced detailed internal thoughts about "verifying the shin length checks out at roughly 95.2" and "outlining the heel, toe tips, and sole contour with a path using lines and curves to sit naturally on the pedal surface around y=478-494." But all that reasoning led nowhere.

The failure pattern suggests "max" reasoning is theater, not substance. It shows elaborate thought processes but doesn't improve outcomes. For builders, this means the reasoning display is a debugging tool, not a performance feature. The transparency helps you understand why a model made specific decisions, but it doesn't make those decisions better.

The cost structure makes this worse. Two failed attempts cost $5.12 total with zero output. That's more than most teams spend on hundreds of successful completions at the base tier. For production workflows, the "max" thinking level becomes unusable on cost alone, regardless of the failure rate.

This connects to broader patterns in model development. Teams building AI products often over-engineer the model intelligence instead of focusing on memory and state management. The "max" reasoning mode is the model-level equivalent of that mistake. More thinking doesn't equal better thinking, just as more parameters don't automatically equal better results.

What this tells me about reasoning models is that the transparency is valuable for debugging and understanding, but not for performance improvement. Teams should use standard reasoning modes for anything user-facing. Reserve "max" modes for analyzing edge cases or understanding why a model made specific decisions. Treat it as a development tool, not a production feature.

The broader lesson is about marketing versus utility in model features. "Max" reasoning sounds impressive in demos and marketing materials. But when it fails on simple tasks while burning through token limits, it becomes clear that the feature optimizes for impressiveness rather than usefulness. Builders need to separate what sounds good in a pitch from what works in production.

This pattern repeats across AI product development. Teams over-invest in model sophistication and under-invest in memory, state management, and error recovery. The "max" reasoning mode is the perfect metaphor for this mistake. More computation doesn't automatically produce better outcomes. Sometimes it produces worse outcomes at higher cost.

The failure also reveals how reasoning transparency can mislead rather than inform. Reading the model's internal thoughts about "heel, toe tips, and sole contour with a path using lines and curves" feels like insight into sophisticated processing. But those detailed thoughts led nowhere. The transparency became a distraction from the core problem, the model couldn't complete the task.

For teams building AI products, this suggests focusing on results rather than process. Use reasoning transparency to debug failures and understand edge cases. Don't use it as a substitute for better outcomes. Most users care about getting the right answer, not understanding how the model approached the problem.

The cost failure is even more instructive. $2.56 for zero output is a unit economics disaster. Scale that to production workflows and "max" reasoning becomes a budget killer. Teams optimizing for cost per successful completion should avoid features that increase token consumption without improving success rates.

---

### Amazon blocks Meta's Muse and reveals platform power dynamics

[Amazon predictably blocked Meta's Muse](https://stratechery.com/2026/amazon-blocks-muse-amazons-competitive-advantage-aggregator-v-aggregator/), the AI agent that would let users research and purchase products across multiple retailers. The block demonstrates platform power dynamics that every AI startup building on closed ecosystems must understand and plan for.

Muse represented the first major AI agent designed to arbitrage across e-commerce platforms. Users could describe what they wanted, and Muse would search Amazon, eBay, Walmart, and other retailers to find the best deals. Amazon's terms of service gave them clear grounds to block this behavior, and they exercised that right within days of Muse's public launch.

Ben Thompson's analysis reveals the strategic logic. Amazon's physical world investments, warehouses, delivery networks, supplier relationships, create genuine competitive advantages that software-only retailers cannot replicate. When AI agents make price comparison frictionless, those physical investments become more valuable, not less. Amazon can afford to block agents that make shopping a generic commodity because they win on fulfillment speed and reliability.

For AI builders, this illustrates the platform dependency risk that most teams underestimate. Companies building agents that scrape or automate interactions with major platforms should assume those platforms will eventually restrict access. The restriction comes when the agent threatens core business models, which happens faster than most founders expect.

The pattern applies beyond e-commerce. Social platforms will block agents that automate content creation or engagement. Financial platforms will restrict agents that automate trading or account management. Cloud platforms will limit agents that optimize across multiple providers. Every platform has terms of service that give them broad discretion to block automated access.

The solution requires multi-platform strategies and direct data partnerships. Teams building on platform APIs need backup data sources and alternative distribution channels. Teams scraping public data need legal review and technical redundancy. Teams depending on a single platform for core functionality are building on borrowed time.

What's revealing is the speed of Amazon's response. Muse wasn't a stealth product, Meta announced it publicly with significant media coverage. Amazon's legal and technical teams were ready to respond within days. This suggests major platforms are actively monitoring AI agent development and preparing to restrict access as soon as agents threaten revenue streams.

The competitive dynamics favor platforms with deep physical or regulatory advantages. Amazon can block shopping agents because their logistics network creates customer value that software cannot replicate. Banks can restrict financial agents because they control the underlying account infrastructure. Platforms without those deep advantages, aggregators built purely on software, face more serious competitive threats from AI agents.

for builders, this means evaluating platform risk as seriously as technical risk. Build on platforms where your use case aligns with the platform's business model. Avoid platforms where your success depends on behaviors the platform will eventually want to restrict. Plan for platform restrictions as part of your competitive analysis, not as an edge case.

---

### What to do this week

**Re-benchmark your model costs** (30 minutes): If you're using GPT-5.6 Luna or Opus 5.0, run your typical workload against GPT-6 Luna. Calculate savings at your current volume. Most teams will save 50%+ on inference costs. Use your actual prompt lengths and completion targets, not synthetic benchmarks. Document the performance differences alongside the cost differences, Luna may require different prompt engineering for optimal results.

**Test cache performance on long conversations** (1 hour): For agentic workflows with context windows over 10,000 tokens, compare Opus 5.5's 60% cheaper cache reads against GPT-6's overall lower prices. Use realistic conversation lengths from your application logs. Calculate the break-even point where cache discounts offset base price premiums. Most teams will find GPT-6 Luna wins unless cache ratios exceed 90%.

**Avoid "max" reasoning modes in production** (immediate): Based on Willison's findings, max thinking modes are debugging tools, not performance upgrades. Use standard modes for anything user-facing. Reserve "max" modes for understanding edge case failures or analyzing model decision-making during development. The cost and reliability trade-offs make them unsuitable for production workflows where users expect consistent responses.
