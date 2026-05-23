# Worked Example Selection

**Purpose:** Choose the first flagship example for proving Nuclear-grade as a practical control system for AI-accelerated software work.

**Selected example:** `ai-agent-tool-permissions` — an AI agent workflow service that may write files, call external APIs, and request human approvals.

**Boundary:** This is a public educational/workflow example. It is not a compliance package, safety case, regulatory submittal, or certification artifact.

---

## 1. Selection decision

The first worked example should be:

```text
AI agent workflow service with file-write permissions, external API calls, approval gates, dependency trust basis, release readiness, and OPEX loop.
```

Why this is the right flagship:

| Criterion | Why this example fits |
|---|---|
| Expresses the thesis | Frontier AI horsepower needs explicit permission boundaries, basis, verification, and release control. |
| Concrete enough | Readers understand file writes, API calls, approvals, tests, logs, and rollback. |
| Consequential enough | Mistakes can leak data, overwrite files, bypass approvals, call the wrong API, or ship unverified agent behavior. |
| Not fake-nuclear | The example uses source-grounded engineering logic without pretending to be nuclear safety software. |
| Exercises the spine | Activates `risk.md`, `basis.md`, `verification.md`, `ship.md`, plus future dependency/AI controls when needed. |
| Teachable in Git | The artifact can live under `.nuclear/changes/add-agent-tool-permissions/` with links to code, tests, logs, and release notes. |

---

## 2. Scenario frame

A product team wants to add controlled tool permissions to an AI workflow service.

The agent may eventually:

- read selected repository files;
- write generated files under an approved workspace path;
- call external APIs for retrieval, tickets, or deployment metadata;
- ask a human to approve risky actions;
- produce audit logs and evidence for reviewers.

The core engineering problem:

> How do we let the agent do useful work without letting it silently exceed its authority?

---

## 3. Activation threshold

Use this as a **Standard-mode worked example** by default.

Escalate portions toward Nuclear-mode records only when the implementation includes one or more of these triggers:

- agent may write outside a sandbox or mutate durable production assets;
- agent may access secrets, customer data, private repositories, or sensitive logs;
- agent may trigger external side effects such as deployments, payments, ticket closure, customer messages, or infrastructure changes;
- failure could be silent, hard to detect, hard to reverse, or externally trusted;
- enterprise diligence requires stronger dependency, provenance, independent review, or release evidence.

Keep Quick mode only for tiny reversible permission-doc edits or non-executable examples.

---

## 4. Minimum useful version

The first public example does **not** need a full application. It needs one navigable packet and one small evidence chain.

Minimum useful version:

```text
.nuclear/changes/add-agent-tool-permissions/
  risk.md          # why Standard mode is activated
  basis.md         # protected outcomes, unacceptable outcomes, assumptions, trust boundaries
  verification.md  # claims, tests/evals/reviews, results/gaps
  ship.md          # release decision, rollback, monitoring, handoff
```

Minimum evidence chain:

| Claim | Basis | Design feature | Evidence | Release signal |
|---|---|---|---|---|
| Agent writes only under approved workspace. | Prevent destructive or unauthorized file mutation. | Path normalization + allowlist + denied-write logging. | Unit tests for traversal/symlink/out-of-scope paths; integration test for allowed path. | Monitor denied writes and approval bypass attempts. |

That one chain is enough to show Nuclear-grade’s value before adding more templates.

---

## 5. Overhead trap

Do not turn the example into a standards essay or a fictional enterprise binder.

Avoid:

- quoting long source passages;
- copying every source-map entry into the example;
- pretending the example proves formal regulatory compliance;
- adding Nuclear-mode artifacts before the thin spine exposes a real need;
- filling trace tables for low-value implementation details;
- letting AI-generated explanations outrun executable proof.

The example should feel like a strong pull request plus durable evidence, not a quality-manual simulation.

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

The blueprint is complete enough for the next build step when a reader can answer:

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

This selection is an original software example inspired by public configuration management, safety-in-design, software assurance, secure development, AI risk, supply-chain, and high-reliability software sources mapped in `../00-standards-foundation/source-map.md` and `../01-field-guide/source-to-concept-crosswalk.md`.

Primary public source families likely to appear in the example lineage:

- DOE-STD-1073-2016 for configuration/change discipline;
- DOE-STD-1189-2016 and DOE-STD-3024-2011 for basis/design maturation and design-description logic;
- NRC public software RG family for lifecycle, V&V, configuration management, requirements, and test documentation concepts;
- NIST SP 800-218, NIST SP 800-161, and NIST AI RMF for secure development, supply-chain risk, and AI risk framing;
- CISA Secure by Design and CISA SBOM guidance for product security and dependency transparency;
- NASA software/systems engineering and lessons-learned sources for lifecycle, assurance, and OPEX;
- SLSA, OpenSSF, and OWASP for practical supply-chain and application-security evidence.

The example does not claim compliance with any of those sources or with DOE, NRC, NASA, NIST, CISA, OpenSSF, OWASP, SLSA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other standard.
