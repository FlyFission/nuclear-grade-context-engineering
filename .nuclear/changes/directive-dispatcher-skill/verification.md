# Standard Verification

**Purpose:** Show the directive-router claims have evidence that fits the change.

---

## Verification context

- Slug: directive-dispatcher-skill
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-06-08
- Verification scope: the directive content is present and guarded; the skill stays within its contract + token budget. Excludes the behavioral-lift measurement (the A3 go/no-go, which needs a model-in-the-loop run).

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test + peer review | guard test asserts the classify-first step; manual read | "Classify first" + "declaration of intent" present | pass | `tests/test_skill_contracts.py` | none |
| REQ-002 | local proof | deterministic test | guard test asserts the MUST-promote trap list | >= 5 traps named; "MUST" + "Standard-plus" | pass | `tests/test_skill_contracts.py` | none |
| REQ-003 | local proof | deterministic test | the guard test exists and runs in the suite | guard test present and passing | pass | `tests/test_skill_contracts.py` | none |
| REQ-004 | local proof | deterministic test | skill-contract + token-budget tests | required sections; <=200 desc / <=3000 body | pass | `tests/test_skill_contracts.py`; `tests/test_tokens.py` | none |
| efficacy (behavioral lift) | unknown | independent measurement | A3 classification-rate eval, preamble ON vs OFF | a measurable lift at acceptable overhead | deferred | A3 (maintainer model-run) | tracked in `ship.md` |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Full suite | `python -m pytest -q` | Python 3 | all pass (incl. the new guard test) | CI |
| Lint | `python -m ruff check .` | ruff 0.15.16 | clean | CI |
| Doctor | `python tools/ng.py doctor .` | repo | OK | CI |
| Token budget | `python tools/ng.py tokens .` | repo | OK (skill body within budget) | CI |
| Packet validate | `python tools/ng.py validate .nuclear/changes/directive-dispatcher-skill` | repo | OK | CI |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Classification step silently removed | guard test asserts it is present | pass (fails if removed) | `tests/test_skill_contracts.py` |
| Skill body over budget | token-budget test | pass | `tests/test_tokens.py` |

## AI-assisted work checks

- AI scope: edited one skill's prose + added a guard test + drafted this packet under review.
- Model/tool used: Claude Code agent.
- Permissions/actions allowed: edit files; run tests; no executable hooks shipped.
- Independent checks performed: full suite + lint + doctor + tokens + validate.
- Self-check / turnover records: not activated.
- Hallucination/slop screening: the directive design traces to the approved plan, not invented.
- Human approval gates exercised: PR review + maintainer A3 run pending.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: GitHub Actions on the PR.
- Implementation diff / PR: this branch's PR.

## Exit criteria

- Each important claim has a status.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on software verification and validation and AI risk, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
