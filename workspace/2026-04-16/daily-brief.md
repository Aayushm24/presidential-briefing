# Daily Brief — 2026-04-16

**Lead:** Codex for (almost) everything

# AI agents aren't adding features to software. They're replacing it.

Anthropic's chief product officer just resigned from Figma's board because Anthropic is about to ship a design tool that competes with Figma directly.

That single move captures what's happening across the entire software industry this week. The AI labs and agent-native companies aren't building plugins for existing tools. They're building replacements. OpenAI's Codex now does computer use, browsing, image generation, and plugins. Agentic coding workflows are making pull requests obsolete. Go-to-market teams are wiring Claude directly into their CRMs and data warehouses, bypassing the SaaS apps those tools were built around. The pattern is unmistakable: **agents are becoming the primary interface layer**, and every traditional software workflow is a target.

**Key takeaways:**
- Anthropic is entering design tooling, signaling that even creative SaaS categories (not just dev tools) face direct competition from AI labs
- OpenAI's Codex expansion and Agents SDK updates are building a full platform, not just a coding assistant, positioning it against Cursor, Replit, and the entire IDE category
- Pull requests, the backbone of collaborative software development since 2005, are being actively deprecated by GitHub itself as agentic coding workflows take over
- Non-technical teams (sales, marketing, RevOps) are already connecting Claude to production business systems via MCP, creating agent workflows that replace multi-tool SaaS stacks
- The defensible position for software companies is shifting from "best UI for a workflow" to "best data and domain logic for an agent to consume"

### The AI labs are coming for your category

Mike Krieger resigned from Figma's board on April 14. The same day, The Information reported that Anthropic's next model, Opus 4.7, will include design tools that could compete with Figma's core product. This is not subtle.

Krieger co-founded Instagram. He joined Anthropic as chief product officer in 2024. He joined Figma's board in a move that seemed like a natural alignment between a frontier AI lab and a design tool company integrating AI assistants. Now that alignment is a conflict of interest.

> His departure was disclosed to the U.S. Securities and Exchange Commission by the publicly traded $10 billion company the same day that the Information reported Anthropic's next model, Opus 4.7, will include design tools that could compete with Figma's primary offering.

Think about what this means for the broader SaaS landscape. Figma isn't some sleepy incumbent. It's a $10 billion public company that has been actively collaborating with Anthropic to integrate Claude into its product. And Anthropic is building a competing product anyway.

This is the playbook we've seen in developer tools playing out in creative software. OpenAI built Codex as a coding assistant, then expanded it into a full development environment with computer use, browsing, image generation, memory, and plugins. That's not an assistant for Cursor. That's a competitor to Cursor. Now Anthropic is doing the same thing to Figma.

The lesson for every SaaS founder: **your AI integration partner may become your primary competitor**. The labs have the models, the distribution, and increasingly the product ambition to go vertical.

### The death of the pull request is a bigger deal than it sounds

GitHub is, for the first time in its history, allowing people to disable pull requests on open source repos. That sentence should stop every engineering leader in their tracks.

Pull requests were invented in 2005. GitHub popularized them into the universal standard for collaborative software development. Every engineering team on earth uses them. And now the platform that made them ubiquitous is making them optional.

> The rise of Generative AI in code has spelled the pending death of the Pull Request for a while now. Pete Steinberger is by now well known for only wanting Prompt Requests rather than Pull Requests.

The reasoning is practical, not theoretical. When agents generate code, the traditional PR review process breaks down in multiple ways. Merge conflicts become meaningless when you can regenerate from a prompt. It's easier for a maintainer to modify a prompt than to review thousands of lines of generated code. And prompt-based contributions are harder to use as vectors for slipping in malicious code.

Mitchell Hashimoto and Amp Code have already built "reputation-based" systems for handling untrusted code contributions. These aren't experiments. They're production workflows replacing a 21-year-old standard.

The deeper question Latent Space raises is worth sitting with: if code reviews are dead, and pull requests are dead, **how long until Git itself is dead?** Git was designed for human collaboration patterns. Agents don't have the same constraints. They don't need branching strategies or conflict resolution. They need task specifications and verification systems.

This connects directly to what Notion learned after rebuilding their agent system five times. The infrastructure assumptions we've carried from the human-centric era of software development are being invalidated one by one. Teams that redesign their workflows around agent-native patterns, rather than bolting agents onto Git-based processes, will move faster.

### GTM teams are already living in the agent-native world

The most surprising evidence this week doesn't come from developer tools. It comes from sales and marketing teams.

Brendan Short organized a live event for go-to-market operators using MCPs (Model Context Protocol) with Claude. Close to 800 people registered. Almost 400 joined live. Six people presented production workflows they've built.

> The gap between teams that have connected their tools to AI and teams that haven't is getting wider every week. MCPs are the connective tissue. They let Claude talk to your CRM, your data warehouse, your call recorder, your prospecting tools.

This is the part that should alarm every SaaS company selling to GTM teams. These operators aren't using Claude as a writing assistant inside their existing tools. They're connecting Claude directly to their data sources via MCP and building workflows that bypass the SaaS applications entirely.

> Without them, Claude is smart but blind. With them, it becomes something closer to a second brain that actually knows your business.

When a sales rep can ask Claude to pull data from their CRM, cross-reference it with call recordings, enrich it with prospecting data, and generate an action plan, the value of the individual SaaS tools in that chain shifts. The CRM becomes a data store. The call recorder becomes a data source. The prospecting tool becomes an API. **The interface layer is Claude.**

This is happening across 800 registrants for a single event. It's not a demo. It's a movement.

