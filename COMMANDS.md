# Nuclear-grade Portable Command Prompts

These are portable command prompts: plain Markdown prompt cards that can be pasted into an AI coding agent or adapted for a local harness. Public v0 does not claim packaged marketplace integration.

## Catalog

| Prompt | Use when | Output |
|---|---|---|
| [`ng-question`](commands/ng-question.md) | Applying questioning attitude before build, review, or release | Assumptions, gaps, stop conditions |
| [`ng-classify`](commands/ng-classify.md) | Selecting a mode | Mode decision and proof obligation |
| [`ng-new`](commands/ng-new.md) | Creating a packet | Packet files |
| [`ng-cm-items`](commands/ng-cm-items.md) | Identifying controlled configuration items | Controlled item list |
| [`ng-impact`](commands/ng-impact.md) | Screening change impact and revalidation | Impact screen |
| [`ng-baseline`](commands/ng-baseline.md) | Recording accepted baseline state | Baseline record |
| [`ng-context-pack`](commands/ng-context-pack.md) | Bounding agent context | Context pack |
| [`ng-prove`](commands/ng-prove.md) | Mapping claims to evidence | Claim-to-evidence table |
| [`ng-ship-review`](commands/ng-ship-review.md) | Making a release decision | Ship/readiness record |
| [`ng-source-check`](commands/ng-source-check.md) | Checking source lineage | Source-safe wording |
| [`ng-legal-check`](commands/ng-legal-check.md) | Checking license and assurance boundaries | Boundary-safe wording |

## Contract

Every command card must include purpose, use and non-use conditions, inputs, prompt text, files created or modified, expected outputs, verification command, failure modes, and legal/assurance boundary note.

See `docs/05-reference/command-authoring-contract.md`.

## Boundary note

Portable command prompts support reviewable evidence. They do not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
