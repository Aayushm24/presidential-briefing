# Council — 2026-07-30 (iteration 1)

## Deterministic findings (pre-flight)

**CONFIRMED violations found via regex and clean_text.py — MUST fix before ship:**

### Word count violation
- Brief is at 1472 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Em dash violations (16 total)
- Em dashes found throughout both brief and posts. All must be replaced with regular hyphens or commas.

### MBA vocabulary violations 
- "moat" appears in posts.md Option 2. Replace with "the thing competitors can't copy" or name the specific advantage.

### Guru voice violations (3 total)
- Brief: "For builders, this changes..." (appears twice) - rewrite in first-person observation
- Posts: "Teams are treating AI like a magic eight-ball when they should be..." - remove prescription, make observational

### Long sentence violations (2 total files violated)
- Multiple sentences over 22 words in both brief and posts need to be split

### Not X, it's Y violation (1 total)
- Posts: "isn't the LLM. It's the" - rewrite without inversion pattern

**PRE-FLIGHT VERDICT: REVISE** (due to confirmed violations above)

## Aayush Voice Audit (partial results)
**Option 1:** Score appeared to be 8/10 (partially truncated response)
- Good first-person observer presence ("I see it across every builder I talk to")  
- Specific named details (OpenAI, GPT-5.6, ARC-AGI-3, 32% to 91%, Atlan)
- Missing hedge markers (no IMO, tbh, fwiw)

**Option 2:** Strong first-person observer voice ("I watch teams", "Every week I see")
- Has specific company names and numbers
- Uses present-tense observation pattern

**Option 3:** Has personal anecdotes ("I broke GPT once", "My mom asked AI") 
- Specific numbers ($180 per million tokens, 47 times, 147 words)
- Absurdist style with humor

## Fact Check Findings (partial)
- Brief and posts reference GPT-5.6 and specific performance claims (32% to 91% on ARC-AGI-3)
- Claims about OpenAI API settings need verification
- Microsoft investment amounts ($3.2B from Anthropic) need verification
- All em dash counts flagged throughout content

## Overall Verdict: REVISE

**Primary Issues requiring fixes:**
1. **Word count violation** - Brief at 1472 words, needs 2000+
2. **16 em dashes** throughout both files - must replace all
3. **MBA vocabulary** - "moat" in posts must be replaced  
4. **Guru voice** - 3 instances of prescriptive language
5. **Long sentences** - Multiple sentences over 22 words
6. **Not X, it's Y inversion** - "isn't the LLM. It's the harness"
