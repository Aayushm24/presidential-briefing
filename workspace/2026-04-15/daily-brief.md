# Daily Brief — 2026-04-15

**Lead:** Not all AI agents are created equal

# The Agent Reality Check Is Here

**April 15, 2026**

Here's the pattern: AI agents are the hottest category in software right now, and the people actually building them are telling you, loudly, that it's way harder than anyone expected. Not "hard" in the fun, intellectually stimulating way. Hard in the "we rebuilt this five times and it still breaks on tasks longer than a few steps" way.

Three stories landed in the last 24 hours that, taken together, paint a very clear picture. A widely shared framework for why most teams can't even prioritize their agent backlogs correctly. A candid postmortem from Notion's cofounder about what it actually cost to ship agent features in production. And a new research benchmark showing, with data, exactly where and why agents fall apart as tasks get more complex.

The through-line: the gap between demo-quality agents and production-quality agents is not a gap. It's a canyon. And the teams that will win are the ones building honest internal frameworks for understanding their agents' limitations, not the ones optimizing for impressive demos.

Let me walk through the evidence.

---

## Evidence 1: Most teams can't even compare their agent ideas properly

Hamza Farooq and Jaya Rajwani, who teach two of the most popular AI agent courses (Agent Engineering Bootcamp and Agentic AI for PMs), published a framework on Lenny's Newsletter that cuts right to the core problem. They've had the same conversation "at least 30 times" with AI leaders: someone shows up with 5 to 10 agent initiatives on a roadmap and asks which to build first.

The list always looks similar. A PM assistant. A RAG copilot. A customer support system. A code review agent. A voice-enabled shopping assistant. And teams try to compare them using the same impact-vs-effort matrix they'd use for any product feature.

This doesn't work. And the reason it doesn't work is the important part.

One agent might take six weeks and cost $500/month to run. Another might take six months and generate a six-figure annual LLM bill. One can be assembled by a product manager using n8n (a workflow automation tool). Another requires a dedicated ML engineering team. These are not the same category of thing, even though everyone calls them all "agents."

Farooq and Rajwani's framework, built from work with Fortune 500 companies including Jack in the Box, Tripadvisor, and The Home Depot, groups agent initiatives into three tiers based on their underlying architecture. The specifics of the tiers matter less than the insight: **you cannot prioritize agent work until you first categorize it.** Teams that skip this step end up comparing "apples, oranges, and jet engines on the same spreadsheet," as they put it.

This connects to something we've been tracking for the past week. The agent layer is bifurcating. Generic agents are getting commoditized by platform players like Microsoft. Domain-specific agents with real operational ownership are where defensible value lives. But you can't make that strategic choice if you don't even have a shared vocabulary for what kind of agent you're actually proposing to build.

The real takeaway: if your team has a backlog of agent ideas and you're treating them all as comparable line items, you're almost certainly going to waste your first few months of engineering time on the wrong thing.

---

## Evidence 2: Notion rebuilt their agent system five times

This one is the most revealing.

