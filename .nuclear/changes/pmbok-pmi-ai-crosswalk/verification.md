# Standard Verification Template

**Purpose:** Show that the important claims, controls, and assumptions have evidence that fits the size of the change.

**Activation threshold:** Use for Standard changes, and any Quick change whose proof needs more than one simple check.

**Minimum useful version:** the claims, the methods, the acceptance criteria, the commands/evals/reviews, the results, the evidence links, and the gaps.

**Overhead trap:** Do not treat "tests passed" as proof. The evidence must match the claim, be repeatable enough to review, and carry a status label.

---

## Verification context

- Slug: pmbok-pmi-ai-crosswalk
- Related basis: `basis.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-06-21
- Verification scope: Boundary discipline (no overclaim), no PMI text/structure reuse, flat always-on token cost, link integrity.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test / peer review | Overclaim scan + human PR review of wording | No bare compliance/conformance/PMP claim; all hits negative/boundary | pass | `ng doctor` OK; scan output (all hits negative) | none |
| REQ-002 | local proof | self-check / peer review | Inspect crosswalk + source-map; confirm PMI excluded-direct, PMBOK 8 structural only | No PMI text reproduced; excluded-direct rows present | pass | `source-map.md` Tier 10 + excluded list; `do-not-cite-directly.md` | none |
| REQ-003 | local proof | deterministic test | `git diff` descriptions + `gen-commands` card diff | No `description:` change; no `commands/` change | pass | `git diff -U0 skills/` (no description lines); `git status commands/` empty | none |

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
| Boundary scan | `python tools/ng.py doctor .` | repo | OK | console |
| Packet validation | `python tools/ng.py validate .nuclear/changes/pmbok-pmi-ai-crosswalk` | repo | (run at audit) | console |
| Command-card flatness | `python tools/ng.py gen-commands && git status --short commands/` | repo | empty diff | console |
| Description flatness | `git diff -U0 skills/ \| rg -i 'description:'` | repo | empty | console |
| Link integrity | extract+test relative links in crosswalk | repo | all resolve | console |

## Negative / failure-mode checks

What did you try to break?

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Hidden compliance claim | grep for compliant/conforms/certified/PMP/aligned-with outside negative sentences | only negative/boundary hits | scan output |
| Skill description creep | diff descriptions | none | `git diff` |
| Command-card churn | regenerate + status | none | `git status commands/` |
| Broken cross-links | resolve every relative link in new doc | all resolve | link check |

## AI-assisted work checks

Use if AI did real work here or had power over tools.

- AI scope: drafted the crosswalk, governance edits, skill fold-ins, and this packet under an approved plan.
- Model/tool used: Claude Code (claude-opus-4-8) with repo file tools.
- Permissions/actions allowed: edit repo files on the feature branch; run `ng` tooling and read-only scans.
- Independent checks performed: deterministic `ng`/git checks above; human PR review required before merge.
- Self-check / turnover records: self-check folded into this file; no turnover (single session).
- Hallucination/slop screening: PMBOK 8 per-item names deliberately not asserted; only public-described themes used.
- Human approval gates exercised: plan approval (ExitPlanMode); PR review pending before merge.

## Security / dependency / supply-chain checks

Use if activated. — Not activated; no code, dependency, or build change.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: PR checks
- Implementation diff / PR: this PR

## Exit criteria

- Each important claim has a status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software verification and validation (V&V), test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
