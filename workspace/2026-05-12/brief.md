# Companies are restructuring engineering teams around AI agents, not just adding AI to existing workflows

[General Motors](https://techcrunch.com/2026/05/11/gm-just-laid-off-hundreds-of-it-workers-to-hire-those-with-stronger-ai-skills/) laid off hundreds of IT workers last week to hire AI-native engineers instead, the clearest signal yet that Fortune 500s are replacing roles, not just adding AI on top.

Companies across industries are restructuring their engineering organizations around agent-native workflows. [Notion](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering) ships PRs from Slack comments in 20 minutes. [Shopify's CEO](https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/) works with an AI agent in public channels that 100+ employees follow. This is workforce transformation, not augmentation. The coordination overhead that made large teams necessary is collapsing.

**Key takeaways:**
- GM replaced hundreds of legacy IT roles with AI-native positions (data engineering, prompt engineering, agent development). Fortune 500 workforce replacement is happening now, not later
- Notion's engineering team ships full PRs from single Slack comments via their internal "Boxy" system. This is spec-driven development where agents do implementation while humans do thinking
- Shopify's CEO works with River, an AI coding agent, entirely in public Slack channels with 100+ employees watching and learning. This transparency-first agent deployment creates organizational learning
- Infrastructure companies like GitLab are restructuring around "the agentic era" by consolidating geographic footprints and focusing team structure around AI-first workflows
- Small teams using AI coordination can now outcompete traditional 50-person organizations by eliminating status meetings, handoffs, and documentation overhead

### GM traded legacy IT headcount for AI-native engineers

General Motors made the most explicit workforce transition announcement yet. The company [laid off hundreds of IT workers](https://techcrunch.com/2026/05/11/gm-just-laid-off-hundreds-of-it-workers-to-hire-those-with-stronger-ai-skills/) this week and immediately posted new job listings for AI-native roles. The new positions focus on "AI-native development, data engineering and analytics, cloud-based engineering, and agent and model development." They also include "prompt engineering and new AI workflows."

This signals the transition from traditional IT maintenance to AI-first engineering. GM's bet is that maintaining legacy systems with human labor costs more than rebuilding those systems with AI agents. They're trading overhead for velocity.

The timing reveals why Fortune 500s are making this swap now. Two years ago, AI tools required specialist knowledge to deploy. Model access was limited, prompting techniques were esoteric, and integration required custom infrastructure. Today, any engineer can prompt Claude Code or Cursor to generate working solutions. The accessibility gap closed.

GM's calculation is straightforward economics. Legacy IT teams maintain systems built in the 2000s and 2010s. These include .NET applications, on-premise databases, and custom integrations that require institutional knowledge to modify. These systems work but cannot adapt quickly to new requirements. Each change requires multiple people, extensive testing, and coordination across teams.

AI-native engineers approach the same problems differently. Instead of maintaining legacy code, they rebuild systems using modern frameworks that AI agents can modify directly. Instead of complex deployment pipelines, they use platforms that AI can deploy to automatically. Instead of team coordination, they use agents that handle integration testing.

What forced GM's hand was competitive pressure from Tesla and Rivian. Both companies ship software updates faster because they built their engineering orgs around small, AI-augmented teams from day one. Tesla's Full Self-Driving updates arrive weekly. Rivian's mobile app gets features monthly. GM's equivalent systems required quarterly release cycles with months of testing.

GM had to choose: gradually retrain existing IT staff over 3 years while losing market share, or swap the entire org structure in 6 months and match competitor velocity. The retraining path assumes legacy systems can coexist with AI workflows. GM's bet is that assumption is wrong.

The causal chain forward is clear. Other automakers face the same labor cost and velocity gap. Ford, Stellantis, and every industrial company with large IT departments will follow GM's playbook within 18 months. The talent market is already shifting. Traditional systems administrators can't compete with prompt engineers for the same salary.

This proves the first conviction: small teams with AI beat 50-person orgs. GM is betting $100M+ in reorganization costs on this being true at enterprise scale.

### Notion engineers ship PRs from Slack comments in 20 minutes

[Ryan Nystrom at Notion](https://www.lennysnewsletter.com/p/spec-driven-development-the-ai-engineering) described their internal "Boxy" system where engineers @mention Codex from within Notion comments and get a full pull request with screenshots delivered in 20 minutes. The workflow removes traditional development friction entirely.

Here's how it works: An engineer types a feature request as a natural language comment in Notion. They @mention Boxy. The agent reads the comment, understands the existing codebase context, writes the implementation, creates screenshots of the changes, and opens a pull request. The human engineer reviews the PR and merges or requests changes.

> "You dictate an idea into Whisper, have Codex format it as a proper spec, commit it to the repo, and let the agent implement and verify it autonomously," Nystrom explained.

This is spec-driven development. The engineer's job shifts from writing code to writing specifications and reviewing agent output. The agent handles implementation details, testing, and documentation. Engineering velocity jumps because humans focus on what to build rather than how to build it.

I keep coming back to the infrastructure requirements this creates. Notion runs "Project Afterburner" to cut their CI time to one-quarter of current duration because fast feedback loops become critical when agents write more code per day than human teams could write per week.

The causal chain reshapes engineering management. Traditional metrics like lines of code per week become meaningless when agents write the code. Product requirements become more important than coding skill. The boundary between PM and engineer blurs when both roles focus on specification rather than implementation.

Memory and context matter more than raw model capability. Notion's agents work because they know the existing codebase, understand the team's conventions, and learn from previous PRs. This compounds over time in ways that using general-purpose coding assistants cannot match.

The infrastructure investment required is substantial but pays forward. Notion runs continuous integration that completes in minutes rather than hours. Their agents generate more code per day than human teams generated per week, so slow CI becomes a bottleneck that kills productivity gains. Fast feedback loops are essential for agent-augmented development.

What I find most interesting is how this changes the skill profile for engineering roles. Traditional senior engineers optimized for code architecture and debugging complex systems. Notion's engineering structure optimizes for specification writing and agent prompt design. The ability to clearly communicate requirements to AI becomes more valuable than the ability to implement those requirements manually.

This creates a talent arbitrage opportunity. Engineers skilled at working with AI agents can outproduce traditional teams by 3-5x while commanding similar salaries. The market has not yet priced in this productivity differential, creating temporary competitive advantage for teams that hire AI-native engineers before the salary premium emerges.

### Shopify's transparent agent development in public channels

Tobias Lütke, Shopify's CEO, works with an AI coding agent named River entirely in public Slack channels. [Simon Willison highlighted](https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/) the unusual transparency: River refuses direct messages and suggests creating public channels instead. Lütke works in #tobi_river, and over 100 Shopify employees follow the channel to watch and learn.

> "River does not respond to direct messages. She politely declines and suggests to create a public channel for you and her to start working in," Lütke explained.

This makes agent deployment a training ground for the entire organization. Every conversation is searchable. Anyone can jump in with questions or improvements. The CEO's workflow becomes the template that other teams copy and modify for their own agents.

What caught my eye is the knowledge transfer effect. Instead of one person learning to work effectively with AI agents, 100+ people absorb the patterns through observation. They see how Lütke prompts River, how he iterates on responses, how he handles edge cases. This scales AI adoption faster than any training program.

The transparency creates competitive advantage through shared learning. Private agent work becomes organizational inefficiency when teams solve the same prompting problems in isolation. Public-first deployment prevents duplicate effort and spreads best practices instantly.

The model spreads beyond engineering. Sales, marketing, and support teams at Shopify are launching their own public agent channels. The pattern: instead of departmental AI pilots, make agent learning visible across the company.

### Infrastructure companies restructuring for the agentic era

Even the companies selling development tools are restructuring around AI-native workflows. [GitLab announced](https://simonwillison.net/2026/May/11/gitlab-act-2/) "workforce reduction" and "structural and strategic decisions" for what they explicitly called "the agentic era." They're consolidating by up to 30% the number of countries where they have small teams.

GitLab's reasoning reveals the structural changes happening. When small AI-augmented teams outship large distributed teams, geographic distribution becomes a liability rather than an asset. Coordination overhead kills velocity. Better to consolidate talent in fewer locations where agents can work with tighter human feedback loops.

This affects every distributed software company. The companies that built remote-first cultures around human coordination are discovering that AI agents work better with centralized context and faster iteration cycles. GitLab's restructuring signals that even the most distributed-friendly companies see agent workflow efficiency outweighing remote work benefits.

What these three examples prove is the same organizational bet at different scales. GM (Fortune 10), Notion (growth-stage startup), and GitLab (public infrastructure company) are all restructuring around the same principle: small teams with AI agents beat large teams with traditional workflows.

The pattern holds across industries and company sizes. Traditional org charts built around human coordination are becoming cost centers. The companies that restructure first gain 18 months of competitive advantage while their competitors figure out how to retrain existing teams.

---

### #2 LLM shebang scripts turn natural language into executable code

[Simon Willison discovered](https://simonwillison.net/2026/May/11/llm-shebang/) you can use his LLM CLI tool as a script interpreter via shebang lines. This turns natural language files into executable scripts that generate code, images, or data on demand.

The simplest pattern uses LLM fragments: `#!/usr/bin/env -S llm -f Generate an SVG of a pelican riding a bicycle`. Save that line in a file, make it executable with `chmod +x`, and running it generates SVG code for a pelican on a bicycle.

More sophisticated versions incorporate tool calls: `#!/usr/bin/env -S llm -T llm_time -f Write a haiku about the current time`. This pulls real-time data into the generation process.

What makes this clever is removing the friction between idea and execution. Instead of opening a terminal, typing an LLM command, copying the output, and saving it to a file, the entire workflow becomes `./make-pelican-svg` and you get the result immediately.

The practical applications stack up quickly. Generate boilerplate code for new projects. Create data visualization scripts that adapt to current data. Build documentation that updates itself based on codebase changes. All without traditional programming overhead.

I think this represents a broader pattern in AI tooling. The best integrations hide the complexity of prompt engineering behind familiar interfaces. A shebang line looks like normal Unix scripting. The underlying LLM call becomes invisible infrastructure.

The real power emerges when you combine this with traditional Unix tools. Pipe LLM shebang output to `jq` for JSON processing. Chain multiple AI generation steps with `&&` operators. Build sophisticated workflows where each step uses natural language but the composition follows standard shell patterns.

For developers already using LLM CLI, this immediately upgrades their toolkit. For teams adopting AI tools, it demonstrates how AI can integrate with existing workflows rather than replacing them entirely.

The broader pattern this represents is infrastructure that makes AI feel native to existing environments. Instead of switching to web interfaces or learning new command syntax, developers can use AI generation through familiar Unix conventions. This reduces adoption friction and increases usage frequency.

I expect this pattern to spread across other development tools. SQL queries in shebang lines for data analysis. API calls that generate based on current system state. Documentation that writes itself by reading code and configuration files. The constraint of Unix conventions forces AI tools to integrate naturally rather than demanding workflow changes.

---

### #3 The "Zombie Internet" problem threatens content trust

[Jason Koebler's angry piece](https://simonwillison.net/2026/May/11/zombie-internet/) about AI content pollution coined the term "Zombie Internet" to describe something more insidious than the "Dead Internet" theory. While Dead Internet imagines bots talking to each other, Zombie Internet describes AI content mixed with human content in ways that make filtering mentally exhausting.

The problem goes beyond fake news. AI writing is starting to distort regular human writing styles. People read AI-generated content, absorb the patterns, and begin mimicking the same structures and phrase choices in their own writing. The contamination spreads through imitation rather than intentional deception.

> "The truth is that large parts of the internet are not 'dead' in the sense that they are filled with bots talking to each other. They are filled with zombie content that is designed to look human, mixed in with human content, in a way that makes it incredibly difficult to distinguish," Koebler wrote.

This creates a trust crisis for anyone building content or media products. Readers develop defensive skepticism toward everything they encounter online. They spend cognitive energy trying to detect AI generation rather than engaging with ideas. This mental filtering overhead reduces attention and engagement across all content.

For builders in the content space, this represents both threat and opportunity. Products that solve the trust problem gain competitive advantage as readers actively seek trustworthy sources. These solutions include verified human authorship, transparent AI usage, or community validation.

The second-order effect hits search and social platforms. When AI content floods search results and social feeds, the platforms lose utility. Users shift toward curated sources, newsletter subscriptions, and direct relationships with trusted creators. Distribution power moves away from algorithmic feeds back to human curation.

What Koebler captured is the user experience of this transition. Reading online becomes work rather than discovery. The internet shifts from infinite content library to adversarial environment where you must constantly evaluate source credibility.

The companies that win will be the ones that solve the trust problem rather than contributing to it. Transparency beats sophistication when readers can't tell what's real anymore.

---

### What to do this week

**Audit your team's coordination overhead** (2 hours). Track time spent in status meetings, Slack updates, progress reports, and cross-team handoffs this week. Calculate the actual hours, not estimates. Most teams discover 30-40% of engineering time goes to coordination rather than building. This baseline helps you identify which processes AI agents could eliminate first.

**Test Notion's custom agents feature** (1 hour setup). Build an agent that pulls from your existing tools. Include GitHub issues, Slack messages, and calendar events to generate daily team updates automatically. Start with read-only data sources to avoid shift. The goal is proving that agents can handle routine information gathering that humans currently spend 30+ minutes per day coordinating manually.

**Implement one "public by default" AI experiment** (ongoing). Follow Shopify's pattern: pick one AI workflow your team uses privately and make it visible to other departments. Create a shared Slack channel where your AI agent interactions happen in public. Let other teams observe how you prompt, iterate, and handle edge cases. This accelerates organization-wide AI adoption without formal training programs.

The pattern across all three actions is measurement-first implementation. You cannot manage what you do not measure, and most teams underestimate how much time they spend on coordination versus creation. AI agents excel at eliminating coordination overhead, but only if you first understand where that overhead actually lives in your current workflows.
