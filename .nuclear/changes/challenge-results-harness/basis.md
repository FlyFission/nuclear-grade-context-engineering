# Basis: challenge results harness

## Requirements

| ID | Requirement | Evidence planned |
|---|---|---|
| REQ-001 | `score.py --json` reports the same verdict and checks as the text scorecard. | unit test |
| REQ-002 | The scorer still flags edits to the judge and the original tests after the change. | existing challenge tests |
| REQ-003 | Each harness run uses a fresh copy, the fixed prompt, and the repository's scorer, and saves its scorecard, transcript, and diff. | unit test with fake agents |
| REQ-004 | The task-only track removes the house rules and the seeded record and keeps the task and tests. | unit test |
| REQ-005 | Results show counts per outcome with a 95% range, no overall rank, and accept human rulings that must name a known outcome. | unit tests |
| REQ-006 | The real agent CLIs in `agents.json` run headless with the listed flags. | live runs, not done yet |

## Required links

- Risk: [`risk.md`](risk.md)
- Trace: [`trace.md`](trace.md)

## Exit criteria

Each requirement is testable or named as open.

## Source-lineage note

Original Nuclear-grade record inspired by public configuration-management and operating-experience concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
