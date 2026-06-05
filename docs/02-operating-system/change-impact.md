# Change Impact

**Purpose:** This file helps you check what a controlled change might break or make out of date.

## Impact screen

Ask whether the change affects:

- requirements, outcomes you protect, assumptions, or limits;
- code, tests, docs, templates, skills, command prompts, or how the checker behaves;
- prompts, models, dependencies, APIs, credentials, or what a tool is allowed to do;
- release notes, support posture, monitoring, rollback, or handoff;
- the wording about where ideas came from, or the wording that marks the limits of what you claim.

## Runtime and migration blast radius

For brownfield and migration work (see `work-type-lens.md`), screen the running system, not just the repo's files:

- **Schema and state** — data or schema migrations, and whether they are forward-only or reversible.
- **API consumers** — callers that depend on the current contract; whether the change is backward-compatible or needs a versioned or phased rollout.
- **Concurrency and load** — behavior under existing traffic, ordering, and retries.
- **Security surface** — new inputs, permissions, or trust boundaries the change exposes.
- **Rollback-of-state** — how to undo after partial progress, not just how to revert the code.

Record each as update / no-op / defer / block with an owner and a re-check trigger, the same as the artifact screen.

## Exit criteria

The impact screen is complete when each affected group of files is updated, linked to a follow-up, or clearly marked not applicable.

## Source-lineage note

This impact-screen model is an original software workflow. It draws on public sources about keeping the approved version of everything under control, secure development, and the lifecycle, mapped in `../00-standards-foundation/source-map.md`.
