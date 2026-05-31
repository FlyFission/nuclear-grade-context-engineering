# Governance

Governance here is light. Keep the public language safe about its sources, keep tests passing, keep the workflows usable, and refuse to overclaim.

## Release gates

Before a public release or a big public-facing change, run:

```bash
python -m pytest -q
python -m py_compile tools/ng.py tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/reference/workspace_guard.py
python tools/ng.py doctor .
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

Run the source and boundary scans when docs, templates, skills, commands, or examples change.

For changes that turn on the HPI habits (small habits from Human Performance Improvement), also confirm the handoff, self-check, OPEX (lessons from real operation), and trust records for a dependency, model, or API are used only when the stakes call for them.

## Versioning

Public v0 uses rough semantic milestones:

- patch-level changes for docs, templates, and checker fixes;
- minor milestones for new workflow surfaces or examples;
- no compatibility promise for pre-1.0 internals.

## Contributions

Contributions should:

- keep every claim tied to its evidence;
- add or update tests when behavior changes;
- avoid new dependencies unless there is a clear reason;
- update the indexes when adding skills, commands, templates, or examples;
- keep the MIT license and boundary wording;
- keep the HPI wording software-native and free of compliance claims.

## AI-assisted contributions

If AI agents make real changes to code, docs, tests, templates, release evidence, or source-lineage wording, record the scope, the evidence, and the independent check in the right packet or pull request.

If work moves to another agent or thread, record the handoff state. If a critical action happens, record the target, the expected result, the stop condition, and the evidence afterward.

## Boundary note

Governance keeps the public workflow consistent. It does not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
