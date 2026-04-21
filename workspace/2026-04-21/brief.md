# AI coding agents just proved they can 2x engineering velocity with real companies

[Intercom](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering) doubled their engineering throughput in 9 months using Claude Code skills and telemetry.

This isn't a demo or a benchmark. It's 100% of their engineers, plus designers and PMs, shipping measurable output gains with full quality tracking. The methodology is documented, the metrics are public, and the toolchain is available to any team. When a 500-person engineering org publishes specific velocity gains with named tools, that's the signal smart builders have been waiting for.

**Key takeaways:**
- AI coding agents now deliver consistent 2x productivity gains when implemented with proper telemetry and workflow structure (not just autocomplete)
- Economics research shows Claude Code and other agents produce near-human median results with less variance, giving founders calibration data for reliable performance expectations
- OpenAI's Codex acquisition proves real computer-use automation is shipping now, moving beyond coding into full system interaction
- Model cost patterns follow a sawtooth curve where efficiency gains get reset by accuracy improvements, making financial planning more complex
- Small teams with AI infrastructure can now outperform large traditional engineering organizations

### The measurement problem is solved

What I keep coming back to is how [Brian Scanlan](https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering) at Intercom built telemetry that actually tracks AI impact. They didn't guess at productivity. They measured merged PRs per R&D employee month over month. They built hooks that enforce engineering standards automatically. They created a skills repository where every Claude Code interaction gets logged and analyzed.

The result: 2x throughput with maintained code quality across their entire engineering org.

This solves the biggest blocker to enterprise AI adoption. CTOs couldn't justify the investment because they couldn't measure the return. Intercom just published the playbook. They instrumented everything, built culture around agent-first workflows, and gave every technical role access to shipping tools. Not just engineers, designers, PMs, and TPMs all cut code through Claude Code now.

The methodology matters more than the metric. Anyone can claim 2x velocity. Intercom showed their work. They tracked individual developer adoption rates, quality metrics, and output consistency. They built infrastructure that makes AI coding a skill, not a lucky accident.

This changes the game because you now have benchmarking data from a real company with real scale. No more guessing whether Claude Code will work at 100+ engineers. No more wondering if quality holds up under agent assistance. The evidence is public and replicable.

### Economics shows what agents reliably deliver

