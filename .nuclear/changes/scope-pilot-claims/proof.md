# Quick Proof Record

**Purpose:** Capture the smallest believable evidence record for a Quick change.

**Activation threshold:** Use with `risk.md` when a change is low-stakes, easy to undo, easy to check, and does not trip Standard mode.

**Minimum useful version:** one proof command, check, or eval; the result; an evidence link; and a reviewer note.

**Overhead trap:** Do not paste long logs. Link to the evidence and quote only the result that matters.

---

## Proof summary

- Change slug: scope-pilot-claims
- Proof owner: FlyFission
- Date/time: 2026-08-01
- Risk record: `risk.md`

## Claim proven

> The public benchmark claim now states its scope (the 28 skills in the catalog when the pilot ran) and marks the pilot a historical snapshot, and the pilot's run date is verifiable from the linked folder.

Claim: The narrowed wording matches the checked-in pilot evidence and embeds no unverifiable or over-broad claim.

## Method

- Command/check/eval/review: `python -m pytest tests/test_public_docs.py -q`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `git diff --check`; confirm the pilot README carries the run date the top-level docs reference.
- Environment: Python 3.11, repo checkout.
- Inputs/fixtures: `README.md`, `SKILLS.md`, `evals/skill-benchmark-pilot/README.md` and its dated `data/` transcripts.
- Expected result: all checks pass; no benchmark claim asserts coverage beyond the tested 28 skills; the "July 2026" reference resolves to the dated pilot artifacts.
- Self-check used? yes; target: the two claim sentences and the pilot README status block.
- Reproducible by the reviewer (command/artifact), not just the author's narration? yes; rerun the commands and read the linked pilot README.

## Result

- Status: pass
- Actual result: `pytest tests/test_public_docs.py` green; `doctor` OK; `tokens` OK; `git diff --check` clean; the pilot README now records the run date (bulk 2026-07-03/04).
- Evidence link or artifact path: PR #86 CI run; `evals/skill-benchmark-pilot/README.md`.
- If failed/gap: n/a.

## Reviewer note

- Reviewer: maintainer (merge gate)
- Review note: Docs-only scoping change; narrows an existing claim and makes its date verifiable. AI-drafted; maintainer merge review is the independent check.
- Is Quick mode still valid after proof? yes.

## Required links

- Related PR/issue: #86
- Relevant changed files: `README.md`, `SKILLS.md`, `evals/skill-benchmark-pilot/README.md`
- CI run / test output / eval report / screenshot / log: PR #86 checks (validate 3.11/3.12, wheel-smoke, mcp-smoke).
- If AI-assisted: link to AI scope or independent check note: AI authored the edit and this record; maintainer merge review is the independent check.

## Exit criteria

- The evidence matches the claim in `risk.md` directly.
- The actual result is compared to the expected result you named before the proof.
- The result status is stated plainly.
- Any failure or gap has a next action or an escalation.
- The reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on software test documentation, verification, work records, and keeping the approved version under control, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
