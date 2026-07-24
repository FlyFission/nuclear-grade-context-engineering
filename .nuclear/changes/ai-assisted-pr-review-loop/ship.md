# AI-Assisted PR Review Loop: Ship

## Release identity

- Change slug: ai-assisted-pr-review-loop
- Version / release / baseline: PR candidate based on `origin/main` 77f1645e9205c45c754a567fc5e0a3fcede52f0e
- PR / commit / artifact: branch `docs/minimum-assurance-loop`; commit and PR pending final freeze
- Owner: FlyFission
- Date: 2026-07-24
- Intended release window: After human PR review and green required checks

## Scope and exclusions

- Included: Existing public role diagram, compact Standard-mode PR explanation, correction budget fields, exact-candidate closure fields, contract test, changelog, and this packet.
- Excluded: New workflow mode, skill, command, validator behavior, model router, production deployment, merge, or release.
- Known non-goals: No claim that model diversity is independent validation or that this workflow creates formal assurance.

## Reviewed candidate identity

- Acceptance-criteria revision: `basis.md` dated 2026-07-24, REQ-001 through REQ-005
- Reviewed candidate commit / artifact hash: pending final implementation commit
- Current candidate commit / artifact hash: pending final implementation commit
- Candidate matches reviewed identity? no
- Material changes after verdict: No verdict has been issued; candidate remains open.
- Re-review status: pending
- Current verdict status: stale
- Verifier and evidence link: pending E-003 in `verification.md`

The packet deliberately marks the verdict stale until one exact committed candidate is reviewed and compared again before PR handoff. A pushed branch or PR number alone is not the candidate identity.

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
| Review / approval | gap | `verification.md` E-003 | Frozen semantic review and human PR decision pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Diagram may be more detailed than the simple external inspiration | Medium adoption friction | mitigate through frozen semantic review and human PR review | FlyFission | Review finding |
| Template fields are contract-tested for presence, not validator-enforced | Low; this PR makes no enforcement claim | accept as documented template behavior | FlyFission | Evidence of repeated omission |
| GitHub checks may reveal environment or render drift | Medium | block until green | FlyFission | Remote PR checks and rendered view |
| Candidate identity is not frozen yet | High for verdict use | block; record exact commit and renew review | FlyFission | Commit freeze |

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

- Operator/customer/support notes: PR body will explain the minimum assurance loop and exact-candidate stale-verdict rule.
- Docs/runbook updated: README, WORKFLOWS, canonical diagrams, Standard plan and ship templates.
- Communication needed: PR review only; no release announcement.
- Turnover record if activated: Not activated.
- Follow-up date: At PR review and after any base movement.

## Release decision

- Decision: defer
- Decision maker: FlyFission
- Rationale: The implementation candidate exists and all local gates are green, but frozen semantic review, exact commit identity, remote checks, and human PR review are not complete.
- Decision question answered by evidence? no
- Verdict owner's authority axis relative to the actor: separated; FlyFission owns the final PR decision while Hermes is the builder.
- Minimum coupling profile for this consequence met? no; E-003 and remote checks remain planned.
- Decision rests on primary evidence the reviewer can reproduce, not the actor's narrative? no; mechanical evidence is reproducible, semantic review remains open.
- Conditions attached: Complete full gates, freeze commit, close P0/P1 review findings, verify GitHub head and checks.
- Decision posture: conservative enough
- Abort or rollback trigger: Scope accretion, unresolved P0/P1, failed checks, malformed Mermaid, stale candidate identity, or public overclaim.
- OPEX or post-release learning trigger: User or reviewer finds the new lane harder to understand or sees stale-verdict ambiguity survive.

## Apply clearance

This PR makes no real-world deployment. Merge is the applicable controlled action and remains human-owned.

| Clearance check | Status | Notes |
|---|---|---|
| Required approvals present and current | no | Human PR review pending |
| Release / maintenance (freeze) window open | not applicable | No deployment window |
| External state unchanged since verification: verdict not stale | no | No current verdict; exact commit pending |
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
