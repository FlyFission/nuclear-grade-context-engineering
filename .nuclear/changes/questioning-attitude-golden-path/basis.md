# Basis

## Change basis

The public golden path should start with a nuclear/HPI-native behavior that is teachable to agent users. DOE-HDBK-1028-2009 provides public source lineage for questioning attitude, validate assumptions, pause when unsure, review, and operating learning. For this repo, that translates to "grill my change with facts before the agent builds."

## Derived requirements or claims

| ID | Requirement / claim | Evidence planned |
|---|---|---|
| QA-001 | Public lifecycle uses `Question -> Discover -> Specify -> Plan -> Execute -> Verify -> Review -> Decide -> Baseline -> Operate -> Learn`. | Public-doc test and README/lifecycle scan. |
| QA-002 | New questioning-attitude skill and `ng-question` command satisfy repo contracts. | Skill and command contract tests. |
| QA-003 | CLI doctor/list knows the golden-path templates. | CLI tests and `python tools/ng.py doctor .`. |
| QA-004 | DOE-HDBK-1028 is source lineage only, not a compliance claim. | Source-map/crosswalk docs and boundary scans. |

## Required links

- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`
- `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The public hook is Questioning Attitude.
- `Classify` remains an internal risk/mode screen.
- Baseline is presented as accepted state after review/decision.

## Source-lineage note

Original workflow basis mapped to public source lineage in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
