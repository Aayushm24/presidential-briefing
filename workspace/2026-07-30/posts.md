# LinkedIn posts, 2026-07-30 (iteration 2)

**Lead:** Practitioners can extract dramatically better AI performance today through configuration and tooling rather than waiting for new models
**Briefing type:** pattern
**Best option:** 2 (pre-council self-score)

---

## OPTION 1, Contrarian Philosopher (hook score: 8)

**Conviction:** L2: Most teams focus on prompt engineering while completely ignoring the API configuration settings that can triple performance without changing models.

**Post:**
Everyone's waiting for GPT-6.

Meanwhile, OpenAI just proved two API flags can triple benchmark performance.

i see it across every builder i talk to. Same models, same prompts, wildly different results.

The gap lives in the harness around the model, not the model itself.

OpenAI enabled reasoning retention and compaction on GPT-5.6. Performance jumped from 32% to 91% on ARC-AGI-3. No new training. No months of compute. One API call.

Here's what happened:
- Reasoning retention keeps step-by-step thinking visible between calls
- Compaction reduces repetitive token usage during inference
- Together they changed how the model processes complex reasoning

Training GPT-5.6 took months and cost millions. Enabling two flags cost nothing extra.

At Atlan, we've been building agents for months and this tracks. Teams shipping mediocre AI products versus high-performing ones differ on configuration, not compute.

Most teams treat API parameters as an afterthought. That's backwards.

The performance delta from configuration tuning matches what most teams expect from waiting for GPT-6.

Config parameters give you immediate performance gains while you wait for model upgrades. The teams optimizing both layers compound their advantages faster.

Try temperature, top-p, reasoning retention on your next API call. Same model, different results.

What API settings are you not testing?

---

## OPTION 2, Personal-i Observer (hook score: 9)

**Conviction:** L3: The harness engineering gap between teams is becoming the thing competitors can't copy. Model access is commodity, prompts are commodity, but the infrastructure around API calls compounds.

**Post:**
i watch teams use identical models and get completely different results.

Same GPT-5.6. Same basic prompts. But one team's agents work 3x better.

The difference lies in what happens when your API call completes.

Every week i see builders focus on prompt engineering while completely ignoring:
- Configuration parameters that can triple performance
- MCP servers that bridge custom tools
- Statistical testing infrastructure that catches what manual testing misses

OpenAI just proved this with ARC-AGI-3. Two API flags, reasoning retention and compaction, jumped performance from 32% to 91%.

The mechanism is straightforward. Without retention, the model discards reasoning steps between calls. With it enabled, context carries forward. Compaction optimizes token usage of that retained reasoning.

When we build agents at Atlan, we don't have them click buttons. They call APIs, read databases, talk to other apps through MCPs. The humans never open the app when the agent is working.

Simon Willison just documented how to add custom MCP servers to both ChatGPT and Claude. Instead of copy-paste between your AI chat and your actual tools, they get full workflow completion in one session.

The best-performing teams already do statistical evaluation. Anthropic runs constitutional AI with proper benchmarks. OpenAI publishes results with error bars. The tooling is catching up to make this accessible.

Manual testing might improve performance 10%. Statistical testing with proper controls adds another 15%. Configuration tuning might add 25%. MCP tool integration could add 20% more.

You don't get linear addition. You get multiplication across the performance stack.

Instead of waiting for Claude-5, you can get 50-100% performance improvements from better harness engineering today.

What does your team remember from last quarter's AI experiments?

---

## OPTION 3, Absurdist Truth-Teller (hook score: 8)

**Conviction:** L1: Teams treat AI like a magic eight-ball when a database is the better mental model, with proper configuration, indexing, and connection management.

**Post:**
Someone just spent $180 per million tokens to ask Claude the same question 47 times.

Because they didn't know about reasoning retention settings.

i broke GPT once asking how many r's are in strawberry. It said 2. S-T-R-A-W-B-E-R-R-Y. There are 3.

Better configuration fixed it, not a better model.

i watch teams building AI products focus on prompts like they're crafting magic spells. But the real magic happens in the parameters you pass to the API.

OpenAI just proved it with two settings that tripled ARC-AGI-3 performance:
- Reasoning retention (keeps thinking visible)
- Compaction (reduces repetitive tokens)

Same model. Same training. Different configuration. 32% to 91% accuracy jump.

My mom asked AI to cancel her dentist appointment. It wrote a LinkedIn message. 147 words. 3 paragraphs. "i am writing to formally request..."

She deleted all of it. Typed "can't make Saturday." Sent.

Every AI tool i touch breaks the same way. Rocket engines on bicycles.

At Atlan, i've built agents that handle chat, research accounts, write personalized emails. The pattern that works treats AI like infrastructure, not magic.

Statistical testing instead of manual validation. MCP integrations instead of copy-paste workflows. Configuration tuning instead of prompt optimization.

Ethan Mollick's team released the AI Behavioral Observatory. It runs hundreds of test cases with proper randomization. You get "Version B improved accuracy by 12% with 95% confidence" instead of "Version B seemed better."

Teams that figure out harness engineering first build a lead that model upgrades alone won't close.

What's the ugliest workaround in your current AI setup? 👀
