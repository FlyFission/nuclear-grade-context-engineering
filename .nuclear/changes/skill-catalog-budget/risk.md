# Skill catalog budget boundary

## Selected mode

- **Mode:** Quick
- **Why this mode:** This narrows one false absolute in public authoring guidance; it changes no skill, runtime, dependency, permission, or release stance and is easy to revert.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: `skill-catalog-budget`
- PR / issue: PR to be opened from `docs/daily-1pct-20260729-skill-catalog-budget`
- Owner: FlyFission
- Date: 2026-07-29
- Summary: Replace the repository's cross-host "always loaded" promise with a measured catalog-metadata boundary and make names and description openings carry the routing signal.

## Scope

- Affected files/configs/docs: `INTEGRATIONS.md`, `docs/05-reference/skill-authoring-contract.md`, `docs/05-reference/skills-token-audit.md`, `nuclear_grade/tokens.py`, `nuclear_grade/cli.py`, `tests/test_tokens.py`, and this Quick packet
- User-visible behavior changed? yes; `ng tokens` uses host-neutral labels, with no counting or gate change
- Dependency/model/API/prompt/tool permission changed? no
- Release or rollback posture changed? no

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A skill author may over-optimize names or description openings; no runtime effect. |
| Reversibility | One focused commit with no data or configuration migration. |
| Detectability | CLI regression test, public-doc checks, and direct comparison with the cited host behavior. |
| Exposure | Public authoring guidance only. |
| Uncertainty | Host behavior varies, so the wording says `may` and names Codex only as an example. |
| Why Quick is enough | The change removes a portability overclaim without establishing a new requirement or trust boundary. |

## Required proof

- Command/check/eval to run: full pytest and Ruff; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; strict-custody worked-example validation; packet validation; `git diff --check`
- Expected result: all checks pass and the guidance matches the cited merged Codex changes.
- Evidence link/location: `proof.md`; [Codex #34738](https://github.com/openai/codex/pull/34738); [Codex #34997](https://github.com/openai/codex/pull/34997)

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: not applicable; no critical action beyond the later branch push and PR creation
- Expected result: not applicable
- Stop condition: stop if tests reveal the wording is part of an enforced cross-host contract

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected;
- a trust decision about a dependency, model, or API changed;
- a failure could be silent, delayed, costly, or hard to undo;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting;
- the proof will not fit in one small `proof.md`.

## Required links

- Packet: `.nuclear/changes/skill-catalog-budget/`
- Related PR/issue: PR to be opened
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: `docs/00-standards-foundation/source-map.md` Tier 9 records Codex as a supporting mechanics source

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
