# Decision Authority Record

This record says who may decide each step of adding this repository's consequence policy. The controlling rule is the engine's built-in policy-self rule: any change to `.nuclear/consequence-policy.json` requires `standard+authority`, which means a human decides the merge.

This validator checks record structure and declared consistency only. It does not authenticate actors, prove evidence quality or independence, authorize an action, or establish engineering adequacy, safety, security, or compliance.

## Decision episode

- **Decision ID:** DEC-001
- **Candidate / action:** merge `.nuclear/consequence-policy.json` (12 rules) and its pinning test into `main`.
- **Policy version:** built-in policy-self rule in `nuclear_grade/consequence.py` at commit `5b4e023`, plus owner decisions 1-6 in the WS1 master plan.
- **Policy authority ID:** FlyFission (repository owner).
- **Policy custodian:** FlyFission (repository owner); the rule ships in the engine merged as #123.
- **Policy digest:** sha256:cddfb6f3ba08960ac405262ece164fb13bfb2c31d9d07488a937b1671569cf44
- **Policy valid through:** not applicable: the rule holds until a later change to `nuclear_grade/consequence.py` alters it, and that change is itself gated.
- **Action identity:** `.nuclear/consequence-policy.json` with sha256 `b069000e4afda479f79a3b4e1e8342ae23e3ba02539689e131b89ac0cb001199`, on branch `claude/ws1-repo-policy`.
- **Decision status:** pending maintainer review
- **Reversible:** yes; revert the commit, and CI does not read the file yet.
- **Consequence if wrong:** once CI reads it, a wrong rule either leaves a trust surface without a record or asks for records on ordinary work.

Do not treat a general tool permission, repository role, agent capability, or prior approval as authorization for this exact action.

## Evidence basis

Allowed coded source states (the field remains named `Raw state`) are `observed`, `bounded_absence`, `unknown`, and `disputed`.

| Evidence ID | Raw state | Scope / basis | Intended use / V&V status | Custody / profile link |
|---|---|---|---|---|
| E-001 | observed | `tests/test_repo_policy.py`, 21 tests, run locally and in CI on the PR | supports the rule mapping; self-check | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |
| E-002 | observed | the `dependency_lane` block and the path-match check against `git ls-files` | supports lane configuration; self-check | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |
| E-003 | observed | backtest over the 49 first-parent commits ending at `31e0a9e` | supports the cost and shortfall picture; not ground truth | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |

Every Evidence ID in this file must be declared in `verification.md`. The evidence state is an author-coded, source-linked determination, not a sensor-raw fact or a conclusion about control, authorization, adequacy, completeness, or independence.

## Decision-right allocation

Allowed authority values are:

- `agent_permitted`
- `human_required`
- `separate_control_required`
- `dual_authority_required`
- `blocked_pending_evidence`
- `prohibited_for_agent`

| Decision right | Proposed actor | Evidence IDs | Evidence-basis authority | Policy / standing gate | Required authority | Transfer trigger |
|---|---|---|---|---|---|---|
| prepare | AI agent | not applicable | AI agent | owner request "start the policy file PR" | agent_permitted | transfer when preparation would touch CI, hooks, or the engine |
| recommend | AI agent | E-001, E-003 | AI agent | owner decisions 1-6 | agent_permitted | transfer when a rule departs from a recorded owner decision |
| verify | AI agent; GitHub Actions re-runs the test | E-001 | AI agent | CI on the PR | agent_permitted | transfer when CI fails or a reviewer disputes a rule |
| validate | maintainer (FlyFission) | E-001, E-003 | maintainer (FlyFission) | policy-self rule | human_required | transfer or block when the 13 shortfalls are judged over-classification |
| verdict | maintainer (FlyFission) | E-001, E-003 | maintainer (FlyFission) | policy-self rule | human_required | block when review finds a rule wrong |
| accept | maintainer (FlyFission) | E-001, E-003 | maintainer (FlyFission) | policy-self rule | human_required | block when residual risks in `ship.md` lack an owner |
| apply | maintainer (FlyFission) merges | E-001, E-003 | maintainer (FlyFission) | policy-self rule; owner decision 3 (human merge) | human_required | block while CI is red or a review thread is open |
| reopen | maintainer (FlyFission) | not applicable | maintainer (FlyFission) | any later policy change is itself `standard+authority` | human_required | reopen when owner labels or advisory receipts contradict a rule |
| close | maintainer (FlyFission) | E-001 | maintainer (FlyFission) | policy-self rule | human_required | close after the advisory CI job has run on real PRs |

`accept` and `apply` are separate rights. Nominal approval is not proof that the approver had the evidence, time, authority, or effective ability to stop or reverse the action.

## Derived authority result

- **Decision right evaluated:** apply
- **Result:** human_required
- **Basis:** the policy-self rule makes this change `standard+authority`, and all decisive evidence (E-001, E-003) is self-check, so the agent cannot clear its own policy for merge.
- **Derived by:** AI agent, reading the built-in policy-self rule; to be confirmed by the maintainer.
- **Recorded at:** 2026-11-03T15:30:00Z

Allowed derived results are `agent_apply_structurally_clearable`, `human_required`, `separate_control_required`, `dual_authority_required`, `blocked_pending_evidence`, `prohibited_for_agent`, and `policy_result_indeterminate`.

## Reopen and closure controls

- **Reopen authority:** maintainer (FlyFission)
- **Reopen trigger:** owner labels or advisory CI receipts that contradict a rule; a change to the policy-self rule; a changed policy digest.
- **Superseded decision handling:** a later policy change opens a new decision episode with its own record; this one is not reused.
- **Close authority:** maintainer (FlyFission)
- **Closure evidence:** E-001, plus advisory CI receipts once that job exists.
- **Interim expiry:** not applicable: CI does not read the policy until the advisory job lands, which carries its own record.

Reopening preserves the prior record and creates or identifies a successor decision episode. It does not rewrite the historical decision basis.

## Required links

- [Verification and evidence custody](verification.md)
- [Release decision, rollback, and monitoring](ship.md)
- Exact policy or standing-gate record: `nuclear_grade/consequence.py#_evaluate_policy_self` at commit `5b4e023`.

## Exit criteria

- Every required decision right appears exactly once.
- The derived result is policy-consistent with the `apply` allocation.
- Reopen and closure authorities and triggers are explicit.

## Source-lineage note

This record follows the repository's evidence-custody and actor-authority model, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
