# Five people shipped a full AI product line in 10 weeks using Claude Code

[Gusto's CTO Eddie Kim](https://www.lennysnewsletter.com/p/no-figma-no-jira-no-docs-how-gusto) just proved that small teams with AI tools can ship what took 50-person engineering orgs in 2022.

His 5-person team built and launched Gusto AI, a complete product line with multiple features, in 10 weeks. No Figma mockups. No Jira tickets. No documentation. Just Claude Code, a permanent Zoom call, and aggressive iteration. This is the new playbook for AI-native product development, and founders who get it early will build tomorrow's category winners.

The mechanics behind this speed are fundamentally different from traditional software development. Instead of sequential handoffs between design, engineering, and product management, Gusto's team collapsed these roles into a single shared workspace. The designer sketched directly in code. The product manager adjusted requirements by watching live implementation. Engineers solved problems collaboratively with AI assistance rather than filing tickets for later resolution.

This approach works because AI tools like Claude Code handle the coordination overhead that typically scales with team size. In conventional engineering organizations, you spend weeks synchronizing requirements, architecture decisions, and interface contracts across multiple people. With AI agents managing the mechanical aspects of coding, documentation, and testing, human cognitive load shifts from implementation details to product decisions.

The result is a development velocity that seems impossible under traditional project management frameworks. Instead of planning sprints, writing specs, and coordinating across multiple disciplines, the team built directly against user feedback. Instead of managing technical debt through separate refactoring cycles, they continuously improved code quality through AI-assisted iteration.

**Key takeaways:**
- Gusto shipped a full AI product line with 5 engineers in 10 weeks using Claude Code as their primary development tool
- The team skipped traditional software planning processes (Figma, Jira, docs) and used continuous pairing plus AI agents
- [Cursor mobile](https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/) enables builders to supervise coding agents remotely, making async development feasible
- Open-source [Ornith-1.0](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) provides MIT-licensed agentic coding without API vendor lock-in
- Traditional software development overhead is collapsing, teams that restructure around AI tools achieve 5-10x output gains

### The Gusto playbook: how 5 people built a product line in 10 weeks

Eddie Kim's team structure tells the whole story. Five engineers. One product manager. One designer. Everyone in the same permanent Zoom room, all day. No tickets to track. No specs to write. No design handoffs.

The team used Claude Code as their primary development environment. When someone hit a problem, they'd share their screen and solve it together with AI assistance. The designer would sketch directly in the code. The PM would adjust requirements in real-time by watching the implementation.

What I keep coming back to is the speed. Ten weeks for a full product line. That's not a prototype or MVP, it's a shipping product with multiple features that Gusto customers pay for today.

The key was treating Claude Code as an execution layer, not just a coding assistant. The team used it for documentation, testing, debugging, and even customer research. Instead of writing specifications, they wrote working code. Instead of reviewing design documents, they reviewed running features.

This works because AI handles the coordination overhead that normally scales with team size. In a traditional 25-person engineering team, you spend weeks aligning everyone on requirements, architecture, and interfaces. With 5 people and AI agents doing the heavy lifting, you can ship and iterate in real-time.

### Mobile coding agents change how builders work

[Cursor's mobile app launch](https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/) signals that agentic coding is moving beyond the desktop. Builders can now supervise long-running coding tasks from anywhere, commuting, traveling, or away from their primary workspace.

The mobile supervision model unlocks something new: truly async coding agents. You can start a complex refactoring job, give the agent high-level guidance from your phone while you're in meetings, and return to find working code ready for review.

This changes the fundamental economics of software development. Traditional coding requires continuous human attention, keyboard access, and desktop-class tooling. Mobile supervision decouples the thinking work from the implementation work. You make architectural decisions and provide guidance through voice commands or brief text messages. The agent handles syntax, testing, debugging, and iteration.

The workflow looks completely different from conventional programming. Instead of sitting at a computer for 8-hour coding sessions, builders now work in short bursts of high-level direction followed by long periods of agent execution. A typical day might include 30 minutes of morning planning, 15-minute check-ins during lunch and commute, and 45 minutes of evening review and refinement.

This matters because it extends the working day without extending human coding hours. Your agent codes while you sleep, while you're in calls, while you're thinking about product strategy. The bottleneck shifts from typing speed to decision-making speed.

Early adopters are already using this pattern. Set up the agent with clear objectives before leaving the office. Check progress and provide direction remotely. Review and ship the next morning. What does this mean in practice? You get a junior engineer who works nights and weekends, except the code quality is often better than human output.

The implications for team structure are profound. Instead of hiring more developers to increase output, teams can hire fewer senior engineers who specialize in architectural thinking and agent supervision. The cost structure flips from linear scaling (more engineers = more output) to logarithmic scaling (better supervision = exponentially more output).

### Open-source agentic coding breaks the API dependency

[Ornith-1.0](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) just shipped as the first MIT-licensed model purpose-built for agentic coding. This changes the game for teams worried about vendor lock-in or token costs.

You can now deploy your own coding agent infrastructure. No API keys. No usage limits. No vendor dependencies. The performance benchmarks show it matches frontier models on most coding tasks, with the advantage of complete control over the stack.

Simon Willison's analysis highlights the self-scaffolding architecture, the model can improve its own reasoning chains for complex coding problems. That's typically something you only get with the most expensive commercial APIs.

The economics are compelling for any team running significant coding workloads. Commercial API pricing typically ranges from $10-50 per million tokens, with enterprise contracts reaching $100+ per million tokens for premium models. For a team generating 100 million tokens monthly, that translates to $1,000-5,000 in recurring API costs.

Ornith-1.0 flips this equation. After initial infrastructure investment, the marginal cost per token approaches zero. Teams can run unlimited coding tasks without worrying about token budgets or rate limits. The self-hosted model becomes more cost-effective than commercial APIs once monthly usage exceeds 50 million tokens.

The strategic implications extend beyond cost savings. Running your own coding agents means complete control over code privacy, training data, and model behavior. Enterprise customers who refuse to send proprietary code through external APIs can now access frontier-level coding assistance entirely within their own infrastructure.

For startups building AI-native products, this represents a new strategic option. Instead of paying escalating API costs as you scale, you can invest in local infrastructure that gets cheaper per unit over time. The total cost of ownership math completely flips once you're running serious volume.

Three different approaches. Same underlying pattern. AI is collapsing the traditional coordination costs of software development. Small teams can ship at previously impossible speed and scale.

---

### #2 California just made AI procurement a state-level business

[Anthropic and Governor Newsom](https://techcrunch.com/2026/06/29/anthropic-and-gov-newsom-forge-deal-allowing-california-government-to-use-claude-at-half-price/) signed a deal giving California government agencies Claude access at 50% discount. This is the first state-level AI procurement contract at this scale, and it signals how enterprise AI sales will work in the government sector.

The deal covers multiple California agencies and departments. Anthropic gets guaranteed revenue and a reference customer for other state governments. California gets frontier AI capabilities for public services at a significant discount.

What makes this strategically interesting is the precedent it sets. State governments are becoming AI buyers with real budgets and specific needs. They want the same capabilities as Fortune 500 companies, but with compliance, security, and cost constraints that commercial customers don't face.

The procurement mechanics reveal how government AI adoption actually works. Unlike enterprise customers who can sign contracts and deploy immediately, state agencies must navigate complex compliance frameworks, security audits, and budget approval processes. The 50% discount likely compensates for the additional overhead of government sales, including specialized support, compliance documentation, and extended security reviews.

This creates a different competitive landscape for AI vendors. Success in government markets requires capabilities beyond technical performance: regulatory expertise, security certifications, and patience for multi-year sales cycles. Companies that master government procurement processes gain access to stable, long-term revenue streams that don't exist in the volatile enterprise market.

For AI companies, this represents a new sales channel with different dynamics. Government sales cycles are longer but more predictable. Once you're in with one state, adjacent states often follow similar procurement patterns. The revenue is more stable than enterprise customers who might churn or downgrade.

The pricing model matters too. The 50% discount suggests Anthropic sees government as volume business, lower margins but higher certainty. That's different from the high-margin enterprise deals that most AI companies prioritize today.

This also positions Anthropic politically. While OpenAI faces regulatory scrutiny and restrictions, Anthropic is building direct relationships with government agencies. That could translate into preferential treatment in future AI policy decisions.

---

### #3 South Korea commits $550B to solve AI's memory bottleneck

[Samsung and SK Hynix](https://techcrunch.com/2026/06/29/south-korean-tech-giants-commit-over-550b-to-ease-ramageddon/) are investing over $550 billion in new memory fabrication facilities to address what the industry calls "RAMageddon", the shortage of high-bandwidth memory needed for AI training and inference.

The scale of this investment tells you everything about where AI infrastructure bottlenecks really are. Not compute. Not algorithms. Memory bandwidth. The current generation of AI models is memory-bound, meaning they spend more time waiting for data than processing it.

The technical constraint is specific: High Bandwidth Memory (HBM) chips that can deliver the data transfer rates required by modern AI accelerators. NVIDIA's H100 and H200 GPUs require HBM3 memory configurations that only Samsung and SK Hynix can manufacture at volume. Without sufficient HBM supply, even unlimited compute budgets can't fully use available processing power. Training clusters sit idle waiting for memory, not compute cycles.

Current HBM (High Bandwidth Memory) production can't keep up with demand from AI training clusters. NVIDIA's latest chips need specific memory configurations that only Samsung and SK Hynix can manufacture. Without enough memory, you can't fully use the compute capacity you're paying for.

The $550B figure represents the largest coordinated infrastructure investment in AI history. For context, that's larger than the entire market cap of most Fortune 100 companies. South Korea is betting its entire tech sector on becoming the memory supplier for global AI infrastructure.

This creates a clear timeline for when the memory ceiling lifts. New fab facilities take 3-4 years to build and ramp production. So relief arrives around 2027-2028, assuming construction starts immediately.

For anyone planning AI infrastructure investments, this timing matters. If you're building systems that scale beyond current memory constraints, you're betting on this timeline. If these fabs deliver on schedule, memory becomes abundant and cheap around 2028. If they don't, memory stays the limiting factor on AI scaling through the decade.

---

### What to do this week

**Test local coding agents**, Download [Ornith-1.0](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) and run it locally for one development task this week. Compare output quality and speed vs your current AI coding setup. Budget 2 hours for setup and testing. Document the performance differences and detailed cost implications for your team.

**Audit your development process overhead**, Time how much of your engineering team's week goes to coordination activities (standups, tickets, documentation, handoffs) vs actual building. If it's above 40%, experiment with Gusto's approach: smaller teams, permanent communication channels, AI-assisted development.

**Try mobile code supervision**, If you use Cursor, download the mobile app and start one medium-complexity coding task you can monitor remotely. Test whether you can provide useful guidance while away from your main workspace. Time investment: 30 minutes setup, ongoing experimentation with async development workflows.
