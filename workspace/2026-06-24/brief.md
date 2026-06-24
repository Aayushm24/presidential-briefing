# AI shifts from tools to persistent teammates embedded in your workflow

Claude Tag lives in your Slack, remembers everything your team said about the Jakarta project, and jumps into threads when someone mentions feature flags.

[Anthropic](https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/) launched Claude Tag this week. [Karpathy](https://x.com/karpathy/status/2069547676849557725) called it the third major redesign of LLM interfaces, from website to app to persistent org-wide entity. [MoEngage](https://techcrunch.com/2026/06/23/indias-moengage-bets-marketings-future-on-millions-of-ai-agents/) bought a company to deploy per-customer agents. The pattern is clear: AI is moving from discrete tools you open to embedded teammates that live inside existing workflows.

**Key takeaways:**
- Claude Tag embeds an always-on AI entity in Slack that learns from every message and context-switches across company projects
- Karpathy frames this as the third fundamental redesign of LLM interaction, moving from chat interfaces to persistent org-wide presence
- Real companies are betting real money: MoEngage acquired tech to assign individual AI agents to customers, Cornell recovered $100K with a custom treasury skill
- The winning distribution pattern is ambient integration, not destination applications, builders who treat AI as standalone products are solving yesterday's problem
- Enterprise procurement shifts from "can we try AI?" to "which AI teammate can we commit to for 36 months?"

### Claude becomes your company's third hire

What caught my eye about Claude Tag is how [Anthropic](https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/) frames it. Claude Tag operates as a team member with persistent memory rather than traditional productivity software.

Claude Tag doesn't just answer questions in Slack. It remembers every project your team discussed. When someone mentions the Jakarta deployment, Claude knows that's the project Sarah leads, that it's running two weeks behind, and that the blocker is feature flag permissions.

The mechanism works through persistent memory across conversations. Traditional Claude forgets everything when the chat window closes. Claude Tag accumulates context from every Slack thread it sees. Your company's knowledge becomes Claude's working memory.

The technical architecture leverages vector embeddings to index every message Claude observes. When someone asks about the Jakarta project, Claude doesn't just pattern-match keywords. It retrieves the embedded context from six different conversations: Sarah's initial project proposal, the timeline discussion from two weeks ago, yesterday's blocker update, and three related technical threads about feature flags. The system weights recent conversations higher but maintains access to historical context that would otherwise be buried in search results.

This creates compound intelligence that improves with time. Week one, Claude Tag answers basic questions about who owns what project. Month three, it connects patterns across projects that your team missed. Month six, it becomes the institutional memory that survives team changes and onboards new hires.

Here's why this timing works: Slack already holds 80% of your company's institutional knowledge. Design decisions, post-mortems, budget discussions, project updates. Claude Tag positions itself as the entity that remembers all of it and can surface connections you forgot existed.

The economic model shifts too. You're not paying per conversation anymore. You're paying for Claude to be present in every conversation your team has. It's infrastructure, not tooling.

What I keep thinking about is the handoff moment. When Claude Tag knows enough about your company to onboard new hires. When it remembers vendor relationships better than your procurement team. When it becomes the single source of truth for "why did we decide that?"

### Karpathy maps the interface evolution that everyone missed

[Andrej Karpathy](https://x.com/karpathy/status/2069547676849557725) called Claude Tag the third major redesign of how humans interact with LLMs. His breakdown:

First generation: website chat interfaces. You go to claude.ai, type questions, get answers.

Second generation: apps and APIs. Claude Code, Cursor, Notion AI. LLMs embedded in software you already use.

Third generation: persistent org-wide entities. Claude Tag lives in your Slack, learns from every message, context-switches across your company's entire knowledge graph.

The shift from generation two to three changes everything about how you build AI products. Generation two optimizes for single-session utility. Generation three optimizes for long-term memory and ambient presence.

Most AI builders are still designing for generation two. They build tools that solve specific problems well. Claude Tag suggests the winning pattern is tools that solve any problem adequately because they know everything about your context.

This explains why every AI startup's demo looks identical but customer retention varies wildly. The ones that stick remember what you did last week rather than just having better models.

The technical challenge has shifted from model quality to memory architecture. How do you store, index, and retrieve six months of company conversations? How do you decide what Claude should remember and what it should forget? How do you handle sensitive information that Claude shouldn't learn from?

Anthropic solved this by making Slack the memory layer. Every message Claude sees becomes part of its working knowledge of your company. The model doesn't need to be perfect if the context is complete.

### The procurement question changes from "should we" to "which one"

The most telling detail about Claude Tag focuses on how Anthropic positioned it as infrastructure from day one rather than the underlying technology.

You don't trial Claude Tag. You deploy Claude Tag. It learns your company's processes, builds up institutional knowledge, becomes the entity that knows why your team made specific decisions. Switching costs rise every day it's live.

That's the real strategic play here. Anthropic wants to become so embedded in your workflow that evaluating competitors means rebuilding six months of accumulated context.

I've seen this procurement shift firsthand at Atlan. Three months ago, enterprise teams asked "should we try AI?" Now they ask "which AI can we commit to for 36 months?" The second question assumes AI adoption is inevitable. The debate is about which vendor becomes part of your company's memory.

Claude Tag accelerates this shift. When your AI teammate knows every project, every vendor relationship, every design decision your company made in the last year, switching to a different AI means starting over. The knowledge graph doesn't transfer.

This is why [MoEngage](https://techcrunch.com/2026/06/23/indias-moengage-bets-marketings-future-on-millions-of-ai-agents/) paid cash to acquire technology that assigns individual agents to customers. They're not buying software. They're buying persistent relationships.

The winning AI products in 2026 won't be the ones with the best answers. They'll be the ones with the longest memories.

---

### Cornell recovered $100K with a custom treasury skill, the case for dedicated AI labs

[Ethan Mollick](https://x.com/emollick/status/2069486790075908261) shared the exact kind of story every CFO needs to hear about AI ROI.

Cornell's finance team worked with their AI lab to build a custom Claude skill for treasury management. The skill analyzed payment records, identified overdue invoices from vendors, and flagged discrepancies in accounts receivable. Result: $100,000 recovered in back payments that would have been written off.

The specific mechanism matters here. This wasn't Claude giving generic financial advice. Cornell built a skill that understood their vendor contracts, payment terms, and accounting workflows. The AI knew which vendors historically pay late, which contracts include penalty clauses, and which payments were worth pursuing.

The implementation reveals how enterprise AI succeeds when you solve process problems rather than capability problems. Cornell's treasury team had always known they were losing money to forgotten receivables. The challenge wasn't identifying the problem. The challenge was systematically executing the recovery process across thousands of vendor relationships.

Their Claude skill automated the tedious parts: cross-referencing payment histories, calculating penalty amounts based on contract terms, prioritizing recovery efforts by dollar impact and likelihood of success. It generated follow-up templates tailored to each vendor's payment pattern. For repeat late-payers, it suggested stronger language and escalation timelines. For first-time delays, it recommended gentle reminders that preserved relationships.

The $100K recovery happened over six months through systematic execution of a process the finance team already understood but couldn't scale manually. This is the pattern that separates AI successes from AI experiments: using AI to execute human expertise consistently rather than replacing human judgment.

Most companies approach AI backwards. They ask "what can AI do for us?" Cornell asked "what specific problem costs us money every quarter?" Then they built AI around that problem.

The bigger insight is organizational: Cornell has both employee AI exploration and a dedicated AI builder lab. Most companies pick one. You either let employees experiment with AI tools, or you have a centralized team building AI solutions. Cornell does both.

Their finance team identified the treasury problem. Their AI lab built the solution. That split lets subject matter experts define problems while technical teams solve them. The $100K recovery happened because the people who understand treasury workflows collaborated with the people who understand AI capabilities.

---

### IBM drops 24 working agent examples on a lightweight harness

[IBM Research](https://huggingface.co/blog/ibm-research/cuga-apps) released CUGA, two dozen working agentic applications built on a lightweight harness you can run today.

What makes this interesting is the approach. Instead of releasing another AI framework, IBM built 24 single-file applications that demonstrate how to handle the boring parts of agent development: tool integration, state management, execution loops, guardrails.

Each application is a complete FastAPI file wrapping one agent. Movie recommender. IBM Cloud architecture advisor. Document analyzer. You can read every line, copy what works, and deploy it unchanged.

The philosophy behind CUGA inverts the usual agent development process. Most teams spend weeks building plumbing before their agent does anything useful. You pick a framework, wire up tool adapters, build state management, create streaming interfaces. The interesting part arrives last.

CUGA handles the plumbing. What's left is the part that's actually yours: which tools the agent can reach and what you tell it to do.

This matters because most agentic applications fail in the infrastructure layer, not the prompt layer. Building an agent that can reliably call APIs, manage state across conversations, and handle errors gracefully is harder than writing the prompts that make it useful.

IBM's examples prove their harness works by showing 24 different ways to use it. That's the kind of proof builders need when choosing architecture for agent projects.

The timing matters for this release. Most enterprise teams are moving past the "should we build agents?" question toward "how do we build agents that actually work in production?" CUGA addresses the infrastructure gap that kills most agent projects before they reach users.

The 24 examples span different complexity levels and use cases. Simple agents like the movie recommender demonstrate basic tool integration and conversation management. Complex agents like the IBM Cloud architecture advisor show how to handle multi-step reasoning, external API dependencies, and domain-specific knowledge retrieval. Each example includes error handling, state persistence, and deployment instructions that work in real environments.

This approach reduces the time from agent idea to working prototype from weeks to hours. Instead of building infrastructure, teams can focus on the domain-specific logic that makes their agent useful. The examples become reference implementations that teams can modify rather than starting from scratch.

---

### What to do this week

**Test Claude Tag's memory against your company's knowledge graph.** If your team uses Slack, request access to Claude Tag beta and spend one week letting it observe your project discussions. Then ask it to summarize a project from two months ago. The quality of its recall will tell you whether persistent AI memory is ready for your workflow. Time: 2 hours setup, 30 minutes daily testing.

**Map your organization's treasury recovery opportunities.** Cornell found $100K in back payments using AI. Run a similar analysis on your accounts receivable. Which vendors pay late? Which invoices get forgotten? Which contracts include penalty clauses you never enforce? Build a simple dashboard that flags these patterns before considering AI automation. Time: 4 hours analysis, results immediately actionable.

**Clone one CUGA example and modify it for your use case.** Visit the [CUGA applications gallery](https://huggingface.co/blog/ibm-research/cuga-apps), pick the example closest to a problem you're solving, and adapt it. The single-file architecture means you can understand every component and modify what doesn't fit. This is the fastest path from "AI could help with this" to "AI is helping with this." Start with the document analyzer or movie recommender for simpler use cases. Time: 3 hours to clone and modify, 1 hour to deploy locally.
