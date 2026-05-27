# Governance

Nuclear-grade governance is lightweight: preserve source-safe public language, keep tests passing, keep workflows usable, and refuse overclaiming.

## Release gates

Before a public release or major public-facing change:

```bash
python -m pytest -q
python -m py_compile tools/ng.py tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/reference/workspace_guard.py
python tools/ng.py doctor .
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

Run source and boundary scans when docs, templates, skills, commands, or examples change.

For HPI-activated changes, also confirm turnover, self-check, OPEX, and dependency/model/API trust records are used only when consequence warrants them.

## Versioning

Public v0 uses semantic-ish public milestones:

- patch-level changes for docs, templates, and validator fixes;
- minor milestones for new workflow surfaces or examples;
- no compatibility promise for pre-1.0 internals.

## Contributions

Contributions should:

- keep claims evidence-scoped;
- add or update tests for behavior changes;
- avoid new dependencies unless clearly justified;
- update indexes when adding skills, commands, templates, or examples;
- preserve MIT license and boundary language.
- keep HPI language software-native and non-compliance-claiming.

## AI-assisted contributions

If AI agents materially change code, docs, tests, templates, release evidence, or source-lineage wording, record the scope, evidence, and independent check in the relevant packet or PR.

If work transfers to another agent or thread, record the turnover state. If a critical action is performed, record the target, expected result, stop condition, and after-action evidence.

## Boundary note

Governance keeps the public workflow coherent. It does not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
