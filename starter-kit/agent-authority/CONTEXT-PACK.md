# Context pack: `<task name>`

A focused brief for an AI agent that holds real authority on a single task. Fill in every
section before granting authority. Keep this short — a context pack is not a project plan.

## Objective

`<fill-in: one sentence on what this task accomplishes>`

## Decision question

`<fill-in: the falsifiable question this task answers>`

## Packet path

`<fill-in: path to the .nuclear/changes/<slug>/ packet that holds this task's evidence, or N/A
with the reason>`

## Allowed actions

The agent may:

- `<fill-in: file paths or globs it may write>`;
- `<fill-in: commands it may run>`;
- `<fill-in: network calls it may make, with hosts>`;
- `<fill-in: credentials it may use, with rotation policy>`.

## Forbidden actions

The agent may not:

- write outside the allowed paths;
- run any command not listed above;
- make a public claim;
- change the release stance;
- edit its own tests, prompts, or this context pack;
- `<fill-in: project-specific forbidden actions>`.

## Approval gates

- `<fill-in: which actions require explicit human approval before execution>`.

## Required proof

The agent must produce, before the work is accepted:

- `<fill-in: the exact tests, commands, or evidence artifacts that must run and their
  expected status>`.

## Stop conditions

The agent must stop and surface (not "ask first" — see denial rule) when:

- a forbidden action is attempted;
- a required-proof artifact does not run;
- a step the agent took is not reproducible;
- `<fill-in: project-specific stop conditions>`.

## Source-lineage note

This template is derived from the context-pack pattern described in
`docs/02-operating-system/context-packs.md` of the Nuclear-grade repository. It does not create
assurance.
