# Verification

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| C-001 | New pytest case plus CLI regression test. | Marker triggers a file-named failure; CLI regression on copied real templates also fails. | pass | `tests/test_ng_validate.py::test_placeholder_marker_blocks_validation`, `tests/test_ng_cli.py::test_new_packet_from_real_templates_fails_validation_until_marker_removed` | None. |
| C-002 | Repo grep across all four template directories. | One marker line in each `*.md`. | pass | `grep -c` recorded below shows 1 per file. | None. |
| C-003 | Repo grep across `.nuclear/changes/`, the flagship example, and `tests/`. | Marker absent except as the constant in the validator and as a runtime injection in `tests/test_ng_validate.py` (never as a packet fixture). | pass | `grep -rn` recorded below. | None. |
| C-004 | `python tools/ng.py doctor .` plus full pytest run. | Doctor green; CLI tests that already scaffold every `REQUIRED_PUBLIC_FILES` entry still pass. | pass | Commands below. | None. |
| C-005 | `git status` and repo grep. | SWOT path removed from version control; no remaining reference. | pass | Commands below. | None. |
| C-006 | Public signatures intact. | `validate_packet`, `detect_packet_mode`, `ValidationResult`, `main` still importable from `tools.ng_validate`. | pass | `python -c "from tools.ng_validate import validate_packet, detect_packet_mode, ValidationResult, main"` | None. |

## Commands, evals, and reviews

| Method | Command | Environment | Result | Evidence link |
|---|---|---|---|---|
| Tests | `python -m pytest -q` | Python 3.11.15 / local | pass | 56 tests passed (54 prior + 2 new). |
| Compile | `python -m py_compile nuclear_grade/cli.py nuclear_grade/ng_validate.py tools/ng.py tools/ng_validate.py` | Python 3.11.15 / local | pass | Local output silent. |
| Doctor | `python tools/ng.py doctor .` | Python 3.11.15 / local | pass | `OK: Nuclear-grade doctor`. |
| Launch packet | `python tools/ng.py validate .nuclear/changes/public-v0-launch` | local | pass | `OK:`. |
| Productization packet | `python tools/ng.py validate .nuclear/changes/peer-ready-release` | local | pass | `OK:`. |
| CM packet | `python tools/ng.py validate .nuclear/changes/cm-public-readiness` | local | pass | `OK:`. |
| Golden-path packet | `python tools/ng.py validate .nuclear/changes/questioning-attitude-golden-path` | local | pass | `OK:`. |
| Flagship packet | `python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions` | local | pass | `OK:`. |
| This packet | `python tools/ng.py validate .nuclear/changes/harden-evidence-gate` | local | pass | `OK:`. |
| Marker grep, templates | `grep -c "$PLACEHOLDER" templates/quick/*.md templates/standard/*.md templates/cm/*.md templates/golden-path/*.md` (where `PLACEHOLDER` is the `PLACEHOLDER_MARKER` constant value defined in `nuclear_grade/ng_validate.py`) | local | pass | Every template file reports `1`. |
| Marker grep, packets | `grep -rn "$PLACEHOLDER" .nuclear/changes/ docs/03-worked-examples/` | local | pass | No matches. |
| Marker grep, tests | `grep -rn "$PLACEHOLDER" tests/` | local | pass | One match in `tests/test_ng_validate.py` as runtime injection, not as a packet fixture. |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Untouched scaffold validates green. | Copy real `templates/` into a tmp repo, run `python tools/ng.py new demo --mode quick --repo <tmp>`, then validate. | pass: validate returns non-zero with the placeholder-marker message. | `tests/test_ng_cli.py::test_new_packet_from_real_templates_fails_validation_until_marker_removed` |
| Marker absent from a template. | Grep across all four template directories. | pass: count is exactly 1 in every template file. | Grep above. |
| Marker present in a real packet or the flagship example. | Grep across `.nuclear/changes/` and `docs/03-worked-examples/`. | pass: no matches. | Grep above. |
| Doctor regresses on the four added required files. | `python tools/ng.py doctor .` and CLI pytest. | pass: green. | Doctor command above. |
| Public signature change. | Targeted import from `tools.ng_validate`. | pass: imports succeed. | C-006 row. |

## AI-assisted work checks

- AI scope: AI-assisted edits to the validator, CLI, templates, packet, tests, docs, CI, and changelog under maintainer direction.
- Model/tool used: Claude Code on the web running on the configured Claude model.
- Permissions/actions allowed: Repository file edits, local test execution, packet validation, and a push to the designated branch.
- Independent checks performed: Full pytest, doctor, packet validations, py_compile, and repo greps recorded above.
- Hallucination/slop screening: All evidence rows reference commands that were actually run in this session.
- Human approval gates exercised: Branch is pushed; merge decision remains a maintainer action.

## Deferred items

- Defense-in-depth status check that requires a real status token inside a Markdown table data row: deferred to avoid a fragile heuristic. The current marker gate plus the unfilled-prompt and prohibited-claim checks already prevent the dominant failure mode (untouched scaffold validates green).
- Vendor-neutral rename of `docs/00-standards-foundation/flyfission-ops-knowledge-graph-usage.md`: deferred for maintainer decision; not in scope.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- `tests/test_ng_validate.py`
- `tests/test_ng_cli.py`
- `nuclear_grade/ng_validate.py`
- `nuclear_grade/cli.py`

## Exit criteria

- Every C-00n has a status.
- Negative checks have results.
- Deferred items are explicit.

## Source-lineage note

Original Nuclear-grade verification record grounded in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
