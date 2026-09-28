# Closed models pulled ahead in agentic AI while open models lag behind

[Ethan Mollick](https://x.com/emollick/status/2104326478766952624) documented something builders have been feeling for months: Fable/Astra class models are agentic in a way pre-Fable models are not.

The open-closed parity window has closed temporarily. Builders choosing model infrastructure for agentic workloads today face a meaningful capability gap that affects architecture decisions immediately. When you choose a closed model for agent work, you're not just picking an API endpoint. You're committing to authentication systems, sandbox security, and browser automation tools that will be hard to reverse when open models catch up.

**Key takeaways:**
- Closed frontier models crossed an agentic capability line that no open model has reached yet, [Ethan Mollick](https://x.com/emollick/status/2104326478766952624) observes a larger gap between open and closed models than in months
- Real-world task completion shows [Opus 5.5 with Openclaw outperforming GPT-6 Astra](https://x.com/garrytan/status/2104224426091016247) in Garry Tan's daily use
- [AsideAI browser with MCP](https://x.com/garrytan/status/2104221282095218731) solves the anti-bot problem that breaks agentic workflows using real credentials in real Chromium
- AI agents threaten friction-based business models like [bank deposits paying 0.1% instead of 3-5%](https://x.com/emollick/status/2104273082433081732) when agents can sweep accounts automatically
- This capability gap affects build-vs-buy decisions happening now that will be hard to reverse later

### The capability line that open models haven't crossed

[Ethan Mollick's observation](https://x.com/emollick/status/2104326478766952624) cuts through months of benchmark confusion. "Qualitatively, there is now a larger gap between open and closed models than there has been in awhile. Fable/Astra class models are agentic in a way pre-Fable models are not, for better or worse. None of the open models have crossed that line, yet."

This matches what [Garry Tan reports](https://x.com/garrytan/status/2104224426091016247) from daily usage: "Opus 5.5 with Openclaw is strangely smarter and better at completing tasks than GPT-6 Astra." The surprise isn't that one model beats another on specific tasks. The surprise is how consistently the closed models maintain context and execute multi-step workflows without breaking down.

I've been tracking this through my own agent work over the past three months. Open models can follow complex instructions. They can write good code. They can reason through problems step by step. But when you chain those capabilities together into autonomous workflows, something breaks down around step 4 or 5. The model loses track of its original goal, starts optimizing for the wrong thing, or makes assumptions that derail the entire process.

Closed frontier models don't just perform better on individual tasks. They hold their objectives longer. They recover from errors without human intervention. They distinguish between "the thing I was asked to do" and "the thing that would be impressive to do" more consistently. That distinction turns out to matter enormously when you're not watching every step.

The gap shows up most clearly in what researchers call "long-horizon planning." Open models excel at single-turn tasks where you can evaluate the output immediately. Closed models excel at multi-turn tasks where the agent needs to maintain state across interactions, learn from mistakes, and adjust its approach based on feedback it receives along the way.

What catches my attention is the timing. This capability gap emerged just as the tooling around agentic AI matured enough for production use. [AsideAI browser with MCP](https://x.com/garrytan/status/2104221282095218731) solves the anti-bot detection that was breaking agent workflows for months. Cursor and Claude Code make it possible to delegate actual software development tasks to AI. The infrastructure exists to build reliable agent systems. But only if you use the closed models.

This creates a strategic inflection point for builders. Teams that started building agents six months ago, when open and closed models were closer in capability, could reasonably bet on open model parity returning quickly. Teams starting today face a different calculation. The agentic capabilities aren't just incrementally better in closed models. They represent a qualitative difference in how autonomous these systems can be.

### Infrastructure decisions that lock you in

When [Garry Tan recommends](https://x.com/garrytan/status/2104221282095218731) running AsideAI browser "on a spare laptop or computer you keep plugged in somewhere" so agents can use "your real credentials as yourself from a real Chromium," he's describing the infrastructure reality of production agent systems.

Agentic AI isn't just an API call. It requires authentication management, sandbox environments, browser automation, credential storage, and audit logging. These components integrate differently depending on which models you target. Closed model APIs come with built-in session management, rate limiting that accounts for multi-step workflows, and error handling designed for autonomous operation. Open model deployments require you to build all of that yourself.

The authentication problem illustrates this clearly. Many agent tasks require logging into services as the user. With closed models, you can use OAuth flows, API key rotation, and credential storage that the model provider validates and maintains. With open models, you're managing credentials directly, implementing your own OAuth flows, and handling token refresh without proven patterns to follow.

Browser automation compounds the infrastructure complexity. Anti-bot detection has become sophisticated enough to break most headless browser solutions. The services agents need to interact with actively fight automated access. AsideAI's approach of using a real browser with real user credentials works because it looks exactly like human usage patterns. But integrating that approach with open models means building custom orchestration layers that don't exist yet.

I'm not arguing that closed models are inherently superior for agent work. I'm pointing out that the infrastructure ecosystem developed around closed model APIs first. The tooling, the documentation, the community knowledge, and the third-party integrations all assume you're using Claude, GPT, or Gemini APIs. When open models reach agentic parity, builders will still need to reconstruct all of that infrastructure for self-hosted deployments.

Teams making infrastructure decisions today are weighing known solutions that work now against unknown solutions that might work later. That's not a technical judgment. It's a business risk assessment. For most builders, the rational choice is to build on the infrastructure that works and switch later if necessary.

The switching cost won't be trivial. Agent systems develop implicit dependencies on specific model behaviors. The error recovery patterns you build around Claude's failure modes won't work for Llama's failure modes. The prompt engineering techniques that make GPT agents reliable might not transfer to other architectures. The authentication integrations that work with OpenAI's API might not work with your own deployment.

### What gets disrupted when agents work reliably

[Apollo's chief economist](https://x.com/emollick/status/2104273082433081732) described how agents could cause bank runs by sweeping household cash from accounts paying 0.1% to accounts paying 3-5%. That's not a prediction about AI capability. That's a description of what happens when friction disappears from systems that depend on friction to function.

Most people keep money in low-interest checking accounts because moving money requires time, attention, and expertise they don't want to spend. An agent that monitors interest rates, compares account options, and executes transfers automatically removes all three barriers. The result isn't just individual optimization. It's systemic shift of how banks fund themselves.

Banking is the obvious example because the numbers are stark. The average checking account pays 0.1% while money market accounts at the same banks pay 3-5%. The gap exists because customers don't optimize actively. When agents optimize continuously, the gap disappears. Banks lose their cheapest source of funding overnight.

But friction-dependent business models extend far beyond banking. Software-as-a-Service pricing relies on customers not downgrading when they don't need premium features. Insurance companies profit from customers not switching when better rates become available. Enterprise sales cycles depend on procurement teams not having perfect information about alternatives and competitive pricing.

I keep coming back to the timing aspect. We're seeing these shift scenarios emerge just as closed models became reliably agentic. Open models reaching the same capability level will accelerate the shift because more teams will be able to build agent systems that work consistently. The current capability gap isn't permanent. But it's creating a window where the economic shift potential of reliable agents becomes visible before the technology becomes democratized.

The pattern extends beyond consumer finance into enterprise workflows. HR systems depend on employees not optimizing their benefits selections every year. Procurement systems depend on buyers not researching alternatives for every purchase. Customer support systems depend on customers not escalating every issue to the optimal resolution path.

When agents work reliably across multi-step workflows, they remove friction from all of these systems simultaneously. The compound effect is what makes this interesting strategically. It's not just one industry facing shift. It's every industry that built business models around customers accepting suboptimal outcomes due to time, attention, or expertise constraints.

---

### #2 Simon Willison's year in review reveals how fast the baseline moved

[Simon Willison's WeAreDevelopers keynote](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) traced the psychological shift builders experienced as AI capabilities advanced throughout 2026. His chronological tour of the year shows how quickly "incremental improvements" compound into qualitative changes in what's possible.

November 2025 marked the inflection point. Claude Opus 4.5 and GPT-5.1 crossed what Willison calls the "reliable enough to use on a day-to-day basis" threshold for coding agents. The models existed before that. The harnesses existed. But the combination hadn't reached production reliability until those releases.

Willison's personal transformation illustrates the broader industry shift. His New Year's resolution changed from "stay focused, take on fewer projects" to "be more ambitious, let's see what coding agents can do." That's not just individual adaptation. That's recognition that the constraint on what one person can accomplish changed fundamentally.

The keynote documents month-by-month examples of builders realizing their assumptions about AI limitations were outdated. January brought "AI mania" where developers stayed up late getting agents to build projects that would have taken weeks of manual work. February and March saw the emergence of production agent workflows in enterprise settings. By summer, entire software categories were being replaced by agent-powered alternatives.

What makes Willison's retrospective valuable is the acknowledgment of both capabilities and costs. He built a JavaScript interpreter in Python and a WebAssembly runtime in Python using AI assistance. These projects worked. They also taught him that "just because you can build something with AI doesn't mean you should." The technology enables extraordinary ambition. It also requires extraordinary discipline to use effectively.

The year-over-year comparison reveals how much the baseline shifted. Tasks that required senior engineering expertise in 2025 became accessible to anyone who could prompt an agent effectively by mid-2026. The democratization of technical capability created new bottlenecks around problem definition, quality assessment, and strategic judgment.

Willison's "Deep Blue" concept captures the psychological challenge builders face. The term describes "that feeling of AI induced ennui where software engineers get listless because the AI can do anything." It's not depression. It's the professional identity crisis that comes when your core value proposition becomes automatable.

His prediction tracking shows how quickly the impossible became inevitable. The "Challenger disaster" he predicted for coding agent security hasn't materialized exactly as expected. But the broader security concerns he identified are now mainstream conference topics with dedicated tracks and working groups.

---

### #3 Anthropic plays the DC game while capabilities advance

[Anthropic CEO Dario Amodei's dinner with President Trump](https://techcrunch.com/2026/09/27/anthropics-ceo-is-about-to-have-dinner-with-president-trump/) represents the first one-on-one meeting between the two leaders. The timing isn't coincidental. As AI capabilities create real economic shift, the companies building those capabilities need regulatory relationships.

This dinner happens while Anthropic's models lead the agentic capability race. Claude's advantage in multi-step autonomous tasks makes it the preferred choice for enterprise AI deployments that handle sensitive data and critical workflows. Government contracts could determine which models become the standard for regulated industries.

The DC engagement strategy reflects lessons learned from social media regulation. Tech companies that ignored Washington during their growth phase faced hostile regulatory environments later. AI companies are investing in political relationships proactively, while they still have influence over how the technology gets regulated.

Anthropic's positioning differs from competitors in ways that matter for government relationships. Their constitutional AI approach provides explicit frameworks for controlling model behavior. Their research on AI safety gives them credibility with policymakers worried about autonomous systems. Their slower, more cautious deployment timeline aligns with regulatory preferences for predictability.

The regulatory implications extend beyond direct government contracts. Enterprise buyers increasingly require AI vendors to have clear compliance frameworks, audit capabilities, and regulatory relationships. Companies building on Anthropic's models can point to established government engagement when selling into regulated industries.

What interests me is how the capability advantage reinforces the regulatory advantage. Anthropic's models work better for agentic applications that government agencies want to deploy. Their DC relationships make them the safer choice for enterprise buyers who need regulatory cover. The feedback loop between technical capabilities and political positioning creates sustainable competitive advantages that pure technical excellence can't match.

The dinner also signals that AI regulation is moving from hypothetical to practical. When model capabilities were primarily chatbots and content generation, regulation focused on abstract safety concerns. When model capabilities include autonomous systems that can execute financial transactions and access sensitive data, regulation becomes immediate and specific.

---

### What to do this week

**Test agentic capability differences yourself** (30 minutes): Take a multi-step task like "research 3 competitors, write a positioning document, and create a simple landing page mockup." Run it through Claude Opus 5.5 vs the latest Llama model on HuggingFace. Document where each one breaks down or requires intervention. Pay attention to context maintenance across steps, error recovery patterns, and objective adherence. Use this data to inform your model selection for any agent work starting in the next quarter.

**Audit your friction-based revenue streams** (1 hour): List your company's revenue that depends on customer inertia, manual processes, or information asymmetry. Score each stream 1-10 on vulnerability to reliable agents. Include subscription services customers don't actively optimize, pricing strategies that rely on comparison difficulty, and workflows that depend on users accepting suboptimal outcomes. Start planning alternatives for anything scoring 7 or higher. The agents that will disrupt these models are being built right now.

**Try AsideAI browser for anti-bot problems** (45 minutes): If you're building agents that hit website anti-bot measures, test [AsideAI browser with MCP](https://x.com/garrytan/status/2104221282095218731) on a dedicated computer. Configure it with real user credentials and test against the sites your agents need to access. Document success rates and failure patterns. This approach could unblock agent workflows you've been stuck on for months, but it requires dedicated hardware and credential management that changes your deployment architecture.
