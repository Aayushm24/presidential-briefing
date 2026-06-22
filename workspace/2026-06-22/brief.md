# AI coding agents work. Everything else is still broken.

[Ethan Mollick](https://x.com/emollick/status/2068729258176819253) put his finger on exactly why AI coding agents work while everything else still feels like a demo.

Coding agents succeed because software has a ground truth. The code either runs or it doesn't. But most knowledge work lacks this verification layer, making AI agents brittle outside engineering. The breakthrough isn't better models. It's designing work outputs that can be verified like code.

This verification gap explains why enterprise AI rollouts show predictable patterns. Engineering teams achieve measurable ROI within quarters, while marketing and strategy departments struggle to justify AI investments after months of pilots. The difference isn't capability or adoption willingness, it's the presence of built-in feedback mechanisms that allow rapid iteration and improvement.

**Key takeaways:**
- AI coding agents hit practical utility because software provides instant verification feedback, GLM 5.2 now matches proprietary models on coding benchmarks
- The "software-brained" architecture breaks down for knowledge work where process matters as much as output, no equivalent to "does the code compile?"
- Open-weight coding models like GLM are production-ready through FireworksAI, removing API vendor lock-in for builders
- Enterprise AI adoption accelerates at Samsung-scale deployments, but success clusters in engineering-adjacent workflows where verification exists
- Memory and context layers matter more than model upgrades for building AI products that stick beyond demos

### Why coding agents work when everything else breaks

The problem with AI agents isn't capability. It's feedback.

[Nathan Lambert](https://x.com/natolambert/status/2068695675299336270) noted this week that GLM 5.2, an open-weight model, achieved "practically useful coding" benchmarks before Google's Gemini. That milestone came roughly 200 days after Claude Opus 4.5 set the bar. The sequence reveals something crucial about AI development: coding agents reached utility first not because they're technically superior, but because they have better feedback loops.

The technical achievement matters less than the underlying mechanism. Coding agents work because code provides instant, objective verification. When Claude Code generates a function, you know within seconds whether it compiles and passes tests. When it refactors a module, the test suite either goes green or red. When it suggests an optimization, the benchmarks either improve or they don't.

This verification loop creates a training signal that makes coding agents genuinely useful. The AI gets immediate, unambiguous feedback on whether its output actually works. Over hundreds of iterations, the model learns to generate code that compiles, runs efficiently, and solves the intended problem. The feedback is binary and fast, two properties that accelerate learning.

Contract this with other AI applications. When an AI writes a marketing email, how do you know if it's good? Open rates won't come for hours. Click-through rates take days. Revenue attribution takes weeks. The feedback signal is delayed, noisy, and hard to isolate. The AI can't learn to write better emails because "better" has no clear definition.

Mollick articulates why this architectural difference matters: "A fundamental problem with extending Codex/Cowork/Code to all knowledge work is that they remain very 'software-brained' where the end result is what is important & that code serves as a source of truth. For a lot of other knowledge work, the process is at least as important as the outcome."

The insight cuts deeper than most founders realize. In knowledge work, writing, research, analysis, strategy, the value often lives in the exploration process, the failed experiments, the reasoning chain that led to the conclusion. A perfectly formatted report that reaches the wrong conclusion is worthless. A beautifully designed presentation that misses the key insight wastes everyone's time. But there's no equivalent to "compilation failed" for bad insights or flawed reasoning.

This architectural constraint explains why AI adoption clusters in engineering teams first, even at companies with ambitious AI strategies. [Samsung Electronics](https://openai.com/index/samsung-electronics-chatgpt-codex-deployment) just deployed ChatGPT Enterprise and Codex to employees worldwide, marking one of OpenAI's largest enterprise rollouts to date. The scale is massive, tens of thousands of employees across global operations.

But I'd bet the highest usage rates and strongest ROI metrics cluster in Samsung's semiconductor engineering divisions, not their marketing departments or business development teams. Engineers have tools to measure AI output quality. They run tests, check performance metrics, validate against specifications. Other functions lack these built-in verification systems.

The causal chain forward is predictable and already happening. Companies will see measurable AI ROI in engineering workflows months or years before other departments show similar returns. CTOs will become AI champions because they have concrete metrics to defend budget allocation. Engineering teams will expand AI usage because they can prove it works. Meanwhile, other functions will struggle to justify AI spend without clear success measures.

What I keep coming back to is the verification problem. Most AI product failures aren't model limitations. They're architectural design failures. The teams building AI for knowledge work need to create new output formats that can be verified like code, or accept that their AI products will remain impressive demos rather than reliable tools.

### The verification gap shapes enterprise adoption patterns

[Fiona Fung](https://www.lennysnewsletter.com/p/building-the-most-ai-pilled-engineering) manages the Claude Code and Cowork teams at Anthropic. Her job is building "the most AI-pilled engineering team in the world." The framing reveals the constraint: even at Anthropic, the AI-first workflows succeed primarily in engineering contexts.

This isn't because other functions can't use AI. Samsung's global ChatGPT deployment shows appetite exists across departments. The constraint is architectural. Engineering work produces artifacts that can be tested, deployed, and measured. Marketing campaigns, strategy documents, and research reports don't have the same built-in verification mechanisms.

The pattern plays out at scale. Large enterprises adopt AI for coding, data analysis, and technical documentation first. These workflows already have testing infrastructure. Pull requests get reviewed. Analyses get validated against known datasets. Documentation gets checked for accuracy.

But when the same companies try to deploy AI for creative briefs, strategic planning, or customer research, the projects stall. The AI can do the work, but no one can confidently evaluate whether the AI did the work well.

The mental model shift: successful AI products don't just automate tasks. They redesign outputs to be more verifiable. Instead of generating a marketing strategy, generate a marketing experiment with clear success metrics. Instead of writing a research report, create a set of testable hypotheses with data collection plans.

The winners will be teams that recognize verification as a design constraint, not an afterthought. They'll build AI workflows that produce outputs which can be rapidly tested and iterated, borrowing the feedback loops that make coding agents effective.

### Open weights change the game for builders

The deployment equation shifted this week. [Nathan Lambert](https://x.com/natolambert/status/2068720732797014188) spent an hour testing GLM 5.2 through FireworksAI and came away impressed: "Very easy to set up on @FireworksAI_HQ, props to them for that, took me like 5min to get going in claude code."

Five minutes to production-ready coding assistance. No API waiting lists. No vendor negotiations. No usage limits imposed by a third party whose priorities might change.

This matters more than the benchmark scores suggest. Open-weight models hitting practical utility removes the biggest risk for builders building coding-adjacent products: API dependency. When your entire product relies on OpenAI or Anthropic staying responsive, affordable, and aligned with your needs, you're building on rented land.

GLM 5.2 via FireworksAI gives you ownership of your AI stack. You can fine-tune for your specific use case. You can guarantee uptime. You can scale without negotiating enterprise contracts.

The timing aligns with the broader conviction I've been tracking: small teams with AI beat 50-person orgs in 2026. But only if they can move fast without getting blocked by vendor dependencies. Open-weight coding models remove the biggest bottleneck.

I think founders should ship coding agent integrations now. The capability is real. The open alternatives are production-ready. The verification problem is solved for software outputs. The competitive window exists while most teams still treat AI as a nice-to-have instead of core infrastructure.

The founders who integrate coding agents this quarter will have six months of compound advantage over teams that wait for "better models." The models are good enough. The distribution is open. The feedback loops work.

---

### GBrain open sourced, where AI products fail without memory

[Garry Tan](https://x.com/garrytan/status/2068701357696323769) open-sourced GBrain this week. It's his personal and company context layer on top of AI tools. The repo gives you a concrete look at where most AI products actually break: memory.

GBrain solves the problem that makes demos feel magical and products feel frustrating. The AI remembers what you worked on last week. It knows your company's context. It learns from your feedback patterns. It builds on previous conversations instead of starting fresh every time.

This is the real competitive advantage in AI products. The memory layer matters more than the underlying model or UI polish.

Most teams spend engineering cycles on model upgrades and miss the memory architecture entirely. They build AI features that work beautifully for the first interaction and feel broken by the third. Users try the demo, get excited, then abandon it because it can't remember their preferences or build on past work.

Tan's decision to open-source GBrain signals something important. The personal/company brain category is still nascent enough that sharing implementations helps everyone. But it also suggests the real value isn't in the memory storage code, it's in the specific context and relationships you build over time.

The pattern connects to the verification problem. Memory systems work well when they're tested against real workflows. Tan built GBrain for his own company's needs first. It works because it evolved through daily use, not theoretical requirements.

Teams building AI products should study the GBrain repo and ask: what's our equivalent memory layer? How does context persist between sessions? How does the system learn from user corrections? How do insights compound over time instead of getting lost?

The memory problem is harder than the model problem. But it's also more defensible once solved.

---

### Trump administration targets Anthropic, political risk for AI builders

The [TechCrunch report](https://techcrunch.com/2026/06/21/when-the-trump-administration-cracks-down-on-anthropic-who-benefits/) on the Trump administration's moves against Anthropic should wake up every founder building on Claude APIs.

The regulatory risk isn't hypothetical anymore. When governments can target specific AI labs, API dependencies become political liabilities. Teams that built their entire product on Claude face potential shift from policy changes that have nothing to do with their business.

This reshapes the competitive landscape in ways most founders haven't considered. If Anthropic faces restrictions or compliance costs that slow development, which models benefit? If Claude APIs become less accessible or more expensive, where do teams migrate?

The immediate winners are likely OpenAI (less regulatory scrutiny currently) and open-weight alternatives (no single point of government pressure). But the deeper lesson is about diversification. Products that depend on a single AI provider face concentration risk that goes beyond technical considerations.

The smart move for teams building on Claude: implement model switching now while you have time to architect properly. Build your AI layer to abstract across providers. Test your product with multiple backends. Ensure your competitive advantage doesn't depend entirely on one model's specific capabilities.

Political risks compound with technical dependencies. The most resilient AI products will be the ones that can swap models without breaking core functionality.

---

### What to do this week

**Test GLM 5.2 via FireworksAI** (15 minutes). If you're building anything coding-adjacent, spend 15 minutes setting up GLM through FireworksAI. Nathan Lambert's experience suggests the integration is straightforward. You'll get a sense of open-weight coding capability without committing to infrastructure changes.

**Audit your AI product for verification layers** (30 minutes). Look at every AI feature you're building and ask: what's the equivalent of "code compiles" for this output? If you can't define clear success criteria, redesign the output format. The verification problem is solvable, but only if you acknowledge it exists.

**Build memory persistence before upgrading models** (ongoing). Study the GBrain repo and identify your memory gaps. Context persistence and learning from user feedback matter more than model capability for product stickiness. Start with simple state storage and build toward compound learning.

The pattern is clear: AI succeeds when outputs can be verified quickly and improved iteratively. Code has this property built-in. Most knowledge work doesn't. The winning teams will be those who redesign their workflows around verification loops, not just LLM upgrades.
