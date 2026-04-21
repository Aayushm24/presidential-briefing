# AI coding agents just proved they can 2x engineering velocity with real companies

Brian Scanlan spent nine months building something most engineering leaders won't invest in: [telemetry for AI impact](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering).

Not the model. Not the IDE plugin. A system that logs every Claude Code interaction, enforces engineering standards through hooks, and compounds institutional knowledge into a shared skills repository. Every engineer, designer, and PM at Intercom in the same loop. The result: 2x throughput, maintained code quality, measured in merged PRs per R&D employee per month over nine months.

That's the story this week. Not that AI helps engineers code faster. That one VP built the infrastructure to make AI compound, and published the whole playbook.

**Key takeaways:**
- Intercom's 2x gain came from building memory infrastructure on top of Claude Code, not from Claude Code alone
- Ethan Mollick's economics research shows Claude Code performs near human median with 76% less variance, giving founders real calibration data
- OpenAI's Skybysoftware acquisition signals that state persistence, not computer use, is the prize
- Model costs follow a sawtooth pattern: Opus 4.7's new tokenizer added 46% more tokens while improving accuracy, breaking simple cost forecasts
- Noetik is applying transformers to cancer trial matching, betting that 95% of trial failures are a matching problem, not a drug problem

---

### The measurement problem is solved

Brian Scanlan, VP of Engineering at Intercom, spent nine months building infrastructure most teams skip entirely.

Not plugins. Not autocomplete. Telemetry.

Every Claude Code interaction logged. Every pattern analyzed. Every engineering standard enforced through hooks. A shared skills repository where the team's workflows, preferences, and edge cases compound into something no new install can replicate.

The result: [2x throughput with maintained code quality](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering). Not in a controlled experiment. Across their entire engineering org, measured in merged PRs per R&D employee per month.

What makes Intercom's case worth studying is the methodology, not just the number. They tracked individual adoption rates. They measured quality metrics alongside velocity. They gave designers and PMs access to Claude Code skills, not just engineers, and found those roles started merging PRs too. That expansion only happens when the tooling is instrumented well enough that non-engineers can operate it safely.

The thing most teams miss: Intercom didn't get lucky with a smart sprint. They built infrastructure that teaches itself. A competitor who signs up for Claude Code today gets the same tool. They don't get nine months of logged patterns, calibrated workflows, and institutional knowledge baked into every agent interaction. That gap doesn't close by paying for the subscription.

What I keep coming back to: CTOs have been asking for months whether AI coding tools actually work at scale. Brian Scanlan just published the answer. The methodology is documented. The metrics are real. Any engineering leader who reads this piece and doesn't start building telemetry this week is making a deliberate choice to fall behind.

### 76% less variance, and why that number matters more than the median

