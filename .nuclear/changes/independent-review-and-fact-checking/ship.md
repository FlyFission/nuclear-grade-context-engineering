# Independent Review and Fact Checking — Ship

## Release identity

- Change slug: independent-review-and-fact-checking
- Version / release / baseline: `[Unreleased]` in `CHANGELOG.md`; no version bump
- PR / commit / artifact: draft PR from `claude/independent-review-fact-check`
- Owner: FlyFission
- Date: 2026-11-03
- Intended release window: next release after owner review; no date set

## Scope and exclusions

- Included: `--two-party` wiring; `verification-methods-and-depth.md`; the `checking-facts` skill and its catalog wiring; reciprocal skill pointers; the skill-catalog audit as a proposal.
- Excluded: any skill merge or removal; making `--two-party` default or adding it to CI; branch protection and CODEOWNERS.
- Known non-goals: detecting identity aliasing or same-model-family reviewers inside the validator.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard |
| Basis / requirements / claims | pass | `basis.md` | 5 requirements |
| Questioning attitude | pass | `risk.md` | inline summary |
| Verification | pass with one gap | `verification.md` | REQ-005a gap: audit rows beyond the 4 spot-checks have no second-party check |
| Dependency / supply-chain evidence | not applicable | none | no new dependency |
| AI-assisted work checks | pass | `verification.md` | agent review recorded and classified as self-check |
| Evidence custody / coupling profile | pass (disclosed) | `verification.md` | every decisive row is a self-check; `--two-party` fails by design |
| Review / approval | gap | this file | human second party pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No human has verified the two-party rule; the only review was an agent of the same model family briefed by the author | A rule that passes a packet it should fail would give adopters false confidence | defer to owner review before merge | FlyFission | owner review of `two_party.py` and `tests/test_two_party.py` |
| `checking-facts` has no efficacy measurement | The skill may add nothing over a generic prompt, as the audit found for several others | accept; follow-up: an adversarial set (wrong units, stale revision, fabricated citation, two sites repeating one error, docs vs actual API behavior, misleading context, unreachable source) scored on false acceptance | FlyFission | next ladder run |
| The audit's per-skill verdicts rest on n=3, one model family, and repo-authored rubrics | A merge chosen on them could remove a skill that helps | defer; each merge needs its own packet and owner decision | FlyFission | any merge packet |
| Skill count went from 30 to 31 while the audit recommends 22 | Adds catalog surface the audit says to shrink | accept on the owner's explicit request for a fact-check skill; revisit in the consolidation decision | FlyFission | consolidation decision |
| `--two-party` compares declared strings only | Two names for one actor pass | accept; documented in the module, `validators.md`, and the doctrine page | FlyFission | an aliasing incident |

## Rollback / restore plan

- Rollback method: `git revert` the merge commit, then `python tools/ng.py gen-commands` and `python tools/build_diagrams.py`.
- Data migration reversal or restore notes: not applicable; no data.
- Feature flag / kill switch: `--two-party` is opt-in; not passing the flag is the kill switch.
- Owner on call: FlyFission
- Time to restore estimate: minutes

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI on the PR | all jobs green | FlyFission | PR checks | fix forward or revert |
| Adopter reports of default `ng validate` changing | zero; default output is byte-identical | FlyFission | issues | revert the `ng_validate.py` wiring |
| `--two-party` false pass found in review or use | zero | FlyFission | issues, OPEX | add a failing test, fix the rule |

## Handoff

- Operator/customer/support notes: `--two-party` is new and opt-in; the CHANGELOG entry says what it does not detect.
- Docs/runbook updated: `validators.md`, `cli-reference.md`, `verification-methods-and-depth.md`, `CORE.md`, `SKILLS.md`, `COMMANDS.md`.
- Communication needed: the draft PR description summarizes the audit and asks the owner to decide on the merges.
- Turnover record if activated: not applicable; the open decisions are listed below.
- Follow-up date: at owner review.

Open decisions for the owner:

1. Whether to merge this PR.
2. Whether to add `--two-party` to this repo's own CI, and from which packet forward.
3. Which of the audit's merges to open packets for, if any (answered by the stacked consolidation PR).
4. When to make `--two-party` mandatory: the reviews advise new Standard packets first, with historical records handled by an explicit migration or legacy exception.

## Release decision

This is the verdict on correctness and release-worthiness.

- Decision: defer
- Decision maker: FlyFission (the author recommends; the owner decides)
- Rationale: the evidence supports the claims as built: tests, a byte-identical default-mode sweep, and a two-copy quotation check. But every decisive evidence row is a self-check, including the agent review. The change is to the repo's own independence checker, so the repo's rule for Standard work needs a human second party before merge.
- Decision question answered by evidence? yes, by self-check evidence only
- Verdict owner's authority axis relative to the actor: separated; the owner did not author the change
- Minimum coupling profile for this consequence met? no; gap: no human second party yet
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes; every command in `verification.md` reruns
- Conditions attached: the owner records a custody row as verifier for the claims they accept; `ng validate --two-party` then passes for those claims.
- Decision posture: conservative enough
- Abort or rollback trigger: a default-mode output change for any existing packet, or a confirmed false pass under `--two-party`
- OPEX or post-release learning trigger: any false pass or false fail under `--two-party`

## Apply clearance

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | no | owner review pending |
| Release / maintenance (freeze) window open | not applicable | no scheduled release |
| External state unchanged since verification — verdict not stale | yes | branched from current `main` |
| Deployment policy satisfied | not applicable | merge is the apply |
| Rollback / kill-switch confirmed ready at apply-time | yes | revert plus regeneration |

- Clearance decision: hold
- Cleared by (operator or policy owner, independent of the actor where trust-bearing): pending, FlyFission
- Apply window / valid until: re-check if `main` moves before merge
- Re-clearance trigger: `main` moves, or the PR changes after the owner's review

## Baseline trigger

- Baseline required? no; no release is cut
- Baseline record: not applicable
- Revalidation trigger: a release that includes this change

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: draft PR from `claude/independent-review-fact-check`
- Monitoring/dashboard/log query: PR checks
- Rollback/runbook: this file, Rollback section

## Exit criteria

- The release decision is stated plainly.
- The apply-clearance call is stated.
- The leftover risks have an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade release record inspired by public release-readiness and configuration-management practice mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
