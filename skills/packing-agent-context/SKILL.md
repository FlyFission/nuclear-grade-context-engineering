---
name: packing-agent-context
description: Use when preparing bounded context for a human or AI agent working on a packet.
---

# Packing Agent Context

## Overview

Context packs give agents and reviewers the right bounded information: role, mode, objective, affected files, proof obligations, approvals, forbidden actions, and source lineage.

## When to Use

- An AI agent will edit files, run commands, call tools, or prepare release evidence.
- A reviewer needs a one-screen summary of a Standard packet.
- A long research or implementation thread must be distilled into operational context.

## When Not to Use

- The task is a small Quick change with all context already in `risk.md` and `proof.md`.
- The agent has no authority to act and only needs a file explanation.

## Inputs

- Packet path and selected mode.
- Role: builder, reviewer, verifier, releaser, incident lead, or researcher.
- Affected files, allowed commands, forbidden actions, approval gates, and required evidence.
- `docs/02-operating-system/context-packs.md`.

## Process

1. Name the role and objective.
2. Include only the packet files, affected files, source rows, and proof commands needed for the next decision.
3. State file, command, network, credential, approval, and release authority.
4. State forbidden claims and stop conditions.
5. Link the context pack back to the packet and relevant mode rules.

## Outputs

- A context pack section or file.
- Clear authority boundaries.
- Next action and evidence requirement.

## Verification

- A reader can answer what they may do, what must remain true, what proof is required, and when to stop.
- The context pack does not ask for whole-repo or full-standards loading without an activated reason.

## Escalation

- Stop if requested actions exceed the context pack authority.
- Escalate when credentials, network effects, production data, release authority, or external trust claims appear.

## Common Rationalizations

- "More context is safer." Excess context hides the actual decision and increases token burn.
- "The agent can infer permissions." Tool authority must be explicit.
- "Approval can happen later." Approval gates belong before the side effect.

## Red Flags

- No forbidden actions.
- No allowed file or command scope.
- Source lineage is pasted wholesale instead of linked.

## Source-lineage note

This skill is an original context-discipline pattern influenced by public configuration management, secure development, AI risk, and systems engineering sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance.
