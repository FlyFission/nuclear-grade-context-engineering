# Plan

**Purpose:** Bound the work, the review, the verification, and the rollback before the change grows.

## Change context

- Slug: trust-propagation-two-party
- Related risk record: `risk.md`
- Related basis record: `basis.md`
- Owner: Ben Huffer (maintainer)
- Date: 2026-07-17
- Current lifecycle phase: Verify

## Charter and anchor check

- Mission anchor confirmed (objective, success criteria, non-goals) before Plan? yes
- Re-checked before Verify? yes
- Charter articles in play: operational unambiguity; evidence over persuasion; independence of the decider.

If you must cross a non-goal or a charter article, record why here:

| What is crossed | Why it is necessary | Why no simpler path | Owner decision |
|---|---|---|---|
| None | Not applicable | Not applicable | No crossing required |

## Build sequence

| # | Task | Reqs | Prereqs | Inputs (`file#section`) + budget | Outputs / artifact | Proof | Stop/done |
|---|---|---|---|---|---|---|---|
| 1 | Write `propagation.py` computing effective trust as the minimum over claim statuses | REQ-001 | none | `basis.md#derived-requirements-or-claims` | `nuclear_grade/propagation.py` | unit tests | module imports and tests pass |
| 2 | Write `two_party.py` flagging a self-verified pass claim | REQ-002 | step 1 style | `basis.md#derived-requirements-or-claims` | `nuclear_grade/two_party.py` | unit tests | module imports and tests pass |
| 3 | Add unit tests for both modules | REQ-001, REQ-002 | steps 1 and 2 | `verification.md#claim-to-evidence-table` | `tests/test_propagation.py`, `tests/test_two_party.py` | pytest green | all new tests pass |

For any model-mediated slice, determinism posture: modules are deterministic pure functions over Markdown text; tests are fully replayable.

## Two-speed work plan

| Work phase | Allowed actions | Acceptance gate |
|---|---|---|
| explore | Draft module shape and status ordering | Design reviewed in this packet |
| candidate | Implement modules and tests | Unit tests green, ruff clean |
| audit | Run full suite, doctor, packet validation | No regression to existing packets |
| accept | Maintainer merge decision | Independent review recorded in `ship.md` |

## HPI task preview

| Critical step | Likely error | Consequence | Control / contingency | Evidence |
|---|---|---|---|---|
| Parsing the claim table | Miscount rows on a varied schema | Wrong trust computed | Keep gate inert; normalize table before wiring | `tests/test_propagation.py` |

## Agent briefing

- Role: AI builder under maintainer direction.
- Authority source: maintainer (Ben Huffer).
- Active procedure/template: Standard packet.
- Last completed action if resumed: modules and tests written and passing.
- Handoff or turnover needed? yes; pickup continues elsewhere per the ship.md handoff.
- Pause when unsure condition: pause before wiring gates into `validate_packet`.

## Affected files and assets

| File / asset | Change expected | Requirements covered | Why it matters | Owner |
|---|---|---|---|---|
| `nuclear_grade/propagation.py` | new module | REQ-001 | Trust computation | Ben Huffer |
| `nuclear_grade/two_party.py` | new module | REQ-002 | Independence check | Ben Huffer |
| `tests/test_propagation.py` | new test | REQ-001 | Proof | Ben Huffer |
| `tests/test_two_party.py` | new test | REQ-002 | Proof | Ben Huffer |

## Non-goals

- This packet does not wire either check into `validate_packet`.
- This packet does not normalize the claim-to-evidence table schema.

## Dependency / model / tool decisions

| Decision | Option selected | Alternatives rejected | Evidence or reason | Revalidation trigger |
|---|---|---|---|---|
| Parser implementation | Stdlib regex and string ops | A Markdown-table library | Keep zero runtime deps | Any added dependency |

## Review checkpoints

| Checkpoint | Required before moving on | Status |
|---|---|---|
| Requirements approved | Each requirement is one clear trigger to response statement with a `REQ-NNN` id | pass |
| Design approved | The basis design outline is complete for this change | pass |
| Tasks approved | Every build step carries the requirement ids it delivers | pass |
| Specification reviewed | Protected outcomes and outcomes to prevent are stated plainly | pass |
| Tests/evals defined | Each piece of evidence maps to a claim | pass |
| Build complete | The affected files match the plan | pass |
| Verification complete | The evidence is linked in `verification.md` | pass |
| Release decision ready | The leftover risks and the rollback are recorded | pass |
| Turnover complete if activated | The next owner has the state and the work left | pass |

## Rollback approach

- Rollback method: `git revert` the merge commit, or delete the four new files.
- State/data reversal notes: none; no state is created.
- Feature flag / kill switch: not applicable; modules are inert until imported.
- Owner: Ben Huffer.
- Time to restore estimate: under one minute.

## Proof commands

```bash
python -m pytest tests/test_propagation.py tests/test_two_party.py -q
python -m ruff check nuclear_grade/propagation.py nuclear_grade/two_party.py tests/test_propagation.py tests/test_two_party.py
python -m pytest -q
python tools/ng.py validate .nuclear/changes/trust-propagation-two-party
```

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Issue / PR / ADR / design doc: this PR

## Exit criteria

- The work is bounded enough to keep scope from creeping.
- The review checkpoints are named.
- Rollback and restore are thought through before release.
- The proof commands or checks are ready for `verification.md`.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software lifecycle, keeping the approved version under control (CM), software assurance, secure development, release readiness, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
