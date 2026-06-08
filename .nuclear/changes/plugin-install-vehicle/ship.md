# Standard Ship

**Purpose:** State the release decision for the plugin install vehicle.

---

## Release identity

- Change slug: plugin-install-vehicle
- Version / release / baseline: plugin manifest v0.5.0 (tracks `pyproject`)
- PR / commit / artifact: this branch's PR
- Owner: FlyFission
- Date: 2026-06-08
- Intended release window: with this PR merge

## Scope and exclusions

- Included: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, the packaging test, and the INSTALL.md + README install updates.
- Excluded: executable hooks, SessionStart/PreToolUse behavior, the `ng` CLI, skill/command bodies.
- Known non-goals: any enforcement or runtime behavior (a later tier).

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard justified |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..004 |
| Questioning attitude | pass | `risk.md` | captured inline |
| Verification | pass (one deferred) | `verification.md` | live install deferred |
| Dependency / supply-chain evidence | not applicable | this packet | no new dependency; no auto-run hooks configured |
| AI-assisted work checks | pass | `verification.md` | schema verified vs official docs |
| Review / approval | planned | the PR | maintainer review pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Live `/plugin install` not exercised in CI | Install could fail on a real surface despite valid schema | defer | FlyFission | Maintainer runs the documented install once |
| `source: "./"` edge case for URL-added marketplaces | Relative-path installs fail if a marketplace is added by direct URL | accept | FlyFission | If adopters report URL-add failures, document git-add as the supported path |

## Rollback / restore plan

- Rollback method: delete `.claude-plugin/` and revert the doc edits (single revert).
- Data migration reversal or restore notes: none (no state, no migration).
- Feature flag / kill switch: removing `marketplace.json` removes the install path.
- Owner on call: FlyFission
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| First live `/plugin install` | Installs cleanly; skills + commands appear | FlyFission | Claude Code session | Fix manifest; patch release |
| Adopter install reports | No install-failure reports | FlyFission | GitHub issues | Triage; document the supported add path |

## Handoff

- Operator/customer/support notes: install via `/plugin marketplace add FlyFission/nuclear-grade-context-engineering` then `/plugin install nuclear-grade@nuclear-grade`.
- Docs/runbook updated: INSTALL.md + README.
- Communication needed: note the plugin in release notes when the next version is cut.
- Turnover record if activated: not activated.
- Follow-up date: at the next release.

## Release decision

- Decision: ship with residual risk
- Decision maker: FlyFission
- Rationale: manifests are schema-correct and structurally verified; the only unproven step (the live install) is low-risk, reversible, and deferred to a maintainer smoke-test.
- Decision question answered by evidence? yes for schema/structure/version/docs; the live install is the named residual.
- Conditions attached: maintainer runs the documented install once before announcing.
- Decision posture: conservative enough.
- Abort or rollback trigger: live install fails -> revert `.claude-plugin/`.
- OPEX or post-release learning trigger: any install-failure report updates the install docs / manifest.

## Baseline trigger

- Baseline required? yes
- Baseline record: the plugin manifest (version tracks `pyproject`) becomes a controlled item.
- Revalidation trigger: a Claude Code plugin schema change, or a `pyproject` version bump.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this branch's PR.
- Monitoring/dashboard/log query: GitHub issues for install reports.
- Rollback/runbook: delete `.claude-plugin/`.

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

Original Nuclear-grade record inspired by public ideas on configuration management, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
