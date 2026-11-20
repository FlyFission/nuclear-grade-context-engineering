# Risk: lessons from Headroom

## Selected mode

- **Mode:** Standard
- **Why:**
  - The harness decides what the repo will say in public about named coding agents. Every earlier harness change used a Standard packet (`challenge-results-harness`, `challenge-scoring-fixes`, `challenge-harness-review-fixes`).
  - This change also adds a rule to the pre-registered method, and it touches public docs (`ROADMAP.md`, `llms.txt`, `CHANGELOG.md`).
  - It started as a Quick packet. An independent review showed the Quick justification was wrong on two counts, so the mode was raised. The review's points (a) and (b) are dispositioned in [`verification.md`](verification.md).

## Decision

Make challenge-result rows follow Pinning, record the run inputs a commit alone cannot name, and add two roadmap items and an agent index:

1. `build.py` grouped runs by agent, model and track, so two tool versions shared a row, against Pinning. Rows now split by tool version.
2. `run.py` records `inputs_commit`, the last commit that changed a pinned input. A commit that touches only other files leaves it unchanged, so unrelated commits do not split comparisons.
3. `run.py` records `uncommitted_inputs`: pinned files that differ from that commit, read before the copy is made. Untracked and ignored files count, because the copy carries them into the agent's folder; an ignored local settings file there could change the agent's permissions. The validator in `nuclear_grade/` is pinned, because the scorer loads it and its result separates "Recorded…" from "record does not validate". Result schema version 2.
4. `build.py` marks a row not comparable, with each reason, when its runs mismatch. Counts and ranges are unchanged, and no run leaves the row.
5. `METHOD.md` states the rule, logs the change with its date, and says "tool version" in How many runs.
6. ROADMAP v0.2 gains two items: write-back safety as a precondition for the memory store, and an opt-in transcript-to-OPEX draft. `llms.txt` is a short agent index, and a test checks that its links resolve.

Main failure modes and controls:

- **A row is flagged wrongly and reads as worse than it is.** The flag is a label, not a change to counts, and every run file is kept. Control: tests for each reason; a person reads the reason in the table.
- **A real mismatch is missed.** Control: six single-guard mutation runs, each caught by a test (`evidence/mutation-check.txt`).
- **The record cannot be rebuilt later.** Inputs a run did not record cannot be recovered by rebuilding. That is why this lands before any published round.
- **A rule changes after results are seen.** No round is published (`challenge-results/results/` holds only `.gitkeep`). `METHOD.md` logs the change with its date.
- **Public text overclaims.** The roadmap items sit under v0.2 as intent. The Headroom wording says it guards against the problem, not that it had a bug history. Control: `tests/test_public_docs.py` and review.

Controlled items: the results harness, the pre-registered method, ROADMAP, CHANGELOG, a new agent index. No separate CM baseline record is added. No baseline record exists for the harness today, and this packet's plan names the controlled items, as the earlier harness packets did.

## Required links

- Basis: [`basis.md`](basis.md)
- Plan: [`plan.md`](plan.md)
- Verification: [`verification.md`](verification.md)
- Ship decision: [`ship.md`](ship.md)

## Exit criteria

Each new guard has a test that fails when the guard is disabled, and every gate passes.

## Source-lineage note

See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
