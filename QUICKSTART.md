# Nuclear-grade Quickstart

**Goal:** question a real AI-assisted change, create a useful controlled-change record in about 15 minutes, and prove one important claim.

## 1. Check the repo

```bash
python tools/ng.py doctor .
python tools/ng.py list
```

If your shell only has `python3`, use `python3`.

## 2. Pick a real change

Good first changes:

- add an AI-agent permission boundary;
- update a dependency with security relevance;
- change API behavior;
- add an AI tool call;
- prepare a small release.

For the first pass, name the controlled item: the file, prompt, model, dependency, tool permission, release artifact, or doc claim whose state must stay reviewable.

Avoid starting with a whole platform redesign. Prove one important claim before expanding the packet.

## 3. Question, then classify the mode

Start with a questioning-attitude screen:

```text
Question: What decision are we making?
Assumptions: What must be true?
Facts to verify: What would change the decision?
Stop conditions: What would make us pause or escalate?
Next artifact: Quick proof, Standard spec, context pack, CM record, or release decision.
```

| If the change is... | Use |
|---|---|
| Low consequence, reversible, easy to prove | Quick |
| User-facing, security-relevant, dependency-relevant, AI-authority-changing, durable, or release-facing | Standard |
| High consequence, hard to reverse, external-trust-bearing, critical, or regulated-adjacent | Human-reviewed stronger mode |
| A failure, defect, incident, or near miss | Incident pattern |
| Mostly an architecture or research decision | Research Board pattern |
| A release-readiness decision | Release pattern |

When unsure, start with Standard and keep the packet thin.

## 4. Create the packet

Quick:

```bash
python tools/ng.py new <slug> --mode quick
```

Standard:

```bash
python tools/ng.py new <slug> --mode standard
```

Manual fallback:

```bash
mkdir -p .nuclear/changes/<slug>/
cp templates/quick/*.md .nuclear/changes/<slug>/
```

For Standard, use `templates/standard/*.md` instead. Use either Quick or Standard templates, not both.

If the change affects controlled configuration, copy the activated CM record you need:

```bash
cp templates/cm/controlled-items.md .nuclear/changes/<slug>/
cp templates/cm/change-impact.md .nuclear/changes/<slug>/
cp templates/cm/baseline.md .nuclear/changes/<slug>/
```

If the change needs the public golden path, copy the activated records:

```bash
cp templates/golden-path/questioning-attitude.md .nuclear/changes/<slug>/
cp templates/golden-path/spec.md .nuclear/changes/<slug>/
cp templates/golden-path/decision.md .nuclear/changes/<slug>/
```

## 5. Fill the minimum useful version

Answer only what helps a reviewer decide:

1. What are we questioning?
2. What facts did we discover?
3. What are we specifying?
4. What evidence will prove the important claim?
5. What files, tests, dependencies, prompts, models, tools, or release artifacts are affected?
6. What would escalate the mode?
7. What decision is needed before release or merge?
8. What baseline or revalidation trigger changes after the decision?

## 6. Prove one claim

Example from the included worked example:

```text
Claim: agent writes are limited to the approved workspace root.
Basis: prevent destructive writes outside approved scope.
Control: canonical path guard and workspace containment check.
Evidence: allowed-write test, traversal denial, absolute-path denial, symlink-escape denial, audit event checks.
Ship posture: C-001 passes; broader API and approval-gate chains are deferred, not assumed.
```

Run the example:

```bash
python -m pytest docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q
python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

## 7. Validate your packet

```bash
python tools/ng.py validate .nuclear/changes/<slug>
```

The v0 validator checks Quick and Standard packet structure, required sections, evidence status, source-lineage notes, local packet links, and prohibited overclaiming phrases. It does not decide whether your system is safe, secure, compliant, or suitable for a regulated use case.

## 8. Decide or stop

Decide to ship or merge only when:

- exit criteria are satisfied;
- unresolved gaps are accepted or explicitly block release;
- verification evidence is reproducible enough for the risk;
- rollback, monitoring, and handoff are proportional to consequence.

Stop or escalate when:

- the change affects sensitive data, money, safety, external trust, irreversible actions, critical operations, or AI authority;
- proof is flaky, indirect, or missing;
- dependency, model, API, or tool trust is not understood;
- reviewers cannot determine what changed and why.

## 9. Read next

- [`WORKFLOWS.md`](WORKFLOWS.md)
- [`SKILLS.md`](SKILLS.md)
- [`COMMANDS.md`](COMMANDS.md)
- [`EXAMPLES.md`](EXAMPLES.md)
- [`docs/04-adoption/reviewer-playbook.md`](docs/04-adoption/reviewer-playbook.md)
- [`docs/05-reference/cli-reference.md`](docs/05-reference/cli-reference.md)

## Source-lineage note

This quickstart is an original software workflow based on Nuclear-grade's public source foundation and operating-system docs. It does not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
