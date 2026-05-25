# Council — 2026-05-25 (iteration 1)

## Deterministic findings (pre-flight violations)

**CONFIRMED hard-rule failures from clean_text.py scan:**

### Brief violations:
- **EM DASHES: 20 instances** — automatic fail threshold exceeded 
- **NOT X, IT'S Y: 3 instances** — Zero tolerance policy violated
  - "isn't to build more sophisticated reasoning systems. It's to"
  - "isn't a limitation of current models. It's fundamental"  
  - "aren't mature standards developed over decades. They're active"
- **GURU VOICE: 2 instances** — Direct violation of voice rules
  - "teams that build interfaces assuming users want to hand"
  - "founders making infrastructure decisions should evaluate"
- **MBA VOCABULARY: 1 instance**
  - "enterprise customers" (banned in briefs, flagged for replacement)
- **LONG SENTENCES: 5 instances over 22-word limit**
  - 36w: "AI augmentation demands more human judgment, not less Dan Shipper spent a..."
  - 131w: "Key takeaways: AI augmentation creates more human touchpoints, not fewer, successful teams..."
  - Plus 3 additional violations

### Posts violations:
- **EM DASHES: 13 instances** — posts-gate.sh will reject at ship
- **MBA VOCABULARY: 2 instances**
  - "moat" appears twice (allowed in posts, different from brief rules)
- **LONG SENTENCES: Multiple violations**
  - Including 69w header line and several compound sentences

**Verdict from deterministic scan: REVISE REQUIRED** — Cannot ship with em-dash violations.

---

## Aayush voice score (10-point gate check)

### Option 1: 8/10 — SHIP
- First-person observer: 2/2 (strong present-tense placement)
- Hedge markers: 2/2 ("IMO" well-placed)  
- Contrast labels: 1/2 (weak resolution)
- Fragment paragraphs: 2/2 (clean single-idea rhythm)
- Specific named details: 1/2 (borrows Dan's data, no proprietary Aayush numbers)

### Option 2: 6/10 — REVISE
- First-person observer: 1/2 (weak résumé line, not genuine observation)
- Hedge markers: 0/2 (**FATAL** — zero instances of IMO/tbh/fwiw/i think)
- Contrast labels: 1/2 (soft setup, no crisp resolution)
- Fragment paragraphs: 2/2 (strong single-idea lines)
- Specific named details: 2/2 (best specificity of the three)

### Option 3: 5/10 — REVISE  
- First-person observer: 1/2 (arrives late, feels inserted)
- Hedge markers: 0/2 (**FATAL** — stated as universal laws)
- Contrast labels: 1/2 (contrast setup, no labeled snap)
- Fragment paragraphs: 1/2 (mixed, essay register creeps in)
- Specific named details: 0/2 (**FATAL** — no Aayush-owned numbers, all generic)

**Voice gate result:** Only Option 1 meets the 8/10 threshold for shipping.

---

## Writing audit (Sonnet compliance check)

**Total violations: 20 across brief + all three posts**

### Brief violations (6):
- EM DASH: 1 instance in key takeaways bullet  
- VAGUE GENERICS: 4 instances ("Most agent frameworks", "every investor pattern-match", "top labs", unattributed narrative)
- UNSOURCED STATS: 1 instance ("significant real usage")

### Option 1 violations (4):
- EM DASH: 1 instance in interface layer sentence
- CONVICTION MISSING: IMO hedge weakens direct statement
- PADDING: 2 instances of restated content

### Option 2 violations (6):  
- NOT X, Y NEGATION: 2 instances
- UNSOURCED STATS: 3 instances ("significantly more time", "much more effort", percentage question baseline)
- PADDING: 1 instance

### Option 3 violations (4):
- VAGUE GENERICS: 1 instance ("everywhere I look")  
- UNSOURCED STATS: 1 instance (Miller's Law needs attribution)
- PADDING: 2 instances of restated conclusions
- NOT X, Y NEGATION: 1 instance ("not committee")
- PASSIVE VOICE: 1 instance

---

## Fact check (Gemini verification)

### Brief:
- **VERIFIED:** Dan Shipper runs Every (CEO and co-founder), Every is a media company, Miller's Law (7±2 items)
- **UNVERIFIABLE:** Exact "30-person" count (LinkedIn shows 15-20), exact "year" timeline of AI usage
- **FALSE:** None found
- **EM DASHES:** 0 found in submitted snippet (incomplete review due to truncated input)

### Posts: 
- Factual claims largely derivative from brief
- No independent fact-check violations found in post content
- EM DASHES: Multiple instances flagged as automatic fail

**Recommendation:** Option with fewest issues = brief (but posts need revision for em-dash removal)

---

## Adversarial attack (Grok freshness + anti-slop)

### Brief verdict: REVISE
- **Logical gaps:** Dan Shipper study methodology not summarized, no concrete examples
- **Unsupported claims:** "Every successful AI implementation" assertion too broad
- **Straw men:** "AI will replace humans narrative" dismissed without engaging strongest counter-version  
- **NOT X, IT'S Y:** Multiple violations confirmed
- **Guru voice:** "Winners design for active participation" = prescriptive positioning

### Option 1 verdict: REJECT
- **Freshness:** SATURATED (similar takes flooding X timeline)
- **Builder relevant:** FALSE (generic authority claim without practitioner detail)
- **Guru voice:** "Every week I watch founders" = unsubstantiated authority positioning
- **Critique:** Recycles briefing's exact stat without adding practitioner insight

### Option 2 verdict: REJECT  
- **Freshness:** SATURATED
- **Builder relevant:** FALSE 
- **Critique:** Pure "Stat-Stat-Reframe-Metaphor" scaffolding with zero new insight

### Option 3 verdict: REVISE
- **Freshness:** SATURATED  
- **Builder relevant:** TRUE (concrete mortgage metaphor engages counter-examples)
- **Critique:** Best of three — uses concrete metaphor instead of binary flattening

### Angle diversity: FAIL
All 3 options use same "study quote + binary inversion" Blueprint style — lack diversity required for shipping

**Grok recommendation:** Option 3 (only one with builder relevance despite flaws)

---

## Overall Council Verdict: REVISE

**Cannot ship due to:**
1. **Deterministic violations:** 33 em-dashes (automatic fail threshold)  
2. **Voice gate failures:** Options 2 & 3 score below 8/10 minimum
3. **Writing audit:** 20 violations across content  
4. **Adversarial review:** All posts saturated angle, 2 of 3 rejected entirely
5. **Angle diversity fail:** All 3 use identical Blueprint style approach

**Specific revision priorities:**
1. **URGENT:** Remove all em-dashes from brief and posts (hard-gate blocker)
2. **VOICE:** Add hedge markers (IMO, tbh, fwiw) to Options 2 & 3 
3. **SPECIFICITY:** Replace Aayush's generic claims with concrete Atlan examples + numbers
4. **ANGLE DIVERSITY:** Rewrite 2 of 3 posts with different Blueprint styles (not all "study quote + inversion")
5. **FRESH TAKES:** Option 1 & 2 are saturated — need unique practitioner insights beyond Dan's study

**Best foundation for revision:** Option 3 (only builder-relevant angle, despite needing voice fixes)

**Iteration count:** 1 → proceeding to /revise with detailed fix notes above.