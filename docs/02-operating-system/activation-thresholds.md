# Activation Thresholds

**Purpose:** This file says exactly when Nuclear-grade records turn on, what the smallest useful version is, and when to skip them.

**Rule:** Rigor must earn its place. Turn on records by their decision value and the stakes, not by a wish for a tidy, complete binder.

While you explore and build drafts, stay light when you can undo the work. Raise the bar at the acceptance gate, not at every keystroke. That gate is where a draft becomes a claim, a controlled item, a public statement, a release decision, the version everyone agreed is correct (a baseline), or a change to what the agent may do.

---

## The administrative floor (below Quick)

Some changes are so small a packet would cost more than it could ever return. Name that floor instead of leaving it implicit: an **administrative** change carries **no packet -- the commit message is its record**. (The completion standard accepts "the change record or reasoning it used," and `change-control-packets.md` asks for a packet only "where a future review needs more than a commit message.")

A change sits on the floor only when **all** of these hold:

- it is purely administrative -- a typo, a comment, formatting, a dead-link fix, a doc-only version bump;
- it crosses **no new trust boundary**; and
- it is instantly reversible.

**Tripwires -- any one lifts it to Quick or higher.** These are the same traps the router guards in `../../skills/using-nuclear-grade/SKILL.md`: it touches authentication, permissions, secrets, data, a dependency or manifest, a model id, a prompt, agent authority, CI or `.github/`, a release, a baseline, or claim-bearing public wording (a non-claim administrative fix -- a typo or dead-link in public docs -- does not by itself trip this); or a reviewer would need more than the commit message to judge it; or it is not instantly reversible. **When in doubt it is Quick, not the floor** -- the floor never downgrades a change that earns more, and it never waives the always-on Core habits (see `modes.md` and `../../MAXIMS.md`).

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
| Controllability | A human can interrupt or override in time | Delayed feedback; only checkpoint-gated | One-way or auto-committed; no mid-course catch |
| Performance history | Clean recent record | Some past defects or churn here | Live deficiency, recent incident, or recurring escaped defects on this component |

**The front door: the dominant three.** For the ten-second call, weigh only consequence × reversibility × uncertainty; reach for the other five dimensions when one of those three is unclear or the change trips a trap surface. The full eight are for the audit trail, not the spoken classification.

**Multiplicative, not additive.** A high-consequence change that is a one-keystroke revert and a known pattern is not high-rigor work — reversibility and low uncertainty pull it back down. A single "High" does not force escalation; weigh the three together. Reversibility is the axis physical engineering cannot lean on, and it is your main escape from burden — but pair it with detectability, because a failure you cannot see in time is not cheaply reversible.

**Controllability gates placement, not just height.** When an action can be caught and steered as it runs, a watching review suffices; when it commits before results are known (a one-way migration, an auto-merge, an unattended agent action), the pre-action brief and dry run become the gating controls — the after-the-fact review cannot undo it. Score controllability when a human gate is in question; otherwise the dominant three carry the call.

The first eight dimensions are intrinsic to the change. The last is a **modulator**: a component carrying a live deficiency, a recent incident, or recurring escaped defects earns a higher mode than its intrinsic risk alone, because past performance is part of the stakes. Read it from the `deficiency-register.md` and recent OPEX before you settle the mode; this is the operating-experience loop (DOE-HDBK-1028, NASA Lessons Learned) feeding the next decision.

---

## Artifact trigger table

| Trigger | Minimum artifact | Minimum useful version | Exit criteria | Overhead trap |
|---|---|---|---|---|
| Trivial / administrative change (the floor) | none -- the commit message is the record | files changed and the one-line reason, in the commit | No tripwire fires; a reviewer needs nothing beyond the commit. | Spinning up a packet for a typo. |
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
If it is purely administrative, instantly reversible, and crosses no trust boundary → no packet; the commit message is the record (the administrative floor).
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
