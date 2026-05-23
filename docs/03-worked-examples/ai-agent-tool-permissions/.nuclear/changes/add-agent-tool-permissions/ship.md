# Ship — Add Agent Tool Permissions

**Purpose:** Make the worked-example v0 release decision explicit.

---

## Release identity

- **Change slug:** `add-agent-tool-permissions`
- **Version / release / baseline:** Worked example v0 in repository baseline
- **PR / commit / artifact:** Files under `docs/03-worked-examples/ai-agent-tool-permissions/`
- **Owner:** Nuclear-grade example maintainer
- **Date:** 2026-05-17
- **Intended release window:** Public v0 after launch-readiness verification.

## Scope and exclusions

- **Included:** C-001 workspace-only file-write guard, C-004a denied-write in-memory audit event, packet docs, tests, and launch-doc references.
- **Excluded:** Production sandbox, external API tool registry, scoped credentials, human approval gate, persistent audit log, multi-tenant runtime, Windows-specific validation, TOCTOU hardening.
- **Known non-goals:** Formal compliance package, certification artifact, QA program, regulator-facing submittal, security guarantee for production deployment.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified; Nuclear extension not activated. |
| Basis / requirements / claims | pass | `basis.md` | Protected/unacceptable outcomes stated for C-001. |
| Trace | pass | `trace.md` | C-001 complete; C-002/C-003 deferred. |
| Verification | pass | `verification.md` | Four C-001 tests passing. |
| Dependency / supply-chain evidence | not applicable | `basis.md` | Standard library only for reference implementation; pytest for tests. |
| AI-assisted work checks | pass | `verification.md` | Scope and tool actions recorded. |
| Review / approval | pass | `adversarial-review.md` | Lightweight adversarial review completed for educational v0. |
| Validator | pass | `tools/ng_validate.py` | Packet passes the v0 validator. |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Reference guard is not a production sandbox. | Users may over-apply the example. | mitigate with scope warnings and README/Quickstart language. | Maintainer | Any production reuse language. |
| Windows/path-platform edge cases not separately tested. | Cross-platform claim would be overbroad. | accept for WSL/Linux example; add tests before cross-platform claim. | Maintainer | Windows support claim. |
| TOCTOU and concurrent filesystem attacks not covered. | Production adversary could exploit timing or FS semantics. | defer; explicitly out of v0. | Maintainer | Production/multi-user deployment. |
| C-002/C-003 not implemented. | Tool/API and approval claims remain unproven. | defer and mark in trace. | Maintainer | Expansion beyond C-001. |
| Persistent audit not implemented. | Operational review would be weak in real service. | defer; in-memory audit proves concept only. | Maintainer | Any real runtime or incident workflow. |

## Rollback / restore plan

- **Rollback method:** Revert/remove the example packet, tests, and reference implementation from the docs tree; no production service state exists.
- **Data migration reversal or restore notes:** Not applicable.
- **Feature flag / kill switch:** Not applicable for docs/example v0.
- **Owner on call:** Maintainer.
- **Time to restore estimate:** Less than 15 minutes for local file revert before commit.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Validator result | Packet passes required-section/status/prohibited-language checks. | Maintainer | `python tools/ng_validate.py ...` | Fix packet before launch. |
| Reader confusion / overclaim risk | Any issue/comment suggesting this is compliance/certification or production sandbox. | Maintainer | GitHub issues/reviews after launch. | Patch README and disclaimers. |
| C-001 test suite | Four tests pass. | Maintainer | Local/CI pytest output. | Block launch until fixed. |

## Handoff

- **Operator/customer/support notes:** This is a teaching example, not a production permission system.
- **Docs/runbook updated:** README and Quickstart link to the worked example and validator command.
- **Communication needed:** Explain that Nuclear-grade proves bounded claims, not vibes.
- **Follow-up date:** Next repo pass after user review.

## Release decision

- **Decision:** ship with residual risk after launch-readiness verification.
- **Decision maker:** Maintainer.
- **Rationale:** C-001 has enough evidence for an educational worked example; remaining broader claims are visibly deferred.
- **Conditions attached:** Do not claim production sandboxing, cross-platform security, formal compliance, or completion of C-002/C-003.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- PR/commit/release artifact: repository files under `docs/03-worked-examples/ai-agent-tool-permissions/`
- Monitoring/dashboard/log query: validator/test commands for v0
- Rollback/runbook: revert/remove the worked-example files if public-v0 review finds a blocking issue

## Exit criteria

- Release decision is explicit.
- Evidence status and gaps are visible.
- Rollback/restore path exists or the lack is consciously accepted.
- Monitoring/handoff covers the claims most likely to fail in operation.
- Any accepted residual risk has an owner and recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public configuration-management, release-readiness, secure-development, software-assurance, supply-chain, lifecycle, and operating-learning concepts mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
