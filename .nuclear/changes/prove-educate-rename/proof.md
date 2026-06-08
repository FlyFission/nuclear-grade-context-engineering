# Quick Proof

**Purpose:** Capture the smallest credible evidence record for this Quick change.

---

## Proof summary

- Change slug: prove-educate-rename
- Proof owner: FlyFission
- Date/time: 2026-06-08
- Risk record: `risk.md`

## Claim proven

Claim: Renaming the PROVE fifth beat Embed → Educate is a label-only change. It keeps the full test suite, `doctor`, `tokens`, ruff, and every in-repo packet green; preserves the canonical eleven-beat path strings the public-doc tests assert byte-for-byte; leaves no stale "Embed" beat in any spellout or diagram; and is guarded going forward by a new `test_public_docs` invariant.

## Method

- Command/check/eval/review: `python -m pytest -q`; `python -m ruff check .`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `python tools/ng.py validate .nuclear/changes/prove-educate-rename`.
- Environment: Python at `/usr/local/bin/python`, pytest 9.0.3, ruff 0.15.16; repo working tree on `claude/pensive-cori-bWkzD`, fast-forwarded onto `main` at #28 (`343e811`).
- Inputs/fixtures: the four changed docs (`README.md`, `WORKFLOWS.md`, `docs/02-operating-system/lifecycle.md`, `docs/diagrams.md`), the new test, and this packet.
- Expected result: full suite green including the new PROVE-handle invariant and the existing `test_public_docs` path assertions; ruff clean; doctor OK; token budget OK; this packet validates.
- Self-check used? yes; target = the canonical eleven-beat ASCII path strings in `README.md` and `lifecycle.md`, confirmed unchanged (only the PROVE acronym's fifth word changed).

## Result

- Status: pass
- Actual result: `python -m pytest -q` → 118 passed (was 117; +1 for the new `test_prove_handle_uses_educate_and_stays_consistent`); `ruff check .` → All checks passed; `doctor .` → OK; `tokens .` → OK: token budget; `validate .nuclear/changes/prove-educate-rename` → passed. No "Embed" beat remains in `README.md`, `WORKFLOWS.md`, `lifecycle.md`, or `docs/diagrams.md`; the historical `prove-overlay` packet is intentionally left unchanged.
- Evidence link or artifact path: the commands above; changed files listed in `risk.md` Scope.
- If failed/gap: none. The classDef token `emb` in `docs/diagrams.md` is intentionally left unrenamed — it is a shared color class for the green Baseline·Operate·Learn nodes used by both the PRO billboard (labeled "Operate") and the PROVE map (labeled "Educate"); renaming it to `edu` would mislabel the PRO usage. The visible subgraph title is now "E — EDUCATE"; GitHub renders the Mermaid client-side.

## Reviewer note

- Reviewer: FlyFission
- Review note: Label-only rename of the PROVE handle's fifth beat across the five live spellouts, plus a one-line diagram gloss clarifying that the seven control points are the everyday short form of the eleven beats and that the letter O is reused (Observe in PROVE, Operate in PRO). The eleven-beat path, its order, and the control points are unchanged. A new doc-invariant guards the handle against future mirror drift. Supersedes the `Embed` label from `prove-overlay` without rewriting that historical record.
- Is Quick mode still valid after proof? yes.

## Required links

- Related PR/issue: Rename the PROVE fifth beat Embed → Educate
- Relevant changed files: `README.md`, `WORKFLOWS.md`, `docs/02-operating-system/lifecycle.md`, `docs/diagrams.md`, `tests/test_public_docs.py`
- CI run / test output: `python -m pytest -q` (118 passed), `python -m ruff check .` (clean), `python tools/ng.py doctor .` (OK), `python tools/ng.py tokens .` (OK)
- If AI-assisted: changes prepared by an AI agent under review; scope is a documentation label rename plus one guard test.

## Exit criteria

- Evidence directly matches the claim in `risk.md`.
- Actual result is compared to the expected result named before proof.
- Result status is explicit.
- Any failure or gap has a next action or escalation.
- Reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade record inspired by public software test-documentation and verification concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
