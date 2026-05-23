# Standard Verification Template

**Purpose:** Show that important claims, controls, and assumptions have evidence proportionate to the change.

**Activation threshold:** Use for Standard changes and any Quick change whose proof needs more than one simple check.

**Minimum useful version:** Claims, methods, acceptance criteria, commands/evals/reviews, results, evidence links, and gaps.

**Overhead trap:** Do not equate “tests passed” with proof. Evidence must match the claim, be reproducible enough for review, and be status-labeled.

---

## Verification context

- Slug:
- Related basis: `basis.md`
- Owner:
- Date:
- Verification scope:

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`.

## Claim-to-evidence table

| Claim / requirement ID | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|
| REQ-001 | | | | | |

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

Use if AI materially contributed or had tool authority.

- AI scope:
- Model/tool used:
- Permissions/actions allowed:
- Independent checks performed:
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

- Each important claim has `pass`, `fail`, `gap`, `deferred`, or `not applicable` status.
- Evidence is linked rather than pasted in full.
- Gaps are explicit and reflected in `ship.md`.
- Reviewer can tell whether the evidence supports the release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public software V&V, test-documentation, secure-development, software assurance, AI-risk, and application-security verification sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
