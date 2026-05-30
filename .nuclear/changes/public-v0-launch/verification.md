# Verification — Public v0 Launch

**Purpose:** Record the evidence that public v0 is ready to launch.

---

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| L-001 | Public residue scan | No unsafe internal launch residue remains. | pass | scan commands below | None. |
| L-002 | Source-gap scan | No unstructured verification placeholders remain. | pass | scan commands below | None. |
| L-003 | Validator pytest suite | Quick and Standard validator tests pass. | pass | `tests/test_ng_validate.py` | None. |
| L-004 | Packet validation | Worked-example and launch packets validate. | pass | validator commands below | None. |
| L-005 | GitHub release gate | Visibility is changed only after merged PR and CI pass. | planned | `ship.md` | Execute after PR merge. |
| L-006 | Legal/license boundary scan | MIT reuse is explicit and no regulated verification/NQA-1/QA/regulatory/fitness assurance is implied. | pass | README, DISCLAIMER, compliance-boundaries, validator tests | Not legal advice; qualified counsel remains appropriate for regulated or customer-facing use. |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Tests | `uv run --no-project --python 3.12 --with pytest python -m pytest tests/test_ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/tests/test_workspace_guard.py -q -s` | Python 3.12 / local uv environment | pass | local output: 13 tests passed |
| Compile | `python3 -m py_compile tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/reference/workspace_guard.py` | Python 3.12 / local | pass | local output |
| Worked-example packet | `python3 tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions` | Python 3.12 / local | pass | local output |
| Launch packet | `python3 tools/ng_validate.py .nuclear/changes/public-v0-launch` | Python 3.12 / local | pass | local output |
| Diff whitespace | `git diff --check` | Git | pass | local output |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Internal residue remains | `rg` scan for names, local paths, and stale launch language. | pass | scan output |
| Source placeholders remain | `rg` scan for unstructured source-gap phrases. | pass | scan output |
| Prohibited overclaim appears | `rg` scan for seed prohibited phrases. | pass | Hits limited to validator seed lists, tests, validator docs, and explicit boundary context. |
| License/use boundary unclear | Targeted scan for MIT, warranty, regulated verification, NQA-1, quality assurance, regulatory, safety, procurement, and fitness terms. | pass | Boundary hits only; no assurance claim. |
| Quick packet unsupported | pytest Quick packet test. | pass | `tests/test_ng_validate.py` |

## AI-assisted work checks

- **AI scope:** AI-assisted edits updated docs, validator, tests, and launch packet under maintainer direction.
- **Model/tool used:** Local AI-assisted coding tools.
- **Permissions/actions allowed:** Repository file edits, tests, scans, Git branch/PR work when approved.
- **Independent checks performed:** Local pytest, py_compile, validator commands, diff check, and residue/source/overclaim scans.
- **Hallucination/slop screening:** Source-map entries must be verified-public or explicitly downgraded.
- **Human approval gates exercised:** Visibility flip remains blocked until PR merge and CI pass.

## Security / dependency / supply-chain checks

- **Dependency review:** Validator remains Python standard library only. Tests use pytest.
- **SBOM/provenance/build evidence:** Not applicable for public docs/tooling v0.
- **Vulnerability/security review:** Focused on overclaiming, private residue, example sandbox scope, and license/use boundary clarity.
- **Revalidation trigger:** New source-map entries, validator mode expansion, or public claims beyond Quick/Standard support.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`
- CI run / eval report / test logs / review notes: PR checks and local command output.
- Implementation diff / PR: launch-readiness PR.

## Exit criteria

- Each launch claim has `pass`, `fail`, `gap`, `deferred`, or `not applicable` status.
- Evidence is linked or command-reproducible.
- Gaps are explicit and reflected in `ship.md`.
- Reviewer can tell whether evidence supports public visibility.

## Source-lineage note

Original Nuclear-grade verification record inspired by public software V&V, test-documentation, software assurance, and release-readiness concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
