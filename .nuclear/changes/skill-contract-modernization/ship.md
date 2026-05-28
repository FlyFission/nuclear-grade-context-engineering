# Ship

## Release decision

- **Decision:** ship as 0.3.0 once CI is green.
- **Rationale:** The change modernizes a public authoring contract and is non-breaking (it loosens the repo's own test and adds no required field). A minor bump is honest because the authoring contract is a documented interface.
- **Pre-merge gates:**
  - `python -m pytest -q` green
  - `ruff check .` clean
  - `python tools/ng.py doctor .` OK
  - `python tools/ng.py validate` OK on every packet including this one
  - CI green on the matrix and wheel-smoke jobs

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Verification | pass | `verification.md` |
| Trace | pass | `trace.md` |
| Contract test | pass | `tests/test_skill_contracts.py` |
| Version sync | pass | `pyproject.toml`, `nuclear-grade.yaml`, `CITATION.cff` |
| Packet self-validation | pass | `python tools/ng.py validate .nuclear/changes/skill-contract-modernization` |

## Rollback / restore plan

- Revert the branch; descriptions, test, docs, and version revert cleanly. No data migration.
- If a rewritten description is found to under-trigger in practice, edit that single description; the contract permits it without further change.

## Monitoring and post-release checks

- Watch for any agent harness that fails to parse a description; the colon-space ban should prevent it.
- Watch triggering behavior of the rewritten descriptions; refine individual ones if they over- or under-trigger.
- Revisit the deferred trigger-eval automation once there is signal on real triggering accuracy.

## Maintainer follow-ups

- Consider the next deferred bundle: progressive-disclosure engine support (recognizing `references/` in tooling) and the evidence-coverage validator rule.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`

## Exit criteria

- Decision recorded; rollback named; monitoring named.

## Source-lineage note

Original Nuclear-grade ship record influenced by release-readiness concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
