# LinkedIn posts, 2026-06-06

**Lead:** AI compute costs force architecture choices that will define the next 12 months
**Briefing type:** pattern
**Best option:** 2 (pre-council self-score)

---

## OPTION 1, contrarian-philosopher (hook score: 8)

**Conviction:** L2: The cost discussion is happening at the wrong level, founders are optimizing tokens when they should be architecting routing decisions as core product strategy

**Post:**

Google just paid SpaceX $11 billion annually for compute they can't get anywhere else.

The era of 'just call the API and optimize later' officially ended.

Every founder I talk to this week is asking the wrong question. They're asking "how do we reduce our token costs?" when they should be asking "how do we architect routing as a core product decision?"

The teams that built cost routing six months ago now have sustainable unit economics. The ones optimizing for capability without considering cost are retrofitting their entire architecture or running out of money.

At Atlan, we build agents that route explicitly:
- Simple queries go local
- Complex reasoning goes to frontier models
- Document processing stays on device
- Creative writing gets sent to Claude

The decision happens at the request level. This routing occurs in real-time, not during monthly budget meetings.

This isn't cost-cutting. This is systems thinking. Teams building hybrid routing from day one ship products with predictable costs and zero API dependency risk.

The Google-SpaceX deal proves even hyperscalers face the same constraint. When the company that runs one of the world's three largest clouds goes to a rocket company for compute, the supply problem is real.

But here's what most founders miss: this constraint creates opportunity. Small teams with explicit routing can build better unit economics than 50-person orgs that default to cloud APIs for everything.

The coordination overhead disappears when the architecture makes cost decisions automatic.

The founders who treat routing as infrastructure win. The ones who treat it as an optimization problem get surprised by their next bill.

What routing decisions is your architecture making for you right now?

---

## OPTION 2, personal-I-observer (hook score: 9)

**Conviction:** L3: Teams need an immediate cost audit and explicit routing logic while Chinese open weights are still available

**Post:**

I broke GPT, asked how many r's are in strawberry. It said 2. S-T-R-A-W-B-E-R-R-Y. There are 3.

LLMs are like autocomplete on steroids, they predict patterns, not count characters. That's why most teams burn through tokens on tasks that local models handle fine.

I see it across my network. Teams shipping with identical tools, but getting wildly different burn rates.

The difference lies in what happens before you call the API.

Most teams I talk to track tokens consumed but don't connect consumption to monthly budget burn rate. They optimize for capability without considering the unit economics death spiral.

I build AI agents at Atlan. Here's what we learned about cost routing:

Start with an audit. Track every API call your team made in the last month. Categorize by task type. Most teams discover 70% of their AI budget goes to tasks that local models handle fine.

Simple pattern: if the task needs creativity or complex reasoning, send to frontier models. If it's classification, summarization, or structured data processing, route local first.

The 78% local routing that Tunguz demonstrated only works if capable models exist to download. Right now, that means DeepSeek, Qwen, and other Chinese labs releasing frontier-quality weights for free.

But Mollick's economic argument is sound. Training runs that cost $100 million don't sustain themselves on goodwill. If Chinese labs stop releasing models, the local AI ecosystem breaks.

Download capable local models this week while Chinese open weights are still available. Test Qwen 2.5, DeepSeek V2, or Llama 3.1 on your actual use cases.

Build local inference capability as insurance against future access restrictions.

The teams that nail cost routing in the next 60 days will ship products with sustainable unit economics.

What's the ugliest cost routing workaround in your current setup? 👀

---

## OPTION 3, absurdist-truth-teller (hook score: 8)

**Conviction:** L1: The Google-SpaceX deal reveals AI infrastructure has become so constrained that tech giants are literally going to space for compute

**Post:**

Google just paid a rocket company $920 million per month to rent computers in space.

Read that sentence again.

The company that runs one of the world's three largest clouds can't scale fast enough to meet AI demand. So they went to SpaceX.

Not AWS. Not Azure. Not another cloud provider.

A rocket company.

This is what happens when demand doubles every quarter and data centers take 24 months to build. The math broke. SpaceX can launch compute capacity in weeks, not years.

Every week I watch founders optimize for AI output quality while their CFOs ask why cloud bills tripled. The conversation shifted overnight from "tokenmaxxing and go fast" to "we need guardrails, how do we control this?"

The experimental budget became a real line item.

What Google's $11 billion annual bet tells us: even hyperscalers face supply constraints that break normal procurement. When traditional infrastructure can't keep up, you literally go to space.

But here's the absurd part. Satellite compute means latency, power constraints, and thermal management issues that ground-based clouds don't face. Google chose these tradeoffs over waiting for terrestrial capacity.

That tells you everything about how desperate the supply situation has become.

The causal chain runs straight through every AI builder's architecture. More hyperscaler-to-satellite deals are coming. Compute location becomes a strategic decision, not an operational detail.

Teams that understand this split win contracts. Latency-sensitive workloads stay on ground. Batch training jobs go to space.

The founders building AI startups today face the same supply constraints as Google. The difference is Google has $11 billion to solve the problem. Bootstrapped teams don't.

That makes routing decisions survival choices, not optimization opportunities.

My mom asked AI to cancel her dentist appointment. It wrote a LinkedIn message. 147 words. 3 paragraphs.

She deleted all of it. Typed "can't make Saturday." Sent.

Sometimes the rocket ship solution isn't the right solution.

What are you overengineering that could be solved with "can't make Saturday"?
