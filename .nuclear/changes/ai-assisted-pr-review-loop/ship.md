# AI-Assisted PR Review Loop: Ship

## Release identity

- Change slug: ai-assisted-pr-review-loop
- Version / release / baseline: PR candidate based on `origin/main` 77f1645e9205c45c754a567fc5e0a3fcede52f0e
- PR / commit / artifact: branch `docs/minimum-assurance-loop`; first reviewed commit `2bc9c005b8a796afae1857500d1f27573f754c43`; corrected payload first introduced at `6cc462a422a00907c836b256aaa0e3c6fd5428ea`; final attestation is an excluded packet-only follow-up
- Owner: FlyFission
- Date: 2026-07-24
- Intended release window: After human PR review and green required checks

## Scope and exclusions

- Included: Existing public role diagram, compact Standard-mode PR explanation, correction budget fields, exact-candidate closure fields, contract test, changelog, and this packet.
- Excluded: New workflow mode, skill, command, validator behavior, model router, production deployment, merge, or release.
- Known non-goals: No claim that model diversity is independent validation or that this workflow creates formal assurance.

## Reviewed candidate identity

- Identity method and attestation location: SHA-256 manifest over the public/template/test payload; provenance commit recorded separately; attestation lives in this excluded packet and PR review.
- Identity scope and exclusions: Seven controlled payload files named in `plan.md`; exclude `.nuclear/changes/ai-assisted-pr-review-loop/` so the decision record does not identify itself.
- Superseded first-round payload / provenance: SHA-256 `5bdc1044d2be0ea061690a21ea744543359fd8b3ae93d3041b21aa80e543572d` at `2bc9c005b8a796afae1857500d1f27573f754c43`
- Reviewed payload / content identity: SHA-256 `3d6270a98cafe28cc44fe90a88222c5a7c9a24eb90375bbd5ad38086bc655950`
- Reviewed provenance identity: `6cc462a422a00907c836b256aaa0e3c6fd5428ea`
- Current payload / content identity: SHA-256 `3d6270a98cafe28cc44fe90a88222c5a7c9a24eb90375bbd5ad38086bc655950` for the corrected seven-file payload
- Current provenance identity: corrected payload first introduced at `6cc462a422a00907c836b256aaa0e3c6fd5428ea`; final PR head will add only this excluded attestation packet
- Payload identity matches reviewed identity? yes
- Base / provenance impact check: Base remains `77f1645e9205c45c754a567fc5e0a3fcede52f0e`; the packet-only attestation follow-up does not alter scoped requirements, dependencies, admitted payload evidence, or applicability.
- Material changes after verdict: Role taxonomy unified; diagram simplified; record authority corrected; correction-to-reverification and budget exhaustion made explicit; identity method made non-recursive; delta-review fields and exact mirror test added.
- Delta review evidence: `reviews/payload-manifest-round-1.txt` and `reviews/corrected-delta-adjudication.md`
- Re-review status: delta review complete
- Current verdict status: current
- Verifier and evidence link: E-003 first-round reviews and E-004 corrected-candidate closure in `verification.md`

The first-round verdict became stale after material corrections. The corrected seven-file payload is now frozen, locally reverified, and accepted by the counted delta reviewer. This excluded attestation update does not change that payload and does not ask an in-tree file to contain its own commit SHA.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode is proportionate |
| Basis / requirements / claims | pass | `basis.md` | Five bounded requirements |
| Questioning attitude | pass | `risk.md` | Summary captures decision-changing evidence and stop conditions |
| Verification | pass | `verification.md` | Focused and full local gates pass; remote GitHub checks remain PR-time evidence |
| Dependency / supply-chain evidence | not applicable | `risk.md` | No dependency change |
| AI-assisted work checks | pass | `verification.md` | Scope and authority disclosed |
| Evidence custody / coupling profile | pass | `verification.md` | Actor coupling disclosed; planned separated checks not inflated |
| Review / approval | pass with open human gate | `verification.md` E-003 and E-004 | Corrected-candidate review has no unresolved P0/P1; human PR decision remains pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Corrected diagram may still be too dense | Medium adoption friction | local delta review accepted; inspect GitHub render before merge | FlyFission | Rendered PR view |
| Template fields are contract-tested for presence, not validator-enforced | Low; this PR makes no enforcement claim | accept as documented template behavior | FlyFission | Evidence of repeated omission |
| GitHub checks may reveal environment or render drift | Medium | block until green | FlyFission | Remote PR checks and rendered view |
| Packet-only attestation commit is outside reviewed payload | Low chronology risk | record final PR head in remote/PR evidence and confirm scoped digest unchanged | FlyFission | Push or rebase |

