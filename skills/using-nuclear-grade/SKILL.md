---
name: using-nuclear-grade
description: The always-first router for AI-assisted work — before acting, state the mode (Quick or Standard-plus) and the one fact that sets it, then set up the matching change record and plan the proof. Use at the start of any change, repo adoption, or release call. Do not use for a throwaway experiment with nothing worth reviewing.
---

# Using Nuclear-grade

## Overview

This is the always-first router for Nuclear-grade work. Before you act, classify the change by consequence and route to the matching rigor — move fast while ideas are throwaway, slow down the moment the work becomes a promise. Start by asking the real question the change must answer, then state the mode it earns and the one fact that sets it. Build the smallest change record that does the job, prove the claims that matter, and say the release decision out loud.

The repo charter (`.nuclear/charter.md`) holds the lasting rules every change follows. Each change also gets a goal anchor — what that one change is for — so the work does not drift off course.

## Decision contract

- **Claim checked:** this change is named the cheapest-fitting mode -- Quick or Standard-plus -- with the one fact that sets it stated before the first tool call, and any Standard-plus trap (auth, user-visible, data, dependency, model/prompt/agent power, CI, release) forces the stronger mode.
- **Artifact observed:** the request, diff, and any record under `.nuclear/changes/` -> the declared mode, its one-fact reason, and the change-record path that routes the work into its skill cluster.
- **Decision affected:** block -- the mode declared before the first tool call (Quick or Standard-plus) and the skill cluster it routes into.
- **Failure class:** unclassified-or-downgraded-start (work begun before a mode, or a Standard-plus trap waved off as Quick).
- **Next action:** state the mode before the first tool call; raise to Standard or human review when a trap or outside-trust claim appears.

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

**Classify first — out loud.** Before the first tool call, state the mode this change earns — **Quick**, or **Standard-plus** (Standard, or a stronger human-reviewed mode) — and the **one fact** that sets it. This is a declaration of intent, not a request for permission: you name the mode and act. Re-state it whenever the change grows.

You MUST treat the change as **Standard-plus**, never Quick, when it touches any of these — the cheap "it's only small" traps:

- authentication, permissions, or secrets;
- behavior a user can see;
- data handling, schema, or a migration;
- a dependency or a dependency manifest;
- a model id, a prompt, or what a tool or agent may do;
- CI or `.github/`;
- a release, a saved baseline, or public wording.

When one is present, justify the mode in the record or escalate — do not let "it is a one-line change" downgrade it.

Then:

1. **Question first.** Name the decision question, the assumptions, the one fact that would change the decision, the evidence gaps, and the stop conditions.
2. **Build the smallest record that fits the mode** under `.nuclear/changes/<slug>/`. Adopting for the first time? Take the Core 7 habits from `CORE.md` and switch on ancillary clusters by trigger, not all at once.
3. **Write the least you need:** what the change must do, what it must prove, the files it touches, and the claims it must not make.
4. **Keep build work tied to the claims and their evidence.** If the chosen path stops fitting, write down where you left it and why.
5. **Slow down at the promise boundary** — before you accept a claim, write public wording, save an approved version, ship a release, or change what an agent may do.
6. **Run the checker** on Quick or Standard-plus records (`python tools/ng.py validate .nuclear/changes/<slug>`).
7. **Stop before release** if the evidence status, the rollback, the monitoring, the decision, the baseline trigger, or the legal wording is unclear.

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

- "It's a small change, so it's Quick." Size is not stakes. A one-line edit to auth, a dependency, a model id, a migration, or public wording is Standard-plus.
- "I'll classify it later." The mode call is the cheapest control and the one most prone to motivated error under pressure. State it before the first tool call, not after the diff exists.
- "The tests pass, so we don't need a record." Passing tests do not save the assumptions, the scope, the leftover risk, or the release decision.
- "The agent remembers the context." Chat history is not a lasting review record.
- "This is only documentation." Public docs can create claims about law, trust, and assurance.
- "The template is just ceremony." Use the smallest useful version. But write down when the chosen path no longer fits.

## Red Flags

- Work began before a mode was declared. The classification is the entry gate; skip it and everything after is on the honor system.
- The record cannot name a single claim that matters.
- The evidence is loose prose instead of commands, links, reviews, or named gaps.
- The work says or hints at compliance, approval, safety, security, or formal verification and validation. None of those are provided here.

## Source-lineage note

This skill is part of an original workflow. It draws on public ideas from high-consequence engineering, secure development, software assurance, and configuration discipline, mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
