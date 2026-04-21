# AI coding agents just proved they can 2x engineering velocity with real companies

Brian Scanlan, VP of Engineering at [Intercom](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering), spent nine months building something most engineering leaders skip entirely: telemetry.

Not the model. Not the plugin. A system that logs every Claude Code interaction, enforces engineering standards through hooks, and compounds everything the team learns into a shared skills repository. Every engineer, designer, and PM in the same loop. The result: 2x throughput, maintained code quality, measured in merged PRs per R&D employee per month over nine months.

**Key takeaways:**
- Intercom's 2x came from building institutional memory on top of Claude Code, not just deploying it
- Ethan Mollick's economics research shows AI agents deliver near-human median performance with 76% less variance, giving real calibration data for planning
- OpenAI's Skybysoftware acquisition was about state persistence, not computer use
- Tomasz Tunguz: Opus 4.7's new tokenizer added 46% more tokens while improving accuracy, breaking the assumption that model upgrades compress costs
- Noetik's Ron Alfa and Daniel Bear are applying transformers to cancer trial matching, betting that 95% of trial failures are a matching problem

---

### The measurement problem just got solved

Brian Scanlan didn't start by deploying Claude Code. He started by asking what he would measure.

That question produced a telemetry layer that most teams never build. Every Claude Code interaction logged. Every hook enforced. Every skill catalogued in a shared repository where the team's patterns, preferences, and edge cases accumulate into something no fresh installation can replicate.

Nine months later: [2x throughput with maintained code quality](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering). Measured in merged PRs per R&D employee per month. Not self-reported. Not estimated. Counted.

Intercom tracked individual adoption rates alongside output quality. They gave designers and PMs access to Claude Code skills, not just engineers, and found those roles started merging PRs too. That expansion only happens when the infrastructure is good enough that non-engineers can operate it safely without making a mess of the codebase.

What Scanlan built is essentially a teaching system. Agents learn the codebase's patterns because the patterns are logged. They enforce standards because the hooks make enforcement automatic. The team's nine months of decisions compound into the infrastructure rather than sitting in individual engineers' heads.

A competitor who signs up for Claude Code today starts at zero. Intercom's agents start with nine months of institutional memory. That gap doesn't close by paying for the subscription. It closes by doing what Intercom did, nine months ago.

The CTOs who've been skeptical about AI coding tools at scale now have a documented case: one company, real numbers, published methodology, reproducible process. The telemetry layer either starts now or it starts later. Later just means the gap keeps growing.

### Why 76% less variance matters more than the median

