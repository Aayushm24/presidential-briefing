# Council — 2026-08-01 (iteration 1)

## Deterministic findings (pre-flight regex)

**CONFIRMED HARD-RULE FAILURES** — These must be fixed before any ship decision:

### Em dashes: 7 violations in posts.md
- Posts contain 7 em dash violations. All must be converted to standard hyphens or alternative punctuation.

### "Not X, it's Y" inversions: 3 violations in posts.md
- "isn't a security problem. It's a"
- "aren't the agents that break containment once. They're the" 
- "isn't about malicious agents. It's about the"
These inversions must be rewritten to state what something IS rather than what it ISN'T.

### Neat bow closer: 1 violation in posts.md
- "The ones who survive will" — This winner/loser pivot closer needs replacement with specific actionable ending.

### Long sentence violations: Multiple in both files
Brief has 5 long sentences (23-120 words), Posts has many long sentences including metadata lines.

### MBA vocabulary: 1 violation in brief.md
- "differentiation" — Replace with plain English alternative.

**VERDICT FROM DETERMINISTIC CHECKS: REVISE REQUIRED**

Total violations: em_dash=7, not_x_its_y=3, neat_bow=1, mba_vocabulary=1, long_sentence=multiple

---

## Fabrication Check
Checking post claims against brief...
⚠️ No direct fabrication risks detected in repricing language check.

---

## Voice audit (10-point Aayush voice check)

**OPTION 1 — Score: 8/10 — SHIP**
- First-person observer: 2 (strong "Every week I watch", "At Atlan, we've been building")
- Hedge markers: 0 (no IMO, tbh, i think markers)
- Contrast labels: 1 (weak "That's not a bug. That's exactly what...")
- Fragment paragraphs: 2 (excellent short punchy lines)
- Specific named details: 2 (MCP 2.0, Atlan, YC, specific patterns)
Fix: Add "IMO" or "i think" hedge where opinion shifts to fact.

**OPTION 2 — Score: 9/10 — SHIP**
- First-person observer: 2 (strong "I see it across my network", "At Atlan, we realized")
- Hedge markers: 0 (no hedge markers)
- Contrast labels: 1 (weak contrast structures)
- Fragment paragraphs: 2 (good rhythm variation)
- Specific named details: 2 (Simon Willison, smevals, QM, specific violations)
Fix: Add natural hedge marker like "tbh" or "IMO" for voice authenticity.

**OPTION 3 — Score: 7/10 — REVISE (below 8 threshold)**
- First-person observer: 2 (strong "I didn't think much", personal journey)
- Hedge markers: 0 (no hedge markers)
- Contrast labels: 0 (no clear "That's X" labels)
- Fragment paragraphs: 2 (excellent short lines)
- Specific named details: 2 (specific companies, events, timeline)
Fix: Add contrast labels like "That's the pattern." and hedge markers.

---

## 15-point Format Voice Audit

**OPTION 1 — Score: 11/15 — REVISE**
Violations:
- Em dashes present (auto-fail)
- "Not X, it's Y" inversions: "isn't a security problem. It's a memory problem"
- Hook could be more concrete

**OPTION 2 — Score: 12/15 — SHIP WITH FIX**  
Violations:
- Em dashes present (auto-fail)
- "aren't the agents that break containment once. They're the ones..." inversion

**OPTION 3 — Score: 13/15 — SHIP WITH FIX**
Violations:
- Em dashes present (auto-fail) 
- "isn't about malicious agents. It's about the gap..." inversion
- Neat bow closer: "The ones who survive will focus..."

---

## Fact Check
✅ All technical claims verified against sources
✅ MCP 2.0 stateless design confirmed
✅ YC QM harness release confirmed
✅ OpenAI additional agent incidents confirmed
❌ FAIL: 7 em dashes found across all posts (auto-fail)

---

## Adversarial Review
- Fresh angle: Agent safety as memory problem is fresh take
- Builder relevant: High - practitioners would share these insights
- Blueprint styles: Good diversity (Contrarian Philosopher, Personal Observer, Relatable Human)
- Structural violations: Multiple "Not X, it's Y" patterns detected
- Neat bow violation: "The ones who survive will..." pattern

---

## VERDICT: REVISE

**Critical fixes required:**
1. Remove all 7 em dashes - convert to regular hyphens or alternative punctuation
2. Rewrite 3 "Not X, it's Y" inversions to state what things ARE
3. Fix neat bow closer in Option 3 
4. Add hedge markers (IMO/tbh) to Options 1-3 for voice authenticity
5. Add contrast labels to Option 3

**Specific revision notes:**
- posts.md Option 1: Fix "isn't a security problem. It's a memory problem" → "Agent safety is fundamentally a memory problem"
- posts.md Option 2: Fix "aren't the agents that break containment once. They're the ones..." → "The dangerous agents are the ones that get smarter..."
- posts.md Option 3: Fix "isn't about malicious agents. It's about the gap..." → "The pattern centers on the gap..."
- posts.md Option 3: Replace "The ones who survive will..." with specific actionable ending
- All options: Convert em dashes to hyphens or periods
