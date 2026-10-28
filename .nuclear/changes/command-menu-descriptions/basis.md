# Basis: Menu descriptions for the command cards

## Mission

A person scrolling Claude Code's `/` menu can tell what each `ng-*` card does, without adding anything to the model's context.

## Requirements

- **REQ-001:** Every generated card shall start with frontmatter whose `description` is the first sentence of its skill's description.
- **REQ-002:** Every generated card shall set `disable-model-invocation: true`.
- **REQ-003:** Every card shall stay within `command_max`, and the command total within `command_total_max`.
- **REQ-004:** The prompt text in each card shall be unchanged, and `gen-commands --check` shall pass.
- **REQ-005:** The command authoring contract and COMMANDS.md shall describe the new structure.

## Non-goals

No change to any skill, any prompt, or any token ceiling.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)

## Exit criteria

Each requirement maps to evidence in [`trace.md`](trace.md).

## Source-lineage note

Original Nuclear-grade synthesis. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
