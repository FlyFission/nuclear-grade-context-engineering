# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** Additive documentation and a template-legend line; no code paths, validator logic, or public claims changed.

**Purpose:** Decide whether the visual/readability enhancements can safely stay in Quick mode and name the proof required.

---

## Change

- Slug: visual-readability-enhancements
- PR / issue: repo-review enhancements (PR #1 of the multi-perspective review)
- Owner: FlyFission
- Date: 2026-05-30
- Summary: Add Mermaid diagrams (lifecycle, mode tree, skill graph, packet artifact graph), a glossary, an agent threat-model doc, name `using-nuclear-grade` as the skill router, align the QUICKSTART first-run note with actual validator output, and add `planned` to the verification template legend.

## Scope

- Affected files/configs/docs: `docs/diagrams.md` (new), `docs/glossary.md` (new), `docs/02-operating-system/agent-threat-model.md` (new), `README.md`, `SKILLS.md`, `QUICKSTART.md`, `docs/README.md`, `SECURITY.md`, `templates/standard/verification.md`.
- User-visible behavior changed? no (documentation and one template legend line).
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A diagram or doc reads incorrectly; reversible by edit. No runtime or evidence-gate effect. |
| Reversibility | Fully reversible; documentation and one template line. |
| Detectability | High; diagrams render visibly, tests and doctor cover docs/templates. |
| Exposure | Public docs, but additive and boundary-noted. |
| Uncertainty | Low; no logic change. |
| Why Quick is enough | No new trust boundary, dependency, permission, or release effect. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`; `python tools/ng.py doctor .`; validate all in-repo packets; Mermaid render-check via diagram validator.
- Expected result: 76 tests pass, doctor OK, 10/10 packets green, all 4 diagrams valid.
- Evidence link/location: `proof.md`.

## Escalation check

Escalate to Standard if any are true:

- users, data, security, permissions, operations, or architecture care — no;
- a dependency/model/API trust decision changed — no;
- failure could be silent, delayed, costly, or hard to reverse — no;
- AI had write/execute/network/approval authority beyond drafting — no;
- proof cannot be captured in one small `proof.md` — false.

None apply. Quick stands.

## Required links

- Packet: `.nuclear/changes/visual-readability-enhancements/`
- Related PR/issue: repo-review enhancements
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Mode is justified as Quick.
- Required proof is named before or during the change.
- No Standard/Nuclear activation trigger is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public graded-rigor and software-assurance concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
