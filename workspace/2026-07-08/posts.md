# LinkedIn posts, 2026-07-08 (iteration 2)

**Lead:** Open-source AI has a China problem, and builders need to map this risk now
**Briefing type:** pattern
**Best option:** 2 (pre-council self-score)

---

## OPTION 1, contrarian-philosopher (hook score: 8)

**Conviction:** L1: The $9.75B forward-deployed engineering spend proves AI still needs massive human expertise to work in real business contexts.

**Post:**
Five AI companies spent $9.75 billion on forward-deployed engineers this year.

Not on better models. Not on compute. On humans.

Every week I watch builders treat AI like plug-and-play software.

But the biggest number in AI this year tells a different story.

Forward-deployed engineering means sending engineers to live inside customer offices. Configure the AI system. Train their teams. Operate it daily.

This is permanent human infrastructure.

If AI models were truly ready for deployment, companies wouldn't need armies of implementation specialists.

The $9.75 billion spend went from "a Palantir signature" to 25% of Accenture's labor budget.

That's not a niche deployment model anymore.

At Atlan, we've learned shipping agents fast and fixing them publicly beats shipping perfectly.

But even our best agents need humans in the loop for the complex stuff.

The successful pattern: start with forward-deployed teams to prove value. Then gradually automate the human work into the product.

That transition takes years, not months. Meanwhile, you need enough margin to fund human deployment at scale.

I think this explains why AI companies raise such large rounds relative to traditional SaaS companies. They're not just funding R&D and customer acquisition. They're funding human deployment teams that cost $200,000+ per year per customer.

What does your AI actually need humans for right now?

---

## OPTION 2, personal-observer (hook score: 9)

**Conviction:** L2: The entire open-source AI system depends on Chinese researchers continuing to release frontier models. That assumption is about to fail.

**Post:**
Every startup's AI strategy has the same hidden dependency.

Chinese researchers sharing their work.

I see it across my network. Teams building on Llama alternatives for cost reasons. Sovereign AI projects banking on DeepSeek releases. Startups using open-weights models instead of paying OpenAI.

But what happens if Chinese labs stop releasing model weights?

Three forces could break the pattern. US export controls tightening further. Chinese government restrictions on foreign access. Chinese labs realizing they can monetize instead of giving away for research prestige.

Building a real AI product on open weights takes 12-18 months. Policy changes happen in weeks.

The symbiosis between frontier labs and open-source works because frontier labs push boundaries while open-source implementations chase them 6-12 months later.

But that chase depends on the chasers keeping up.

DeepSeek stops releasing weights tomorrow? Sovereign AI projects lose their technical foundation. Startups hit a capability ceiling. The entire "open-source will make AI cheap" thesis collapses.

I keep coming back to the timeline mismatch.

The foundation of AI strategy is changing faster than most builders realize. Build vs buy decisions depend on continued access to open-weights models that might disappear.

IMO, the window to architect around this risk is narrowing fast.

What's your backup plan if open-weights models disappear in six months?

---

## OPTION 3, absurdist-truth-teller (hook score: 8)

**Conviction:** L3: Microsoft's own AI models can't beat third-party models in Microsoft's own products. Even massive resources hit quality gaps when building in-house.

**Post:**
Microsoft built MAI-1 to power Office applications they control.

Their own model loses to Anthropic's in Excel tasks.

Think about that absurdity for a second.

Microsoft has 200,000 employees, $200+ billion cash, and more business customer feedback than almost any company.

They built MAI-1 specifically for Office. Yet Claude plugins outperform native Copilot integration.

This is the in-house model trap.

Every team I talk to is weighing build vs buy for AI. Microsoft just gave us the answer.

Building frontier AI capabilities requires continuous scaling, massive compute clusters, and specialized research talent.

Most companies lack one of these. Microsoft, with infinite resources, still produces models that underperform external alternatives.

This proves the build side carries enormous hidden costs. You're not just building a model. You're building the research capability to keep that model competitive indefinitely.

At Atlan, we use Claude for most of our agent workflows because it consistently outperforms alternatives we could build ourselves.

The lesson: vendor lock-in creates immediate product risk, but so does trying to match frontier capabilities in-house.

Sometimes the thing you can't build is exactly what you should buy.

How much of your AI stack are you building that you should probably be buying?
