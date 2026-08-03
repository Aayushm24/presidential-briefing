# Karpathy's 1M token stress test reveals the new practical frontier for procedural AI content generation

[Andrej Karpathy](https://x.com/karpathy/status/2083749667410727319) spent $10 and 2 hours to have Opus 5 generate 5,500 lines of JavaScript that renders Lord of the Rings as a playable 3D browser demo.

The paradigm has shifted from "create an SVG of a pelican on a bicycle" toy demos to million-token procedural content generation that produces genuinely usable creative tools. We're past proof-of-concept and into practical deployment territory. But the bottleneck has moved from generation to auditing multimodal outputs.

**Key takeaways:**
- Karpathy's LLM stress tests define a new practical frontier. 1M token budgets ($10) enable custom creative workflows no human would attempt.
- Open model proliferation is accelerating rather than consolidating. More labs train billion-dollar models and release them openly instead of expected market contraction.
- The architecture for AI creative pipelines is crystallizing. Procedural code handles control. Video-to-video models handle texturing. API orchestration ties them together.
- LLMs can orchestrate third-party APIs like ElevenLabs in complex creative workflows. This proves agentic content pipelines work in production today.
- Classical methods like ngram tables may outperform LLMs in constrained environments under 25KB. This signals cost optimization opportunities for teams over-engineering with large models.

### From pelican SVGs to procedural worlds, the new frontier test

We're leaving the territory of toy LLM demos. The "create an SVG of a pelican on a bicycle" test that became the standard LLM benchmark tells you nothing about production capabilities. [Karpathy's stress test](https://x.com/karpathy/status/2083749667410727319) gave Opus 5 the first paragraph of Lord of the Rings, a 1M token budget worth $10, and asked for a JavaScript render. The model spent 2 hours writing 5,500 lines of code that procedurally renders the story as a [playable 3D browser demo](https://karpathy.ai/lotr-movie/).

This crosses a threshold that matters for builders. The demo works. You can fork it, modify it, drop players into Middle-earth as NPCs or characters. What Karpathy calls "an ephemeral GTA of X on demand." The code orchestrates polygon assets in 3D coordinates, animates characters across scenes, manages narrative timing, and creates an interactive experience that would have taken a game studio months to prototype.

The shift is economic and creative. I keep coming back to Karpathy's framing: "no one in their right mind would ever spend the time to write something this custom but LLMs have all the stamina and patience in the world." We've moved from "no one would ever do this" to "sure, why not, it's free."

The cost structure changes everything. Custom content that was economically impossible becomes economically trivial. The Lord of the Rings demo cost $10. A similar prototype from a creative agency would cost $10,000 minimum and take weeks. The quality gap exists, but the speed and cost gap is orders of magnitude.

What makes this practically significant is the complexity coordination. Opus 5 had to manage spatial relationships between dozens of characters, coordinate animations across multiple scenes, handle collision detection, implement camera movements, and synchronize audio cues. These are systems-level coordination problems that require understanding context across thousands of lines of code.

The mechanism here differs from traditional code generation. Instead of writing isolated functions, the model had to maintain state across an entire interactive system. It tracked character positions in 3D space, managed their behavioral patterns, coordinated visual timing with narrative beats, and ensured the player could navigate the world without breaking immersion. That's not just code generation. That's procedural world-building at compile time.

The implications compound for product teams. Custom game worlds become default, not premium features. Procedural content generation stops being a research problem and becomes a product category. Creative teams who understand this shift will ship experiences that feel handcrafted but scale like templates.

But Karpathy flags a critical gap that defines the current practical boundary. Opus 5 had to place and orchestrate polygon assets in 3D coordinates, animate them, coordinate timing across thousands of elements. The model did it, but blind. It couldn't see what it was building until it was done.

This blindness creates the bottleneck that determines what works today versus what needs human oversight. Generation capability leaped ahead. The models can write complex, multi-file, coordinated systems. But they can't audit their work across modalities. They can't watch a game being played, see how a 3D scene actually renders, or understand whether the player experience feels smooth.

The new architecture emerges from this constraint. Code for control and structure. Models for texture and polish. The LLM handles the procedural logic, the spatial relationships, the narrative beats, the interaction patterns. Other models handle the sensory layer, the visuals, audio, feel. Human oversight handles the evaluation layer, the testing, iteration, and quality control.

### The auditing weakness that matters

Opus 5 had to debug its Lord of the Rings render by taking screenshots "very slowly and painstakingly." It messed up several times, creating what Karpathy calls "a bunch of jank." The model could write thousands of lines of coordinated JavaScript but couldn't efficiently perceive whether the output worked.

This limitation defines the current practical boundary for autonomous creative AI. The model can generate procedural 3D worlds, but it can't see them. It can orchestrate complex animations, but it can't watch them play. It can coordinate spatial relationships across dozens of objects, but it can't tell if they collide correctly.

The debugging process Karpathy describes reveals the bottleneck. The model writes code, runs it, takes a screenshot, analyzes the static image, identifies problems, and modifies the code. This works, but it's orders of magnitude slower than human visual evaluation. A game developer can spot collision bugs, timing issues, or visual glitches within seconds of seeing gameplay. The model needs minutes per screenshot.

[Karpathy identifies this](https://x.com/karpathy/status/2083749667410727319) as "raw capability (multimodal, gameplay) that I think is still quite lacking." The models have multimodal input but not multimodal evaluation at the speed and granularity needed for iterative creative work. They can read images, but they can't efficiently perceive dynamic visual experiences like games, videos, or interactive demos.

This creates the value capture opportunity that most builders are missing. The teams who solve multimodal auditing will own the next wave of AI creative tools. Everyone is optimizing prompt engineering and context windows when the real opportunity is building evaluation loops that can iterate on video, audio, and interactive content at model speed.

Think about the competitive advantage. Your team can generate procedural content like Karpathy's demo. But can you evaluate it automatically? Can you catch quality issues before human review? Can you iterate on visual design, timing, and user experience without human oversight at each step?

The companies building evaluation layers will capture more value than the companies perfecting generation. Generation is becoming commodity, multiple models can write complex, coordinated code. Evaluation remains the human bottleneck in creative AI workflows.

This creates immediate tactical opportunities that most product teams haven't recognized. If your product generates video, build evaluation that can assess frame quality, motion consistency, and narrative coherence automatically. If you're generating interactive content, build testing that can simulate user interactions and catch edge cases before human testing.

The evaluation infrastructure becomes your competitive advantage because it's the constraint that determines iteration speed. Teams with good evaluation can ship higher-quality AI content faster than teams with better generation but manual quality control.

### Architecture emerging: procedural control plus model texturing

[Karpathy sketches the pattern](https://x.com/karpathy/status/2084017844455690558): "procedural code for storyboarding and control, and then video to video models for texturing and looksmaxxing."

This is the architecture that's crystallizing across creative AI products. The LLM writes the procedural logic, the structure, timing, spatial relationships. Video models handle texture and polish. Audio models like [ElevenLabs integrate](https://x.com/karpathy/status/2083756186663551388) for the sound layer.

Each layer optimizes for what it does best. Code for precise control. Video models for visual quality. Audio models for voice and music. The LLM orchestrates the pipeline but doesn't try to be everything.

I see this pattern in production products now. Teams that separate control from texture ship faster and get better results than teams trying to do everything with one model.

The convictions from the brief start connecting. Small teams with AI beat 50-person orgs because they can coordinate these pipelines without meetings. One person can orchestrate Opus for structure, Runway for video, ElevenLabs for audio, and ship something that would have taken a creative agency months.

Most AI products fail because they skip memory, not because of the model. The procedural layer IS the memory layer. The code that Opus wrote remembers the spatial relationships, the character positions, the narrative structure. That state persists and compounds across the experience.

Founders treating Claude Code as just a coding assistant are missing this shift. Understanding it as a procedural content engine unlocks products that feel magical to users who don't see the architecture underneath.

---

### Open model proliferation defies consolidation predictions

[Nathan Lambert observes](https://x.com/natolambert/status/2083917557560721890) that the predicted consolidation of open model labs isn't happening. More companies are training strong models and releasing them openly, not fewer.

"Consolidation has been one of the paths that many astute observers predicted," Lambert writes. "It was labelled as inevitable, as training costs are increasing by orders of magnitude every year." But we're seeing the opposite: more organizations investing hundreds of millions to billions in training, then releasing models openly.

This changes the build-versus-buy calculus for builders. The assumption was that training costs would force consolidation, leaving a few major API providers. Instead, [Interconnects documents](https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21) Laguna S2.1, Inkling, and Kimi K3 as deployable alternatives on the Pareto frontier.

Thinking Machines leads US open models. Chinese labs sustain pace despite export restrictions. The market is entering what Lambert calls "a decisive era for open model market share" where proliferation accelerates rather than contracts.

I see self-hosted alternatives becoming credible defaults, not backup options. The open model quality gap is closing faster than API pricing is dropping. Teams with cost sensitivity or privacy requirements have real choices now.

The conviction holds: founders should stop waiting for the open model market to settle. The Pareto frontier moves fast enough that self-hosted open models work for cost-sensitive or privacy-sensitive products today.

---

### Sam Altman calls for pacing AI development

[Sam Altman is publicly calling](https://techcrunch.com/2026/08/02/sam-altman-and-ais-decel-debate/) for the industry to "pace the rate of AI development." This is a regulatory and strategic signal founders need to track for product roadmap and policy risk.

Altman's position matters because OpenAI drives industry norms around safety practices, capability disclosure, and development timelines. When the CEO of the leading AI lab argues for deliberate pacing, it signals potential policy coordination or regulatory preparation.

The timing connects to recent safety incidents. OpenAI's agent reliability issues, Anthropic's Claude models breaching security evaluations, and the broader pattern of containment failures across labs. Public calls for pacing often precede private industry coordination on safety standards.

I watch regulatory risk rising on capability development timelines. Teams building products that depend on rapid capability scaling will need to consider scenarios where development pace becomes regulated or industry-coordinated.

The tactical response is building products that work with current capabilities rather than betting on exponential capability growth. Products that depend on today's models working better will outperform products that depend on next year's models existing on schedule.

---

### What to do this week

**Test the procedural content architecture.** Fork [Karpathy's Lord of the Rings demo](https://karpathy.ai/lotr-movie/) and modify it for your use case. Budget 2-3 hours and $20 maximum. The goal is to understand what procedural content generation feels like hands-on and where the evaluation bottlenecks appear in your domain.

**Audit your token costs with compression.** Use [Simon Willison's condense-json 1.0](https://simonwillison.net/2026/Aug/2/condense-json/#atom-everything) to compress JSON in your LLM pipelines. The library saves 20-40% tokens on structured data flows. If you're making thousands of API calls monthly, this compounds to real cost savings.

**Benchmark classical alternatives for constrained inference.** Karpathy suggests [ngram tables or decision trees](https://x.com/karpathy/status/2084056739197108667) may outperform LLMs in constrained environments under 25KB total program size. If you're running inference in resource-constrained environments or need sub-millisecond response times, test classical methods against your LLM calls for cost and latency optimization.
