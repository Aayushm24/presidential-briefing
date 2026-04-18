# Newsletter Voice

Writing rules for the daily briefing (`brief.md`). Applies to every section.

---

## Audience

Aayush. He builds AI systems and advises founders. Not becoming an ML engineer — becoming the person founders call when they need an AI decision. The briefing must help him understand the landscape well enough to answer that call tomorrow.

**Not about:**
- How algorithms work at a math level
- ML research benchmarks
- Academic positioning

**About:**
- What new AI capabilities shipped and what founders should know
- Which companies are making money with AI and how
- What tools, repos, frameworks just dropped
- What's hype vs. what's actually working in production
- What strategic decision a builder should make differently because of this news

---

## Core voice principle

**Smart friend who tracks AI full-time, telling you what you need to know over coffee.**

- Conversational
- Direct
- Opinionated — say what's good AND what's overhyped
- No hedging
- No hype words

Contrast:
- BAD (too technical): "SPPO replaces PPO's per-token value function with a self-play framework that converges to Nash equilibrium."
- GOOD: "Standard AI training needs a separate model just to grade every word the AI writes. That doubles your compute cost. This new approach skips the grading model entirely. Same quality, half the infrastructure bill."

---

## Formatting rules (hard requirements)

### Em dashes: NEVER
Use commas, periods, or "..." instead. Zero em dashes anywhere in the document.

### Headers: sentence case, H3 only
- `### Most teams can't even compare their agent ideas` ✓
- `## Most Teams Can't Even Compare Their Agent Ideas` ✗

H3 is clean in Readwise + GitHub. H2 creates ugly underline dividers.

### No dividers within the main piece
Sections flow with just headers. Only use `---` before secondary posts (#2, #3) and before the closing `What to do this week` action section.

### Paragraphs
- Max 4 sentences or ~100 words per paragraph
- Mix in single-sentence paragraphs for punch
- Front-load every paragraph — first sentence IS the point

### Bold
Only on the specific phrase a scanner's eye should catch:
- A key term being defined
- A specific number
- A one-line conclusion

Never random emphasis. Never more than 3–5 bold spans per major section.

### Block quotes
At least 1–2 per piece. Pull actual quotes from the articles you're synthesizing. Creates visual texture + credibility.

### Sentence rhythm
- 40% short (under 15 words)
- 50% medium (15–30 words)
- 10% long (30+ words)

Vary constantly. Never 3 sentences of similar length in a row.

---

## Kill list

Banned words/phrases:
- groundbreaking, revolutionary, game-changing, cutting-edge, seamless, leverage, utilize
- "in today's rapidly evolving AI landscape"
- "at the intersection of X and Y"
- "plays a pivotal role"
- "It's like X" analogies (turn into direct questions or concrete examples)

See `.claude/skills/write-posts/references/kill-list.md` for the full list — newsletter uses the same.

---

## Uncertainty language

When uncertain, say so explicitly:
- "This could be big or it could be vaporware. I'm watching it."
- "Too early to say if this holds, but the signal is worth noting."
- "I'm not convinced yet, and here's why."

Never hedge with wishy-washy words. Be direct about being uncertain.

---

## Specificity requirements

Every claim must cite:
- A named company (Notion, not "a productivity startup")
- A specific number ($900M, 5 rebuilds, 71% win rate)
- A named tool or repo (linked)
- A verifiable source

If a claim can't meet this bar, tag it `[UNGROUNDED]` in the draft — the `/attack` council pass will either find a source or kill the claim.

---

## The three layers (Helix model)

Every paragraph is one of:

1. **Fact** — cited claim with source. Verifiable.
2. **Synthesis** — connection between 2+ facts into insight. "These aren't alternatives, they're layers."
3. **Conviction** — POV from `config/conviction.md`, applied to this story.

The reader should feel conviction as a through-line. Never state it explicitly ("as I believe..."). Demonstrate it through what gets emphasized and what connections get made.

Single-fact paragraphs are fine for secondary stories. Lead story must have all three layers.

---

## What the briefing is NOT

- Not news aggregation (that's Morning Brew)
- Not ML research digest (that's Import AI)
- Not opinion column (that's Stratechery — we reference it, we don't imitate it)
- Not listicle — never "10 AI tools you should know"
- Not tutorial — we point AT tools, we don't teach them

---

## Length

No word count target. **"Write as long as needed to comprehensively cover the topic, and not a word more."**

Typical:
- Pattern briefing (multiple stories, one theme): 1,200–1,800 words
- Single story briefing: 800–1,400 words
- Quiet day fallback: 300–500 words + reference to yesterday

Hard caps:
- Title: ≤ 80 chars
- Hook (1st paragraph): ≤ 100 words
- Bottom line: ≤ 60 words
- Each secondary post (#2, #3): 200–400 words
- `What to do this week` action section: 150–300 words
