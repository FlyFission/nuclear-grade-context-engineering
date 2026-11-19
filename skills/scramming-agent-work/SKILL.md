---
name: scramming-agent-work
description: Places agent work on hold and produces a plain-language status and reversible-action map. Use when the operator says SCRAM, stop agents, hold work, or requests an immediate stop-and-debrief. Do not use for routine reflection or brainstorming.
---

# SCRAM — Stop, Account, Report, Assess, Maintain Hold

## Overview

`/ng-scram` is an operator-initiated **hold and turnover** action, not a brainstorm, review verdict, or an invitation to change direction. First stop initiating work, then account for what actually stopped, explain where the work stands in ordinary language, identify reversible versus irreversible effects, and hand control to the operator. A skill **cannot guarantee that all external agents, subprocesses, scheduled jobs, or remote tools stopped**. Never report a global stop unless host/orchestrator acknowledgements and independent checks support it.

## Decision contract

- **Claim checked:** work has ceased *to the verified scope*, with every running or unknown actor named and unverified stops disclosed.
- **Artifact observed:** live agent/orchestrator status when available, current workspace, change packet, tool trace, commits, running jobs, and pending actions -> SCRAM status/turnover note.
- **Decision affected:** block -- new voluntary delegated work, writes, executions and external effects in this session remain on hold pending explicit operator release; host/runtime enforcement is separately verified.
- **Failure class:** phantom-stop (claiming everyone stopped while child agents, jobs, or external effects continue), lost-state or unsafe-resume.
- **Next action:** give the operator a concise debrief and maintain hold until an authorized, evidence-backed resume decision.

## When to Use

- The user explicitly says `/ng-scram`, `SCRAM`, `stop all agents`, `freeze work`, or requests a stop-and-status debrief.
- Ongoing delegated work is producing surprising, unbounded, costly, or irreversible side effects.
- A live operator needs a short status, evidence of actual stop coverage, or a handoff before resetting direction.

## When Not to Use

- For merely questioning an architecture or generating alternatives; use `reconsidering-the-approach`.
- For investigating ordinary assumptions without a hold; use `questioning-attitude`.
- For changing mission direction after work is safe; use `staying-on-mission`.
- For stabilizing production harm; initiate containment through `responding-to-incidents` first, and retain any needed incident responders.
- For claiming a physical reactor SCRAM, hardware E-stop, or safety-system action; this is a software-workflow command only.

## Inputs

- Current session identity, host/runtime and connected agent IDs; operator's stop scope.
- Live task list, jobs, tool calls, queued work, latest known commits or files, and trace/packet references.
- Known side effects, active credentials and scheduled external actions, and the person authorized to resume.

## Process

1. **Honor stop first.** Do not brainstorm, finish the current feature, commit, deploy, queue new child work or send further mutating tool calls. If an authorized host cancel/stop mechanism exists, invoke it for the named scope. Do not assume that sending a chat message interrupts already-running calls.
2. **Record stop coverage honestly.** For each actor/job mark `STOPPED (acknowledged)`, `STOP REQUESTED (unconfirmed)`, `STILL RUNNING`, or `UNKNOWN`; state timestamp/source if available. Where a real out-of-band runtime stop controller exists, use its verified report. If absent, explain that this is only a cooperative in-session hold. Never say "all agents stopped" on the strength of this skill alone.
3. **Prevent further work.** In the current session do not resume delegation, code edits, execution, pushing, release, or external activity until an explicit operator resume. Never disable protective hooks or approval gates. Do not kill unrelated processes, discard unsaved work, rewrite history, or revoke credentials without separate authority. Existing external jobs may remain active and must be listed.
4. **Take a bounded, read-only snapshot.** Use current visible context and permitted read-only status commands if they do not undermine the hold. Capture last completed step, latest known in-flight step, branch/commit, changed artifacts, tests actually run, active approvals, and open evidence gaps. Do not invent a clean working tree or a completed cancellation.
5. **Classify reversibility.** Separate (a) uncommitted local changes, (b) committed/unmerged changes, (c) pushed/shared changes, (d) external or published effects, and (e) possibly irreversible actions such as deleted data, sent notifications or triggered workloads. Say what can be rolled back mechanically, what requires a compensating action or human approval, and what cannot be reliably undone. Never execute rollback on SCRAM alone.
6. **Debrief plainly.** Lead with a one-sentence overall state and actual stop coverage. Then report what was done, what is in progress/uncertain, reversible versus non-reversible effects, current risks, and the next safe choice. Use `handing-off-work` for a fuller turnover and `recording-what-an-agent-did` if trace evidence matters; avoid duplicating their full outputs.
7. **Maintain hold.** End in `HELD — AWAITING OPERATOR`, or `PARTIAL HOLD — EXTERNAL WORK UNCONFIRMED`. The stop does not lift because the debrief is complete. Resume requires a fresh operator instruction, a current state/authority check, and reclassification if scope changed. Any host-enforced latch may only be cleared by its authorized control plane.

