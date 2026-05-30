# Controlled Items Record

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Name the controlled items this change affects, and why their state matters.

**Activation threshold:** Use when the affected items include prompts, models, tools, dependencies, source-lineage claims, release artifacts, public docs, validators, runbooks, or other state that carries trust.

**Minimum useful version:** the controlled item, its current state, its intended state, the owner, an evidence link, and a re-check trigger.

**Overhead trap:** Do not list the whole repo. List only the items whose state matters to this change.

---

## Change context

- Slug:
- Related packet:
- Owner:
- Date:

## Controlled item table

| Item | Type | Current state | Intended state | Why controlled | Owner | Evidence / link | Revalidation trigger |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Required links

- `risk.md`
- `basis.md`
- `change-impact.md` if activated
- `baseline.md` if activated

## Exit criteria

- Each item has a reason it is kept under control.
- Each item has an evidence link or a clearly marked gap.
- Re-check triggers are named for items that carry trust.

## Source-lineage note

Original Nuclear-grade CM template (for keeping the approved version under control) inspired by public sources on configuration management and software assurance, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