[Ethan Mollick's study](https://x.com/emollick/status/2046362044786458648) replicated classic multi-team economics experiments with AI agents. Claude Code and other coding agents consistently perform near the median of human teams. With 76% less variance in outcomes.

The variance number is the story. Not the median.

Human engineering teams are inherently unpredictable. Your 10x engineer has off weeks. Junior devs have good months and bad ones. Sprint estimates carry wide error bars because the humans carrying them carry wide error bars. You budget for variance as a constant cost of doing business.

Agents don't have off weeks. Consistent median performance. Every sprint. That predictability, compounded over quarters, changes how you plan, how you hire, and what you optimize for.

Intercom's 2x velocity gain didn't come from random acceleration. It came with zero regression and no quality spikes. Month-over-month predictability at higher throughput. That's what 76% less variance looks like in production.

The implication for how you build: if you're currently structuring your team to compensate for variance (buffer sprints, senior dev coverage, contingency planning), those structures assume the human performance distribution is your baseline. As agents hold the floor more consistently, that assumption needs updating.

### Real computer use is shipping, and the acquisition that explains it

[Swyx's read on OpenAI's Skybysoftware acquisition](https://x.com/swyx/status/2046362691606855700): "one of OpenAI's best deals of the year."

The framing you'll see everywhere is "computer use." That's the wrapper. What OpenAI actually paid for is state persistence. Agents that carry context between sessions, that remember your codebase, your deployment preferences, your environment configuration, operate fundamentally differently than agents that reset with every conversation.

Swyx flagged this clearly: the "real computer use" problem has been stuck in demos for 18 months. What unlocks it isn't better vision models. It's memory. An agent that can click through your CI dashboard and knows what it saw last Tuesday is a different product than an agent that starts fresh every time.

This connects directly to what Intercom found. Their biggest velocity gains came from agents handling deployment, testing, and integration tasks outside the IDE. When an agent can interact with every tool in your stack and remember what it did last time, the 2x multiplier becomes achievable. Without memory, computer use is a party trick.

The timing: ChatGPT App plus computer vision plus state persistence is a meaningful near-term unlock. Teams that have already built the context layer will be positioned to use it. Teams waiting for the tools to mature first are building that disadvantage in real time.

---

### #2 Model costs follow a sawtooth pattern, Opus 4.7 just proved it

[Tomasz Tunguz's analysis](https://x.com/ttunguz/status/2046277504797974700) of Opus 4.7's new tokenizer is the most useful financial signal this week.

Model upgrades don't compress your AI budget. They follow a sawtooth: efficiency gains get erased by accuracy improvements in alternating cycles.

When Opus 4.5 shipped, it ran 40% cheaper than Sonnet despite higher per-token pricing, because it used 76% fewer tokens to reach the same outcome. Every team building on Claude got an immediate bill reduction. That felt like a permanent trend.

Then Opus 4.7 landed with a tokenizer that breaks text into smaller pieces. Better instruction following. Fewer coding errors. But 46% more tokens for the same content. The efficiency gain vanished.

The pattern across vendors: resolution improvements increase costs, efficiency improvements reduce them, in alternating waves. Tunguz's conclusion: budget for cost volatility, not steady compression. A model upgrade can take your bill 40% higher overnight.

Practical implication: track token usage by task type, not just total spend. When Opus 4.8 or GPT-5 ships, you want to understand the financial impact on your highest-volume use cases within days, not weeks.

---

### #3 Transformers tackle cancer trials with a 95% failure rate

[Noetik](https://www.latent.space/p/noetik), founded by Ron Alfa and Daniel Bear, is applying autoregressive transformers to clinical trial matching. Their thesis: 95% of cancer treatments fail to pass clinical trials not because the drugs don't work, but because the wrong patients enrolled.

It's a matching problem, not an efficacy problem.

The same transformer architecture powering Claude Code can be trained on patient records and trial criteria to match patients to trials more accurately than current methods. If clinical trial failure is primarily a matching problem, transformers trained on enough data can flip those odds.

The business model is direct: pharmaceutical companies spend billions on failed trials. A 10-percentage-point improvement in success rates is worth more than most software businesses ever generate. Noetik doesn't need to invent new science, they need to apply proven architecture to a domain with clearer failure modes and more patient capital than most startup markets.

What this illustrates for builders: transformer models trained for language transfer to pattern-matching problems in other domains. Clinical matching, materials science, supply chain optimization, the architecture is becoming a general-purpose problem-solving tool. The question is whether the training data and domain expertise exist to calibrate it.

---

### The thread connecting all three stories

All three leading stories this week share the same underlying mechanism: **context that persists and compounds**.

Intercom built a skills repository so agents learn from every interaction. The value isn't Claude Code access, it's nine months of logged patterns their agents carry forward. Competitors can't buy that with a subscription.

OpenAI paid for state persistence. The computer-use acquisition is about agents that remember your environment across sessions, not just within them.

Noetik's thesis is that 95% of trial failures come from missing accumulated context about which patients match which treatments. Their transformer learns from every trial ever run.

Model quality is a commodity. Every competitor has access to the same foundation models. What compounds over time is the context layer: what your system has seen, remembered, and learned. Intercom's advantage after nine months has nothing to do with which tool they use. Competitors can sign up tomorrow. They can't buy nine months of logged patterns and institutional memory. That gap compounds.

If you're building an AI product and you don't have a memory architecture, you're starting from zero every session. That's the ceiling.

---

### What to do this week

**Build the telemetry layer, not just the tool layer.** Start small: log every Claude Code interaction your team makes this week. What patterns repeat? What edge cases come up? Intercom's playbook is public, read the Lenny's piece, identify which of their instrumentation steps you can implement in a sprint. [Start here](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering).

**Audit your model costs by task, not total spend.** Open your LLM cost dashboard and break out spend by use case (generation vs. summarization vs. classification vs. coding). When Opus 4.8 ships, you'll know exactly which workflows to test first. Takes 2 hours to set up, saves you from a surprise 40% bill increase.

**Read the Mollick study before your next sprint planning.** It gives you the clearest calibration data available on what AI-assisted performance actually looks like, where it's reliable, where it varies, and what that means for how you estimate. [The original thread is here](https://x.com/emollick/status/2046362044786458648). Take 20 minutes before you set Q2 targets.
