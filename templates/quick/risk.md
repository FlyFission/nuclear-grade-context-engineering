# Quick Risk Template

## Selected mode

- **Mode:** Quick
- **Why this mode:** (one line; escalate to Standard if any answer below feels uncertain)

**Purpose:** Decide whether a small change can safely stay in Quick mode and name the proof required.

**Activation threshold:** Use for low-consequence, reversible, easy-to-detect changes with no new user trust boundary, dependency trust decision, security/privacy effect, release posture change, or AI authority change.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, escalate to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden escalation triggers, not to perform a full design review.

---

## Change

- Slug:
- PR / issue:
- Owner:
- Date:
- Summary:

## Scope

- Affected files/configs/docs:
- User-visible behavior changed? yes/no:
- Dependency/model/API/prompt/tool permission changed? yes/no:
- Release or rollback posture changed? yes/no:

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | |
| Reversibility | |
| Detectability | |
| Exposure | |
| Uncertainty | |
| Why Quick is enough | |

## Required proof

- Command/check/eval to run:
- Expected result:
- Evidence link/location:

## Critical-action self-check

Use only if the Quick change has a wrong-target risk.

- Exact target:
- Expected result:
- Stop condition:

## Escalation check

Escalate to Standard if any are true:

- users, data, security, permissions, operations, or architecture care;
- a dependency/model/API trust decision changed;
- failure could be silent, delayed, costly, or hard to reverse;
- AI had write/execute/network/approval authority beyond drafting;
- proof cannot be captured in one small `proof.md`.

## Required links

- Packet: `.nuclear/changes/<slug>/`
- Related PR/issue:
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked:

## Exit criteria

- Mode is justified as Quick.
- Required proof is named before or during the change.
- No Standard/Nuclear activation trigger is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public graded-rigor, configuration-management, software-assurance, and secure-development concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
