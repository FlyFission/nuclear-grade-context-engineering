# Actor-Evidence Independence — Ship

## Purpose

State the release decision for the amendment.

## Evidence status summary

| Evidence area | Status | Notes |
|---|---|---|
| Doctrine and boundary (REQ-001) | gap | Framing reviewed by the actor; correctness pending human review |
| Wiring across the loop (REQ-002) | pass | Reproducible grep |
| Operational hooks and posture (REQ-003) | pass | Template fields present; check kept as a disclosure |
| No regressions (REQ-004) | pass | pytest, ruff, doctor, tokens, packet validators all green |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner |
|---|---|---|---|
| The doctrine's framing may be incomplete or wrong | Medium — it is the method's core claim | Defer to independent human review before merge | FlyFission |
| Independence is disclosed, not enforced by tooling | Low — by design; stated honestly | Accept; enforcement stays human plus out-of-band CI | FlyFission |

## Rollback / restore plan

- Rollback method: revert the branch; all changes are documentation and templates under normal git history.
- Owner on call: FlyFission.
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Expected behavior | Action if bad |
|---|---|---|
| Contract tests on `main` | stay green after merge | revert or fix forward |
| Adopter feedback on the doctrine | the seam is understood and used | refine the wording |

## Release decision

- Decision: defer — ship pending independent human review.
- Decision maker: FlyFission (human reviewer).
- Rationale: The actor authored both the change and this record; per the principle the change introduces, the actor does not self-certify the merge of a trust-bearing change. The mechanical evidence (tests, grep) is reproducible and green; the judgment that the doctrine closes the gap is the reviewer's.
- Decider independent of the actor that produced the change? no — which is exactly why the decision is deferred to a human.
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes for the mechanical claims; the correctness judgment is the reviewer's.
- Abort or rollback trigger: a reviewer finds the framing unsound or inconsistent.

## Baseline trigger

- Baseline required? yes — on human acceptance, this becomes the method's stated defense against persuasive documentation.
- Revalidation trigger: a future change to the loop's gates or the PROVE subagents.

## Required links

- Risk: `risk.md`
- Verification: `verification.md`
- Doctrine: `../../../docs/02-operating-system/actor-evidence-independence.md`

## Exit criteria

- The release decision is stated plainly (defer to human review).
- The residual risks are owned.
- A rollback path exists.
- The independence posture of the decision is disclosed.

## Source-lineage note

Original Nuclear-grade packet inspired by public release-readiness, configuration-management, and software-assurance ideas mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
