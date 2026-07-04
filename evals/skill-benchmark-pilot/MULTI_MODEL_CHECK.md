# Multi-Model Check — Small, Cheap, Honestly Scoped

Addresses the self-audit's "single model only" gap. Not a full fix — a
bounded first look, scoped down from the original amendment plan after
adversarial review found the original 8-skill/2-model estimate understated
cost by 1.5–3x (Opus pricing) and didn't flag that 8 of 28 skills is still
partial coverage, not a resolved gap.

## What was actually run

4 skills, chosen to span result categories, not randomly: one clean round-1
WINS (`learning-from-experience`), one thin-margin round-1 WINS
(`staying-on-mission`), one closed-via-recheck TIE (`proving-claims`), and the
newly-closed `creating-change-records` (using the corrected, scope-limited
criterion from the PR #63 reconciliation, not the original compound one).
Existing scenarios reused — no new scenario-design cost. Subject model:
`claude-haiku-4-5` (materially weaker than the `claude-sonnet-5` used
everywhere else in this project). Grader: `claude-sonnet-5`, kept deliberately
separate from the subject model — using the same model as both actor and
judge is exactly the self-check pattern `proving-claims` itself flags as a
red flag. n=3 per condition. Total cost: **$0.32** for 24 runs.

**This is 4 of 28 skills on 1 additional model. It does not license any claim
about the other 24 skills, and it does not reach GPT/Gemini/other providers —
there are no credentials for non-Anthropic models in this environment. Read
this as a first data point, not a multi-model validation.**

## Results

| Skill | Sonnet result (original) | Haiku result (this check) | Read |
|---|---|---|---|
| `learning-from-experience` | 3/3 vs 0/3(+2p) | 2/3 vs 0/3(+2p) | Replicates — same direction, similar magnitude |
| `staying-on-mission` | 3/3 vs 2/3(+1p) | 3/3 vs 2/3(+0p) | Replicates closely |
| `proving-claims` (decision correctness) | 5/5 vs 5/5 (tie) | 3/3 vs 3/3 (tie) | Replicates — the tie itself replicates, reinforcing that even a weaker model reaches the right decision by default; consistent with the earlier finding that this skill's real value is structural, not decision-correctness |
| `creating-change-records` (corrected file-naming criterion) | 4/5 vs 0/5 | **0/3 vs 0/3** | **Does not replicate** |

## The one result that didn't replicate, and what that actually means

`creating-change-records` was a clean win on Sonnet under the corrected
criterion (does the response name 4+ of the 6 required packet files). On
Haiku, **neither condition** named the files, with or without the skill
loaded. Reading the actual transcripts (not just the grader's count) before
drawing a conclusion: Haiku's `with_skill` response is substantively
reasonable — it correctly identifies the risk, correctly rejects "ship now,
document later," and recommends creating a change record — but it asks
clarifying questions and reasons qualitatively rather than concretely listing
the six required filenames the way every Sonnet `with_skill` trial did. The
`without_skill` Haiku response is similar in overall quality. This looks like
a real model-capability difference in following a skill's specific structural
convention under instruction, not a grading artifact — both transcripts are
in `data/multi-model-check/runs/` for independent reading.

**What this does NOT mean:** it does not mean `creating-change-records` is
broken, and it does not retract the Sonnet finding — that finding is specific
to Sonnet and stands. **What it does mean:** the claim "this skill adds value"
is now known to be model-dependent for at least this one skill on this one
scenario, and that dependency should be stated wherever this skill's result
is cited, not smoothed over. See `PLAN_STATUS.md` for the decision rule this
triggers.
