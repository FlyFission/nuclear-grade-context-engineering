# Ship

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

## Release identity

- Change slug: trust-propagation-two-party
- Version / release / baseline: not a tagged release; a branch for maintainer review
- PR / commit / artifact: this PR on branch `trust-propagation-two-party`
- Owner: Ben Huffer (maintainer)
- Date: 2026-07-17
- Intended release window: at maintainer discretion after independent review

## Scope and exclusions

- Included: `nuclear_grade/propagation.py`, `nuclear_grade/two_party.py`, `tests/test_propagation.py`, `tests/test_two_party.py`, and this packet.
- Excluded: wiring the checks into `validate_packet`; normalizing the claim-to-evidence table; GitHub branch-protection changes.
- Known non-goals: no change to existing validator behavior.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified |
| Basis / requirements / claims | pass | `basis.md` | Three requirements, two verified now |
| Questioning attitude | pass | `risk.md` | Captured inline |
| Verification | pass | `verification.md` | Unit tests, full suite, ruff, validation |
| Dependency / supply-chain evidence | not applicable | `verification.md` | Zero new dependencies |
| AI-assisted work checks | pass | `verification.md` | Recorded |
| Review / approval | gap | this PR | Independent maintainer review pending at merge |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Evidence authored by the AI actor, not yet independently confirmed | A load-bearing claim rests on the actor's own tests | mitigate | Ben Huffer | Maintainer review before merge |
| REQ-003 integration deferred | The gates are inert until wired in | defer | Ben Huffer | After the claim table is normalized |
| Claim-table schema varies across packets | Blocking wire-in could false-block | defer | Ben Huffer | When normalization is scoped |

## Rollback / restore plan

- Rollback method: `git revert` the merge commit, or delete the four new files.
- Data migration reversal or restore notes: none; the change creates no state or data.
- Feature flag / kill switch: not applicable; the modules are inert until imported.
- Owner on call: Ben Huffer.
- Time to restore estimate: under one minute.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI on the branch | Full suite, ruff, doctor, and packet validation all green | Ben Huffer | GitHub Actions | Re-run, then fix root cause |
| Imports of the new modules | No existing code imports them yet | Ben Huffer | grep of the repo | Confirm inertness before any wire-in |

## Handoff

- Operator/customer/support notes: the modules are a proposal; they do nothing until a follow-up packet wires them into `validate_packet`.
- Docs/runbook updated: this packet documents design, findings, and the integration path so work can continue elsewhere.
- Communication needed: maintainer to decide gate severity and the `Claim authorship` schema addition.
- Turnover record if activated: this ship record is the turnover.
- Follow-up date: at maintainer discretion.

## Release decision

- Decision: ship with residual risk
- Decision maker: Ben Huffer (maintainer)
- Rationale: The modules are inert and reversible, unit-tested, and lint clean, and they carry a documented integration path; landing them now preserves the design without changing validator behavior.
- Decision question answered by evidence? yes
- Decider independent of the actor that produced the change? yes: the maintainer decides the merge, and the actor was the AI.
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes: the proof commands are runnable.
- Conditions attached: do not wire the gates into `validate_packet` in this packet.
- Decision posture: conservative enough
- Abort or rollback trigger: any regression in the existing suite, or any unexpected import of the new modules.
- OPEX or post-release learning trigger: revisit after the table-normalization follow-up.

## Apply clearance

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | no | Independent maintainer review pending |
| Release / maintenance (freeze) window open | not applicable | No production surface |
| External state unchanged since verification — verdict not stale | yes | Local, deterministic evidence |
| Deployment policy satisfied | not applicable | No deployment |
| Rollback / kill-switch confirmed ready at apply-time | yes | Revert or delete files |

- Clearance decision: hold
- Cleared by (operator or policy owner, independent of the actor where trust-bearing): pending maintainer
- Apply window / valid until: on maintainer approval
- Re-clearance trigger: re-confirm if approvals, external state, or policy change before apply.

## Baseline trigger

- Baseline required? yes: when the modules are wired into `validate_packet`, a baseline record captures the new validator behavior.
- Baseline record: to be created in the follow-up integration packet.
- Revalidation trigger: any change to the claim-to-evidence table schema.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this PR
- Monitoring/dashboard/log query: GitHub Actions for this branch
- Rollback/runbook: the rollback method above

## Exit criteria

- The release decision is stated plainly.
- The apply-clearance call is stated: hold.
- Clearance was checked against operational context at apply-time, not inherited stale from the verdict.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned.
- A rollback/restore path exists.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on keeping the approved version under control (CM), release readiness, secure development, software assurance, supply-chain risk, software lifecycle, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
