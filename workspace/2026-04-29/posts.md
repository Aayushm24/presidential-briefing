# LinkedIn posts, 2026-04-29

**Lead:** All AI-at-work research became obsolete this week
**Briefing type:** pattern
**Best option:** 2 (pre-council self-score)

---

## OPTION 1, contrarian-philosopher (hook score: 8)

**Conviction:** Any ROI model or workflow design built on pre-2026 AI-at-work data is now unreliable, builders should treat agentic patterns as the new baseline to design around.

**Post:**
Every productivity study on AI at work just became wrong.

Ethan Mollick called it directly: all the research everyone cites predates agentic AI.

The timing matters more than most founders realize. Every McKinsey report measuring AI impact comes from the era of autocomplete and chat interfaces. Before Claude Code shipped agents that run for 8 hours without human intervention. Before teams used Cursor to rebuild entire codebases overnight.

The productivity gains from those patterns are orders of magnitude beyond what researchers measured when they studied ChatGPT helping someone write emails faster.

This creates a dangerous blind spot for builders. You pitch investors with data showing 20% productivity gains from AI writing assistance. Your competitor ships an agent that eliminates entire categories of manual work.

Which pitch wins Series A funding?

At Atlan, we've been building agents for months and the results can be magical. But the mental models people use to think about AI at work come from the pre-agentic world.

Managers plan around humans-with-AI instead of AI-systems-with-human-oversight.

Product teams build features instead of autonomous capabilities.

Engineering teams optimize latency instead of long-horizon reliability.

What changed everything was reliability at time horizons that matter. Pre-2026 AI tools worked for tasks measured in minutes. Agentic AI works for tasks measured in hours or days.

That shift breaks every assumption about how work gets structured.

IMO, any ROI model or workflow design built on pre-2026 data is now unreliable. The teams that realize this early will redesign their tools around agent patterns while competitors are still optimizing chat interfaces.

What does your team's AI strategy assume about human involvement?

---

## OPTION 2, absurdist-truth-teller (hook score: 7)

**Conviction:** Running long-horizon coding agents in sandboxes with skip permissions is the pattern every AI engineering team should adopt immediately.

**Post:**
Running coding agents for 8 hours without skip permissions.

Simon Willison nailed the pattern that makes long-horizon agents actually work: run them in environments where mistakes don't matter. Give them skip permissions so they don't halt on every file operation.

This is immediately actionable advice for every AI engineering team.

The sandbox pattern solves what was the reliability bottleneck for coding agents. When an agent couldn't modify files, it would stop and ask permission hundreds of times per hour. When it could modify files freely, teams would lose confidence after the first system break.

Skip permissions in a sandbox environment means the agent operates at machine speed while the blast radius stays contained.

You get the productivity gains of autonomous execution without the risk of system damage.

This pattern is spreading beyond coding:
- Document processing agents run in isolated storage buckets
- Customer service agents operate in test environments before touching live systems
- Infrastructure agents work in staging with full system privileges

The result is AI systems that work more like utilities than tools.

You give them goals, not step-by-step instructions. They run until completion, not until the next human checkpoint.

The productivity implications are massive because the bottleneck shifts from human attention to system capacity.

Teams that adopt this pattern report engagement changes that go beyond efficiency. Engineers who were hesitant about AI tools start using them daily after seeing 8-hour autonomous sessions that actually ship features.

The time compression is brutal for competitors who still operate on traditional cycles.

While they're scheduling follow-up meetings to discuss requirements, teams using sandboxed agents are shipping iterative improvements to working systems.

What's the ugliest workaround in your current agent setup?

---

## OPTION 3, personal-observer (hook score: 8)

**Conviction:** Teams building AI into their operational backbone operate faster than teams using AI as an external tool, the advantage compounds.

**Post:**
I've been watching meeting dynamics change overnight.

Ethan Mollick suggested a simple tactic that transforms everything: build the thing you're talking about in the meeting during the meeting using Claude Code or Cursor.

Every week I see the same pattern.

Traditional meetings end with action items and follow-up tasks. AI-native meetings end with working prototypes and immediate feedback loops.

The psychology matters as much as the productivity. When someone says "we should build a dashboard that shows X" and you build it while they're talking, the conversation shifts from whether to build it to how to improve what already exists.

Teams that adopt this pattern report engagement changes that go beyond efficiency. Engineers who were hesitant about AI tools start using them daily after seeing live coding sessions.

At Atlan, we've learned that shipping agents fast and fixing them publicly beats shipping perfectly.

The AI-skeptical team members can't dismiss something they just watched work.

GitHub's MCP server provides the infrastructure patterns teams need to wire agents into development workflows. Instead of using AI for one-off tasks, teams build AI into their operational backbone.

Agents handle routine code reviews, generate documentation from code changes, update project tracking based on commit patterns, and surface blockers before they delay releases.

The compound effect builds over weeks and months.

Teams with AI wired into their core workflows operate faster than teams using AI as an external tool. The advantage compounds because every process improvement makes the next improvement easier to implement.

The time compression is brutal for competitors who still operate on traditional cycles.

While they're scheduling follow-up meetings to discuss requirements, AI-native teams are shipping iterative improvements to working systems.

I doubt we're optimizing for the right metrics anymore. The question shifted from "how much faster can humans work with AI" to "how much work can happen without human intervention."

What does your team remember from last sprint's AI experiments?
