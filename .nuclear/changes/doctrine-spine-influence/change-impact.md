# Change Impact Record

**Purpose:** Check which downstream files may go out of date when the doctrine-spine controls change.

**Activation threshold:** Use because this change affects multiple artifact families and could stale public docs, skills, commands, templates, evaluation prompts, and release posture.

**Minimum useful version:** Impacted artifact family, required update, evidence, owner, and disposition.

**Overhead trap:** Only record impacts that could change review, adoption, agent behavior, or release decisions.

---

## Change context

- Slug: doctrine-spine-influence
- Related packet: `.nuclear/changes/doctrine-spine-influence/`
- Owner: FlyFission
- Date: 2026-05-30

## Impact screen

| Artifact family | Impact | Required action | Evidence / link | Disposition | Owner |
|---|---|---|---|---|---|
| Docs/public claims | Public doctrine and adoption wording changes | update | `verification.md` | planned | FlyFission |
| Tests/evals/validator | Contract/public tests must still pass; no validator changes planned | update evaluation prompts; no-op validator | `verification.md` | planned | FlyFission |
| Skills/commands/templates | Agent-operable surfaces must reflect control stack | update | `verification.md` | planned | FlyFission |
| Dependencies/models/tools | No trust-bearing external item changes | no-op | `basis.md` | not applicable | FlyFission |
| Release/operate/support | Baseline and PR review posture changes | update | `ship.md`, `baseline.md` | planned | FlyFission |

## Revalidation triggers

| Trigger | What must be rerun or reviewed | Owner |
|---|---|---|
| Skill or command wording changes | Skill/command contract tests and evaluation prompt review | FlyFission |
| Public docs or templates change | Public-doc tests, doctor, boundary scan | FlyFission |
| New source lineage, quote, or attribution is proposed | Source/legal check and source-map decision | FlyFission |
| Validator or CLI behavior change is proposed | Full validator/CLI tests and packet update | FlyFission |

## Required links

- `risk.md`
- `basis.md`
- `controlled-items.md`
- `verification.md`
- `ship.md`

## Exit criteria

- Impacted artifact families are updated, deferred with owner, or explicitly not applicable.
- Revalidation triggers are visible.
- No stale public claim or validator behavior is silently accepted.

## Source-lineage note

Original Nuclear-grade CM record inspired by public configuration-management, secure-development, lifecycle, and release-readiness sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
