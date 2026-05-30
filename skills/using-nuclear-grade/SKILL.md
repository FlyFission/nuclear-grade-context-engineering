---
name: using-nuclear-grade
description: Turns an AI-assisted change into a clear evidence path. Picks a mode, sets up the change record, and plans the proof, then points to the charter and the goal anchor. Use when you start using this workflow on a change, a repo, or a release call. Do not use for a throwaway experiment with nothing worth reviewing.
---

# Using Nuclear-grade

## Overview

Use Nuclear-grade to turn AI-assisted work into a clear evidence path. Start by asking the real question the change has to answer. Then judge how high the stakes are. Build the smallest change record that does the job. Write down what the change must do. Prove the claims that matter. Then say the release decision out loud.

The repo charter (`.nuclear/charter.md`) holds the lasting rules every change follows. Each change also gets a goal anchor. The anchor states what that one change is for, so the work does not drift off course.

## When to Use

- A person or an AI agent will change code, tests, docs, prompts, tools, dependencies, or release evidence.
- A reviewer needs more than a commit message and a test result to judge the risk.
- Agent power, dependency trust, security, or release readiness is on the line.
- A team needs to follow the workflow: take the chosen path, or write down why it no longer fits.

## When Not to Use

- The work is a throwaway local note that nothing depends on.
- Someone asks for formal compliance, certification, a safety analysis, or a regulatory filing. This workflow does not provide those.
- The right next step is to contain an incident or roll back. Use the incident path first.

## Inputs

- The user request or the goal of the pull request.
- The diff, or the files the change is planned to touch.
- Any change records already under `.nuclear/changes/`.
- `WORKFLOWS.md`, `QUICKSTART.md`, and `docs/02-operating-system/activation-thresholds.md`.

## Process

1. Start with a questioning attitude. Name the decision question, the assumptions, the fact that would change the decision, the gaps in evidence, and when to stop.
2. Sort the change into Quick, Standard, or a stronger mode that a human reviews.
3. Create or find the change record under `.nuclear/changes/<slug>/`.
4. Write down the least you need: what the change must do, what it must prove, the files it touches, and the claims it must not make.
5. If the chosen workflow or template stops fitting the real situation, write down where you went off it and why.
6. Keep the build work tied to the claims and the evidence.
7. Move fast while ideas are easy to undo. Slow down before you accept a claim, write public wording, save an approved version, ship a release, or change what an agent may do.
8. Run the checker on Quick or Standard records.
9. Stop before release if the evidence status, the rollback plan, the monitoring, the decision, the trigger for saving a version, or the legal wording is unclear.

## Outputs

- The chosen mode and the reason for it.
- The path to the change record.
- The evidence commands you need, or the gaps stated plainly.
- A note where you stepped off the normal path.
- The release posture: ship, block, defer, or ship with named leftover risk.

## Verification

- `python tools/ng.py status .`
- `python tools/ng.py validate .nuclear/changes/<slug>`
- A reviewer can answer what changed, why it matters, what proved it, and what is still uncertain.

## Escalation

- Move from Quick to Standard when the change affects users, dependency trust, permissions, data, AI power, or the release.
- Move to human review when the work touches regulated, safety-critical, security-critical, or procurement work, or any claim about outside trust.
- Stop when asked to claim formal assurance or compliance. This workflow does not grant either.

## Common Rationalizations

- "The tests pass, so we don't need a record." Passing tests do not save the assumptions, the scope, the leftover risk, or the release decision.
- "The agent remembers the context." Chat history is not a lasting review record.
- "This is only documentation." Public docs can create claims about law, trust, and assurance.
- "The template is just ceremony." Use the smallest useful version. But write down when the chosen path no longer fits.

## Red Flags

- The record cannot name a single claim that matters.
- The evidence is loose prose instead of commands, links, reviews, or named gaps.
- The work says or hints at compliance, approval, safety, security, or formal verification and validation. None of those are provided here.

## Source-lineage note

This skill is part of an original workflow. It draws on public ideas from high-consequence engineering, secure development, software assurance, and configuration discipline, mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
