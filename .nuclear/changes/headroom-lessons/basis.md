# Basis: lessons from Headroom

## Mission

Before the first published round, challenge results compare only runs that share one identity, as `challenge-results/METHOD.md` (Pinning) already promises, and any mismatch is shown rather than hidden. Two lessons from the Headroom project (https://github.com/headroomlabs-ai/headroom, Apache-2.0, commit `53a2521`) are recorded where they bind future work.

## Requirements

- **REQ-001:** Runs with different tool versions shall be in different rows.
- **REQ-002:** Each run shall record the last commit that changed a pinned input (`challenge/`, the harness including `run-all.py`, the plain track, and the `nuclear_grade` validator the scorer loads), and which pinned inputs differed from it when the run started. Untracked and ignored files count, except the folders the copy leaves out (`__pycache__`, `.pytest_cache`).
- **REQ-003:** A row shall be marked not comparable, with the reason, when its runs span more than one inputs commit or scorer digest, when a scored run has no scorer digest, or when it holds a run made from uncommitted or unrecorded inputs. The marking shall not change a row's counts, good-outcome share or range.
- **REQ-004:** `METHOD.md` shall state the rule and log the change with its date.
- **REQ-005:** `llms.txt` shall link only to files that exist, and a test shall check this.
- **REQ-006:** ROADMAP v0.2 shall record write-back safety as a precondition for the memory store, and an opt-in item to draft OPEX from transcripts that never edits instruction files itself, each with a pinned link to its idea source.

## Non-goals

- No change to the scorer, the outcomes, the tracks, the validator, the hooks or the skills.
- No run is made or published.
- The roadmap items are not built.

## Required links

- Risk: [`risk.md`](risk.md)
- Plan: [`plan.md`](plan.md)

## Exit criteria

Each requirement maps to evidence in [`trace.md`](trace.md).

## Source-lineage note

Original Nuclear-grade synthesis. The idea source is Headroom's `docs/adr/0003-a1-b-release-benchmark.md` (paired arms must share identities; a mismatch is inconclusive) and `headroom/managed_block.py`; no code or wording is copied. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
