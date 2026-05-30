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

## Exit criteria

Agent authority is acceptable when a reviewer can see four things: what the agent was allowed to do, what it actually changed, what evidence it produced, and what it was forbidden to claim.

## Source-lineage note

This model is an original workflow pattern. Public sources on AI risk, secure development, configuration, and software assurance shaped it. Those sources are mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
