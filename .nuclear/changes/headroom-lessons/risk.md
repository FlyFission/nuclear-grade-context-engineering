# Quick Risk: lessons from Headroom

## Selected mode

- **Mode:** Quick
- **Why this mode:** one harness fix that makes the challenge results follow rules `challenge-results/METHOD.md` already states, plus two roadmap entries and an agent-facing index. No runtime behavior of the `ng` CLI, the validator, the hooks, the skills, a dependency, a permission or the release stance changes, and no results are published yet (`challenge-results/results/` is empty), so no published number moves.

---

## Change

- Slug: `headroom-lessons`
- PR / issue: draft PR from branch `claude/focused-noether-n5a59m`
- Owner: FlyFission (decision owner); drafted by Claude Code under the owner's instruction to apply the high-confidence lessons from reviewing the Headroom project (https://github.com/headroomlabs-ai/headroom, Apache-2.0, commit `53a2521`)
- Date: 2026-11-19
- Summary: five edits.
  - `challenge-results/run.py` records which pinned inputs (the task, the scorer, the harness, the plain track) had uncommitted changes when a run started (`uncommitted_inputs`; result schema version 2).
  - `challenge-results/build.py` makes a new tool version a new row, as `METHOD.md` (Pinning) already says. It marks a row not comparable, with the reason, when its runs span repo commits or scorer digests or include a run from uncommitted or unrecorded files.
  - `METHOD.md` states the not-comparable rule.
  - `ROADMAP.md` adds write-back safety as a precondition for the memory store, and an opt-in item to draft OPEX from agent transcripts.
  - `llms.txt` is a short index for agents, with a test that its links resolve.

## Scope

- Affected files/configs/docs: `challenge-results/run.py`, `challenge-results/build.py`, `challenge-results/METHOD.md`, `tests/test_challenge_results.py`, `ROADMAP.md`, `llms.txt` (new), `tests/test_public_docs.py`, this packet, `.nuclear/badge.json`.
- User-visible behavior changed? yes. The challenge results table gains a "Tool version" column and a "not comparable" note where it applies, and `results.json` rows replace `tool_versions` (a list) with `tool_version` (one string) plus `identity_problems`, `repo_commits` and `scorer_sha256`. No results exist yet, so nothing published changes.
- Dependency/model/API/prompt/tool permission changed? no. Standard library only; the challenge prompt is unchanged.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A future results row is split or flagged wrongly, or a real mismatch is missed. The failure is visible in the table, and every run file is kept, so a rebuild fixes it. |
| Reversibility | Revert the commit; `build.py` reruns from the kept run files. |
| Detectability | High. Three new tests cover grouping, flagging and the git-status read, and each fails when its guard is disabled (`evidence/mutation-check.txt`). |
| Exposure | Repository harness and public docs. No results are published yet. |
| Uncertainty | Low for the harness. The roadmap items are intent, not shipped features, and say so by where they sit. |
| Why Quick is enough | The code change implements rules the pre-registered method already states; the rest is documentation. |

## Required proof

- Command/check/eval to run: the pre-PR commands in `CONTRIBUTING.md` (pytest, ruff check, doctor, tokens, the worked-example strict-custody validation, the release version check, validation of this packet, the badge, `git diff --check`), plus a mutation check of the three new guards.
- Expected result: all pass; with the guards disabled, the three new tests fail.
- Evidence link/location: `proof.md` and `evidence/`.

## Critical-action self-check

- Exact target: the files in Scope, on branch `claude/focused-noether-n5a59m` from `origin/main` at `154ac1d`.
- Expected result: `git status` shows only those files.
- Stop condition: any change to the hooks, the gate policy, `.github/workflows/`, the validator, a skill, or a published result.

## Escalation check

Move up to Standard if results are published under the new grouping in this change, if the validator or a skill changes, or if the roadmap items are built. None of these is in this change.

## Required links

- Packet: `.nuclear/changes/headroom-lessons/`
- Related PR/issue: draft PR pending.
- Proof record: [`proof.md`](proof.md)
- Relevant source-map/crosswalk if invoked: not invoked. The idea source is Headroom at the commit above, its `docs/adr/0003-a1-b-release-benchmark.md` (paired arms must share identities, mismatch is inconclusive) and `headroom/managed_block.py` (transcript text written into instruction files). No Headroom code or wording is copied.

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on software test documentation, verification, work records, and keeping the approved version under control, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
