---
name: using-nuclear-grade
description: The always-first router for AI-assisted work. Perform a bounded read-only preflight, then state the mode and controlling fact before mutation or external effect; route to the matching record and proof. Use at the start of any change, repo adoption, or release call. Do not use for a throwaway experiment with nothing worth reviewing.
---

# Using Nuclear-grade

## Overview

This is the always-first router for Nuclear-grade work. First perform a bounded read-only preflight against the request and accessible source of truth so classification rests on evidence rather than guesswork. Then state the mode the change earns and the one fact that sets it before the first mutation or external side effect. Move fast while ideas are throwaway; slow down when the work becomes a promise. Build the smallest change record that does the job, prove the claims that matter, and say the release decision out loud.

The repo charter (`.nuclear/charter.md`) holds the lasting rules every change follows. Each change also gets a goal anchor — what that one change is for — so the work does not drift off course.

## Decision contract

- **Claim checked:** a bounded read-only preflight supports the classification; the administrative floor, Quick, or Standard-plus and its one controlling fact are declared before the first mutation, external side effect, credential use, publication, or release action; any Standard-plus trap forces the stronger mode.
- **Artifact observed:** the request plus bounded read-only inspection of the source of truth and any record under `.nuclear/changes/` -> the declared mode, controlling fact, and change-record path.
- **Decision affected:** block -- mutation or an external side effect cannot begin until the evidence-backed mode and controlling fact are declared.
- **Failure class:** unclassified-or-downgraded-start (mutation or external effect began before a mode, or a Standard-plus trap was waved off as Quick).
- **Next action:** inspect read-only evidence when needed, declare the mode before mutation or external effect, and raise to Standard or human review when a trap or outside-trust claim appears.

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

**Preflight read-only, then classify out loud.** Perform only the bounded read-only preflight needed to inspect the request, repository state, existing records, and other accessible source of truth. Do not write files, use credentials, call a mutating API, publish, deploy, merge, or release during preflight. Then state the mode this change earns: the **administrative floor** (no packet; the commit message is the record), **Quick**, or **Standard-plus** (Standard, or a stronger human-reviewed mode), plus the **one fact** that sets it. This declaration of intent is required before the first mutation, external side effect, credential use, publication, or release action. Re-state it whenever the change grows.

The **administrative floor** is the mode below Quick: it fits only a purely administrative, instantly reversible change that crosses no trust boundary — a typo, a comment, formatting, a dead-link fix, a doc-only bump — and carries no packet, with the commit message (the files changed and the one-line reason) as its record. Any trap below lifts it to at least Quick, and **when in doubt it is Quick, not the floor**. The floor never waives the always-on Core habits (see `docs/02-operating-system/activation-thresholds.md` and `MAXIMS.md`).

You MUST treat the change as **Standard-plus**, never Quick, when it touches any of these — the cheap "it's only small" traps:

- authentication, permissions, or secrets;
- behavior a user can see;
- data handling, schema, or a migration;
- a dependency or a dependency manifest;
- a model id, a prompt, or what a tool or agent may do;
- CI or `.github/`;
- a release, a saved baseline, or claim-bearing public wording.

When one is present, justify the mode in the record or escalate — do not let "it is a one-line change" downgrade it.

Then:

1. **Question first.** Name the decision question, the assumptions, the one fact that would change the decision, the evidence gaps, and the stop conditions.
2. **Build the smallest record that fits the mode.** On the administrative floor there is no packet — the commit message, naming the files changed and the one-line reason, is the record. Otherwise build the smallest record that fits the mode under `.nuclear/changes/<slug>/`. Adopting for the first time? Take the Core 7 habits from `CORE.md` and switch on ancillary clusters by trigger, not all at once.
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

- "It's a small change, so it's Quick." Size is not stakes. A one-line edit to auth, a dependency, a model id, a migration, or claim-bearing public wording is Standard-plus.
- "I must classify before I can inspect anything." A guess is not a control. Use a bounded read-only preflight, then declare the mode before mutation or external effect.
- "I'll classify after I start editing." The mode call is the cheapest control and the one most prone to motivated error under pressure. Read-only inspection may precede it; mutation may not.
- "The tests pass, so we don't need a record." Passing tests do not save the assumptions, the scope, the leftover risk, or the release decision.
- "The agent remembers the context." Chat history is not a lasting review record.
- "This is only documentation." Public docs can create claims about law, trust, and assurance.
- "The template is just ceremony." Use the smallest useful version. But write down when the chosen path no longer fits.

## Red Flags

- Mutation, credential use, publication, or another external side effect began before a mode and controlling fact were declared.
- The record cannot name a single claim that matters.
- The evidence is loose prose instead of commands, links, reviews, or named gaps.
- The work says or hints at compliance, approval, safety, security, or formal verification and validation. None of those are provided here.

## Source-lineage note

This skill is part of an original workflow. It draws on public ideas from high-consequence engineering, secure development, software assurance, and configuration discipline, mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
