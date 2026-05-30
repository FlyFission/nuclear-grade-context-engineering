# Verification - CM Public Readiness

**Purpose:** Record the evidence for the CM (keeping the approved version under control) public-readiness pass.

## Verification context

- Slug: `cm-public-readiness`
- Related basis: `basis.md`
- Owner: Maintainer
- Date: 2026-05-23
- Verification scope: Public docs, CM artifacts, package entry point, contracts, validator, boundary scans.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| CM-001 | Public doc review and scans | README/workflows describe CM without overclaiming. | pass | Commands below | Boundary hits are negative disclaimers or validator seed lists. |
| CM-002 | Template/catalog review | CM templates exist and are indexed. | pass | `templates/cm/`, `nuclear-grade.yaml` | None. |
| CM-003 | Contract tests and doctor | Skills/commands pass contract tests and catalog checks. | pass | pytest / doctor | None. |
| CM-004 | Packaging test and editable install | `nuclear-grade doctor .` works after install. | pass | packaging commands | None. |
| CM-005 | Packet validation | This packet validates. | pass | validator command | None. |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Focused packaging tests | `python -m pytest tests/test_packaging.py tests/test_ng_cli.py tests/test_ng_validate.py -q` | local Python | pass | local output |
| Full test suite | `python -m pytest -q` | local Python | pass | local output: 41 passed |
| Compile | `python -m py_compile nuclear_grade/cli.py nuclear_grade/ng_validate.py tools/ng.py tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/reference/workspace_guard.py` | local Python | pass | local output |
| Doctor | `python tools/ng.py doctor .` | local Python | pass | local output |
| Packet validation | `python tools/ng.py validate .nuclear/changes/cm-public-readiness` | local Python | pass | local output |
| Worked-example packet validation | `python tools/ng.py validate docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions` | local Python | pass | local output |
| Editable install | `python -m venv .venv`; `.venv\Scripts\python.exe -m pip install -e .`; `.venv\Scripts\nuclear-grade.exe doctor .` | local venv | pass | local output |
| Boundary scan | `rg -n "docs/superpowers|2026-05-19-public-v0-launch" .` and prohibited-phrase scan over public docs/artifacts | local shell | pass | no stale internal-link hits; prohibited hits reviewed as negative disclaimers or validator seed lists |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Package discovery collision | Packaging contract test failed before fix, then passed after namespacing. | pass | `tests/test_packaging.py` |
| Stale internal scaffolding links | Search for `docs/superpowers` after cleanup. | pass | scan output |
| Overclaiming CM as formal assurance | Boundary scan over public docs. | pass | scan output |

## AI-assisted work checks

- AI scope: Repo-wide docs, templates, skills, commands, tests, and tooling edits under maintainer direction.
- Permissions/actions allowed: Local file edits and verification commands.
- Independent checks performed: pytest, doctor, validator, compile, install, scans.
- Human approval gates exercised: User explicitly requested public-readiness pass.

## Security / dependency / supply-chain checks

- Dependency review: No new runtime dependency. Tests still use pytest.
- Build/provenance evidence: Editable install check exercises package metadata.
- Revalidation trigger: Packaging metadata, CM artifact shape, or public claim changes.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`
- `controlled-items.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Each important claim has status.
- Evidence is command-reproducible or linked.
- Gaps are explicit and reflected in `ship.md`.

## Source-lineage note

Original Nuclear-grade verification record inspired by public software V&V, test-documentation, software assurance, configuration-management, and release-readiness concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
