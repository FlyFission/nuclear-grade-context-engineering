# Amendment Plan: Status After Adversarial Review and Execution

Original plan drafted to close the 5 gaps in `README.md`'s self-audit table,
then adversarially critiqued by a fresh reviewer with no investment in it
looking good before any of it was executed. The critique found real,
checkable problems in 3 of the 5 items — not stylistic notes. This document
is the plan as it actually stands after both the critique and execution,
including a mid-execution discovery (PR #63) that changed the priority order.

## 0. PR #63 reconciliation (discovered mid-plan, became priority 0)

A parallel, independent effort (PR #63, branch `alfred/skill-audit-efficacy-20260704`)
touched the same three skill files this project's own work had already
diagnosed or amended: `briefing-an-agent`, `proving-claims`,
`creating-change-records`. Handled before any further new spend:

- **`briefing-an-agent`**: PR #63 independently reached the same diagnosis
  (overlap with `handing-off-work`) with a different specific fix (link-based
  composition vs. this project's hard separation). Flagged the conflict and
  the validation-status asymmetry as a PR comment on #63 — this project's
  version has a live regression test behind it (5/5 vs 0/5 on the skill's true
  niche); #63's version is explicitly unvalidated pending live A/B. Recommended
  #63's maintainer treat the validated version as the tiebreaker unless the
  link-based approach gets the same kind of before/after check. Not resolved
  unilaterally — this is the repo maintainer's call, not mine to force by
  editing a branch I don't own.
- **`proving-claims`**: PR #63's boundary-clarifying edit (excludes
  release/legal/source-lineage territory) is compatible with this project's
  finding (no content amendment needed; the skill already adds real value on
  a structural dimension). No conflict.
- **`creating-change-records`**: PR #63's scope clarification (this skill
  owns packet shell/files/links, not mode-choice or evidence-adequacy
  judgment) directly explained why this project's original Gate 1 criterion
  never produced a clean pass — the criterion was implicitly asking the skill
  to do two other skills' jobs. Re-graded the existing transcripts against a
  criterion corrected for that scope: **4/5 vs 0/5, a clean win, no content
  change needed.** Reported back on the PR #63 thread. This resolves what was
  previously the one genuinely unresolved skill in the whole 28.

## 1. Statistical significance — done, with a result stronger than expected

See `STATISTICAL_ANALYSIS.md` in full. Headline: **0 of 47 tests survive
Benjamini-Hochberg correction at α=0.05** (updated from an original 44 after
a later Codex review caught 3 closeout rechecks missing from the family),
including the single strongest raw results in the project (`handing-off-work`,
`briefing-an-agent`'s and `proving-claims`'s closeout rechecks, each raw
p=0.0079, BH-adjusted p=0.124). The critique predicted this before the number
existed and warned specifically against letting a p-value column look more
rigorous than the evidence supports — the table in that document states the
non-significance in the table itself, not just in surrounding prose, per that
warning.

## 2. Pre-calibration — resolved for free, exactly as the critique predicted

The critique found this item's proposed new trials were largely redundant
with data already in `REPORT.md`. Correct: **17 of 27 round-1 scenarios
(63%) had a `without_skill` baseline success rate ≥50%** — the threshold this
project's own plan proposed borrowing from SkillsBench — computable from
existing data at zero cost. Full breakdown in `STATISTICAL_ANALYSIS.md`. No
new trials were run for this item; the original plan's "~$0.15" cost estimate
for retroactive baseline-testing is retracted as unnecessary, not merely
recosted.

## 3. Oracle-based verification POC — re-scoped, not executed

The critique read the actual `reviewing-code-quality` transcripts and found
the plan's core premise wrong: responses are free-form prose recommendations
("delete the wrapper function," "inline the three branches"), not literal
diffs. Extracting a mechanically-appliable patch from that prose requires
either a new LLM synthesis call per transcript (real new cost, and it
reintroduces the LLM-mediated judgment an oracle is supposed to eliminate) or
manual per-transcript patch authorship (real uncounted labor). **This item is
not executed in this pass.** It remains a legitimate, valuable idea, correctly
scoped now instead of under-costed: building it for real would mean writing
an actual patch-synthesis-and-test-execution harness, which is a distinct
engineering task, not a "free reuse" of existing data. Recommend treating it
as a separate, explicitly-scoped follow-up, not folded into a "quick fixes"
pass.

## 4. Multi-model sample — executed at reduced, honestly-costed scope

See `MULTI_MODEL_CHECK.md` in full. Reduced from the original plan's 8
skills × 2 models (Haiku + Opus, ~$7 originally estimated, corrected by the
critique to likely $10-20+ once Opus's real pricing is accounted for) to 4
skills × 1 model (Haiku only, $0.32 actual cost). Opus is deferred, not
abandoned — explicitly flagged as unexecuted rather than silently dropped.
3 of 4 sampled skills replicated on Haiku; 1 (`creating-change-records`)
did not, and the divergence is documented with the actual transcripts, not
smoothed into an aggregate percentage.

## 5. Independent-replication mitigations — not executed this pass

Lower priority than items 0-4 given the PR #63 discovery and the volume of
free/cheap findings items 1-2 produced. Not attempted in this pass; remains
open, stated as "Not yet" in `README.md`'s self-audit exactly as before —
per the critique's specific instruction, that label should not be softened
by partial mitigations that were never actually executed.

## Disconfirmation protocol (the gap the critique found nothing else covered)

The critique's sharpest finding: no item in the original plan specified what
would happen if a fix *contradicted* an existing claim rather than confirming
it — meaning the plan, as drafted, could only ever produce results that
looked like validation. One did contradict: `creating-change-records` on
Haiku. The rule applied here, stated in advance for future cases too:

1. **A result specific to one model is reported as specific to that model,
   not generalized.** The Sonnet finding for `creating-change-records` is not
   retracted — it's true for Sonnet, on the scenario tested. The Haiku
   divergence is reported alongside it, not averaged into it or hidden behind
   an aggregate.
2. **A skill with a model-dependent result gets a stated caveat everywhere
   its status is cited**, not just in the document that discovered the
   divergence. (Action taken: this document and `MULTI_MODEL_CHECK.md`; the
   master status table in `README.md` should be updated to flag this the
   next time it's revised.)
3. **A divergence triggers reading the actual transcripts before drawing a
   conclusion, not just reporting the count.** Done here — the Haiku
   transcripts were read directly before concluding this was a real
   capability difference and not a grading artifact.
4. **No result pattern from this plan changes any of this project's earlier
   WINS/TIE/LOSES verdicts for Sonnet.** Those verdicts were about Sonnet's
   behavior specifically and remain what they were. What changes is the
   confidence with which any of them can be extended to "this skill works,"
   full stop, independent of model — that confidence was already stated as
   low (single model tested) before this plan started, and item 4's result is
   a first concrete instance of why that caveat matters, not a new problem.

## What's still open after this pass

- Oracle-based verification: correctly scoped, not built.
- Independent/third-party replication: unchanged, "Not yet."
- Multi-model coverage: 4 of 28 skills on 1 additional model, not 28 skills,
  not cross-provider.
- The `briefing-an-agent` conflict with PR #63: flagged, not resolved — a
  maintainer decision, not something to resolve unilaterally.
