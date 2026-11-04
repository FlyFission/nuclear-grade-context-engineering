# Plan: Menu descriptions for the command cards

## Build sequence

1. In `nuclear_grade/gen_commands.py`, add `menu_description()` and emit the frontmatter; drop the quoted full description; shorten the generation note and closing pointer.
2. Regenerate the cards with `python tools/ng.py gen-commands`.
3. Add a contract test in `tests/test_command_contracts.py`.
4. Update `docs/05-reference/command-authoring-contract.md`, `COMMANDS.md`, and `CHANGELOG.md`.

Controlled items changed: the command generator and all 29 generated cards.

## Proof commands

```bash
python tools/ng.py gen-commands --check
python tools/ng.py tokens .
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python -m nuclear_grade.release
claude plugin validate .
git diff --check
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit, or its result is recorded as a gap.

## Source-lineage note

The plan follows [`change-control-packets.md`](../../../docs/02-operating-system/change-control-packets.md), with lineage in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
