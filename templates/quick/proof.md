# Quick Proof Template

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Capture the smallest believable evidence record for a Quick change.

**Activation threshold:** Use with `risk.md` when a change is low-stakes, easy to undo, easy to check, and does not trip Standard mode.

**Minimum useful version:** one proof command, check, or eval; the result; an evidence link; and a reviewer note.

**Overhead trap:** Do not paste long logs. Link to the evidence and quote only the result that matters.

---

## Proof summary

- Change slug:
- Proof owner:
- Date/time:
- Risk record: `risk.md`

## Claim proven

> Example: The renamed command still starts successfully.

Claim:

## Method

- Command/check/eval/review:
- Environment:
- Inputs/fixtures:
- Expected result:
- Self-check used? yes/no; target if yes:

## Result

- Status: pass / fail / gap / not applicable
- Actual result:
- Evidence link or artifact path:
- If failed/gap: follow-up action:

## Reviewer note

- Reviewer:
- Review note:
- Is Quick mode still valid after proof? yes/no:

## Required links

- Related PR/issue:
- Relevant changed files:
- CI run / test output / eval report / screenshot / log:
- If AI-assisted: link to AI scope or independent check note:

## Exit criteria

- The evidence matches the claim in `risk.md` directly.
- The actual result is compared to the expected result you named before the proof.
- The result status is stated plainly.
- Any failure or gap has a next action or an escalation.
- The reviewer can decide whether the Quick change is acceptable without reading unrelated docs.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on software test documentation, verification, work records, and keeping the approved version under control, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
