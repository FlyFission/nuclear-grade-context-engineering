# Agent Authority Model

**Purpose:** Spell out what an AI agent is allowed to do before it can cause any side effects.

## Authority dimensions

| Dimension | Questions |
|---|---|
| Files | What may the agent read, create, modify, or delete? |
| Commands | What commands may run locally? |
| Network | May the agent browse, call APIs, fetch packages, or upload data? |
| Credentials | May the agent see, use, rotate, or request secrets? |
| Review | What human approval is required before changes, commits, pushes, or release? |
| Release | May the agent prepare, tag, merge, deploy, or publish? |
| Claims | What public claims are forbidden? |

## Context pack requirement

When an agent gets real authority, write a context pack that states:

- objective;
- decision question;
- packet path;
- allowed and forbidden actions;
- approval gates;
- required proof;
- stop conditions.

## Denial rule

If an action goes beyond what the agent is allowed to do, the agent must stop. It must record the approval it needs, or the path to escalate.

At a cut point, the agent must pause before acting if any of these is unclear: the exact target, the expected result, the forbidden claim, or the stop condition. A cut point includes file writes, broad commands, public claims, changes to trust in a dependency, model, or API, release actions, and other steps that are hard to undo.

For an **unattended** agent there is no human to ask mid-run. "Ask first" degrades to **stop, record the needed approval, and halt** (or hard-block the action). Design the gate as block / escalate / record, not as a prompt for permission that nothing will answer.

## Self-modification boundary

An agent with write or run authority over its own tests, prompts, approval policy, or CI config can satisfy a gate by changing the gate. "Ships green by editing its own test" is not proof; it is the control failing silently. A guard inside the agent's writable working set is not enforcement — it is a suggestion the agent can edit.

The rule: the control that decides whether the agent's work is acceptable must sit where the agent cannot rewrite it.

### Enforcement rungs (weak to strong)

| Rung | Mechanism | Agent can defeat by | Use when |
|---|---|---|---|
| 1 | Advisory print or log | ignoring the output | drafting only |
| 2 | Exit code in a script the agent can edit | editing the script | reversible local work |
| 3 | Tests the agent can edit | rewriting the test | low stakes, trusted loop |
| 4 | Out-of-band CI the agent cannot push to | nothing in-repo | authority over its own working set |
| 5 | Branch protection or required human review | nothing | irreversible or trust-bearing |

Match the rung to the authority. An agent that can edit files at rungs 1-3 has no real gate; promote to rung 4-5 before granting write or run authority over its own controls.

## Plan-phase vs build-phase authority

Planning and building are different authority phases, and naming the line keeps a
read-only planner from sliding into an unreviewed writer. During the question,
specification, and plan phases the agent is read-only over product code: its writes are
confined to the change-record packet, and it prepares, but does not take, release
actions. Build authority over product code opens only after the plan clears its
human-approved gate (the `plan.md` review checkpoints — Requirements / Design / Tasks
approved). This is the self-modification boundary above, applied in time: the control
that approves the plan must sit where the planning agent cannot rewrite it. See the
agent-drafts-spec workflow in `CORE.md`.

## Exit criteria

Agent authority is acceptable when a reviewer can see five things: what the agent was allowed to do, what it actually changed, what evidence it produced, what it was forbidden to claim, and **where the controls that gate its work live relative to its writable set** (rung 4 or higher when the agent has authority over its own tests, prompts, or CI).

## Source-lineage note

This model is an original workflow pattern. Public sources on AI risk, secure development, configuration, and software assurance shaped it. Those sources are mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
