# Ship

## Release decision

- **Decision:** ready for PR review after local verification pass; public visibility remains blocked until PR merge and final repository visibility gate.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Product surface | pass | `trace.md` |
| CLI and tests | pass | `verification.md` |
| Public boundary scans | pass | `verification.md` |

## Residual risks

- Public v0 does not include packaged harness integration.
- Public v0 includes one full worked example; additional examples remain roadmap items.
- Stronger modes remain human-reviewed patterns until project-specific validators exist.

## Rollback / restore plan

- Before merge: close or revise the branch.
- After merge: revert the productization PR and rerun CI plus packet validation.

## Monitoring and post-release checks

- Watch public issues for onboarding confusion.
- Track requests for harness packaging separately from core workflow defects.
- Re-run source and boundary scans on public-facing changes.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Release decision is updated after verification and PR review.
- Residual risks are accepted or blocking.

## Source-lineage note

This ship record is part of the original Nuclear-grade packet workflow and references `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
