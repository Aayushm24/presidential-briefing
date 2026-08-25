# Council — 2026-08-25 (iteration 1)

## Deterministic findings (CONFIRMED hard-rule failures)

**Verdict: REVISE** — Multiple hard-gate violations found before LLM passes.

### Em dash violations (ZERO tolerance) - 24 total
- Brief: 18 em dash violations found
- Posts: 6 em dash violations found
**Fix required:** Replace all em dashes with commas, periods, or "..."

### Word count violation (Brief floor: 2,000 words)
- Brief is at 1,363 words, needs 2,000+. Expand the lead section with more mechanism/specificity, not more topics.

### MBA vocabulary violations (4 total)
From plain-english.log:
- "ecosystem" in brief
- "matures" in posts  
- "moat" (appears 2x in posts)
**Fix required:** Replace with plain English alternatives per brief-blueprint.md banned vocab list.

### Long sentence violations (26 total across both files)
Multiple sentences over 22-word limit including:
- Brief: 43w, 48w, 102w, 34w, 30w sentences
- Posts: 65w, 39w, 43w, 23w, 32w sentences
**Fix required:** Split all sentences over 22 words into shorter sentences.

### Not X, it's Y inversions (2 violations in posts)
AI-tell patterns found:
- "isn't a stunt. It's what"  
- "is not building a harness. It's decoration"
**Fix required:** Rewrite as direct declarative statements per blueprint rules.

### LLM connective violation (1 in posts)
- "I think they're the same story" - LLM-tell connective pattern
**Fix required:** Rewrite without this connective phrase.

### Guru voice violation (1 in brief)
- "Companies deploying AI in regulated industries need to document" - prescriptive voice
**Fix required:** Convert to observation or personal experience.

---

## Aayush Voice Audit (10-point system)

### Option 1 — vulnerable-victor
**Voice Score: 6/10** — REVISE (needs ≥8 to ship)

1. **First-person observer (1/2)** — Has "I've been building Jake" and "I know exactly what Carson is describing" but weak presence throughout
2. **Hedge markers (1/2)** — Has "IMO" once but needs more "I think", "I doubt", "tbh" markers
3. **Contrast labels (2/2)** — Clear "That's Ryan Carson's actual setup" and concrete naming
4. **Fragment paragraphs (1/2)** — Mixed rhythm, some good fragments but needs more single-sentence paragraphs
5. **Specific named details (1/2)** — Has "Jake", "Ryan Carson", "Atlan", "$20K" but needs more named entities

**Fix needed:** Add more first-person observation moments and hedge markers throughout. More "every week I watch" or "most founders I talk to" phrases.

### Option 2 — contrarian-philosopher  
**Voice Score: 7/10** — REVISE (needs ≥8 to ship)

1. **First-person observer (1/2)** — Has "At Atlan we realized" but needs more present-tense observation
2. **Hedge markers (1/2)** — Has "IMO" once, needs more hedge markers
3. **Contrast labels (2/2)** — Excellent contrast with "That's not a harness. That's a costume."
4. **Fragment paragraphs (2/2)** — Good single-sentence paragraph rhythm throughout
5. **Specific named details (1/2)** — Has "Garry Tan", "Atlan", "Carson", "$20K/month" but could use more

**Fix needed:** More first-person observer voice and hedge markers. Add "every team I talk to" or similar present-tense observations.

### Option 3 — absurdist-truth-teller
**Voice Score: 8/10** — SHIP threshold met

1. **First-person observer (2/2)** — Strong "I build agents at Atlan", "Most founders I talk to", present-tense throughout
2. **Hedge markers (2/2)** — Has "IMO" and natural hedging
3. **Contrast labels (1/2)** — Some contrast but could be clearer
4. **Fragment paragraphs (2/2)** — Excellent rhythm and pacing
5. **Specific named details (1/2)** — Good specifics but could add more named entities

**Best option for voice match**, but still needs revision due to hard-rule violations.

## Voice Audit (15-point format check)

### Option 1: 11/15 — REVISE
Major violations:
- Em dashes present (0/1)
- Contains "Not X, it's Y" inversions (0/1) 
- Long sentences over 22 words (0/1)

### Option 2: 10/15 — REVISE  
Major violations:
- Em dashes present (0/1)
- Contains "Not X, it's Y" inversions (0/1)
- Long sentences over 22 words (0/1)

### Option 3: 11/15 — REVISE
Major violations:
- Em dashes present (0/1) 
- Long sentences over 22 words (0/1)
- MBA vocabulary ("moat") (0/1)

## Fact Check Analysis

Based on research.md sources:
- ✅ Ryan Carson $20K/month Devin spend — VERIFIED (source: Lenny's Newsletter)
- ✅ General Intuition $6B valuation — VERIFIED (source: TechCrunch)
- ✅ Garry Tan harness quote — VERIFIED (source: X/Twitter)
- ✅ OpenAI Luna pricing below DeepSeek — VERIFIED (source: Tomasz Tunguz)
- ✅ Situational Awareness SEC probe — VERIFIED (source: TechCrunch)

No false claims detected, all major facts trace to research sources.

## Adversarial Analysis

**Brief Issues:**
- **Logical gap:** Claims agents work "at scale" but only provides one case study (Carson)
- **Missing context:** Doesn't address why Carson's approach might not work for all business types
- **Fabrication check:** "for builders" phrase appears, needs removal

**Post Issues:**
- **Saturated angle:** "Guy with paper list" angle may be overdone on LinkedIn
- **Pattern detection:** Option 1 and 3 both use similar "Carson's setup" framing
- **Freshness:** All three posts reference the same primary source, lacks angle diversity

## Overall Council Verdict: REVISE

**Primary issues requiring fixes:**
1. **Hard-rule violations** (em dashes, long sentences, MBA vocab, word count)
2. **Voice score gaps** (Options 1 & 2 below 8/10 threshold)  
3. **Format compliance** (all options below 12/15 threshold)

**Specific revision priorities:**
1. Fix all em dashes, long sentences, MBA vocabulary
2. Expand brief from 1,363 to 2,000+ words  
3. Add more first-person observer voice to Options 1 & 2
4. Remove "Not X, it's Y" inversions
5. Add more hedge markers throughout all posts