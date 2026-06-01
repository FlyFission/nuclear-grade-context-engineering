# AI Agent Tool Permissions - Worked Example

**Purpose:** Show how Nuclear-grade handles a change to what an AI agent may do. It treats the change as a controlled setting, with a written reason, a check of what it affects, proof, a release check, and hooks for learning from real operation.

**Example status:** Worked example v0. This directory now includes a finished Standard-mode packet at `.nuclear/changes/add-agent-tool-permissions/`, a small sample build, and pytest proof for C-001.

**For adopters: this packet is your template, not just an illustration.** If your agent has write, run, network, or approval authority over its own working set, see the Agent-authority row in [`../../../CORE.md`](../../../CORE.md)'s decision matrix and start by copying this packet's shape.

**Boundary:** This example is for teaching and is built for software. It is not a compliance package, a regulated safety analysis, a formal QA record, or a certification claim.

---

## 1. The change

Add a controlled set of tool permissions to an AI agent service.

The agent is allowed to:

- read approved project context;
- write files only under an approved workspace path;
- call approved external APIs under scoped credentials;
- request human approval for actions outside normal authority;
- emit audit logs for tool calls, denials, approvals, and release evidence.

The agent is not allowed to:

- write outside the approved workspace;
- follow path traversal, symlink, or environment tricks into protected locations;
- call arbitrary external APIs;
- use credentials outside intended scope;
- bypass approval gates;
- hide or overwrite evidence of denied actions.

---

## 2. Why Nuclear-grade applies

This change is not "just another feature." It changes what an AI system is allowed to do.

| Nuclear-grade concept | How it appears here |
|---|---|
| Design basis | Name what must stay true for the agent to work safely and usefully. |
| Configuration discipline | Treat permissions, prompts, the tool list, credentials, evals, and logs as controlled items. |
| Baseline discipline | Record which permission behavior is accepted, and what would force a re-check. |
| Claims-to-evidence traceability | Link each important permission claim to tests, reviews, logs, or a clearly marked gap. |
| Verification | Prove allowed actions work, and prove forbidden actions fail safely. |
| Release readiness | Ship only when the evidence, the rollback plan, the monitoring, and the handoff are clear. |
| OPEX loop | Denials, near misses, incidents, and user friction (the lessons from real operation, OPEX) feed back into the controls and tests. |

---

## 3. Activation threshold

Default mode: **Standard**.

Why Standard is turned on:

- users see a change in behavior;
- the agent gains the power to write files and call APIs;
- permissions, credentials, prompts, and tools become controlled items;
- a failure can hurt data, security, the audit trail, and user trust;
- proof needs more than one easy "it works" test.

Move up to Nuclear-mode extensions if:

- the agent can change production systems, regulated records, financial records, customer data, work close to safety, or anything you cannot undo;
- a failure is hard to spot or hard to reverse;
- outside customers rely on the service as a line of trust;
- a careful business review needs independent review, a written reason to trust dependencies, or saved release-version evidence.

---

## 4. Minimum useful version

The smallest version should fit on one screen per file.

```text
.nuclear/changes/add-agent-tool-permissions/
  risk.md
  basis.md
  plan.md
  trace.md
  verification.md
  ship.md
  adversarial-review.md
```

Minimum content:

| File | Must answer |
|---|---|
| `risk.md` | What power is changing, what could go wrong, and why is Standard mode enough for the first example? |
| `basis.md` | What outcomes do we protect, what outcomes must never happen, and which assumptions and lines of trust matter? |
| `verification.md` | Which claims are proven by unit tests, integration tests, evals, review, or logs, and which are open gaps? |
| `ship.md` | What is the saved release version, the leftover risk, the rollback plan, the monitoring signal, and the release decision? |

---

## 5. Example evidence chain