## Outputs

- Plain-language one-line state, scope and actual STOPPED / REQUESTED / RUNNING / UNKNOWN coverage.
- Last proven completed action; current position, changed files/commits, unfinished actions and evidence gaps.
- Reversibility map, irreversible or external side effects, unconfirmed agents and immediate risks.
- Optional `scram.md` linked into the current packet when doing so does not require prohibited writes; otherwise produce the report in chat and leave a pending record.
- A hold disposition and operator choices; no autonomous resumption or rollback.

## Verification

- Every claim of a stopped agent/job has runtime evidence; lack of access is explicitly UNKNOWN.
- Stop coverage distinguishes current chat from remote workers and persistent jobs.
- The status distinguishes verified completed work from planned or in-flight work.
- Rollback/compensation is described without executing it.
- No mutation, child spawn, release or unilateral restart happened after the stop request.
- Report is concise enough to understand without raw transcripts, and it includes gaps and the owner of resume.

## Escalation

- If active production harm exists, use `responding-to-incidents` to contain it; a SCRAM must not disable containment or protective monitoring.
- If a remote agent cannot be stopped, immediately mark PARTIAL HOLD, disclose it and provide the authorized shutdown path. Do not call that a successful stop.
- Escalate uncertain external effects, irreversible actions, lost trace, or inability to establish safe state to the responsible operator.
- No skill text can kill arbitrary processes or enforce a distributed stop without a separately deployed, independent execution-plane control.

## Common Rationalizations

- "I said stop, so every agent stopped." A model's statement is not an acknowledgement.
- "We should finish one more edit to preserve state." SCRAM suspends new mutations; preserve state read-only and defer saving until authorized.
- "The green tests prove safe to resume." Tests do not authorize a restart.
- "Git revert undoes everything." External effects, migrations and messages may not be reversible.
- "The status looks clean." Unknown workers and running external jobs must remain visible.

## Red Flags

- Child agents continue receiving tasks after SCRAM or stop coverage is unknown.
- A debrief reports the plan as completed work or hides unresolved tool calls.
- The tool changes the repo while claiming to be read-only.
- An agent clears the hold or resumes itself.
- A kill command affects unrelated user processes or disables incident response.

## Prompt

```text
SCRAM. Stop initiating actions now. Request host-supported cancellation of in-scope agents and queued work if available. Do not assume external processes stopped.

Produce a short operator debrief:
- Stop coverage: STOPPED / STOP REQUESTED / STILL RUNNING / UNKNOWN (with evidence).
- What finished and what remains in flight, in everyday language.
- Current branch/commit, changed artifacts, and checks actually run if known.
- What is safely reversible, what needs a compensating action, and what cannot be undone.
- The most important unresolved risk and the next safe operator choice.

Do not commit, push, roll back, delete, deploy, or restart anything merely to prepare the report. Maintain HELD or PARTIAL HOLD until an explicit operator resume and applicable control-plane clearance. No software skill guarantees global cancellation.
```

## Source-lineage note

Inspired by nuclear-operational stop-work, human performance improvement, plant status control, and structured turnover as workflow analogies only. This is not a reactor SCRAM, emergency shutdown safety function, safety approval, or formal nuclear compliance.
