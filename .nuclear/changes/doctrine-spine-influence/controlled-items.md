# Controlled Items Record

**Purpose:** Name the controlled items this doctrine-spine change affects, and why their state matters.

**Activation threshold:** Use because this change affects public docs, skills, command prompts, templates, evaluation prompts, and baseline records.

**Minimum useful version:** Controlled item, current state, intended state, owner, evidence link, and revalidation trigger.

**Overhead trap:** Do not inventory the whole repo. List only trust-bearing artifact families affected by this change.

---

## Change context

- Slug: doctrine-spine-influence
- Related packet: `.nuclear/changes/doctrine-spine-influence/`
- Owner: FlyFission
- Date: 2026-05-30

## Controlled item table

| Item | Type | Current state | Intended state | Why controlled | Owner | Evidence / link | Revalidation trigger |
|---|---|---|---|---|---|---|---|
| `.nuclear/charter.md` | charter | Existing 1.0.0 articles | 1.1.0 with doctrine-spine articles | Durable principles guide all changes | FlyFission | `verification.md` | Charter amendment |
| README / WORKFLOWS / QUICKSTART | public docs | Teach lifecycle and quick adoption | Teach control stack without quotes or ceremony | End-user first-contact surface | FlyFission | `verification.md` | Public wording update |
| Operating-system docs | public docs | Lifecycle, HPI, thresholds, evidence spine | Preserve fast build and slow acceptance controls | Core workflow doctrine | FlyFission | `verification.md` | Workflow phase change |
| Adoption docs | public docs | Reviewer and authority guidance | Add end-user and downstream-agent review challenges | Team rollout and agent authority expectations | FlyFission | `verification.md` | Adoption guidance update |
| Selected skills | agent instructions | Existing trigger/process wording | Harder-to-misuse decision, evidence, drift, and acceptance controls | Downstream agent behavior | FlyFission | `verification.md` | Skill contract update |
| Selected commands | portable prompts | Existing pasteable prompt cards | Prompt outputs reflect control stack | Portable agent behavior | FlyFission | `verification.md` | Command prompt update |
| Standard templates | packet interface | Existing Standard packet prompts | Capture decision question, fact/source status, and audit gates | User evidence records | FlyFission | `verification.md` | Template update |
| Skill evaluation prompts | test/reference | Existing trigger prompt bank | Add prompts for wrong-question, ambiguity, premature acceptance, drift | Future skill quality review | FlyFission | `verification.md` | Skill behavior review |

## Required links

- `risk.md`
- `basis.md`
- `change-impact.md`
- `baseline.md`

## Exit criteria

- Each item has a reason for control.
- Each item has an evidence link or explicit gap.
- Revalidation triggers are named for trust-bearing items.

## Source-lineage note

Original Nuclear-grade CM record inspired by public configuration-management and software assurance sources mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
