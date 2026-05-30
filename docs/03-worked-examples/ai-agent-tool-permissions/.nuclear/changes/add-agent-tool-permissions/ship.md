# Ship — Add Agent Tool Permissions

**Purpose:** State the worked-example v0 release decision plainly.

---

## Release identity

- **Change slug:** `add-agent-tool-permissions`
- **Version / release / baseline:** Worked example v0 in repository baseline
- **PR / commit / artifact:** Files under `docs/03-worked-examples/ai-agent-tool-permissions/`
- **Owner:** Nuclear-grade example maintainer
- **Date:** 2026-05-17
- **Intended release window:** Public v0 after the launch-readiness check.

## Scope and exclusions

- **Included:** the C-001 workspace-only file-write guard, the C-004a in-memory audit event for denied writes, the packet docs, the tests, and the launch-doc links.
- **Excluded:** a production sandbox, an external API tool list, scoped credentials, a human approval gate, a lasting audit log, a multi-tenant runtime, Windows-specific testing, and TOCTOU hardening.
- **Known non-goals:** a formal compliance package, a certification artifact, a QA program, a regulator-facing submittal, or a security guarantee for production use.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified; Nuclear extension not turned on. |
| Basis / requirements / claims | pass | `basis.md` | The protected outcomes and outcomes to prevent are stated for C-001. |
| Trace | pass | `trace.md` | C-001 complete; C-002 and C-003 deferred. |
| Verification | pass | `verification.md` | Four C-001 tests pass. |
| Dependency / supply-chain evidence | not applicable | `basis.md` | The sample code uses the standard library only; tests use pytest. |
| AI-assisted work checks | pass | `verification.md` | The scope and the tool actions are recorded. |
| Review / approval | pass | `adversarial-review.md` | A light attack review was done for teaching v0. |
| Validator | pass | `tools/ng_validate.py` | The packet passes the v0 validator. |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| The sample guard is not a production sandbox. | Users may stretch the example too far. | mitigate with scope warnings and README/Quickstart wording. | Maintainer | Any wording about production reuse. |
| Windows and other platform path cases not tested on their own. | A cross-platform claim would reach too far. | accept for the WSL/Linux example; add tests before any cross-platform claim. | Maintainer | A Windows-support claim. |
| TOCTOU and concurrent filesystem attacks not covered. | A production attacker could abuse timing or filesystem rules. | defer; clearly out of v0. | Maintainer | Production or multi-user deployment. |
| C-002 and C-003 not built. | The tool, API, and approval claims stay unproven. | defer and mark them in trace. | Maintainer | Any work beyond C-001. |
| No lasting audit log yet. | Operational review would be weak in a real service. | defer; the in-memory audit only proves the idea. | Maintainer | Any real runtime or incident workflow. |

## Rollback / restore plan

- **Rollback method:** revert or remove the example packet, tests, and sample code from the docs tree. No production service state exists.
- **Data migration reversal or restore notes:** not applicable.
- **Feature flag / kill switch:** not applicable for docs/example v0.
- **Owner on call:** Maintainer.
- **Time to restore estimate:** under 15 minutes to revert local files before commit.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Validator result | The packet passes the required-section, status, and banned-language checks. | Maintainer | `python tools/ng_validate.py ...` | Fix the packet before launch. |
| Reader confusion / overclaim risk | Any issue or comment that reads this as compliance, certification, or a production sandbox. | Maintainer | GitHub issues and reviews after launch. | Patch the README and disclaimers. |
| C-001 test suite | Four tests pass. | Maintainer | Local or CI pytest output. | Block launch until fixed. |

## Handoff

- **Operator/customer/support notes:** this is a teaching example, not a production permission system.
- **Docs/runbook updated:** the README and Quickstart link to the worked example and the validator command.
- **Communication needed:** explain that Nuclear-grade proves narrow, bounded claims, not vibes.
- **Follow-up date:** the next repo pass after user review.

## Release decision

- **Decision:** ship with leftover risk, after the launch-readiness check.
- **Decision maker:** Maintainer.
- **Rationale:** C-001 has enough evidence for a teaching worked example, and the broader claims are clearly deferred.
- **Conditions attached:** do not claim production sandboxing, cross-platform security, formal compliance, or that C-002 and C-003 are done.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- PR/commit/release artifact: repository files under `docs/03-worked-examples/ai-agent-tool-permissions/`
- Monitoring/dashboard/log query: the validator and test commands for v0
- Rollback/runbook: revert or remove the worked-example files if the public-v0 review finds a blocking issue

## Exit criteria

- The release decision is stated plainly.
- The evidence status and the gaps are visible.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade ship record inspired by public ideas on keeping the approved version under control (CM), release readiness, secure development, software assurance, supply-chain risk, software lifecycle, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
