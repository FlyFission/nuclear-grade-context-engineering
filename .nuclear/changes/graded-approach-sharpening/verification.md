# Standard Verification Record

**Purpose:** Record the evidence that the changes hold and that nothing regressed.

**Activation threshold:** Standard mode: public doctrine, an agent-loaded skill, the maxims, and the source map change.

**Minimum useful version:** the claims, the methods, the acceptance criteria, the commands/reviews, the results, and the gaps.

**Overhead trap:** Do not treat "tests passed" as proof. The evidence must match the claim and carry a status label.

---

## Verification context

- Slug: graded-approach-sharpening
- Related basis: `basis.md`
- Owner: FlyFission
- Date: 2026-06-17
- Verification scope: the floor + tripwires, the non-waiver maxim, change-vs-item, the performance-history modulator, and the DOE-anchored lineage, plus no regression in contracts, tokens, doctor, or boundary wording.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test / peer review | `doctor`, `validate`, manual read | Floor named on the same axis; reads as completing "smallest mode" | pass | `doctor` + `validate` output | PR review confirms wording |
| REQ-002 | local proof | deterministic test / peer review | skill contract tests; read of the tripwire list | Tripwires dominate; rationalizations extended, not blunted | pass | `pytest` (skill contracts) | PR review |
| REQ-003 | local proof | deterministic test | `test_public_docs` boundary check | Maxim present; no banned wording | pass | `pytest` | — |
| REQ-004 | local proof | deterministic test / peer review | `gen-commands --check`; read | Card matches skill; change-vs-item line present | pass | `gen-commands --check` | — |
| REQ-005 | local proof | peer review | read + link check | Performance-history dimension present; links to `deficiency-register.md` resolve | pass | `doctor` link check | — |
| REQ-006 | local proof | peer review | boundary read + `doctor` links | DOE-anchored; refs concept-only / `public-url-needed`; no compliance claim | pass | `doctor`; manual boundary read | Promote URLs when verified |

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
| Card parity | `python tools/ng.py gen-commands --check` | local py3.x | `OK: every command card matches its skill.` | console |
| Token budget | `python tools/ng.py tokens .` | local | `OK: token budget` | console |
| Repo health | `python tools/ng.py doctor .` | local | `OK: Nuclear-grade doctor` | console |
| Full suite | `python -m pytest -q` | local | `190 passed, 1 skipped` | console |
| Lint | `python -m ruff check .` | local | `All checks passed!` | console |
| Packet validation | `python tools/ng.py validate .nuclear/changes/graded-approach-sharpening` | local | required files present; no placeholder; links resolve; statuses set | console |
| Description bound | `len(description)` check | local | 453 chars, no colon-space | console |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Floor used to skip a trust-bearing change | Read tripwire list + extended rationalization ("It is administrative, so the floor covers it") | Loophole closed; "when in doubt it is Quick" | `rating-change-risk` Common Rationalizations |
| Description breaches contract | Measured length + colon-space scan | 453 chars, no `": "` | console |
| Identical prose pasted into many files | Token redundancy gate | Largest repeated block 4 files (< 8) | `tokens` output |
| Implied compliance with a regulator | Boundary read of new source rows | Concept-only; catch-all disclaimer covers IAEA/CNSC/ONR | `source-map.md`, `compliance-boundaries.md` |

## AI-assisted work checks

Use if AI did real work here or had power over tools.

- AI scope: drafted all doc/skill/packet edits under the user-approved plan; the human approves via PR.
- Model/tool used: Claude Code agent; repo CLI (`ng gen-commands`, `tokens`, `doctor`, `validate`), pytest, ruff.
- Permissions/actions allowed: edit repo files on the feature branch; run read-only checks and tests; no production/credential/network authority.
- Independent checks performed: deterministic contract/parity/public-docs tests the agent cannot satisfy by editing the doctrine alone; PR review pending.
- Self-check / turnover records: the promise-boundary self-check in `plan.md`; no turnover (same owner).
- Hallucination/slop screening: every cross-jurisdiction source marked `public-url-needed` because URLs could not be verified from this environment.
- Human approval gates exercised: AskUserQuestion resolved scope, the floor's record model, and the source policy before edits.

## Security / dependency / supply-chain checks

Not activated — no dependency, build, or security-relevant change.

- Dependency review: n/a
- SBOM/provenance/build evidence: n/a
- Vulnerability/security review: n/a
- Revalidation trigger: n/a

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: local `pytest`/`ruff`/`doctor`/`tokens` output above; CI will re-run on the PR
- Implementation diff / PR: forthcoming draft PR on `claude/zealous-sagan-g9sfn0`

## Exit criteria

- Each important claim has a status.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade verification record inspired by public sources on software V&V, test documentation, secure development, and software assurance, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
