# AI startups have 12 months before platform providers absorb their categories

Notion rebuilt their agent system five times before platform providers started shipping the features they were building.

Foundation models are expanding into adjacent categories faster than most founders realize. The window to build defensible moats is measured in months, not years. Teams that differentiate on distribution, proprietary data, or deep workflow integration win. Everyone else becomes a feature.

**Key takeaways:**
- Claude 4.7 costs 46% more tokens than 4.6 for text, 3x for images, API budgets based on sticker pricing miss hidden inflation
- TechCrunch names it directly: AI startups exist because foundation models haven't expanded into their category yet
- Canva's $26B AI strategy shows how incumbents with distribution win the integration race
- Half of product managers face displacement as AI automates the coordination layer they used to own
- Enterprise security incidents via AI platforms are accelerating, Context.ai compromise hit Vercel users

### The 12-month countdown

[TechCrunch published a piece yesterday](https://techcrunch.com/2026/04/19/the-12-month-window/) that puts a timeline on something every AI founder fears but few discuss openly. The title says it all: "The 12-month window."

The thesis is brutal in its simplicity. Most AI startups exist because OpenAI, Anthropic, and Google haven't built their category yet. That protection won't last.

> "Many AI startups exist partly because foundation models haven't expanded into their category yet, acknowledging this won't last forever."

What caught my eye is how [Canva's CPO Cameron Adams](https://www.therundown.ai/p/exclusive-inside-canva-ai-2-0-with-cpo-cameron-adams) describes their AI 2.0 strategy. They're not building AI features. They're rebuilding the entire creative workflow around AI. The difference matters.

Canva has 100 million users and $26 billion in market value. When they decide your AI startup's feature belongs in their workflow, you compete against their distribution, not just their product. A three-person team with better AI can't overcome a platform with 100 million daily users who never have to leave to get what they need.

This explains the urgency behind OpenAI's acquisition spree and Anthropic's partnership strategy. They're not just buying talent. They're buying time before someone else builds the complete solution.

The countdown started when o1 proved reasoning could scale with compute. Now every platform provider can see the path from here to there. Twelve months is optimistic.

### Where the moats still exist

Not every AI startup dies in this window. The ones that survive own something platform providers can't easily replicate.

Distribution is the obvious moat. [Nikhyl Singhal from Meta and Google](https://www.lennysnewsletter.com/p/why-half-of-product-managers-are-in-trouble) puts a number on what this means for product roles. Half of product managers are at risk because AI automates the coordination work they used to own.

> "Half of product managers are in trouble, how to cross the reinvention threshold, and why the next two years will be chaotic for PMs."

The insight cuts both ways. If AI eliminates coordination overhead, small teams can ship faster. But if you're competing against a platform that already has users, your speed advantage gets neutralized by their distribution advantage.

Proprietary data works, but only if it's truly unique and continuously updating. Customer support logs from 2023 aren't defensible. Real-time workflow data from power users who can't switch might be.

Deep workflow integration is the third moat. Not "AI features inside your existing product." Complete reimagining of how work gets done. Canva isn't adding AI image generation to their existing canvas. They're changing what it means to design.

The pattern holds across categories. The AI startups that survive integrate so deeply into existing workflows that switching costs become prohibitive. Platform providers can build the AI capability. They can't easily replicate years of workflow optimization.

### The hidden cost trap

While founders worry about platform competition, a quieter risk builds in their API bills. [Simon Willison discovered](https://x.com/simonw/status/2046029612820594962) that Claude Opus 4.7 uses 46% more tokens for text than 4.6, and up to 3x more for images.

Same per-token pricing. Invisible cost increase.

Any team budgeting Claude API usage based on sticker pricing will miss this. The real cost of upgrading models isn't just the new features. It's the token inflation that nobody warns you about.

[Simon built a tool](https://simonwillison.net/2026/Apr/20/claude-token-counts/#atom-everything) to compare token counts across Claude models. Free to use. Takes five minutes to check your actual costs.

This connects to the bigger platform risk. Google has the strongest models in some benchmarks, but [their app and website lack proper tooling](https://x.com/emollick/status/2045909435315323321). Teams choosing which API to build on can't just compare model capabilities. They need to audit the entire development experience.

The gap between model quality and product quality creates opportunities for teams that own the complete developer experience. Platform providers with great models but poor tooling lose to platforms with adequate models and great tooling.

---

### #2 Security becomes the new AI differentiator

The [Vercel security incident](https://x.com/swyx/status/2046030085237432573) via Context.ai shows how AI platforms create new attack surfaces. A compromise in one AI service cascade to every developer platform that integrates with it.

This isn't theoretical risk. Live systems got compromised because teams treated AI vendor security as someone else's problem.

The response matters more than the incident. Teams with strong AI vendor security reviews win deals against teams that integrate first and audit later. Enterprise buyers already ask harder questions about your AI supply chain than they do about your core infrastructure.

Simon Willison's concept of ["headless everything"](https://simonwillison.net/2026/Apr/19/headless-everything/#atom-everything) becomes relevant here. Personal AI agents will drive demand for headless service APIs because they can provide better security isolation than monolithic platforms.

The pattern: AI creates new ways to attack systems, which creates new ways to defend them, which creates new categories of tooling. Security becomes a feature differentiator, not just a compliance requirement.

---

### #3 o1 preview was the second most important model release after GPT-3.5

[Ethan Mollick's retrospective](https://x.com/emollick/status/2046053467941163055) on OpenAI's o1 preview frames it as the second most important LLM release after GPT-3.5. That ranking matters for how founders explain capability jumps to boards and investors.

o1 proved that test-time compute scales reasoning in ways that training-time compute alone couldn't achieve. The architectural insight unlocks a new scaling law. More compute during inference improves output quality even with the same base model.

This changes how teams think about model deployment. Inference becomes variable cost based on problem complexity, not fixed cost based on token count. Complex reasoning tasks cost more compute. Simple tasks cost less.

The implication: AI applications can dynamically trade latency and cost for output quality. The teams that build this trade-off into their product architecture win against teams that treat all AI calls as equally expensive.

---

### What to do this week

**1. Audit your Claude API token usage across model versions** (15 minutes)
Use [Simon Willison's Claude Token Counter](https://simonwillison.net/2026/Apr/20/claude-token-counts/#atom-everything) to compare token costs between Claude models. Test your actual prompts, not sample text. Budget for 46% token inflation when upgrading from 4.6 to 4.7.

**2. Map your product's defensible elements** (30 minutes)
List what you own that platform providers can't easily replicate: unique distribution channels, proprietary data sources, or deep workflow integrations. If your entire moat depends on model access, you have a 12-month problem to solve.

**3. Review your AI vendor supply chain for security exposure** (45 minutes)
Document every third-party AI service your product integrates with. Check their security incident history. Map which vendors could compromise your users if they get breached. Enterprise customers will ask these questions during security reviews.
