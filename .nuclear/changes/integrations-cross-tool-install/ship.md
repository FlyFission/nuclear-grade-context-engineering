# Standard Ship Record

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

**Activation threshold:** Use when a Standard change is merged or released, when the release stance changes, or when users, operations, dependencies, security, data, or AI power are affected.

**Minimum useful version:** the evidence status, the leftover risks, the rollback/restore plan, the monitoring, the handoff, the release decision, and the baseline trigger.

**Overhead trap:** Do not treat a green CI run as release readiness. Ship when the evidence matches the claims and the operational controls are ready.

---

## Release identity

- Change slug: integrations-cross-tool-install
- Version / release / baseline: 0.6.0 (mirrors `pyproject`, both plugin manifests, `nuclear-grade.yaml`, `CITATION.cff`)
- PR / commit / artifact: PR #42 on branch `claude/loving-ride-sgg6ww`
- Owner: FlyFission (Ben Huffer)
- Date: 2026-06-16
- Intended release window: when PR #42 is reviewed and merged.

## Scope and exclusions

- Included: `ng install`, `ng mcp-config`, `install.sh`, `.codex-plugin`, the optional MCP server, docs, and the version bump.
- Excluded: any always-on hooks; any base-install dependency; submission to external plugin directories.
- Known non-goals: no change to existing CLI commands, templates, or methodology.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard, justified by the optional dependency |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..004 |
| Questioning attitude | pass | `risk.md` | captured inline |
| Verification | pass | `verification.md` | suite, lint, doctor, MCP smoke |
| Dependency / supply-chain evidence | pass | `verification.md` | `mcp` optional; base zero-dep |
| AI-assisted work checks | pass | `verification.md` | scope and screening recorded |
| Review / approval | planned | PR #42 | awaiting human review |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| VS Code user-scope path is best-known, not doc-confirmed | a wrong user path mislocates skills | accept | FlyFission | VS Code documents the user path |
| Codex self-serve plugin directory is still rolling out | no official listing yet | defer | FlyFission | OpenAI opens self-serve publishing |

## Rollback / restore plan

- Rollback method: revert the PR #42 commits; the change is additive.
- Data migration reversal or restore notes: none; no data or state is created.
- Feature flag / kill switch: the MCP server is gated behind the optional `mcp` extra.
- Owner on call: FlyFission.
- Time to restore estimate: minutes (a single revert).

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI on PR #42 | all checks green | FlyFission | GitHub Actions | re-diagnose and fix forward |
| User path reports | installs land in the documented dir | FlyFission | issues / discussions | correct the path or document `--dest` |

## Handoff

- Operator/customer/support notes: `INTEGRATIONS.md` documents per-tool install and the opt-in MCP server.
- Docs/runbook updated: `INSTALL.md`, `INTEGRATIONS.md`, `CHANGELOG.md`.
- Communication needed: PR #42 description summarizes the change.
- Turnover record if activated: not applicable.
- Follow-up date: when PR #42 merges.

## Release decision

- Decision: ship with residual risk
- Decision maker: FlyFission (on PR #42 review)
- Rationale: additive, reversible, locally checkable; the two residual items are accepted/deferred and flagged at runtime.
- Decision question answered by evidence? yes
- Conditions attached: human review approves PR #42 and CI is green.
- Decision posture: conservative enough.
- Abort or rollback trigger: a CI failure that is a real defect, or a confirmed wrong tool path with no override.
- OPEX or post-release learning trigger: a user reports skills landing in the wrong directory.

## Baseline trigger

- Baseline required? yes
- Baseline record: the 0.6.0 tag/release once PR #42 merges.
- Revalidation trigger: a future change to the install paths or the MCP surface.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: PR #42
- Monitoring/dashboard/log query: GitHub Actions on PR #42
- Rollback/runbook: revert PR #42

## Exit criteria

- The release decision is stated plainly.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on keeping the approved version under control (CM), release readiness, secure development, software assurance, supply-chain risk, software lifecycle, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
