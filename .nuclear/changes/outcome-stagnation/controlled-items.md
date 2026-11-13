# Controlled items — outcome stagnation

Owner: change actor for candidate; repository reviewer for merge. Approved source
state is commit 3609ff2; this is a candidate, not a new approved baseline.

| Items | Current -> intended | Reason controlled | Evidence / recheck trigger |
|---|---|---|---|
| staying-on-mission skill, generated ng-drift-check | failed-attempt loop -> explicit green-check outcome stall | agent decision behavior | command parity, skill tests; regenerate/retest on prompt edits |
| using-nuclear-grade skill, CORE | generic evidence tie -> explicit stall routing | entry activation | diff inspection, skill tests; recheck on routing edits |
| eval manifests, scenario, prompt bank, output test, command prompt fixture | generic drift -> concrete flat closure case | regression scope | existing scorer tests; recheck on case/schema changes |

See [risk](risk.md), [basis](basis.md), [change impact](change-impact.md), [verification](verification.md).

## Required links

[Risk](risk.md) · [basis](basis.md) · [verification](verification.md) · [ship](ship.md)

## Exit criteria

REQ-001 and REQ-002 have reviewable evidence; unchanged acceptance gates and live efficacy gaps remain explicit.

## Source-lineage note

This clarifies existing mission-drift doctrine; no new external source or formal assurance claim. Existing lineage: [source-map.md](../../../docs/00-standards-foundation/source-map.md).
