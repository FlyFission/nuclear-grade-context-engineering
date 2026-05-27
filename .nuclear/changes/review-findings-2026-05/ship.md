# Ship

## Release decision

- **Decision:** ship as version 0.2.0 once CI is green on both Python 3.11 and 3.12 legs and the `wheel-smoke` job passes.
- **Rationale:** The validator's new Mode requirement is a deliberate breaking change versus 0.1.x. A minor-version bump signals that to anyone with pinned downstream usage. The `migrate` subcommand exists to help.
- **Pre-merge gates:**
  - `python -m pytest -q` green
  - `python tools/ng.py doctor .` OK
  - `python tools/ng.py validate` OK on every existing packet
  - `python tools/ng.py validate .nuclear/changes/review-findings-2026-05` OK
  - CI green on both 3.11 and 3.12 matrix legs
  - `ruff check .` clean
  - `wheel-smoke` job green

## Evidence status summary

| Area | Status | Link |
|---|---|---|
| Verification | pass | `verification.md` |
| Trace | pass | `trace.md` |
| Basis | pass | `basis.md` |
| Test suite | pass | `tests/` (73 tests at this writing) |
| Wheel install | pass | local build artifact + `wheel-smoke` job |
| Packet self-validation | pass | `python tools/ng.py validate .nuclear/changes/review-findings-2026-05` |

## Rollback / restore plan

- The work lands as one branch (`claude/intelligent-knuth-QA4L5`) with commits aligned to the layered execution order in `plan.md`. The PR is a draft.
- Rollback option A (clean revert): `git revert <merge-commit>` after merge.
- Rollback option B (partial revert): revert only the validator commits if F3/F4 trip an unexpected downstream. The wheel rework and the content fixes are independent and survive.
- Rollback option C (deferred F2): if the `wheel-smoke` job uncovers a hatchling incompatibility, revert `pyproject.toml` and `_bundled/`-resolver code; ship the other eleven fixes as 0.2.0 and call out F2 as "deferred to 0.2.1" in `CHANGELOG.md`.

## Monitoring and post-release checks

- Watch the `wheel-smoke` job on every PR for at least the first three PRs after merge.
- Watch `validate` runs against the seven existing repo packets for any false-positive prohibited-claim regressions.
- Encourage early adopters to file a GitHub issue with the offending phrase and surrounding paragraph if the paraphrase detector flags legitimate boundary prose. Treat each as a deduplication candidate for the negation gate (`BOUNDARY_PREFIXES` or `_has_paragraph_disclaimer` markers).
- After release, watch for any external user reports that `migrate` produced a wrong-mode inference. The default behavior (Standard if any Standard-only file present, otherwise Quick) is the simplest possible heuristic and may need refinement.

## Maintainer follow-ups (post-merge)

- Replace `MAINTAINER:` placeholder in `CITATION.cff` with the preferred citation identity.
- Replace `@MAINTAINER` in `.github/CODEOWNERS` with the maintainer's GitHub handle.
- Tag the release as `v0.2.0` after the placeholder edits land on `main`.

## Required links

- `risk.md`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`

## Exit criteria

- Decision is recorded.
- Rollback plan is named.
- Monitoring is named.
- Maintainer follow-ups are explicit.

## Source-lineage note

Original Nuclear-grade ship record inspired by lifecycle-decision and release-readiness concepts mapped in [`docs/00-standards-foundation/source-map.md`](../../../docs/00-standards-foundation/source-map.md). No compliance claim is made.
