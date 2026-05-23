# Change Control Packets

**Purpose:** Define the core Git-native object of Nuclear-grade:

```text
.nuclear/changes/<slug>/
```

A packet is the bounded evidence context for one change. It lets humans and agents work from design basis, configuration discipline, traceability, verification, and release readiness without reading the whole repo or every source.

---

## Packet principles

1. **One change, one packet.** Keep intent, basis, plan, evidence, and release decision together.
2. **Packets scale by mode.** Quick packets are tiny; Nuclear packets are activated only by consequence.
3. **Links beat duplication.** The packet points to source files, tests, PRs, issues, docs, dashboards, and releases.
4. **Evidence status is explicit.** `pass`, `fail`, `gap`, `deferred`, and `not applicable` are better than silent assumptions.
5. **AI assistance is bounded.** If AI changed code/docs/configs or exercised tools, record scope, authority, and independent checks.

---

## Quick packet

```text
.nuclear/changes/<slug>/
  risk.md
  proof.md
```

Use for low-consequence, reversible, easy-to-verify changes with no new trust boundary.

### Minimum useful version

- `risk.md`: scope, risk, why Quick is enough, proof to run.
- `proof.md`: command/check/eval, result, evidence link, reviewer note.

### Exit criteria

The proof matches the risk; no activated Standard trigger is hidden.

---

## Standard packet

```text
.nuclear/changes/<slug>/
  risk.md
  basis.md
  plan.md
  trace.md
  verification.md
  ship.md
```

Use for meaningful feature/product/configuration changes, user-visible behavior, important dependencies, data handling, permissions, model/prompt/tool behavior, or durable architecture.

### Minimum useful version

- `risk.md`: mode, consequence, reversibility, exposure, uncertainty, activated artifacts.
- `basis.md`: mission, protected outcomes, unacceptable outcomes, assumptions, constraints, evidence required.
- `plan.md`: implementation steps, affected files/assets, dependency decisions, rollback path.
- `trace.md`: important claim → design feature → implementation/evidence link.
- `verification.md`: tests/evals/reviews, acceptance criteria, results, gaps.
- `ship.md`: baseline, residual risk, release decision, rollback, monitoring, handoff.

### Exit criteria

A reviewer can navigate from change intent to evidence and release decision in under a few minutes.

---

## Nuclear packet

```text
.nuclear/changes/<slug>/
  risk.md
  controlled-glossary.md
  design-basis.md
  assumption-register.md
  product-design-description.md
  system-design-description.md
  dependency-trust-basis.md
  change-impact-screen.md
  traceability.md
  verification-ledger.md
  independent-review.md
  release-readiness.md
  handoff.md
  opex.md
```

Do not create this whole folder by default. Activate only the records required by consequence, uncertainty, external trust, irreversible impact, sensitive data, agent authority, or enterprise diligence.

---

## Activation threshold

Create a packet for any non-trivial work where future review needs more than a commit message. Escalate to Standard/Nuclear when the change affects:

- requirements, design basis, architecture, interfaces, or operating assumptions;
- AI tool permissions, prompts, models, context packs, evals, or autonomous authority;
- dependency trust, build provenance, SBOM, supply chain, or vendor/API reliance;
- security, privacy, availability, data integrity, or release posture;
- customer-visible behavior or operational handoff.

---

## Overhead trap

A packet is not a dumping ground. If an artifact is activated, it must answer a decision question. If it only repeats text from another file, replace it with a link and a one-line status.

---

## Required links

Every packet should maintain a top-level summary or equivalent fields in `risk.md`:

```text
change slug
mode
current phase
affected files/assets
activated artifacts
proof commands
release/rollback status
unresolved gaps
next action
```

Source-lineage links go to `../00-standards-foundation/source-map.md` and `../01-field-guide/source-to-concept-crosswalk.md`, not to paywalled/proprietary sources.

---

## Source-lineage note

This packet model is an original Git-native translation of public configuration management, lifecycle, software assurance, secure development, and evidence-record concepts. It is not a substitute for project-specific regulated QA or certification work and makes no compliance claim.
