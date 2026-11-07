# Decision Authority Record

This record says who may decide each step of changing the receipt contract and the consequence policy. The controlling rule is the engine's built-in policy-self rule: any change to `.nuclear/consequence-policy.json` requires `standard+authority`, which means a human decides the merge.

This validator checks record structure and declared consistency only. It does not authenticate actors, prove evidence quality or independence, authorize an action, or establish engineering adequacy, safety, security, or compliance.

## Decision episode

- **Decision ID:** DEC-001
- **Candidate / action:** merge the acceptance block, `verify_receipt`, three CLI flags, the MCP line, the 32-test fixture suite, and the policy edit into `main`.
- **Policy version:** built-in policy-self rule in `nuclear_grade/consequence.py`, plus this repository's `.nuclear/consequence-policy.json` before this change (the digest below is of that base file, as of commit `06e762e`).
- **Policy authority ID:** FlyFission (repository owner).
- **Policy custodian:** FlyFission (repository owner).
- **Policy digest:** sha256:73ea9ddf3ccfb538bb2a9895a8b6ef5f1938160ea7151bfc29aef51244db8139
- **Policy valid through:** not applicable: the rule holds until a later change to `nuclear_grade/consequence.py` alters it, and that change is itself gated.
- **Action identity:** the branch `claude/amazing-mayer-tb7nbm`, as opened in the draft pull request.
- **Decision status:** pending maintainer review
- **Reversible:** yes; revert the commit. The additions are inert unless a client reads `acceptance`.
- **Consequence if wrong:** a reader trusts an eligibility state that does not fit their records, or a fixture gives false confidence in the acceptance path.

Do not treat a general tool permission, repository role, agent capability, or prior approval as authorization for this exact action.

## Evidence basis

Allowed coded source states (the field remains named `Raw state`) are `observed`, `bounded_absence`, `unknown`, and `disputed`.

| Evidence ID | Raw state | Scope / basis | Intended use / V&V status | Custody / profile link |
|---|---|---|---|---|
| E-001 | observed | `tests/test_acceptance_adversarial.py` and the full suite, run locally and in CI on the PR | supports the contract and its consumers; self-check | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |
| E-002 | observed | seven weakened-control reruns of the fixture suite | supports that the fixtures can fail; self-check | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |
| E-003 | observed | receipts for the 82 earlier records | supports the usability picture; not ground truth | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |

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
| prepare | AI agent | not applicable | AI agent | maintainer request to act on the roadmap review | agent_permitted | transfer when preparation would touch CI, hooks, or `validate_packet` |
| recommend | AI agent | E-001 | AI agent | the maintainer's review comments | agent_permitted | transfer when a rule departs from the comments |
| verify | AI agent; GitHub Actions re-runs the suite | E-001 | AI agent | CI on the PR | agent_permitted | transfer when CI fails or a reviewer disputes a fixture |
| validate | maintainer (FlyFission) | E-001, E-002 | maintainer (FlyFission) | policy-self rule | human_required | transfer or block when the eligibility split is judged wrong |
| verdict | maintainer (FlyFission) | E-001, E-002 | maintainer (FlyFission) | policy-self rule | human_required | block when review finds a fixture that tests nothing |
| accept | maintainer (FlyFission) | E-001, E-002 | maintainer (FlyFission) | policy-self rule | human_required | block when residual risks in `ship.md` lack an owner |
| apply | maintainer (FlyFission) merges | E-001, E-002 | maintainer (FlyFission) | policy-self rule; human merge | human_required | block while CI is red or a review thread is open |
| reopen | maintainer (FlyFission) | not applicable | maintainer (FlyFission) | any later policy change is itself `standard+authority` | human_required | reopen when owner labels contradict the eligibility split |
| close | maintainer (FlyFission) | E-001 | maintainer (FlyFission) | policy-self rule | human_required | close after the contract has been read on real PRs |

`accept` and `apply` are separate rights. Nominal approval is not proof that the approver had the evidence, time, authority, or effective ability to stop or reverse the action.

## Derived authority result

- **Decision right evaluated:** apply
- **Result:** human_required
- **Basis:** the change edits the consequence policy, so the policy-self rule makes it `standard+authority`, and all decisive evidence (E-001, E-002) is self-check, so the agent cannot clear it for merge.
- **Derived by:** AI agent, reading the built-in policy-self rule; to be confirmed by the maintainer.
- **Recorded at:** 2026-11-07T00:00:00Z

Allowed derived results are `agent_apply_structurally_clearable`, `human_required`, `separate_control_required`, `dual_authority_required`, `blocked_pending_evidence`, `prohibited_for_agent`, and `policy_result_indeterminate`.

## Reopen and closure controls

- **Reopen authority:** maintainer (FlyFission)
- **Reopen trigger:** owner labels that contradict the eligibility split; a change to the policy-self rule; a decision-custody change that makes an expected failure pass.
- **Superseded decision handling:** a later contract change opens a new decision episode with its own record; this one is not reused.
- **Close authority:** maintainer (FlyFission)
- **Closure evidence:** E-001, plus the PR's CI run.
- **Interim expiry:** not applicable: nothing reads the new fields by default.

Reopening preserves the prior record and creates or identifies a successor decision episode. It does not rewrite the historical decision basis.

## Required links

- [Verification and evidence custody](verification.md)
- [Release decision, rollback, and monitoring](ship.md)
- Exact policy or standing-gate record: `nuclear_grade/consequence.py#_evaluate_policy_self`.

## Exit criteria

- Every required decision right appears exactly once.
- The derived result is policy-consistent with the `apply` allocation.
- Reopen and closure authorities and triggers are explicit.

## Source-lineage note

This record follows the repository's evidence-custody and actor-authority model, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
