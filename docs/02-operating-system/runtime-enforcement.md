# Runtime Enforcement

**Purpose:** Name a principle Nuclear-grade already practices — that a control should
*act*, not merely advise — and map the contemporary "enforceable AI-governance" concepts
onto the controls in this repo that already provide them. This page adds no new mechanism;
it is an index and a reading lens.

**Boundary:** Original software-workflow translation of public practice. It does not create
assurance, compliance, certification, safety, security, or regulatory adequacy.

---

## The principle

Guidance that lives only in prose is a suggestion. An AI agent — or a hurried human — can
read it, agree with it, and then not do it, and nothing notices. The durable move, visible
across public engineering practice (policy-as-code, branch protection, signed build
provenance, and secure-development guidance mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md)), is
to convert guidance into mechanics that act: checks that fail, gates that block, roles that
cannot approve their own work, and scopes an agent cannot quietly widen.

The test for any control is one question:

```text
can the thing it governs defeat the control by editing it?
```

If yes, it is advice, not enforcement. A check an agent can rewrite sits at a low rung; the
same check run out-of-band in CI — where the agent cannot push — is a real gate. The
enforcement rungs are defined in
[`../04-adoption/agent-authority-model.md`](../04-adoption/agent-authority-model.md).

Push advisory wording up the rungs only when the stakes warrant it. Quick mode stays
advisory on purpose; a reversible, low-blast-radius change does not earn a runtime gate.
Rigor scales with consequence ([`risk-tiers-and-modes.md`](risk-tiers-and-modes.md)).

## Where each control already lives

Read the table as: a contemporary enforcement concept, the Nuclear-grade control that
already provides it, and where that control lives. The point is that the methodology already
covers this ground — this page only makes it legible in one place.

| Enforcement concept | Nuclear-grade control | Where it lives |
|---|---|---|
| Enforcement over documentation | Enforcement rungs; structural validator run by CI | [`agent-authority-model.md`](../04-adoption/agent-authority-model.md), [`validators.md`](validators.md) |
| Role-separated agent work | Plan-phase vs build-phase authority; deciding who decides | [`agent-authority-model.md`](../04-adoption/agent-authority-model.md), [`deciding-who-decides`](../../skills/deciding-who-decides/SKILL.md) |
| No self-approval | Self-modification boundary — a gate the agent can edit is not a gate | [`agent-authority-model.md`](../04-adoption/agent-authority-model.md), [`MAXIMS.md`](../../MAXIMS.md) |
| Bounded change scope / isolation | One change, one packet; the working branch or worktree is the isolation boundary | [`change-control-packets.md`](change-control-packets.md) |
| Zone boundaries for file access | Authority dimensions (which files the agent may touch); workspace-boundary example | [`agent-authority-model.md`](../04-adoption/agent-authority-model.md), [`../03-worked-examples/ai-agent-tool-permissions/`](../03-worked-examples/ai-agent-tool-permissions/) |
| Blast-radius / change budgets | Risk screen plus the change-impact record | [`risk-tiers-and-modes.md`](risk-tiers-and-modes.md), [`../../templates/cm/change-impact.md`](../../templates/cm/change-impact.md) |
| Session hooks and gates | Validator activation thresholds; double-check at cut points | [`validators.md`](validators.md), [`double-checking-before-acting`](../../skills/double-checking-before-acting/SKILL.md) |
| Completion receipt / handoff | Completion standard; the enforced `ship.md` fields; the handoff record | [`../../AGENTS.md`](../../AGENTS.md), [`../../templates/standard/ship.md`](../../templates/standard/ship.md), [`handing-off-work`](../../skills/handing-off-work/SKILL.md) |
| Rising tide / no-new-debt | Recorded baseline; every surprise updates a control | [`configuration-management.md`](configuration-management.md), [`MAXIMS.md`](../../MAXIMS.md) |
| Production-readiness gate | Release-readiness decision; CI passing is not a release decision | [`checking-release-readiness`](../../skills/checking-release-readiness/SKILL.md), [`MAXIMS.md`](../../MAXIMS.md) |
| Session context injection | The context pack / briefing an agent | [`context-packs.md`](context-packs.md), [`briefing-an-agent`](../../skills/briefing-an-agent/SKILL.md) |
| Audit / evidence report | The verification record; the packet summary in `risk.md` | [`change-control-packets.md`](change-control-packets.md), [`../../templates/standard/ship.md`](../../templates/standard/ship.md) |

## What this page is not

It is not a new standard, a benchmark, a maturity model, or a compliance source, and it adds
no gate of its own. Where a control here is only advisory and the stakes have risen, the fix
is to move that control up a rung in the file that owns it — not to add ceremony in this one.

## Source-lineage note

Original Nuclear-grade synthesis. It reads public practice on enforceable engineering
controls — secure-development guidance, supply-chain provenance, and configuration
discipline — mapped in
[`../00-standards-foundation/source-map.md`](../00-standards-foundation/source-map.md). It
does not create assurance, certification, or compliance.
