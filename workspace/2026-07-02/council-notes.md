# Council — 2026-07-02 (iteration 1)

## Deterministic findings (CONFIRMED violations)

⚠️ **HARD RULE FAILURES DETECTED** - Verdict: REVISE

**MBA Vocabulary violations (5 found):**
- "enterprise customers" (multiple instances)
- "Enterprise customers"

**Long sentence violations (21 found - excerpts from clean_text.py):**
- 49w: "Cursor built an internal sales AI that books 3x qualified meetings, and..."
- 28w: "George Hou https://www.thesignal.club/p/chatgtm built ChatGTM for Cursor's 400+ person sales org with..."
- 134w: "Key takeaways: Cursor's internal ChatGTM system generates 3x qualified meetings for SDRs..."
- 25w: "ChatGTM pulls company intelligence from multiple data sources, scores prospect fit based..."
- 25w: "New AEs get conversation guides that reference the prospect's current development stack,..."
- 71w: "LinkedIn posts, 2026 07 02 Lead: Cursor built an internal sales AI..."
- 28w: "Cursor's Head of Enterprise Growth just published the numbers from their internal..."
- 25w: "ChatGTM pulls company intelligence from multiple data sources, scores prospect fit based..."
- 23w: "The question for builders is whether to build these systems before competitors..."

**Word count violation:**
- Brief is at 1585 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

**Em dash violations (6 found):**
- Multiple em dashes detected in both brief and posts

**Not X, it's Y violations (2 found):**
- "This is not theory. This is the" (appears in both brief and posts)

**Guru voice violation (1 found):**
- "Startups that have already trained on web data may need to retrain"

## Fabrication Check
Checking post claims against brief...
⚠️ FABRICATION RISK: Need to verify all numerical claims against source material

## Post-clean_text.py Status
After running clean_text.py, violations remain:
- MBA vocabulary: 5 instances ("enterprise customers")
- Long sentences: 21 instances (>22 words)
- Not X, it's Y: 2 instances ("This is not theory. This is the")
- Guru voice: 1 instance ("Startups that have already trained...")

## Voice Audit (Manual Review)
Without working LLM proxy access, conducted manual review:

**Option 1 (Contrarian Philosopher):**
- ❌ Hook length: >70 chars ("Most AI companies are still hiring sales reps like it's 2015")
- ❌ Long sentences: Multiple violations >22 words
- ❌ MBA vocabulary: "enterprise" usage
- ✅ Named tools: ChatGTM, Cursor
- ✅ Specific numbers: 3x meetings, 50% faster
- ❌ Not X, it's Y violation: "This is not theory. This is the"

**Option 2 (Personal-I Observer):**
- ✅ Hook: "Every week i watch..." (good first-person observer)
- ✅ Lowercase i: Consistent usage
- ❌ Long sentences: Multiple violations
- ❌ MBA vocabulary: "enterprise" usage
- ✅ Named tools: Cursor, Forward Deployed Engineers

**Option 3 (Absurdist Truth-Teller):**
- ✅ Hook: Strong contrarian opener
- ✅ Specific numbers: $65M, $1B, $70M ARR
- ❌ Long sentences: Multiple violations
- ❌ MBA vocabulary: "enterprise" usage

## Fact Check
- ✅ Venice AI funding: $65M Series A verified
- ✅ Cursor ChatGTM: 3x meetings claim sourced
- ⚠️ Need to verify specific implementation details

## Adversarial Review
- Brief word count: 1585 words (needs 2000+ for format compliance)
- Posts have strong angles but suffer from length/MBA vocabulary issues
- Option 1: Solid contrarian take but needs sentence shortening
- Option 2: Good first-person voice but too wordy
- Option 3: Compelling absurdist angle but verbose

## VERDICT: REVISE

**Primary issues requiring revision:**
1. Brief word count: Expand from 1585 to 2000+ words
2. Long sentences: Break all 22+ word sentences into shorter ones
3. MBA vocabulary: Replace "enterprise customers" with "big companies" or similar
4. Not X, it's Y: Rewrite "This is not theory. This is the blueprint" 
5. Guru voice: Fix "Startups that have already trained..."

**Recommended revisions:**
- Brief: Expand lead section with more mechanism/specificity
- Posts: Shorten sentences, replace MBA terms, maintain voice authenticity
- All: Remove "Not X, it's Y" constructions
