# Worked Example Selection

**Purpose:** Pick the first main example. It should show that Nuclear-grade is a practical way to control AI-assisted software work.

**Selected example:** `ai-agent-tool-permissions` — an AI agent service that may write files, call outside APIs, and ask people to approve actions.

**Boundary:** This is a public teaching example. It is not a commercial-grade dedication package, a safety case, a regulatory submittal, or a certification artifact, and it does not pretend to be one.

---

## 1. Selection decision

The first worked example should be:

```text
AI agent workflow service with file-write permissions, external API calls, approval gates, dependency trust basis, release readiness, and OPEX loop.
```

Why this is the right pick:

| Criterion | Why this example fits |
|---|---|
| Shows the main idea | Powerful AI needs clear limits on what it may do, a written reason for the design, proof, and control over releases. |
| Concrete enough | Readers already know file writes, API calls, approvals, tests, logs, and undo plans. |
| Serious enough | A mistake can leak data, overwrite files, skip approvals, call the wrong API, or ship agent behavior nobody checked. |
| Not fake-nuclear | The example uses plain, sound engineering. It does not pretend to be nuclear safety software. |
| Uses the core records | It uses `risk.md`, `basis.md`, `verification.md`, and `ship.md`, plus dependency and AI controls later when needed. |
| Easy to teach in Git | The record can live under `.nuclear/changes/add-agent-tool-permissions/` with links to code, tests, logs, and release notes. |

---

## 2. Scenario frame

A product team wants to add controlled tool permissions to an AI workflow service.

In time, the agent may:

- read selected files in the repository;
- write new files only under an approved workspace path;
- call outside APIs to fetch data, file tickets, or read deployment details;
- ask a person to approve risky actions;
- produce audit logs and evidence for reviewers.

The core engineering problem:

> How do we let the agent do useful work without letting it quietly do more than it is allowed to do?

---

## 3. Activation threshold

Treat this as a **Standard-mode worked example** by default.

Raise parts of it toward Nuclear-mode records only when the build hits one or more of these triggers:

- the agent may write outside a safe sandbox or change lasting production assets;
- the agent may reach secrets, customer data, private repositories, or sensitive logs;
- the agent may cause outside effects such as deployments, payments, closing tickets, messages to customers, or infrastructure changes;
- a failure could be quiet, hard to spot, hard to undo, or trusted by people outside the team;
- a careful business review needs stronger proof about dependencies, where code came from, independent review, or the release.

Keep Quick mode only for tiny, easy-to-undo edits to permission docs, or examples that do not run.

---

## 4. Minimum useful version

The first public example does **not** need a full application. It needs one packet a reader can follow and one small chain of evidence.

Minimum useful version:

```text
.nuclear/changes/add-agent-tool-permissions/
  risk.md          # why Standard mode is turned on
  basis.md         # outcomes to protect, outcomes to prevent, assumptions, trust boundaries
  verification.md  # claims, tests/evals/reviews, results/gaps
  ship.md          # release decision, rollback, monitoring, handoff
```

Minimum evidence chain:

| Claim | Basis | Design feature | Evidence | Release signal |
|---|---|---|---|---|
| Agent writes only under approved workspace. | Stop file writes that damage or go where they should not. | Clean up the path, check it against an allowed list, and log every blocked write. | Unit tests for traversal, symlink, and out-of-scope paths; an integration test for an allowed path. | Watch for blocked writes and tries to skip approval. |

That one chain is enough to show why Nuclear-grade is worth it, before you add more templates.

---

## 5. Overhead trap

Do not turn the example into a standards essay or a made-up corporate binder.

Avoid:

- quoting long passages from sources;
- copying every source-map entry into the example;
- pretending the example proves it meets a regulator's rules;
- adding Nuclear-mode records before the small set of core records shows a real need;
- filling trace tables for small implementation details that do not matter;
- letting AI-written explanations run ahead of proof you can actually run.

The example should read like a strong pull request plus lasting evidence, not a pretend quality manual.

---

## 6. Required links

The example should link to:

- `../00-standards-foundation/source-map.md` for public source families;
- `../01-field-guide/source-to-concept-crosswalk.md` for concept lineage;
- `../02-operating-system/change-control-packets.md` for packet shape;
- `../02-operating-system/thin-evidence-spine.md` for minimum records;
- future template files used in the example;
- implementation artifacts, tests, logs, approvals, release notes, and monitoring signals.

---

## 7. Exit criteria for the example blueprint

The blueprint is ready for the next build step when a reader can answer:

1. What changed?
2. Why did this activate Standard mode?
3. What outcomes are protected?
4. What is the agent allowed and forbidden to do?
5. Which important claims have evidence?
6. What remains as an explicit gap?
7. What would block shipment?
8. What would operation teach us after release?

---

## 8. Source-lineage note

This choice is an original software example. It draws on public ideas about keeping the approved version under control (CM), safety built into design, software assurance, secure development, AI risk, supply-chain risk, and high-reliability software. Those sources are mapped in `../00-standards-foundation/source-map.md` and `../01-field-guide/source-to-concept-crosswalk.md`.

Main public source families the example draws from:

- DOE-STD-1073-2016 for keeping changes and versions under control;
- DOE-STD-1189-2016 and DOE-STD-3024-2011 for building up the design basis and writing a design description;
- NRC public software RG family for the software lifecycle, verification and validation (V&V), keeping the approved version under control (CM), requirements, and test documentation;
- NIST SP 800-218, NIST SP 800-161, and NIST AI RMF for secure development, supply-chain risk, and AI risk framing;
- CISA Secure by Design and CISA SBOM guidance for product security and dependency transparency;
- NASA software/systems engineering and lessons-learned sources for lifecycle, assurance, and lessons from real operation (OPEX);
- SLSA, OpenSSF, and OWASP for practical supply-chain and application-security evidence.

The example does not claim compliance with any of those sources or with DOE, NRC, NASA, NIST, CISA, OpenSSF, OWASP, SLSA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other standard.
