# Decision Authority Record

## Decision episode

- **Decision ID:** DEC-001
- **Candidate / action:** Open branch `feat/matt-skill-lifecycle-and-flow` as a pull request for maintainer review; do not merge or release.
- **Policy version:** repository `AGENTS.md` at pre-change baseline `3ade94ee994f727098a90ee7c5b69c157b107ddf`.
- **Policy authority ID:** FlyFission repository maintainer.
- **Policy custodian:** FlyFission repository maintainer.
- **Policy digest:** sha256:9811ff4ed1f099de2965410992ec3d85675ba8fcd6dc1998f5830f313efcc68c
- **Policy valid through:** not applicable: the repository policy has no declared expiry; a content or baseline change triggers revalidation.
- **Action identity:** pull-request candidate on branch `feat/matt-skill-lifecycle-and-flow` based on `3ade94ee994f727098a90ee7c5b69c157b107ddf`.
- **Decision status:** blocked pending evidence
- **Reversible:** yes; the unmerged branch or commits can be closed or reverted without runtime state migration.
- **Consequence if wrong:** an incomplete lifecycle or routing contract could be presented for review or merged into distributed agent guidance.

## Evidence basis

| Evidence ID | Raw state | Scope / basis | Intended use / V&V status | Custody / profile link |
|---|---|---|---|---|
| E-001 | observed | Router contract test on the local candidate, 2026-08-05 | Local deterministic proof for PR readiness; not formal V&V | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |

## Decision-right allocation

| Decision right | Proposed actor | Evidence IDs | Evidence-basis authority | Policy / standing gate | Required authority | Transfer trigger |
|---|---|---|---|---|---|---|
| prepare | implementing agent | not applicable | FlyFission maintainer | explicit request permits branch and PR preparation | agent_permitted | transfer when preparation changes merge/release state |
| recommend | provider-diverse review chair | E-001 | FlyFission maintainer | review findings are advisory | agent_permitted | transfer when recommendation contains a material tradeoff or unresolved P0/P1 |
| verify | deterministic tools and commissioned reviewers | E-001 | FlyFission maintainer | recorded commands and frozen diff | separate_control_required | block when required checks or review seats are absent |
| validate | repository validator and CI | E-001 | FlyFission maintainer | structural validation only | separate_control_required | block when validation fails or candidate identity changes |
| verdict | FlyFission maintainer | E-001 | FlyFission maintainer | human PR review | human_required | retain with maintainer until review is complete |
| accept | FlyFission maintainer | E-001 | FlyFission maintainer | merge/release authority is not delegated | human_required | no agent transfer |
| apply | FlyFission maintainer | E-001 | FlyFission maintainer | merge/release authority is not delegated | human_required | block before merge or release without maintainer action |
| reopen | FlyFission maintainer | not applicable | FlyFission maintainer | evidence invalidation or candidate change | human_required | reopen on changed diff, base, evidence, or policy |
| close | FlyFission maintainer | E-001 | FlyFission maintainer | PR/packet closure requires maintainer disposition | human_required | block closure while review findings remain unresolved |

## Derived authority result

- **Decision right evaluated:** apply
- **Result:** human_required
- **Basis:** The agent may prepare and recommend the PR, but the repository policy and explicit task retain merge and release authority with the FlyFission maintainer.
- **Derived by:** `nuclear_grade.ng_validate` structural policy record.
- **Recorded at:** 2026-08-05T22:00:00Z

## Reopen and closure controls

- **Reopen authority:** FlyFission maintainer.
- **Reopen trigger:** Evidence invalidation, changed diff or base, failed CI, disputed provenance, changed policy, or a new P0/P1 finding.
- **Superseded decision handling:** Preserve this episode and create a successor; do not silently reuse it after a material change.
- **Close authority:** FlyFission maintainer.
- **Closure evidence:** E-001, plus the final local gate, review disposition, and CI state linked from `verification.md`.
- **Interim expiry:** not applicable: any candidate, policy, or evidence change triggers revalidation instead of time-based expiry.

## Required links

- [Verification and evidence custody](verification.md)
- [Release decision, rollback, and monitoring](ship.md)
- Controlling policy: repository `AGENTS.md` at baseline `3ade94ee994f727098a90ee7c5b69c157b107ddf`.

## Exit criteria

- Every decision right appears exactly once.
- The PR may be prepared and recommended without granting merge or release authority.
- Referenced evidence exists in `verification.md`.
- Candidate, policy, and evidence changes trigger revalidation.

## Source-lineage note

This record applies the repository's public authority and evidence-custody model described in `docs/00-standards-foundation/source-map.md`. It is a structural software record, not formal authorization, assurance, or compliance.
