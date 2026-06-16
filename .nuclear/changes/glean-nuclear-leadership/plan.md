# Standard Plan Record

**Purpose:** Sequence the edits so each workstream lands as a small, reviewable change against the file that already owns the concept.

**Activation threshold:** Standard mode: multiple controlled docs, a charter article, a skill, a command, and a template change together.

**Minimum useful version:** An ordered build sequence with the files each step touches, the requirement it covers, and a per-step done condition.

---

## Build sequence

| # | Task | Requirements covered | Files | Proof for this step | Done condition |
|---|---|---|---|---|---|
| 1 | Refine charter Art. 19 + bump to 1.3.0; add just-culture to the learning skill and `ng-learn` | REQ-001 | `.nuclear/charter.md`, `skills/learning-from-experience/SKILL.md`, `commands/ng-learn.md` | skill + command contract tests pass | Honest-error vs willful-violation distinction reads cleanly and tests pass |
| 2 | State layer independence in the HPI control stack; cross-link from authority-and-intent; add crosswalk row | REQ-002 | `docs/02-operating-system/configuration-management.md`, `docs/02-operating-system/authority-and-intent.md`, `docs/01-field-guide/source-to-concept-crosswalk.md` | manual read; links resolve | Independence + correlated-failure + graded layering are stated and cross-linked |
| 3 | Add deliberate temporary-modification discipline to variance doc + template; add crosswalk row | REQ-003 | `docs/02-operating-system/variance-and-drift.md`, `templates/cm/variance.md`, `docs/01-field-guide/source-to-concept-crosswalk.md` | template still carries its placeholder; token audit green | Temp-mods have visibility, back-out, and expiry; back-out column added |
| 4 | Fold competence-to-act qualification into authority-and-intent | REQ-004 | `docs/02-operating-system/authority-and-intent.md` | manual read; links resolve | Qualification section defines action-class → competence → revalidation |
| 5 | Write the durable-memory doctrine; back-link from context-window discipline; amend the leadership boundary; add nav | REQ-005 | `docs/02-operating-system/durable-memory.md`, `docs/02-operating-system/context-window-discipline.md`, `docs/01-field-guide/leadership-and-high-reliability.md`, `docs/README.md` | manual boundary read; links resolve | Memory doctrine exists with provenance guard; boundary stays crisp |
| 6 | Record CHANGELOG entry and author this packet | all | `CHANGELOG.md`, this packet | `ng validate` passes | Packet validates and CHANGELOG names the change |
| 7 | Verify end to end | all | none (test run) | suite + token audit + doctor + validate green | All checks pass; residual risk recorded in `ship.md` |

## Rollback

- Method: revert the branch commit; every change is text in version control.
- State reversal: none; no data, schema, or production state is touched.

## Required links

- `risk.md`
- `basis.md`
- `trace.md`
- `ship.md`

## Exit criteria

- Each step names its files, requirement, and done condition.
- A rollback path exists.
- The sequence keeps each edit in the file that already owns the concept.

## Source-lineage note

Original Nuclear-grade plan record inspired by public configuration-management and lifecycle sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
