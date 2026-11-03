# Independent Review and Fact Checking — Trace

| Requirement | Design feature | Implementation | Evidence |
|---|---|---|---|
| REQ-001 | Parties from the custody record or the authorship table; self-check rows excluded; placeholder verifiers empty; fail closed | `nuclear_grade/two_party.py` (`check_two_party`, `_is_second_party`, `_excluded_identities`); `nuclear_grade/ng_validate.py` (`parties_out`, `require_two_party`) | `tests/test_two_party.py`; `verification.md` V-2, V-3 |
| REQ-001 | Flag exposed on every entry point | `nuclear_grade/cli.py` `--two-party`; `ng_validate.main`; `mcp_server.validate_change_record(two_party=)`; `receipt.strict.two_party` | `tests/test_receipt.py`; `verification.md` V-1 |
| REQ-002 | Opt-in only; the authorship table is the sole default-mode trigger | `check_two_party(required=False)` returns early unless a `## Claim authorship` table exists | `verification.md` V-4 |
| REQ-003 | Quotes copied from fetched primary text | `docs/02-operating-system/verification-methods-and-depth.md`; source-map and crosswalk rows | `verification.md` V-5 |
| REQ-004 | Skill contract and catalog wiring | `skills/checking-facts/SKILL.md`; `commands/ng-fact-check.md`; `nuclear-grade.yaml`; `CORE.md`; `SKILLS.md`; `COMMANDS.md`; eval cases; tests | `verification.md` V-1, V-6 |
| REQ-005 | Audit with stated limits; proposal only | `evals/skill-catalog-audit/2026-11-03.md` | `verification.md` V-7 |

## Required links

- Basis: `basis.md`
- Verification: `verification.md`

## Exit criteria

- Every requirement traces to an implementation and to evidence.

## Source-lineage note

Original Nuclear-grade traceability record inspired by public requirements-to-verification practice mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
