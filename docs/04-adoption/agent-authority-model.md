# Agent Authority Model

**Purpose:** Make AI-agent permissions explicit before side effects occur.

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

For material agent authority, create a context pack that states:

- objective;
- packet path;
- allowed and forbidden actions;
- approval gates;
- required proof;
- stop conditions.

## Denial rule

If the requested action exceeds authority, the agent must stop and record the needed approval or escalation path.

## Exit criteria

Agent authority is acceptable when a reviewer can see what the agent was allowed to do, what it actually changed, what evidence it produced, and what it was forbidden to claim.

## Source-lineage note

This model is an original workflow pattern influenced by public AI risk, secure development, configuration, and software assurance sources mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance.
