# Standard Ship

**Purpose:** State the release decision for the CI-scaffold generator.

---

## Release identity

- Change slug: ci-scaffold-generator
- Version / release / baseline: `ng scaffold-ci` (the rung-4 gate generator)
- PR / commit / artifact: this branch's PR
- Owner: FlyFission
- Date: 2026-06-08
- Intended release window: with this PR merge

## Scope and exclusions

- Included: the `scaffold-ci` subcommand + hardened workflow template in `cli.py`, the `permissions` block in this repo's `ci.yml`, and generator tests.
- Excluded: in-session hooks, a live GitHub Actions run, guessed action SHAs.
- Known non-goals: any in-session enforcement; any claim the gate decides engineering adequacy.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard justified |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..004 |
| Questioning attitude | pass | `risk.md` | captured inline |
| Verification | pass (one deferred) | `verification.md` | live run deferred |
| Dependency / supply-chain evidence | pass | `verification.md` | hardened per F5; SHA-pin recommended |
| AI-assisted work checks | pass | `verification.md` | no SHAs guessed |
| Review / approval | planned | the PR | maintainer review pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No live GitHub Actions run here | Gate behavior unproven end-to-end | defer | FlyFission | Maintainer runs the generated workflow on a real PR |
| Gate runs from PR code on `pull_request` | A PR can edit the generated workflow unless branch protection requires the check | accept | FlyFission | Pair with branch protection (require this check + review + restrict workflow edits); the generated banner documents this |
| Actions tag-pinned, not SHA-pinned | Mutable-tag supply-chain risk | accept | FlyFission | The in-file comment recommends SHA-pinning for production |
| Validator install assumes `nuclear-grade` is installable | A non-published package breaks the install step | accept | FlyFission | The template comments the git-install fallback; PyPI publish is a ROADMAP item |

## Rollback / restore plan

- Rollback method: revert the `cli.py`, `ci.yml`, and test edits; adopters delete the generated workflow.
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: removing the `scaffold-ci` subcommand disables the generator.
- Owner on call: FlyFission
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| First generated-workflow run | The gate passes valid packets and fails invalid ones | FlyFission | adopter Actions run | Fix the template; patch release |
| This repo's CI after the permissions block | All jobs stay green | FlyFission | GitHub Actions | Widen the token only if a job genuinely needs it |

## Handoff

- Operator/customer/support notes: adopters run `ng scaffold-ci .` then commit `.github/workflows/nuclear-grade.yml`.
- Docs/runbook updated: the generated workflow self-documents (banner + comments).
- Communication needed: note the generator in release notes when cut.
- Turnover record if activated: not activated.
- Follow-up date: when a maintainer runs the generated workflow on a real PR.

## Release decision

- Decision: ship with residual risk
- Decision maker: FlyFission
- Rationale: the generator is deterministic, the output is valid and hardened, and the repo now practices it; the only unproven step (a live Actions run) is low-risk and reversible.
- Decision question answered by evidence? yes for generation + hardening; the live run is the named residual.
- Conditions attached: maintainer runs the generated workflow on a real PR before announcing.
- Decision posture: conservative enough.
- Abort or rollback trigger: the generated workflow fails on a real PR → fix the template or revert.
- OPEX or post-release learning trigger: any adopter CI failure updates the template.

## Baseline trigger

- Baseline required? yes
- Baseline record: `ng scaffold-ci` + its template become controlled items; this repo's `ci.yml` permissions block is part of the CI baseline.
- Revalidation trigger: a GitHub Actions security-model change, or a validator install-path change.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this branch's PR.
- Monitoring/dashboard/log query: GitHub Actions runs.
- Rollback/runbook: revert the edits; delete the generated workflow.

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

Original Nuclear-grade record inspired by public ideas on configuration management, release readiness, and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
