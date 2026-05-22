# AI agents split into two markets by compute costs

[Daytona](https://www.latent.space/p/daytona) hit 850K daily agent runs with 74% month-over-month growth while [Ethan Mollick warned](https://x.com/emollick/status/2057565824341127432) the richest companies will get agents and everyone else gets chatbots.

Compute scarcity is forcing builders to choose their lane now. Invest in efficient small-model agentic stacks for broad deployment, or accept that full agentic workflows become premium products for well-funded customers. There is no middle ground as compute costs bite. The infrastructure is mature enough to make this choice permanent.

**Key takeaways:**
- Agent sandbox infrastructure is hitting real scale (Daytona: 850K daily runs, 74% MoM growth) while compute becomes expensive enough to create two-tier market split
- Microsoft ships small-model agents (MagenticLite) that work across browser and filesystem, proving efficient agent workflows are possible without frontier pricing
- Simon Willison releases production SQLite agents, showing the data exploration layer is ready for builders today
- Compute shortage will price out most teams from complex agentic workflows while single-turn chatbots get cheaper, creating strategic forcing function for product decisions

### The numbers prove agents are crossing into production

[Ivan Burazin at Daytona](https://www.latent.space/p/daytona) dropped the kind of metrics that separate real traction from demo theater. 850,000 daily runs. 74% month-over-month growth. Agent sandboxes running across bare metal infrastructure with reinforcement learning evaluation loops.

These aren't experimental numbers. This is builders running agents in production workflows every single day. When Ivan talks about their agent cloud handling nearly a million daily executions, he's describing infrastructure that already crossed from research to operational scale. The sandbox layer that every agent builder needs is no longer theoretical.

The mechanism behind these numbers reveals why agent infrastructure finally reached production readiness. Daytona solved the three core problems that killed previous agent platforms: security isolation, resource management, and evaluation feedback loops. Their bare metal sandboxes give AI agents full compute environments without risking host system contamination. Their orchestration layer manages CPU and memory allocation so agents can't monopolize resources or crash other workloads. Their RL evaluation system continuously measures agent performance and feeds that data back into training loops.

Each technical component addresses a specific failure mode that developers encountered when trying to deploy agents in real applications. Security isolation prevents agents from accessing sensitive data or modifying system files outside their designated workspace. Resource management prevents runaway agents from consuming infinite CPU cycles or memory. Evaluation feedback loops catch agents that produce incorrect outputs before those outputs reach end users.

What I keep coming back to is how these infrastructure metrics emerged during the exact same period when compute costs started forcing architectural decisions across the AI ecosystem. The timing isn't coincidental. Teams building agents discovered they need two things simultaneously: reliable sandboxing infrastructure and sustainable compute cost structures. Daytona solved the first problem by building specialized infrastructure. The second problem is where the market splits in half.

The operational scale behind 850K daily runs creates network effects that benefit every team building on the platform. More agent executions generate more training data for the RL evaluation systems. More training data improves agent performance across different use cases. Better performance attracts more developers to the platform. More developers create more diverse agent workloads that stress-test the infrastructure and reveal new optimization opportunities.

The causal chain forward reveals why these infrastructure metrics signal a permanent shift rather than temporary traction. When agent sandbox providers hit operational scale, they create the foundation for every downstream agent product. But foundation infrastructure only matters if teams can afford to run agents on it regularly without hitting cost barriers that limit their user base or require venture funding to subsidize operations.

The companies that commit to efficient agent architectures now will own the broad market because they can serve price-sensitive customers profitably. The companies that bet on maximum agent capability regardless of cost will own the premium segment because they can deliver superior experiences for customers willing to pay higher prices. There's no middle path because compute physics creates a binary choice between efficiency and capability at scale.

This traces directly to small teams beating large organizations through AI multiplication effects. A 3-person startup using Daytona's efficient agent infrastructure can ship agent-powered features faster than a 50-person team that hasn't solved the sandbox problem. But only if their compute architecture scales with their user base without requiring external funding to cover operational costs. Teams that pick expensive agent architectures will hit cost walls that force them to either raise venture funding or scale back their agent features. Teams that pick efficient architectures can grow organically and reinvest revenue into better product experiences.

### Microsoft proves small models can run agents well enough

[Microsoft Research shipped MagenticLite](https://www.microsoft.com/en-us/research/blog/magenticlite-magenticbrain-fara1-5-an-agentic-experience-optimized-for-small-models/) this week with a claim that sounds impossible at first. Small models can power agentic workflows across browsers and local file systems in a single integrated experience. These are full agents that navigate web interfaces, manipulate local files, and maintain context across different applications.

The technical breakthrough that makes this work challenges the foundational assumption that drove most agent development over the past two years. Instead of using one large model to handle all agent capabilities, Microsoft built specialized small models that each excel at narrow tasks, then orchestrated them through a coordination layer that maintains state and handles handoffs between models.

MagenticLite's architecture reveals why this approach delivers better cost efficiency without sacrificing user experience. The web navigation model focuses purely on understanding DOM structures, identifying interactive elements, and executing actions on web pages. It doesn't need to understand natural language reasoning or file system operations. The filesystem model specializes in file manipulation, directory traversal, and local data management. It doesn't need web browsing capabilities. The natural language processing model handles user intent understanding and response generation. It doesn't need to interact with external systems directly.

Each specialized model can be smaller, faster, and cheaper to run than a general-purpose frontier model that tries to handle all these capabilities simultaneously. The orchestration layer coordinates between models by maintaining shared state, routing tasks to appropriate specialists, and ensuring that data flows correctly between different components of the agent workflow.

This isn't a research demo optimized for benchmarks. Microsoft built MagenticLite as a production system designed for daily use across common workplace tasks. The system demonstrates agent workflows that most knowledge workers actually need: browse to a website to research a topic, extract relevant information from that website, save the information to local files with appropriate organization, then use those files as inputs for subsequent analysis or reporting tasks.

The cost implications become clear when you compare compute requirements. A frontier model handling these tasks through multiple API calls might consume 50-100x more compute resources per user session than MagenticLite's orchestrated small-model approach. At scale, this cost difference determines whether agent features can be offered to broad consumer markets or must be restricted to premium enterprise customers willing to pay higher prices.

What this forces next is a fundamental rethinking of agent architecture patterns across the entire ecosystem. Teams that built their agents around single large models will need to choose between refactoring toward Microsoft's orchestrated approach or accepting that their compute costs limit their addressable market to well-funded customers. Teams that haven't shipped agents yet can skip the expensive architecture entirely and build on small-model orchestration foundations from day one.

The mental model shift for builders is more significant than it appears. Instead of asking "which large language model should power our agent?" the key questions become: "which specific tasks does our agent need to perform?", "which small models excel at each task?", and "how should we orchestrate between models to maintain user experience quality?" This architectural change reduces compute costs by orders of magnitude while preserving the agentic user experience that distinguishes these products from basic chatbots.

For teams already building agents, Microsoft's approach provides a clear upgrade path from expensive to efficient architectures. For teams planning their first agent products, it removes the cost barrier that previously limited agent features to venture-funded startups or enterprise-focused companies with high-value customers willing to pay premium prices.

### The two-tier split is already here

[Ethan Mollick's observation](https://x.com/emollick/status/2057565824341127432) cuts straight to the strategic reality most builders are avoiding. We're quite short of compute. Complex agentic workflows will become expensive even as single-turn chatbots get cheaper. The richest companies will get AI agents while everyone else gets stuck with basic chatbots.

This describes what's happening right now across the AI ecosystem. Teams building sophisticated agent workflows are hitting compute costs that force them to limit features, raise prices, or reduce their user base. Meanwhile, single-turn AI applications can serve millions of users profitably because they don't require the multi-step reasoning and context management that agents need.

The market bifurcation creates a permanent strategic choice for every builder. Chase maximum agent capability and accept that your product serves a premium market segment. Or optimize for efficiency and serve the broad market with good-enough agent experiences. There's no middle ground because compute physics creates a discontinuous cost structure between simple and complex AI workflows.

What's forcing this split now is the collision between increasing demand for agent features and limited GPU availability across cloud providers. When OpenAI, Anthropic, Google, and Microsoft are all competing for the same finite compute resources, the price signals propagate down to every application layer. Teams building agents feel this as higher API costs per user session, longer response times during peak usage, and rate limits that kick in earlier than they used to.

The causal chain forward reveals why this becomes a permanent competitive advantage for teams that choose correctly. Builders who commit to efficient agent architectures now will have sustainable unit economics when compute costs rise further. Builders who optimize for capability without considering efficiency will either need venture funding to subsidize their compute costs or will need to raise prices high enough to limit their market to well-funded enterprise customers.

This creates two distinct product categories that serve different market segments permanently. Premium agent products that deliver maximum capability for customers willing to pay higher prices. Efficient agent products that deliver good-enough capability for price-sensitive markets. Teams that try to serve both segments will get squeezed by the compute cost structure and will eventually need to pick a lane.

---

### Simon Willison ships SQLite agents for production data work

[Simon Willison released Datasette Agent](https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything) this week after three years of building his LLM Python library. The announcement reads like a quiet milestone, but it represents something significant. The first production-ready AI agent specifically designed for data exploration and analysis.

Datasette Agent provides conversational interfaces for asking questions of structured data stored in SQLite databases. Add the datasette-agent-charts plugin and it generates visualizations of your data as well. This isn't a research prototype or a startup's demo. It's a mature tool built by someone who has been shipping production AI applications since before the current wave of excitement.

What makes this release important is the gap it fills between AI capabilities and actual data work. Most teams building on AI APIs can create chatbots that answer questions about text. Far fewer teams have solved the problem of letting AI agents explore structured data safely and effectively. Simon solved both the technical challenges and the practical deployment challenges that prevent most database agents from working reliably.

The technical approach reveals why database agents have been harder to build than text-based agents. Conversational data interfaces need to translate natural language questions into precise SQL queries, execute those queries safely without risking data corruption, and present results in formats that non-technical users can interpret. Each step requires different types of AI capabilities coordinated through a reliable orchestration layer.

Simon's implementation handles the safety and reliability concerns that most database agent projects skip. The system validates SQL queries before execution to prevent destructive operations. It manages database connections to avoid overloading the underlying data store. It formats query results in ways that make sense for conversational interfaces rather than dumping raw SQL output into chat responses.

The broader implication is that the data exploration layer is ready for builders to ship today. Teams that need to let their users ask questions of structured data can now deploy a proven solution instead of building database agents from scratch. This removes a significant barrier for product teams that want to add AI-powered data features but lack the database expertise to build safe conversational SQL interfaces.

---

### Trump delays AI security executive order, removes compliance blocker

President Trump delayed signing an executive order that would have required pre-release government security reviews of AI models. [The delay removes](https://techcrunch.com/2026/05/21/trump-delays-ai-security-executive-order-i-dont-want-to-get-in-the-way-of-that-leading/) a near-term compliance burden that was creating uncertainty for AI builders shipping to government and enterprise customers.

The executive order would have established mandatory security assessments for AI models before they could be deployed in federal systems or sold to federal contractors. Teams building AI applications for government markets were preparing for review processes that could add months to their deployment timelines. The delay eliminates this bottleneck for the immediate future.

What's significant about the timing is how it removes regulatory friction during the period when AI teams are making fundamental architecture decisions. Companies building agent systems can now focus on technical and business challenges without needing to factor pre-release government reviews into their development timelines. This is particularly relevant for startups that were considering avoiding government markets entirely to sidestep compliance complexity.

The mechanism behind the delay reveals the ongoing tension between AI safety regulation and American competitive positioning in AI development. Trump cited dissatisfaction with the order's language and concern about creating blockers for American AI leadership. This suggests that future AI regulation will prioritize maintaining competitive advantages over implementing precautionary security measures.

For builders, this creates a temporary window where government and enterprise AI deployments face fewer regulatory barriers. Teams that can ship AI solutions to federal agencies and large enterprises during this period may establish market positions that become harder to displace once regulatory frameworks eventually stabilize.

The causal chain forward points toward an eventual return to security-focused AI regulation, but with approaches designed to preserve American AI advantages rather than slow down development. This means teams should expect future compliance requirements to focus on auditing and monitoring deployed systems rather than blocking pre-deployment reviews that could create competitive disadvantages.

---

### What to do this week

**Test Datasette Agent on your structured data** (15-minute setup). If your product works with databases or structured data files, [install Datasette Agent](https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything) and test it against a sample of your actual data. This will show you whether conversational data interfaces could improve your user experience and what types of questions your users might ask. The plugin architecture means you can extend it for your specific data schemas and business logic.

**Audit your current agentic workflows for compute costs versus outcomes**. List every AI feature in your product that requires multiple API calls or complex reasoning. Calculate the actual compute cost per user session for each feature. Compare those costs against the value delivered to users and the price you can charge. Features with poor cost-to-value ratios should either be redesigned around smaller models or repositioned as premium offerings.

**Choose your agent architecture lane based on your market and funding strategy**. If you're targeting broad consumer markets or building without significant venture funding, commit to efficient small-model architectures like Microsoft's MagenticLite approach. If you're serving enterprise customers who pay premium prices for maximum capability, invest in frontier model architectures but price them to cover compute costs. Teams that try to serve both markets will get squeezed by the compute cost structure as the two-tier split deepens.
