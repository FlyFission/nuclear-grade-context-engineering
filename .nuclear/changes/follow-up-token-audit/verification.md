# Follow-up to Skills Token Audit (post-rename): Verification

**Purpose:** Show that the important claims, controls, and assumptions have evidence that fits the size of the change.

**Activation threshold:** Use for Standard changes, and any Quick change whose proof needs more than one simple check.

**Minimum useful version:** the claims, the methods, the acceptance criteria, the commands/evals/reviews, the results, the evidence links, and the gaps.

**Overhead trap:** Do not treat "tests passed" as proof. The evidence must match the claim, be repeatable enough to review, and carry a status label.

---

## Verification context

- Slug: `follow-up-token-audit`
- Related basis: `basis.md`
- Owner: `@codex[agent]`
- Date: 2026-05-31
- Verification scope: Doc + change-record updates only; confirm deterministic gates/tests remain green and that audit doc numbers match the current measurement.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test | `python tools/ng.py tokens .` | Numbers in `docs/05-reference/skills-token-audit.md` match current output | pass | command output in this record (below) | none |
| REQ-002 | local proof | deterministic test | `python -m pytest -q` | Tests pass | pass | command output in this record (below) | none |
| REQ-003 | local proof | deterministic test | `python -m ruff check .` | Ruff passes | pass | command output in this record (below) | none |
| REQ-004 | local proof | deterministic test | `python tools/ng.py doctor .` | Doctor passes | pass | command output in this record (below) | none |
| REQ-005 | local proof | deterministic test | `python tools/ng.py eval .` | Efficacy harness stays 15/15 | pass | command output in this record (below) | none |
| REQ-006 | local proof | deterministic test | `python tools/ng.py validate .nuclear/changes/follow-up-token-audit` | Packet validates (no placeholders, required sections present) | pass | command output in this record (below) | none |

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
| Lint | `python -m ruff check .` | local | pass | (captured below) |
| Tests | `python -m pytest -q` | local | pass | (captured below) |
| Repo doctor | `python tools/ng.py doctor .` | local | pass | (captured below) |
| Efficacy eval | `python tools/ng.py eval .` | local | pass | (captured below) |
| Token gate | `python tools/ng.py tokens .` | local | pass | (captured below) |
| Packet validation | `python tools/ng.py validate .nuclear/changes/follow-up-token-audit` | local | planned | (captured below) |

## Negative / failure-mode checks

What did you try to break?

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Scope creep to skill edits/merges | Verified `skills/` untouched in the diff | pass | `git diff` |

## AI-assisted work checks

Use if AI did real work here or had power over tools.

- AI scope: updated docs/change record; ran local checks.
- Model/tool used: Codex CLI (GPT-5.2) + local shell tools.
- Permissions/actions allowed: repo-local edits and local command execution; no release actions.
- Independent checks performed: `ruff`, `pytest`, `ng doctor`, `ng eval`, `ng tokens`, `ng validate`.
- Self-check / turnover records: not applicable.
- Hallucination/slop screening: numbers copied only from measured `ng tokens` output.
- Human approval gates exercised: not applicable.

## Security / dependency / supply-chain checks

Use if activated.

- Dependency review: not applicable (no dependency changes).
- SBOM/provenance/build evidence: not applicable.
- Vulnerability/security review: not applicable.
- Revalidation trigger: re-run the proof commands when any affected doc/contract changes.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- Skill token audit doc: `docs/05-reference/skills-token-audit.md`

## Exit criteria

- Each important claim has a status: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software verification and validation (V&V), test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.

---

## Evidence (command output)

Note: outputs are intentionally short; link to CI for full logs when used outside this local run.

### `python -m ruff check .`

```text
All checks passed!
```

### `python -m pytest -q`

```text
........................................... [ 66%]
.....................................                                    [100%]
```

### `python tools/ng.py doctor .`

```text
OK: Nuclear-grade doctor
```

### `python tools/ng.py eval .`

```text
U02 Agent workspace boundary: 5/5 signals [ok]
U04 Public assurance wording: 5/5 signals [ok]
U07 Payment webhook idempotency: 5/5 signals [ok]

Decision-signal coverage: 15/15 across 3 worked example(s).
Coverage means the artifact names the decision element; it is not proof the element is adequately handled, safe, secure, or compliant.
```

### `python tools/ng.py tokens .`

```text
Skill totals: descriptions 2361 tokens (always loaded), bodies 30222 tokens (loaded only when the skill fires).
Commands: 22 cards, 19923 tokens total, largest 1406 (ng-folders.md).
All measured prose: 194596 tokens.

Worked-example cost per decision signal (tokens / signal):
  U02: 182
  U04: 170
  U07: 192

[Assurance disclaimer frequency line omitted here to avoid the verification record changing the count.]

OK: token budget
```

### `python tools/ng.py validate .nuclear/changes/follow-up-token-audit`

```text
OK: .nuclear/changes/follow-up-token-audit
```
