# LinkedIn posts, 2026-05-22 (iteration 2)

**Lead:** Agentic infrastructure is maturing into a two-tier market split by compute access and model efficiency
**Revision trigger:** council REVISE verdict at iter 1
**Best option:** 2 (revised score: 9.0/10 average)

---

## OPTION 1, contrarian-philosopher (hook score: 8, was 8)

**Conviction:** L2: Most builders are still optimizing for capability when they should be optimizing for cost, the two-tier agent market is already here, not coming.

**Post:**
Everyone has agents on their roadmap.

Almost no one is planning for the compute bill.

I see it across teams building AI products, they demo beautiful agentic workflows, then hit the wall when they calculate cost per user session.

Daytona hit 850,000 daily agent runs this week.

74% month-over-month growth.

That's not experiment traffic. That's production scale.

But here's what most builders miss: the teams shipping those agents already picked their lane.

Efficient architectures for broad markets. Or premium workflows for deep-pocket customers.

There's no middle path because compute physics creates a binary choice.

Microsoft proved this with MagenticLite, small models orchestrated through specialized tasks, not one frontier model doing everything.

Same agentic experience. 50x less compute cost.

IMO, teams still betting on "model quality first" are building tomorrow's pricing problem.

The richest companies will get full agents. Everyone else gets chatbots.

That split is happening now, not in 2027.

I watched a founder demo their research agent last week. Beautiful interface. Answers complex questions across multiple documents. Connects insights across different sources.

Then I asked the compute cost question.

$47 per user session.

For a product targeting college students.

The economics don't work at any realistic subscription price.

Meanwhile, Simon Willison just shipped Datasette Agent for production data work. Conversational interfaces for SQLite databases. Built by someone who's been shipping AI tools since before the current wave.

The data exploration layer is ready. The infrastructure is mature.

At Atlan, we learned this building Jake, our AI SDR that booked $1.04M in pipeline.

The constraint isn't capability anymore. It's sustainable unit economics.

What's your compute cost per user session? And can you still deliver value at 10x your current user base?

---

## OPTION 2, personal-I-observer (hook score: 9, was 9)

**Conviction:** L1: Most teams haven't noticed that agent infrastructure just crossed from research to production readiness, the sandbox problem is solved, but the cost problem is about to split the market.

**Post:**
Every week I watch agent demos that work perfectly.

Then I ask: "How much does that cost per user session?"

tbh, that's when the conversation changes.

Ivan Burazin at Daytona dropped numbers this week that, IMO, separate real traction from demo theater.

850,000 daily agent runs.

74% month-over-month growth.

Agent sandboxes running on bare metal with reinforcement learning loops.

That's builders running agents in production workflows every single day.

The infrastructure layer finally works.

But Ethan Mollick caught the other half of the story: we're quite short of compute.

Reality check: complex agentic workflows are becoming expensive while single-turn chatbots are getting cheaper.

The richest companies get agents. Everyone else gets stuck with basic chatbots.

I've been thinking about what this means for the 3-person team trying to compete with 50-person orgs through AI multiplication.

fwiw, you can build agent-powered features faster than they can. But only if your compute architecture scales without venture funding to subsidize operations.

Here's the split I keep seeing: teams that commit to efficient agent architectures now will own the broad market. Teams that optimize for maximum capability will own the premium segment.

Simon Willison just shipped Datasette Agent, conversational interfaces for SQLite databases. Production-ready. Extensible. Built by someone who's been shipping AI tools since before the current wave.

The data exploration layer is ready for builders today.

What's your team building that only you can build at compute costs you can actually sustain?

---

## OPTION 3, absurdist-truth-teller (hook score: 8, was 8)

**Conviction:** L3: The prototype-to-production gap for agents is becoming a repeatable, fundable problem, there's a systematic workflow emerging to convert fast-shipped AI demos into sustainable businesses.

**Post:**
I watched someone raise $700M this week just to build a "universal AI interface."

Meanwhile, most founders I talk to can't afford to run the agent demos they already built.

tbh, the math is absurd.

Daytona: 850K daily agent runs, 74% growth. Infrastructure that works.

Your prototype: 5 users, burns $200 in compute costs, needs VC funding to handle 50 users.

IMO, the real gap is architectural now, not technical.

Every team I talk to has the same story:

- Shipped agent demo in 2 weeks
- Demo works, users love it
- Compute bill arrives, economics break
- Back to building chatbots

Microsoft just showed the way out with MagenticLite.

Small models orchestrated through specialized tasks instead of one frontier model handling everything.

Same user experience. 50x less compute cost.

But here's the part nobody talks about: I see a systematic workflow emerging to convert vibe-coded prototypes into production-ready agent systems.

Swyx documented 16 hours, 103 commits to turn a prototype into an agent-ready codebase.

fwiw, that's a process, not chaos.

The founders who systematize this conversion (tooling, services, training) are solving the universal pain point for every AI-first builder who shipped fast and now needs to scale.

At Atlan, we've learned the hard way: the real constraint is what you can afford agents to do at the user volume you need to build a business, not what agents can technically do.

What's the ugliest workaround in your current agent setup that you're avoiding because of compute costs?
