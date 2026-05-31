# Modes

**Purpose:** This file defines Nuclear-grade modes that scale with risk. They let teams apply enough control to matter, without burning tokens or process on low-stakes work.

**Rule:** Start with the smallest mode that can honestly hold on to the design intent, the evidence, the release readiness, and the learning. Move up by stakes, uncertainty, exposure, how hard it is to undo, how much the agent acts on its own, and how much outside trust is on the line.

---

## Mode table

| Mode | Use when | Artifact spine | Exit criteria |
|---|---|---|---|
| Quick | Low stakes, easy to undo, local, easy to spot a failure, no change to a trust boundary. | `risk.md`, `proof.md`. | Reviewer can see the scope, why Quick is enough, and the proof result. |
| Standard | A feature or change that matters; behavior users can see; a dependency that is not trivial; a data, permissions, or setup change; a long-lived design decision. | `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`. | Important claims link to evidence; the release decision is stated out loud. |
| Nuclear | High stakes, high uncertainty, close to regulated work, outside trust, failure that is hard to spot, damage you cannot undo, an agent that acts on its own in a big way, sensitive data, or the careful checks a large organization expects. | Standard plus the turned-on records: design basis, dependency trust, change impact, independent review, release readiness, handoff, and OPEX. | An independent reviewer can trace the path from basis to controls to evidence to release readiness. |
| Incident | A defect that escaped, a security event, a near miss, an eval failure, or a surprise in operation. | An incident or OPEX record, plus proof the bug stays fixed and updates to the basis, tests, or controls. | The lesson changes something lasting, or is closed out on purpose. |
| Research Board | Big-picture uncertainty, a fork in the architecture, doubt about a source, disputed requirements, or a major buy, build, or dependency decision. | A source-map excerpt, an options table, the assumptions, an adversarial review, and a decision record. | The decision is bounded, the parts you can and cannot undo are named, and the next action is chosen. |
| Release | A release changes customer, operational, security, compliance-adjacent, or trust posture. | Release readiness or `ship.md`, the release decision, the baseline trigger, rollback, monitoring, handoff, and a post-release check. | The proceed, block, or defer decision is backed by evidence. |

---

## Activation threshold

Move up one or more modes when any answer is "yes":

- Could this harm users, customers, data, finances, operations, safety, security, reputation, or legal standing?
- Could this give an AI or agent the power to write, run commands, use the network, approve actions, or touch sensitive data?
- Could a failure be hard to spot, reproduce, explain, or undo?
- Does the change add or seriously alter a dependency, model, API, SaaS, or build service?
- Will another team, a customer, an auditor, or a future maintainer rely on the claim?
- Is there real uncertainty, disagreement, or doubt about a source?

---

## Minimum useful version

A mode decision is useful when it has:

```text
selected mode
why lower mode is insufficient or sufficient
activated artifacts
required evidence
review/approval trigger
exit criteria
```

For Quick mode, this can be six bullet points in `risk.md`.

---

## Overhead trap

Do not make "Nuclear" the default you reach for. The strongest Nuclear-grade move is often to refuse needless process and keep just enough evidence for the real risk.

---

## Required links

- Link mode choice to `activation-thresholds.md`.
- Link activated artifacts to `change-control-packets.md`.
- Link source concepts to `../01-field-guide/source-to-concept-crosswalk.md` when source lineage matters.
- Link release decisions to `ship.md` or release-readiness records.

---

## Source-lineage note

This mode system is an original software workflow that scales with risk. It draws on public ideas about matching effort to stakes (the graded approach), the lifecycle, keeping the approved version of everything under control, software assurance, and secure development, all from the main source map. It does not implement or claim formal compliance with any cited source.
