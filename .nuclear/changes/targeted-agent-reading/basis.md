# Basis — targeted agent reading

## Mission

Prevent the repository's own always-loaded guidance from requiring 582 lines of broad background before every edit. Preserve discovery: agents still begin with the controlling guidance and applicable change record, then retrieve deeper workflow material on demand.

## Requirement

**REQ-001:** Before editing, agents shall read `AGENTS.md` and the applicable change record, and shall retrieve `README.md` or `WORKFLOWS.md` only when task needs make them relevant.

This addresses context distraction and excess standing cost. It does not claim that less context always improves task outcomes; the value claim is narrower and provisional: irrelevant mandatory preload is avoidable.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Source doctrine: [`context-window-discipline.md`](../../../docs/02-operating-system/context-window-discipline.md)

## Exit criteria

The requirement is unambiguous, keeps the record mandatory, and adds no new artifact, role, gate, or tool.

## Source-lineage note

The repository already maps Anthropic's smallest-high-signal-context guidance and the Gloaguen et al. AGENTS.md evaluation in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No superiority claim is made.
