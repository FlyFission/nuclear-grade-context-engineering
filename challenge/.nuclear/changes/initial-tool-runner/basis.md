# Basis: initial tool runner

## Requirements

| ID | Requirement | Evidence planned |
|---|---|---|
| REQ-001 | The agent may only run tools that are both configured and registered. | unit tests |
| REQ-002 | File tools may only touch paths inside `workspace/`. | unit tests |
| REQ-003 | Tools that need the network are denied while `network` is false. | unit tests |

## Required links

- Risk: [`risk.md`](risk.md)
- Trace: [`trace.md`](trace.md)

## Exit criteria

Each requirement is testable.

## Source-lineage note

Record shape from Nuclear-grade, https://github.com/FlyFission/nuclear-grade-context-engineering. No compliance claim is made.
