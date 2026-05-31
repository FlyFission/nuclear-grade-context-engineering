# Activation Thresholds

**Purpose:** This file says exactly when Nuclear-grade records turn on, what the smallest useful version is, and when to skip them.

**Rule:** Rigor must earn its place. Turn on records by their decision value and the stakes, not by a wish for a tidy, complete binder.

While you explore and build drafts, stay light when you can undo the work. Raise the bar at the acceptance gate, not at every keystroke. That gate is where a draft becomes a claim, a controlled item, a public statement, a release decision, the version everyone agreed is correct (a baseline), or a change to what the agent may do.

---

## Primary threshold dimensions

Score this by feel. Do not turn it into a math problem.

| Dimension | Low | Escalating | High |
|---|---|---|---|
| Consequence | Cosmetic/local | User or team impact | Security/safety/privacy/financial/operational/trust impact |
| Reversibility | Easy rollback | Some migration/state risk | Irreversible or expensive to restore |
| Detectability | Obvious failure | Needs targeted tests/monitoring | Silent, delayed, intermittent, or hard to attribute |
| Exposure | Internal/local | Production/customer-visible | External trust, public release, enterprise/government diligence |
| Uncertainty | Known pattern | New integration/assumption | Novel architecture, AI autonomy, disputed basis |
| Dependency trust | No new trust | Package/API/model/config changes | Critical supplier/model/build/data trust decision |
| AI authority | Drafting only | Tool use under supervision | Write/execute/network/approval/data authority |

---

## Artifact trigger table

| Trigger | Minimum artifact | Minimum useful version | Exit criteria | Overhead trap |
|---|---|---|---|---|
| Any non-trivial change | `risk.md` | decision question, scope, consequence, mode, proof needed | Mode is justified. | Writing a risk essay for a tiny diff. |
| Low-risk reversible change | `proof.md` | command/check/eval and result | Evidence matches declared risk. | Treating test output as proof for unrelated claims. |
| User-visible or durable behavior | Standard packet | basis, plan, trace, verification, ship | Important claims have evidence or explicit gaps before acceptance. | Backfilling trace after release. |
| New protected outcome or unacceptable outcome | `basis.md` / `design-basis.md` | what must remain true; assumptions; evidence required | Requirements/design features follow from basis. | Grand narrative without decisions. |
| Important external dependency/model/API/SaaS | dependency trust basis section or record | intended use, consequence, source/version, evidence, revalidation trigger | Trust decision is scoped and revisit-able. | Package-name/version-only review. |
| AI/agent tool authority changes | AI-control fields in packet | authority, permissions, approvals, independent checks | Agent cannot exceed intended envelope without detection/approval. | Letting AI document its own unchecked proof. |
| Security/privacy/auth/data handling change | verification + ship security fields | threat/failure prompt, tests/reviews, rollback/monitoring | Security claim is evidence-backed. | Final scan treated as full assurance. |
| Hard-to-detect or hard-to-reverse failure | Nuclear subset | change-impact, independent review, release readiness | Fresh reviewer can challenge basis and proof. | Creating every Nuclear artifact automatically. |
| Release changes trust/ops/customer posture | `ship.md` / release readiness | baseline, evidence status, risks, rollback, monitoring, handoff | Ship/no-ship is explicit after slow-audit review. | Shipping because CI passed once. |
| Incident/near miss/eval failure | OPEX/corrective action | event, cause, action, verification, basis/test/control update | Lesson changes future behavior or is closed. | Postmortem theater. |

---

## Mode selection shortcut

```text
If it is local, reversible, and obvious → Quick.
If users, dependencies, permissions, data, operations, or architecture care → Standard.
If failure is severe, silent, hard to reverse, externally trusted, or agentic/autonomous → Nuclear subset.
If something already went wrong → Incident.
If the right answer is uncertain → Research Board.
If the release itself changes trust posture → Release.
```

---

## Required links

When a record turns on, it must link to:

- the condition that triggered it;
- the mode you chose;
- the source or basis, if it matters;
- the build work or the configuration item it affects;
- the verification evidence, or the named gap;
- the release, rollback, and monitoring decision, when that applies.

---

## Source-lineage note

This threshold system is an original, software-first model for scaling rigor by stakes. It is inspired by public sources on quality assurance, keeping the approved version of everything under control (configuration management), safety in design, software assurance, secure development, AI risk, and supply chain, all listed in `../00-standards-foundation/source-map.md`. It does not claim compliance with those sources.
