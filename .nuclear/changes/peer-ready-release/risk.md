# Risk

## Selected mode

- **Mode:** Standard
- **Change:** Productize Nuclear-grade Public v0 with action-first WBS, skills, portable command prompts, CLI, adoption docs, and contract tests.
- **Why Standard:** Public-facing onboarding, tooling, tests, and legal-boundary wording affect user expectations and release readiness.

## Risk summary

| Area | Status | Note |
|---|---|---|
| Public orientation | pass | README and top-level docs are action-first. |
| Tooling | pass | CLI avoids silent overwrite and preserves validator behavior. |
| Skill quality | pass | Skills are contract-tested. |
| Legal boundary | pass | Public text avoids assurance overclaiming. |

## Required links

- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Productization docs, skills, commands, CLI, and tests are present.
- Contract tests pass.
- Validator passes this packet and the flagship worked-example packet.
- Public boundary scans show no unsafe unbounded claims.

## Source-lineage note

This packet describes an original workflow productization change grounded in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
