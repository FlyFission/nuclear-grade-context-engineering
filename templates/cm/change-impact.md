# Change Impact Record

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Check which downstream files may go out of date when a controlled item changes.

**Activation threshold:** Use when a change affects more than one family of files, or could make docs, tests, skills, command prompts, validators, the release stance, source lineage, or operating assumptions out of date.

**Minimum useful version:** the family of files affected, the update needed, the evidence, the owner, and the disposition.

**Overhead trap:** Do not turn the impact check into a generic checklist. Record only the effects that could change a review or release decision.

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
| Runtime/data blast radius (only if a running system or stored data is touched: schema/state, API consumers, backward-compat, rollback-of-state) | | update / no-op / defer / block | | | |

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

- The affected families of files are updated, deferred with an owner, or clearly marked not applicable.
- The re-check triggers are visible.
- No out-of-date public claim or validator behavior is quietly accepted.

## Source-lineage note

Original Nuclear-grade CM template (for keeping the approved version under control) inspired by public sources on configuration management, secure development, software lifecycle, and release readiness, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
