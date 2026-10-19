# Plan: initial tool runner

## Build sequence

1. Add `app/agent_config.json` with two tools, network off, and the workspace folder.
2. Add `app/tool_runner.py` with the config checks.
3. Add `app/tests/test_tool_runner.py`.

Non-goals: network tools, shell tools.

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

`python -m pytest -q app/tests` passes.

## Source-lineage note

Record shape from Nuclear-grade, https://github.com/FlyFission/nuclear-grade-context-engineering. No compliance claim is made.
