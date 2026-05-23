# Modes

**Purpose:** Define risk-scaled Nuclear-grade modes so teams apply enough control to matter without burning tokens or process on low-consequence work.

**Rule:** Start with the smallest mode that can honestly preserve design intent, evidence, release readiness, and learning. Escalate by consequence, uncertainty, exposure, irreversibility, autonomy, and external trust.

---

## Mode table

| Mode | Use when | Artifact spine | Exit criteria |
|---|---|---|---|
| Quick | Low consequence, reversible, local, easy to detect, no trust boundary change. | `risk.md`, `proof.md`. | Reviewer can see scope, why Quick is enough, and proof result. |
| Standard | Meaningful feature/change; user-visible behavior; non-trivial dependency; data/permissions/configuration change; durable design decision. | `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md`. | Important claims link to evidence; release decision is explicit. |
| Nuclear | High consequence, high uncertainty, regulated-adjacent, external trust, hard-to-detect failure, irreversible impact, important autonomy, sensitive data, enterprise diligence. | Standard plus activated design-basis, dependency-trust, change-impact, independent-review, release-readiness, handoff, OPEX records. | Independent reviewer can inspect basis → controls → evidence → release/readiness path. |
| Incident | Escaped defect, security event, near miss, eval failure, operational surprise. | incident/OPEX record plus regression proof and basis/test/control updates. | Lesson changes something durable or is explicitly closed. |
| Research Board | Strategic ambiguity, architecture fork, source uncertainty, disputed requirements, major buy/build/dependency decision. | source map excerpt, options matrix, assumptions, adversarial review, decision record. | Decision is bounded, reversible/irreversible parts named, next action selected. |
| Release | A release changes customer, operational, security, compliance-adjacent, or trust posture. | release readiness / `ship.md`, release decision, baseline trigger, rollback, monitoring, handoff, post-release check. | Proceed/block/defer decision is evidence-backed. |

---

## Activation threshold

Escalate one or more modes when any answer is “yes”:

- Could this harm users, customers, data, finances, operations, safety, security, reputation, or legal posture?
- Could this grant AI/agents write, execution, network, approval, or sensitive-data authority?
- Could failure be hard to detect, reproduce, explain, or reverse?
- Does the change add or materially alter a dependency/model/API/SaaS/build service?
- Will another team, customer, auditor, or future maintainer rely on the claim?
- Is there significant uncertainty, disagreement, or source ambiguity?

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

For Quick mode, this can be six bullets in `risk.md`.

---

## Overhead trap

Do not make “Nuclear” the aspirational default. The strongest Nuclear-grade behavior is often refusing unnecessary process and preserving enough evidence for the actual risk.

---

## Required links

- Link mode choice to `activation-thresholds.md`.
- Link activated artifacts to `change-control-packets.md`.
- Link source concepts to `../01-field-guide/source-to-concept-crosswalk.md` when source lineage matters.
- Link release decisions to `ship.md` or release-readiness records.

---

## Source-lineage note

This mode system is an original risk-scaled software workflow inspired by public graded-approach, lifecycle, configuration-management, software assurance, and secure-development concepts from the canonical source map. It does not implement or claim formal compliance with any cited source.
