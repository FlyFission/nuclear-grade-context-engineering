# Skill Audit Amendments and Recommendations — 2026-07-04

## Executive conclusion

The original `99.6/100` result was too easy to misread. It is now explicitly labeled as a **structural completeness score**, not an efficacy score. It means the 28 skills are well-formed enough to test; it does **not** mean they outperform prompt-only.

After re-reviewing PR #62 and the local repo, the most defensible interpretation is:

- Static readiness: **28/28 skills are eligible for live A/B**.
- Existing live evidence: **internal and promising, but not independent**.
- Weakest first retest targets: `briefing-an-agent`, `proving-claims`, and `creating-change-records`.
- Highest systemic risk: overlapping skill boundaries and author-derived prompts/criteria.

## What changed in this branch

### 1. Static audit reframed

Added `tools/ng_skill_audit.py` and generated:

- `evals/skill-static-audit/2026-07-04/skill-audit.jsonl`
- `evals/skill-static-audit/2026-07-04/skill-audit.md`
- `evals/skill-static-audit/2026-07-04/pilot-findings.json`

The report now states that the score is structural completeness only and that a 100 can still tie or lose to prompt-only.

### 2. Deterministic anti-vibe test scaffolding added

Added deterministic route/output scorers and tests:

- `tools/ng_skill_route_score.py`
- `tools/ng_skill_output_score.py`
- `evals/skill-routing-cases.jsonl`
- `evals/skill-output-cases.jsonl`
- `tests/test_skill_route_score.py`
- `tests/test_skill_output_score.py`
- `tests/test_skill_efficacy_coverage.py`

These do not replace live A/B. They make future live A/B runs easier to score and regress without relying only on reviewer preference.

### 3. Prompt-bank and worked-example tests hardened

Added:

- `tests/test_skill_prompt_bank_quality.py`
- `tests/test_efficacy_signal_mutations.py`

These catch weak prompt-bank quality, tautological prompts, duplicate/conflicting labels, and signal checks that would still pass after a required phrase is removed.

### 4. Independent benchmark protocol added

Added:

- `docs/05-reference/independent-skill-benchmark-protocol.md`

It defines fair baselines, required scenario mix, grading rules, routing benchmarks, acceptance guidance, and overlap clusters.

### 5. Clear skill amendments made

Amended three highest-priority skills from PR #62 tie/loss findings:

- `skills/briefing-an-agent/SKILL.md`
  - narrowed to context packaging before work/review;
  - removed ownership of durable turnover records;
  - routes actual responsibility transfer to `handing-off-work`.
- `skills/proving-claims/SKILL.md`
  - narrowed to claim-to-evidence trace construction;
  - routes ship/defer/block to `checking-release-readiness`;
  - routes public assurance wording to `checking-legal-and-safety-wording`;
  - routes citation lineage to `checking-source-claims`.
- `skills/creating-change-records/SKILL.md`
  - narrowed to packet shell/files/links/status labels/validator receipts;
  - routes mode choice to `rating-change-risk`;
  - routes evidence adequacy to `proving-claims`;
  - routes release decision to `checking-release-readiness`.

Generated command cards were refreshed with `python tools/ng.py gen-commands`.

## Findings from PR #62 review

### Round 1

- 13 wins
- 13 ties
- 1 loss
- Separate `reviewing-code-quality` pilot: gain on 1/3 planted-defect tasks, tie on 2/3

### Gate 1

- 14 hard-case retests
- 11 became wins
- `briefing-an-agent` stayed tied
- `proving-claims` stayed tied
- `creating-change-records` improved from loss to tie, but not to a clean win

### Methodology limitations

PR #62 is useful but not enough for strong claims because:

- scenarios and pass criteria were authored from the skills themselves;
- sample sizes were small (`n=3` and `n=5`);
- grading used one model-grader path;
- no equal-token generic checklist baseline was run;
- no irrelevant-skill control was run;
- no skill-description-only ablation was run;
- routing confusion was barely tested;
- some wins may be phrase-bar wins rather than substantive decision changes.

## Prioritized retest queue

### P0 — Retest after amendments

1. `briefing-an-agent` vs `handing-off-work`
2. `proving-claims` vs `checking-release-readiness`
3. `proving-claims` vs `checking-source-claims`
4. `proving-claims` vs `checking-legal-and-safety-wording`
5. `creating-change-records` vs `rating-change-risk` / `proving-claims` / `checking-release-readiness`

### P1 — Retest for systemic routing risk

6. `using-nuclear-grade` vs `rating-change-risk` vs `questioning-attitude`
7. `choosing-what-to-control` vs `checking-what-a-change-affects` vs `recording-a-known-good-version`
8. `reporting-shared-defects` vs `tracking-deficiencies`
9. `deciding-who-decides` vs `declaring-intent` vs `double-checking-before-acting`

### P2 — Cost/latency compression candidates

10. `organizing-project-folders` — largest body token cost
11. `breaking-down-the-work` — high body token cost
12. `staying-on-mission` / `closing-stale-packets` / `using-nuclear-grade` — high cost, broad trigger surface

## Recommended next live A/B plan

Run a focused independent Gate 2 before testing all 28 exhaustively:

1. Create independent scenarios for the P0 cluster without showing authors the skill bodies.
2. Use at least these variants: naive prompt-only, best-practice prompt-only, equal-token generic checklist, irrelevant skill, skill-description-only, full skill, compressed skill.
3. Run 8-12 scenarios per P0 skill/cluster, 5 trials per variant.
4. Score route selection separately from answer quality.
5. Use deterministic route/output scorers for required/forbidden elements.
6. Blind labels for subjective graders and include calibration answers.
7. Report cost per substantive improvement, not just yes/no win counts.

After P0, expand to all 28 with the same framework.

## Verification performed

- `pytest tests/test_efficacy_signal_mutations.py tests/test_skill_prompt_bank_quality.py -q` — passed
- `pytest tests/test_skill_route_score.py tests/test_skill_output_score.py -q` — passed after adding scorer scripts/manifests
- `pytest tests/test_skill_contracts.py tests/test_efficacy_signal_mutations.py tests/test_skill_prompt_bank_quality.py tests/test_skill_route_score.py tests/test_skill_output_score.py tests/test_skill_efficacy_coverage.py -q` — passed after the all-28 routing/output manifests were expanded.
- `python tools/ng_skill_route_score.py --cases evals/skill-routing-cases.jsonl --skills-dir skills` — loaded 152 routing cases and validated manifest shape.
- Output manifest validation — loaded 28 output cases and validated all skill references.
- `python tools/ng_skill_audit.py --root . --jsonl evals/skill-static-audit/2026-07-04/skill-audit.jsonl --markdown evals/skill-static-audit/2026-07-04/skill-audit.md` — passed.
- `python tools/ng.py eval .` — `15/15` worked-example decision signals present.
- `python tools/ng.py tokens .` — OK token budget.
- `python tools/ng.py gen-commands` — regenerated command cards from amended skills.
- `pytest -q` — passed after all-28 deterministic coverage was made complete.

## Remaining known limits

- The deterministic route/output cases cover all 28 skills, but they are signal checks rather than live efficacy proof.
- No new live LLM A/B run was executed in this branch; this branch prepares the measurement harness and patches clear boundary defects first.
- PR #62 evidence should still be described as internal pilot evidence, not independent validation.
- Live Gate 2 must still compare with-skill runs against naive prompt-only, best-practice prompt-only, equal-token checklist, skill-description-only, compressed-skill, and irrelevant-skill controls.
