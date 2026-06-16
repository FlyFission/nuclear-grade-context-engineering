---
name: creating-change-records
description: Creates or updates Quick or Standard change records, adds the required files, and refreshes what each claim must prove for an evidence-backed pull request. Use when starting or revising a change record. Do not use for a one-off throwaway script, or for work that belongs in an existing record rather than a new one.
---

# Creating Change Records

## Overview

A change record keeps the whole story in Git, together: the scope, what the change must do, the plan, the trace from claim to evidence, the proof, and the release decision. Use the smallest record that still lets a doubting reviewer decide.

## Decision contract

- **Claim checked:** the record carries every file its mode requires, with the required links, exit criteria, source-lineage notes, and plain status labels (`pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`) present and the internal links resolving.
- **Artifact observed:** the mode from `risk.md` and the `templates/quick/` or `templates/standard/` templates -> a Quick record (`risk.md`, `proof.md`) or Standard record (`risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`) plus the validator result.
- **Decision affected:** block -- whether the packet is structurally complete and valid (`python tools/ng.py validate` pass/fail).
- **Failure class:** incomplete-record (a missing file, broken internal link, or proof command absent).
- **Next action:** add the missing file or link and rerun the validator; raise Quick to Standard or human review when proof cannot answer the reviewer.

## When to Use

- You are starting a real AI-assisted change.
- You are updating a record after the scope, proof, risk, or release posture changed.
- You are preparing a pull request that needs evidence beyond the usual review notes.
- A preview, a self-check, a handoff, a lesson from operation (OPEX), or a supplier trust check is in play and needs a record.

## When Not to Use

- The work leaves no lasting artifact and no need for review.
- The request is only to browse or explain existing docs.

## Inputs

- The chosen mode from `risk.md` or from the risk-rating skill.
- A questioning-attitude screen, when uncertainty, AI power, dependency trust, or release stakes are real.
- Templates under `templates/quick/` or `templates/standard/`.
- The files the change affects and the proof commands.
- An existing record, if there is one.

## Process

1. Run `python tools/ng.py new <slug> --mode quick|standard`.
2. Fill in only the parts of each file that help someone decide.
3. Add habit records (self-check, handoff, and the like) only when they change a decision or an action.
4. Link to the files affected, the tests, the reviews, the source-map rows, and the known gaps.
5. Keep status labels plain: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
6. Run `python tools/ng.py validate .nuclear/changes/<slug>`.

## Outputs

- Quick record: `risk.md`, `proof.md`.
- Standard record: `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`.
- Habit records such as `turnover.md`, `self-check.md`, `opex.md`, or `supplier-trust.md` when the stakes call for them.
- The checker result.

## Verification

- The required files exist.
- The required links, exit criteria, and source-lineage notes are present.
- The proof or verification file states the evidence status.
- The links inside the record resolve.

## Escalation

- Move from Quick to Standard when Quick proof cannot answer the reviewer's question.
- Move to human review when a stronger written mode is in play.
- Stop if the record turns into a long story with no links from claim to evidence.

## Common Rationalizations

- "We will fill it in after the pull request." The evidence should shape the work, not dress it up afterward.
- "Everything is obvious." If it matters to a future review, save the assumption and the path to the evidence.
- "One big record is easier." One change per record keeps the review small enough to do well.

## Red Flags

- A missing proof command or evidence link.
- Claims that reach past what the tests or the review evidence cover.
- Record files that repeat each other instead of linking.

## Prompt

```text
Create or update a Nuclear-grade change record.

Inputs:
- slug: <slug>
- mode: <quick|standard>
- scope: <summary>
- affected files/assets: <list>
- questioned assumptions: <list>
- what the change must prove: <command/review/evidence>
- safety-habit (HPI) records started: <turnover/self-check/opex/supplier-trust/none>

Use the repo templates. Keep the record short. Lean on links, and point at evidence. Include the required links, the conditions for being done, and a note on where the ideas come from. Do not imply formal assurance or compliance.
```

## Source-lineage note

This change-record skill is an original Git-native workflow. It draws on public configuration, lifecycle, assurance, secure-development, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. It does not create a certified quality assurance program.
