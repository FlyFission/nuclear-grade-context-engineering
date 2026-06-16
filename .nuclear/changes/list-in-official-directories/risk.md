# Quick Risk Record

## Selected mode

- **Mode:** Quick
- **Why this mode:** docs-only, additive, reversible; no code, dependency, security, or release-stance change.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: list-in-official-directories
- PR / issue: PR #42 (branch claude/loving-ride-sgg6ww)
- Owner: FlyFission (Ben Huffer)
- Date: 2026-06-16
- Summary: Add `docs/04-adoption/listing-and-discovery.md` (verified steps to submit to the Claude Code community directory and the openai/skills catalog) and link it from the adoption README and `INTEGRATIONS.md`.

## Scope

- Affected files/configs/docs: `docs/04-adoption/listing-and-discovery.md` (new), `docs/04-adoption/README.md`, `INTEGRATIONS.md`.
- User-visible behavior changed? no; documentation only.
- Dependency/model/API/prompt/tool permission changed? no.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | a doc lists a stale submission step; a reader follows an outdated link |
| Reversibility | high; revert the doc |
| Detectability | high; links and steps are checkable against the linked official sources |
| Exposure | documentation only; no code or runtime surface |
| Uncertainty | low; both directory processes were verified first-hand this session |
| Why Quick is enough | additive docs with no code, dependency, security, or release change |

## Required proof

- Command/check/eval to run: full `pytest`, `ruff check .`, `ng doctor .`, `ng tokens .`, `ng validate` on this packet, and `claude plugin validate .`.
- Expected result: all green; the plugin validates.
- Evidence link/location: `proof.md`.

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: the three documentation files listed under Scope.
- Expected result: only docs change; no code or manifest behavior changes.
- Stop condition: stop if any non-doc file would change.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected;
- a trust decision about a dependency, model, or API changed;
- a failure could be silent, delayed, costly, or hard to undo;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting;
- the proof will not fit in one small `proof.md`.

None apply: this is additive documentation.

## Required links

- Packet: `.nuclear/changes/list-in-official-directories/`
- Related PR/issue: PR #42
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md`

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
