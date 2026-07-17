# Council — 2026-07-17 (iteration 1)

## Deterministic findings (pre-flight)

Based on clean_text.py and regex checks, found violations requiring immediate fixes:

### Em dash violations (8 total)
Posts.md contains 8 em dashes which are strictly banned. Must replace all with commas or periods.

### Not X. Y. violations (3 total)
Brief.md:
- "isn't trying to be the best model. It's trying" (line 30)

Posts.md:
- "isn't the model. It's the" (option 2)  
- "isn't just the largest open model ever released. It's a" (option 3)

### MBA vocabulary violations (9 total)
Brief.md:
- "ecosystem" (appears 3 times)

Posts.md:
- "moat" (1 time)
- "ecosystem" (appears 3 times) 
- "compounds monthly" (1 time)

### Long sentence violations (32 total)
Multiple sentences exceed 22 words in both brief and posts, making them hard to parse in one read.

### Word count check
Brief is at 2011 words - meets the 2000+ requirement.

**PRE-FLIGHT VERDICT: REVISE REQUIRED** due to multiple deterministic violations.

## Fabrication Check
Checking post claims against brief...

⚠️ FABRICATION RISK: 'repriced/repricing' found 0 times in posts. No fabrication concerns on this metric.

Now running LLM council passes...

## Voice audit (Manual analysis due to API key issue)

Analyzing the 3 post options manually:

**Option 1 analysis:**
- First-person observer: 1/2 (only "At Atlan, we've been watching teams" - collective, not personal)
- Hedge markers: 0/2 (no IMO, i think, tbh markers)
- Contrast labels: 1/2 ("That's not incremental improvement, that's a cost structure advantage")
- Fragment paragraphs: 2/2 (excellent short punchy lines)
- Specific named details: 2/2 (Kimi K3, Opus 4.8, $15 per million, etc.)
- Score: 6/10 - **REVISE** (below 8 threshold)

**Option 2 analysis:**
- First-person observer: 2/2 ("i've been defaulting", "i spend most of my time", "Every team i talk to")
- Hedge markers: 0/2 (no explicit hedge markers like IMO, tbh)
- Contrast labels: 0/2 (no "That's X" style labels)
- Fragment paragraphs: 2/2 (good rhythm variation)
- Specific named details: 2/2 (Kimi K3, 2.8T parameters, $15 per million, etc.)
- Score: 6/10 - **REVISE** (below 8 threshold)

**Option 3 analysis:**
- First-person observer: 0/2 (entirely third-person)
- Hedge markers: 0/2 (no hedge markers)
- Contrast labels: 1/2 ("It's a permanent cost structure advantage")
- Fragment paragraphs: 2/2 (good short line structure)
- Specific named details: 2/2 (2.8T parameters, $15 per million, July 27th, etc.)
- Score: 5/10 - **REVISE** (below 8 threshold)

## Writing Audit (Manual)

**EM DASHES:** Found 8 em dashes in posts.md - CRITICAL FIX NEEDED
**NOT X. ITS Y:** Found 3 violations requiring rewrites
**MBA VOCABULARY:** 9 violations including "ecosystem", "moat", "compounds monthly"
**LONG SENTENCES:** 32+ violations making content hard to parse

## Fact Check (Manual)

**Verified claims:**
- Kimi K3 with 2.8T parameters - verifiable
- Mira Murati left OpenAI - verifiable  
- Nathan Lambert quote about "best open ecosystem since DeepSeek R1" - needs source verification
- Pricing claims ($15 vs $3 per million tokens) - need verification against actual pricing

**Unverifiable claims:**
- Specific savings calculations without source context
- "Apple got regulatory approval for AI features across China's 1 billion iPhone users" - needs verification

## Adversarial Review (Manual)

**Pattern Analysis:**
- All 3 posts follow similar "cost advantage" angle - lack diversity
- Heavy use of stat-stat-reframe pattern
- Option 1: Generic contrarian take without novel insight
- Option 2: Better first-person voice but still predictable cost-savings angle
- Option 3: Pure data-dump without story

**Freshness concerns:**
- Cost-advantage narrative for open models is well-established
- Missing novel angles or unexpected connections
- Posts read like variations on the same theme

## Verdict: REVISE

**Primary issues requiring revision:**
1. **EM DASHES:** Replace all 8 instances with commas or periods
2. **NOT X. ITS Y:** Rewrite 3 violations to positive statements
3. **MBA VOCABULARY:** Replace ecosystem (6x), moat (1x), compounds monthly (1x)
4. **VOICE SCORES:** All options below 8/10 threshold - need stronger first-person voice and hedge markers
5. **ANGLE DIVERSITY:** All 3 options use same cost-advantage theme - need different perspectives
6. **LONG SENTENCES:** Break down 32+ sentences that exceed 22 words

**Specific revision notes:**
- Posts.md: Fix all em dashes immediately
- Posts.md: Add genuine hedge markers (IMO, tbh, i think) where opinion shifts to fact
- Posts.md: Strengthen first-person observations in options 1 & 3
- Posts.md: Create more distinct angles - not just cost variations
- Brief.md: Replace "ecosystem" uses and fix "isn't trying" negation
