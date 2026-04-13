April 13, 2026

Andrej Karpathy — the person who built Tesla's self-driving vision system and co-founded OpenAI — posted last week that he's stopped using AI to write code. Instead, he's using it to build something he calls a knowledge wiki. He dumps raw research papers and articles into a folder, points an LLM at it, and the model reads everything and writes an interconnected encyclopedia. His wiki on a single AI topic has grown to 100 articles and 400,000 words. All created and maintained by the LLM, not by Karpathy.

This sounds like a small personal workflow change. It's not. Let me explain why.

When most people talk about AI being useful, they mean it helps you do things faster. Write code faster. Write emails faster. Summarize documents faster. The entire AI coding assistant market — Cursor ($900M raised), GitHub Copilot, Windsurf — is built on this premise. AI as a typing accelerator.

Karpathy is saying something different. He's saying the bottleneck was never typing. It was thinking. Specifically, the hard part of understanding AI isn't reading one paper — it's connecting a paper you read today to something you read three months ago and realizing they're describing the same underlying phenomenon from different angles. That's synthesis. And that's what his wiki does.

To understand why this is technically interesting, you need to understand how most AI knowledge systems work today. The dominant pattern is called RAG — retrieval-augmented generation. It works like this: you take your documents, chop them into chunks (usually 300-500 words each), convert each chunk into an "embedding" (a list of numbers that represents the meaning of that text in a mathematical space — think of it as GPS coordinates, but for meaning instead of location), store those embeddings in a vector database, and when someone asks a question, you convert the question into an embedding too, find the closest document chunks by measuring distance in that mathematical space, and feed those chunks to an LLM along with the question.

RAG works. But it has a flaw that most people don't talk about. The chunks are fragments. They don't contain synthesized understanding — they contain pieces of the original text. The LLM has to synthesize on the fly, every single time someone asks a question. If you ask "how has thinking about AI agents changed over the past year?" the system retrieves 10 disconnected chunks from 10 different documents and tries to stitch them together in real time. Sometimes it does a good job. Often it misses connections because the relevant chunks aren't close in embedding space even though they're conceptually related.

Karpathy's approach flips this. Instead of retrieving raw chunks and synthesizing at query time, the LLM synthesizes at write time. It reads all the raw material once, thinks hard about it, and writes a structured wiki page that represents its understanding. When you need that knowledge later, you just read the wiki page. The synthesis is pre-computed.

This is the same tradeoff that databases have been making for decades. A materialized view in a database pre-computes an expensive query so that reads are fast. You pay the compute cost once at write time instead of paying it repeatedly at read time. Karpathy's wiki is a materialized view of his research knowledge.

This is also what gbrain (Garry Tan's knowledge system) does with its two-layer page model. Every brain page has a compiled_truth field (the pre-computed synthesis — always current) and a timeline field (the raw evidence, append-only). When new information arrives, the compiled_truth gets rewritten to incorporate it. The timeline just records what happened and when. It's the same architectural pattern Karpathy described, but productized.

Two more data points that connect to this. MCP — the Model Context Protocol from Anthropic — crossed 97 million installs last month. MCP is the standard way for AI agents to connect to external tools and data sources. The fact that it's hitting infrastructure-scale adoption means the plumbing for knowledge agents (agents that access, organize, and synthesize information from many sources) already exists. You don't need to build custom integrations anymore.

And Copilot, the biggest AI coding assistant, is still losing money on every paying user. GitHub hasn't figured out how to make "AI types your code faster" profitable at scale. Maybe that's a pricing problem. Or maybe it's a signal that the value of AI-as-typing-accelerator has a ceiling, and the real value is in AI-as-thinking-partner.

The pattern forming across all three data points: the most sophisticated AI practitioners are moving from "AI does my work" to "AI helps me think." The infrastructure for this (MCP, knowledge graphs, pre-computed synthesis) is maturing. The market hasn't caught up yet — most investment is still in coding assistants and chatbots. That gap is where the next wave of AI products will come from.

Meta launched Muse Spark, the first model from their new Superintelligence Labs (the team they built after the $14B Alexandr Wang deal). It's deliberately small and fast — good at science and math reasoning without being massive. This is the opposite bet from Anthropic's 10-trillion-parameter Mythos 5. The tension worth watching: does performance come from scale (more parameters) or from architecture (smarter design at smaller size)? The answer matters because it determines whether AI stays concentrated in a few companies who can afford massive compute, or becomes something anyone can run.

A research paper reported a system that cuts AI inference energy by 100x while improving accuracy. If this holds up outside the lab, it changes the economics of running multi-model pipelines. Today, calling 4-5 different models per pipeline run costs real money. A 100x efficiency gain would make sophisticated AI systems cheap enough to run for personal use, not just enterprise.

ProPublica journalists walked off the job in the first US newsroom strike over AI. Most AI newsletters skip this because their audience is pro-AI. But regulatory response follows labor action — it always has. If you're building AI systems in an enterprise, watch the policy response.

The thread that keeps building: "AI for thinking, not typing." Karpathy's RSS advocacy in February. The Obsidian + Claude Code explosion in March. Now the knowledge wiki. Each data point from a different direction, all pointing the same way.

If you read one thing today, read the gbrain README on GitHub — specifically the section on how pages are structured with compiled_truth and timeline. It's the production implementation of what Karpathy described, and understanding it will change how you think about knowledge systems. Takes about 15 minutes. github.com/garrytan/gbrain
