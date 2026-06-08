# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** A label-only rename of the PROVE handle's fifth beat (Embed → Educate) across the docs that spell it, plus a one-line diagram clarity gloss and one doc-invariant test. No code path, validator logic, dependency, permission, release posture, or public assurance claim changes; the eleven-beat path, its order, and the control points are untouched.

**Purpose:** Decide whether renaming the PROVE beat `Embed → Educate` can safely stay in Quick mode, and name the proof required.

---

## Change

- Slug: prove-educate-rename
- PR / issue: Rename the PROVE fifth beat Embed → Educate
- Owner: FlyFission
- Date: 2026-06-08
- Summary: Rename the fifth PROVE beat from **Embed** to **Educate** so the handle reads Plan · Run · Observe · Verdict · Educate. "Educate" names the same Baseline · Operate · Learn beats by what they are for — turning real operation into the lesson the next loop is taught — and drops the borrowed machine-learning "embedding" vocabulary. The five live spellouts change in lockstep: `README.md`, `WORKFLOWS.md`, `docs/02-operating-system/lifecycle.md`, and `docs/diagrams.md` (the PROVE-diagram subgraph title and the zoom-crosswalk row). A one-line gloss is added in `docs/diagrams.md` clarifying that the seven control points are the everyday short form of the eleven beats, and that the letter **O** is reused (Observe in PROVE, Operate in PRO). A new `tests/test_public_docs.py` invariant guards the handle so the mirror cannot drift. This supersedes the `Embed` label introduced by the `prove-overlay` packet; that historical record is left unchanged.

## Scope

- Affected files/configs/docs: `README.md`, `WORKFLOWS.md`, `docs/02-operating-system/lifecycle.md`, `docs/diagrams.md`, `tests/test_public_docs.py`.
- User-visible behavior changed? no (a documentation label plus a guard test).
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A diagram label or acronym reads poorly; reversible by edit. No runtime, evidence-gate, or trust-boundary effect. |
| Reversibility | Fully reversible; a label rename plus a one-line gloss and one test. |
| Detectability | High; the new `test_public_docs` invariant plus `pytest`, `doctor`, and `tokens` cover it, and the diagram renders visibly. |
| Exposure | Public docs, but the change is a label swap within existing boundary wording. |
| Uncertainty | Low; no logic change; the canonical eleven-beat path strings are untouched. |
| Why Quick is enough | No new trust boundary, dependency, permission, or release effect; follows the `prove-overlay` Quick precedent for the same handle. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `python tools/ng.py validate .nuclear/changes/prove-educate-rename`.
- Expected result: full suite green (including the new PROVE-handle invariant and the existing `test_public_docs` path assertions); doctor OK; token budget OK; this packet validates.
- Evidence link/location: `proof.md`.

## Critical-action self-check

- Exact target: the five PROVE/PRO spellouts and the diagrams crosswalk and subgraph title; specifically NOT the canonical eleven-beat ASCII path strings in `README.md` and `docs/02-operating-system/lifecycle.md` that `test_public_docs` asserts byte-for-byte.
- Expected result: only "Embed" → "Educate" (and the one diagram clarity gloss) changes; the eleven-beat sequence string and the `Decide -> Baseline -> Operate -> Learn` string stay byte-for-byte unchanged.
- Stop condition: if any edit would alter a canonical path string or an existing `test_public_docs` assertion, stop and revert.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected — no;
- a trust decision about a dependency, model, or API changed — no;
- a failure could be silent, delayed, costly, or hard to undo — no (a wrong label is visible and reverts cleanly);
- the AI had the power to write, run commands, use the network, or approve actions beyond drafting — no (drafting docs plus a guard test under review);
- the proof will not fit in one small `proof.md` — false.

None apply. Quick stands.

## Required links

- Packet: `.nuclear/changes/prove-educate-rename/`
- Related PR/issue: Rename the PROVE fifth beat Embed → Educate
- Proof record: `proof.md`
- Superseded label source: `.nuclear/changes/prove-overlay/` (left unchanged)
- Relevant source-map/crosswalk if invoked: `docs/diagrams.md` (canonical diagrams)

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public graded-rigor and software-assurance concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
