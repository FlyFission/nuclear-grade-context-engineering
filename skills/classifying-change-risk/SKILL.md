---
name: classifying-change-risk
description: Use when selecting Quick, Standard, or stronger human-reviewed mode for code, docs, dependency, AI-authority, release, or public-claim changes.
---

# Classifying Change Risk

## Overview

Classify the change before building so rigor scales by consequence. The output is a mode decision with proof obligations and escalation triggers.

## When to Use

- A change request is new, vague, or expanded.
- A PR has AI-generated code, tests, docs, prompts, or release artifacts.
- Reviewers disagree about whether Quick evidence is enough.

## When Not to Use

- A packet already has a fresh mode decision and no scope changed.
- The system is actively failing and needs incident handling first.

## Inputs

- User request, issue, PR, or diff.
- Affected files, dependencies, prompts, data, credentials, APIs, release artifacts, and users.
- `docs/02-operating-system/activation-thresholds.md`.
- Existing packet `risk.md` if present.

## Process

1. Identify consequence, reversibility, exposure, detectability, uncertainty, and agent authority.
2. Choose Quick only for local, reversible, easy-to-prove work with no new trust boundary.
3. Choose Standard for user-visible, durable, dependency, permission, data, AI, operational, or release consequence.
4. Mark Nuclear, Incident, Research Board, or Release as human-reviewed patterns when activated.
5. Record escalation triggers and the minimum proof required.

## Outputs

- Selected mode.
- Mode rationale.
- Required packet files.
- Proof command or evidence gap.
- Escalation triggers.

## Verification

- `risk.md` names mode, scope, consequence, reversibility, exposure, uncertainty, and proof required.
- Quick and Standard packets pass `python tools/ng.py validate <packet>` after required files are filled.

## Escalation

- Escalate when the change affects money, sensitive data, security, external trust, irreversible operations, autonomous tools, or release readiness.
- Stop when the requested mode understates evident consequence.

## Common Rationalizations

- "It is small." Small code can change a large trust boundary.
- "The agent only changed docs." Docs can make public claims.
- "We can fix it later." Hard-to-detect or hard-to-reverse failures need stronger mode now.

## Red Flags

- Mode selected from effort tolerance instead of consequence.
- No rollback or restore path is named for release-facing work.
- AI tool authority is broader than the packet records.

## Source-lineage note

This skill is an original risk-scaling workflow influenced by public source families mapped in `docs/00-standards-foundation/source-map.md`. It does not determine regulatory classification or compliance.
