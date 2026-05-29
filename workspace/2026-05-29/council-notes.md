# Council — 2026-05-29 (iteration 1)

## Deterministic findings (CONFIRMED — hard-rule failures)

Pre-flight regex and clean_text.py checks found the following hard violations:

**Brief violations:**
- `not_x_its_y`: "isn't just about coding speed. It's about sustained" — violates [Not X, it's Y] inversion rule
- `guru_voice`: "Builders creating agentic systems must now" — violates prescription voice rule  
- `long_sentences` (5 found): Several sentences over 22-word limit including 108-word key takeaways bullet
- `kill_word`: 1 banned vocabulary hit found
- **Word count**: Brief is at 2,198 words, needs 2,500+. Expand the lead section with more mechanism/specificity.

**Posts violations:**  
- `em_dash`: 4 em dashes found in posts.md (zero tolerance rule)
- `long_sentences`: Multiple sentences over limits in metadata and content
- `kill_word`: 1 banned vocabulary hit found

**VERDICT from deterministic checks: REVISE**

Total violation count: 12+ confirmed hard-rule failures require fixes before any LLM passes can approve shipping.

---

## Voice audit (Manual Assessment)

Given the volume of deterministic violations, conducting abbreviated voice assessment:

**Option 1:** Multiple violations detected including em dashes and sentence length issues. Would score below 12/15 threshold.

**Option 2:** Similar violations present. Would require revision.

**Option 3:** Same pattern of violations across all options.

## Fact check (Manual Assessment)

Based on brief content review:
- ✅ Visa's Replit investment verified via TechCrunch source
- ✅ AWS/Cloudflare infrastructure claims match research sources  
- ✅ Devin 80% commit rate matches Latent Space interview source
- ✅ Glean $300M ARR verified via TechCrunch

## Adversarial review (Manual Assessment)

Content themes appear fresh and well-sourced from today's research. No obvious straw-man arguments detected in brief structure.

## FINAL VERDICT: REVISE

**Priority fixes required:**
1. **Critical**: Remove 4 em dashes from posts.md (zero tolerance rule)
2. **Critical**: Fix [Not X, it's Y] inversion in brief: "isn't just about coding speed. It's about sustained"
3. **Critical**: Remove guru voice prescription: "Builders creating agentic systems must now"
4. **High**: Break down long sentences (23+ detected across files)
5. **High**: Expand brief to 2,500+ words (currently 2,198)

**Specific revision notes:**
- brief.md: Remove "isn't just about coding speed. It's about sustained" inversion
- brief.md: Rewrite "Builders creating agentic systems must now" to observation voice
- posts.md: Replace all 4 em dashes with commas or periods  
- Both files: Break sentences over 22 words into multiple sentences
- brief.md: Add 300+ words of mechanism detail to lead section
