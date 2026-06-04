# Nuclear-grade Examples

Public v0 ships one fully worked example that is checked by tests, plus one hands-on comparison study. More worked examples are on the roadmap, not launch claims.

## Included and validated

| Example | What it proves | Start here |
|---|---|---|
| AI agent tool permissions | The agent's file-write power is kept under control and proven to stay inside an approved workspace root | `docs/03-worked-examples/ai-agent-tool-permissions/README.md` |

## Included comparison

| Example | What it checks | Start here |
|---|---|---|
| Skill and workflow comparison | How each published skill and workflow does against plain prompting across twelve real use cases | `docs/03-worked-examples/skill-workflow-comparison/README.md` |

Run it:

```bash
python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

## Roadmap examples

| Example | Planned chain from claim to proof |
|---|---|
| External API controls | allowed-tool list, credential boundary, proof that denied calls are blocked, audit events |
| Human approval gates | an action that needs approval, denial before approval, the recorded approval, evidence after the action |
| Dependency upgrade | impact check, why this version, tests, rollback, supply-chain notes |
| Prompt/model baseline | the controlled prompt and model state, eval evidence, what triggers a re-check |
| Release readiness | evidence status, leftover risk, rollback, monitoring, handoff |

## Boundary note

Examples show focused paths from claim to evidence. They do not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
