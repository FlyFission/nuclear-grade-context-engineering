# Quick Risk Record

## Selected mode

- **Mode:** Quick
- **Why this mode:** Narrows two existing public benchmark claims to the tested catalog; documentation-only, one-line revert, no capability or trust boundary change.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: scope-pilot-claims
- PR / issue: #86
- Owner: FlyFission
- Date: 2026-08-01
- Summary: Scope the skill-benchmark claim in `README.md` and `SKILLS.md` to the 28 skills that were in the catalog when the pilot ran, and state explicitly that the pilot is a historical snapshot, not evidence for skills added later. Adds a verifiable run-date note to the pilot README.

## Scope

- Affected files/configs/docs: `README.md`, `SKILLS.md`, `evals/skill-benchmark-pilot/README.md`.
- User-visible behavior changed? no — public wording only; no runtime, skill, template, or command change.
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A reader could over- or under-read the pilot's scope; mitigated because the change narrows (not widens) the claim to the tested set. |
| Reversibility | One-line: revert the commit to restore the prior wording. |
| Detectability | High: the two sentences and the run-date note are inspectable in the diff. |
| Exposure | Low: public docs; no data, credentials, or release surface. |
| Uncertainty | Low: the pilot's 28-skill scope and July 2026 run date are established by the checked-in artifacts. |
| Why Quick is enough | Reversible, detectable, docs-only, narrows an existing claim. |

## Required proof

- Command/check/eval to run: `python -m pytest tests/test_public_docs.py -q`, `python tools/ng.py doctor .`, `python tools/ng.py tokens .`, `git diff --check`.
- Expected result: all pass; the pilot README carries a verifiable run date the top-level docs point to.
- Evidence link/location: `proof.md`.

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: the benchmark-claim sentences in `README.md` and `SKILLS.md`, plus the pilot README status block.
- Expected result: only wording changes; no numeric claim is widened beyond the tested 28 skills.
- Stop condition: any code, template, skill, or command file changes unexpectedly.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected; — no
- a trust decision about a dependency, model, or API changed; — no
- a failure could be silent, delayed, costly, or hard to undo; — no (one-line revert)
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting; — no
- the proof will not fit in one small `proof.md`. — no

## Required links

- Packet: `.nuclear/changes/scope-pilot-claims/`
- Related PR/issue: #86
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: n/a.

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
