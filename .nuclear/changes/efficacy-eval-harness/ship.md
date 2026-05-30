# Ship

## Release decision

- **Decision:** ship on the review branch as part of the repo-review enhancements; merge once CI is green.
- **Rationale:** The harness makes one efficacy claim reproducible and adds a regression guard for the worked examples, with wording bounded against overclaiming. It is read-only and non-breaking.
- **Pre-merge gates:**
  - `python -m pytest -q` green
  - `ruff check .` clean
  - `python tools/ng.py doctor .` OK
  - `python tools/ng.py eval .` reports full coverage
  - `python tools/ng.py validate` OK on every packet including this one
  - CI green on the matrix and wheel-smoke jobs

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Verification | pass | `verification.md` |
| Trace | pass | `trace.md` |
| Harness behavior | pass | `tests/test_efficacy.py` |
| Boundary wording | pass | `docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md` |
| Packet self-validation | pass | `python tools/ng.py validate .nuclear/changes/efficacy-eval-harness` |

## Rollback / restore plan

- Revert the branch; the module, eval cases, subcommand, doc, and tests revert cleanly. No data migration.
- If a signal is found to be too loose or too strict, edit that single JSON case; the harness permits it without code change.

## Monitoring and post-release checks

- Watch CI: the efficacy test will fail if a worked example later drops a decision signal, which is the intended regression signal.
- Watch for any reading of the harness as a safety, security, or compliance claim; the boundary note and printed caveat exist to prevent that, and should be reinforced if misread.
- Revisit adding more eval cases as new worked examples are published.

## Maintainer follow-ups

- Consider pairing this with the `closing-stale-packets` skill (Track C) so abandonment and efficacy both have first-class support.
- Consider whether a future case should score a non-comparison artifact (for example a real packet) to broaden the guard.

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
