# LinkedIn posts, 2026-06-03

**Lead:** GitHub preps the platform for agents as 85 million developers meet their agentic future
**Briefing type:** pattern
**Best option:** 2 (pre-council self-score)

---

## OPTION 1, contrarian (hook score: 8)

**Conviction:** L2: The platform wars aren't about models anymore, they're about who controls the development workflow when agents become teammates.

**Post:**

GitHub's biggest challenge has moved past Copilot competition.

85 million developers don't know agents are about to break their platform.

Every week I watch teams hit GitHub's API limits when their agents start doing real work.

The problem sits with the platform. GitHub was built for humans who open one pull request, wait for review, then merge.

Agents spawn 20 workstreams simultaneously. They coordinate changes across multiple repos. They need authentication schemes that don't exist and rate limits that assume human usage patterns.

Kyle Daigle laid this out on Latent Space: GitHub is rebuilding core infrastructure because agents operate in completely different patterns than humans.

At Atlan, when we build agents, we don't have them click buttons. They call APIs, read databases, and coordinate through MCPs. But GitHub's current architecture creates artificial bottlenecks that slow everything down.

The technical implications run deep:
- Authentication for agents acting with delegated authority
- Rate limits that distinguish agent workflows from abuse
- Permissions that span organizational boundaries

GitHub is preparing for a fundamental shift.

Making GitHub work when half your development team are autonomous agents.

Microsoft gets this. They're building MAI-Code-1-Flash specifically for VS Code integration in ways external models can't match.

The pattern is platform control over pure performance.

What happens when your agents can't ship because they broke your git workflow?

---

## OPTION 2, data-point (hook score: 9)

**Conviction:** L1: Uber burning through their entire annual AI budget in 4 months is every CTO's wakeup call about consumption economics vs software licensing.

**Post:**

Uber capped employee AI usage after burning through their annual budget in 4 months.

Every CTO I talk to just felt their stomach drop.

The math looked simple during pilot programs: 50 employees testing Claude Code for 3 months, $10,000 in tokens. Scale to 29,000 employees = $1.9M annual budget.

But real adoption curves don't scale from pilot data.

The top 10% of power users discovered AI workflows that 10x their output. Instead of occasional code completion, they built entire features using AI pair programming. Instead of one-off documents, they created AI-powered content pipelines.

Usage exploded because AI actually works well enough to use daily now.

The budget shock is hitting everywhere:
- Google's own employees adopting internal AI tools
- Meta's teams burning tokens at unpredicted rates
- Microsoft facing similar explosions quarterly

Most executives still think about AI costs like software licenses: predictable per-seat pricing that scales linearly with headcount.

But AI operates on consumption economics that scale with usage intensity, not user count.

At Atlan, we track AI spending alongside productivity metrics: features shipped per token, pipeline value per dollar spent. The ROI is there, but you need visibility before the budget explodes.

The governance challenge is immediate. Cap per employee? You punish high performers. Cap per team? Teams game the system. Productivity-based allocation? Most companies can't measure knowledge worker output accurately enough.

Uber chose hard caps: maximum AI spending per employee per month. Crude but implementable immediately.

What's your plan when your team's AI usage suddenly jumps 5x because they found workflows that actually work?

---

## OPTION 3, pattern-observation (hook score: 8)

**Conviction:** L3: The three-layer AI stack is consolidating around platform control, not performance, GitHub controls workflow, Microsoft controls tools, Cohere controls compliance.

**Post:**

Three announcements this week connect into one pattern.

GitHub rebuilding for agents. Microsoft building MAI models in-house. Cohere targeting regulated enterprises with Command A+.

Each represents a different layer consolidating around platform control rather than pure performance.

GitHub is rebuilding collaboration primitives that agents need. Authentication, rate limiting, permissions for systems that spawn multiple workstreams and coordinate across repos simultaneously.

Microsoft isn't chasing the parameter arms race. MAI-Code-1-Flash has just 137B parameters but integrates with VS Code in ways external models can't replicate. The advantage comes from platform integration, not model capability.

Cohere's Command A+ doesn't beat GPT-4 on benchmarks. But it's the only option for enterprises that can't use cloud AI due to regulatory constraints. They win by solving deployment problems, not building better models.

The pattern: AI competition is shifting from model capabilities to platform control.

Pure model providers risk getting squeezed between platform companies above and hardware providers below.

At Atlan, this changes our evaluation framework. We pick AI tools based on platform integration and deployment requirements, not just model performance.

The best model that doesn't integrate with your workflow is worse than a good model that does.

This means:
- Evaluate based on where the tool fits in your stack
- Consider switching costs, not just performance metrics
- Platform lock-in matters more than benchmark scores

The companies winning AI deployments control critical infrastructure layers: development tools, deployment infrastructure, or compliance frameworks.

Which layer of your AI stack do you actually control?
