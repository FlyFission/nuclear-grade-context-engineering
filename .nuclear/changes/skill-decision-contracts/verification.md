# Verification -- skill decision contracts

**Purpose:** Show the important claims have evidence that fits the size of the change.

---

## Verification context

- Slug: skill-decision-contracts
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-06-16
- Verification scope: the decision-contract block, its enforcement, and the rollup command.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test | `pytest` and `ng doctor` over all skills | every skill has the receipt, the five fields, and a valid tier | pass | `tests/test_skill_contracts.py` | none |
| REQ-002 | local proof | deterministic test | `ng decisions` and a CLI smoke test | all 27 skills render with a named decision | pass | `tests/test_ng_cli.py` | none |
| REQ-003 | local proof | deterministic test | `ng tokens` | descriptions stay flat, bodies stay under budget | pass | `docs/05-reference/skills-token-audit.md` | none |

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
| test | `python -m pytest -q` | local Python 3.11 | pass | CI to confirm on the PR |
| doctor | `python tools/ng.py doctor .` | local Python 3.11 | `OK: Nuclear-grade doctor` | CI to confirm on the PR |
| tokens | `python tools/ng.py tokens .` | local Python 3.11 | `OK: token budget` | CI to confirm on the PR |
| rollup | `python tools/ng.py decisions .` | local Python 3.11 | 27 skills, 20 block, 7 warn, 0 observe | CI to confirm on the PR |

## Negative / failure-mode checks

What did you try to break?

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Missing or malformed block | the lint asserts the labels and the class | doctor fails on a gap | `nuclear_grade/cli.py` |
| HTML-escaped placeholders in blocks | grep for `&lt;` and `&gt;` across skills | none found | `skills/` |

## AI-assisted work checks

Use if AI did real work here or had power over tools.

- AI scope: drafted the blocks, the validator change, the rollup, and this record under human approval.
- Model/tool used: Claude Code on branch `claude/practical-faraday-dwcv5b`.
- Permissions/actions allowed: edit repository files and run tests locally.
- Independent checks performed: the full pytest suite, doctor, tokens, and decisions.
- Self-check / turnover records: not activated; the change is low-risk and reversible.
- Hallucination/slop screening: each block was reviewed against the skill's real artifacts, and paths were grep-verified.
- Human approval gates exercised: plan approval, and PR review before merge.

## Security / dependency / supply-chain checks

Use if activated.

- Dependency review: not applicable; no dependencies added.
- SBOM/provenance/build evidence: not applicable.
- Vulnerability/security review: not applicable; this is documentation and a stdlib lint.
- Revalidation trigger: a future change to the skill contract or the validator.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: CI on the PR
- Implementation diff / PR: branch `claude/practical-faraday-dwcv5b`

## Exit criteria

- Each important claim has a status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade change record, influenced by public software verification and assurance ideas mapped in `docs/00-standards-foundation/source-map.md`. It does not create formal assurance, compliance, certification, safety, security, or regulatory adequacy.
