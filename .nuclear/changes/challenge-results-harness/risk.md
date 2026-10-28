# Risk: challenge results harness

## Selected mode

- **Mode:** Standard
- **Why:** It changes the challenge scorer (a judge), adds a harness that runs coding agents with flags that let them act without asking, and adds public results that name other people's tools.

## Decision

Add `score.py --json` and a `challenge-results/` harness that runs an agent on fresh copies of the challenge, scores each run with the repository's own scorer, and publishes counts per agent, model, and track under a method written before any run.

Main failure modes and controls:

- **The JSON scorecard disagrees with the text scorecard.** Control: both come from the same `Score` object; a test compares the verdicts.
- **The scorer change lets a played folder pass the judge check.** Control: the judge manifest is regenerated and the existing tamper tests still pass.
- **An agent run escapes onto the maintainer's machine.** Control: the README and METHOD say to run only in a throwaway container or VM. Gap: nothing enforces it.
- **Published results read as a safety rating or an accusation.** Control: neutral outcome names, no overall rank, a stated conflict of interest, a 5-run minimum, a dispute form, and a corrections log.
- **The rules track mostly measures following this repo's format.** Control: a second, task-only track.

## Required links

- Basis: [`basis.md`](basis.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Each failure mode has a control or a named gap.

## Source-lineage note

Original Nuclear-grade record inspired by public configuration-management and operating-experience concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
