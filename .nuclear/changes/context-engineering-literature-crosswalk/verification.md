# Standard Verification Template

**Purpose:** Show that the important claims, controls, and assumptions have evidence that fits the size of the change.

**Activation threshold:** Use for Standard changes, and any Quick change whose proof needs more than one simple check.

**Minimum useful version:** the claims, the methods, the acceptance criteria, the commands/evals/reviews, the results, the evidence links, and the gaps.

**Overhead trap:** Do not treat "tests passed" as proof. The evidence must match the claim, be repeatable enough to review, and carry a status label.

---

## Verification context

- Slug: context-engineering-literature-crosswalk
- Related basis: `basis.md`
- Owner: Ben Huffer (FlyFission)
- Date: 2026-07-03
- Verification scope: Boundary discipline (no endorsement/superiority/compliance claim), no skill/command churn, source-map integrity, packet validity, link integrity.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Environment note (evidence honesty)

The local execution environment's command classifier was unavailable during this session, so
`python`-based gates (`ng validate`, `ng doctor`, `ng tokens`, `pytest`) could not be executed
locally. Their authoritative run is delegated to CI on the PR — which is an *independent*
reproduction of the evidence rather than the actor's own local run, consistent with
`docs/02-operating-system/actor-evidence-independence.md`. The inspection-based checks below were
performed with read-only and allowlisted-`git` tooling and are marked `pass`; the tool-run checks
are marked `planned (CI)` until the PR's CI run confirms them.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | deterministic scan | Overclaim scan for endorse/affiliat/superior/implements/conforms outside negative context | All hits in boundary/negative context | pass | overclaim grep of the crosswalk + `WORKFLOWS.md` + `ROADMAP.md` (all hits negative/boundary) | CI `ng doctor` reproduces link/contract gate |
| REQ-002 | local proof | self-check / peer review | Inspect crosswalk, `context-packs.md`, `WORKFLOWS.md` for "not a compliance claim" framing; mappings conceptual only | No claim of implementing/conforming to taxonomy or PRP | pass | Status lines + "what not to claim" section | human PR review |
| REQ-003 | local proof | deterministic test | `git status --short skills/ commands/` | No `skills/` or `commands/` change | pass | `git status` returned empty for both paths | `gen-commands` diff reproduced by review |
| REQ-004 | local proof | self-check | Inspect `source-map.md` Tier 9 for the two verified-public rows | Both rows present with role + boundary notes | pass | `source-map.md` Tier 9 | none |
| Packet + repo gates | local proof | deterministic test | `ng validate`, `ng doctor`, `ng tokens`, `pytest` | All green | planned (CI) | statically traced against the validator/test rules; CI run authoritative | resolve any CI finding before merge |

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
| Overclaim scan | grep endorse/affiliat/superior/implements/conforms outside negative context | repo | pass (all hits negative/boundary) | grep output |
| Skill/command flatness | `git status --short skills/ commands/` | repo | pass (empty) | console |
| Link integrity | resolve every relative link in the crosswalk doc | repo | pass (all resolve) | file check |
| Boundary scan | `python tools/ng.py doctor .` | CI | planned | PR CI |
| Packet validation | `python tools/ng.py validate .nuclear/changes/context-engineering-literature-crosswalk` | CI | planned | PR CI |
| Token budget | `python tools/ng.py tokens .` | CI | planned | PR CI |
| Test suite | `python -m pytest -q` | CI | planned | PR CI |

## Negative / failure-mode checks

What did you try to break?

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Hidden endorsement/superiority claim | grep endorse/affiliat/superior/implements/conforms outside negative context | only negative/boundary hits | overclaim grep |
| Skill description or command churn | `git status` on `skills/` and `commands/` | none | `git status` |
| Broken cross-links | resolve every relative link in new doc | all resolve | file check |
| Unfair representation of a peer project | review each mapping row for "complementary, not superior" framing | framing intact | crosswalk §1, §5 |

## AI-assisted work checks

Use if AI did real work here or had power over tools.

- AI scope: drafted the crosswalk, the source-map rows, the doc fold-ins, and this packet under an approved plan and the user's direction.
- Model/tool used: Claude Code with repo file tools.
- Permissions/actions allowed: edit repo files on the feature branch; run `ng` tooling and read-only scans.
- Independent checks performed: deterministic `ng`/git checks above; human PR review required before merge.
- Self-check / turnover records: self-check folded into this file; no turnover (single session).
- Hallucination/slop screening: external repo summaries taken from live READMEs this session; mappings kept conceptual so a repo revision does not falsify them.
- Human approval gates exercised: plan written and approved; PR review pending before merge.

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
