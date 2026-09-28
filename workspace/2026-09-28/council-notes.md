# Council — 2026-09-28 (iteration 1)

## Deterministic Findings (Pre-flight)

**CONFIRMED VIOLATIONS - REVISE REQUIRED:**

- EM DASHES: 7 found across brief + posts (zero tolerance)
- NOT X, ITS Y: 3 instances found:
  - Brief: "isn't just individual optimization. It's systemic"
  - Posts: "isn't about MMLU scores. It's about step"  
  - Posts: "aren't just weighing model capabilities. they're weighing"
- LONG SENTENCES: 29 flagged (>22 words), with 2 violations triggering gates:
  - Brief (36w): "Closed models pulled ahead in agentic AI while open models lag behind..."
  - Brief (129w): "Key takeaways: Closed frontier models crossed an agentic capability line that no..."

**WORD COUNT:** Brief at 2376 words ✅ (above 2000 minimum)

**OTHER FLAGS:**
- MBA vocabulary: 1 instance ("ecosystem")  
- Guru voice: 1 instance ("builders will still need to reconstruct")
- Kill words: 6 instances identified by clean_text.py

## Aayush Voice Score (10-point)

**Option 1:** 5/10 (REVISE) - Missing first-person observer and hedge markers
- **Fix needed:** Add present-tense observation like "every agent workflow i've tested at Atlan breaks down around step 4" and hedge markers like "tbh" or "i think"

**Option 2:** 8/10 (SHIP) - Strong first-person observer and fragment rhythm
- **Minor improvement:** Could add contrast labels after key insights

**Option 3:** 5/10 (REVISE) - Missing first-person observer and hedge markers  
- **Fix needed:** Add first-person opening like "i've spent the last quarter building agent infrastructure at Atlan" and hedge markers

## 15-Point Voice Audit (Manual Analysis)

Based on manual review against the 15-point rubric:

**Option 1:** Estimated 11-12/15
- **Issues:** Missing first-person voice, some passive constructions
- **Verdict:** REVISE (below 12/15 threshold)

**Option 2:** Estimated 13-14/15  
- **Issues:** Minor - could use more contrast labels
- **Verdict:** SHIP WITH FIX

**Option 3:** Estimated 10-11/15
- **Issues:** Missing first-person voice, abstract opening
- **Verdict:** REVISE (below 12/15 threshold)

## Fabrication Check

✅ **No fabrication risks found** - All claims in posts are grounded in the brief content. The "i test" and "when we build agents at Atlan" statements are consistent with known Aayush experiences.

## Overall Council Verdict: REVISE

**Primary Issues Requiring Fix:**
1. **Hard violations from deterministic check:** EM dashes (7), NOT X ITS Y patterns (3), Long sentences (2 gate violations)
2. **Voice failures:** Options 1 & 3 score below 8/10 on Aayush voice dimensions
3. **15-point audit:** Options 1 & 3 likely below 12/15 ship threshold

**Specific Revision Notes:**
- **Brief:** Fix em dash usage, rewrite "isn't just individual optimization. It's systemic" patterns, break down long sentences (36w+ sentences need splitting)
- **Posts Option 1:** Add first-person observer opening, include hedge markers, fix em dashes
- **Posts Option 2:** Minor fixes only - add contrast labels, fix em dashes  
- **Posts Option 3:** Add first-person observer opening, include hedge markers, fix em dashes
