# Nuclear-grade Command Prompts

These are portable command prompts: plain Markdown prompt cards you can paste into an AI coding agent or wire into your own setup. This first release (v0) does not ship a packaged plug-in for any one platform.

## The prompts

| Prompt | Use it when | What you get |
|---|---|---|
| [`ng-question`](commands/ng-question.md) | You want to challenge assumptions before you build, review, or release | Assumptions, gaps, and stop conditions |
| [`ng-classify`](commands/ng-classify.md) | You need to pick how careful to be | The chosen mode and what it must prove |
| [`ng-new`](commands/ng-new.md) | You are starting a change record | The record files |
| [`ng-what-to-control`](commands/ng-what-to-control.md) | You need to decide what to keep under control | A short list of what to control |
| [`ng-impact`](commands/ng-impact.md) | You want to know what else a change touches | A list of ripple effects and re-checks |
| [`ng-baseline`](commands/ng-baseline.md) | You want to record the version everyone agreed is correct | A saved known-good record |
| [`ng-context-pack`](commands/ng-context-pack.md) | You are about to hand an agent a focused task | A tight briefing pack |
| [`ng-turnover`](commands/ng-turnover.md) | You are passing unfinished work to another agent, person, reviewer, releaser, or your future self | A clean handoff record |
| [`ng-self-check`](commands/ng-self-check.md) | An agent is about to do something risky and should check itself first | A short self-check record |
| [`ng-prove`](commands/ng-prove.md) | You need to tie claims to evidence | A claim-to-evidence table |
| [`ng-ship-review`](commands/ng-ship-review.md) | You have to make a release call | A ship-or-hold record |
| [`ng-learn`](commands/ng-learn.md) | A near miss, bad handoff, surprise, or incident should turn into a lasting fix | A lessons-learned record |
| [`ng-trust-check`](commands/ng-trust-check.md) | You are bringing in a dependency, model, API, SaaS, or generated artifact you did not write | A trust check tied to how you will use it |
| [`ng-source-check`](commands/ng-source-check.md) | You are about to cite a source | Wording that is honest about the source |
| [`ng-legal-check`](commands/ng-legal-check.md) | You are reviewing license and safety wording | Wording that stays inside the real limits |
| [`ng-drift-check`](commands/ng-drift-check.md) | You suspect the work has drifted from its goal | A re-anchor, escalate, or stop decision |
| [`ng-code-review`](commands/ng-code-review.md) | You are reviewing a diff or module for sloppy standards and needless complexity | Findings and one clear verdict |
| [`ng-red-team`](commands/ng-red-team.md) | You want to attack your own agent change before someone else does | A record of what you tried and found |
| [`ng-trace`](commands/ng-trace.md) | You need a clear record of what an agent actually did | A structured run record |
| [`ng-breakdown`](commands/ng-breakdown.md) | You need to split a deliverable into clean pieces | A work-breakdown table and a short dictionary |
| [`ng-folders`](commands/ng-folders.md) | You need a folder layout from a work breakdown or an existing tree | A folder map and a naming and depth check |

## What every prompt card must include

Every prompt card must have: its purpose, when to use it, when not to use it, the inputs, the prompt text itself, the files it creates or changes, the expected outputs, a command to verify the result, the common failure modes, and a short note on legal and safety limits.

See `docs/05-reference/command-authoring-contract.md`.

## A note on limits

These command prompts help you keep your evidence and boundaries intact. They do not create formal verification and validation, compliance, certification, or any safety, security, or regulatory guarantee.
