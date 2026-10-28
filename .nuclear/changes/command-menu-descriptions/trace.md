# Trace: Menu descriptions for the command cards

## Claim trace

| ID | Implemented in | Evidence | Status |
|---|---|---|---|
| REQ-001 | `menu_description()` and `render_card()` in `nuclear_grade/gen_commands.py` | E-001, E-004 | pass |
| REQ-002 | `render_card()` | E-001 | pass |
| REQ-003 | shorter card text | E-002 | pass |
| REQ-004 | prompt sections untouched | E-003 | pass |
| REQ-005 | `docs/05-reference/command-authoring-contract.md`, `COMMANDS.md` | E-005 | pass |
| REQ-001 live | The `/` menu shows the description in a live session | E-006 | gap |

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every requirement has an implementation and an evidence ID with a status.

## Source-lineage note

Traceability here is an internal review aid. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
