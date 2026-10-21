# Running a Review Panel — Plan

## Purpose

Record the sequence the change actually followed, including the steps taken out of order, and state what was deliberately left out.

## Review checkpoints

- Requirements approved: partially. The owner approved the shape in discussion — doctrine-level skill, overlay rather than a review variant, no vendor runner — and approved proceeding. The requirement rows in `basis.md` were written afterward from the finished diff, so they were not an approved gate the build had to pass.
- Design approved: yes. Three scoping decisions were settled before drafting: overlay rather than editing `reviewing-code-quality`, gated to Nuclear / Tier 0 and trust-bearing calls, and no external dependency.
- Tasks approved: no separate approval. The sequence below was executed as one pass and is recorded here rather than pre-registered.

## Sequence

| # | Task | Files | Status |
|---|---|---|---|
| 1 | Establish the gap: confirm the panel was prescribed with no method | `evaluation-integrity.md`, `independence-architecture.md` | done |
| 2 | Surface the prior on-record refusal to add a skill and its decisive objection | `../quality-verdict-accountability/plan.md` | done |
| 3 | Draft the skill: decision contract, triggers, eight Process steps, outputs, escalation, rationalizations, red flags, prompt | `skills/running-a-review-panel/SKILL.md` | done |
| 4 | Register in the manifest and generate the command card | `nuclear-grade.yaml`, `commands/ng-panel.md` | done |
| 5 | Update the catalog, cluster placement, and every stated skill count | `SKILLS.md`, `CORE.md`, `COMMANDS.md`, `INSTALL.md`, `cli-reference.md`, `skill-authoring-contract.md` | done |
| 6 | Cross-link the doctrine that prescribed the panel to the procedure | `evaluation-integrity.md`, `independence-architecture.md` | done |
| 7 | Add eval coverage and prompt-bank entries | `skill-routing-cases.jsonl`, `skill-output-cases.jsonl`, `skill-evaluation.md` | done |
| 8 | Record the skill in the comparison table using the post-trial convention | `results-summary.md` | done |
| 9 | Extend the contract tests to the new skill, command, and rolled-up count | `test_skill_contracts.py`, `test_command_contracts.py`, `test_ng_cli.py` | done |
| 10 | Cut the skill body and the generated card to fit the existing token budget rather than raising the ceiling | `SKILL.md`, `ng-panel.md` | done |
| 11 | Regenerate cards and rebuild the golden prompt fixture | `tests/fixtures/command_prompts.json` | done |
| 12 | Write the CHANGELOG entry naming the efficacy gap as a risk | `CHANGELOG.md` | done |
| 13 | Merge `main` after discovering the branch was two commits behind a release and its green CI was stale | `CHANGELOG.md` conflict resolved; commit `a33f858` | done |
| 14 | Write this packet, out of order, and record the deviation | `.nuclear/changes/running-a-review-panel/` | done |
| 15 | Act on two upheld review findings: gate the panel's matrix row on its trigger, and reword the gate exclusion so the panel feeds a required human gate rather than being suppressed by one | `CORE.md`, `SKILL.md`, regenerated `commands/ng-panel.md` | done |
| 16 | Act on the second review round: give the panel a matrix route keyed to its own verdict trigger rather than nesting it under agent authority, and hold Nuclear / Tier 0 to the independence floor the doctrine already states | `CORE.md`, `SKILL.md`, regenerated `commands/ng-panel.md` | done |
| 17 | Act on the third review round: carry the Tier 0 independence floor into the `## Prompt` block an agent may receive alone, and widen the matrix route to the correlated-reviewer case the routing eval already treats as a trigger | `SKILL.md`, `CORE.md`, regenerated `commands/ng-panel.md`, `tests/fixtures/command_prompts.json` | done |
| 18 | Verify the fourth review round, draft the fix, measure that it does not fit, and hold it for the owner rather than deleting substance or raising a controlled limit | `ship.md`, `verification.md` V-22 | done |
| 19 | Owner chose to reseed the ceilings: raise `skill_body_max` to 3900 and `command_max` to 1700 with the basis recorded beside the values, then apply the held fix and widen the catalog rows | `nuclear-grade.yaml`, `SKILL.md`, `SKILLS.md`, `COMMANDS.md`, regenerated `commands/ng-panel.md` | done |

## Out-of-order steps, and what that costs

Tasks 1 through 12 ran before any packet existed. Task 14 reconstructs the record afterward.

The token-budget step (task 10) is the one worth naming, because it is where the pressure landed. The first draft failed the gate at 4176 tokens against a `skill_body_max` of 3600, and the generated card at 1724 against 1600. The budget comment in `nuclear-grade.yaml` says the limits are "seeded above the measured maxima with headroom, so the gate blocks regression, not the accepted corpus" — raising a ceiling to admit the file that broke it would have converted a regression gate into a formality. The skill was cut instead: Overview sentences, two Common Rationalizations, one Red Flag, one Escalation bullet, and tightened Decision-contract, Verification, and source-lineage wording. Reshuffling or merging Process steps saved almost nothing; only deleting content moved the number.

## Deliberately not done

- **No runner script, provider config, or `.council/`-style runtime directory.** The original draft this change descends from carried a Python runner and a four-provider panel config. Both were dropped from `skills/`: the catalog is host-neutral, a vendor CLI list dates immediately, and a runtime directory holding raw reviewer output is a data-handling surface with its own retention and redaction questions. The procedure works with subagents, a second model family, a different mechanism, or a human colleague. If the orchestration is wanted later, its home is `INTEGRATIONS.md` with its own packet.
- **No edit to `skills/reviewing-code-quality/`.** Its decision contract decides one thing and is currently clean. The panel is an overlay on any verdict-bearing skill; folding it in would have made that contract decide two things at once.
- **No new external source registered.** Every source the skill cites — the diversity taxonomy in NUREG/CR-6303, independence axes in NASA SWE-141, tool qualification proportional to reliance in SWE-136, independent verification in DOE-HDBK-1028-2009, and the LLM-as-judge self-preference literature at arXiv:2502.01534 — was already in `source-map.md`. Verified: the skill commit does not touch that file.
- **No token-budget change.** See task 10.
- **No efficacy trial.** Running the July 2026 pilot harness against this skill was considered and not done: the pilot is reported as a historical snapshot of the catalog as it stood, and bolting one late entry onto it would either misrepresent the snapshot or require a fresh run with its own design, sample, and pre-registration. That is its own change with its own packet. The consequence is that this skill ships unmeasured, which is recorded as a named risk rather than deferred quietly.
- **No `decision-authority.md`.** Strict-authority validation is not claimed for this packet; no decision right is transferred, and the merge call stays with a human reviewer by default.

## Required links

- Risk: `risk.md`
- Basis: `basis.md`
- Trace: `trace.md`
- Verification: `verification.md`
- Ship: `ship.md`

## Exit criteria

- Every task is done or explicitly deferred with a reason.
- The out-of-order steps are named, not implied by file dates.
- The scope boundary — what was dropped from the originating draft and why — is stated.

## Source-lineage note

Original Nuclear-grade packet inspired by public planning, scope-control, and configuration-management concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
