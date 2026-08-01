# Quick Risk Template

## Selected mode

- **Mode:** Quick
- **Why this mode:** One public-guidance sentence is changed; the edit is local, immediately reversible, and directly checkable against the canonical risk skill.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: `quickstart-mode-ambiguity`
- PR / issue: #87
- Owner: FlyFission
- Date: 2026-07-27
- Summary: Replace a blanket "start with Standard" fallback with the repo's existing stakes-based ambiguity rule.

## Scope

- Affected files/configs/docs: `QUICKSTART.md` and this Quick packet
- User-visible behavior changed? yes — mode-selection guidance is sharper
- Dependency/model/API/prompt/tool permission changed? no
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A reader may over-grade routine work or under-grade genuinely uncertain work. |
| Reversibility | One-line documentation revert. |
| Detectability | Direct text review and public-doc tests. |
| Exposure | Public quickstart readers; no runtime behavior. |
| Uncertainty | Low; `rating-change-risk` already says mode follows stakes, not effort, and genuinely unclear tiers rise. |
| Why Quick is enough | No new mechanism, trust boundary, runtime behavior, or assurance claim. |

## Required proof

- Command/check/eval to run: `python -m pytest tests/test_public_docs.py -q`; `python tools/ng.py doctor .`; `python tools/ng.py validate .nuclear/changes/quickstart-mode-ambiguity`; `git diff --check`
- Expected result: all tests and checks pass; the Quick packet validates.
- Evidence link/location: `proof.md` and PR checks

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: `QUICKSTART.md` mode-selection fallback only
- Expected result: ambiguity routes by stakes while effort is explicitly excluded
- Stop condition: any edit that introduces a new mode, artifact, or workflow

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected;
- a trust decision about a dependency, model, or API changed;
- a failure could be silent, delayed, costly, or hard to undo;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting;
- the proof will not fit in one small `proof.md`.

## Required links

- Packet: `.nuclear/changes/quickstart-mode-ambiguity/`
- Related PR/issue: #87
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: none; this aligns existing repo doctrine

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
