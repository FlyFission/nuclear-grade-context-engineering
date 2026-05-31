# Verification

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim | Result status | Evidence link | Notes |
|---|---|---|---|
| C-001 contract test relaxed | pass | `../../../tests/test_skill_contracts.py` | Drops the `Use when` prefix and 90-180 cap; enforces 80-500 chars, a negative-clause marker, no colon-space. |
| C-002 all 18 descriptions rewritten | pass | `../../../skills` | A script applied the rewrites and verified each is colon-free and within 80-500 characters; the contract test iterates every skill. |
| C-003 name-format rule | pass | `../../../tests/test_skill_contracts.py` | Lowercase, hyphen-separated, no length cap; all 18 names pass, including the 41-character `checking-legal-and-safety-wording`. |
| C-004 optional license/compatibility | pass | `../../../tests/test_skill_contracts.py` | Frontmatter key set is a subset of name, description, license, compatibility. |
| C-005 progressive disclosure documented | pass | `../../../docs/05-reference/skill-authoring-contract.md`; `../../../SKILLS.md` | Optional `references/`, `scripts/`, `assets/` layout described; wheels bundle whole skill dirs. |
| C-006 version synced to 0.3.0 | pass | `../../../pyproject.toml`; `../../../nuclear-grade.yaml`; `../../../CITATION.cff` | `test_packaging.py` asserts 0.3.0; the stale 0.1.0 in the catalog is fixed. |
| C-007 non-breaking | pass | reasoning | The change only loosens the repo's own contract test and adds no required field, so externally authored skills cannot newly fail. |

## Reproduction commands

```bash
ruff check .
python -m pytest -q
python tools/ng.py doctor .
python tools/ng.py validate .nuclear/changes/skill-contract-modernization
```

## Known gaps and deferrals

- Description enforcement remains in the contract test, not the CLI doctor. Recorded as `deferred`: adding it to doctor would false-fail the doctor stub fixtures and offers low value given the generous bounds.
- Trigger-eval automation (selecting descriptions by held-out triggering score) is `deferred`; the should/should-not prompts in `skill-evaluation.md` remain the manual proxy.
- CI has not run at packet-authoring time; it is the public evidence for the matrix and wheel jobs.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `ship.md`

## Exit criteria

- Every claim has a recorded status.

## Source-lineage note

Original Nuclear-grade verification record influenced by graded-rigor evidence concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
