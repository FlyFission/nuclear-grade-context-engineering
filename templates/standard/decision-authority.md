# Decision Authority Record

NUCLEAR-GRADE-PLACEHOLDER

Use this optional Standard-mode record when an AI agent or automation can recommend, decide, accept, apply, reopen, or close a consequential change. The record joins decision rights to the exact evidence IDs declared in `verification.md`.

This validator checks record structure and declared consistency only. It does not authenticate actors, prove evidence quality or independence, authorize an action, or establish engineering adequacy, safety, security, or compliance.

## Decision episode

- **Decision ID:** DEC-001
- **Candidate / action:** Replace with the exact bounded action under consideration.
- **Policy version:** Replace with the controlling local policy identifier and version.
- **Action identity:** Replace with a stable artifact, commit, request, or payload identifier.
- **Decision status:** blocked pending evidence
- **Reversible:** Replace with `yes`, `no`, or a bounded condition.
- **Consequence if wrong:** Replace with the bounded consequence of an incorrect authority result.

Do not treat a general tool permission, repository role, agent capability, or prior approval as authorization for this exact action.

## Evidence basis

Allowed raw states are `observed`, `bounded_absence`, `unknown`, and `disputed`.

`bounded_absence` requires the Scope / basis cell to state both a finite enumerated scope and a time boundary. Missing telemetry is `unknown`, not `bounded_absence`.

| Evidence ID | Raw state | Scope / basis | Intended use / V&V status | Custody / profile link |
|---|---|---|---|---|
| E-001 | unknown | Records required for this decision have not yet been observed | Intended use and V&V status remain unresolved | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |

Every Evidence ID in this file must be declared in `verification.md`. The evidence state is a source-linked observation, not a human-entered conclusion about control, authorization, adequacy, or independence.

## Decision-right allocation

Allowed authority values are:

- `agent_authorized`
- `human_required`
- `separate_control_required`
- `dual_authority_required`
- `blocked_pending_evidence`
- `prohibited_for_agent`

| Decision right | Proposed actor | Evidence IDs | Policy / standing gate | Required authority | Transfer trigger |
|---|---|---|---|---|---|
| prepare | named preparer | E-001 | controlling local policy | blocked_pending_evidence | transfer or block when evidence is unknown, disputed, stale, or outside policy |
| recommend | named recommender | E-001 | controlling local policy | blocked_pending_evidence | transfer or block when evidence is unknown, disputed, stale, or outside policy |
| verify | named verifier | E-001 | controlling local policy | blocked_pending_evidence | transfer or block when required separation is absent or unresolved |
| validate | named validator | E-001 | controlling local policy | blocked_pending_evidence | transfer or block when intended-use fitness is unresolved |
| verdict | named decision maker | E-001 | controlling local policy | blocked_pending_evidence | transfer or block when verdict authority is absent or unresolved |
| accept | named acceptance owner | E-001 | controlling local policy | blocked_pending_evidence | transfer or block when residual uncertainty lacks an authorized owner |
| apply | named executor | E-001 | controlling local policy | blocked_pending_evidence | block before side effects until the exact action is authorized |
| reopen | named reopen authority | E-001 | controlling local policy | human_required | reopen when admitted evidence is invalidated, expires, or materially changes |
| close | named closure authority | E-001 | controlling local policy | blocked_pending_evidence | block closure until required effectiveness evidence is admitted |

`accept` and `apply` are separate rights. Nominal approval is not proof that the approver had the evidence, time, authority, or effective ability to stop or reverse the action.

## Derived authority result

- **Decision right evaluated:** apply
- **Result:** blocked_pending_evidence
- **Basis:** Evidence E-001 is unknown, so the proposed action is not cleared for application.
- **Derived by:** Replace with the validator/tool version or named policy evaluator.
- **Recorded at:** Replace with an ISO 8601 timestamp.

Allowed derived results are the six authority values above plus `indeterminate`.

A blocking result may override a less restrictive standing allocation. A non-blocking result must match the recorded `apply` authority.

## Reopen and closure controls

- **Reopen authority:** named owner
- **Reopen trigger:** Evidence invalidation, expiry, disputed provenance, changed action identity, failed monitoring, or ineffective correction.
- **Superseded decision handling:** Prior approval cannot be silently reused after a material action or evidence change.
- **Close authority:** named owner
- **Closure evidence:** Exact Evidence IDs required to demonstrate the recorded correction or effectiveness condition.
- **Interim expiry:** Replace with a timestamp or `not applicable` and a basis.

Reopening preserves the prior record and creates or identifies a successor decision episode. It does not rewrite the historical decision basis.

## Required links

- [Verification and evidence custody](verification.md)
- [Release decision, rollback, and monitoring](ship.md)
- Exact policy or standing-gate record: replace with a stable identifier or public URL.

## Exit criteria

- Every required decision right appears exactly once.
- Every referenced Evidence ID exists in `verification.md`.
- Unknown or disputed evidence does not clear `agent_authorized` application.
- Decisive self-check evidence does not clear `agent_authorized` application.
- Any `bounded_absence` identifies a finite scope and time boundary.
- The derived result is policy-consistent with the `apply` allocation or is a blocking override.
- Reopen and closure authorities and triggers are explicit.
- The placeholder marker has been removed.

## Source-lineage note

This template extends the repository's public evidence-custody and actor-authority model: https://github.com/FlyFission/nuclear-grade-context-engineering
