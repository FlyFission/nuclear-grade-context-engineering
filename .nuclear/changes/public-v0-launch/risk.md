# Risk — Public v0 Launch

**Purpose:** Sort the public v0 launch hardening work by risk, and name the evidence needed before the repository is made public.

---

## Change identity

- **Slug:** `public-v0-launch`
- **PR / issue:** launch-readiness branch / PR
- **Owner:** Maintainer
- **Date:** 2026-05-19
- **Current lifecycle phase:** Prove
- **Summary:** Prepare Nuclear-grade for public v0 by cleaning public residue, tightening source-lineage status, aligning validator behavior with Quick and Standard packet docs, and gating GitHub visibility behind PR/CI/review.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| Public docs | Documentation | First public trust surface. | `README.md`, `QUICKSTART.md`, `docs/` |
| Source map | Documentation | Controls citation safety and source-lineage claims. | `docs/00-standards-foundation/source-map.md` |
| Validator | Tooling | Deterministic launch gate for packets. | `tools/ng_validate.py` |
| Validator tests | Tests | Prove Quick and Standard behavior. | `tests/test_ng_validate.py` |
| Worked example | Example packet/code/tests | Public proof of the thin evidence spine. | `docs/03-worked-examples/ai-agent-tool-permissions/` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | Medium | Public release can create overtrust if language is stale or overbroad. |
| Reversibility | Medium | Docs can be patched, but first public impression and forks may persist. |
| Detectability | Medium | Residue and source-status issues need explicit scans. |
| Exposure | High | GitHub public visibility exposes all tracked files. |
| Uncertainty | Medium | Source pages and GitHub API availability can change. |
| Dependency trust | Low | Python standard library plus pytest in CI. |
| AI authority | Medium | AI-assisted edits affect public docs/tooling and need independent verification. |

## Selected mode

- **Mode:** Standard
- **Why this mode:** The launch affects public trust posture and release readiness.
- **Why lighter mode is not enough:** Quick mode would not capture source-lineage, validator, and visibility gates.
- **Why heavier mode is not yet required:** This is a public educational v0, not a regulated or production assurance release.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `basis.md` | yes | Defines launch claims and non-claims. | Maintainer |
| `plan.md` | yes | Bounds implementation and verification sequence. | Maintainer |
| `trace.md` | yes | Links launch claims to evidence. | Maintainer |
| `verification.md` | yes | Records commands and scan results. | Maintainer |
| `ship.md` | yes | Controls PR/merge/visibility decision. | Maintainer |
| Nuclear subset record | no | Not activated for public educational v0. | Maintainer |

## Immediate proof obligations

- Public residue scan is clean.
- Source-map status labels are explicit.
- Quick and Standard validator tests pass.
- Worked-example and launch packets validate.
- GitHub visibility changes only after PR merge and CI pass.

## Required links

- Packet: `.nuclear/changes/public-v0-launch/`
- `basis.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references: `../../../docs/00-standards-foundation/source-map.md`, `../../../docs/01-field-guide/source-to-concept-crosswalk.md`

## Exit criteria

- Mode is justified.
- Activated artifacts are explicit.
- Launch blockers and proof obligations are visible.
- Visibility flip remains gated behind PR/CI/review.

## Source-lineage note

Original Nuclear-grade launch packet inspired by public graded quality, configuration management, lifecycle, verification, release-readiness, and source-lineage concepts mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