Simon Last (Notion's cofounder) and Sarah Sachs (head of AI) went on the Latent Space podcast and gave what might be the most honest account I've seen of what it takes to ship AI agents inside a real product used by millions of people.

The headline numbers: **5 rebuilds. 100+ tools.** And this is Notion. A $10B+ company with world-class engineering talent, deep context on their own product, and every reason to get this right quickly. They started building AI tooling before ChatGPT launched. Their first agent attempts failed because there was no tool-calling standard, context windows were too short, and the models simply weren't reliable enough.

They went through the full journey: early failed tool-calling experiments in 2022, building agent harnesses, figuring out progressive tool disclosure, using meeting notes as a data capture mechanism, and eventually landing on their Custom Agents feature that was teased at their last Make conference.

Let me be specific about what "5 rebuilds" means in practice. It means that a team of very smart people, with direct access to the best foundation models, built something that worked in testing, shipped it or tried to ship it, discovered it didn't work well enough in production, and went back to fundamentally rethink the architecture. Not once. Not twice. Five times.

This is not a story about incompetence. This is a story about the state of the technology. The gap between "this works in a demo" and "this works reliably for millions of users across thousands of different knowledge-work contexts" is enormous. And it's not a gap you can see clearly until you've shipped and watched real users interact with your system.

The podcast also gets into the MCP vs. CLI debate, pricing decisions, org design, and their long-term vision for "software factories." But the core lesson is simpler: **budget for multiple rebuilds.** If Notion needed five, you probably need at least three.

---

## Evidence 3: New research quantifies exactly where agents break

A team from UW-Madison, UC Berkeley, and other institutions (Xinyu Jessica Wang, Haoyue Bai, and collaborators) published a paper called "The Long-Horizon Task Mirage?" that does something the industry desperately needs: it systematically diagnoses where and why agentic systems fail as tasks get longer and more complex.

They built a benchmark called HORIZON, collected 3,100+ trajectories across four representative agentic domains, and tested state-of-the-art agents from multiple model families, including GPT-5 variants and Claude models.

The findings confirm what practitioners have been feeling but couldn't prove rigorously. LLM agents perform strongly on short and mid-horizon tasks. But they "often break down on long-horizon tasks that require extended, interdependent action sequences." The key phrase there is "interdependent." It's not just that agents struggle with long task lists. They struggle specifically when step 7 depends on the outcome of step 3, and step 12 depends on both.

The paper introduces a "trajectory-grounded LLM-as-a-Judge pipeline" for diagnosing failures in a scalable way. In plain English: they built a systematic method for figuring out exactly which step in a multi-step agent task went wrong and why. This is directly actionable. If you're building agents and you don't have a systematic failure diagnosis process, you're flying blind.

Here's why this matters beyond academia. The most common pitch for AI agents right now is some version of "it handles the whole workflow end to end." That's the value proposition. But the research shows that "end to end" is precisely where current agents are weakest. The longer the chain of dependent actions, the more likely something breaks. And when something breaks in step 4 of a 15-step process, the agent doesn't gracefully degrade. It confidently continues down the wrong path.

This is the "mirage" in the paper's title. Agents look capable because they nail the short tasks. Buyers and investors extrapolate from those demos to assume the agent can handle the complex, multi-step workflows that actually deliver business value. But the extrapolation doesn't hold.

---

## How these three stories connect

Take a step back and look at what these three pieces are saying together:

1. **Teams can't even properly categorize their agent initiatives** (Farooq/Rajwani), which means they're making investment decisions based on flawed comparisons.

2. **Even the best teams need multiple full rebuilds** (Notion), which means timelines and budgets based on "build it once" assumptions are fantasy.

3. **Agents systematically fail on the complex tasks that justify their existence** (HORIZON benchmark), which means the core value proposition of most agent products is built on shakier ground than demos suggest.

The pattern is clear: **production agent development is in a phase where honest assessment of limitations is more valuable than impressive capability claims.**

This doesn't mean agents aren't real or valuable. Notion shipped their Custom Agents feature. It works. Companies like Jack in the Box and Tripadvisor are deploying agents that deliver measurable results. The HORIZON benchmark shows agents performing well on short and medium tasks. There's real value being created.

But the value is being created by teams that are brutally honest about what their agents can and can't do, that build systematic processes for diagnosing failures, and that budget for the reality that their first (and second, and third) architecture probably won't survive contact with production users.

---

## What this means if you're building

**If you're a founder pitching an agent product:** Investors who've read any of this material are going to ask harder questions. "How many rebuilds have you done?" is becoming a credibility signal, not an embarrassment. If you say "we got it right the first time," that's a red flag. If you say "we've rebuilt the core loop three times and here's what we learned each time," that's a signal you actually understand the problem.

**If you're a CTO prioritizing agent initiatives:** Use a categorization framework before you touch an impact/effort matrix. Not necessarily Farooq and Rajwani's specific framework, but something that forces you to acknowledge that your customer support chatbot and your multi-step workflow automation agent are fundamentally different kinds of projects requiring different teams, timelines, and budgets.

**If you're an engineering team building agents:** Invest in failure diagnosis infrastructure before you invest in new capabilities. The HORIZON paper's approach of systematic trajectory analysis is the right idea. You need to know exactly where your agent breaks and why, not just that it "sometimes gets things wrong." The teams that build the best internal tooling for understanding agent failures will iterate faster than the teams that build the flashiest demos.

**If you're buying agent products from vendors:** Ask to see failure rates on tasks with more than 5 interdependent steps. Ask what happens when the agent gets stuck. Ask how many times the product has been fundamentally rebuilt. The answers will tell you whether you're buying a production system or a demo.

The honest truth is that we're in the "it's harder than it looks" phase of agent development. This phase is uncomfortable but necessary. The companies that emerge from it with real, reliable agent products will have enormous advantages. But getting there requires accepting that the current state of the art has real, well-documented limitations, and building your roadmap around that reality rather than around the version of agents that looks great in a 3-minute demo.

---

## Also worth satisfying

### Vibe-coding apps are learning that Apple controls the door

Anything, a vibe-coding app that lets non-developers build mobile apps using natural language, has been kicked off the Apple App Store twice. Replit and Vibecode have also had updates paused.

The core issue: Apple doesn't love apps that let users create and distribute other apps, because it undermines Apple's control over what runs on iOS. Anything's cofounder Dhruv Amin says the app was primarily for letting users preview their own apps on their own devices during development. Apple apparently didn't see it that way.

Anything is now pivoting to a desktop version as a workaround. This is the right move tactically, but the strategic lesson is bigger: **if your AI product's core distribution channel is someone else's app store, you have a platform dependency problem that no amount of product quality can solve.** This isn't new wisdom (ask any game developer who's been at the mercy of Steam or the App Store), but it's hitting the AI app wave for the first time.

