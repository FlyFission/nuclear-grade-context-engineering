# Plan — targeted agent reading

## Build sequence

1. Replace the blanket `README.md` and `WORKFLOWS.md` preload in `AGENTS.md` with task-triggered retrieval while retaining the applicable change record requirement (REQ-001).
2. Inspect the one-line guidance diff and run repository verification.
3. Open a reviewable PR; do not merge or alter release posture.

Non-goals: changing skill routing, completion criteria, templates, permissions, or public positioning.

## Proof commands

```bash
git diff --check
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/targeted-agent-reading --strict-custody
```

## Required links

- Risk: [`risk.md`](risk.md)
- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Only `AGENTS.md` and this packet change; every proof command passes before commit.

## Source-lineage note

The plan applies existing repository doctrine and sources mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md); it introduces no external standard or compliance claim.
