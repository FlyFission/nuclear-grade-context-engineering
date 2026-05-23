---
name: using-nuclear-grade
description: Use when adopting Nuclear-grade for an AI-assisted software change or repo workflow.
---

# Using Nuclear-grade

## Overview

Use Nuclear-grade to turn AI-assisted software work into a bounded evidence path: question assumptions, classify consequence inside the risk screen, create the smallest useful packet, specify intent, prove important claims, and make the release decision explicit.

## When to Use

- A human or AI agent will change code, tests, docs, prompts, tooling, dependencies, or release evidence.
- A reviewer needs more than a commit message and test output to understand risk.
- Agent authority, dependency trust, security posture, or release readiness matters.

## When Not to Use

- The work is a disposable local note with no durable engineering consequence.
- The user asks for formal compliance, certification, safety analysis, or regulatory submittal adequacy.
- The right next action is incident containment or rollback; use the incident path first.

## Inputs

- The user request or PR objective.
- The repository diff or planned affected files.
- Existing `.nuclear/changes/` packets.
- `WORKFLOWS.md`, `QUICKSTART.md`, and `docs/02-operating-system/activation-thresholds.md`.

## Process

1. Apply questioning attitude: decision question, assumptions, evidence gaps, stop conditions.
2. Classify the change as Quick, Standard, or a human-reviewed stronger mode.
3. Create or locate the packet under `.nuclear/changes/<slug>/`.
4. Record the minimum specification/design basis, proof obligation, affected files, and forbidden claims.
5. Keep implementation work linked to claims and evidence.
6. Run the validator for Quick or Standard packets.
7. Stop before release if evidence status, rollback, monitoring, decision, baseline trigger, or legal boundary wording is unclear.

## Outputs

- Selected mode and rationale.
- Packet path.
- Required evidence commands or explicit evidence gaps.
- Release posture: ship, block, defer, or ship with named residual risk.

## Verification

- `python tools/ng.py status .`
- `python tools/ng.py validate .nuclear/changes/<slug>`
- Reviewer can answer what changed, why it matters, what proved it, and what remains uncertain.

## Escalation

- Escalate from Quick to Standard when user impact, dependency trust, permissions, data, AI authority, or release posture matters.
- Escalate to human review when the work touches regulated, safety-significant, security-significant, procurement, or external-trust claims.
- Stop when asked to claim formal assurance or compliance.

## Common Rationalizations

- "The tests pass, so the packet is unnecessary." Passing tests do not preserve assumptions, scope, residual risk, or release decision.
- "The agent remembers the context." Chat history is not a durable review artifact.
- "This is only documentation." Public docs can create legal, trust, and assurance claims.

## Red Flags

- The packet cannot name one important claim.
- Evidence is broad prose instead of commands, links, reviews, or named gaps.
- The work says or implies compliance, approval, safety, security, or formal verification.

## Source-lineage note

This skill is part of an original workflow influenced by public high-consequence engineering, secure development, software assurance, and configuration discipline sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