For founders building AI-powered app creation tools: plan your desktop/web strategy from day one. Don't treat mobile as your primary distribution channel unless you've gotten explicit guidance from Apple's review team that your use case is acceptable. "No problems through December" followed by removal in March is exactly the kind of rug-pull that kills startups.

---

### Anthropic is making OpenAI's investors nervous

This one is significant. According to the Financial Times, some of OpenAI's own investors are getting second thoughts about the company's $852 billion valuation. The reason has a name: Anthropic.

The numbers tell the story. Anthropic's annualized revenue jumped from $9 billion at the end of 2025 to $30 billion by the end of March 2026. That's more than tripling in a quarter, driven largely by demand for coding tools. One investor who has backed both companies told the FT that justifying OpenAI's round required assuming an IPO valuation of $1.2 trillion or more. Meanwhile, Anthropic's current $380 billion valuation is starting to look like the better deal.

On the secondary market, demand for Anthropic shares has become "nearly insatiable" while OpenAI shares are trading at a discount.

What's actually happening here: **the market is repricing the assumption that OpenAI would be the dominant AI lab.** Anthropic's coding tools (Claude Code and related products) have found extraordinary product-market fit with developers and enterprises. OpenAI is "scrambling to reorient itself around enterprise customers," which is a polite way of saying their consumer-first strategy hasn't produced the kind of revenue growth that justifies their valuation.

For founders, this matters in two ways. First, if you're building on top of either company's APIs, the competitive dynamics between them are actually good for you. Both labs are aggressively courting developers and enterprises, which means better pricing, better tools, and more willingness to support your use case. Second, if you're raising money, be aware that investor sentiment around AI valuations is shifting. The "just add AI" premium is compressing. Investors are starting to differentiate between companies with real revenue traction and companies with impressive demos. Sound familiar?