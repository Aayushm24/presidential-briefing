# Council — 2026-06-10 (iteration 1)

## Deterministic findings (pre-flight)

**CONFIRMED violations from regex and clean_text.py — REVISE required:**

### Brief violations:
- **Guru voice (2 hits):** "Teams building on Claude need to implement" + "For builders"
- **MBA vocabulary:** "table stakes" + "enterprise customers"  
- **Long sentences (5 hits):** 
  - 43w: "Lovable hits $500M ARR, Fable 5 ships with silent guardrails that could..."
  - 108w: "Key takeaways: Lovable reports $500M ARR with 1M new projects weekly, proving..."
  - 29w: "Lovable https://techcrunch.com/2026/06/09/lovable says it has hit 500m in annualized revenue with 1..."
  - 27w: "If 1 million people per week will start new projects on a..."
  - 26w: "This extends beyond coding to design tools, marketing automation, content management, anything..."

### Posts violations:
- **Em dashes (7 hits):** Em dashes found in posts.md, LinkedIn will render as broken display
- **Not X, it's Y inversions (2 hits):** "aren't building better tools for engineers. They're building" + "isn't about no-code. It's about the"
- **Guru voice (1 hit):** "Teams using Claude in production need to know"
- **Long sentences (multiple hits in formatted headers)**

**Verdict from deterministic checks: REVISE**

---

## Aayush voice score (10-point gate at 8)

**Results from Gemini voice audit:**

- **Option 1:** 10/10 — SHIP (perfect voice markers)
  - first_person_observer: 2 ("Most people I talk to", "At Atlan, we see")
  - hedge_markers: 2 ("IMO")
  - contrast_labels: 2 ("That's not the story", clear inversions)
  - fragment_paragraphs: 2 (excellent rhythm)
  - specific_named_details: 2 (Lovable, $500M, 1M projects, Atlan, Notion)

- **Option 2:** 6/10 — REVISE (below 8 threshold)
  - first_person_observer: 2 ("I've been testing", "I build AI agents")
  - hedge_markers: 0 (missing IMO/tbh/etc)
  - contrast_labels: 1 (weak contrast)
  - fragment_paragraphs: 1 (mixed long/short)
  - specific_named_details: 2 (Sebastian Raschka, Simon Willison, Atlan)
  - **Fix needed:** Add hedge markers, convert to strict contrast labels, break up long paragraphs

- **Option 3:** 5/10 — REVISE (below 8 threshold)
  - first_person_observer: 2 ("I've been building AI agents")
  - hedge_markers: 0 (missing)
  - contrast_labels: 1 (weak)
  - fragment_paragraphs: 0 (essay-like compound sentences)
  - specific_named_details: 2 (Swyx, Simon Willison, GPT-4, Fable 5)
  - **Fix needed:** Add hedge markers, convert to contrast labels, fragment the long paragraphs

---

## 15-point format audit (Opus)

**Results:**

- **Option 1:** 11/15 — ship_with_fix
  - Fails: uppercase "I" pronouns (need lowercase), opens abstract not story/person, weak actionable outcome, contains corporate framing
  - Strengths: strong hook, concrete names, rhythm variation

- **Option 2:** 13/15 — ship_with_fix  
  - Fails: uppercase "I" pronouns, lacks specific numbers
  - Strengths: personal story opener, named sources, tactical checklist, strong hook

- **Option 3:** 12/15 — ship_with_fix
  - Fails: uppercase "I" pronouns, weak actionable outcome, contains hype language ("massive takeoff")
  - Strengths: named sources, specific numbers (5.5 hours), good hook

**Recommended option:** Option 2 (highest score, most actionable)

---

## Fact check (Gemini - partial)

Response was cut off at token limit. Key concerns likely around:
- Lovable $500M ARR claim verification
- Claude Fable 5 shadowban specifics
- Benchmark claims verification
- OpenAI case study details

---

## Writing audit findings

From clean_text.py analysis:
- **Em dashes:** 7 found in posts.md (auto-fail)
- **Not X, it's Y:** 2 violations in posts ("aren't building better tools... They're building", "isn't about no-code... It's about")
- **Guru voice:** 3 total violations (brief + posts)
- **Long sentences:** 23+ violations across brief and posts
- **MBA vocabulary:** 2 violations (table stakes, enterprise customers)

---

## Verdict: REVISE

**Multiple hard failures require revision:**
1. **Deterministic violations:** Em dashes, Not X/Y inversions, guru voice, MBA vocab, long sentences
2. **Voice scores:** Options 2 and 3 below 8/10 threshold
3. **Format issues:** All options fail uppercase "I" requirement

**Priority fixes:**
1. Remove all em dashes from posts
2. Rewrite "Not X, it's Y" inversions as direct statements
3. Add hedge markers to Options 2 & 3
4. Break long sentences under 22 words
5. Convert all "I" to lowercase "i"
6. Fragment long paragraphs in Options 2 & 3

**Best foundation for revision:** Option 2 (13/15 format score, actionable content)