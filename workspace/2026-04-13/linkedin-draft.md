i've been sabotaging my own AI pipelines for months.

didn't even know it.

every prompt i wrote started with "think step by step." it was muscle memory. the internet said so. every tutorial agreed.

then i read a paper that tested chain-of-thought across 15 models.

the finding broke my brain:

CoT consistently degrades instruction-following accuracy.

not on edge cases. across nearly every model tested. GPT, Claude, LLaMA, DeepSeek.

for math and logic? still helps.

but for the tasks most production systems actually need?

- structured output
- JSON parsing
- classification
- format compliance

chain-of-thought actively hurts.

the reason is stupidly simple.

models have a fixed attention budget. when you force them to "show their work," those reasoning tokens eat the attention that should go toward following your format spec.

translating this to real world (where you and i live) — would you ever ask someone to explain their thinking AND fill out a form at the same time?

probably not.

i've been building multi-model pipelines at work. some tasks need reasoning. others need precision.

the moment i stopped treating "think step by step" as a universal default, my outputs got noticeably better.

the 10X AI engineers won't memorize every technique.

they'll know which technique to skip.

what's one "best practice" you stopped using and got better results?
