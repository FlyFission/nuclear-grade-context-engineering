# Plan: Guard plugin, deny-rule comparison, and `init` add-ons

## Build sequence

1. Extend `hooks/pre_tool_use.py`: deny `~/.claude/plugins/**`, add `.claude/plugins` to the shell trust tokens, and ask on `claude plugin disable|uninstall|remove` and `claude plugin marketplace remove|rm`.
2. Add `plugins/nuclear-grade-guard/` with `.claude-plugin/plugin.json`, `hooks/hooks.json`, a copy of the gate, and a short README. List it in `.claude-plugin/marketplace.json`.
3. Add the guard manifest to `MANIFESTS` in `nuclear_grade/release.py` and to `docs/05-reference/releasing.md`.
4. In `nuclear_grade/cli.py`, add `gate_hook_entry`, `plan_gate_settings`, and `ci_writes` (shared with `scaffold-ci`), the four `init` flags, and a `keep_existing` mode for `apply_writes`.
5. Bundle `hooks/pre_tool_use.py` and `starter-kit/core/AGENTS.md` in the wheel, and include `hooks/` and `starter-kit/` in the sdist.
6. Add tests in `tests/test_plugin_packaging.py`, `tests/test_pre_tool_use_hook.py`, `tests/test_ng_cli.py`, and `tests/test_packaging.py`.
7. Update HOOKS.md (guard install, removal, the deny-rule comparison, the timeout), INSTALL.md, INTEGRATIONS.md, `docs/05-reference/cli-reference.md`, and QUICKSTART.md.

Controlled items changed: the gate (`hooks/pre_tool_use.py` and its plugin copy), the plugin marketplace and a new plugin manifest, the CLI (`nuclear_grade/cli.py`), the release identity checker, the wheel and sdist contents, the tests above, and the public docs above.

## Proof commands

```bash
git diff --check
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python -m nuclear_grade.release
claude plugin validate .
claude plugin validate plugins/nuclear-grade-guard
claude --plugin-dir ./plugins/nuclear-grade-guard plugin details nuclear-grade-guard
claude --plugin-dir . plugin details nuclear-grade
python -m build --outdir <scratch> .
python tools/ng.py validate .nuclear/changes/guard-plugin-and-init-addons --strict-custody
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit, or its result is recorded as a gap.

## Source-lineage note

The plan follows [`change-control-packets.md`](../../../docs/02-operating-system/change-control-packets.md), with lineage in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
