# Quick Risk Template

## Selected mode

- **Mode:** Quick
- **Why this mode:** A small, documentation-only clarification to existing trace guidance; no runtime behavior, dependency, permission, release stance, or secret material changes.

**Purpose:** Decide whether a small change can safely stay in Quick mode, and name the proof it needs.

**Activation threshold:** Use for low-stakes changes you can undo and check easily, with no new line of user trust, no dependency trust decision, no effect on security or privacy, no change in release stance, and no change in AI power.

**Minimum useful version:** Fill the short fields below. If any answer feels uncertain, move up to Standard.

**Overhead trap:** Do not write a risk essay for a tiny diff. The goal is to catch hidden reasons to escalate, not to run a full design review.

---

## Change

- Slug: `trace-secret-redaction`
- PR / issue: daily 1% improvement; PR pending
- Owner: FlyFission
- Date: 2026-09-09
- Summary: Require durable agent traces to redact secret and credential values while preserving reviewable field names and results.

## Scope

- Affected files/configs/docs: trace doctrine, trace skill, generated command, execution-trace template, and this Quick packet.
- User-visible behavior changed? yes, trace instructions become explicit; no runtime behavior changes.
- Dependency/model/API/prompt/tool permission changed? the portable trace prompt changes; no model, dependency, API, or permission changes.
- Release or rollback posture changed? no.

## Quick-mode screen

| Question | Answer |
|---|---|
| Consequence if wrong | A trace could still disclose a secret, or over-redaction could hide useful evidence. |
| Reversibility | One focused commit can be reverted. |
| Detectability | Diff review and generated-command parity expose the complete change. |
| Exposure | Public documentation only; no secret values or credential-bearing systems are accessed. |
| Uncertainty | Low: the rule preserves field names/results and routes original values to protected sources. |
| Why Quick is enough | The edit narrows an existing recording instruction and is mechanically checkable. |

## Required proof

- Command/check/eval to run: full pytest and Ruff suites; `python tools/ng.py gen-commands --check .`; `python tools/ng.py doctor .`; `python tools/ng.py tokens .`; Quick packet validation; `git diff --check`.
- Expected result: all checks pass and generated `commands/ng-trace.md` carries the redaction rule.
- Evidence link/location: `proof.md` and the pull-request checks.

## Critical-action self-check

Use only if the Quick change could hit the wrong target.

- Exact target: `docs/daily-1pct-20260909-trace-redaction` from `origin/main`.
- Expected result: only the trace guidance and its Quick record change.
- Stop condition: any runtime behavior, dependency, permission, or unrelated documentation change appears.

## Escalation check

Move up to Standard if any of these are true:

- users, data, security, permissions, operations, or architecture are affected;
- a trust decision about a dependency, model, or API changed;
- a failure could be silent, delayed, costly, or hard to undo;
- the AI had the power to write, run commands, use the network, or approve actions, beyond just drafting;
- the proof will not fit in one small `proof.md`.

## Required links

- Packet: `.nuclear/changes/<slug>/`
- Related PR/issue: PR pending.
- Proof record: `proof.md`
- Relevant source-map/crosswalk if invoked: not invoked; the primary implementation source is recorded in `proof.md`.

## Exit criteria

- The mode is justified as Quick.
- The required proof is named before or during the change.
- No trigger for Standard or Nuclear mode is hidden.

## Source-lineage note

Original Nuclear-grade template inspired by public ideas on matching rigor to stakes, keeping the approved version under control (CM), software assurance, and secure development, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
