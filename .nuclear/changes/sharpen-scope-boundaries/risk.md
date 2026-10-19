# Quick Risk Record

## Selected mode

- **Mode:** Quick
- **Why this mode:** README-only wording update that narrows scope and clarifies boundaries; easy to review and revert; no code, dependency, security, release, permission, or runtime behavior changes.

**Purpose:** Keep the repository sharp by making minimum sufficient context and runtime/tooling boundaries explicit.

**Activation threshold:** Low-stakes public documentation change with a clear proof path: inspect the diff and run the repository validator on this Quick packet.

**Minimum useful version:** This record names the changed files, the scope boundary, and the proof commands.

**Overhead trap:** Keep this record short; the change exists to reduce framework creep, not create more process around it.

---

## Change

- Slug: `sharpen-scope-boundaries`
- PR / issue: not opened yet
- Owner: change actor
- Date: 2026-07-01
- Summary: Add concise README language for minimum sufficient context, agent context files as operating-envelope items, and a clear boundary that the repo is not an agent runtime/task manager/approval/observability platform.

## Scope

- Affected files/configs/docs: `README.md`, `.nuclear/changes/sharpen-scope-boundaries/risk.md`, `.nuclear/changes/sharpen-scope-boundaries/proof.md`
- User-visible behavior changed? no
- Dependency/model/API/prompt/tool permission changed? no
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | Confusing or over-broad README wording; reversible by editing/removing the paragraphs. |
| Reversibility | High; single docs diff can be reverted. |
| Detectability | High; reviewers can inspect the exact README diff. |
| Exposure | Public docs only; no code/runtime effect. |
| Uncertainty | Low; requested change is scope/wording clarification aligned with prior discussion. |
| Why Quick is enough | The change reduces claims and scope rather than adding authority, dependencies, or behavior. |

## Required proof

- Command/check/eval to run: `python tools/ng.py validate .nuclear/changes/sharpen-scope-boundaries`; `git diff --check`
- Expected result: Quick packet validates; diff has no whitespace errors.
- Evidence link/location: `proof.md`

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: `README.md` and this Quick packet only.
- Expected result: Docs clarify scope without changing CLI/templates/workflows.
- Stop condition: Any code, template, command, permission, dependency, or release-posture change appears in the diff.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected;
- a trust decision about a dependency, model, or API changed;
- a failure could be silent, delayed, costly, or hard to undo;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting;
- the proof will not fit in one small `proof.md`.

None are true for this docs-only boundary clarification.

## Required links

- Packet: `.nuclear/changes/sharpen-scope-boundaries/`
- Related PR/issue: not opened yet
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: not invoked; no new source-lineage or compliance claim added.

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
