# Decision Authority Record

This record says who may decide each step of adding job timeouts to this repository's CI. The controlling rule is the repository policy rule `ci` in `.nuclear/consequence-policy.json`: any change under `.github/**` requires `standard+authority`, which means a human decides the merge.

This validator checks record structure and declared consistency only. It does not authenticate actors, prove evidence quality or independence, authorize an action, or establish engineering adequacy, safety, security, or compliance.

## Decision episode

- **Decision ID:** DEC-001
- **Candidate / action:** merge `timeout-minutes` on the 9 jobs of `ci.yml` and `release.yml`, the scaffold workflow text, and `tests/test_workflow_timeouts.py` into `main`.
- **Policy version:** rule `ci` in `.nuclear/consequence-policy.json` at the base commit of this branch.
- **Policy authority ID:** FlyFission (repository owner).
- **Policy custodian:** FlyFission (repository owner).
- **Policy digest:** sha256:73ea9ddf3ccfb538bb2a9895a8b6ef5f1938160ea7151bfc29aef51244db8139
- **Policy valid through:** not applicable: the rule holds until a later change to the policy file, which is itself gated.
- **Action identity:** the four paths in `risk.md` with combined sha256 `8000fedcbacccf4ed8799913759b71e0f794bddd7c503abe7682fa611385073b` (ci.yml, release.yml, cli.py, test file concatenated in that order), on branch `claude/funny-fermi-hls5sp`.
- **Decision status:** pending maintainer review
- **Reversible:** yes; revert the commit.
- **Consequence if wrong:** a cap shorter than a real run fails a CI or release run until rerun with a larger cap; a missing cap changes nothing from today.

Do not treat a general tool permission, repository role, agent capability, or prior approval as authorization for this exact action.

## Evidence basis

Allowed coded source states (the field remains named `Raw state`) are `observed`, `bounded_absence`, `unknown`, and `disputed`.

| Evidence ID | Raw state | Scope / basis | Intended use / V&V status | Custody / profile link |
|---|---|---|---|---|
| E-001 | observed | `tests/test_workflow_timeouts.py` failing on the unchanged files and passing on the changed ones, run locally and re-run by CI on the PR | supports REQ-001..003; self-check | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |
| E-002 | observed | job durations of run 42293941938 on `main` | supports cap sizing for `ci.yml` only; one run | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |
| E-003 | observed | the independent reviewer's findings | a challenge to the change, not verification | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |

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
| prepare | AI agent | not applicable | AI agent | owner instruction to copy valuable XERJ ideas after an adversarial review | agent_permitted | transfer when preparation would touch secrets, permissions, triggers or pins |
| recommend | AI agent | E-001, E-002 | AI agent | owner instruction | agent_permitted | transfer when a cap departs from measured runtime by more than the stated margin |
| verify | AI agent; GitHub Actions re-runs the test | E-001 | AI agent | CI on the PR | agent_permitted | transfer when CI fails or a reviewer disputes a cap |
| validate | maintainer (FlyFission) | E-001, E-002, E-003 | maintainer (FlyFission) | policy rule `ci` | human_required | transfer or block when the release caps are judged unsafe |
| verdict | maintainer (FlyFission) | E-001, E-002, E-003 | maintainer (FlyFission) | policy rule `ci` | human_required | block when review finds a cap wrong |
| accept | maintainer (FlyFission) | E-001, E-002 | maintainer (FlyFission) | policy rule `ci` | human_required | block when residual risks in `ship.md` lack an owner |
| apply | maintainer (FlyFission) merges | E-001, E-002 | maintainer (FlyFission) | policy rule `ci`; no agent merge authority | human_required | block while CI is red or a review thread is open |
| reopen | maintainer (FlyFission) | not applicable | maintainer (FlyFission) | any later change under `.github/**` is itself `standard+authority` | human_required | reopen when a release or CI run times out |
| close | maintainer (FlyFission) | E-001 | maintainer (FlyFission) | policy rule `ci` | human_required | close after the next tagged release completes inside its caps |

`accept` and `apply` are separate rights. Nominal approval is not proof that the approver had the evidence, time, authority, or effective ability to stop or reverse the action.

## Derived authority result

- **Decision right evaluated:** apply
- **Result:** human_required
- **Basis:** rule `ci` makes this change `standard+authority` and not overridable, and all decisive evidence (E-001) is self-check, so the agent cannot clear its own change to CI for merge.
- **Derived by:** AI agent, reading the policy rule; to be confirmed by the maintainer.
- **Recorded at:** 2026-11-06T22:00:00Z

Allowed derived results are `agent_apply_structurally_clearable`, `human_required`, `separate_control_required`, `dual_authority_required`, `blocked_pending_evidence`, `prohibited_for_agent`, and `policy_result_indeterminate`.

## Reopen and closure controls

- **Reopen authority:** maintainer (FlyFission)
- **Reopen trigger:** a CI or release job that hits its cap; a change to rule `ci`; a changed policy digest.
- **Superseded decision handling:** a later change to the caps opens a new decision episode with its own record; this one is not reused.
- **Close authority:** maintainer (FlyFission)
- **Closure evidence:** E-001, plus the next tagged release completing inside its caps.
- **Interim expiry:** not applicable: the caps have no expiry.

Reopening preserves the prior record and creates or identifies a successor decision episode. It does not rewrite the historical decision basis.

## Required links

- [Verification and evidence custody](verification.md)
- [Release decision, rollback, and monitoring](ship.md)
- Exact policy or standing-gate record: `.nuclear/consequence-policy.json` rule `ci`.

## Exit criteria

- Every required decision right appears exactly once.
- The derived result is policy-consistent with the `apply` allocation.
- Reopen and closure authorities and triggers are explicit.

## Source-lineage note

This record follows the repository's evidence-custody and actor-authority model, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
