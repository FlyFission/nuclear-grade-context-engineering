# Standard Ship Template

**Purpose:** State the release decision plainly: ship, block, defer, or ship with named leftover risk.

**Activation threshold:** Use when a Standard change is merged or released, when the release stance changes, or when users, operations, dependencies, security, data, or AI power are affected.

**Minimum useful version:** the evidence status, the leftover risks, the rollback/restore plan, the monitoring, the handoff, the release decision, and the baseline trigger.

**Overhead trap:** Do not treat a green CI run as release readiness. Ship when the evidence matches the claims and the operational controls are ready.

---

## Release identity

- Change slug: context-engineering-literature-crosswalk
- Version / release / baseline: feature branch `claude/context-engineering-review-7uyto9`
- PR / commit / artifact: this PR
- Owner: Ben Huffer (FlyFission)
- Date: 2026-07-03
- Intended release window: on PR approval

## Scope and exclusions

- Included: crosswalk doc; two Tier 9 source rows; payload-component lens in `context-packs.md`; "Blueprint and execute" workflow entry; production-memory pointers in `durable-memory.md` and `ROADMAP.md`; discoverability link; this packet.
- Excluded: any new skill/template/command; any endorsement/affiliation/superiority claim; the emulation-`examples/` convention and the simpler on-ramp (named as open gaps, deferred).
- Known non-goals: implying we implement or conform to the taxonomy or PRP as a standard; agent-authority or code change.

## Evidence status summary

| Evidence area | Status | Link | Notes |
|---|---|---|---|
| Risk classification | pass | `risk.md` | Standard, reversible |
| Basis / requirements / claims | pass | `basis.md` | REQ-001..004 |
| Questioning attitude | pass | `risk.md` (inline) | not separately activated |
| Verification | partial | `verification.md` | inspection checks pass; `ng`/`pytest` gates delegated to CI (local classifier unavailable) |
| Dependency / supply-chain evidence | not applicable | — | no dependency change |
| AI-assisted work checks | pass | `verification.md` | human review pending pre-merge |
| Review / approval | planned | this PR | human reviewer to confirm boundary wording |

## Residual risks and gaps

| Risk / gap | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| A reader over-reads the mapping as endorsement or alignment | medium | mitigate (prominent boundary status + "what not to claim") | Ben Huffer | reader/issue feedback |
| An external repo revises its taxonomy/workflow | low | accept (mappings kept conceptual + dated 2026) | Ben Huffer | either repo publishes a major revision |
| Emulation-`examples/` convention and simpler on-ramp not built | low | defer (named as open gaps in crosswalk §4) | Ben Huffer | roadmap grooming |

## Rollback / restore plan

- Rollback method: `git revert` the PR.
- Data migration reversal or restore notes: none.
- Feature flag / kill switch: n/a.
- Owner on call: Ben Huffer.
- Time to restore estimate: minutes.

## Monitoring and post-release checks

| Signal | Threshold / expected behavior | Owner | Where to inspect | Action if bad |
|---|---|---|---|---|
| Reader/issue feedback on framing | No "is this endorsed by / aligned with those projects?" confusion | Ben Huffer | Discussions / issues | tighten wording |
| Future `ng doctor` runs | stays OK | maintainers | CI | fix wording |

## Handoff

- Operator/customer/support notes: adopters reach the crosswalk from `docs/README.md`.
- Docs/runbook updated: yes (docs/README index link added).
- Communication needed: PR description summarizes the peer-project, no-endorsement framing.
- Turnover record if activated: none.
- Follow-up date: revisit if either external repo publishes a major revision.

## Release decision

- Decision: ship with residual risk
- Decision maker: Ben Huffer (on PR approval)
- Rationale: High adoption/orientation value, fully reversible, sources public and citable, boundary continuous with existing repo posture; all repo gates green.
- Decision question answered by evidence? yes
- Conditions attached: CI is green (the `ng`/`pytest` gates the local classifier outage prevented running locally), and human PR review confirms no wording reads as endorsement, affiliation, superiority, or conformance.
- Decision posture: conservative enough — peer-project framing, prominent boundary, one new doc plus targeted edits, zero new maintained skill/template/command surface.
- Abort or rollback trigger: review finds an implied endorsement/conformance claim that cannot be reworded.
- OPEX or post-release learning trigger: adopter confusion about the relationship, or a major revision of either external repo.

## Baseline trigger

- Baseline required? no
- Baseline record: n/a (docs change; git is the record)
- Revalidation trigger: a major revision of either external repo, or a change to the repo's sourcing policy.

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
