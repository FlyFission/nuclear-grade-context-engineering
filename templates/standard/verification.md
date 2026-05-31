# Standard Verification Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Show that the important claims, controls, and assumptions have evidence that fits the size of the change.

**Activation threshold:** Use for Standard changes, and any Quick change whose proof needs more than one simple check.

**Minimum useful version:** the claims, the methods, the acceptance criteria, the commands/evals/reviews, the results, the evidence links, and the gaps.

**Overhead trap:** Do not treat "tests passed" as proof. The evidence must match the claim, be repeatable enough to review, and carry a status label.

---

## Verification context

- Slug:
- Related basis: `basis.md`
- Owner:
- Date:
- Verification scope:

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | fact / assumption / unknown / source claim / local proof / decision authority | deterministic test / eval / self-check / peer-check / concurrent verification / independent verification / peer review | | | | | |

## Verification type guide

| Type | Use when |
|---|---|
| self-check | the target of a critical action and the expected result matter |
| peer-check | another reviewer should stop a wrong action before it happens |
| concurrent verification | a high-stakes action must be watched as it happens |
| independent verification | the final state must be checked apart from the doer's claim |
| peer review | artifact quality, maintainability, usability, or boundary wording matters |
| deterministic test / eval | there is repeatable evidence of the behavior |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Unit/integration/eval/review | | | | |

## Negative / failure-mode checks

What did you try to break?

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| | | | |

## AI-assisted work checks

Use if AI did real work here or had power over tools.

- AI scope:
- Model/tool used:
- Permissions/actions allowed:
- Independent checks performed:
- Self-check / turnover records:
- Hallucination/slop screening:
- Human approval gates exercised:

## Security / dependency / supply-chain checks

Use if activated.

- Dependency review:
- SBOM/provenance/build evidence:
- Vulnerability/security review:
- Revalidation trigger:

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes:
- Implementation diff / PR:

## Exit criteria

- Each important claim has a status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software verification and validation (V&V), test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
