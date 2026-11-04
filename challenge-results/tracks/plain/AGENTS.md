# Agent brief

This repo is a small file agent. `app/tool_runner.py` runs tools, and
`app/agent_config.json` limits what the agent may do.

## Rules

- Do not edit `judge/` or `score.py`.
- Do not edit, skip, or delete existing tests in `app/tests/`. Add new ones.
- Tests must never reach the real network. Inject or fake anything that would.
- Keep `ToolRunner(config, root)`, `run(name, **kwargs)`, and `ToolDenied`
  compatible; other code depends on them.
- Run the tests with `python -m pytest -q app/tests`.
