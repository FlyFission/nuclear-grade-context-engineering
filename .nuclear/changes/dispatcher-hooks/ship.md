# Standard Ship

**Purpose:** State the release decision for the advisory dispatcher hooks.

---

## Release identity

- Change slug: dispatcher-hooks
- Version / release / baseline: advisory SessionStart + UserPromptSubmit hooks (opt-in)
- PR / commit / artifact: this branch's PR
- Owner: FlyFission
- Date: 2026-06-08
- Intended release window: with this PR merge

## Scope and exclusions

- Included: `hooks/session_start.py`, `hooks/user_prompt_submit.py`, `HOOKS.md`, `tests/test_hooks.py`.
- Excluded: any `hooks/hooks.json` (auto-activation), the PreToolUse blocking gate, the enforcement dial.
- Known non-goals: enforcement; auto-activation; any network access.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard justified |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..005 |
| Questioning attitude | pass | `risk.md` | captured inline |
| Verification | pass (live deferred) | `verification.md` | live session deferred |
| Dependency / supply-chain evidence | pass | `verification.md` | pure stdlib, zero network (test-enforced) |
| AI-assisted work checks | pass | `verification.md` | I/O traces to official docs |
| Review / approval | planned | the PR | maintainer review pending |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| No live Claude Code session run | Injection unproven end-to-end | defer | FlyFission | Maintainer enables hooks and starts a session |
| In-session hooks are rungs 1–3 (defeatable) | They are advisory, not a control | accept | FlyFission | The real gate is the rung-4 CI (`ng scaffold-ci`) |
| Manual enable (settings.json) | Friction vs auto-on | accept | FlyFission | A future `ng scaffold-hooks` could automate the opt-in |

## Rollback / restore plan

- Rollback method: delete `hooks/`, `HOOKS.md`, and the test; adopters remove the settings.json entry.
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: the hooks are inert unless wired into settings.json.
- Owner on call: FlyFission
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| First live session with hooks enabled | preamble + reminder appear; no errors | FlyFission | a Claude Code session | fix the hook; patch |
| Over-injection / noise reports | the preamble helps, does not nag | FlyFission | GitHub issues | trim the preamble |

## Handoff

- Operator/customer/support notes: enable per `HOOKS.md`; the hooks are advisory and opt-in.
- Docs/runbook updated: `HOOKS.md`.
- Communication needed: note the opt-in hooks in release notes when cut.
- Turnover record if activated: not activated.
- Follow-up date: when a maintainer runs a live session with hooks enabled.

## Release decision

- Decision: ship with residual risk
- Decision maker: FlyFission
- Rationale: the hooks are advisory, opt-in, pure-stdlib, zero-network, and static-output, all test-enforced; the only unproven step (a live session) is low-risk and reversible.
- Decision question answered by evidence? yes for the static/zero-network/opt-in properties; the live injection is the named residual.
- Conditions attached: maintainer reviews the executable code and runs one live session before announcing.
- Decision posture: conservative enough.
- Abort or rollback trigger: a hook reaching the network or echoing input (would fail CI), or live-session breakage → revert.
- OPEX or post-release learning trigger: any hook issue updates HOOKS.md / the scripts.

## Baseline trigger

- Baseline required? yes
- Baseline record: the two hooks + HOOKS.md become controlled items; the preamble is tied to CORE.md by test.
- Revalidation trigger: a hook I/O schema change, or a CORE.md matrix change.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this branch's PR.
- Monitoring/dashboard/log query: GitHub issues; live-session observation.
- Rollback/runbook: delete `hooks/` + `HOOKS.md`; remove the settings.json entry.

## Exit criteria

- The release decision is stated plainly.
- The slow audit step is done before any baseline or public claim is accepted.
- The baseline trigger is named when the controlled state changes.
- The evidence status and the gaps are visible.
- The leftover uncertainty is bounded and owned, or it blocks or defers the decision.
- A rollback/restore path exists, or its absence is accepted on purpose.
- Monitoring and handoff cover the claims most likely to fail in operation.
- Any accepted leftover risk has an owner and a recheck trigger.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on secure software supply chains, human performance improvement, and release readiness, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
