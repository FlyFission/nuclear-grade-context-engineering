# Change impact

## Change

- Slug: `matt-skill-lifecycle-and-flow`
- Base: `3ade94ee994f727098a90ee7c5b69c157b107ddf`
- Candidate: branch `feat/matt-skill-lifecycle-and-flow`

## Impact decisions

| Controlled family | Update / leave / defer / block | Impact | Required reconciliation |
|---|---|---|---|
| Catalog, CLI, generator, package tests | update | lifecycle semantics become executable | exact parity and compatibility projections |
| Four pilot skills and generated commands | update | context/load and command source change | receipts, output fixtures, and commands must remain equivalent |
| Remaining skills | leave | no mass rewrite in this PR | they stay valid under relaxed optional modules |
| Workflow doctrine and Standard templates | update | build and review routing changes | one crosswalk and conditional language |
| Live provider evaluation | defer | nondeterministic/costly and not CI-suitable | scorer and run contract included; no cross-host claim |
| Merge/release/version | block | requires human authority after PR review | `ship.md` remains hold |

## Propagation surfaces

- Canonical: lifecycle registry, skill bodies/assets, workflow doctrine, templates, executable modules.
- Generated/projected: command cards, compatibility lists/maps, package/install surfaces.
- Indexed: `SKILLS.md`, `WORKFLOWS.md`, integration docs as changed.
- Evaluated: routing/output fixtures, token report, tests, packet.

## Required links

- `risk.md`
- `controlled-items.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Every changed canonical surface has its projections and checks updated.
- Deferred live evidence is not represented as a pass.

## Source-lineage note

This record applies the public change-impact disciplines mapped in `docs/00-standards-foundation/source-map.md`. It is a software change-impact record, not a formal impact analysis or compliance artifact.
