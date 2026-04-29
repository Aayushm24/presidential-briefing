# All AI-at-work research became obsolete this week

[Ethan Mollick](https://x.com/emollick/status/2049188184135782899) called it directly: every productivity study on AI at work predates agentic AI.

This shift creates a window where builders either redesign their tools around agent patterns or watch their competitors ship systems that make traditional AI features look ancient. The pre-agentic data everyone cites to pitch investors, plan roadmaps, and set pricing assumptions just expired. What I keep coming back to is how few founders realize this yet.

**Key takeaways:**
- All productivity research on AI predates long-running agents, making current ROI models and workflow assumptions unreliable for 2026 planning
- Sandboxed agent execution with skip-permissions eliminates the reliability barrier that kept coding agents from 8-hour autonomous runs
- Live coding during meetings using Claude Code or Codex shifts team dynamics from talking to building, accelerating adoption timelines
- GitHub's MCP server provides production-ready patterns for wiring AI agents into development workflows today
- Mobile vibe-coding signals no-code AI tools are competing for mindshare beyond desktop environments

### Every benchmark study just became wrong

[Ethan Mollick's observation](https://x.com/emollick/status/2049188184135782899) cuts straight through the noise: "A big problem with all AI at work punditry right now is that it all rests on data from the pre-agentic era (which is basically just now ending) and we have very little information about what has been happening since the Claude Code moment."

The timing matters more than most founders realize. Every study measuring AI impact on knowledge work comes from the era of autocomplete and chat interfaces. Think about what changed in the past six months alone. Claude Code ships agents that run for hours without human intervention. Teams use Cursor to rebuild entire codebases overnight. Agents coordinate with each other to complete complex workflows.

The productivity gains from those patterns are orders of magnitude beyond what researchers measured when they studied ChatGPT helping someone write emails faster.

This creates a dangerous blind spot for builders. You pitch investors with McKinsey data showing 20% productivity gains from AI writing assistance. Your competitor ships an agent that eliminates entire categories of manual work. Which pitch wins Series A funding?

The evidence gap runs deeper than just measurement problems. The mental models people use to think about AI at work come from the pre-agentic world. Managers plan around humans-with-AI instead of AI-systems-with-human-oversight. Product teams build features instead of autonomous capabilities. Engineering teams optimize latency instead of long-horizon reliability.

What changed everything was reliability at time horizons that matter. Pre-2026 AI tools worked for tasks measured in minutes. Agentic AI works for tasks measured in hours or days. That shift breaks every assumption about how work gets structured.

### Sandboxes solved the biggest agent problem

[Simon Willison](https://x.com/simonw/status/2049138029017833635) shared the pattern that makes long-horizon coding agents actually work: "I can't imagine any way of running a coding agent for 8 hours without skip perms - the trick is to run it in a sandbox where mistakes don't matter."

This is immediately actionable advice. Every AI engineering team should adopt this pattern today. Run your agents in environments where they can break things without consequences. Give them skip permissions so they don't halt on every file operation. Design the system assuming the agent will make mistakes and making those mistakes recoverable.

The sandbox pattern solves what was the reliability bottleneck for coding agents. When an agent couldn't modify files, it would stop and ask permission hundreds of times per hour. When it could modify files freely, it would eventually break something critical and teams would lose confidence.

Skip permissions in a sandbox environment means the agent operates at machine speed while the blast radius stays contained. You get the productivity gains of autonomous execution without the risk of system damage.

This pattern is spreading beyond coding. Document processing agents run in isolated storage buckets. Customer service agents operate in test environments before touching live systems. Infrastructure agents work in staging environments with full system privileges.

The result is AI systems that work more like utilities than tools. You give them goals, not step-by-step instructions. They run until completion, not until the next human checkpoint. The productivity implications are massive because the bottleneck shifts from human attention to system capacity.

### Meeting dynamics changed overnight

[Ethan Mollick suggested](https://x.com/emollick/status/2048981050051715090) a simple tactic that changes everything: "An easy way to get a team engaged with AI is just to build the thing you are talking about in the meeting during the meeting using Codex or Claude Code."

This works because it eliminates the gap between deciding and building. Traditional meetings end with action items and follow-up tasks. AI-native meetings end with working prototypes and immediate feedback loops.

The psychology matters as much as the productivity. When someone says "we should build a dashboard that shows X" and you build it while they're talking, the conversation shifts from whether to build it to how to improve what already exists. The AI-skeptical team members can't dismiss something they just watched work.

Teams that adopt this pattern report engagement changes that go beyond efficiency. Engineers who were hesitant about AI tools start using them daily after seeing live coding sessions. Product managers begin prototyping ideas directly instead of writing specifications. Marketing teams build landing pages during campaign planning meetings.

The time compression is brutal for competitors who still operate on traditional cycles. While they're scheduling follow-up meetings to discuss requirements, AI-native teams are shipping iterative improvements to working systems.

[GitHub's MCP server](https://x.com/swyx/status/2048986073200738584) provides the infrastructure patterns teams need to wire agents into development workflows. The walkthrough shows exactly how to connect AI agents to GitHub repositories, issue tracking, and code review processes.

This infrastructure layer is where the real productivity gains accumulate. Instead of using AI for one-off tasks, teams build AI into their operational backbone. Agents handle routine code reviews, generate documentation from code changes, update project tracking based on commit patterns, and surface blockers before they delay releases.

The compound effect builds over weeks and months. Teams with AI wired into their core workflows operate faster than teams using AI as an external tool. The advantage compounds because every process improvement makes the next improvement easier to implement.

### Distribution patterns are evolving fast

[Lovable's mobile launch](https://techcrunch.com/2026/04/28/lovable-launches-its-vibe-coding-app-on-ios-and-android/) signals that no-code AI builders are expanding beyond desktop environments. The app allows developers to build web applications from their phones using natural language descriptions.

This expansion matters because it changes when and where people build software. Desktop-only tools compete for focused work time at computers. Mobile tools compete for idle time everywhere else. A founder who can prototype an idea during a commute or build a feature while waiting for coffee has more iteration cycles than someone tied to a workstation.

The pattern reflects broader infrastructure maturity. Mobile development used to require specialized native toolchains. Cloud platforms made deployment simpler. AI makes the actual building accessible to non-programmers. Each layer reduces the barriers to software creation.

Teams building AI development tools should watch this expansion carefully. The winners will be those that meet users where they are, not where traditional software development happened. That might mean mobile interfaces for quick prototyping, voice interfaces for hands-free coding, or collaborative interfaces that work across different devices and contexts.

What I find interesting is how distribution advantages compound in AI tools. Lovable users don't just get mobile access to vibe-coding. They get mobile access to something that works better than desktop alternatives for certain use cases. When an AI tool is genuinely easier to use on a phone than on a computer, the distribution advantage becomes a product advantage.

---

### #2 The subsidy era just ended

The [AI Daily Brief](https://aidailybrief.beehiiv.com/p/the-ai-subsidy-era-is-over) marked April 28, 2026 as the end of AI pricing subsidies. Foundation model providers can no longer afford to sell compute below cost to drive adoption.

This timing creates immediate planning pressure for every AI startup. Product pricing that assumed OpenAI would subsidize inference costs indefinitely now needs revision. Business models built on unlimited cheap API calls need new assumptions about unit economics.

The mechanism driving this change is straightforward. Foundation model companies raised billions in venture capital by promising future revenue that required below-cost pricing to capture market share. The strategy worked for user acquisition but created unsustainable burn rates as usage scaled.

Now those companies face pressure to demonstrate profitable unit economics to justify their valuations. Anthropic, OpenAI, and Google all raised recent rounds at sky-high valuations that require revenue growth trajectories incompatible with subsidized pricing.

For builders, this means immediate tactical decisions about infrastructure costs. Teams that built systems assuming inference would get cheaper indefinitely need contingency plans for pricing that reflects true compute costs. That might mean architectural changes to reduce API calls, local deployment for high-volume use cases, or pricing model changes that pass compute costs through to customers.

The timing couldn't be worse for AI startups approaching their next funding rounds. Investors who funded teams based on subsidized unit economics will now evaluate them on realistic pricing assumptions. Many business models that looked attractive at subsidized API pricing will struggle to justify venture scale returns at market pricing.

Smart founders are already modeling both scenarios. They're building systems that work efficiently at current pricing while preparing for 2-5x price increases over the next 12 months. The teams that get this math right will survive the transition. The teams that don't will become cautionary tales about dependency on unsustainable pricing.

---

### #3 Ethics became a vendor selection variable

[Google expanded Pentagon access](https://techcrunch.com/2026/04/28/google-expands-pentagons-access-to-its-ai-after-anthropics-refusal/) to its AI systems after Anthropic refused to allow Department of Defense use for domestic mass surveillance and autonomous weapons.

This divergence creates the first clear distinction between AI providers based on ethics policies rather than capabilities. Enterprise and government buyers can no longer treat foundation model vendors as interchangeable options with different pricing and performance characteristics.

The decision forcing function is binary for many use cases. Defense contractors need AI providers willing to support military applications. Healthcare companies need providers with clear data handling policies. Financial services need providers that comply with regulatory frameworks that govern algorithmic decision-making.

Anthropic's refusal to support autonomous weapons applications creates immediate competitive advantage for Google in defense markets. But it also creates competitive advantage for Anthropic in markets where ethical AI positioning matters for procurement decisions.

This split will accelerate over the next 18 months as more enterprise buyers face regulatory requirements that mandate specific AI ethics policies from their vendors. Teams building on AI APIs need to evaluate whether their provider's ethics policies align with their target markets' requirements.

[NVIDIA's Nemotron 3 Nano Omni](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence) launch adds another dimension to this vendor selection complexity. Deployable multimodal models that handle documents, audio, and video in one package create on-premises alternatives to cloud APIs for teams with data sovereignty requirements.

The combination of ethics policy divergence and local deployment options means AI infrastructure decisions now involve legal, reputational, and technical trade-offs that didn't exist 12 months ago. Builders need frameworks for evaluating these trade-offs instead of optimizing purely for cost and performance.

---

### What to do this week

**Start running coding agents in sandboxes.** Set up development environments where AI agents can modify files and run commands without breaking production systems. Enable skip permissions so agents don't halt on file operations. This pattern unlocks 8-hour autonomous coding sessions that ship real features while you focus on higher-level problems.

**Test live coding in your next team meeting.** Pick one concrete thing your team is discussing building and use Claude Code or Cursor to build it during the meeting. Document what changes in team dynamics when they can see and test ideas immediately instead of waiting for follow-up tasks. This builds AI confidence faster than any demo or training session.

**Model your unit economics at 3x API pricing.** Calculate what your product margins look like if inference costs triple over the next 12 months. Identify which features or workflows would need architectural changes to maintain profitability. Build systems that work efficiently at current pricing while preparing for realistic market pricing once subsidies end.
