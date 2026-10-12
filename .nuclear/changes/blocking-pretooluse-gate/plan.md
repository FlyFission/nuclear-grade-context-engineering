# Plan — Blocking PreToolUse gate (opt-in)

## Build sequence

1. Add `hooks/pre_tool_use.py` with `decide()`, which turns raw stdin into a decision or `None`, and `main()`.
2. Add `tests/test_pre_tool_use_hook.py` with tests for deny, ask, pass-through, fail-closed input, the no-`allow` sweep, the policy file, the CLI protocol, and the static AST checks.
3. In `tests/test_hooks.py`, scope the two advisory-only AST tests (imports limited to `json`/`sys`, no `open`) to the two advisory hooks. The gate gets its own stricter allowlist. The banned-substring network scan still covers every hook.
4. Update `HOOKS.md` with the table row, the gate section, the default policy, the policy file, the enable snippet, and the honesty note.

Not touched: `hooks/hooks.json` (stays absent), `CHANGELOG.md` (the owner adds the entry), and the docs under `docs/`, which never said this tier was deferred.

## Proof commands

```bash
git diff --check
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/blocking-pretooluse-gate --strict-custody
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit.

## Source-lineage note

The plan follows [`change-control-packets.md`](../../../docs/02-operating-system/change-control-packets.md), with lineage in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