| ID | Claim | Basis | Design feature | Verification evidence | Status |
|---|---|---|---|---|---|
| C-001 | Agent writes only under `./workspace/<change-slug>/`. | Prevent destructive writes outside approved scope. | Normalize path, reject traversal, enforce workspace allowlist, log denials. | Pytest: allowed path, `../` traversal, absolute path, symlink escape; integration-style allowed write appears in workspace. | Pass |
| C-002 | External API calls require approved tool IDs and scoped credentials. | Prevent arbitrary network side effects and credential misuse. | Future tool registry, per-tool scope, no raw URL execution, credential binding. | Future unit tests for unregistered tool denial; integration test with mock API; review of credential scope. | Deferred |
| C-003 | Human approval is required for high-impact actions. | Keep humans in the loop when agent authority crosses consequence threshold. | Future approval policy engine and immutable approval record. | Future scenario eval: blocked without approval, allowed with approval, denied approval remains blocked. | Deferred |
| C-004 | Denied actions are observable. | Silent denial bypass attempts are operational signals. | Structured audit log with event type, tool, actor, path/API, reason, correlation ID. | C-001 denied-write tests assert `write_denied` audit events; broader API/approval audit deferred. | Partial pass |

The first build proves C-001 in full before the example grows. One narrow chain that is complete beats a wide table that is made up.

---

## 6. Required links

The finished example should link to:

- change packet: `.nuclear/changes/add-agent-tool-permissions/`;
- templates used: `templates/standard/risk.md`, `basis.md`, `verification.md`, `ship.md`;
- source lineage: `../../00-standards-foundation/source-map.md` and `../../01-field-guide/source-to-concept-crosswalk.md`;
- operating docs: `../../02-operating-system/change-control-packets.md`, `../../02-operating-system/activation-thresholds.md`, `../../02-operating-system/thin-evidence-spine.md`;
- docs on keeping the approved version under control (CM): `../../02-operating-system/configuration-management.md`, `../../02-operating-system/controlled-items.md`, `../../02-operating-system/baselines.md`;
- the sample code that builds the C-001 path guard;
- build files, tests and evals, approvals, release notes, and monitoring signals for the C-002 and C-003 work.

---

## 7. Overhead trap

Keep the example small.

Do not:

- add a full Nuclear packet before a Standard packet is proven;
- invent a big application just to make the template look complete;
- cite every source in every file;
- claim that tests prove broad safety or security that they do not actually test;
- turn approval gates into rubber stamps;
- use "compliance" language as if it proved engineering quality.

Use plain status labels for evidence instead: `pass`, `fail`, `gap`, `planned`, `deferred`, `not applicable`.

---

## 8. Exit criteria for the worked example v0

The example v0 is done when:

1. a reader can study the packet without reading the whole repo;
2. the chosen mode and the triggers that turned it on are stated plainly;
3. C-001 has at least one complete chain: basis → design feature → test/evidence → release signal;
4. the other claims are clearly marked planned, gap, or deferred, not quietly assumed;
5. the release check includes rollback and monitoring;
6. source lineage points to public source families, not private standards;
7. the example makes no formal compliance claim.

---

## 9. Source-lineage note

This example is an original Git-native workflow inspired by public sources already mapped in the Nuclear-grade source foundation:

- DOE-STD-1073-2016: keeping changes and the approved version under control;
- DOE-STD-1189-2016 and DOE-STD-3024-2011: building up the design basis and the design description;
- NRC public software regulatory-guide family: software lifecycle, verification and validation (V&V), requirements, keeping the approved version under control (CM), and test documentation;
- NIST SP 800-218: secure software development;
- NIST SP 800-161, CISA SBOM, SLSA, and OpenSSF: dependency and supply-chain evidence;
- NIST AI RMF: AI risk and trustworthiness framing;
- CISA Secure by Design and OWASP ASVS/Top 10: secure product and verification prompts;
- NASA software/systems engineering and lessons-learned sources: lifecycle discipline and the loop that learns from real operation (OPEX).

This example does not implement, certify, or claim compliance with DOE, NRC, NASA, NIST, CISA, OpenSSF, OWASP, SLSA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other standard.

---

## 10. Next expansion paths

1. Add a C-002 evidence chain for approved external API and tool calls.
2. Add a C-003 evidence chain for human approval gates.
3. Add lasting audit-log evidence only when the example has a runtime that needs it.
4. Turn on Nuclear-mode extensions only when an example claim really needs them.
