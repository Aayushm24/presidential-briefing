# Kill List

Words, phrases, patterns, formatting banned from every LinkedIn post and briefing. Any violation = automatic revise.

## 1A: Classic AI buzzwords
delve, testament, tapestry, landscape, paradigm, paradigm shift, ecosystem, synergy, synergies, holistic, empower, democratize, disrupt, disruption, disrupting

## 1B: Corporate fluff
crucial, robust, cutting-edge, seamless, leverage, utilize, optimize, streamline, scalable, innovative, best-in-class, world-class, next-generation, state-of-the-art, mission-critical, end-to-end

## 1C: AI tells (2025–2026)
"at its core", "plays a significant role", "it's important to note", "it's worth noting", "in today's rapidly evolving", "the future of", "in an era of", "as we navigate", "the intersection of"

## 1D: Overwrought emotion
breathtaking, extraordinary, unparalleled, remarkable, game-changing, game changer, groundbreaking, ground-breaking, revolutionary, transformative, transformational, unprecedented, monumental

## 1E: Transition crutches
"In fact", "Indeed", "Additionally", "Furthermore", "Moreover", "Notably", "Interestingly", "Importantly", "Essentially", "Fundamentally", "Ultimately"

## 1F: Cliche openers
"Imagine if", "Picture this", "Let me share", "Here's what I learned", "I've been thinking a lot about", "Let's talk about", "Can we talk about", "Hot take:", "Unpopular opinion:", "I'll say it:", "Great question!", "I spent X hours researching this so you don't have to"

## 1G: Structural patterns
- Bullet points (`•`) — ALWAYS use dashes (`-`) instead
- Em-dashes — use commas or periods
- More than 1 emoji per post
- Hashtag spam (max 3, only at end, exact topical match)
- Starting 3+ sentences with the same word
- Rule of three (LLMs force groups of 3 — use 2 or 4 instead)
- Generic positive conclusions ("The future looks bright", "Exciting times ahead")
- Starting the post with uppercase "I" (use lowercase "i" for confessional style, or start with the topic)
- Bold more than 3–5 words in the entire post
- Lists without story context
- Pure self-promotion without value
- Explaining why you're qualified before giving the insight
- Three short sentences in a row (sentence-length rhythm required)
- Same word repeated twice in one post (other than proper nouns and conjunctions)

## 1H: LLM analogy patterns
- "It's like [analogy]. [Short dramatic sentence]." — most common LLM tell
- "Think of it as [analogy]." — second most common
- Any analogy stated as a declaration instead of a question to the reader
- Fix: turn analogies into direct questions using "you and I" language

## 1I: Engagement bait
- "Like if you agree"
- "Comment YES if..."
- "Share this with someone who needs to hear it"
- "Tag someone who..."
- Questions as hooks (algorithm penalizes this)
- "Who else feels this way?"
- "Am I the only one who..."

## 1J: Formatting violations
- No line breaks between ideas (every idea needs its own line)
- Dense paragraphs (max 2–3 sentences per paragraph, prefer 1)
- Numbered lists without story (pure listicles feel AI-generated)
- Consistent sentence length (must have rhythmic variation — short, medium, long cascade)

## 1K: Corporate announcement language (from atlan-linkedin-posts)
- "excited to announce"
- "thrilled to announce"
- "proud to announce"
- "honored to announce"
- "unlock the power of"
- "at Atlan we believe" (or any "at X we believe" formula)
- "check out our latest"
- "Learn more" as CTA

## 1L: Audience direct-address (founder-specific)
- "for founders"
- "hey founders"
- "fellow founders"
- "if you're a founder"
- Any second-person address targeting the audience as a category

## 1M: Composite AI tells (auto-flagged by /attack)
- "in today's [X] landscape" — double violation (1C + 1A)
- "leverage AI to seamlessly [verb]" — triple stacked
- "cutting-edge, game-changing, revolutionary" — any two of these in one post

## Enforcement

During `/attack` review:
1. Scan for every word/phrase in 1A–1F + 1K.
2. Check formatting against 1G + 1J.
3. Check analogies against 1H.
4. Check CTAs against 1I.
5. Check audience framing against 1L.
6. Any match = specific revision instruction. "Replace 'leverage' with 'use'." "Turn this analogy into a question." "Cut 'for founders'."
7. Re-scan after revision. Repeat until clean.

The `/attack` skill uses regex tests from `tests/kill-list-regex.sh` as a fast pre-filter before the LLM pass.