[Ethan Mollick](https://x.com/emollick/status/2046362044786458648) replicated classic multi-team economics experiments using AI agents. Claude Code and other coding agents consistently perform near the median of human teams, with 76% less variance in outcomes.

Most readers focus on the median. The variance number is the real signal.

Human engineering teams swing. Your 10x engineer has off weeks. Junior developers have unpredictable months. Sprint velocity estimates carry wide error bars because the humans producing them carry wide error bars. Engineering leaders build buffer weeks, contingency sprints, and coverage systems specifically to absorb variance. That cost is invisible because it's structural and assumed.

Agents don't swing. Consistent median performance. Every sprint. Every quarter.

Intercom's case validates this at production scale. Their 2x velocity gain came with no regression spikes, no quality dips, no bad months. Month-over-month predictability at higher throughput. That's what 76% less variance looks like when it runs for nine months in a real company.

If you're structuring your team to absorb variance, that structure assumes a human performance distribution as the baseline. Buffer weeks, senior coverage, contingency planning, all overhead costs built around unpredictable humans. As agents hold the floor more consistently, those costs can be redirected.

This isn't about replacing engineers. The teams who've figured this out are doing something more specific: they're using agents to hold the consistent parts of delivery, and freeing their humans for the judgment-intensive work that actually requires taste, architecture, and context.

The Mollick study gives you calibration data. If your engineering team currently has wide performance spreads, AI agents compress that distribution. If you have a genuinely exceptional team, agents probably won't beat your best people. What they will do is make your predictability look very different in a planning spreadsheet.

### OpenAI paid for memory, not computer use

[Swyx flagged the Skybysoftware acquisition](https://x.com/swyx/status/2046362691606855700) as "one of OpenAI's best deals of the year."

The frame you'll see everywhere is "computer use." That's the product description. What OpenAI actually bought is state persistence.

An agent that can click through your CI dashboard is interesting. An agent that can click through your CI dashboard, remembers what it saw last Tuesday, and carries that context across sessions is a different product category. The first is a capable tool. The second is something closer to a persistent collaborator.

The "real computer use" problem has been stuck in demos for 18 months. Research labs and startups have shown impressive one-session walkthroughs. The blocker to production use wasn't capability, it was the inability to maintain context between sessions. Every session restart means re-explaining the environment, re-establishing the preferences, re-loading the state. That overhead makes computer use impractical for anything except self-contained one-shot tasks.

Skybysoftware was working on persistent state. That's what OpenAI paid for.

This connects directly to what Intercom built. Their biggest velocity gains came from agents handling deployment, testing, and integration tasks that go beyond writing code. Those gains require agents that remember the deployment preferences, the testing standards, the integration patterns. Without session persistence, that context has to be re-established every time.

As ChatGPT App adds computer vision and state persistence together, the gap between "impressive demo" and "useful production tool" gets much smaller. Teams that have already built the memory and context layer will be positioned to use this capability immediately. Teams waiting for the tools to mature are building that disadvantage in real time.

### The common thread: memory compounds, models don't

Intercom's telemetry layer isn't just logging, it's building a memory system. The skills repository accumulates the team's patterns. The hooks encode the standards. Nine months of interactions become institutional knowledge that new team members and new agents inherit.

OpenAI's acquisition is specifically about making context persist across sessions, giving agents the ability to accumulate knowledge about an environment rather than starting fresh each time.

Noetik, [founded by Ron Alfa and Daniel Bear](https://www.latent.space/p/noetik), is applying this same principle to clinical trial matching. Their thesis: 95% of cancer treatments fail to pass clinical trials not because the drugs don't work, but because the wrong patients enrolled. The fix is accumulated pattern matching, transformer models trained on the full history of every trial ever run, learning which patient profiles match which treatment criteria.

Model quality is now a commodity. Every serious team has access to the same foundation models. What compounds over time is the context layer, what your system has seen, logged, remembered, and learned. Intercom's advantage after nine months isn't Claude Code access. It's nine months of logged interactions their agents carry forward. A competitor can sign up for the same tool tomorrow and never replicate that context without putting in the same nine months.

This is where the 2026 competitive dynamic plays out. Not at the model layer, that's a subscription. At the context layer, that's accumulated time and institutional investment.

---

### #2 Model costs follow a sawtooth pattern, and Opus 4.7 proves it

[Tomasz Tunguz analyzed Opus 4.7's new tokenizer](https://x.com/ttunguz/status/2046277504797974700) and surfaced the most useful financial signal of the week.

Model upgrades don't reliably compress your AI costs. They follow a sawtooth pattern: efficiency gains and accuracy improvements alternate, and the accuracy cycles increase costs by breaking the token reduction gains from the previous cycle.

When Opus 4.5 shipped, it ran 40% cheaper than Sonnet despite higher per-token pricing, because it used 76% fewer tokens to reach the same outcome. Every team building on Claude got an immediate bill reduction. That felt like a permanent trend toward cheaper, more efficient models.

Then Opus 4.7 landed with a tokenizer that breaks text into smaller pieces to improve instruction following and reduce coding errors. Better outputs. But 46% more tokens for the same content. The efficiency gain from Opus 4.5 vanished.

The pattern across vendors: resolution improvements increase costs, efficiency improvements reduce them, in alternating cycles. Tunguz's conclusion is the operational takeaway: budget for cost volatility, not steady compression. A model upgrade can take your bill 40% higher overnight.

The practical implication: track token usage by task type, not just total spend. Build cost alert thresholds on individual workflow categories. When a new model ships, test your highest-volume use cases on the new tokenizer before rolling out at scale. The teams who do this know within days what a new model costs them. The teams who don't find out in the next billing cycle.

---

### #3 Noetik's bet: cancer trial failures are a matching problem

[Noetik](https://www.latent.space/p/noetik), founded by Ron Alfa and Daniel Bear, is applying autoregressive transformers to clinical trial matching.

Their thesis: 95% of cancer treatments fail to pass clinical trials. Not because the drugs don't work, because the wrong patients enrolled. Trial sponsors spend billions recruiting patients based on inclusion criteria that rely on structured data like age, diagnosis stage, and specific biomarkers. But the actual matching problem is more complex. Patients who would benefit from a treatment often don't get enrolled because the matching process can't process the unstructured clinical context that would identify them.

Noetik is training transformers on the full history of clinical trial data, patient records, and treatment outcomes to match patients to trials more accurately than current methods.

The business model is clear: pharmaceutical companies spend tens of billions on trials that fail. A 10-percentage-point improvement in trial success rates is worth more to that industry than most software companies generate in a decade. Noetik doesn't need to invent new science. They need to apply a proven architecture, the same transformer design that powers Claude Code, to a domain with well-defined failure modes, abundant data, and an industry that has demonstrated willingness to pay.

Transformer architectures trained for language transfer to pattern-matching problems in completely different domains. The architecture is general-purpose. The competitive advantage comes from having the domain data and the domain expertise to calibrate it. That combination, proven architecture plus specialized data plus domain knowledge, is exactly the wedge that makes vertical AI applications defensible against horizontal competitors.

---

### What to do this week

**Build the telemetry layer this week, not this quarter.** Read [Brian Scanlan's piece](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering) and identify three things you can start logging: which prompts your team runs most, which outputs they accept vs. modify, and which workflows they've automated. You don't need a full skills repository on day one. You need the habit of logging started, because the value compounds and day one of nine months is today.

**Audit your AI token spend by task type before the next model ships.** Log into your LLM cost dashboard and break spend by use case: code generation, summarization, classification, retrieval augmentation. Build a simple spreadsheet with current spend per task type. When Opus 4.8 or GPT-5 ships, run your top three highest-volume tasks on the new tokenizer before rolling it out. Takes 3 hours to set up, prevents a billing surprise.

**Read the [Mollick study thread](https://x.com/emollick/status/2046362044786458648) before your next quarterly planning.** It gives you the clearest available data on where AI agents perform consistently versus where human judgment still dominates. That boundary matters when you're deciding which parts of your roadmap to accelerate and which parts still need senior human attention. Twenty minutes before Q2 planning is the right time to have that calibration.
