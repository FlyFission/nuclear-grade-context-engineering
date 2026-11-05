---
# Optional MADR 4 decision metadata for ADR indexers. Delete this block if unused.
# status: proposed | accepted | rejected | deprecated | superseded by <slug>
# See docs/02-operating-system/change-control-packets.md#optional-decision-metadata
status: proposed
date: 2026-11-05
decision-makers: Ben Huffer (maintainer)
consulted:
informed:
---

# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** It makes one opt-in check stricter. If the change is wrong, the check fails loudly instead of passing silently. It is one function, covered by tests, and a single revert undoes it.

## Change

- Slug: `two-party-placeholder-actor`
- PR / issue: draft PR from `claude/zealous-knuth-nhjn6h`
- Owner: Ben Huffer (maintainer); change actor `agent:claude`
- Date: 2026-11-05
- Summary: `--two-party` treated a row as a second party when the identity the verifier is compared against was a placeholder. In a custody row, a "Change actor" cell reading `change actor` or `TBD` let `agent:claude` name itself as verifier and pass. The authorship table had the same hole with an evidence author of `TBD`. That breaks the module's own rule that every parsing mistake fails closed. The fix requires that party to be named.

## Scope

- Affected files/configs/docs: `nuclear_grade/two_party.py`, `tests/test_two_party.py`, `docs/02-operating-system/validators.md`
- User-visible behavior changed? yes: `validate --two-party`, and the default mode for packets that declare a `## Claim authorship` table, now fail a row whose change actor or evidence author is empty or a placeholder.
- Dependency/model/API/prompt/tool permission changed? no
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A packet that names a real second party fails `--two-party` by mistake. The failure is loud, and the message names the cell. |
| Reversibility | One revert. No data or record migration. |
| Detectability | High. 140 two-party unit tests plus a sweep of all 74 repo packets. |
| Exposure | `--two-party` is opt-in and not in CI. The default mode applies only to packets that declare an authorship table. In this repo, that table appears only in `trust-propagation-two-party`, whose author is named, so it still passes. |
| Uncertainty | Low for the rule. Whether generic role verifiers such as `human reviewer` should count is a separate open question for the owner, not decided here. |
| Why Quick is enough | Stricter-only, reversible, test-covered, and not in the CI gate. `required-mode --base HEAD` reports `none`. Quick is used because a checker is a controlled item. |

## Required proof

- Command/check/eval to run: `python -m pytest -q tests/test_two_party.py`, the same tests against the pre-fix module, a `--two-party` sweep over `.nuclear/changes/*`, then the pre-PR set in `CONTRIBUTING.md`
- Expected result: the new tests fail before the fix and pass after it. The sweep moves `claude-agents-bridge` from OK to FAILED with the new message, and every other packet keeps its result.
- Evidence link/location: `proof.md`

## Critical-action self-check

- Exact target: `_is_second_party` and `_why_not` in `nuclear_grade/two_party.py`
- Expected result: the only new failures are rows whose reference identity is a placeholder
- Stop condition: any packet other than `claude-agents-bridge` changes its `--two-party` result

## Escalation check

None of the Standard triggers apply. The change tightens a verification check and does not change permissions, a trust decision, or the release stance. Its failure mode is a loud false fail, not a silent pass. The agent drafted and ran local commands. The maintainer decides the merge.

## Required links

- Packet: `.nuclear/changes/two-party-placeholder-actor/`
- Related PR/issue: draft PR from `claude/zealous-knuth-nhjn6h`
- Proof record: `proof.md`
- Prior record for this check: `../independent-review-and-fact-checking/verification.md` (R-4 and CX-3 fixed the same class of bug on the verifier side)

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade packet. Concept lineage for two-party independence is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
