# Shopify's CTO just revealed when enterprise AI went from experiment to infrastructure

[Mikhail Parakhin, Shopify's CTO, sat down with Latent Space](https://www.latent.space/p/shopify) and shared something rare: hard numbers on enterprise AI adoption inside one of the largest e-commerce companies in the world.

The headline: Shopify's token usage did not grow gradually. It exploded in December 2025. And the trigger was not a new model release. It was an internal decision to give every team unlimited Opus-4.6 tokens.

This matters because most companies are still rationing AI access. They hand out seats, cap monthly spend, run ROI reviews on individual pilots. Shopify ran the opposite experiment and got the data every AI buyer has been asking for.

**Key takeaways:**
- Shopify removed token budget limits in late 2025 and watched internal usage explode in December, a phase transition rather than a gradual ramp
- [OpenAI shipped workspace agents inside ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt) that run in the cloud and automate workflows across tools, direct pressure on Zapier, n8n, and Notion
- [Qwen3.6-27B](https://simonwillison.net/2026/Apr/22/qwen36-27b/#atom-everything) claims flagship-level agentic coding in a 27B open-weight model that beats the previous 397B-parameter Qwen flagship
- [Ethan Mollick](https://x.com/emollick/status/2046979551046013125) points out every system regulated by human effort cost is now breaking under AI's zero-effort floor
- The common thread this week: the buyers treating AI as infrastructure are pulling away from the ones treating it as a tool

### Why Shopify ran the unlimited-tokens experiment

Most engineering leaders I talk to are stuck in the same loop. They buy Claude or GPT seats for a team. They watch the first few enthusiastic users burn through monthly budget by day 10. Finance escalates. IT writes a usage policy. Everyone else stays cautious, rations their queries, and the tool never reaches the point where it changes how work gets done.

Parakhin described the same pattern at Shopify earlier in 2025. Teams were experimenting, but nobody was building AI into the default workflow. The usage graphs were flat. Engineers treated every Opus call like it was coming out of their own pocket.

So Shopify made a call that sounds reckless on paper and obvious in hindsight. They told every team inside the company to stop rationing. Unlimited Opus-4.6 tokens. Do not worry about the bill. If you think AI can help with this task, just use it.

December 2025 is when the graphs broke. The shape was a vertical wall, not a trend line going up. Teams that had been tentatively running a few prompts a day started running thousands. Workflows that used to take a day started shipping in an hour. The ratio of AI-assisted code commits inside Shopify jumped from a minority to a majority in under three weeks.

I doubt this would have worked in 2024. The capability floor was not there yet. Opus-4.6 had crossed some internal threshold at Shopify where engineers stopped second-guessing its output on real production code, and once that trust existed, the only remaining barrier was the budget anxiety. Remove the anxiety, and the usage finds its natural level.

That natural level turned out to be enormous.

### The economics of artificial scarcity

There is a deeper point buried in Parakhin's data that most coverage is going to miss.

When Shopify rationed tokens, they were not optimizing for cost. They were creating artificial scarcity that obscured the actual ROI. Because teams were being careful, they only used AI on the tasks where they were sure it would work. That meant the usage data showed only the high-confidence use cases. Which meant the ROI always looked like "nice to have" rather than "fundamental shift."

The unlimited budget was not an AI experiment. It was a measurement experiment. Shopify wanted to see what usage looked like when friction and anxiety were removed, so they could decide how to think about AI spend going forward.

The answer they got is the one every AI infrastructure team is now reverse-engineering from Shopify's leak: if you give engineers real access, AI becomes the default execution surface for anything involving text, code, data, or decisions. It stops being a tool you reach for and becomes the layer underneath everything.

This is the part that matters for anyone sizing their own AI spend. If your token usage is tidy and predictable and your teams are reporting "thoughtful adoption," you have not actually measured demand. You have measured rationing. The real demand shows up only when you remove the constraint, and then it looks like December 2025 at Shopify.

The strategic question that follows is uncomfortable. Shopify is Shopify. They can absorb a token bill. Can your company? If the answer is no, the next question is whether your competitors who can absorb that bill are about to pull three years ahead of you on productivity per engineer.

### Why this connects to the dev tool consolidation

The other thing that jumped out at me in Parakhin's interview is how the enterprise picture lines up with what is happening in the developer tool market right now.

[Cursor just locked in a $10 billion collaboration deal with SpaceX](https://techcrunch.com/2026/04/22/how-spacex-preempted-a-2b-fundraise-with-a-60b-buyout-offer/) with a $60 billion acquisition option on top. [Tom Tunguz broke down the math](https://x.com/ttunguz/status/2046815672957870276): Cursor is at roughly $2 billion ARR. That's the revenue profile of infrastructure, not an IDE.

You cannot get to $2B ARR on developer tools with a rationing mindset. That number requires thousands of companies doing exactly what Shopify did internally: treating AI coding as a default surface, not a cautious experiment. The SpaceX deal is the public market signal that Shopify's private data proves out.

Taken together, these are two views of the same shift. Shopify shows what usage looks like when the budget constraint disappears inside a company. Cursor's revenue shows what the aggregate bill looks like when thousands of companies hit that same point at once.

For builders, the read here is that the AI adoption curve is not gradual. It is a step function. Most of a company's adoption happens in the week after they stop rationing. And the companies hitting that step in 2026 are building a compounding lead on the ones still running pilot programs.

### OpenAI's workspace agents want to own the automation layer

The second big move this week is [OpenAI launching workspace agents inside ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt). On the surface it looks like another product release. One layer down, it is a direct attack on Zapier, n8n, Notion's automation features, and anyone else sitting in the business-workflow automation layer.

These agents are Codex-powered, which is the detail that matters. They can run in the cloud, persist state between sessions, and write their own automation logic on the fly rather than relying on a pre-built connector library. You describe a workflow in natural language, "when someone fills out this form, create a record in Salesforce, send the account team a Slack message, generate a first-draft proposal," and the agent assembles the pipeline.

That is a completely different shape of product from Zapier. Zapier's defensibility came from its connector library. Workspace agents bypass the library by writing the integration code when needed. If a tool has an API, the agent can hit it. If it has a web interface, the agent can drive a browser.

The strategic play is obvious if you step back. OpenAI started by selling model access to companies like Zapier. Then they built ChatGPT to own the consumer interface. Now they are reaching into the workflow surface itself. This is the standard platform playbook: enable the ecosystem, watch where the value concentrates, then build directly in those layers.

For anyone building in the automation or workflow space, the question is not whether OpenAI will come for your category. It is how fast. The teams that survive this wave will be the ones who picked a layer OpenAI does not want to own: deep enterprise compliance, regulated industry workflows, legacy system integration, or verticalized playbooks that require domain knowledge OpenAI does not have.

Horizontal "connect anything to anything" automation is now a platform battle, not a startup opportunity.

### Qwen3.6-27B puts flagship coding inside an open-weight model

The third story worth slowing down on is [Qwen's new 27B release](https://simonwillison.net/2026/Apr/22/qwen36-27b/#atom-everything). The claim, which Simon Willison is treating with appropriate skepticism but takes seriously, is that Qwen3.6-27B matches or beats the previous generation Qwen3.5-397B-A17B flagship on every major coding benchmark.

Read that number again. A 27 billion parameter dense model is claiming to outperform a 397 billion parameter mixture-of-experts model from the same team, one generation back. And the weights are open. You can download them and run them on reasonable hardware.

If the benchmarks hold up in practice, this changes the economics of agentic coding for anyone who does not want to send their code to a third-party provider. The compute you need for flagship-level coding just dropped by more than an order of magnitude. That puts it inside the range of what a single serious workstation can run locally, or what any team with a modest GPU budget can host on their own infrastructure.

The business implication lines up with the Shopify story. One of the main frictions on unlimited-token experiments is the vendor bill. If you can run a model that is close-enough to frontier on your own hardware for a fixed cost, the token-anxiety barrier that Shopify had to explicitly remove just disappears for free. You get the unlimited-access experiment without the unlimited-access spend.

I doubt the closed frontier labs are going to let this stay true for long. There is a reason Anthropic and OpenAI have been pushing hard on memory, tools, and agent infrastructure rather than raw model capability. The model layer is compressing fast, and the labs that built their business on a model capability lead are visibly pivoting toward product advantages instead.

For builders right now, Qwen3.6-27B is worth an afternoon of testing. If it performs as claimed on your actual codebase, that is a meaningful shift in the cost structure of anything you are trying to build with local or private inference.

### What to do this week

First, run a small-scale version of the Shopify experiment. Pick one team inside your company. Give them unlimited Claude or GPT budget for two weeks. No questions about spend. Track what they build. You are not measuring cost, you are measuring what demand looks like when anxiety goes away. That data is the input to every AI budget conversation you have for the rest of the year.

Second, go look at your automation stack. If you are paying for Zapier or n8n or any workflow tool and the workflows are simple enough that a natural-language description would cover them, try rebuilding one of them inside ChatGPT workspace agents. Not to migrate, to calibrate. You need a direct read on how close OpenAI is to eating your current automation bill, and the only way to get that is to use the product on a real workflow.

Third, download Qwen3.6-27B and run it on a coding task that matters. Even if you stay on Claude or GPT for production, you want a first-hand sense of how close open weights are to frontier. That sense is the input to every lock-in decision you make this year about embeddings, inference, and agent infrastructure.

The thread across all three of these stories is the same one Parakhin drew out in the Shopify interview. The companies treating AI as an infrastructure layer, budgeted like AWS and sized like electricity, are on a different trajectory from the ones treating it as a line-item software expense. Shopify picked the first path in late 2025 and the graphs went vertical in December. The public market is pricing the same shift into Cursor's valuation. Every week that goes by, the gap between the two groups widens.

One last thing to sit with from Parakhin's interview. He was asked what changed internally when Shopify shifted to unlimited tokens, and his answer was not about cost or productivity metrics. It was that engineers stopped treating AI like a vending machine and started treating it like a colleague. They began looping the model in on design discussions, using it to pressure-test architecture choices, having it draft pull request reviews. That is not a usage pattern a rationing regime can produce, because rationing forces a task-by-task ROI calculation and collaboration does not fit that shape. The real unlock at Shopify was not the token budget. It was the posture shift that unlimited access made possible. If you want to see what your team is actually capable of with current models, you probably have to pay for their vending-machine phase to end.
