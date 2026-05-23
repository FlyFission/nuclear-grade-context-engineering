# Nuclear-grade Examples

Public v0 includes one validated worked example. Additional examples are roadmap items, not launch claims.

## Included and validated

| Example | What it proves | Start here |
|---|---|---|
| AI agent tool permissions | Agent file-write authority is treated as controlled configuration and proven inside an approved workspace root | `docs/03-worked-examples/ai-agent-tool-permissions/README.md` |

Run it:

```bash
python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

## Roadmap examples

| Example | Planned proof chain |
|---|---|
| External API controls | tool allowlist, credentials boundary, denial evidence, audit events |
| Human approval gates | approval-required action, denial before approval, recorded approval, post-action evidence |
| Dependency upgrade | impact screen, version rationale, tests, rollback, supply-chain notes |
| Prompt/model baseline | controlled prompt/model state, eval evidence, revalidation trigger |
| Release readiness | evidence status, residual risk, rollback, monitoring, handoff |

## Boundary note

Examples demonstrate scoped evidence paths. They do not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
