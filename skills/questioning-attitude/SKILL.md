---
name: questioning-attitude
description: Challenges the assumptions behind a change before an agent builds, merges, or releases, and names the one fact that would change the decision. Use when a request, plan, diff, dependency, agent action, public claim, or release is vague, high-stakes, or easy to talk yourself into. Do not use for a tiny, obvious, easy-to-undo edit, or when someone wants a formal guarantee.
---

# Questioning Attitude

## Overview

This is the front door. Before an agent builds, merges, or releases, find the real question the work has to answer. Trust facts over confidence. Say out loud what you are not sure about. And stop the moment a doubt would change what you decide.

## Decision contract

- **Claim checked:** the change is restated as one decision question evidence could settle, each assumption is checked, marked a gap, or assigned, and the one fact that would change the decision is named.
- **Artifact observed:** the request/diff/plan/dependency -> a questioning-attitude write-up (or `questioning-attitude.md`) of assumptions, unknowns, shaky sources, and stop conditions.
- **Decision affected:** warn -- the Quick/Standard mode choice routed into `rating-change-risk`, and whether to proceed, escalate, or stop.
- **Failure class:** unexamined-assumption (an unchecked assumption driving the build, or a claim with no evidence).
- **Next action:** raise the mode or escalate/stop when a load-bearing assumption is a gap; otherwise proceed with the gaps named.

## When to Use

- A request is vague, high-stakes, or easy to talk yourself into.
- A diff, plan, dependency, prompt, model, tool, or release claim needs a skeptical second look.
- A reviewer asks "what are we assuming?" or "what would make this wrong?"
- An agent is about to get power over files, commands, the network, credentials, approvals, or releases.
- You see the warning signs of mistakes: too many files, stale memory, hidden links between parts, a messy workspace, grabbing the first answer, or pressure to be done.

## When Not to Use

- The task is a tiny edit with obvious proof and no new trust boundary.
- An incident is live and you must contain it before you analyze it.
- Someone is asking for a formal guarantee, a certification, a safety analysis, or regulatory approval.

## Inputs

- The request, issue, pull request, diff, or path to the change record.
- The files, dependencies, prompts, models, tools, data, and release items the change touches.
- What you already know, what you are assuming, the evidence you have, and the gaps.
- Any related past records, lessons from operation, or source notes.

## Process

1. Restate the change as one clear question that evidence could prove right or wrong.
2. List the assumptions that have to be true for the change to work.
3. Sort what you know into facts, assumptions, unknowns, and "how good is this source?"
4. Spot the uncertainty, the danger words, the warning signs, the steps where mistakes are likely, and any hidden reasons this should be treated as a standard change. Name the work type — greenfield, brownfield, defect-fix, refactor-migration — and apply every type that fits, because more than one can (a production defect fix is brownfield and defect-fix; a live migration is brownfield and refactor-migration). Ask the questions every applicable type forces: brownfield and migration force blast-radius and rollback-of-state questions; a defect forces a reproduction and a regression guard; greenfield forces interface and acceptance questions. Work type is orthogonal to the Quick/Standard/Nuclear mode, which grades rigor, not kind. See `docs/02-operating-system/work-type-lens.md`.
5. Ask what evidence would change the decision. If nothing could change it, the question is not useful yet.
6. Check the facts before you trust memory, confidence, or anything an agent generated.
7. Name the conditions that should make you pause, hold, or escalate.
8. Pick the next step: quick proof, a standard spec, a briefing pack, a handoff, a self-check, a control record, a goal or drift check, or a release decision.

## Outputs

- A short questioning-attitude write-up, or a `questioning-attitude.md` file.
- Assumptions that are now checked, and the ones still open.
- What you know, what you don't, and any shaky sources.
- The triggers for choosing a mode or escalating.
- The evidence you need before you execute, verify, review, decide, or save the version.
- The work type(s), and the questions every applicable type forces.
- The one fact that would change the decision.

## Verification

- Every assumption is written down and is either checked, marked as a gap, or assigned to someone.
- The chosen mode follows the evidence, not what is easiest or fastest.
- The stop conditions are concrete enough that an agent or a reviewer can actually obey them.
- The next step is named.

## Escalation

- Escalate when facts are missing and the change affects users, data, security, dependencies, agent power, operations, or a release.
- Stop when a claim has no evidence behind it.
- Get a second, independent reviewer when the only thing holding the decision up is one agent's read of the situation.

## Common Rationalizations

- "It worked last time." Past success does not prove the setup is still under control.
- "The agent seems confident." Confidence is not a source.
- "The first answer sounded right." Sounding right is not the same as checked.
- "We can sort the risk later." The mode depends on the assumptions and unknowns you have right now.
- "It's just docs." Public wording can change who trusts you and how they use the work.

## Red Flags

- Unchecked assumptions are driving the build.
- The record names the proof only after the work is already done.
- Standard-change triggers get waved off because the diff is small.
- Words like "probably", "should", "safe", "secure", "approved", or "compliant" show up with no evidence.
- Release text says "safe", "secure", "approved", or "compliant" without a qualified outside authority behind it.

## Prompt

```text
Question this change the Nuclear-grade way.

Inputs:
- request/diff/change record:
- affected items:
- known assumptions:
- evidence available:
- limits or deadlines:

Return:
- the decision question in one sentence
- the work type(s), all that apply (a production defect is brownfield and defect-fix), and the questions each forces
- the evidence that would change the decision
- the assumptions that must be true
- known facts, unknowns, danger words, and worries about how good the sources are
- facts to check before work continues
- warning signs, signs an agent is about to slip, steps where mistakes are likely, and hidden reasons to treat this as a Standard change
- evidence needed before you execute, verify, review, decide, or save the approved version (the baseline)
- conditions that should make you pause or ask for help
- the next thing to produce: Quick proof, Standard spec, context pack, handoff, self-check, a record of what stays under control (the controlled items), or a release decision

Trust facts over confidence. Do not imply formal verification and validation, compliance, certification, safety, security, or regulatory adequacy.
```

## Source-lineage note

This skill is an original software-workflow translation of the questioning-attitude, validate-your-assumptions, pause-when-unsure, and review habits from DOE-HDBK-1028-2009, the Human Performance Improvement Handbook, Volumes 1 and 2, used as public idea lineage. It does not create DOE compliance, formal assurance, safety, security, certification, or regulatory adequacy.
