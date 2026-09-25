# LinkedIn posts, 2026-09-25

**Lead:** AI agents are moving from capability demos to real-world deployment infrastructure
**Briefing type:** pattern
**Best option:** 1 (pre-council self-score)

---

## OPTION 1, contrarian-philosopher (hook score: 8)

**Conviction:** L2: Teams building coding agents think they're solving the capability problem, but they're actually creating a deployment complexity problem that overwhelms most organizations.

**Post:**

Every team I talk to wants coding agents.

Almost none of them should build one.

Simon Willison spent months working with coding agents and reached an uncomfortable truth: they make software engineering harder, not easier.

I see it across my network. Teams shipping with identical models, but getting wildly different outcomes.

The difference comes down to operational overhead.

Coding agents demand extraordinary discipline:
- prompt engineering becomes a core skill
- output validation becomes constant
- error handling becomes complex debugging
- human-agent coordination becomes its own workflow

At Atlan, we've been building agents for months and this tracks.

The magical demos everyone shares? Those work.

The teams that deploy them successfully? They invest heavily in agent operations as a distinct engineering discipline.

Most teams skip that investment. They assume the agent handles the complexity.

It doesn't.

The agent creates new categories of complexity that traditional software engineering doesn't prepare you for.

VMware just shared what changes when agents move from developer laptops to enterprise environments: everything.

Identity management. Access controls. Audit logs. Sandboxing. Monitoring. Failure recovery.

Every capability that works on localhost becomes an infrastructure problem at scale.

The capability paradox is real.

Teams that successfully deploy coding agents treat them like high-maintenance power tools, not autonomous coworkers.

They build custom toolchains around the agents. They train engineers to think like AI operators.

Success depends on operational sophistication, not just model access.

What's the ugliest workaround in your current agent setup?

---

## OPTION 2, absurdist-truth-teller (hook score: 7)

**Conviction:** L1: Most builders are treating coding agents like magic when they're actually complex distributed systems that require infrastructure thinking.

**Post:**

GPT-6 Astra just ascended in Nethack on its third attempt.

For context: most human players never ascend despite years of trying.

Nethack is famously the hardest game ever made. 50+ dungeon levels. Thousands of decision points. Strategic planning across massive time horizons.

And an AI just beat it in three tries.

So clearly, coding agents are ready for production, right?

Wrong.

Here's what makes this absurd.

The same AI that can plan 10,000 moves ahead in a game breaks when you ask it to deploy to staging.

It can navigate complexity that humans can't even comprehend. But it can't handle a merge conflict without human supervision.

The capability demonstration is extraordinary. The deployment reality is brutal.

I watch this happen every week. Teams see frontier model capabilities and assume agent deployment is solved.

It's not.

The LLM handles game complexity fine. Context management, state persistence, error recovery, and human handoff protocols remain the hard parts.

The infrastructure requirements that nobody talks about:
- agent build packs that package logic with runtime dependencies
- MCP gateways for authentication and authorization
- shared memory systems for agent coordination
- monitoring and debugging tools for agent behavior

At Atlan, when we build agents, we spend more time on the operational layer than the agent logic itself.

The Nethack ascension proves long-horizon planning works in structured environments with clear rules and observable feedback loops.

Most enterprise workflows are the opposite of that.

The teams building production agents successfully have solved the deployment problem, not just the capability problem.

The rest are still building demos.

Did you try GPT-6 yet? I'm curious how it handles your actual workflow, not just the benchmark.

---

## OPTION 3, relatable-human (hook score: 7)

**Conviction:** L3: Human-agent collaboration requires new workflow primitives that most teams haven't designed yet.

**Post:**

I build AI agents at Atlan for a living.

And I'm terrible at working with them.

Last week our engineering team was debugging why our AI SDR kept losing context between chat sessions.

Thirty minutes of investigation later: I was passing everything inline instead of using persistent memory.

I blamed the model. It was my workflow design.

This is the thing nobody wants to admit about coding agents.

They don't make you a better engineer automatically. They make engineering different.

And most of us haven't adapted to that difference yet.

Ando just launched a team messaging platform where agents get their own profiles, inboxes, and conversation histories.

They participate in group chats alongside humans.

It sounds simple. It's actually a fundamental shift in how work gets done.

Instead of humans using tools, humans and agents work together as peers.

New workflow patterns emerge:
- agents handle routine tasks while humans focus on creative work
- teams delegate research and data processing to agents
- humans maintain oversight and decision authority

But collaboration also creates new failure modes:
- agents misunderstand context
- agents make incorrect assumptions
- agents drift from assigned tasks

At Atlan, we've learned that effective human-agent collaboration requires explicit role definition and systematic feedback mechanisms.

Teams that treat agents as autonomous coworkers fail.

Teams that integrate agents into structured workflows with human oversight succeed.

The companies building these tools aren't just solving technical problems. They're designing new forms of work.

What workflow would you redesign completely if you had an agent as a permanent team member?

p.s. honestly, most of our agent debugging time goes to fixing my assumptions about what the agent "should" know
