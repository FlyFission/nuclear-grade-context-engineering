# Risk

## Change

- Slug: questioning-attitude-golden-path
- Owner: FlyFission / Codex
- Date: 2026-05-23
- Summary: Make Questioning Attitude the public front door, add the flagship skill/command/templates, and move Baseline after review/decision in lifecycle language.

## Selected mode

- **Mode:** Standard
- Why: Public docs, skills, commands, templates, CLI doctor/list behavior, tests, and source-lineage records change together.
- Why Quick is not enough: The change affects public workflow vocabulary and controlled repo surfaces.
- Escalation triggers: Any wording that implies DOE compliance, formal HPI program adequacy, safety, security, certification, or regulatory adequacy.

## Questioning-attitude screen

| Question | Answer |
|---|---|
| What assumptions changed? | `Frame` was not nuclear/HPI-native enough; Questioning Attitude is a stronger public hook. |
| What must be true? | Questioning Attitude is presented as source lineage only, and Baseline appears after review/decision. |
| What could go wrong? | Public docs could imply DOE compliance or leave old lifecycle wording behind. |
| Stop condition | Boundary scans find unbounded assurance claims or stale `Frame -> ...` lifecycle language. |

## Required links

- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- New skill, command, templates, manifest, CLI, docs, and tests align on the Questioning Attitude golden path.
- Tests and validator pass.

## Source-lineage note

Original workflow update inspired by DOE-HDBK-1028-2009 questioning-attitude practices and public configuration-management sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
