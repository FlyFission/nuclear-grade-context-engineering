# Independent Review and Fact Checking — Basis

## Problem

The review of the repo's own review capability found:

- **The two-party check is parked.** `nuclear_grade/two_party.py` was written to stop a claim from being marked verified by the identity that authored its evidence. Its header said "proposal, not yet wired in", and the validator never imported it. It also read only a `## Claim authorship` table that no packet in the repo used. Meanwhile the evidence-custody record, which 8 packets do carry, already names `Verified / witnessed by`.
- **No fact-checking skill exists.** `checking-source-claims` checks how a citation is worded, not whether the cited fact is true. `proving-claims` maps claims about the change to local evidence. Nothing covered "is this number, quote, version, or behavior true?"
- **There is no depth vocabulary.** `independence-architecture.md` says *who* is separate, but nothing says *how deep* a check went or whether the result was reached by more than one means. Public nuclear QA language draws exactly that line: a design is verified by design review, by alternate or simplified calculation, or by qualification testing, and that is more than a check. The owner asked for that vocabulary explicitly: "independent review (arriving at an outcome using multiple means/methods) as well as deep review."
- **Whether the skills are used and add value had not been answered with evidence.**

## Requirements

| ID | Requirement | Acceptance |
|---|---|---|
| REQ-001 | `ng validate --two-party` fails any `pass` claim in a Standard packet that has no declared second party. A second party comes from the custody record (verifier not the change actor, and the row not classified `self-check`) or from a `## Claim authorship` table (verifier neither the author nor the change actor). Placeholder verifiers count as empty. With nothing to check, the run fails closed. | Unit tests, worked-example behavior, repo sweep |
| REQ-002 | Without the flag, validation output for every existing packet is unchanged. | Byte-identical output against `main`, default and `--strict-custody` |
| REQ-003 | `verification-methods-and-depth.md` quotes 10 CFR 50 Appendix B Criterion III and DOE-HDBK-1028-2009 Vol. 2 exactly, paraphrases them faithfully, and makes no compliance claim. | Two-copy comparison; reviewer re-fetch; prohibited-claims scan |
| REQ-004 | `checking-facts` exists with the skill contract, is wired into every catalog surface, and its boundaries against `checking-source-claims` and `proving-claims` run both ways. | Contract tests, `ng doctor`, `ng tokens`, grep of counts |
| REQ-005 | The question of whether each skill is used and adds value is answered with cited evidence. Consolidation is proposed, not executed. | `evals/skill-catalog-audit/2026-11-03.md` with stated limits; no skill removed |

## Design choices

- **Read the custody record instead of inventing a second table.** The custody record already declares, per evidence row, the change actor, the generator, the verifier, and (in the coupling profile) a classification. `two_party` now takes those parties from the validator's existing parse. The authorship table stays as a lightweight alternative.
- **Compare against the change actor, not the generator, for custody rows.** An independent reproducer legitimately generates and witnesses their own re-run. The existing custody lint already forces actor-controlled evidence paths to be classified `self-check`, and a `self-check` row never counts.
- **Make it opt-in rather than default.** In strict mode 55 of 57 existing packets fail (see `verification.md`), most because they record no second party at all. That is an honest finding about the repo's history, not a reason to break every adopter's CI on upgrade. Declaring a `## Claim authorship` table opts a packet in.
- **Add one doctrine page rather than a skill per rung.** The ladder (self-check, check, design review, alternate method, qualification test) maps onto skills that already exist. Only the fact-checking gap needed a new skill.
- **Propose consolidation without executing it.** `docs/05-reference/independent-skill-benchmark-protocol.md` requires a separate human-reviewed change record before any skill is retired or demoted. Renames also break adopters' command names.

## Non-goals

- Making `--two-party` the default, or adding it to this repo's CI gate. That is the owner's decision; see `ship.md`.
- Detecting two names for one actor, or two agent instances of one model family. The doctrine page and the module docstring say this plainly.
- Executing any skill merge.

## Required links

- Risk: `risk.md`
- Plan: `plan.md`
- Trace: `trace.md`
- Doctrine: `../../../docs/02-operating-system/verification-methods-and-depth.md`
- Module: `../../../nuclear_grade/two_party.py`

## Exit criteria

- Every requirement has an acceptance method that a reviewer can rerun.
- Every design choice names the alternative it rejected.

## Source-lineage note

Original Nuclear-grade packet. Concept lineage for the depth vocabulary: 10 CFR 50 Appendix B, Criterion III, and DOE-HDBK-1028-2009, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
