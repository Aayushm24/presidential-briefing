# Council — 2026-06-21 (iteration 1)

## Deterministic findings (pre-flight, CONFIRMED violations)

### Format violations (golden-format.sh): 4 found
- `not_x_its_y_hits=3` (expect 0) — Lines containing AI-tell inversions
- `mba_vocab_moat_hits=1` (expect 0) — use 'the thing competitors can't copy' or name it concretely
- `mba_vocab_commoditization_hits=3` (expect 0) — use 'gets cheap' / 'everyone has it'
- `word_count=1913` (expect 2000+) — brief is at 1913 words, needs 2000+. Expand the lead section with more mechanism/specificity, not more topics.

### Plain English violations (clean_text.py):
**Brief.md violations:**
- `not_x_its_y` violations (4 instances):
  - "isn't industrial espionage. It's Tuesday"
  - "aren't the ones with access to the best models. They're the"
  - "isn't the model's capability. It's the" 
  - "aren't the ones with the best models. They're the"
- `guru_voice` violation (1 instance):
  - "founders in knowledge work verticals should stop"
- `mba_vocabulary` violations (3 instances):
  - "commoditization" (appears multiple times)
  - "commoditizes" (appears multiple times)
- `long_sentence` violations (5 instances):
  - 133w: "Key takeaways: Nobel laureate John Jumper leaving Google DeepMind..." (title + bullets combined)
  - 35w: "for builders hiring AI researchers, this creates a strategic choice: architect your..."
  - 33w: "AI talent and model IP are fundamentally non defensible John Jumper..."
  - 30w: "The protein folding breakthrough that won him the Nobel Prize in Chemistry..."
  - 24w: "Four signals this week show talent flows freely between frontier labs, model..."

**Posts.md violations:**
- `em_dash` violations (7 instances) — Em dashes found in posts
- `not_x_its_y` violation (1 instance):
  - "isn't industrial espionage. It's Tuesday"
- `long_sentence` violations (multiple instances) including metadata lines

### Pre-flight verdict: **REVISE REQUIRED**
Multiple confirmed hard-rule failures found. Total violations: 8+ across both brief and posts. These are regex-confirmed violations requiring immediate fixes before any LLM evaluation.

**CRITICAL:** The brief is 87 words short of the 2000-word floor and contains multiple banned MBA vocabulary terms and AI-tell inversions. Posts contain em dashes which are zero-tolerance violations.

---

## Fabrication Check
Checking post claims against brief...
✅ No repricing fabrication risk found.

## Voice audit (Sonnet, 15-point)
**Skipped due to pre-flight hard failures** — deterministic violations require immediate fix before LLM evaluation

## Fact check (Gemini)
**Skipped due to pre-flight hard failures** — deterministic violations require immediate fix before LLM evaluation

## Adversarial attack (Grok)
**Skipped due to pre-flight hard failures** — deterministic violations require immediate fix before LLM evaluation

## Verdict: REVISE

**Reason:** Deterministic pre-flight found 8+ confirmed violations requiring immediate fixes:

Specific revision notes:
- **Brief.md (critical):**
  - Fix 4 `[Not X, it's Y]` inversions: convert to direct declarative statements
  - Remove 3 MBA vocabulary hits: replace "commoditization/commoditizes" with "gets cheap"/"everyone has it"
  - Fix 1 guru voice violation: convert "founders should stop" to observation
  - Fix 5 long sentences (>22w): split into shorter declarative sentences
  - **Expand word count from 1913 to 2000+ words** — add more mechanism/specificity to lead section, not more topics
  
- **Posts.md (critical):**
  - Remove 7 em dashes — zero tolerance, replace with commas/periods
  - Fix 1 `[Not X, it's Y]` inversion: convert to direct statement

**Priority:** Address deterministic violations first, then re-run council review
