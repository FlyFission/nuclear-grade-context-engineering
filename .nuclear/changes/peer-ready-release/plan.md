# Plan

## Build sequence

1. Add catalog and contract tests for skills, commands, public docs, and CLI.
2. Add `nuclear-grade.yaml`.
3. Add skills and portable command prompts.
4. Add `tools/ng.py`.
5. Add top-level product docs and adoption/reference docs.
6. Update README, Quickstart, tool docs, metadata, and CI.
7. Run tests, validator, doctor, compile, diff check, and scans.

## Non-goals

- No marketplace packaging in Public v0.
- No new full worked example before release.
- No formal assurance or compliance claim.

## Rollback

- Revert the productization branch before merge.
- If merged, revert the productization PR and keep the prior Quick/Standard validator path intact.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `ship.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- Implementation sequence is complete.
- CI includes full tests, doctor, compile, and packet validations.

## Source-lineage note

This plan is an original implementation record for the Nuclear-grade workflow surface and references `docs/00-standards-foundation/source-map.md`.
