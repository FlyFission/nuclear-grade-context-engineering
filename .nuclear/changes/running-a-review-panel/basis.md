# Running a Review Panel — Basis

## Purpose

State the decision question, the claims this change has to support, and the checks a reviewer can run against each one.

## Decision question

Does the repo now supply a method for the panel it already prescribed, and does that method change a panel decision rather than restate the doctrine it came from?

## Background

Two doctrine pages already required a panel and already said what a bad one looks like. `docs/02-operating-system/evaluation-integrity.md` §4 prescribed a panel plus a meta-judge for high-consequence verdicts and named the failure directly: "a panel that shares one biased brief is not three independent views, it is one view voiced three times." `docs/02-operating-system/independence-architecture.md` required that a check name the diversity axis it varies, carrying the three independence axes drawn from NASA SWE-141.

Neither page said how to build one. The result was a prescription an adopter could agree with and still not execute: no instruction to freeze the evidence, no instruction to run the first pass independently, no place to record that two of five seats dropped, and no rule against acting on a finding nobody checked. The repo's own `actor-evidence-independence.md` describes the coupling this creates — the same actor selecting evidence, reviewing it, and framing the decision — and the panel was offered as the remedy without a procedure attached.

The gap is the kind this repo treats as a defect rather than a documentation preference: doctrine that cannot be executed is a claim about rigor, not rigor.

## Requirements / claims

| ID | Claim the change must support | How a reviewer checks it |
|---|---|---|
| REQ-001 | The skill is a procedure, not a restatement: each Process step yields an artifact, a count, or a decision. | Read the eight Process steps in `skills/running-a-review-panel/SKILL.md`; confirm each produces something recorded in `## Outputs`. |
| REQ-002 | Each seat declares the diversity axis it varies, and distinct-axis and distinct-family counts are recorded separately from seat count. | Confirm Process step 3 requires the declaration, `## Outputs` requires both counts stated separately, and `## Verification` folds an undeclarable seat into the seat it duplicates before counting. |
| REQ-003 | Panel health is reported beside the result, and a degraded panel is labeled degraded rather than reported as full-strength. | Confirm Process step 6 names dropped, timed-out, invalid, and truncated seats, calls a five-axis plan delivering two a "degraded panel," and that `## Escalation` escalates rather than averages. |
| REQ-004 | No finding becomes actionable until it is verified against live source in the host session. | Confirm Process step 8 requires reading the code path, running the test, or inspecting the authoritative source, and marks each finding `verified`, `rejected`, or `unresolved`; confirm the decision contract's failure class includes acting on an unverified finding. |
| REQ-005 | The cost is gated to consequence, so the skill refuses its own use on reversible low-stakes work. | Read `## When Not to Use`: a panel on a Quick change is ceremony; two seats on one model, brief, and context are one seat; a deterministic check beats four opinions. Confirm the frontmatter description carries the negative clause. |
| REQ-006 | It is an overlay, and `reviewing-code-quality`'s single-reviewer decision contract is unchanged. | `git diff` shows no edit to `skills/reviewing-code-quality/`; the new skill's `## When to Use` triggers on a verdict already resting on one reviewer. |
| REQ-007 | No efficacy claim is made for this skill, and the benchmark gap is disclosed rather than absorbed. | Confirm the comparison table records "formal trial records pending" rather than a trial result, that the CHANGELOG entry names the 28-versus-30 gap, and that `ship.md` carries it as the first named risk. |
| REQ-008 | The catalog wiring is complete and internally consistent across every surface that counts or lists skills. | Run pytest (contract, parity, catalog, and prompt-bank tests), then `ng doctor` and `ng tokens`; confirm `ls -d skills/*/` equals every stated count. |
| REQ-009 | The skill adds no dependency, vendor CLI, runner script, runtime directory, or new external source. | `git diff --name-only` on the skill commit shows no `pyproject.toml`, no new top-level directory, and no change to `source-map.md`. |
| REQ-010 | The boundary wording claims no assurance, certification, or regulatory adequacy, and claims no independence beyond the axes actually varied. | Read the `## Verification` boundary paragraph and the source-lineage note in the skill. |

## Outcomes to protect

- **The boundary discipline.** The skill is about independence, which is exactly the vocabulary an adopter could mistake for an assurance claim. Its `## Verification` section has to say what passing does not establish, including that it does not establish independence beyond the axes actually varied.
- **The honesty of the efficacy surface.** The pilot measured 28 skills and the repo now ships 30. The protection is disclosure, not silence: no row in the comparison table may read as measured, and the gap is named in the CHANGELOG and in `ship.md`.
- **The single-reviewer contract of `reviewing-code-quality`.** It is currently clean. Adding panel machinery there would blur a contract that decides one thing; the overlay keeps that decision intact.
- **The token discipline.** A 30th skill loads by description. The body has to fit the existing budget rather than move the ceiling to admit itself.
- **The command-parity invariant.** The generated `ng-panel` card and the `GOLDEN` prompt fixture have to agree with the skill byte-for-byte.

## Assumptions

- Adopters treat the `SKILL.md` catalog as the executable surface and the doctrine pages as the explanation, so a procedure belongs in a skill even though the prescription lives in doctrine.
- A reviewer can judge whether the axis-declaration step is load-bearing by reading it; no field data exists either way at time of writing.
- #86's scoping of the pilot claim to the tested catalog is the material change that makes a 30th skill admissible. If a reviewer disagrees that scoping is sufficient, the right outcome is to block this change, not to weaken the disclosure.

## Required links

- Risk: `risk.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Verification: `verification.md`
- Skill: `../../../skills/running-a-review-panel/SKILL.md`
- Doctrine: `../../../docs/02-operating-system/evaluation-integrity.md`, `../../../docs/02-operating-system/independence-architecture.md`

## Exit criteria

- Each claim has a check a reviewer can run without re-deriving the change.
- The outcomes to protect are named.
- The assumption that carries the admissibility argument is stated as an assumption.

## Source-lineage note

Original Nuclear-grade packet inspired by public ideas on graded rigor, independent verification, and diversity in redundant review mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
