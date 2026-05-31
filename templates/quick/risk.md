# Quick Risk Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

## Selected mode

- **Mode:** Quick
- **Why this mode:** (one line; escalate to Standard if any answer below feels uncertain)

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

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

Use only if the Quick change could hit the wrong target.

- Exact target:
- Expected result:
- Stop condition:

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected;
- a trust decision about a dependency, model, or API changed;
- a failure could be silent, delayed, costly, or hard to undo;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting;
- the proof will not fit in one small `proof.md`.

## Required links

- Packet: `.nuclear/changes/<slug>/`
- Related PR/issue:
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked:

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
