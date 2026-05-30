# Change Control Packets

**Purpose:** This file defines the core Git-based object of Nuclear-grade:

```text
.nuclear/changes/<slug>/
```

A packet is the focused bundle of evidence for one change. It lets people and agents work from the design basis, the controlled versions, the trace from claim to proof, the verification, and the release readiness. They do this without reading the whole repo or every source.

---

## Packet principles

1. **One change, one packet.** Keep the intent, the basis, the plan, the evidence, and the release decision together.
2. **Packets scale by mode.** Quick packets are tiny. Nuclear packets turn on only when the stakes call for them.
3. **Links beat copies.** The packet points to source files, tests, pull requests (PRs), issues, docs, dashboards, and releases.
4. **Say the evidence status out loud.** `pass`, `fail`, `gap`, `deferred`, and `not applicable` beat silent assumptions.
5. **Scope the AI's part.** If AI changed code, docs, or configs, or used tools, record what it touched, what it was allowed to do, and the independent checks.

---

## Quick packet

```text
.nuclear/changes/<slug>/
  risk.md
  proof.md
```

Use this for low-stakes changes that you can undo and check easily, with no new trust boundary.

### Minimum useful version

- `risk.md`: scope, risk, why Quick is enough, proof to run.
- `proof.md`: command, check, or eval, plus the result, an evidence link, and a reviewer note.

### Exit criteria

The proof matches the risk. No hidden trigger forces this up to Standard.

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

Use this for changes that matter: real feature, product, or setup changes, behavior users can see, important dependencies, data handling, permissions, model, prompt, or tool behavior, or long-lived architecture.

### Minimum useful version

- `risk.md`: mode, how bad failure would be (consequence), whether you can undo it (reversibility), exposure, uncertainty, and which records are turned on.
- `basis.md`: mission, outcomes to protect, outcomes you cannot accept, assumptions, limits, evidence required.
- `plan.md`: build steps, affected files and assets, dependency decisions, rollback path.
- `trace.md`: important claim, then the design feature, then the link to the build or the evidence.
- `verification.md`: tests, evals, and reviews, plus acceptance criteria, results, and gaps.
- `ship.md`: baseline, leftover risk, release decision, rollback, monitoring, handoff.

### Exit criteria

A reviewer can move from the change's intent to its evidence and release decision in a few minutes.

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

Do not create this whole folder by default. Turn on only the records the work needs: high stakes, high uncertainty, outside trust, damage you cannot undo, sensitive data, agent authority, or the careful checks a big organization expects.

---

## Activation threshold

Create a packet for any work that matters, where a future review needs more than a commit message. Move up to Standard or Nuclear when the change affects:

- requirements, design basis, architecture, interfaces, or operating assumptions;
- AI tool permissions, prompts, models, context packs, evals, or self-directed authority;
- dependency trust, where a build came from (build provenance), the list of parts in your software (SBOM, software bill of materials), the supply chain, or reliance on a vendor or API;
- security, privacy, uptime (availability), data integrity, or release posture;
- behavior customers can see, or a handoff in real use.

---

## Overhead trap

A packet is not a junk drawer. If a record is turned on, it must answer a decision question. If it only repeats text from another file, replace it with a link and a one-line status.

---

## Required links

Every packet should keep a top-level summary, or the same fields, in `risk.md`:

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

Source-lineage links go to `../00-standards-foundation/source-map.md` and `../01-field-guide/source-to-concept-crosswalk.md`, not to paid or private sources.

---

## Source-lineage note

This packet model is an original Git-based translation of public ideas: keeping the approved version of everything under control, the lifecycle, software assurance, secure development, and evidence records. It does not replace the regulated quality work or certification a specific project may need, and it makes no compliance claim.
