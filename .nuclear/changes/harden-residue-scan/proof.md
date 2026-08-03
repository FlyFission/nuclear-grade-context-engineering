# Quick Proof Record

**Purpose:** Capture the smallest believable evidence record for a Quick change.

**Activation threshold:** Use with `risk.md` when a change is low-stakes, easy to undo, easy to check, and does not trip Standard mode.

**Minimum useful version:** one proof command, check, or eval; the result; an evidence link; and a reviewer note.

**Overhead trap:** Do not paste long logs. Link to the evidence and quote only the result that matters.

---

## Proof summary

- Change slug: harden-residue-scan
- Proof owner: FlyFission
- Date/time: 2026-08-01
- Risk record: `risk.md`

## Claim proven

> The residue guard now covers the trees that previously slipped past it and has teeth, and the trees are clean after scrubbing the residue it newly catches.

Claim: an internal codename or a machine home/mount/user absolute path in `.nuclear/`, `docs/`, `evals/`, `skills/`, `commands/`, `templates/`, `starter-kit/`, or `tools/` now fails CI, and no such residue remains on this tree.

## Method

- Command/check/eval/review: `python -m pytest tests/test_public_docs.py -q`; a teeth check (write a temp file containing an internal codename and a machine home-directory path into a scanned tree, confirm `test_repo_trees_contain_no_internal_residue` fails, then remove it); full `python -m pytest -q`; `python -m ruff check .`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `python tools/ng.py validate` on each scrubbed packet.
- Environment: Python 3.11, repo checkout.
- Inputs/fixtures: the scanned trees; a temporary probe file for the teeth check.
- Expected result: clean tree passes; probe file fails; all repo gates green; scrubbed packets validate.
- Self-check used? yes; target: the enumerated residue occurrences and the scan scope.
- Reproducible by the reviewer (command/artifact), not just the author's narration? yes; rerun the commands and the teeth check.

## Result

- Status: pass
- Actual result: teeth check failed as expected on the injected probe and passed after removal; `tests/test_public_docs.py` green; full suite green; ruff/doctor/tokens OK; all scrubbed packets validate; residue rescan across the scanned trees returns zero.
- Evidence link or artifact path: this PR's CI run; `tests/test_public_docs.py`.
- If failed/gap: n/a.

## Reviewer note

- Reviewer: maintainer (merge gate)
- Review note: Additive CI guard plus documentation de-identification; reversible. AI-drafted; maintainer merge review is the independent check.
- Is Quick mode still valid after proof? yes.

## Required links

- Related PR/issue: this PR
- Relevant changed files: `tests/test_public_docs.py`; the scrubbed packets and publication file listed in `risk.md`.
- CI run / test output / eval report / screenshot / log: this PR's checks (validate 3.11/3.12, wheel-smoke, mcp-smoke).
- If AI-assisted: link to AI scope or independent check note: AI authored the guard, scrub, and this record; maintainer merge review is the independent check.

## Exit criteria

- The evidence matches the claim in `risk.md` directly.
- The actual result is compared to the expected result you named before the proof.
- The result status is stated plainly.
- Any failure or gap has a next action or an escalation.
- The reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on software test documentation, verification, work records, and keeping the approved version under control, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
