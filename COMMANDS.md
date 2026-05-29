# Nuclear-grade Portable Command Prompts

These are portable command prompts: plain Markdown prompt cards that can be pasted into an AI coding agent or adapted for a local harness. Public v0 does not claim packaged marketplace integration.

## Catalog

| Prompt | Use when | Output |
|---|---|---|
| [`ng-question`](commands/ng-question.md) | Applying questioning attitude before build, review, or release | Assumptions, gaps, stop conditions |
| [`ng-classify`](commands/ng-classify.md) | Selecting a mode | Mode decision and evidence obligation |
| [`ng-new`](commands/ng-new.md) | Creating a packet | Packet files |
| [`ng-cm-items`](commands/ng-cm-items.md) | Identifying controlled configuration items | Controlled item list |
| [`ng-impact`](commands/ng-impact.md) | Screening change impact and revalidation | Impact screen |
| [`ng-baseline`](commands/ng-baseline.md) | Recording accepted baseline state | Baseline record |
| [`ng-context-pack`](commands/ng-context-pack.md) | Bounding agent context | Context pack |
| [`ng-turnover`](commands/ng-turnover.md) | Handing off unfinished work to another agent, human, verifier, releaser, or resumed thread | Turnover record |
| [`ng-self-check`](commands/ng-self-check.md) | Checking critical agent actions before and after execution | Self-check record |
| [`ng-prove`](commands/ng-prove.md) | Mapping claims to evidence | Claim-to-evidence table |
| [`ng-ship-review`](commands/ng-ship-review.md) | Making a release decision | Ship/readiness record |
| [`ng-opex`](commands/ng-opex.md) | Learning from near misses, bad handoffs, review surprises, incidents, or operating signals | OPEX record |
| [`ng-trust-check`](commands/ng-trust-check.md) | Checking dependency, model, API, SaaS, generated artifact, or vendor trust | Intended-use trust screen |
| [`ng-source-check`](commands/ng-source-check.md) | Checking source lineage | Source-safe wording |
| [`ng-legal-check`](commands/ng-legal-check.md) | Checking license and assurance boundaries | Boundary-safe wording |
| [`ng-drift-check`](commands/ng-drift-check.md) | Testing work against its mission anchor and charter | Re-anchor / escalate / stop decision |
| [`ng-code-review`](commands/ng-code-review.md) | Reviewing a diff or module for standards drift and complexity | Findings and a single verdict |
| [`ng-red-team`](commands/ng-red-team.md) | Adversarially reviewing an agent change for prompt injection, escalation, unsafe output, or tool misuse | Red-team findings record |
| [`ng-trace`](commands/ng-trace.md) | Capturing agent execution evidence for verification and release review | Execution trace record |

## Contract

Every command card must include purpose, use and non-use conditions, inputs, prompt text, files created or modified, expected outputs, verification command, failure modes, and legal/assurance boundary note.

See `docs/05-reference/command-authoring-contract.md`.

## Boundary note

Portable command prompts support reviewable evidence. They do not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
