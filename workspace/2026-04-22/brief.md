# AI coding tool valuations have completely decoupled from usage reality

[SpaceX](https://techcrunch.com/2026/04/21/spacex-is-working-with-cursor-and-has-an-option-to-buy-the-startup-for-60-billion/) just locked in a $60B acquisition option on Cursor, that's more than Twitter sold for.

The AI coding tool market is entering a consolidation frenzy that makes zero economic sense. While teams are cutting tool budgets and pausing subscriptions, valuations keep climbing into absurd territory. This disconnect creates real risk for every dev team building workflow dependency on tools that could vanish, pivot, or 10x their prices overnight.

**Key takeaways:**
- Cursor secured a $60B acquisition option from SpaceX despite declining usage among early adopters
- GitHub Copilot paused new individual signups while restructuring pricing and restricting access to premium models
- Anthropic accidentally exposed plans for a potential $100/month Claude Code price hike through a botched A/B test
- George Hotz called the Cursor valuation "sad" and questioned the entire AI coding market's defensibility
- Builders should lock in pricing agreements now and avoid deep workflow dependency on any single tool

### The $60B option that breaks all precedent

The numbers make no sense when you trace them back to actual usage patterns. [SpaceX negotiated an acquisition option](https://techcrunch.com/2026/04/21/spacex-is-working-with-cursor-and-has-an-option-to-buy-the-startup-for-60-billion/) valued at $60 billion for Cursor, a coding assistant that most early adopters have already stopped using regularly.

That valuation puts Cursor above Twitter's $44B sale price. Above whole public companies with decades of revenue and millions of daily active users. For a tool that generates code completions.

The disconnect between valuation and reality is stark when you look at actual developer behavior. [George Hotz pointed this out directly](https://geohot.github.io//blog/jekyll/update/2026/04/22/ai-has-no-moat.html): "Nobody I know even uses Cursor any more." While anecdotal, this matches patterns I keep seeing across teams, initial excitement followed by gradual drift back to existing workflows.

SpaceX's interest makes strategic sense for their own development needs. They're building rockets, satellites, and autonomous systems that require massive amounts of custom software. Having dedicated AI coding infrastructure could accelerate their internal velocity significantly.

But the $60B price tag signals something deeper about how these tools are being valued. This is a defensive play, not a revenue play. SpaceX is betting that controlling AI coding infrastructure will be essential for maintaining competitive advantage in complex engineering domains.

What this means for every other dev team: if SpaceX exercises this option, Cursor becomes an internal tool optimized for SpaceX's needs, not a general-purpose product. Teams depending on Cursor for core workflows could find themselves migrating to alternatives with 60 days notice.

### GitHub Copilot retreats while demand peaks

The timing of [GitHub's Copilot restrictions](https://simonwillison.net/2026/Apr/22/changes-to-github-copilot/#atom-everything) reveals the market's underlying instability. Just as demand for AI coding assistance hits an all-time high, GitHub paused new individual subscriptions and restricted access to their best models.

The changes hit teams hard. Individual plans can no longer sign up. Existing subscribers face tighter usage limits. Access to Claude Opus 4.7 now requires the $39/month Pro+ tier instead of the basic plan. Previous Opus versions got dropped entirely.

This looks like classic pre-consolidation behavior. GitHub is restructuring their entire pricing model while demand is strongest, suggesting they expect the competitive landscape to change dramatically soon. Companies don't voluntarily restrict access to profitable products unless they're preparing for something bigger.

The practical impact lands immediately on thousands of dev teams who built GitHub Copilot into their daily workflows. Teams that started depending on Opus-level reasoning for complex refactoring tasks now face a choice: pay more or downgrade their tooling just as they've adapted to the higher baseline.

I keep coming back to the signal this sends about model access economics. GitHub has direct partnerships with OpenAI and other model providers, giving them better unit economics than almost any competitor. If they're struggling to make premium model access profitable at current pricing, every other coding tool faces the same pressure amplified.

### Anthropic's $100/month trial balloon

The most revealing moment came from [Anthropic's accidental pricing leak](https://simonwillison.net/2026/Apr/22/claude-code-confusion/#atom-everything). For several hours, their pricing page showed Claude Code moved from the $20/month Pro plan to $100/month or $200/month Max plans only.

Anthropic called it an A/B test gone wrong, but the damage was done. Thousands of developers saw a potential 5x price increase for a tool they use daily. The leak exposed what many suspected: current AI coding tool pricing is unsustainable at the unit economics level.

The reaction was swift and harsh. Teams started evaluating alternatives immediately. Some began building internal tools to reduce Claude Code dependency. Others locked in annual contracts at current pricing before potential changes.

This reveals the fundamental fragility in the current market. Most AI coding tools operate at negative unit economics, subsidized by venture funding while they capture market share. When that subsidy pressure builds, pricing can jump overnight.

The contradiction is clear: tools are getting more valuable to developers while becoming more expensive to operate. Model inference costs haven't dropped as fast as usage has grown. Every breakthrough in capability requires more compute, not less.

### The defensibility question George Hotz raised

[Hotz's reaction to the Cursor valuation](https://geohot.github.io//blog/jekyll/update/2026/04/22/ai-has-no-moat.html) cuts to the core tension: "AI has no defensible advantages." His argument is that these tools are thin wrappers around foundation models that anyone can build.

The technical reality supports this view. Cursor's core functionality, code completion, debugging assistance, refactoring suggestions, can be replicated by any team with API access to Claude or GPT-4. The interface matters, but not $60B worth.

Yet the valuations keep climbing. This suggests buyers see something beyond the current product: control over the interface layer between developers and AI models. In a world where every company becomes a software company, controlling how software gets written becomes strategically critical.

The missing piece is data advantage. Cursor sees millions of code completions, refactoring sessions, and debugging flows every day. That behavioral data could train better coding-specific models over time. But only if they can keep users engaged and avoid churn to alternatives.

What founders need to understand is that the current moment may be peak optionality for AI coding tools. Today, you can switch between Cursor, GitHub Copilot, Claude Code, and a dozen alternatives with minimal switching costs. That won't last if consolidation accelerates.

---

### Anthropic drops Claude Code from Pro plan without announcement

[Anthropic appears to have removed Claude Code](https://x.com/simonw/status/2046732056995205620) from their $20/month Pro plan without any public announcement. Users noticed the change when trying to access Claude Code features that had previously been included in their subscription tier.

[Simon Willison's detailed investigation](https://simonwillison.net/2026/Apr/22/claude-code-confusion/#atom-everything) shows the confusion extends beyond just the Pro tier removal. Anthropic's pricing page now shows different tiers and feature sets, but the company hasn't explained the changes or provided migration paths for existing users.

This is a textbook case study in how not to handle pricing changes for developer tools. Silent tier adjustments anger existing users and create immediate opportunities for competitors. Developers who budgeted Claude Code into their workflows now face unexpected costs or forced migrations to alternative tools.

The timing creates a real opening for OpenAI Codex and GitHub Copilot. When developers feel betrayed by pricing changes, they actively seek alternatives rather than grudgingly accepting higher costs. That's different from typical SaaS churn, where users often accept price increases to avoid switching costs.

OpenAI and Microsoft should target frustrated Claude Code users with migration incentives and feature comparisons. Anthropic's confusion gives competitors a window to capture users who are already motivated to switch.

The broader lesson for any AI company building developer tools: pricing transparency matters more for developers than for other user segments. Developers evaluate tools as long-term investments in their workflow. They need predictable costs to make architecture decisions and team budget planning.

Anthropic's silent changes signal that their pricing strategy isn't stable yet. That uncertainty creates risk for any team considering Claude Code for production use. The smart play is either locking in contracts with Anthropic or building abstraction layers that make switching between AI coding assistants less painful.

This connects to the conviction that founders are underusing Claude Code. The teams that treat it as an execution layer for their whole company get more value but also take on more platform risk. Anthropic's pricing instability makes hedging strategies necessary for teams that depend on AI tools for business-critical workflows.

---

### Meta records employee keystrokes to train AI models

[Meta has implemented internal tooling](https://techcrunch.com/2026/04/21/meta-will-record-employees-keystrokes-and-use-it-to-train-its-ai-models/) to capture employee interactions, including keystrokes and mouse movements, for AI model training. The company frames this as improving their AI capabilities by training on real behavioral data from knowledge workers.

The employee consent and privacy implications are immediate. Unlike external users who can choose whether to share data, employees face pressure to participate in data collection as a condition of employment. That creates a different ethical framework than voluntary user data sharing.

What caught my eye is the strategic data advantage this creates. Most AI companies train on public datasets or user-generated content. Meta is now harvesting proprietary behavioral data that competitors can't access. They're seeing exactly how knowledge workers navigate complex tasks, make decisions, and solve problems in real work environments.

This signals a new frontier in AI competitive strategy. The companies with access to the highest-quality behavioral data will train better models for workplace automation. Meta's employee base becomes a proprietary training dataset that Google, Microsoft, and other AI companies can't replicate.

Expect other AI companies to implement similar internal harvesting programs. Amazon already captures extensive behavioral data through AWS usage patterns. Google has Gmail and Workspace interaction data. Microsoft has Office 365 telemetry. The companies that don't have access to large-scale workplace behavioral data will need to acquire it through partnerships or direct employment.

The mental model shift when building AI products: proprietary behavioral datasets now matter more than model architecture improvements. The teams that can capture unique interaction patterns from their specific user base will build better products than teams using generic foundation models.

This also raises immediate questions about employee rights that every AI-building company will face. Can employers require data sharing as a condition of employment? How much behavioral data is reasonable to collect? What consent frameworks protect employee privacy while enabling AI improvement?

The companies that solve these consent and privacy challenges early will have cleaner data collection processes and better employee trust. The ones that implement harvesting without clear ethical guidelines will face internal resistance and potential legal challenges.

---

### What to do this week

**Lock in your Claude Code pricing or build switching infrastructure.** If your team uses Claude Code in production, either negotiate a contract with Anthropic that locks in current pricing or spend 2-3 hours building abstraction layers that make switching to OpenAI Codex or GitHub Copilot less painful. Anthropic's silent pricing changes signal more instability ahead. The teams that prepare now avoid forced migrations later.

**Study the Cursor option structure for strategic partnerships.** Founders building developer tools should spend one hour analyzing the SpaceX-Cursor deal structure as a template for their own strategic partnership negotiations. The option pricing, exclusive model access, and infrastructure positioning create a playbook for how big tech companies will approach dev tool acquisitions. Understanding these mechanics helps in structuring deals with potential acquirers.

**Evaluate backup options for AI coding assistants.** Teams using any AI coding assistant should spend 30 minutes testing alternatives now, before pricing changes or feature removals force rushed decisions. The market is moving toward more platform risk as infrastructure companies acquire independent tools. Having evaluated alternatives makes switching decisions less stressful when they become necessary.

**Consider internal data strategy for AI training.** If you're building AI products and have access to unique user behavioral data, spend time this week defining ethical guidelines for internal data collection. Meta's employee keystroke harvesting shows that proprietary behavioral datasets create real competitive advantages. The companies that establish clean consent frameworks now will have better data collection processes than the ones rushing to catch up later.
