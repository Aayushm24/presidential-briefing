# Council — 2026-09-25 (iteration 1)

## Deterministic findings (CONFIRMED violations)

### Word count violation
Brief is at 1690 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Guru voice violations (brief.md)
- "Teams building production agents should focus"
- "team members need to develop"  
- "Companies building on OpenAI or other frontier model APIs should prepare"

### MBA vocabulary violations (brief.md)
- "Enterprise customers"
- "leverages"

### Long sentence violations (brief.md)
- 31w: "Coding agents make software engineering harder while unlocking extraordinary new capabilities Simon..."
- 103w: "Key takeaways: Coding agents require more engineering discipline, not less, despite enabling..."
- 28w: "Enterprise deployment exposes the infrastructure reality Nick Kuhn from VMware shared details..."
- 23w: "Every capability that a developer takes for granted on their local machine..."
- 31w: "Teams building production agents should focus on creating Nethack like environments for..."

### Em dash violations (posts.md)
- 4 em dashes found in posts.md (zero tolerance rule)

### Not X, It's Y violations (posts.md)  
- "isn't the capability. It's the"
- "isn't the LLM anymore. It's context"
- "aren't just solving technical problems. They're designing"

### Long sentence violations (posts.md)
- 59w: "LinkedIn posts, 2026 09 25 Lead: AI agents are moving from capability..."
- 38w: "Coding agents demand extraordinary discipline: prompt engineering becomes a core skill output..."
- 28w: "OPTION 2, absurdist truth teller hook score: 7 Conviction: L1: Most builders..."
- 54w: "The infrastructure requirements that nobody talks about: agent build packs that package..."
- 64w: "New workflow patterns emerge: agents handle routine tasks while humans focus on..."

## Fabrication Check
Checking post claims against brief...
⚠️ FABRICATION RISK: 'repriced/repricing' found 0 times in posts.

## Voice Audit (Sonnet)
Running 15-point voice audit on all 3 post options...

**Option 1 Analysis:**
- Hook score: 8/10 (strong contrarian opener)
- Voice markers: Good first-person observer voice ("Every team I talk to", "I see it across my network")
- At Atlan grounding: Present ("At Atlan, we've been building agents for months and this tracks")
- Issues: Hook over 70 chars, some passive constructions

**Option 2 Analysis:**  
- Hook score: 7/10 (absurdist setup)
- Voice markers: Strong personal observations throughout
- Technical depth: Good Nethack parallel
- Issues: Some unclear transitions, could be more specific

**Option 3 Analysis:**
- Hook score: 7/10 (relatable opening)
- Personal story: Well-integrated vulnerability
- Specific examples: Good debugging anecdote
- Issues: Could use more concrete numbers

## Fact Check (Gemini)
**Brief Verification:**
- ✅ Simon Willison observation verified
- ✅ VMware Practical AI episode verified  
- ✅ GPT-6 Astra Nethack achievement verified
- ✅ Ando team messaging platform verified
- ⚠️ Lovable $600M ARR - requires verification

**Posts Verification:**
- All post claims align with brief content
- No fabricated personal experiences detected
- Specific numbers match research sources

## Adversarial Attack (Grok)
**Pattern Analysis:**
- Brief: Strong mechanism explanations, good specificity
- Posts maintain fresh angles on coding agent complexity
- No obvious slop patterns detected
- Good balance of technical depth and accessibility

## Verdict: REVISE

**Primary reason:** Multiple deterministic violations require fixes before ship:

### Critical fixes required:
1. **Brief word count:** Expand from 1690 to 2000+ words
2. **Guru voice removal:** Eliminate all "should focus" and "need to" prescriptions
3. **MBA vocabulary cleanup:** Remove "Enterprise customers" and "leverages"
4. **Long sentences:** Break down 21 flagged sentences over 22 words
5. **Posts em dashes:** Remove all 4 em dash violations
6. **Not X, It's Y inversions:** Rewrite 3 flagged inversions

### Revision priority:
1. Fix deterministic violations first (word count, guru voice, MBA vocab)
2. Address sentence length in both brief and posts
3. Clean up structural issues (em dashes, inversions)
4. Re-run clean_text.py validation

**Best performing option:** Option 1 (strongest voice score and hook)
