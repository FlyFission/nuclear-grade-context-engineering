# Basis: Fix five gaps a code review found in the challenge harness

## Mission

Before the first published round, the harness keeps every run, scores what the agent actually did, and records what METHOD.md promises.

## Requirements

- **REQ-001:** Two runs shall never write to the same result files, even when started in the same second.
- **REQ-002:** A timeout shall stop the agent and every process it started before the folder is staged and scored.
- **REQ-003:** The saved diff shall be taken against the starting commit, so work the agent committed is in it.
- **REQ-004:** Each run shall record the operating system and the container image.
- **REQ-005:** A run shall count as "record does not validate" only when its tests pass, and a human ruling shall need run ID, outcome, who ruled, date, and quote.
- **REQ-006:** Two change records shall say what is true: the build plugin has a minimum version, and the command-card change covers 30 cards after the merge with `main`.
- **REQ-007:** A test shall check each command card's description against its skill directly.

## Non-goals

No change to the scorer, the outcomes, or the tracks. No run is made or published.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)

## Exit criteria

Each requirement maps to evidence in [`trace.md`](trace.md).

## Source-lineage note

Original Nuclear-grade synthesis. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
