---
name: creating-change-records
description: Creates or updates Quick or Standard packets, adds the required files, and refreshes evidence obligations for an evidence-backed PR. Use when starting or revising a change record. Do not use for a one-off throwaway script, or for work that belongs in an existing packet rather than a new one.
---

# Creating Change Packets

## Overview

A packet keeps scope, specification/design basis, plan, trace, evidence, and release decision together in Git. Use the smallest packet that lets a skeptical reviewer decide.

## When to Use

- Starting a meaningful AI-assisted change.
- Updating a packet after scope, proof, risk, or release posture changed.
- Preparing a PR that needs evidence beyond normal review notes.
- Task preview, self-check, turnover, OPEX, or supplier trust has been activated and needs a record.

## When Not to Use

- The work has no durable artifact or review need.
- The request is only to browse or explain existing docs.

## Inputs

- Selected mode from `risk.md` or the classification skill.
- Questioning-attitude screen when uncertainty, AI authority, dependency trust, or release consequence is material.
- Templates under `templates/quick/` or `templates/standard/`.
- Affected files and proof commands.
- Existing packet if present.

## Process

1. Use `python tools/ng.py new <slug> --mode quick|standard`.
2. Fill only the decision-useful parts of each packet file.
3. Add HPI microtool records only when they change a decision or action.
4. Link to affected files, tests, reviews, source-map rows, and known gaps.
5. Keep status labels explicit: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
6. Validate with `python tools/ng.py validate .nuclear/changes/<slug>`.

## Outputs

- Quick packet: `risk.md`, `proof.md`.
- Standard packet: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Activated HPI records such as `turnover.md`, `self-check.md`, `opex.md`, or `supplier-trust.md` when consequence warrants them.
- Validator result.

## Verification

- Required files exist.
- Required links, exit criteria, and source-lineage notes are present.
- Proof or verification file includes evidence status.
- Relative packet links resolve.

## Escalation

- Escalate to Standard when Quick proof cannot answer the reviewer question.
- Escalate to human review when a stronger documented mode is activated.
- Stop if the packet becomes a long narrative without claim-to-evidence links.

## Common Rationalizations

- "We will fill it in after the PR." Packet evidence should shape the work, not decorate it after the fact.
- "Everything is obvious." If it matters to future review, preserve the assumption and evidence path.
- "One big packet is easier." One change per packet keeps review bounded.

## Red Flags

- Missing proof command or evidence link.
- Claims are broader than tests or review evidence.
- Packet files repeat each other instead of linking.

## Source-lineage note

This packet skill is an original Git-native workflow influenced by public configuration, lifecycle, assurance, secure development, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create a quality-assurance program.
