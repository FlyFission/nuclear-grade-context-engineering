# Decision Authority Record

## Decision episode

- **Decision ID:** DEC-001
- **Candidate / action:** Prepare and open branch `feat/inspectable-builder-critic-loop` as a draft stacked pull request against `feat/matt-skill-lifecycle-and-flow`; do not merge or release.
- **Policy version:** repository `AGENTS.md` at base `afcc9c5ad737d9919b9887b69ee1cb1eb2b5ee51`.
- **Policy authority ID:** FlyFission repository maintainer.
- **Policy custodian:** FlyFission repository maintainer.
- **Policy digest:** sha256:9811ff4ed1f099de2965410992ec3d85675ba8fcd6dc1998f5830f313efcc68c
- **Policy valid through:** not applicable: the repository policy has no declared expiry; a content, base, or authority change triggers revalidation.
- **Action identity:** follow-up candidate based on PR #98 head `afcc9c5ad737d9919b9887b69ee1cb1eb2b5ee51`.
- **Decision status:** blocked pending evidence
- **Reversible:** yes; the unmerged branch or commit can be closed or reverted without runtime state migration.
- **Consequence if wrong:** public agent guidance could weaken evidence custody, duplicate the lifecycle, or imply unsupported efficacy/independence.

## Evidence basis

| Evidence ID | Raw state | Scope / basis | Intended use / V&V status | Custody / profile link |
|---|---|---|---|---|
| E-001 | observed | RED/GREEN public and command-parity tests on the local candidate, 2026-08-06 | Local deterministic proof for PR preparation; not formal V&V | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |
| E-002 | observed | adversarial transfer review and source inspection | Advisory defect discovery; not independent human validation | [verification.md custody profile](verification.md#evidence-custody-and-coupling) |

## Decision-right allocation

| Decision right | Proposed actor | Evidence IDs | Evidence-basis authority | Policy / standing gate | Required authority | Transfer trigger |
|---|---|---|---|---|---|---|
| prepare | implementing agent | E-001 | FlyFission maintainer | explicit request permits branch and PR preparation | agent_permitted | transfer when preparation changes merge/release state |
| recommend | implementing agent plus advisory reviewer | E-001 | FlyFission maintainer | recommendations preserve dissent and evidence limits | agent_permitted | transfer on material tradeoff or unresolved P0/P1 |
| verify | deterministic tools and fresh reviewer | E-001 | FlyFission maintainer | exact diff and project commands | separate_control_required | block when required checks or review are absent |
| validate | repository validator and CI | E-001 | FlyFission maintainer | structural validation only | separate_control_required | block on failure or candidate identity change |
| verdict | FlyFission maintainer | E-001 | FlyFission maintainer | human PR review | human_required | retain until review is complete |
| accept | FlyFission maintainer | E-001 | FlyFission maintainer | merge and later pilot authority are not delegated | human_required | no agent transfer |
| apply | FlyFission maintainer | E-001 | FlyFission maintainer | merge/release authority is not delegated | human_required | block before merge/release without maintainer action |
| reopen | FlyFission maintainer | not applicable | FlyFission maintainer | evidence invalidation, base change, or new finding | human_required | reopen on changed diff/base/evidence/policy |
| close | FlyFission maintainer | E-001 | FlyFission maintainer | packet/PR closure needs maintainer disposition | human_required | block while findings remain unresolved |

## Derived authority result

- **Decision right evaluated:** apply
- **Result:** human_required
- **Basis:** The agent may prepare and recommend a draft stacked PR. The maintainer retains merge, release, live pilot, and skill-promotion authority.
- **Derived by:** `nuclear_grade.ng_validate` structural policy record.
- **Recorded at:** 2026-08-06T09:02:12-04:00

## Reopen and closure controls

- **Reopen authority:** FlyFission maintainer.
- **Reopen trigger:** changed diff/base, failed CI, invalidated source/evidence, changed policy, or new P0/P1.
- **Superseded decision handling:** preserve this episode and create a successor after material change.
- **Close authority:** FlyFission maintainer.
- **Closure evidence:** E-001 and E-002 plus final full gates, review disposition, and CI linked from `verification.md`.
- **Interim expiry:** candidate, base, policy, or evidence change triggers revalidation.

## Required links

- [Verification and evidence custody](verification.md)
- [Release decision, rollback, and monitoring](ship.md)
- Controlling policy: repository `AGENTS.md` at base `afcc9c5ad737d9919b9887b69ee1cb1eb2b5ee51`.
- Source boundary: `docs/00-standards-foundation/source-map.md`.

## Exit criteria

- Every decision right appears exactly once.
- Draft PR preparation does not grant merge, release, pilot, or promotion authority.
- Referenced evidence exists and candidate changes trigger revalidation.

## Source-lineage note

This record applies the public authority/evidence model mapped in `docs/00-standards-foundation/source-map.md`. It is a structural software record, not formal authorization, assurance, efficacy evidence, or compliance.
