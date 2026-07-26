# Council — 2026-07-26 (iteration 1)

## Deterministic Findings — CONFIRMED Violations

Pre-flight regex and clean_text.py analysis found multiple hard-rule failures that require revision:

### Word Count Violation
Brief is at 1,576 words, needs 2,000+. Expand the lead section with more mechanism/specificity, not more topics.

### MBA Vocabulary Violations (4 hits)
- "infrastructure dependency" (brief)
- "Enterprise customers" (brief, 2 instances)  
- "Enterprise customers" (posts)

### Long Sentence Violations (18 hits, exceeding limit)
Key offenders include:
- 41w: "The open weights movement is fracturing and builders should prepare for access instability"
- 151w: "Key takeaways: The 500 builders supporting open weights have fundamentally different views..."
- 46w: "AI displacement is proven enough to drive backlash that capability arguments cannot overcome"

### Guru Voice Violations (5 hits)
- "Builders betting their infrastructure on open model availability should read" (brief)
- "Builders who design AI-dependent products should treat" (brief) 
- "companies that use oil to build products customers want to buy" (brief, 2 instances)
- "builders betting infrastructure on open weights should read" (posts)

### Em Dashes in Posts (9 hits)
Zero tolerance for em dashes (U+2014). All must be removed.

### "Not X, it's Y" Pattern (1 hit)
- "aren't going away. They're a" (posts)

## Fabrication Check
Checking post claims against brief...
⚠️ Post claim check: "rare demand" vs brief's "unprecedented demand" for AI workshops - inconsistency detected.

## Iteration 1 Results

**RESOLVED:**
- ✅ Word count increased from 1,576 to 2,116 words
- ✅ Em dashes removed (0 remaining)  
- ✅ "Not X, it's Y" pattern fixed (0 remaining)
- ✅ Fabrication fixed ("rare demand" → "unprecedented demand")

**REMAINING VIOLATIONS:**
- ⚠️ Guru voice: 5 instances still present
- ⚠️ MBA vocabulary: 3 instances still present  
- ⚠️ Long sentences: 22 instances still present

## Verdict: NEEDS ITERATION 2

Specific revision priorities:
1. **Expand brief to 2,000+ words** - add mechanism depth to lead section
2. **Remove all MBA vocabulary** - replace with plain English alternatives
3. **Break long sentences** - split all 22+ word sentences
4. **Remove guru voice** - rewrite all "builders should..." prescriptions as observations
5. **Remove em dashes** from posts - replace with commas/periods
6. **Fix "not X, it's Y"** inversion in posts
7. **Fix fabrication** - align "rare demand" with "unprecedented demand"