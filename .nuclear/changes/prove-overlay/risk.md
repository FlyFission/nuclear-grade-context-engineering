# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** Additive documentation only — a new diagrams section, one mirrored diagram, and three one-line callouts. No code, validator logic, dependencies, permissions, or public assurance claims change.

**Purpose:** Decide whether the PROVE/PRO acronym overlay can safely stay in Quick mode and name the proof required.

---

## Change

- Slug: prove-overlay
- PR / issue: PROVE/PRO acronym overlay + swim-lane diagrams
- Owner: FlyFission
- Date: 2026-06-04
- Summary: Overlay a memory handle on the existing eleven-beat path — PRO (Plan · Run · Operate) zoomed out, PROVE (Plan · Run · Observe · Verdict · Embed) zoomed in — with two top-down swim-lane Mermaid diagrams and a zoom-level crosswalk. The beats, their order, and the control points are unchanged. Canonical content lives in `docs/diagrams.md` (new section 2); `README.md` mirrors the PRO diagram; `WORKFLOWS.md` and `docs/02-operating-system/lifecycle.md` get one file-unique callout line each.

## Scope

- Affected files/configs/docs: `docs/diagrams.md` (new section + renumber of later sections), `README.md`, `WORKFLOWS.md`, `docs/02-operating-system/lifecycle.md`.
- User-visible behavior changed? no (documentation only).
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A diagram or label reads poorly; reversible by edit. No runtime, evidence-gate, or trust-boundary effect. |
| Reversibility | Fully reversible; additive docs plus a section renumber. |
| Detectability | High; diagrams render visibly, and `pytest` + `doctor` cover the public-doc invariants. |
| Exposure | Public docs, but additive and within the existing boundary wording. |
| Uncertainty | Low; no logic change; the canonical eleven-beat path is untouched. |
| Why Quick is enough | No new trust boundary, dependency, permission, or release effect. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`; `python tools/ng.py doctor .`; `python tools/ng.py validate .nuclear/changes/prove-overlay`.
- Expected result: full suite green (incl. the `test_public_docs` path assertions and `test_tokens` budget + redundancy index); doctor OK; this packet validates.
- Evidence link/location: `proof.md`.

## Critical-action self-check

- Exact target: the four documentation files in Scope; specifically the canonical ASCII path strings in `README.md` and `docs/02-operating-system/lifecycle.md`, which `test_public_docs` asserts.
- Expected result: overlay text is added *around* those strings; the strings themselves stay byte-for-byte unchanged.
- Stop condition: if any edit would alter the canonical path order or a `test_public_docs` assertion string, stop and revert.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected — no;
- a trust decision about a dependency, model, or API changed — no;
- a failure could be silent, delayed, costly, or hard to undo — no;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting — no (drafting docs under review);
- the proof will not fit in one small `proof.md` — false.

None apply. Quick stands.

## Required links

- Packet: `.nuclear/changes/prove-overlay/`
- Related PR/issue: PROVE/PRO acronym overlay + swim-lane diagrams
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/diagrams.md` (canonical diagrams)

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public graded-rigor and software-assurance concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
