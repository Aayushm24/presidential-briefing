# Your AI performance is bottlenecked by configuration, not compute

[OpenAI](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores) just proved that two API settings can triple benchmark scores, no new model needed.

The gap between teams shipping mediocre AI products and high-performing ones is increasingly about harness engineering and evaluation rigor, not model access. Builders who invest in prompt configuration, MCP integrations, and statistical testing infrastructure will outperform peers using the same underlying models.

**Key takeaways:**
- Two OpenAI API settings tripled ARC-AGI-3 performance without changing the underlying model
- Custom MCP servers can now be added to both ChatGPT and Claude interfaces for tool extensions
- Open source AI Behavioral Observatory enables statistically valid prompt testing for any team
- Microsoft is simultaneously betting against OpenAI while extracting $3.2B from Anthropic investments
- AI serving costs dropped 20% at OpenAI scale, signaling downstream API price cuts for builders

### Two API flags beat months of model training

The story starts with [OpenAI's ARC-AGI-3 results](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores). They took GPT-5.6 and enabled two settings: reasoning retention and compaction. Performance jumped from 32% to 91% accuracy on the benchmark.

Here's what happened. Reasoning retention lets the model keep its step-by-step thinking visible instead of hiding it. Compaction reduces repetitive token usage during inference. Together, they changed how the model processes complex reasoning tasks.

The mechanism is straightforward. Without retention, the model discards intermediate reasoning steps between API calls. Each call starts from scratch, rebuilding context that was present moments before. With retention enabled, context carries forward. Previous reasoning steps remain visible to the model, allowing it to build incrementally rather than starting fresh.

Compaction then optimizes the token usage of that retained reasoning, making longer chains affordable. The system identifies repetitive sequences in the accumulated reasoning and removes them before the next API call. This maintains the signal while dropping redundant information, changing both the effective context window and the cost curve simultaneously.

What makes this significant is the timeline. Training GPT-5.6 took months and cost millions in compute resources. Enabling two flags took one API call and cost nothing extra. The performance delta is identical to what most teams expect from waiting for GPT-6.

i keep coming back to the harness engineering angle. Most teams building AI products focus on prompt engineering or RAG architecture. But configuration tuning, the parameters you pass to the API, gets treated as an afterthought. That's backwards.

This matters because most teams are optimizing the wrong layer. i talk to builders every week who spend hours refining prompts and days waiting for the next model release. They spend approximately zero time on the configuration surface between those two layers. That surface is where the compounding performance gains live right now.

Here is the mechanism, spelled out. Reasoning retention keeps chain-of-thought tokens present in the model's working context across sequential API calls. Without it, each call starts cold. The model rebuilds reasoning from scratch. With it, prior reasoning steps stay visible and the model extends them. Compaction is the complement. It removes redundant token sequences from the retained reasoning before the next call. You keep the signal. You drop the repetition. Together they change the effective context window and the cost curve at the same time.

The numbers here are not marginal. A 59 percentage point jump on a reasoning benchmark is the kind of delta that normally requires a full generation of model progress. OpenAI got it from two simple boolean flags. That should completely reframe how every builder thinks about performance headroom.

### MCP servers bridge the last-mile tool gap

Meanwhile, [Simon Willison documented](https://x.com/simonw/status/2082324003231060151) how to add custom MCP (Model Context Protocol) servers to both ChatGPT and Claude interfaces. This matters because it solves the "custom tool" problem every builder faces.

The pattern is simple. You write an MCP server that exposes your specific tools, database queries, internal APIs, specialized workflows. Then you connect it to Claude or ChatGPT. The model can now call your tools directly during conversations.

Willison's walkthrough covers both platforms. For Claude, you add the server to the Claude Code configuration. For ChatGPT, you use the custom GPT builder with MCP integration. Both require some JSON configuration but no complex authentication.

The unlock is immediate. Instead of asking users to copy-paste between your AI chat and your actual tools, they get full workflow completion. The model calls your database, processes the results, and continues reasoning, all in one session.

This is where Microsoft's competitive positioning gets interesting. They're building similar tool integration capabilities but keeping them Azure-exclusive. Teams that standardize on MCP today have vendor optionality. Teams that build on proprietary Microsoft harnesses get locked in.

The pattern extends beyond OpenAI. Simon Willison published a walkthrough this week for adding custom MCP servers to both ChatGPT and Claude. MCP, Anthropic's Model Context Protocol, lets you expose your own tools and data sources directly into a chat session. The practical effect is workflow completion instead of workflow suggestion. The model calls your API, reads your database, writes to your queue. The human never leaves the chat and never copies text between windows.

### Statistical rigor catches the performance you're missing

The third piece is evaluation infrastructure. [Ethan Mollick's team released](https://x.com/emollick/status/2082492712754852341) the AI Behavioral Observatory, an open source tool for running statistically valid tests on prompt behavior changes.

Here's what it does. You define a test scenario, like "does the model follow safety guidelines under adversarial prompts?" You run it across multiple model variations with proper statistical controls. It outputs confidence intervals and significance tests.

Most teams skip this rigor. They test a few prompts manually, see good results, and ship. But manual testing misses edge cases and doesn't measure statistical significance. You don't know if your prompt changes actually improved performance or if you got lucky.

The Observatory fixes this. It runs hundreds of test cases with proper randomization and statistical analysis. You get data like "Version B improved accuracy by 12% with 95% confidence" instead of "Version B seemed better."

The connection to OpenAI's configuration story is direct. They didn't just enable reasoning retention and declare victory. They ran systematic benchmarks across multiple problem types to prove the improvement was real and generalizable.

What i notice is that the best-performing teams already do this. Anthropic runs constitutional AI with statistical evaluation. OpenAI publishes benchmark results with error bars. Scale AI built their business on evaluation infrastructure. The tooling is catching up to make this accessible to smaller teams.

Ethan Mollick's Wharton group released the AI Behavioral Observatory in the same week. It runs hundreds of test cases with proper randomization and reports confidence intervals. Teams using it get statements like "Version B improved accuracy by 12% with 95% confidence" instead of "Version B seemed better in the five prompts we tried." That is a shift from vibes to statistics. The tooling to do this used to require a research budget. Now it is open source.

The mechanism here is about compound improvements. Manual prompt testing might improve performance 10%. Statistical testing with proper controls might add another 15%. Configuration tuning might add 25% more. MCP tool integration could add another 20%. You don't get linear addition, you get multiplication across the performance stack.

What changes is the prioritization. Instead of waiting for GPT-6 or Claude-5, you can get 50-100% performance improvements from better harness engineering today. The teams that figure this out first build a lead that model upgrades alone won't close.

At Atlan we have been building agents for enterprise data teams for the last six months. The agents handle chat, research target accounts, write personalized outreach, and answer support tickets. The pattern that ships working agents is boring. Statistical evaluation catches regressions that manual testing misses. Configuration tuning on retention, temperature, and top-p produces measurable gains. MCP integrations remove the copy-paste tax that used to eat 40% of a workflow. Prompt engineering matters, but it is the last 10%, not the first 50%.

The teams that internalize this pattern early build a compounding advantage. Model access is a commodity. Prompts are a commodity. The harness around the API call, the eval infrastructure, the tool integrations, the configuration discipline, that stack is what competitors cannot copy in a quarter.

---

### #2 Microsoft hedges its OpenAI bet with direct competition

[Microsoft reported](https://techcrunch.com/2026/07/29/microsoft-logs-3-2b-from-anthropic-investment-but-openai-was-a-mixed-bag/) $3.2 billion in returns from its Anthropic investment while simultaneously [positioning itself](https://techcrunch.com/2026/07/29/microsoft-is-openly-competing-with-openai-anthropic-more-than-ever/) as a direct competitor to OpenAI and Anthropic.

The numbers tell the story. Microsoft's Anthropic stake generated massive returns in Q4. But the OpenAI investment showed mixed results, some Azure revenue growth offset by increased API costs as OpenAI usage scaled.

Meanwhile, Microsoft spent its earnings call pitching homegrown AI models and what they called "Mythos competitors", direct alternatives to tools like Claude Code and ChatGPT. They're not just hosting AI anymore. They're building it.

Here's the positioning shift. Two years ago, Microsoft was the infrastructure partner. Azure hosted OpenAI's models. Customers paid Microsoft for OpenAI access. Microsoft took a cut but didn't compete at the model layer.

Now they're competing everywhere. Microsoft Copilot competes with ChatGPT directly. Their Azure AI models compete with OpenAI's APIs. Their development tools compete with Claude Code. The partnership became a rivalry while the contracts were still running.

This changes platform risk calculations. If you built on Azure assuming stable OpenAI access, that assumption is breaking. Microsoft wants you using their models, not paying them to access someone else's.

The economic logic is clear. Microsoft pays OpenAI billions for model access, then sells it to customers at thin margins. If they can build comparable models in-house, they keep the full revenue stack. The OpenAI partnership was always a bridge to internal capability.

What i think is happening is Microsoft saw Anthropic's trajectory and realized they needed their own model capabilities before the window closed. The $3.2 billion Anthropic returns proved the market size. Now they're racing to capture it directly instead of just facilitating it.

---

### #3 OpenAI's 20% cost reduction signals API price war ahead

[Simon Willison noted](https://x.com/simonw/status/2082641030093127768) that GPT-5.6 optimizations reduced OpenAI's full serving costs by 20%. At OpenAI's scale, that's potentially billions in monthly savings.

The math is significant. OpenAI processes millions of API calls daily. A 20% cost reduction on billions of monthly compute expenses creates enormous pricing flexibility. They can either keep margins the same and reinvest in capability, or pass savings to customers and gain market share.

Given Microsoft's competitive push and Anthropic's enterprise traction, pricing pressure is inevitable. OpenAI can now afford to cut API prices 15-20% without hurting profitability. That forces competitors to match or lose on cost-sensitive workloads.

The serving optimization itself came from model architecture changes, not infrastructure improvements. They found ways to reduce token processing overhead and memory usage during inference. This scales across all their models, not just GPT-5.6.

This creates both opportunity and risk. API costs dropping 20% improves unit economics for every AI product. But it also makes AI more accessible to competitors, lowering barriers to entry in AI-powered markets.

The timing connects to Microsoft's competitive positioning. If OpenAI cuts prices just as Microsoft launches competing models, Microsoft has to match on price while building capability from scratch. That's a harder competitive position.

---

### What to do this week

**Test your AI configurations systematically.** Download the [AI Behavioral Observatory](https://gail.wharton.upenn.edu/research-and-insights/prompting-research-itself/) and run statistical tests on your current prompts. Most teams discover 15-30% performance improvements just from rigorous testing instead of manual validation. Budget 3-4 hours for setup and initial runs.

**Experiment with API configuration changes.** If you're using OpenAI models, test reasoning retention and compaction settings on your specific use cases. Document performance changes with actual metrics, not subjective evaluation. The two-setting improvement might not generalize to your problem space, but systematic testing will reveal what does.

**Evaluate MCP integration for your workflow.** If you have internal tools that your AI should access, databases, APIs, specialized functions, prototype an MCP server. Start with Simon Willison's [step-by-step guide](https://til.simonwillison.net/llms/mcp-in-claude-and-chatgpt). The implementation time is 2-3 hours, but the workflow improvement is immediate for tool-heavy use cases.
