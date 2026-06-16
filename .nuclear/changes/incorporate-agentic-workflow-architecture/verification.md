# Verification — Incorporate Agentic Workflow Architecture

**Purpose:** Show that each requirement has evidence sized to a reversible documentation change.

---

## Verification context

- Slug: `incorporate-agentic-workflow-architecture`
- Related basis: `basis.md`
- Owner: Maintainer
- Date: 2026-06-16
- Verification scope: structural and boundary evidence for REQ-001..007; no runtime behavior changes.

## Evidence status legend

Use: `pass`, `fail`, `gap`, `deferred`, `not applicable`, `planned`.

## Claim-to-evidence table

| Claim / requirement ID | Support type | Verification type | Verification method | Acceptance criteria | Result status | Evidence link | Gap / follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | local proof | peer review | Read `agents/planner.md` and `templates/standard/plan.md` for selective-section inputs + budget | Both require inputs by `file#section` and a context budget | pass | `agents/planner.md`, `templates/standard/plan.md` | none |
| REQ-002 | local proof | deterministic test | `ng doctor` + file presence | Template exists and is registered | pass | `tools/ng.py doctor .` output `OK` | none |
| REQ-003 | local proof | deterministic test | `test_public_docs.py::test_agentic_workflow_doc_stays_in_boundary` | Boundary phrases only in negative context; disclaimer present | pass | `tests/test_public_docs.py` | none |
| REQ-004 | local proof | peer review | Read glossary + `organizing-project-folders` for one reconciled definition | Minimal and full forms named as one pattern | pass | `docs/glossary.md`, `skills/organizing-project-folders/SKILL.md` | none |
| REQ-005 | local proof | peer review | Read `recording-what-an-agent-did` Process step 7 | Link targets named; link-not-copy stated | pass | `skills/recording-what-an-agent-did/SKILL.md` | none |
| REQ-006 | local proof | deterministic test | `test_command_contracts.py` (set, sections, index, catalog) | Command in set/index/catalog with 10 sections | pass | `tests/test_command_contracts.py` | none |
| REQ-007 | local proof | deterministic test | Full local CI mirror (pytest, ruff, doctor, tokens, validate) | All gates green | pass | command output captured at build time | none |

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
| Test suite | `python -m pytest -q` | Python 3.x + pytest | 143 passed | local run |
| Lint | `python -m ruff check .` | ruff | All checks passed | local run |
| Repo doctor | `python tools/ng.py doctor .` | stdlib | OK | local run |
| Token budget | `python tools/ng.py tokens .` | stdlib | OK: token budget | local run |
| Packet validation | `python tools/ng.py validate .nuclear/changes/incorporate-agentic-workflow-architecture` | stdlib | OK | local run |

## Negative / failure-mode checks

| Failure mode | Check performed | Result | Evidence link |
|---|---|---|---|
| Command added but hardcoded test set not updated | Ran `test_command_contracts.py` | pass (set updated) | `tests/test_command_contracts.py` |
| Doctrine doc introduces an unbounded compliance claim | Ran the boundary test | pass (phrases negative-context only) | `tests/test_public_docs.py` |
| Skill edit breaks the 11-section or token contract | Ran `test_skill_contracts.py` + `ng tokens` | pass | local run |

## AI-assisted work checks

- AI scope: drafted all edits and this packet on the feature branch under the approved plan.
- Model/tool used: `claude-opus-4-8`; file edit and shell tools.
- Permissions/actions allowed: edit repo files, run tests/CLI, git on the feature branch.
- Independent checks performed: the deterministic CI suite plus a human review of boundary wording before merge.
- Self-check / turnover records: not activated (single session, no handoff).
- Hallucination/slop screening: every file path and test reference was read or run, not assumed.
- Human approval gates exercised: plan approved before build; human merge decision pending.

## Security / dependency / supply-chain checks

Not applicable — no new dependency, credential, or network surface is introduced.

## Required links

- `risk.md`
- `basis.md`
- `ship.md`
- CI run / eval report / test logs / review notes: local CI-mirror output at build time
- Implementation diff / PR: this branch's draft PR

## Exit criteria

- Each important claim has a status label.
- Each important claim keeps the support type apart from the verification type.
- Evidence is linked, not pasted in full.
- Gaps are stated plainly and carried into `ship.md`.
- The reviewer can tell whether the evidence backs the release decision.

## Source-lineage note

Original Nuclear-grade change record. The stage-contract pattern adapts the Model Workspace Protocol (arXiv:2603.16021); the rung and determinism framing are original. Lineage is mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
