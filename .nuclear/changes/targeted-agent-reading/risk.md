# Risk — targeted agent reading

## Selected mode

- **Mode:** Standard
- **Why:** `AGENTS.md` controls agent behavior; a one-line change still warrants the repository's Standard path.

## Decision

Replace the unconditional preload of two root documents (582 lines total) with task-triggered navigation. The objective is lower irrelevant standing context without weakening the requirement to read the applicable change record.

The main failure is under-reading. The control is explicit: start with `AGENTS.md` and the change record, then follow links when the task needs them. This does not change tests, permissions, release posture, or public assurance claims.

## Required links

- Changed item: [`AGENTS.md`](../../../AGENTS.md)
- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

The instruction no longer requires wholesale preload, still requires the relevant record, and all repository checks pass.

## Source-lineage note

This applies the minimum-sufficient-context posture already mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). It makes no efficacy, compliance, or safety claim.
