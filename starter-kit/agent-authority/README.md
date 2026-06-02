# Starter kit: Agent-authority

Use this when your AI agent has write, run, network, or approval authority over its own
working set. The agent-tool-permissions worked example
([`../../docs/03-worked-examples/ai-agent-tool-permissions/`](../../docs/03-worked-examples/ai-agent-tool-permissions/))
is the reference packet for this kit.

## When this trigger fires

Any "yes" puts you in this kit:

- the agent writes files in your repo or a workspace it shares with humans;
- the agent runs shell commands or network calls in production paths;
- the agent holds credentials, API keys, or model access tokens;
- the agent can approve, merge, deploy, publish, or release;
- the agent has authority over its own tests, prompts, CI config, or approval policy.

If the last one is true, read the **self-modification boundary** in
[`../../docs/04-adoption/agent-authority-model.md`](../../docs/04-adoption/agent-authority-model.md)
before anything else. Guards inside the agent's writable set are not enforcement.

## Drop this into your repo

```bash
# from this repo's root, into your repo at $TARGET:
# 1. Start from Core.
cp -r starter-kit/core/{AGENTS.md,.nuclear} "$TARGET"/
cp -r starter-kit/agent-authority/{CONTEXT-PACK.md,.github} "$TARGET"/
# 2. Add Core 7 skills (see starter-kit/core/README.md).
# 3. Add the Agent-authority cluster:
for s in deciding-who-decides declaring-intent stress-testing-agent-changes \
         vetting-outside-code-and-models recording-what-an-agent-did \
         briefing-an-agent handing-off-work; do
  mkdir -p "$TARGET/skills/$s"
  cp "skills/$s/SKILL.md" "$TARGET/skills/$s/SKILL.md"
done
# 4. Copy the agent-authority adoption doc as required reading:
mkdir -p "$TARGET/docs/04-adoption"
cp docs/04-adoption/agent-authority-model.md "$TARGET/docs/04-adoption/"
```

## What this kit contains

- [`CONTEXT-PACK.md`](CONTEXT-PACK.md) — a fill-in template for the per-task context pack
  required when an agent gets real authority (per
  [`../../docs/02-operating-system/context-packs.md`](../../docs/02-operating-system/context-packs.md)).
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — pre-filled with
  explicit Mode + Proof-command fields and the rung-ladder reminder.

## The Agent-authority cluster (in trigger order)

| Skill | When to invoke |
|---|---|
| `deciding-who-decides` | At the start: who holds authority for this change — agent at the edge, or human gate? |
| `declaring-intent` | Before each irreversible action: state expected result, abort criteria, rollback. |
| `briefing-an-agent` | Hand the agent a focused context pack, not the whole repo. |
| `recording-what-an-agent-did` | Capture the agent's scope, permissions, approvals, and independent checks. |
| `vetting-outside-code-and-models` | When a dependency, model, API, or vendor claim is on the trust path. |
| `stress-testing-agent-changes` | Red-team the change before merge — hostile inputs, escape attempts, authority overflow. |
| `handing-off-work` | When a session ends, the work pauses, or another agent or human takes over. |

## Source-lineage note

This kit packages original patterns from this repository. It does not create assurance. See
[`../../DISCLAIMER.md`](../../DISCLAIMER.md).
