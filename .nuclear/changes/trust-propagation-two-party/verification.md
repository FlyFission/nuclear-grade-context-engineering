# Verification

**Purpose:** Show that the claims and controls have evidence that fits the size of the change.

## Verification context

- Slug: trust-propagation-two-party
- Related basis: `basis.md`
- Owner: Ben Huffer (maintainer)
- Date: 2026-07-17
- Verification scope: The two new modules and their unit tests, plus proof that existing validator behavior is unaffected.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic test | `pytest tests/test_propagation.py` | All-pass promotes; any sub-pass claim taints; acknowledged deferred promotes | pass | `tests/test_propagation.py` | None |
| REQ-002 | local proof | deterministic test | `pytest tests/test_two_party.py` | Self-verified pass claim flagged; distinct parties pass | pass | `tests/test_two_party.py` | None |
| REQ-003 | decision authority | independent verification | Wire checks into `validate_packet` after table normalization | Gates run in the pipeline without false blocks | planned | this PR follow-up | Recorded in Deferred items below |

## Verification type guide

| Type | Use when |
|---|---|
| self-check | the target of a critical action and the expected result matter |
| peer-check | another reviewer should stop a wrong action before it happens |
| concurrent verification | a high-stakes action must be watched as it happens |
| independent verification | the final state must be checked apart from the doer's claim |
| peer review | artifact quality, maintainability, usability, or boundary wording matters |
| deterministic test / eval | there is repeatable evidence of the behavior |

## Evidence independence

| Load-bearing claim | Who authored the evidence (actor / independent verifier / human) | Reproducible by an independent party? (command or artifact) | Independence rung (1-5) | Gap / residual risk if below the stakes |
|---|---|---|---|---|
| REQ-001 | AI actor (Claude), authored the module and its tests | yes: `python -m pytest tests/test_propagation.py` | 3 | Maintainer confirmation pending; carried as residual risk in `ship.md` |
| REQ-002 | AI actor (Claude), authored the module and its tests | yes: `python -m pytest tests/test_two_party.py` | 3 | Maintainer confirmation pending; carried as residual risk in `ship.md` |

- Decider independent of the actor for the ship decision? yes: the maintainer decides the merge.
- Evidence authored only by the actor is labeled a self-check and carried as residual risk in `ship.md`? yes.

## Claim authorship

This table dogfoods REQ-002: it is the proposed schema the two-party gate reads. It honestly records that one identity authored the evidence, so the independent second party for this packet is the maintainer at merge (via review), not a second author here.

| Claim ID | Evidence author | Verified by |
|---|---|---|
| REQ-001 | agent:claude | maintainer-at-merge |
| REQ-002 | agent:claude | maintainer-at-merge |

## Commands, evals, and reviews

| Method | Command / review / eval | Environment | Result | Evidence link |
|---|---|---|---|---|
| Unit tests | `python -m pytest tests/test_propagation.py tests/test_two_party.py -q` | Python 3.12 / local | pass | 13 passed |
| Full suite | `python -m pytest -q` | Python 3.12 / local | pass | Existing suite unaffected |
| Lint | `python -m ruff check nuclear_grade/propagation.py nuclear_grade/two_party.py tests/test_propagation.py tests/test_two_party.py` | Python 3.12 / local | pass | All checks passed |
| Packet validation | `python tools/ng.py validate .nuclear/changes/trust-propagation-two-party` | local | pass | Recorded on the branch |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| A sub-pass claim reads green | Synthetic packet with one `fail` claim | pass: propagation reports taint | `tests/test_propagation.py::test_one_fail_taints_the_packet` |
| A self-verified claim passes silently | Synthetic authorship where author equals verifier | pass: two-party flags it | `tests/test_two_party.py::test_self_verified_claim_blocks` |
| Bare deferred claim slips through | Synthetic deferred claim with no recorded reason | pass: propagation blocks it | `tests/test_propagation.py::test_bare_deferred_blocks_without_recorded_reason` |

## AI-assisted work checks

- AI scope: AI drafted both modules, both test files, and this packet under maintainer direction.
- Model/tool used: Claude Code (Opus) on the configured model.
- Permissions/actions allowed: local file edits, local test and validator execution, and a branch push.
- Independent checks performed: full pytest, ruff, doctor, and packet validation recorded above.
- Self-check / turnover records: turnover captured in the ship.md handoff section.
- Hallucination/slop screening: every evidence row names a command actually run in this session.
- Human approval gates exercised: merge decision remains a maintainer action.

## Security / dependency / supply-chain checks

- Dependency review: not applicable; zero new dependencies (stdlib only).
- SBOM/provenance/build evidence: not applicable; no build artifact produced.
- Vulnerability/security review: not applicable; modules read local Markdown only.
- Revalidation trigger: any future third-party dependency added to the modules.

## Deferred items

- REQ-003 (wire the checks into `validate_packet`): deferred with reason. It depends on normalizing the claim-to-evidence table schema (see the finding below) and on a maintainer decision about gate severity (advisory versus blocking). Tracked for a follow-up packet.

## Findings surfaced while building (for the reviewer)

- Finding 1: running the propagation logic against the real packet `public-v0-launch` flags claim `L-005` (status `planned`, "execute after PR merge") because it is not recorded in a Deferred items section. The current validator passes that packet. Recommendation: treat `planned` like `deferred`, allowed only with a recorded reason.
- Finding 2: the claim-to-evidence table schema varies across existing packets (for example `mission-driven-backbone` places the status in a different column), so a strict parser can miscount. Normalizing the table is a prerequisite before wiring propagation in as a blocking gate.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: this PR's CI run
- Implementation diff / PR: this PR

## Exit criteria

- Each important claim has a status.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade template inspired by public sources on software verification and validation, test documentation, secure development, software assurance, AI risk, and application-security checks, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
