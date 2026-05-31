# Follow-up to Skills Token Audit (post-rename): Ship

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

**Activation threshold:** Use when a Standard change is merged or released, when the release stance changes, or when users, operations, dependencies, security, data, or AI power are affected.

**Minimum useful version:** the evidence status, the leftover risks, the rollback/restore plan, the monitoring, the handoff, the release decision, and the baseline trigger.

**Overhead trap:** Do not treat a green CI run as release readiness. Ship when the evidence matches the claims and the operational controls are ready.

---

## Release identity

- Change slug: `follow-up-token-audit`
- Version / release / baseline: doc-only follow-up; no new baseline required
- PR / commit / artifact: (this branch)
- Owner: `@codex[agent]`
- Date: 2026-05-31
- Intended release window: next doc/maintenance merge window

## Scope and exclusions

- Included: listed below.
  - Update token-audit reference doc with current measured baseline numbers and post-rename skill IDs.
  - Record explicit decisions for overlap clusters and optional prose-cut items.
- Excluded: listed below.
  - Any skill merge, deletion, or skill-body “token cut” work.
  - Any change to the token counter or budgets.
- Known non-goals: listed below.
  - Collapsing the per-file boundary disclaimer family to a single linked source.
  - Relocating `docs/00-standards-foundation/core-source-rationale.md` out of `docs/`.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | mode and scope recorded |
| Basis / requirements / claims | pass | `basis.md` | decisions and constraints recorded |
| Questioning attitude | not applicable | `risk.md` | summary captured in risk |
| Verification | pass | `verification.md` | `ruff`/`pytest`/`ng doctor|eval|tokens|validate` all green |
| Dependency / supply-chain evidence | not applicable | not applicable | no changes |
| AI-assisted work checks | not applicable | not applicable | no tool authority change |
| Review / approval | pass | `verification.md` | peer review optional; doc-only and reversible |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Doc baseline drifts from measured output in the future | confusion / wrong decisions | mitigate | maintainers | re-run `python tools/ng.py tokens .` when audit doc changes |

## Rollback / restore plan

- Rollback method: revert the doc + change record commits.
- Data migration reversal or restore notes: not applicable.
- Feature flag / kill switch: not applicable.
- Owner on call: maintainers
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| `ng tokens` budget gate | `OK: token budget` | maintainers | CI / local | fix regression or raise budgets with rationale |
| Audit doc baseline accuracy | numbers match current `ng tokens` report | maintainers | `docs/05-reference/skills-token-audit.md` | update doc; do not “hand edit” numbers |

## Handoff

- Operator/customer/support notes: not applicable (doc-only change).
- Docs/runbook updated: yes (token audit doc updated).
- Communication needed: optional (notify maintainers that overlap/cut decisions are recorded).
- Turnover record if activated: not applicable.
- Follow-up date: not scheduled; revisit consolidation only if overlap causes measurable confusion or maintenance burden.

## Release decision

- Decision: ship
- Decision maker: maintainers
- Rationale: Doc-only follow-up; bounded by deterministic measurement + existing test suite; does not change skill routing or tool behavior.
- Decision question answered by evidence? yes (see `verification.md`)
- Conditions attached: none
- Decision posture: conservative enough
- Abort or rollback trigger: any unexpected scope creep beyond docs/record; any test/gate failure
- OPEX or post-release learning trigger: if reviewers repeatedly ask “should we merge these skills?” capture the signal and open a scoped consolidation proposal.

## Baseline trigger

- Baseline required? no (no controlled runtime state change).
- Baseline record: not applicable.
- Revalidation trigger: re-run `python tools/ng.py tokens .` if `docs/05-reference/skills-token-audit.md` changes.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- Skill audit doc: `docs/05-reference/skills-token-audit.md`

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

Original Nuclear-grade template inspired by public ideas on keeping the approved version under control (CM), release readiness, secure development, software assurance, supply-chain risk, software lifecycle, and learning from real operation, mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