The [Ethan Mollick study](https://x.com/emollick/status/2046362044786458648) that replicated classic economics experiments with AI agents gives us even better calibration data. Claude Code and other coding agents consistently perform near the median of human teams, with lower variance in outcomes.

What that means in practice: if your human engineering team has wide performance spreads, AI agents compress that to more predictable delivery. If you have superstar 10x engineers, agents probably won't beat them. But if you have a normal distribution of talent, agents bring your floor up and your ceiling down to something more manageable.

The variance reduction is the real story. Human teams have unpredictable performance swings. Agents deliver consistent median performance. More predictable sprint planning, more reliable delivery estimates, fewer surprises in quarterly reviews.

Combined with Intercom's 2x velocity data, you get the full picture: agents don't just make good developers faster, they make all developers more consistent. That's a different kind of productivity gain than most founders expect.

### Real computer use is shipping now

[OpenAI's Codex acquisition](https://x.com/swyx/status/2046362691606855700) of Skybysoftware signals that computer-use automation is moving from research to production. Not just coding, full system interaction. Agents that click through UIs, manage databases, deploy infrastructure.

Swyx called this one of OpenAI's best deals of the year because it solves the "real computer use" problem that's been stuck in demos. When ChatGPT App gets computer vision plus system control, that's not just better coding assistance. That's agents that can manage your entire dev environment.

This connects directly to what Intercom discovered. Their biggest velocity gains came from agents handling deployment, testing, and integration tasks beyond writing code. When agents can interact with every tool in your stack, not just your IDE, that's when the 2x multiplier becomes possible.

The timing matters. Small teams with AI infrastructure can now compete with large engineering organizations. A 3-person team with Claude Code plus computer-use agents can potentially ship what took 25 engineers in 2022. The coordination cost collapse is real, and founders who see this early will build tomorrow's cost structure advantage.

What founders should update in their heads: the question is no longer whether AI will help with coding. It's whether your team will adopt agent-first workflows before your competitors do. The tools are proven, the methodology is documented, and the competitive advantage is available to whoever moves first.

---

### #2 Model costs follow a sawtooth pattern that breaks financial planning

[Tomasz Tunguz's analysis](https://x.com/ttunguz/status/2046277504797974700) of Opus 4.7's new tokenizer reveals why AI cost predictions keep failing. Model upgrades don't always reduce spend. They follow a sawtooth pattern where efficiency gains get erased by accuracy improvements.

When Opus 4.5 shipped, it was 40% cheaper to use than Sonnet despite being 67% more expensive per token. The smarter model used 76% fewer tokens to reach the same outcome. Every founder building on Claude got an instant cost reduction.

Then Opus 4.7 launched with a new tokenizer that breaks text into smaller pieces, forcing the model to pay closer attention to each word. Better instruction following, fewer coding mistakes, but 46% more tokens for the same content. The efficiency gain vanished.

This creates real financial planning problems. Founders budgeting AI costs can't assume that model upgrades will reduce spend. Sometimes they do, sometimes they make your bill 40% higher overnight. The pattern repeats across vendors: resolution improvements increase costs, efficiency improvements reduce them, in a sawtooth cycle.

What builders need to know: budget for cost volatility, not steady decreases. Track your token usage by task type, not just total spend. When a new model ships, test your highest-volume use cases immediately to understand the financial impact before it hits production scale.

---

### #3 Transformers tackle cancer trials with 95% failure rates

[Noetik's approach](https://www.latent.space/p/noetik) to clinical trial matching shows autoregressive transformers solving real-world problems with massive markets and quantified failure rates. 95% of cancer treatments fail to pass clinical trials, but Ron Alfa and Daniel Bear think it's a matching problem, not a drug problem.

They're applying the same transformer architecture that powers coding agents to match patients with trials more effectively. If clinical trial failure is mostly about finding the right patients for the right treatments, transformers trained on medical data can potentially flip those odds.

The business model is clear: pharmaceutical companies spend billions on failed trials. If Noetik can improve success rates by even 10 percentage points, the value is massive. This isn't abstract AI research, it's applying proven architectures to a market with clear demand and measurable outcomes.

What makes this relevant for builders: it shows how transformers trained for one domain (language, code) transfer to completely different problems (medical matching). The architecture is becoming a general-purpose problem-solving tool, not just a coding assistant.

---

### The thread connecting all three stories

Zoom out and today's three leading stories share one mechanism: context that persists and compounds.

Intercom's 2x velocity came from building a skills repository that logs every Claude Code interaction. The agent doesn't forget what worked. Each run is informed by the last 9 months of the team's patterns. That's not just faster coding, it's a learning system.

OpenAI acquired Skybysoftware specifically for state persistence. Computer use was already possible in research settings. The acquisition was about making it real in production, meaning agents that carry context between sessions. An agent that remembers your preferences and your history operates fundamentally differently than one starting fresh each time.

Noetik's core thesis is that 95% of cancer trials fail not because the drugs don't work, but because they can't find the right patients. The fix is contextual matching: transformer models trained to connect patient records with trial criteria at scale. Again, the value is in retained, accumulated knowledge, not raw inference speed.

The pattern matters for anyone building on AI infrastructure right now. Model quality is a commodity. Every competitor has access to the same foundation models. What compounds over time is the context layer: what your system has seen, remembered, and learned from users. Intercom's advantage after 9 months isn't Claude Code access. It's 9 months of logged interactions that made their agents smarter than a fresh install. That's the thing competitors can't copy by signing up for the same tool.

If you're building an AI product and you don't have a memory architecture, you're starting over every session. That's the ceiling.

---

### What to do this week

**Test agent workflows in your dev environment.** Don't wait for perfect tools. Start with Claude Code and document everything you automate. Intercom's 2x gains came from building culture around agent-first workflows, not from having better tools than everyone else. Time investment: 4-6 hours to set up basic telemetry and team access.

**Budget for model cost volatility.** Review your AI spend by use case and model. Create cost alerts for 40% monthly increases. When Opus 4.8 or GPT-5 ships, you want to know the financial impact within days, not weeks. Time investment: 2-3 hours to set up tracking dashboards.

**Hire for agent collaboration, not just coding skill.** The next technical hire should be comfortable with AI pair programming and agent-assisted workflows. Traditional coding interviews miss this entirely. Consider adding an agent collaboration exercise to your technical interviews. Time investment: 1 hour to design the interview component.
