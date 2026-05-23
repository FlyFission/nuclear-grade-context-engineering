# Change Impact Record

**Purpose:** Screen downstream artifacts that may become stale when controlled configuration changes.

**Activation threshold:** Use when a change affects more than one artifact family or could invalidate docs, tests, skills, command prompts, validators, release posture, source lineage, or operational assumptions.

**Minimum useful version:** Impacted artifact family, required update, evidence, owner, and disposition.

**Overhead trap:** Do not turn impact screening into a generic checklist. Only record impacts that could change review or release decisions.

---

## Change context

- Slug:
- Related packet:
- Owner:
- Date:

## Impact screen

| Artifact family | Impact | Required action | Evidence / link | Disposition | Owner |
|---|---|---|---|---|---|
| Docs/public claims | | update / no-op / defer / block | | | |
| Tests/evals/validator | | update / no-op / defer / block | | | |
| Skills/commands/templates | | update / no-op / defer / block | | | |
| Dependencies/models/tools | | update / no-op / defer / block | | | |
| Release/operate/support | | update / no-op / defer / block | | | |

## Revalidation triggers

| Trigger | What must be rerun or reviewed | Owner |
|---|---|---|
| | | |

## Required links

- `risk.md`
- `basis.md`
- `controlled-items.md` if activated
- `verification.md`
- `ship.md`

## Exit criteria

- Impacted artifact families are updated, deferred with owner, or explicitly not applicable.
- Revalidation triggers are visible.
- No stale public claim or validator behavior is silently accepted.

## Source-lineage note

Original Nuclear-grade CM template inspired by public configuration-management, secure-development, lifecycle, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
