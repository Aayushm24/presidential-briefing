# AI infrastructure capex is plateauing while software layers capture the next wave

[Tomasz Tunguz](https://x.com/ttunguz/status/2099547611338551460) posted concrete market data showing mega-cap AI infrastructure stocks declined while SaaS surged 4.5% median with 92% of the index green.

The market rotation away from AI infrastructure to software is happening with measurable dollars and percentages. When NVDA drops 2.8% and ORCL falls 4.3% on the same day that SentinelOne jumps 15.8% and Zscaler climbs 15.5%, that's capital moving from chips to apps. The pacing debate triggered this rotation because investors finally see what builders have known for months: the returns are moving to software companies that capture usage, not just enable it.

**Key takeaways:**
- AI infrastructure stocks (NVDA -2.8%, ORCL -4.3%) declined while SaaS companies surged 4.5% median with 92% showing gains, marking a concrete capital rotation from hardware to software
- Security platforms captured the biggest gains (SentinelOne +15.8%, CrowdStrike +15.4%) because they monetize AI workloads rather than just enabling them
- The AI pacing debate signals formal checks and delayed releases, not slower training, creating structural pauses in raw compute spending that benefit application-layer companies
- Productivity platforms are consolidating through acquisitions like Superhuman buying Fathom, while labs acquire hardware capabilities like OpenAI's $300M Glass Imaging purchase
- Builders should prioritize software-layer products over infrastructure bets as the market rewards usage capture over enablement

### The numbers reveal where the money moved

The rotation wasn't subtle. [Tunguz's data](https://x.com/ttunguz/status/2099547611338551460) shows Oracle down 4.3% and NVIDIA down 2.8% while the median SaaS stock gained 4.5%. That's a 7-9 percentage point spread in a single trading session. Twelve companies gained 10% or more. Eighty of 87 stocks closed green.

What I keep coming back to is the precision of the moves. This wasn't broad market volatility hitting everything randomly. Infrastructure got hammered while software soared. The market parsed Dario Amodei's pacing comments and immediately started pricing in slower hardware capex growth.

Think about what happened at the mechanism level. Every AI workload needs three layers: compute infrastructure, security and governance platforms, and application software. When capex growth slows, the recurring revenue from layers two and three becomes more valuable relative to the one-time infrastructure sales in layer one.

The security layer won biggest. [SentinelOne jumped 15.8%](https://x.com/ttunguz/status/2099547627197206826), Zscaler climbed 15.5%, CrowdStrike gained 15.4%. Rubrik added 13.9%. Palo Alto Networks rose 13.8%. These are software platforms, not infrastructure providers. They charge for protecting the workloads that AI infrastructure enables.

Here's the causal chain that most people miss: as AI workloads move from experimental to production, security and governance become mandatory, not optional. A research team can run models on bare metal. A bank deploying AI for loan decisions needs CrowdStrike monitoring every inference, Zscaler controlling every API call, and Rubrik backing up every model version.

The security premium makes sense when you trace the deployment path. Experimental AI workloads need chips and cloud instances. Production AI workloads need chips, cloud instances, AND security platforms, AND compliance monitoring, AND data governance, AND backup systems. The software layer revenue scales with deployment maturity. The hardware layer revenue scales with raw compute demand.

Here's why that matters: when hardware capex pauses for breath, the software layer doesn't just catch up, it accelerates. Security companies make money every time a new AI model gets deployed into production. Infrastructure companies make money once when the hardware gets bought. The recurring revenue models win when growth rates normalize.

The market figured out what many builders missed: monetizing AI usage beats enabling AI usage. SentinelOne charges monthly for every endpoint it protects. NVIDIA charges once for every chip it sells. When AI deployment growth shifts from exponential to linear, the subscription models compound while the hardware sales flatten.

This creates a mental model shift for builders. The question isn't "how do I build the best AI infrastructure?" The question is "how do I capture recurring revenue from AI workloads after they're deployed?" The companies that answer the second question correctly are the ones gaining 15%+ in single trading sessions.

### Pacing means checks and gates, not slower progress

The pacing debate that triggered this rotation isn't about slowing AI progress. [Sebastian Raschka breaks it down](https://x.com/rasbt/status/2099489528994025951): pacing means formal checks and delayed releases, not slowing training. We've seen this already with Mythos getting delayed and released as a nerfed Fable variant instead.

What changed is the regulatory environment around frontier models. Pacing creates mandatory review periods between training completion and public release. That doesn't slow research but it does slow the cadence of new capabilities hitting production systems. Slower capability releases mean longer windows for application-layer companies to build sustainable businesses on current foundation model performance.

The mechanism here is crucial to understand. Pacing doesn't mean OpenAI stops training GPT-7 or Anthropic pauses Claude-5 development. It means they add formal safety evaluations, external red-teaming, and government review periods between "training complete" and "public release." The models still get built at the same pace. They just sit in review longer before deployment.

This delay structure fundamentally changes the competitive dynamics for AI application companies. Previously, foundation model capabilities jumped every 6-12 months with minimal warning. Application companies had to assume their current advantages would become generic with the next model release. Under pacing, they get longer runway to build defensibility around current capabilities.

The five camps Raschka identifies all agree on one thing: training continues full speed. The difference is in deployment timing. When OpenAI trains GPT-7 but waits six months for safety reviews before release, that's six extra months for companies like Superhuman, Notion, and Cursor to compound their lead using GPT-6 capabilities.

Here's the second-order effect that most people miss: pacing doesn't just create longer development cycles for application companies. It creates predictability. Instead of wondering "will GPT-7 ship next month or next year?", companies can plan around known review timeframes. That planning window lets them make deeper architectural bets and invest in custom infrastructure that pays off over longer time horizons.

This creates a structural advantage for software companies. They can build deeper integration, better user experiences, and stronger network effects during the pause periods. Infrastructure companies face the opposite dynamic: their advantage gets commoditized faster because chips become standard faster than applications get replaced by competitive alternatives.

The investment implications are striking. Under the old model, betting on application-layer companies was risky because foundation model advances could make your investment obsolete overnight. Under pacing, application companies get protected development windows to build sustainable competitive advantages. That's why the market moved so decisively toward software companies this week.

I think the market sees something most builders don't: pacing turns AI from a hardware arms race into a software endurance race. The teams that build the stickiest products during the capability pauses will own the usage when capabilities jump forward again.

### Capital follows usage capture, not enablement

The core insight driving this rotation is simple: charging for usage beats charging for enablement. NVIDIA sells picks and shovels. SentinelOne charges rent on the gold that gets dug up.

Look at the specific percentage moves. Security platforms that charge based on AI workload volume gained 15%+. Infrastructure platforms that enable AI workloads fell 3-4%. The spread reflects a fundamental shift in where investors think the margins will accumulate.

This matches what I'm seeing in founder conversations. Teams building on Claude Code or GPT-6 can ship features faster than teams building custom infrastructure. The application-layer companies compound their advantages through better user experiences, not better hardware. They win through stickiness, not specifications.

The timing matters too. We're hitting the point where foundation model capabilities are good enough for most use cases but not so good that applications become trivial to build. That's the sweet spot for sustainable software businesses. Not too early that the models can't do the job. Not too late that OpenAI ships your entire roadmap.

What surprises me is how fast the market moved. This rotation happened in one trading session after Amodei's pacing comments. That suggests investors were already positioned for this shift. They just needed a catalyst to move capital from infrastructure to applications.

---

### Superhuman acquires Fathom as productivity platforms consolidate

[Superhuman acquired YC-backed notetaker Fathom](https://techcrunch.com/2026/09/14/superhuman-acquires-yc-backed-notetaker-fathom-as-productivity-platforms-push-for-agentic-work/) as productivity platforms consolidate tools into full workflow control systems.

Fathom built a generous free plan that attracted 400,000 monthly active users with over 1 million total meeting recordings. Those aren't vanity metrics. That's distribution that Superhuman can immediately plug into their premium workflow engine. More importantly, it's context data that becomes exponentially more valuable when combined with email workflow data.

The acquisition signals where productivity AI is heading: from standalone tools to integrated platforms that own the full context loop. Fathom captures meeting context. Superhuman manages email workflow. Together they can build agents that understand both communication streams and make decisions across channels.

Here's why this timing matters: productivity AI is hitting the same consolidation pattern we saw in business software 20 years ago. Point solutions get acquired by platform companies that can cross-sell and bundle features. But AI changes the math because context compounds exponentially. A meeting transcription tool plus an email client isn't just two tools, it's a complete communication graph that can predict what you need before you ask.

Think about the data advantage Superhuman gets from this acquisition. They now have 1M+ meeting recordings paired with email threads from the same users. That's training data for agents that understand how decisions flow from meetings to email follow-ups to calendar scheduling. OpenAI's foundation models are generic. Superhuman's combined dataset is specific to executive workflow patterns.

What I notice is the timing. This acquisition happens right as the market rotates toward software companies. Superhuman is betting they can consolidate productivity tools faster than OpenAI can ship productivity features. That's a race between platform assembly and foundation model expansion.

The key insight: standalone notetakers, schedulers, and email assistants are becoming acquisition targets or features inside larger platforms. The builders who survive will either be the consolidators or design specifically for acquisition by building deep workflow integration rather than surface-level AI wrappers.

[YC is building internal agentic systems](https://x.com/garrytan/status/2099354274585338277) using open-source tools like QM and GBrain. That's another signal of consolidation. Even the world's most successful startup accelerator is building integrated systems that share context across functions rather than buying separate AI tools from different vendors.

Fathom's 400K MAU base gives Superhuman immediate scale to test agentic workflows. That's a better path than building meeting capture from scratch. The question now is whether they can integrate deep enough to create switching costs before the next wave of foundation model capabilities makes all current productivity tools look primitive.

The strategic lesson for builders: if you're building a productivity tool, you're either going to be acquired by a platform or you need to become the platform that does the acquiring. The middle ground of successful standalone productivity tools is disappearing as context becomes the key competitive advantage.

---

### OpenAI expands hardware acquisition strategy with Glass Imaging purchase

[OpenAI bought smartphone camera maker Glass Imaging for $300 million](https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/), signaling that frontier AI labs are moving beyond software to acquire physical sensing capabilities.

Glass Imaging was founded by former Apple engineers who developed Portrait Mode. That's not random talent acquisition. OpenAI is buying specific expertise in computational photography and camera hardware integration. The $300M price tag suggests this is strategic, not experimental. When you're willing to pay $300M for a camera startup, you're betting on a future where custom hardware determines AI model quality.

This acquisition fits a pattern: AI labs are vertically integrating into hardware because multimodal AI requires proprietary sensing pipelines. You can't build the best vision models using only public datasets scraped from the web. You need controlled data collection from hardware you design.

Here's the mechanism that drives this vertical integration: foundation models are hitting diminishing returns on publicly available training data. The next frontier is proprietary data collection at massive scale. But you can't collect proprietary visual data without controlling the hardware that captures it. Glass Imaging's camera technology gives OpenAI the ability to collect training data that Google, Anthropic, and Meta can't access.

Think about what this means for competitive positioning. Every iPhone user generates visual data that goes to Apple. Every Android user generates visual data that goes to Google. OpenAI was the odd one out with no direct hardware data collection. The Glass Imaging acquisition is their play to build independent data pipelines that don't depend on platform partnerships.

The timing connects to Apple's iOS 27 Siri overhaul that [actually makes users want to use voice assistants again](https://techcrunch.com/2026/09/14/with-ios-27-im-actually-using-siri-again/). Apple ships new on-device AI that actually works. OpenAI responds by acquiring camera expertise to build better multimodal data collection. These moves position both companies for the next phase where AI model quality depends on proprietary sensor data, not just better training techniques.

This creates a strategic inflection point for the entire AI ecosystem. When foundation model labs own the hardware that generates training data, they can build advantages that pure software companies can't replicate. It's the reverse of the software rotation we saw in public markets. At the infrastructure layer, hardware integration is becoming essential for competitive advantages that pure software companies can't replicate.

For builders, this creates a warning signal: if your vision or embodied AI product depends purely on model quality, you're now competing with labs that own custom hardware pipelines. What makes you different has to come from proprietary data, domain specificity, or distribution advantages rather than model performance alone.

The second-order effect is already visible in other acquisitions. Every major lab is now evaluating hardware companies for strategic acquisition. The question isn't whether more hardware acquisitions will happen, but which sensing capabilities each lab will prioritize. Vision was OpenAI's first move. Audio, tactile sensing, and environmental monitoring will likely follow.

What strikes me is how quickly labs moved from pure software to hardware acquisition. Two years ago, OpenAI was purely a model company. Now they're buying camera makers and robotics companies. That's a massive strategic shift that every AI builder needs to factor into their defensibility planning.

---

### What to do this week

**Start tracking your software layer positioning.** If you're building on AI infrastructure, audit whether you charge for usage or enablement. Usage-based revenue models got a 15%+ market premium this week. Enablement models got hammered. Document where your revenue comes from and whether it compounds with AI deployment or gets commoditized by it.

**Evaluate consolidation opportunities.** The Superhuman-Fathom deal shows how productivity platforms are buying distribution and data rather than building from scratch. If you're a standalone AI tool, either design for acquisition or start acquiring complementary tools yourself. The middle ground is disappearing.

**Plan for pacing impact on your roadmap.** Formal review periods between foundation model releases create longer windows to build sustainable advantages on current capabilities. Map out which features depend on next model performance versus which can be built with existing capabilities plus better engineering.

Time investment: 2-3 hours to audit your positioning and roadmap. The market rotation from infrastructure to software is measurable and ongoing. Position accordingly.