### OpenAI is building the agent platform, not just the model

OpenAI's Agents SDK update adds sandboxing, expanded safety guardrails, and new capabilities for enterprise agent development. On its own, this is an incremental update. In context, it's a piece of a much larger strategy.

Codex now includes computer use, web browsing, image generation, memory, and plugins. The Agents SDK gives enterprises the tools to build their own agents on OpenAI's infrastructure. Together, they form a platform play that looks less like "API provider" and more like "the operating system for agent-based work."

The sandboxing capability matters specifically because it addresses the reliability problems that have plagued agent deployments. Running agents in controlled environments where they can only access specific files and code for particular operations is exactly the kind of guardrail that enterprise buyers need before they'll deploy agents in production.

This is OpenAI learning from the same lessons Notion documented across their five rebuilds. **Production agents need containment, not just capability.** The SDK update signals that OpenAI is building for the messy reality of enterprise deployment, not just for impressive demos.

### What this pattern means for builders

Every story this week points in the same direction. The AI labs are moving up the stack from models to products. Agent workflows are replacing, not augmenting, existing software processes. And this is happening simultaneously in developer tools, creative software, and business operations.

The companies that will struggle most are the ones treating AI as a feature to add to their existing product. Figma integrated Claude as an assistant for designers. Now Anthropic is building a design tool. CRM companies added AI writing features. Now GTM teams are connecting Claude directly to their data and skipping the CRM interface.

The companies that will win are those building around the assumption that an agent is the primary user. Aaron Levie's framing is exactly right: **"the path forward is to make software that agents want."** That means great APIs, clean data models, and domain-specific logic that agents can consume. Not pretty dashboards that humans click through.

The execution gap is closing fast. The tooling exists. The mental models exist. Notion's five rebuilds, the emerging frameworks for agent reliability, the MCP ecosystem, the SDK updates. All of it is available to any team willing to invest. Speed of iteration is the remaining differentiator, and every week you spend adding AI features to a traditional SaaS product is a week an agent-native competitor spends replacing your entire category.

---

### #2 A 21GB local model just out-drew Claude Opus 4.7

Simon Willison's pelican-riding-a-bicycle SVG benchmark started as a joke. It has become one of the most watched informal tests in AI because, weirdly, pelican quality has correlated with general model usefulness over time.

This week, **Qwen3.6-35B-A3B**, a model from Alibaba that fits in a 20.9GB quantized file, running locally on a MacBook Pro M5 via LM Studio, drew a better pelican than Anthropic's brand new Claude Opus 4.7. Opus even messed up the bicycle frame.

> I'm giving this one to Qwen 3.6. Opus managed to mess up the bicycle frame!

Willison tested a backup prompt (flamingo riding a unicycle) to check if Qwen was specifically trained on his benchmark. Qwen won that one too, complete with an SVG comment reading `<!-- Sunglasses on flamingo! -->`.

The practical takeaway for builders running inference budgets: **local models at the 35B parameter range are now competitive with frontier models on creative coding tasks**. Not on everything. Not on complex reasoning chains or long-context analysis. But on the kind of structured generation tasks that make up a huge portion of real-world agent work, a model you can run on your laptop for zero marginal cost is keeping pace with a model that costs real money per token.

This doesn't mean you should ditch Opus or GPT for everything. It means the cost-capability frontier is shifting faster than most teams' infrastructure decisions account for. If you're running agents that do structured generation, code synthesis, or template-based output, benchmark a local model against your current API provider. You might be surprised.

---

### #3 OpenAI's Agents SDK gets the boring features that matter

The headline features of OpenAI's Agents SDK update, sandboxing, safety guardrails, expanded capabilities, sound like enterprise checkbox items. They're actually the features that determine whether agent deployments survive contact with production.

Sandboxing lets agents operate in controlled environments where they can only access specific files and execute specific operations. This directly addresses the "agent went rogue and deleted the wrong thing" failure mode that has killed more pilot programs than any capability gap.

The safety guardrails are designed to give enterprises confidence that agents won't produce harmful outputs or take unauthorized actions. This is table stakes for regulated industries, but it's also what every Fortune 500 procurement team asks about before signing off on an agent deployment.

What's notable is the positioning. OpenAI isn't just selling models anymore. **They're selling the development platform for agent-based applications.** The SDK, Codex, the API, the safety tooling. It's a full stack. Anthropic has MCP and Claude's tool-use capabilities. Google has Vertex AI agents. The platform war for agent development is heating up, and the SDK updates are OpenAI's bid to be the default choice for enterprise builders.

---

### What to do this week

**1. Audit your product's "agent surface area."** Take your product's core workflow and ask: if Claude or Codex were the primary user instead of a human, what would they need? If the answer is "a better API and cleaner data model," start building that now. If the answer is "they'd need our exact UI," you have a problem. This exercise takes 30 minutes and will clarify your strategic position faster than any roadmap review.

**2. Run one production task through a local model.** Download the Qwen3.6-35B-A3B-UD-Q4_K_S GGUF from Unsloth, install LM Studio, and test it against your current API provider on a real structured generation task from your workflow. Compare output quality and calculate the cost difference at your current volume. If quality is within 90%, you just found margin.

**3. If you manage an engineering team, start a "post-PR" experiment.** Pick one low-stakes internal repo. Disable PR requirements. Let contributors submit prompts instead of code, with the maintainer regenerating and verifying. Run it for two weeks. Document what breaks and what gets faster. The teams that figure out agent-native development workflows now will have a structural advantage in 12 months when this becomes the default.