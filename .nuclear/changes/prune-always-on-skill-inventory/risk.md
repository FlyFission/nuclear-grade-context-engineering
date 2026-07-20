# Quick Risk Record

## Selected mode

- **Mode:** Quick
- **Why this mode:** Documentation-only edit to `AGENTS.md` that removes redundant always-on context; one-line revert, no capability or trust boundary changes.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: prune-always-on-skill-inventory
- PR / issue: #71
- Owner: FlyFission
- Date: 2026-07-20
- Summary: Remove the 17-item "Recommended skills" inventory from the always-loaded `AGENTS.md`. Triggered skill selection already routes through the `CORE.md` decision matrix, and `SKILLS.md` remains the discovery catalog, so every skill stays reachable while agents stop carrying an unnecessary always-on list.

## Scope

- Affected files/configs/docs: `AGENTS.md` (removes the `## Recommended skills` section only; the adjacent `## Skill loading rule` is unchanged).
- User-visible behavior changed? no — no skills, commands, templates, or runtime behavior are removed; the list was a routing aid duplicated by `CORE.md`.
- Dependency/model/API/prompt/tool permission changed? no — no skill or capability is removed; only redundant always-loaded prose is dropped. Agent skill access is unchanged.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | An agent could overlook a skill it should load; mitigated because `CORE.md`'s routing matrix and `SKILLS.md`'s catalog still list every skill. |
| Reversibility | One-line: revert the commit to restore the inventory. |
| Detectability | High: `grep -n "Recommended skills" AGENTS.md` and the public-docs tests confirm the state. |
| Exposure | Low: internal agent-guidance prose; no user data, credentials, or release surface. |
| Uncertainty | Low: the "load by trigger, not by inventory" rule already governs this file and this change makes it executable. |
| Why Quick is enough | Reversible, detectable, docs-only, removes no capability. |

## Required proof

- Command/check/eval to run: `python -m pytest tests/test_public_docs.py tests/test_agents.py -q`, `python tools/ng.py doctor .`, `python tools/ng.py tokens .`, `git diff --check`.
- Expected result: all pass; `CORE.md` and `SKILLS.md` still present and still route to every skill.
- Evidence link/location: `proof.md`.

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: the `## Recommended skills` section of `AGENTS.md`.
- Expected result: only that section is removed; `## Skill loading rule` and all other sections remain.
- Stop condition: any adjacent section or another file changes unexpectedly.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected; — no
- a trust decision about a dependency, model, or API changed; — no
- a failure could be silent, delayed, costly, or hard to undo; — no (one-line revert)
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting; — no
- the proof will not fit in one small `proof.md`. — no

## Required links

- Packet: `.nuclear/changes/prune-always-on-skill-inventory/`
- Related PR/issue: #71
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: n/a (external study cited in the PR description, not adopted as template lineage).

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
