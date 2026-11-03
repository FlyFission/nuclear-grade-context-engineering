# Independent Review and Fact Checking — Plan

## Sequence (as executed)

| Step | Work | Check before moving on |
|---|---|---|
| 1 | A background agent audits all 30 skills for use and value, read-only, while the other steps run | Its report is spot-checked against source files before use |
| 2 | Extend `two_party.py` to take parties from the custody record. Align its claim-ID regex with `RECORD_ID_PATTERN`, skip custody and authorship sections when reading claims, treat placeholder verifiers as empty, and fail closed in strict mode | Existing two-party tests still pass; new tests cover each branch |
| 3 | Wire it into `validate_packet(require_two_party=...)`, the CLI flag, standalone `main()`, the MCP tool, and the receipt | Full pytest; default-mode sweep against `main` |
| 4 | Fetch the primary text of App B (eCFR API and Cornell LII) and DOE-HDBK-1028-2009 Vol. 2 (DOE PDF); write `verification-methods-and-depth.md` | Quotes compared across both App B copies |
| 5 | Write `checking-facts`, register it, generate the card, update the golden fixture, counts, eval cases, and the diagram | Contract, parity, and CLI tests; `doctor`; `tokens`; the rendered diagram viewed |
| 6 | Add reciprocal When Not to Use pointers from `checking-source-claims` and `proving-claims` | Regenerated cards; tests |
| 7 | Save the audit as `evals/skill-catalog-audit/2026-11-03.md` with a provenance and coupling header | Header states it is a proposal plus a check, not an independent review |
| 8 | Run an independent review agent in a fresh context, briefed from the basis without the author's conclusions | Every finding verified against source before acting |
| 9 | Write this packet; run the full pre-PR gate; open a draft PR | Gate output recorded in `verification.md` |

## Deliberately not done

- No skill merged or removed. The audit's merges each need their own Standard packet and an owner decision.
- `--two-party` is not added to CI and not made the default.
- No branch-protection or CODEOWNERS change. That is the merge-level half of two-party integrity, and it lives in GitHub settings the owner controls.

## Required links

- Basis: `basis.md`
- Trace: `trace.md`
- Verification: `verification.md`

## Exit criteria

- Each step names the check that gated the next.
- The deliberately-not-done list matches `ship.md`'s open decisions.

## Source-lineage note

Original Nuclear-grade packet inspired by public configuration-management and verification practice mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
