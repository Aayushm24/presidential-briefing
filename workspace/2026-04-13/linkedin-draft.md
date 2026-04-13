"Think step by step" is making your AI system worse.

New research tested chain-of-thought prompting across 15 models. GPT, Claude, LLaMA, DeepSeek. The finding: CoT consistently degrades instruction-following accuracy. Not on some models. Nearly all of them.

Everyone teaches "add reasoning steps to improve output." For math and logic, that's still true. But for the tasks most production systems actually need — structured output, JSON parsing, classification, format compliance — chain-of-thought actively hurts.

The reason is simple. The model has a fixed attention budget. When you ask it to "show its work," those reasoning tokens consume attention that would otherwise go toward following your format spec. It's like asking someone to explain their thinking and fill out a form at the same time. One suffers.

I've been building multi-model pipelines where some tasks need reasoning and others need precision. This paper confirmed something I suspected: your scoring and classification tasks should use direct prompting. Your writing and synthesis tasks should use CoT. Same system, different technique per task.

The 10X AI engineers won't be the ones who memorize every technique. They'll be the ones who know which technique to skip.

When's the last time you removed "think step by step" from a prompt and got better results?
