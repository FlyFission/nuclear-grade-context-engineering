# Ship: lean core, learned from Ponytail

## Release identity

- Change slug: lean-core-from-ponytail
- Version / release / baseline: none; a specification record
- PR / commit / artifact: draft pull request on `claude/bold-hamilton-w8qymj`
- Owner: Ben Huffer (maintainer); drafted by an AI agent
- Date: 2026-11-07
- Intended release window: not applicable; nothing is released

## Scope and exclusions

- Included: `analysis.md`, `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, this file; the regenerated `.nuclear/badge.json`.
- Excluded: every file outside `.nuclear/changes/lean-core-from-ponytail/` and the badge.
- Known non-goals: see `plan.md#Non-goals`.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard; hook phase `standard+authority` |
| Basis / requirements / claims | planned | `basis.md` | eleven requirements awaiting the owner's marks |
| Questioning attitude | pass | `risk.md` | summary in the risk record |
| Verification | planned | `verification.md` | baseline rows pass; gate rows planned |
| Dependency / supply-chain evidence | not applicable | `verification.md` | none |
| AI-assisted work checks | pass | `verification.md` | scope and screening stated |
| Evidence custody / coupling profile | pass | `verification.md` | decisive evidence separated or disclosed |
| Review / approval | planned | `plan.md` | the decision frontier |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Compression measured at five bullets, not at a full rewrite | a phase 2 body could lose a decision-changing line | mitigate; REQ-007 gate before any body ships | maintainer | phase 2 re-run |
| Eval grader and fit reader share a model family with the drafter | correlated error; structured check only | accept; stated in every phase record | maintainer | an external run of the harness |
| One reviewer on the card text | a softened floor could pass one read | mitigate; the floor has a grep test and the diff is small | maintainer | phase 1 review |
| D1 persona unresolved | tone and compression of the card | defer | maintainer | after phase 1 draft |

## Rollback / restore plan

- Rollback method: revert the commit; nothing outside this folder changes.
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: not applicable.
- Owner on call: maintainer.
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| none for this record | phases carry their own | maintainer | phase records | not applicable |

## Handoff

- Operator/customer/support notes: none.
- Docs/runbook updated: none; the specification is the artifact.
- Communication needed: the owner marks the frontier in `plan.md` on the draft pull request.
- Turnover record if activated: not activated.
- Follow-up date: when the frontier is marked.

## Release decision

- Decision: defer
- Decision maker: Ben Huffer (maintainer)
- Rationale: this record asks for approval of a specification. The decision it carries is whether phase 1 may start, which the owner gives by marking D2 to D4 and D6 to D8 in `plan.md`. Until then: defer.
- Decision question answered by evidence? yes/no: no; the baseline evidence motivates the work, and the gates that answer the question run in the phases.
- Verdict owner's authority axis relative to the actor: separated; the maintainer did not draft the text.
- Minimum coupling profile for this consequence met? yes / no; gap if no: yes for a specification; the decisive gates are specified with their custody.
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes/no: yes; every number has a command or a report path.
- Conditions attached: no phase starts before its frontier marks; the hook phase needs a human merge.
- Decision posture: conservative enough.
- Abort or rollback trigger: the owner strikes the specification.
- OPEX or post-release learning trigger: if a phase gate fails, the lesson goes to that phase's record and to `learning-from-experience`.

## Apply clearance

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | not applicable | nothing applies |
| Release / maintenance (freeze) window open | not applicable | nothing applies |
| External state unchanged since verification | yes | a specification only |
| Deployment policy satisfied | not applicable | nothing deploys |
| Rollback / kill-switch confirmed ready at apply-time | yes | revert |

- Clearance decision: not applicable (no real-world action)
- Cleared by (operator or policy owner, independent of the actor where trust-bearing): not applicable
- Apply window / valid until: not applicable
- Re-clearance trigger: not applicable

## Baseline trigger

- Baseline required? yes/no: no
- Baseline record: none
- Revalidation trigger: the phase 1 record re-reads this specification before build.

## Required links

- [`risk.md`](risk.md)
- [`basis.md`](basis.md)
- [`verification.md`](verification.md)
- PR/commit/release artifact: the draft pull request
- Monitoring/dashboard/log query: not applicable
- Rollback/runbook: revert the commit

## Exit criteria

- The release decision is stated plainly.
- The apply-clearance call is stated or marked `not applicable`.
- The evidence status and the gaps are visible.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
