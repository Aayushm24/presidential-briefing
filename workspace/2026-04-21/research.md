# Research — 2026-04-21

**Total scored:** 31 items. **Top 10 selected.**

## Lead (combined score: 8.8)

**Title:** How Intercom 2x'd their engineering velocity in 9 months with Claude Code | Brian Scanlan
**Source:** Lenny's Newsletter — https://www.lennysnewsletter.com/p/how-intercom-2xd-their-engineering
**Scores:** sig=8 biz=9 prac=9 heat=8 story=10
**Why:** Concrete case study with a named company, specific metric (2x velocity in 9 months), and replicable methodology using Claude Code skills and telemetry — exactly what CTOs need to justify AI tooling investment.

Summary: Brian Scanlan (Intercom) shows how they doubled engineering output using Claude Code skills, deep telemetry, and a culture that empowers engineers to ship faster

## #2 (combined score: 8.2)

**Title:** Anthropic takes $5B from Amazon and pledges $100B in cloud spending in return
**Source:** TechCrunch — https://techcrunch.com/2026/04/20/anthropic-takes-5b-from-amazon-and-pledges-100b-in-cloud-spending-in-return/
**Scores:** sig=9 biz=9 prac=6 heat=9 story=8
**Why:** A $5B investment tied to $100B in AWS spend is a landmark circular deal that locks in Anthropic's cloud infrastructure for years and signals AWS as the dominant enterprise AI platform — every founder building on Anthropic needs to understand this dependency.

Summary: Amazon has made another circular AI deal: It's investing another $5 billion in Anthropic. Anthropic has agreed to spend $100 billion on AWS in return.

## #3 (combined score: 7.8)

**Title:** Codex acquisition of Skybysoftware is a top OpenAI deal — real computer use with AI is now rolling out
**Source:** X/swyx — https://x.com/swyx/status/2046362691606855700
**Scores:** sig=8 biz=8 prac=7 heat=8 story=8
**Why:** OpenAI acquiring real computer-use capability through Codex x Skybysoftware signals the next wave of agentic automation is shipping now, not in a roadmap — builders should be watching this closely.

Summary: the Codex x @skybysoftware acquisition may have been one of the best @openai deals made in the last year. I've been waiting for "real" computer use since @romainhuet demoed the ChatGPT App with 4o Vision at AIEWF 2024... and only now it's really, actually rolling out in a usable fashion.

## #4 (combined score: 7.6)

**Title:** Smarter AI models use fewer tokens reducing costs, but Opus 4.7's new tokenizer raises costs — sawtooth pattern in model pricing
**Source:** X/ttunguz — https://x.com/ttunguz/status/2046277504797974700
**Scores:** sig=7 biz=9 prac=8 heat=7 story=7
**Why:** Founders budgeting AI costs need to know that model upgrades don't always reduce spend — the sawtooth cost pattern is a real financial planning insight with immediate P&L implications.

Summary: "As models get smarter, they can solve problems in fewer steps : less backtracking, less redundant exploration, less verbose reasoning. Claude Opus 4.5 uses dramatically fewer tokens than its predecessors to reach similar or better outcomes." When Anthropic launched Opus 4.5 in November 2025, the bigger, more expensive model was actually cheaper to use. On a per-token basis, Opus 4.5 costs 67% more than Sonnet. But Opus 4.5 used 76% fewer tokens to reach the same outcome. A task that cost $1 on Sonnet cost $0.40 on Opus. The trend across vendors has been smarter models using fewer tokens per task. Then Opus 4.7 shipped & the smarter model became much more expensive. The cause : a new tokenizer - software to break text into pieces a computer understands. Smaller pieces force the model to pay closer attention to each word, like reading a contract word by word instead of skimming paragraphs. The model follows instructions more precisely & makes fewer mistakes on coding tasks. The tradeoff : more tokens, higher costs. "For text, I'm seeing 1.46x more tokens for the same content. We can expect it to be around 40% more expensive in practice." - Simon Willison Boris Cherny, creator of Claude Code, acknowledged Anthropic raised rate limits "to make up for it." Will smarter models be increasingly expensive because of greater accuracy or less expensive because they're smarter? Resolution increases make them more expensive, then efficiency gains reduce costs - a sawtooth pattern. But in every case, this means generating more tokens.

## #5 (combined score: 7.6)

