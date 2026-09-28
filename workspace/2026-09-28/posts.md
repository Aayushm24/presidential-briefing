# LinkedIn posts, 2026-09-28

**Lead:** Closed models pulled ahead in agentic AI while open models lag behind
**Briefing type:** pattern
**Best option:** 2 (pre-council self-score)

---

## OPTION 1, contrarian (hook score: 8)

**Conviction:** L2: The open-closed parity window has closed temporarily, and builders who ignore this will make architecture decisions they can't reverse.

**Post:**

open and closed models have the same benchmarks.

but one builds agents that work. the other doesn't.

Ethan Mollick called it: Fable/Astra class models are agentic in a way pre-Fable models aren't. Open models haven't crossed that line yet.

This isn't about MMLU scores.

It's about step 4 in a 7-step workflow.

Open models follow instructions. They write good code. They reason through problems step by step.

But when you chain those capabilities together into autonomous workflows, something breaks down.

They lose track of their original goal. Start optimizing for the wrong thing. Make assumptions that derail the entire process.

Closed frontier models hold their objectives longer.

They recover from errors without human intervention.

They distinguish between "the thing I was asked to do" and "the thing that would be impressive to do."

That distinction matters enormously when you're not watching every step.

The timing makes this worse.

This capability gap emerged just as the tooling around agentic AI matured. AsideAI browser solves anti-bot detection. Cursor makes it possible to delegate software development to AI.

The infrastructure exists to build reliable agent systems.

But only if you use the closed models.

Teams that bet on open model parity returning quickly face a different calculation today.

The agentic capabilities aren't just incrementally better in closed models. They represent a qualitative difference in how autonomous these systems can be.

What architecture decisions are you making this quarter that assume model parity?

---

## OPTION 2, personal-discovery (hook score: 9)

**Conviction:** L3: I've been tracking this capability gap in my own agent work, closed models maintain context and execute multi-step workflows where open models break down.

**Post:**

i've been tracking something builders have been feeling for months.

every open model i test can follow complex instructions. write good code. reason through problems step by step.

but when i chain those capabilities together into autonomous workflows, they break down around step 4 or 5.

the model loses track of its original goal.

starts optimizing for the wrong thing.

makes assumptions that derail the entire process.

when we build agents at Atlan, we don't have them click buttons. they call APIs, read from databases, talk to other apps through MCPs, and post results where we want them.

the humans never open the app when the agent is working.

but here's what i've noticed: closed frontier models don't just perform better on individual tasks.

they hold their objectives longer.

they recover from errors without human intervention.

they distinguish between "the thing i was asked to do" and "the thing that would be impressive to do" more consistently.

Garry Tan sees it too: "Opus 5.5 with Openclaw is strangely smarter and better at completing tasks than GPT-6 Astra."

the gap shows up most clearly in what researchers call "long-horizon planning."

open models excel at single-turn tasks where you can evaluate output immediately.

closed models excel at multi-turn tasks where the agent needs to maintain state across interactions, learn from mistakes, and adjust its approach.

teams making infrastructure decisions today are weighing known solutions that work now against unknown solutions that might work later.

for most builders, the rational choice is to build on the infrastructure that works and switch later if necessary.

but the switching cost won't be trivial.

what multi-step workflows are you trying to automate? and which models are you betting on?

---

## OPTION 3, absurdist (hook score: 7)

**Conviction:** L1: When you choose a closed model for agent work, you're not picking an API endpoint, you're committing to authentication systems and browser automation that will be hard to reverse.

**Post:**

choosing a model for your agent feels like picking a car.

really you're choosing a highway system.

when Garry Tan recommends running AsideAI browser "on a spare laptop you keep plugged in somewhere" so agents can use "your real credentials from a real Chromium," he's describing infrastructure.

not an API call.

agentic AI requires authentication management, sandbox environments, browser automation, credential storage, and audit logging.

these components integrate differently depending on which models you target.

closed model APIs come with built-in session management, rate limiting that accounts for multi-step workflows, and error handling designed for autonomous operation.

open model deployments require you to build all of that yourself.

the authentication problem illustrates this clearly.

many agent tasks require logging into services as the user. with closed models, you can use OAuth flows, API key rotation, and credential storage that the model provider validates and maintains.

with open models, you're managing credentials directly.

implementing your own OAuth flows.

handling token refresh without proven patterns to follow.

browser automation compounds the infrastructure complexity.

anti-bot detection has become sophisticated enough to break most headless browser solutions. the services agents need to interact with actively fight automated access.

AsideAI's approach works because it looks exactly like human usage patterns.

but integrating that approach with open models means building custom orchestration layers that don't exist yet.

teams making infrastructure decisions today aren't just weighing model capabilities.

they're weighing known solutions that work now against unknown solutions that might work later.

the switching cost won't be trivial.

agent systems develop implicit dependencies on specific model behaviors.

the error recovery patterns you build around Claude's failure modes won't work for Llama's failure modes.

what agent workflows are you planning to build? and which infrastructure are you committing to?
