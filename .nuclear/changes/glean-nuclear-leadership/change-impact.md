# Change Impact

**Purpose:** Screen what else could go out of date because of this change, so a stale doc, test, or index is caught before merge.

**Activation threshold:** CM records are activated; more than one group of files is affected.

**Minimum useful version:** Each affected group with the action taken and where it is verified.

---

## Impact screen

| Affected group | Impact | Action | Where verified | Status | Owner |
|---|---|---|---|---|---|
| Charter version + amendment log | Art. 19 refined; version must bump | update to 1.3.0 with a log entry | `verification.md` | pass | FlyFission |
| Skill / command contracts | learning skill edited; `ng-learn` prompt regenerated to match | keep section structure intact; the deliberate prompt change is mirrored in the `command_prompts.json` golden fixture | `verification.md` | pass | FlyFission |
| Token budgets | new doc + doc additions add prose | confirm `ng tokens` stays green | `verification.md` | pass | FlyFission |
| Cross-links between docs | durable-memory ↔ context-window; authority-and-intent; leadership doc | confirm relative links resolve | `verification.md` | pass | FlyFission |
| Docs navigation index | new doc should be discoverable | add a `docs/README.md` row | `verification.md` | pass | FlyFission |
| `nuclear-grade.yaml` / plugin manifest | only if a skill/command/template mode is added | no-op; none added | `basis.md` | not applicable | FlyFission |
| Tests / evals / validator | no behavior change intended | no-op; run the suite to confirm | `verification.md` | pass | FlyFission |
| Dependencies / models / tools | no trust-bearing external item changes | no-op | `basis.md` | not applicable | FlyFission |

## Required links

- `risk.md`
- `controlled-items.md`
- `verification.md`

## Exit criteria

- Every affected group has an action and a verification location.
- No-op groups are named so the absence of action is a decision, not an omission.

## Source-lineage note

Original Nuclear-grade change-impact record inspired by public configuration-management sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
