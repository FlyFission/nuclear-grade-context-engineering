# Ship: Matt skill lifecycle and flow adaptation

## Scope and exclusions

- Included: lifecycle/invocation registry, routing scorer/scenarios, aggregate budgets, router preflight correction, compact skill pilot, workflow adapters/crosswalk, tests, docs, generated cards, and package parity.
- Excluded: merge, release, deployment, version publication, full-catalog compression, and claims of cross-host efficacy.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode |
| Basis and requirements | pass | `basis.md` | REQ-001 through REQ-009 |
| Implementation verification | pass | `verification.md` | full local gate and isolated wheel smoke passed |
| Evidence custody | partial | `verification.md` | local self-check recorded; provider review and GitHub CI pending |
| Review and approval | planned | PR | PR creation requests human review |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Live host routing is not deterministic CI evidence | static/scored cases may not generalize | defer and label honestly | maintainer | promotion/cross-host claim |
| Compact pilot evidence is scenario-specific | shorter bodies may miss uncommon branches | limit rollout to pilot | maintainer | broad compression proposal |
| Lifecycle registry adds a compatibility projection | future drift is possible | machine-enforce exact parity, designated Core router, and status-specific roots | maintainer | catalog change |
| Installer profile shrink requires reviewed cleanup | stale recognized directories remain discoverable until the operator removes them | fail closed before adoption; never auto-delete co-located host files | operator/maintainer | first post-upgrade run or profile shrink |
| PR review is not merge/release authorization | branch could be mistaken for accepted baseline | hold merge/release | maintainer | human review decision |

## Rollback / restore plan

- Revert the branch or individual commits before merge.
- No persistent runtime, data, credentials, or deployment state needs restoration.

## Monitoring and post-release checks

- Watch routing confusion, token-budget exceptions, projection drift, and beta/deprecated leakage in future PRs.
- Re-run live routing and compact-body evaluations before promoting new invocation behavior or broad compression.

## Release decision

- Decision: defer until verification and PR review.
- Decision maker: FlyFission maintainer.
- Rationale: implementation and review evidence are not yet complete.
- Decision question answered by evidence: no, pending.
- Conditions: full gate green, no unresolved P0/P1, remote PR head verified, human review before merge.
- Abort trigger: package parity loss, control deletion, misleading efficacy claim, or unresolved high-severity review finding.

## Apply clearance

- Clearance decision: hold.
- Cleared by: not yet applicable.
- Apply window: none; PR creation only.
- Re-clearance trigger: any material diff or base change after frozen review.

## Baseline trigger

- Baseline required: yes if merged.
- Baseline record: merged commit and finalized packet.
- Revalidation trigger: skill addition/status change, invocation-policy change, host packaging change, routing-scenario change, or compact-contract rollout.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`

## Exit criteria

- PR readiness is separated from merge/release readiness.
- Residual evidence limits remain visible.
- Human review is requested rather than inferred.

## Source-lineage note

This ship record governs PR readiness only under the public boundary disciplines mapped in `docs/00-standards-foundation/source-map.md`. It makes no compliance, formal assurance, safety, security, certification, or efficacy claim.
