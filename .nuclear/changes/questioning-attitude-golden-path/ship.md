# Ship

## Release decision

- **Decision:** ship with maintainer review
- Decision maker: pending maintainer review
- Rationale: Tests, doctor, packet validation, and public scans pass locally.

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Risk classification | pass | `risk.md` |
| Basis / requirements / claims | pass | `basis.md` |
| Verification | pass | `verification.md` |
| Source-lineage boundary | pass | `verification.md` |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Broader golden-path evidence tooling remains future work. | Public users get skill/command/templates before full evidence bundle CLI. | accept | Maintainer | Roadmap/evidence tooling work. |

## Rollback / restore plan

- Revert the questioning-attitude files and wording changes.
- Restore previous lifecycle docs if public wording fails review.

## Monitoring and post-release checks

- Watch GitHub issues and PR feedback for confusion about DOE-HDBK-1028 claims.
- Recheck public docs for stale `Frame` and overclaiming language before release.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`

## Exit criteria

- Release decision is explicit.
- Evidence status and gaps are visible.
- Baseline trigger is named if this change is accepted.

## Source-lineage note

Original release decision record mapped to public source lineage in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
