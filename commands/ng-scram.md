---
description: "Places agent work on hold and produces a plain-language status and reversible-action map."
disable-model-invocation: true
---

# ng-scram

Portable command prompt generated from `skills/scramming-agent-work/SKILL.md`. To change it, edit the skill and run `nuclear-grade gen-commands`.

## Use when

- The user explicitly says `/ng-scram`, `SCRAM`, `stop all agents`, `freeze work`, or requests a stop-and-status debrief.
- Ongoing delegated work is producing surprising, unbounded, costly, or irreversible side effects.
- A live operator needs a short status, evidence of actual stop coverage, or a handoff before resetting direction.

## Do not use when

- For merely questioning an architecture or generating alternatives; use `reconsidering-the-approach`.
- For investigating ordinary assumptions without a hold; use `questioning-attitude`.
- For changing mission direction after work is safe; use `staying-on-mission`.
- For stabilizing production harm; initiate containment through `responding-to-incidents` first, and retain any needed incident responders.
- For claiming a physical reactor SCRAM, hardware E-stop, or safety-system action; this is a software-workflow command only.

## Inputs

- Current session identity, host/runtime and connected agent IDs; operator's stop scope.
- Live task list, jobs, tool calls, queued work, latest known commits or files, and trace/packet references.
- Known side effects, active credentials and scheduled external actions, and the person authorized to resume.

## Prompt text

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

## Verification

- Every claim of a stopped agent/job has runtime evidence; lack of access is explicitly UNKNOWN.
- Stop coverage distinguishes current chat from remote workers and persistent jobs.
- The status distinguishes verified completed work from planned or in-flight work.
- Rollback/compensation is described without executing it.
- No mutation, child spawn, release or unilateral restart happened after the stop request.
- Report is concise enough to understand without raw transcripts, and it includes gaps and the owner of resume.

## Full skill

For the process, outputs, escalation, red flags, and source lineage, see `skills/scramming-agent-work/SKILL.md`. This command sets up evidence for engineering review; it does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy (see `DISCLAIMER.md`).
