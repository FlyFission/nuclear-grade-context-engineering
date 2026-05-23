# ng-context-pack

## Purpose

Prepare bounded context for a human or AI agent working from a packet. This is a portable command prompt.

## Use when

- An agent will edit files, run tools, or prepare evidence.
- A reviewer needs a short operational summary.
- A long thread needs distillation before work continues.

## Do not use when

- The packet itself already contains all needed Quick-mode context.
- The task is only to explain one file.

## Inputs

- Packet path.
- Role, objective, affected files, allowed commands, forbidden actions, approvals, and required evidence.
- `docs/02-operating-system/context-packs.md`.

## Prompt text

```text
Build a Nuclear-grade context pack for this work.

Inputs:
- packet: .nuclear/changes/<slug>/
- role: <builder|reviewer|verifier|releaser|researcher>
- objective: <one paragraph>
- affected files: <list>
- allowed commands/tools: <list>
- forbidden actions: <list>
- approval gates: <list>
- required evidence: <commands/links/reviews>

Return a concise context pack with mode, objective, risk summary, basis summary, required evidence, authority boundaries, forbidden claims, open gaps, and next action.
```

## Files created or modified

- Packet note or context-pack section chosen by the maintainer.
- No implementation files unless separately authorized.

## Expected outputs

- Bounded context pack.
- Clear authority boundaries.
- Next action.

## Verification command

```bash
python tools/ng.py status .
```

## Failure modes

- Loading the whole repo without an activated reason.
- Leaving file, command, network, credential, or release authority unstated.
- Omitting forbidden claims.

## Legal/assurance boundary note

A context pack constrains work. It does not approve side effects, certify adequacy, or create formal assurance.
