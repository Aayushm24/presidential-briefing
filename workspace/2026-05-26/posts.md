# LinkedIn posts, 2026-05-26

**Lead:** AI agents are replacing human workers at scale, forcing a reckoning with how software teams should be structured and governed
**Briefing type:** pattern
**Best option:** 3 (pre-council self-score)

---

## OPTION 1, contrarian-philosopher (hook score: 8)

**Conviction:** The ClickUp workforce substitution isn't about replacing humans, it's about who designs the handoff between human judgment and agent execution

**Post:**

ClickUp replaced hundreds of employees with thousands of AI agents this week.

Everyone's asking: "Will agents replace me?"

Wrong question.

I see it across teams at Atlan and beyond. The real divide comes down to handoff design.

Teams either design the handoff or they don't.

ClickUp didn't just fire people and hire agents. They redesigned workflows so agents could own execution while humans owned oversight and judgment calls.

The difference matters.

When we build agents at Atlan, we don't replace roles. We split them:
- Jake (our AI SDR) handles chat qualification
- Humans handle complex deal negotiation
- Agents parse Demandbase signals
- Humans decide which accounts to pursue

That handoff design is what competitors can't copy.

Teams that skip this step get the worst of both worlds, agents that hallucinate on edge cases and humans who become agent babysitters.

Teams that nail it get superhuman execution with human wisdom at decision points.

The distinction becomes clearer when you see badly designed handoffs in action. Agents get stuck on exceptions they can't handle. Humans spend their day fixing agent mistakes instead of doing strategic work.

Well-designed handoffs create the opposite dynamic. Agents handle the predictable 80%. Humans focus their expertise on the complex 20% that determines outcomes.

The question everyone should be asking: "Where does human judgment matter most in my workflow?"

Because the teams figuring that out now will be the ones still here when the rest are scrambling to retrain their entire org.

What's the ugliest handoff in your current workflow?

---

## OPTION 2, data-point (hook score: 7)

**Conviction:** L1: Agent workflows are already replacing specialist teams in ways most builders haven't noticed, Felix's $20 hardware shows the infrastructure cost collapsed

**Post:**

Someone built an AI agent that runs on $20 hardware.

Felix Rieseberg (the Anthropic engineer behind Claude Code) built a physical "buddy" that listens to conversations, processes them through Claude, and responds with contextual LED signals.

Twenty dollars in hardware costs.

Unlimited agent processing capability.

Most teams I talk to are still thinking about AI as expensive cloud inference. Monthly bills, API limits, usage anxiety.

Felix flipped that assumption.

The hardware is negligible. The agent processing creates value that justifies dedicated devices for specific workflows.

His other workflows hit the same pattern:
- 3D house walkthroughs from floor plans (replaced specialist 3D teams)
- Automated promise tracking across email and Slack (replaced project coordinators)
- Full prospect research pipelines (replaced BDR manual work)

At Atlan, we've been building similar agent-first workflows for months. The pattern tracks.

The constraint was never compute cost. It was workflow design.

Teams that master agent-augmented roles don't just work faster. They work at scales that pure human effort cannot achieve.

The $20 buddy matters because it proves the infrastructure barrier evaporated.

Now it's just: do you know how to design workflows that compound?

What workflow in your company could run on $20 hardware if you redesigned it agent-first?

---

## OPTION 3, pattern-observation (hook score: 8)

**Conviction:** L3: The discipline gap around agent deployment is creating two tiers of builders, those who systematize testing/memory and those who accumulate regression debt

**Post:**

Everyone is shipping with coding agents.

Almost no one is doing it right.

The pattern repeats across every team I talk to:

Agents generate code faster than humans can review it. Teams skip systematic testing. Features work when first shipped but break unexpectedly during modifications.

Simon Willison calls it the discipline gap.

His solution: red/green TDD specifically for agent-generated code. Write failing tests first, let agents generate code that passes them, then write tests for edge cases.

The speed differential creates the problem. One agent outputs more code in an hour than a human reviewer can evaluate in a day.

Teams shipping agent-generated code without testing discipline are building maintenance nightmares.

ClickUp's workforce substitution works because they designed coordination at scale, thousands of agents with systematic oversight.

Felix Rieseberg's workflows compound because each agent interaction builds on tested, reliable foundations.

Google's 9-to-1 math performance over OpenAI matters less than whether your team can systematically deploy the reasoning capability.

IMO, the real competitive advantage goes to teams that establish memory architecture and testing discipline early.

Well-tested agent-generated code compounds into reliable systems.

Poorly tested agent-generated code compounds into technical debt that eventually forces complete rewrites.

At Atlan, we've learned the infrastructure choices determine whether agent productivity creates compounding advantages or compounding overhead.

What's your team's testing discipline for agent-generated code right now?