**Title:** Training Transformers to solve 95% failure rate of Cancer Trials — Ron Alfa & Daniel Bear, Noetik
**Source:** Latent Space — https://www.latent.space/p/noetik
**Scores:** sig=8 biz=8 prac=6 heat=7 story=9
**Why:** Noetik is applying autoregressive transformers to the clinical trial matching problem — a massive market with a quantified failure rate, making this a compelling AI-for-healthcare business story with real stakes.

Summary: 95% of cancer treatments fail to pass clinical trials, but it may be a matching problem — that Noetik is solving with autoregressive transformers like TARIO-2!

## #6 (combined score: 7.4)

**Title:** AI agents produce results near human median with less variance in economics study — Claude Code & Codex tested
**Source:** X/emollick — https://x.com/emollick/status/2046362044786458648
**Scores:** sig=7 biz=8 prac=7 heat=7 story=8
**Why:** Replication of a classic multi-team economics study with AI agents shows consistent near-median performance with lower variance — a credible, specific outcome that helps founders calibrate what AI agents can reliably deliver.

Summary: Classic study gave 146 economist teams the same dataset & got wildly different answers. New paper reruns it with agentic AI. Claude Code & Codex land near the human median, but with far tighter dispersion & no extremes. Suggests that AI is now useful for doing scalable research.

## #7 (combined score: 7.2)

**Title:** Open weight models can fast-follow closed labs until training paradigm changes — no evidence open models are falling behind
**Source:** X/natolambert — https://x.com/natolambert/status/2046299148883046450
**Scores:** sig=7 biz=8 prac=7 heat=7 story=7
**Why:** A credible researcher's framework for when open vs closed models diverge is directly actionable for founders deciding whether to build on proprietary APIs or open weights — affects build vs buy decisions today.

Summary: I've been trying to grapple with what the key inputs are to the open-closed performance gap, and how they're changing. Until the training paradigm changes, open weight models will pretty clearly be able to fast-follow closed labs. There are sources of uncertainty, but that fact of keeping up seems hard to shake. I spent a long time looking for evidence of or arguments supporting open models falling behind, but it's not there at all today. Things I consider include: - How benchmarks evolve over time, becoming more or less correlated with how people actually use models, - How different models' real-world performance relates to their benchmark rankings, and - How training regimes evolve over time to move said benchmarks. I roughly conclude that this equilibrium will last until economic forces initiate a change in strategy, or training needs shift. An example I'm wondering is if closed models more directly integrate user training data, which open labs cannot access, they could pull ahead.

## #8 (combined score: 7.0)

**Title:** Kimi K2.6: world's leading open model refreshes to catch up to Opus 4.6
**Source:** Latent Space — https://www.latent.space/p/ainews-moonshot-kimi-k26-the-worlds
**Scores:** sig=7 biz=7 prac=8 heat=7 story=6
**Why:** A new open-weight model competitive with Opus 4.6 is immediately deployable for cost-sensitive builders who need frontier-class performance without API dependency — worth testing today.

Summary: Yay Kimi!!!

## #9 (combined score: 7.0)

**Title:** NSA spies are reportedly using Anthropic's Mythos, despite Pentagon feud
**Source:** TechCrunch — https://techcrunch.com/2026/04/20/nsa-spies-are-reportedly-using-anthropics-mythos-despite-pentagon-feud/
**Scores:** sig=7 biz=7 prac=5 heat=8 story=8
**Why:** Government intelligence agencies adopting Anthropic's restricted model signals a serious enterprise/gov-tech market opening and validates Anthropic's security positioning — relevant for founders targeting regulated sectors.

Summary: NSA is said to be using Anthropic's restricted Mythos AI model.

## #10 (combined score: 6.8)

**Title:** TSMC Earnings, New N3 Fabs, The Nvidia Ramp — TSMC leadership not fully bought into AI growth story
**Source:** Stratechery — https://stratechery.com/2026/tsmc-earnings-new-n3-fabs-the-nvidia-ramp/
**Scores:** sig=7 biz=8 prac=5 heat=7 story=7
**Why:** If TSMC's own leadership is skeptical of AI demand sustainability, that's a contrarian signal worth tracking for anyone advising founders on infrastructure bets and AI capex cycles.

Summary: TSMC's earnings suggest that the company's leadership is not truly bought into the AI growth story.