# Quick Risk

## Selected mode

- **Mode:** Quick
- **Why this mode:** Docs wording plus three extra lines of `new` output; nothing the validator checks or decides changes, and one revert undoes it.

---

## Change

- Slug: quickstart-validate-steps
- PR / issue: #150 (raised by Copilot's review summary on #145)
- Owner: FlyFission
- Date: 2026-11-09
- Summary: The README and WORKFLOWS.md Quick start ran `validate` straight after `new`, which fails because a fresh record is blank on purpose. The steps now say to fill in the files and delete the placeholder line first, and `new` prints the same next steps.

## Scope

- Affected files/configs/docs: `README.md`, `WORKFLOWS.md`, `CHANGELOG.md`, `nuclear_grade/cli.py` (`handle_new`, new `print_new_next_steps`), `tests/test_ng_cli.py`, this packet.
- User-visible behavior changed? yes: `new` prints next steps after a successful create. Exit codes and created files are unchanged.
- Dependency/model/API/prompt/tool permission changed? no
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A confusing hint line or wording; no record passes or fails differently. |
| Reversibility | One revert of the PR. |
| Detectability | Visible on every `new` run and covered by two CLI tests. |
| Exposure | Anyone following the Quick start or running `new`. |
| Uncertainty | Low; the failure was reproduced on PyPI 0.7.0 before the fix. |
| Why Quick is enough | The blank-record safeguard in `ng_validate.py` is untouched, and the existing test that a fresh scaffold fails validation still passes. |

## Required proof

- Command/check/eval to run: reproduce the Quick start on PyPI 0.7.0 in a fresh venv and repo; run `new` from this branch in a fresh repo; `python -m pytest -q`; `ruff check .`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; `git diff --check`; validate this packet.
- Expected result: the old steps fail at validate with the placeholder message; the new `new` output names the files and the validate step; all gates pass.
- Evidence link/location: `proof.md` in this packet; CI on #150.

## Critical-action self-check

Not applicable: the change cannot hit the wrong target; it touches output text and docs only.

## Escalation check

None of the Standard triggers apply: no users, data, security, permissions or architecture are affected; no trust decision changed; a failure would be visible right away and is easy to undo; the AI only edited files on a branch for a draft PR that a person merges; the proof fits in `proof.md`.

## Required links

- Packet: `.nuclear/changes/quickstart-validate-steps/`
- Related PR/issue: #150, #145
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: not applicable

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record based on the Quick template, which draws on public ideas on matching rigor to stakes, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
