# Quick Proof Template

**Purpose:** Capture the smallest believable evidence record for a Quick change.

**Activation threshold:** Use with `risk.md` when a change is low-stakes, easy to undo, easy to check, and does not trip Standard mode.

**Minimum useful version:** one proof command, check, or eval; the result; an evidence link; and a reviewer note.

**Overhead trap:** Do not paste long logs. Link to the evidence and quote only the result that matters.

---

## Proof summary

- Change slug: glean-agent-control-flow
- Proof owner: FlyFission
- Date/time: 2026-07-03
- Risk record: `risk.md`

## Claim proven

> The three doctrine refinements are additive, internally linked, source-grounded, and pass every repo gate; no external source is named in the changed files.

Claim: The two applied value-adds (decision→action hold point; pre-fetch complement) and the reinforcing skill edit keep the full test suite, doctor, token budget, and structural validation green, and introduce no reference to the external material that prompted the review.

## Method

- Command/check/eval/review: `python -m pytest tests/`; `python tools/ng.py doctor`; `python tools/ng.py tokens`; `python tools/ng.py validate .nuclear/changes/glean-agent-control-flow`; plus a diff grep for external-source names.
- Environment: repo checkout on the change's working branch; Python 3.11; pytest 9.1.1.
- Inputs/fixtures: the working-tree diff to `runtime-enforcement.md`, `context-window-discipline.md`, `double-checking-before-acting/SKILL.md`, and this packet.
- Expected result: suite passes; doctor OK; token budget OK; packet validates; grep of the changed doctrine/skill files returns no external-source name.
- Self-check used? yes; target: the three files named in `risk.md` Scope.
- Reproducible by the reviewer (command/artifact), not just the author's narration? yes; the commands above are deterministic and run in CI (`.github/workflows/ci.yml`).

## Result

- Status: pass
- Actual result: all gates green, itemized below.
  - `pytest tests/` → **186 passed, 1 skipped**.
  - `ng doctor` → **OK: Nuclear-grade doctor**.
  - `ng tokens` → **OK: token budget** (edited skill `double-checking-before-acting` within budget; no violation).
  - `ng validate .nuclear/changes/glean-agent-control-flow` → passes once `proof.md` is present.
  - Diff grep of the changed doctrine and skill files → no external-source name present (the only in-tree occurrences of the string are the git-assigned branch name, kept out of committed file text).
- Evidence link or artifact path: the changed files (`docs/02-operating-system/runtime-enforcement.md`, `docs/02-operating-system/context-window-discipline.md`, `skills/double-checking-before-acting/SKILL.md`) and this packet, on PR #58; CI on that PR ran `.github/workflows/ci.yml` jobs `validate (3.11)`, `validate (3.12)`, `mcp-smoke`, and `wheel-smoke`, all green. Commands are reproducible locally.
- If failed/gap: none.

## Reviewer note

- Reviewer: pending human review
- Review note: Confirm both additions read as native doctrine and refine rather than duplicate; confirm the "Review scope" table's already-covered mappings are accurate.
- Is Quick mode still valid after proof? yes — no Standard trigger surfaced during the change.

## Required links

- Related PR/issue: #58
- Relevant changed files: `docs/02-operating-system/runtime-enforcement.md`, `docs/02-operating-system/context-window-discipline.md`, `skills/double-checking-before-acting/SKILL.md`
- CI run / test output / eval report / screenshot / log: `python -m pytest tests/` (186 passed, 1 skipped); `.github/workflows/ci.yml`
- If AI-assisted: this change was drafted by an agent under review; the proof commands are independently reproducible by a human reviewer.

## Exit criteria

- The evidence matches the claim in `risk.md` directly.
- The actual result is compared to the expected result you named before the proof.
- The result status is stated plainly.
- Any failure or gap has a next action or an escalation.
- The reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade proof record. It documents test, structural-validation, and token evidence for an additive doctrine change grounded in public sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
