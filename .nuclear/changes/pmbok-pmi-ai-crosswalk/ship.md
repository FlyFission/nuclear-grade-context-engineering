# Standard Ship Template

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

**Activation threshold:** Use when a Standard change is merged or released, when the release stance changes, or when users, operations, dependencies, security, data, or AI power are affected.

**Minimum useful version:** the evidence status, the leftover risks, the rollback/restore plan, the monitoring, the handoff, the release decision, and the baseline trigger.

**Overhead trap:** Do not treat a green CI run as release readiness. Ship when the evidence matches the claims and the operational controls are ready.

---

## Release identity

- Change slug: pmbok-pmi-ai-crosswalk
- Version / release / baseline: feature branch `claude/elegant-davinci-h2yoxp`
- PR / commit / artifact: this PR
- Owner: Ben Huffer (FlyFission)
- Date: 2026-06-21
- Intended release window: on PR approval

## Scope and exclusions

- Included: crosswalk doc; source-governance updates; 5 skill body fold-ins; tailoring note; discoverability links; this packet.
- Excluded: any new skill/template; any PMBOK/PMI text; any compliance positioning.
- Known non-goals: PMP/conformance/certification framing; agent-authority or code change.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard, reversible |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..003 |
| Questioning attitude | pass | `risk.md` (inline) | not separately activated |
| Verification | pass | `verification.md` | gates green |
| Dependency / supply-chain evidence | not applicable | — | no dependency change |
| AI-assisted work checks | pass | `verification.md` | human review pending pre-merge |
| Review / approval | planned | this PR | human reviewer to confirm boundary wording |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| A reader still over-reads the rhyme as alignment | medium | mitigate (prominent boundary note + "what not to claim") | Ben Huffer | reader/issue feedback |
| PMBOK editions evolve (a PMBOK 9) | low | accept (mappings kept conceptual + dated 2026) | Ben Huffer | new PMBOK edition |

## Rollback / restore plan

- Rollback method: `git revert` the PR.
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: n/a.
- Owner on call: Ben Huffer.
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Reader/issue feedback on framing | No "is this PMI-compliant?" confusion | Ben Huffer | Discussions / issues | tighten wording |
| Future `ng doctor` runs | stays OK | maintainers | CI | fix wording |

## Handoff

- Operator/customer/support notes: adopters reach the bridge from README and enterprise-rollout.
- Docs/runbook updated: yes (README, enterprise-rollout cross-links).
- Communication needed: PR description summarizes the named-background framing.
- Turnover record if activated: none.
- Follow-up date: revisit on next PMI edition.

## Release decision

- Decision: ship with residual risk
- Decision maker: Ben Huffer (on PR approval)
- Rationale: High adoption value, fully reversible, boundary continuous with existing PMI-excluded policy; all repo gates green.
- Decision question answered by evidence? yes
- Conditions attached: human PR review confirms no wording reads as compliance/conformance.
- Decision posture: conservative enough — named-background only, prominent boundary, zero new maintained surface beyond one doc.
- Abort or rollback trigger: review finds an implied compliance claim that cannot be reworded.
- OPEX or post-release learning trigger: adopter confusion about PMI alignment, or a PMI edition change.

## Baseline trigger

- Baseline required? no
- Baseline record: n/a (docs change; git is the record)
- Revalidation trigger: new PMBOK / PMI AI standard edition.

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- PR/commit/release artifact: this PR
- Monitoring/dashboard/log query: PR review + Discussions
- Rollback/runbook: `git revert`

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
