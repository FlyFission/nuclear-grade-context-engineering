# Basis

## Decision this basis supports

Make Nuclear-grade's evidence gate actually load-bearing: an untouched scaffold packet must not validate green just because instructional template prose contains the same status words that real evidence does.

## Protected outcomes

| Protected outcome | Why it matters | Evidence link |
|---|---|---|
| `validate_packet` and `detect_packet_mode` remain importable from `nuclear_grade.ng_validate` with the same signatures. | `nuclear_grade/cli.py` and `tools/ng_validate.py` import them; `tools/ng_validate.py` re-exports only them plus `ValidationResult` and `main`. | `nuclear_grade/ng_validate.py`, `tools/ng_validate.py` |
| `nuclear_grade/` and `tools/` stay stdlib-only and dependency-free. | The repo promises a zero-dependency validator. | `nuclear_grade/ng_validate.py` imports only `argparse`, `re`, `dataclasses`, `pathlib`. |
| Existing packets validate. | Regression would block CI and contradict the public Try-it path. | `verification.md` evidence runs. |
| The marker lives only in templates. | The marker has to fail real packets, not pollute them. | `verification.md` grep evidence. |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A scaffold packet validates green. | Public Try-it path is misleading. | Marker check in `validate_packet`; CLI regression test copies real templates and asserts the failure. |
| Marker leaks into the flagship or test fixtures. | False positives for users. | Repo-wide grep recorded in `verification.md`; fixtures continue to use hand-written content. |
| Public signatures change. | External importers break silently. | `tools/ng_validate.py` re-export check and CLI/validator tests. |
| Removing the SWOT report breaks an active reference. | Dangling link in public docs. | Grep verified only one reference existed in `docs/04-adoption/README.md`; that bullet is removed in the same change. |

## Assumptions and constraints

| Assumption / constraint | Basis | Invalidation trigger |
|---|---|---|
| `.research/` is gitignored. | `.gitignore` line `.research/`. | Anyone removes that line. |
| The four added public files already exist. | `ls` of repo root shows `DISCLAIMER.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`. | Any one is deleted. |
| Marker is unique enough to be safe in a grep. | Hyphenated all-caps string with no English meaning. | Future docs adopt the literal string. |

## Derived requirements or claims

| ID | Requirement / claim | Evidence planned |
|---|---|---|
| C-001 | Validator rejects any packet whose `*.md` file contains the placeholder marker, with a message naming the file. | New pytest in `tests/test_ng_validate.py` plus CLI regression test in `tests/test_ng_cli.py`. |
| C-002 | Templates in `templates/quick`, `templates/standard`, `templates/cm`, `templates/golden-path` each carry exactly one marker line near the top. | Repo grep recorded in `verification.md`. |
| C-003 | Marker is absent from the four `.nuclear/changes/` packets, the flagship example packet, and all test fixtures. | Repo grep recorded in `verification.md`. |
| C-004 | Doctor requires `DISCLAIMER.md`, `SECURITY.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md`. | `python tools/ng.py doctor .` plus pytest suite. |
| C-005 | `docs/04-adoption/report-swot-gap-remediation.md` is no longer tracked, and the only reference in `docs/04-adoption/README.md` is removed. | `git status` plus repo grep. |

## Required links

- `risk.md`
- `verification.md`
- `ship.md`
- `nuclear_grade/ng_validate.py`
- `nuclear_grade/cli.py`
- `tests/test_ng_validate.py`
- `tests/test_ng_cli.py`

## Exit criteria

- Each C-00n claim has a status in `verification.md`.
- Public signatures still load.
- Existing packets still pass.

## Source-lineage note

Original Nuclear-grade configuration-management hygiene change grounded in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
