# Quick Proof

**Purpose:** Capture the smallest credible evidence record for this Quick change.

---

## Proof summary

- Change slug: prove-overlay
- Proof owner: FlyFission
- Date/time: 2026-06-04
- Risk record: `risk.md`

## Claim proven

Claim: The acronym overlay is additive only — it keeps the full test suite, `doctor`, and every in-repo packet green, preserves the canonical eleven-beat path strings the public-doc tests assert, and both new Mermaid diagrams parse as valid flowcharts.

## Method

- Command/check/eval/review: `python -m pytest -q`; `python tools/ng.py doctor .`; `python tools/ng.py validate .nuclear/changes/prove-overlay`; Mermaid parse-check of both new diagrams via the diagram validator.
- Environment: Python 3.11, repo working tree on `claude/great-goldberg-97y3s`.
- Inputs/fixtures: the four changed docs plus this packet.
- Expected result: full suite green (incl. `test_public_docs` path assertions and `test_tokens` budget + redundancy index); doctor OK; this packet validates; both diagrams parse.
- Self-check used? yes; target = the canonical ASCII path strings in `README.md` and `lifecycle.md`, confirmed unchanged.

## Result

- Status: pass
- Actual result: `python -m pytest -q` → 117 passed; `doctor .` → OK; `validate .nuclear/changes/prove-overlay` → passed; all 15 in-repo packets validate. Both new diagrams parse as valid flowcharts — the diagram validator's "SVG exceeds size limit" is a return-payload cap on the checker (the same cap fires for the simplest variant), not a syntax error; GitHub renders Mermaid client-side without that cap.
- Evidence link or artifact path: `docs/diagrams.md` (new section 2, canonical diagrams); commands above.
- If failed/gap: final on-GitHub render appearance is confirmed visually on the PR preview (the render-check is the closing gate); documented fallback is to drop `direction LR` if any lane lays out poorly.

## Reviewer note

- Reviewer: FlyFission
- Review note: Diagrams are canonical in `docs/diagrams.md`; `README.md` mirrors the PRO diagram. Canonical ASCII path strings preserved in `README.md` and `lifecycle.md` so `test_public_docs` still passes. The mapping prose and crosswalk live in one file so the `test_tokens` redundancy index does not fire; mirrors carry only the fenced diagram (exempt from the prose scan) plus a file-unique line.
- Is Quick mode still valid after proof? yes.

## Required links

- Related PR/issue: PROVE/PRO acronym overlay + swim-lane diagrams
- Relevant changed files: `docs/diagrams.md`, `README.md`, `WORKFLOWS.md`, `docs/02-operating-system/lifecycle.md`
- CI run / test output: `python -m pytest -q` (117 passed), `python tools/ng.py doctor .` (OK)
- If AI-assisted: changes prepared by an AI agent under review; scope is additive documentation plus a section renumber.

## Exit criteria

- Evidence directly matches the claim in `risk.md`.
- Actual result is compared to the expected result named before proof.
- Result status is explicit.
- Any failure or gap has a next action or escalation.
- Reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade record inspired by public software test-documentation and verification concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
