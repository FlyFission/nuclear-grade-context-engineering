# Plan

## Change context

- Slug: skill-contract-modernization
- Mode: Standard
- Owner: maintainer

## Charter and anchor check

A re-evaluated gate, not a one-time note. Confirm before Plan and re-check before Verify. See `staying-on-mission`.

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes.
- Re-checked before Verify? yes; scope held to the contract change, deferred items stayed deferred.
- Charter articles in play: Rising standards, Evidence over persuasion, Formality, Questioning attitude.

If a non-goal or charter article must be crossed, record the justification here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| none | not applicable | not applicable | proceed |

## Build sequence

1. Rewrite all 18 skill descriptions to the what-plus-when-plus-negative form, colon-free, within band.
2. Update `tests/test_skill_contracts.py` to the new rule (length band, negative clause, no colon-space, name regex, optional license/compatibility).
3. Update the published contract: `docs/05-reference/skill-authoring-contract.md` and `SKILLS.md`, including progressive disclosure.
4. Sync version to 0.3.0 across `pyproject.toml`, `nuclear-grade.yaml`, `CITATION.cff`; update `test_packaging.py`.
5. Add the 0.3.0 CHANGELOG section.
6. Fill this dogfood packet; run tests, ruff, doctor, validate.

## Non-goals

- The evidence-coverage validator rule.
- Making the charter or anchor a hard required gate.
- The cross-cutting hedge-word red-flag sweep.
- Adding description enforcement to the CLI doctor.
- Renaming any skill.

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Descriptions rewritten | All within band and colon-free | pass |
| Contract test updated | New rule enforced; suite green | pass |
| Docs updated | Authoring contract and SKILLS.md reflect the rule | pass |
| Version synced | 0.3.0 everywhere; packaging test green | pass |
| Packet validates | This packet passes the validator | pass |

## Rollback approach

- Rollback method: revert the branch; descriptions and test revert cleanly.
- State/data reversal notes: none.
- Feature flag / kill switch: not applicable.
- Owner: maintainer.
- Time to restore estimate: minutes.

## Proof commands

```bash
ruff check .
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/skill-contract-modernization
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Build sequence executed; tests green; packet validates.

## Source-lineage note

Original Nuclear-grade plan influenced by configuration-management concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