## Rollback / restore plan

- Rollback method: Close the unmerged PR or revert the candidate commit after merge.
- Data migration reversal or restore notes: Not applicable.
- Feature flag / kill switch: Not applicable.
- Owner on call: FlyFission.
- Time to restore estimate: Minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Public-doc and full test suites | Green on PR and main | FlyFission | GitHub Actions | Hold, revert, or fix forward |
| Mermaid rendering | Sequence diagram renders legibly | FlyFission | GitHub README and docs page | Correct source and renew review |
| Template adoption feedback | Fields improve closure without routine ceremony | FlyFission | Issues/discussions and future packets | Narrow or conditionally activate wording |
| Review-loop behavior | Teams escalate at budget rather than lower criteria | FlyFission | OPEX records | Update guidance and tests |

## Handoff

- Operator/customer/support notes: PR body will explain the compact Standard loop and exact-candidate stale-verdict rule.
- Docs/runbook updated: README, WORKFLOWS, canonical diagrams, Standard plan and ship templates.
- Communication needed: PR review only; no release announcement.
- Turnover record if activated: Not activated.
- Follow-up date: At PR review and after any base movement.

## Release decision

- Decision: defer
- Decision maker: FlyFission
- Rationale: Three blind first-round reviews found material role, agency, identity-recursion, re-verification, and operability defects. Correction round 1 closed them; the exact corrected payload passed local gates and a counted Codex delta review with no unresolved P0/P1. Remote checks, rendered Mermaid inspection, and human PR review are not complete.
- Decision question answered by evidence? no
- Verdict owner's authority axis relative to the actor: separated; FlyFission owns the final PR decision while Hermes is the builder.
- Minimum coupling profile for this consequence met? yes for local PR handoff; remote checks and the human decision remain open by design.
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? yes for the local payload; Codex independently recomputed its digest and inspected the exact commit.
- Conditions attached: Verify final remote head, unchanged scoped payload digest, green GitHub checks, legible Mermaid render, and human PR review.
- Decision posture: conservative enough
- Abort or rollback trigger: Scope accretion, unresolved P0/P1, failed checks, malformed Mermaid, stale candidate identity, or public overclaim.
- OPEX or post-release learning trigger: User or reviewer finds the new lane harder to understand or sees stale-verdict ambiguity survive.

## Apply clearance

This PR makes no real-world deployment. Merge is the applicable controlled action and remains human-owned.

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | no | Human PR review pending |
| Release / maintenance (freeze) window open | not applicable | No deployment window |
| External state unchanged since verification: verdict not stale | yes | Current scoped payload digest matches the reviewed digest; packet-only attestation is excluded and impact-checked |
| Deployment policy satisfied | not applicable | No deployment |
| Rollback / kill-switch confirmed ready at apply-time | yes | Git revert/PR closure available |

- Clearance decision: hold
- Cleared by: FlyFission after PR review
- Apply window / valid until: Not open
- Re-clearance trigger: Any candidate or base change after review requires identity comparison and affected re-review.

## Baseline trigger

- Baseline required? yes
- Baseline record: Merge commit or preserved PR commit after human acceptance
- Revalidation trigger: Any change to role semantics, candidate identity fields, correction-budget rules, or the Standard release decision path

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: pending
- Monitoring/dashboard/log query: GitHub Actions and repository tests
- Rollback/runbook: git revert or close PR

## Exit criteria

- Exact reviewed and current candidate IDs match.
- Full local and remote checks are green or any absence is disclosed.
- No unresolved P0/P1 remains.
- Human PR review owns merge; no model verdict is treated as authorization.
- Residual risks remain bounded, owned, and linked.

## Source-lineage note

This ship record is an original use of the Nuclear-grade release-readiness pattern whose public lineage is mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal V&V, compliance, certification, safety, security, regulatory adequacy, or release authorization beyond the named human decision.
