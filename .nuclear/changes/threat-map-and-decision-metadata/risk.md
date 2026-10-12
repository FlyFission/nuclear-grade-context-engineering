---
status: proposed
date: 2026-10-12
decision-makers: [FlyFission]
consulted:
informed:
---

# Quick Risk Record

## Selected mode

- **Mode:** Quick
- **Why this mode:** Docs and template additions for follow-ups F-06 (docs half), F-08, and F-09. Each is additive and optional, and one commit reverts it. No validator code, dependency, or release-stance change.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: threat-map-and-decision-metadata
- PR / issue: follow-ups F-06, F-08, F-09 in [`../adr-governance-benchmark/basis.md`](../adr-governance-benchmark/basis.md)
- Owner: FlyFission
- Date: 2026-10-12
- Summary: Map OWASP ASI01 to ASI10 onto existing controls, with gaps marked, in `agent-threat-model.md`. Add an optional MADR 4 front matter block to both `risk.md` templates and document it. Add a release-review page. Add two source-map rows.

## Scope

- Affected files/configs/docs: `docs/02-operating-system/agent-threat-model.md`, `docs/02-operating-system/change-control-packets.md`, `docs/05-reference/release-review.md` (new), `docs/05-reference/README.md`, `docs/README.md`, `docs/00-standards-foundation/source-map.md` (two new rows), `templates/quick/risk.md`, `templates/standard/risk.md`, `tests/test_ng_validate.py`.
- User-visible behavior changed? yes, minor: new packets now start with an optional metadata block. `ng validate` gives the same result, and a test pins that.
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A reader could treat the OWASP map as coverage. Mitigated: the map says it is a reading aid, marks gaps, and holds the source at `public-url-needed`. |
| Reversibility | One commit revert. |
| Detectability | High: the diff is small, and a test fails if the template front matter trips the validator. |
| Exposure | Public docs and scaffold templates; no data, credentials, or release surface. |
| Uncertainty | Medium on OWASP names, because the official page could not be fetched. That is recorded as a gap instead of being claimed. |
| Why Quick is enough | Additive, optional, reversible, and checked by existing tests plus one new test. |

## Required proof

- Command/check/eval to run: `python -m pytest -q`, `python -m ruff check .`, `python tools/ng.py doctor .`, `python tools/ng.py tokens .`, `python tools/ng.py validate` on this packet, a fresh `ng new` scaffold in a temp repo compared with a scaffold made from the pre-change templates, and `git diff --check`.
- Expected result: all pass, and fresh scaffolds give the same validator messages as before.
- Evidence link/location: [`proof.md`](proof.md).

## Critical-action self-check

- Exact target: the two `risk.md` templates and the docs listed above.
- Expected result: no validator code changes, and no existing source-map row is edited.
- Stop condition: a validator change turns out to be needed, or a packet that was valid stops validating.

## Escalation check

- users, data, security, permissions, operations, or architecture are affected; — no. Scaffold output gains an optional block, but validation behavior is unchanged.
- a trust decision about a dependency, model, or API changed; — no
- a failure could be silent, delayed, costly, or hard to undo; — no
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting; — yes, it wrote files, ran commands, and used the web, so this trigger is tripped. Quick was kept because the requester set the mode, the work stayed local, and the commit sits on a worktree branch that was not pushed. The maintainer should move this to Standard if they disagree; merge review is the gate.
- the proof will not fit in one small `proof.md`. — no

## Required links

- Packet: `.nuclear/changes/threat-map-and-decision-metadata/`
- Related PR/issue: follow-ups in `../adr-governance-benchmark/basis.md`
- Proof record: [`proof.md`](proof.md)
- Relevant source-map/crosswalk if invoked: [`source-map.md`](../../../docs/00-standards-foundation/source-map.md), Tier 6 (OWASP agentic) and Tier 7 (MADR).

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record. The OWASP and MADR sources are mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
