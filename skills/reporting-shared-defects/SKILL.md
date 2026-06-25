---
name: reporting-shared-defects
description: Routes a defect found in a shared or supplied artifact (a shared prompt, skill, dependency, model, eval, or template) to the downstream teams, agents, and releases that depend on it, not just a local fix. Use when a discovered defect affects others who consume the same artifact. Do not use for a defect local to your own change, which is an ordinary fix, or for a live incident still being contained.
---

# Reporting Shared Defects

## Overview

A defect you find in something other people use is two problems, not one. The first is the bug itself, which you fix. The second is that every other consumer of that shared or supplied artifact still carries it and does not know. Fixing your own copy and moving on leaves them exposed. This skill makes the outward notice a first-class obligation alongside the local fix, so a defect in a shared prompt, skill, dependency, model, eval, or template reaches the teams, agents, and releases that depend on it.

## Decision contract

- **Claim checked:** a defect found in a shared or supplied artifact has been evaluated for downstream impact and either notified to the affected consumers with an owner and a tracking link, or recorded as not-reportable with a reason -- never fixed locally and forgotten.
- **Artifact observed:** the defect, the shared or supplied artifact it lives in, and who consumes it -> a shared-defect report (description, affected consumers, severity, notice sent, owner, link) tied to the OPEX record and the deficiency register.
- **Decision affected:** block -- whether downstream consumers are notified (the local fix is not complete until they are), or the defect is recorded as not-reportable with a reason.
- **Failure class:** silent-local-fix (a defect in a shared artifact patched in one place while other consumers keep carrying it, unnotified).
- **Next action:** evaluate downstream impact and notify the affected consumers or owners; escalate when the defect touches security, data integrity, credentials, privacy, or a public release.

## When to Use

- You found a defect in something others also use: a shared prompt, skill, command, template, dependency pin, model identifier, eval harness, or config.
- A fix you are about to make corrects your own copy but leaves other consumers exposed.
- An incident or OPEX lesson traced the cause to a shared or supplied artifact.

## When Not to Use

- The defect is local to your own change and affects no other consumer; that is an ordinary fix.
- A live incident still needs containment first -- stabilize with `responding-to-incidents`, then report.
- The artifact has no other consumers, and none are foreseeable.

## Inputs

- The defect, where it lives, and how it was found.
- The shared or supplied artifact and its consumers: teams, agents, releases, downstream repos.
- The severity, and how it could fail for a consumer who does not know about it.
- Any related incident, OPEX lesson, or deficiency entry, and the local fix already made.

## Process

1. Confirm the defect lives in a shared or supplied artifact, not only in your own copy.
2. Evaluate downstream impact: who consumes it, and how it could fail for a consumer who does not know -- separate an honest defect from a non-issue.
3. Make the local fix, but do not treat the work as done: the local fix and the outward notice are separate obligations.
4. Notify the affected consumers or owners with the defect, its severity, and the fix or workaround; give the notice an owner and a tracking link.
5. Record the report and tie it to the OPEX record (`learning-from-experience`) and the deficiency register (`tracking-deficiencies`) so it does not vanish.
6. If the defect cannot reach others, record that judgment with its reason instead of sending a notice.

## Outputs

- A shared-defect report: description, affected consumers, severity, notice sent (to whom, when), owner, and tracking link.
- The local fix, plus the outward notice or a recorded reason none was needed.
- Links to the OPEX record and the deficiency entry.

## Verification

- Every reportable defect has a notice to named consumers, an owner, and a tracking link -- not just a local patch.
- Not-reportable calls record the reason and who decided.
- The report links to the OPEX and deficiency records, so the duty is auditable.

## Escalation

- Escalate when the shared defect touches security, credentials, data integrity, privacy, or a public release.
- Require a qualified or independent reviewer when the consumers are external, or the defect could cause a substantial downstream failure.
- Stop and report upward when no one will own the outward notice.

## Common Rationalizations

- "I fixed it in my repo." Your copy is fixed; every other consumer still carries it.
- "They will pull the update eventually." Silent propagation is not notification -- name them and tell them.
- "It is probably fine for the others." That is a judgment to record with a reason, not an assumption to skip.

## Red Flags

- A shared prompt, skill, dependency, or model defect fixed in one place with no notice to other consumers.
- A report with no named consumers, no owner, or no tracking link.
- A "known issue" in a shared artifact living in chat or memory instead of a routed notice.

## Prompt

```text
Route a Nuclear-grade shared-defect report.

Inputs:
- defect and where it lives:
- shared or supplied artifact (prompt/skill/command/template/dependency/model/eval/config):
- consumers (teams, agents, releases, downstream repos):
- severity and how it fails for a consumer who does not know:
- local fix already made:
- related incident / OPEX / deficiency:

Return:
- a confirmation the defect lives in a shared or supplied artifact, not just your copy
- the downstream impact: who is affected and how
- the outward notice: to whom, what they need to do, the owner, and a tracking link
- the tie to the OPEX record and the deficiency register
- or, if it cannot reach others, the recorded reason no notice is needed
- escalation when security, credentials, data integrity, privacy, or a public release is touched

Treat the local fix and the outward notice as separate obligations. Do not imply formal assurance, compliance, or regulatory adequacy.
```

## Source-lineage note

This skill is an original software-workflow translation of the evaluate-and-notify duty for defects in supplied or shared items, informed by 10 CFR Part 21 (§21.21) as public source lineage and grounded in the operating-experience and corrective-action habits in DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md`. It does not create DOE, NRC, or any compliance, formal assurance, safety, security, certification, or regulatory adequacy.
