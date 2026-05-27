# Ship

## Release identity

- Change slug: `harden-evidence-gate`
- Branch: `claude/zen-ptolemy-ZIQhj`
- Owner: maintainer
- Date: 2026-05-27
- Intended release window: as part of the next merge to `main` for `flyfission/nuclear-grade-context-engineering`.

## Scope and exclusions

- Included: validator marker check, template marker injection, doctor's four added public files, removal of the SWOT report from version control, doc updates to the Try-it sequence, CI step for the new packet, CHANGELOG entry, and tests covering the marker behavior.
- Excluded: vendor-neutral rename of `flyfission-ops-knowledge-graph-usage.md`; defense-in-depth table-row status check.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard mode justified. |
| Basis / claims | pass | `basis.md` | Five claims, each traced. |
| Verification | pass | `verification.md` | All commands rerun in this session. |
| Dependency / supply-chain | not applicable | `verification.md` | No dependency changes. |
| AI-assisted work checks | pass | `verification.md` | Recorded. |
| Review / approval | gap | this PR | Maintainer review pending on merge. |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| `flyfission-ops-knowledge-graph-usage.md` framing is vendor-specific. | Public positioning. | defer | maintainer | Next public-positioning pass. |
| Defense-in-depth table-row status check skipped. | Marginal additional resilience to prose collisions. | defer | maintainer | Recorded in `verification.md`. |

## Rollback / restore plan

- Rollback method: `git revert` the merge commit on `main`.
- State/data reversal: none. The SWOT file already exists in maintainer working trees under `.research/`; a revert would restore the public copy.
- Feature flag / kill switch: not applicable.
- Owner on call: maintainer.
- Time to restore estimate: under one minute.

## Monitoring and post-release checks

| Signal | Expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| CI on `main` | All packet validations pass, including `harden-evidence-gate`. | maintainer | GitHub Actions. | Re-run, then fix root cause and re-merge. |
| Downstream consumers of `tools.ng_validate` | Imports of `validate_packet`, `detect_packet_mode`, `ValidationResult`, `main` still resolve. | maintainer | issues. | Patch release if a real consumer reports a break. |
| User reports of unexpected validation failure | Failure messages name the file plus the marker. | maintainer | issues. | Triage; the message is the documented behavior. |

## Handoff

- Operator/customer notes: README, INSTALL, and QUICKSTART now state that validate is expected to fail on an untouched packet and show the fix.
- Docs updated: README, INSTALL, QUICKSTART, CHANGELOG.
- Communication needed: PR description; no external announcement.
- Follow-up date: next public-positioning pass.

## Release decision

- Decision: ship with named residual risk (deferred vendor-neutral rename, deferred defense-in-depth status check).
- Decision maker: maintainer at merge.
- Rationale: the load-bearing fix is in place, all existing packets and tests stay green, and the deferred items are explicit.
- Conditions attached: monitoring item on CI must remain green post-merge.

## Baseline trigger

- Baseline required? yes. `nuclear_grade/ng_validate.py`, `nuclear_grade/cli.py`, and the templates under `templates/` are now controlled items whose state must remain reviewable.
- Baseline record: this packet plus the merge commit.
- Revalidation trigger: any change to `PLACEHOLDER_MARKER`, `REQUIRED_PUBLIC_FILES`, or the template marker line.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- Branch: `claude/zen-ptolemy-ZIQhj`
- Repo: `flyfission/nuclear-grade-context-engineering`

## Exit criteria

- Release decision is explicit.
- Baseline trigger is explicit.
- Evidence status and gaps are visible.
- Rollback path exists.
- Monitoring covers the validator and the doctor.
- Any accepted residual risk has an owner and recheck trigger.

## Source-lineage note

Original Nuclear-grade release record grounded in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
