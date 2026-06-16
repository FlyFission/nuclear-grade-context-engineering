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
| [`ng-close-packet`](commands/ng-close-packet.md) | A change record has gone stale and `ng status` flagged it | A finished, closed-with-reason, or deleted record |
| [`ng-decide-authority`](commands/ng-decide-authority.md) | An agent could act on something irreversible, trust-bearing, or thinly evidenced and you must place authority | Who decides and the escalation trigger |
| [`ng-intent`](commands/ng-intent.md) | You are about to take a critical or irreversible action and want the reasoning challenged first | An intent declaration or release brief with abort criteria and rollback |
| [`ng-incident`](commands/ng-incident.md) | Production is broken, data is at risk, or an agent action caused harm | A stabilize-first incident record with owned corrective actions |
| [`ng-deficiency`](commands/ng-deficiency.md) | A known problem will outlive a single change and must be owned, not normalized | A deficiency entry, aged and dispositioned |

## How the prompt cards are made

Each card is generated from its paired skill by `ng gen-commands`, so the skill is the single source and the two never drift. A card carries the skill's summary, when to use it and when not to, the inputs, the exact prompt text (kept in the skill's `## Prompt` section), how to verify the result, and a pointer back to the skill for the rest. To change a command, edit the skill and regenerate — do not edit the card by hand.

See `docs/05-reference/command-authoring-contract.md`.

## A note on limits

These command prompts help you keep your evidence and boundaries intact. They do not create formal verification and validation, compliance, certification, or any safety, security, or regulatory guarantee.
