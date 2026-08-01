# Quality / Verdict / Accountability — Basis

## Purpose

State what this change must establish and the claims a reviewer must be able to check.

## Decision question

Does the repo now define all three terms its control loop depends on, and does the archetype lens change a decision rather than decorate the docs?

## Background

Three terms were doing load-bearing work with only one of them defined. `docs/glossary.md` defined "Verdict / apply-clearance" but neither **Quality** nor **Accountability**. The distinction existed in fragments — `MAXIMS.md` ("CI passing is not a release decision"; "human judgment decides engineering adequacy"), `validators.md` §1 ("a lint, not a verdict"), `agents/judge.md` (the V stage) — but nowhere as one statement, so the failure modes of collapsing the three were never enumerated.

Separately, the repo had no lens for the *posture* work is done in. `modes.md` grades consequence and `work-type-lens.md` types the change, but neither catches the most common under-grading path: exploration that becomes a promise without the diff changing.

Two existing assertions also lacked evidence. `leadership-and-high-reliability.md` said "never let AI increase code volume faster than review, testing, and ownership can absorb" with only DORA's qualitative amplifier finding behind it. `token-burn-control.md` said "the smallest honest context is also the most reliable one" with no controlled study behind the cost half.

## Requirements / claims

| ID | Claim the change must support | How a reviewer checks it |
|---|---|---|
| REQ-001 | All three terms are defined once, canonically, with the failure mode of each collapse named. | Read `docs/02-operating-system/quality-verdict-accountability.md`; confirm four collapse rows each point at where the doctrine already refuses it. |
| REQ-002 | The triad is reachable from the headline docs, not buried. | Grep the concept across `CORE.md`, `MAXIMS.md`, `docs/glossary.md`, `docs/README.md`, `validators.md`, `agents/judge.md`. |
| REQ-003 | The archetype lens changes a decision. | Confirm each archetype carries a mode floor and that the re-grade-on-archetype-shift rule is stated as a rule, not advice. An adopter must be able to act differently because of it. |
| REQ-004 | Cherny's own framing is preserved and this repo's extension is not attributed to him. | Read the archetype-lens source-lineage note: "patterns of work, not job titles" is his; the drift/mode-floor/skill mapping is this repo's. |
| REQ-005 | Every external figure is accurately stated with its boundary attached. | Check that the clean-code numbers never appear without "pass rate unchanged," and that both Sonar-derived citations disclose vendor affiliation and survey self-report. |
| REQ-006 | The three new sources are registered under the existing citation discipline. | Read the new rows in `source-map.md` Tiers 6, 9, and 11 and the crosswalk rows; confirm classification/status/confidence values and public links. |
| REQ-007 | The change breaks no existing contract test, token budget, or packet validator, and adds no 29th skill. | Run pytest, ruff, `ng doctor`, `ng tokens`, `ng validate`. Confirm `EXPECTED_SKILLS` is untouched. |

## Outcomes to protect

- The boundary discipline — no formal-assurance claim, and no statistic restated as a promise.
- The skill-count invariant — this change adds no skill, leaving the count at the 29 `main` arrived at via #81. `README.md` still claims "28 of 28 skills show a measured behavior change," so the benchmarked set already trails the shipped set by one; another unbenchmarked skill would widen that gap. Doctrine pages carry this change instead.
- The token discipline — new doctrine bodies load on demand, not in always-on context.
- The command-parity invariant — `skills/reviewing-code-quality/SKILL.md` edits stay outside its `## Prompt` block so the generated command card does not drift.

## Assumptions

- Adopters read `CORE.md` and `MAXIMS.md` as the operative surface, so the triad has to land there to change behavior.
- The archetype lens is more useful as a front-door question than as a skill; the repo's own precedent (`CORE.md`, workflow-architecture) supports doctrine pages over new skills.
- Both vendor-authored sources remain the best available public evidence on their questions despite the affiliation, provided the affiliation is disclosed.

## Required links

- Risk: `risk.md`
- Plan: `plan.md`
- Verification: `verification.md`
- Doctrine: `../../../docs/02-operating-system/quality-verdict-accountability.md`, `../../../docs/02-operating-system/archetype-lens.md`

## Exit criteria

- Each claim has a check a reviewer can run.
- The outcomes to protect are named.

## Source-lineage note

Original Nuclear-grade packet inspired by public ideas on graded rigor, independent verification, and software assurance mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
