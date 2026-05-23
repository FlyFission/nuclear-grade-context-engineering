# AI Agent Tool Permissions - Worked Example

**Purpose:** Show how Nuclear-grade treats AI-agent permission changes as controlled configuration with basis, impact screening, verification, release readiness, and operating-learning hooks.

**Example status:** Worked example v0. This directory now includes a completed Standard-mode packet at `.nuclear/changes/add-agent-tool-permissions/`, a small reference implementation, and pytest evidence for C-001.

**Boundary:** This example is educational and software-native. It is not a compliance package, regulated safety analysis, formal QA record, or certification claim.

---

## 1. The change

Add a controlled tool-permission layer to an AI workflow service.

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

This change is not “just another feature.” It changes the authority boundary of an AI system.

| Nuclear-grade concept | How it appears here |
|---|---|
| Design basis | Define what must remain true for safe/useful agent operation. |
| Configuration discipline | Treat permissions, prompts, tool registry, credentials, evals, and logs as controlled items. |
| Baseline discipline | Record which permission behavior is accepted and what would require revalidation. |
| Claims-to-evidence traceability | Link each important permission claim to tests, reviews, logs, or explicit gaps. |
| Verification | Prove allowed actions work and forbidden actions fail safely. |
| Release readiness | Ship only when evidence, rollback, monitoring, and handoff are clear. |
| OPEX loop | Denials, near misses, incidents, and user friction update controls and tests. |

---

## 3. Activation threshold

Default mode: **Standard**.

Why Standard is activated:

- user-visible behavior changes;
- the agent gains file-write and API-call authority;
- permissions, credentials, prompts, and tools become configuration items;
- failure can affect data integrity, security, auditability, and user trust;
- verification needs more than one happy-path test.

Escalate to Nuclear-mode extensions if:

- the agent can mutate production infrastructure, regulated records, financial records, customer data, safety-adjacent workflows, or irreversible assets;
- failure is hard to detect or hard to reverse;
- the service is relied on by external customers as a trust boundary;
- independent review, dependency trust basis, or release baseline evidence is required for enterprise diligence.

---

## 4. Minimum useful version

The minimum example should fit on one screen per artifact.

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
| `risk.md` | What authority is changing, what could go wrong, and why Standard mode is enough for the first example? |
| `basis.md` | What outcomes are protected, what outcomes are unacceptable, what assumptions/trust boundaries matter? |
| `verification.md` | Which claims are proven by unit tests, integration tests, evals, review, logs, or explicit gaps? |
| `ship.md` | What is the release baseline, residual risk, rollback plan, monitoring signal, and release decision? |

---

## 5. Example evidence chain

| ID | Claim | Basis | Design feature | Verification evidence | Status |
|---|---|---|---|---|---|
| C-001 | Agent writes only under `./workspace/<change-slug>/`. | Prevent destructive writes outside approved scope. | Normalize path, reject traversal, enforce workspace allowlist, log denials. | Pytest: allowed path, `../` traversal, absolute path, symlink escape; integration-style allowed write appears in workspace. | Pass |
| C-002 | External API calls require approved tool IDs and scoped credentials. | Prevent arbitrary network side effects and credential misuse. | Future tool registry, per-tool scope, no raw URL execution, credential binding. | Future unit tests for unregistered tool denial; integration test with mock API; review of credential scope. | Deferred |
| C-003 | Human approval is required for high-impact actions. | Keep humans in the loop when agent authority crosses consequence threshold. | Future approval policy engine and immutable approval record. | Future scenario eval: blocked without approval, allowed with approval, denied approval remains blocked. | Deferred |
| C-004 | Denied actions are observable. | Silent denial bypass attempts are operational signals. | Structured audit log with event type, tool, actor, path/API, reason, correlation ID. | C-001 denied-write tests assert `write_denied` audit events; broader API/approval audit deferred. | Partial pass |

The initial implementation proves C-001 fully before expanding the example. A narrow complete chain beats a broad fictional matrix.

---

## 6. Required links

The completed example should link to:

- change packet: `.nuclear/changes/add-agent-tool-permissions/`;
- templates used: `templates/standard/risk.md`, `basis.md`, `verification.md`, `ship.md`;
- source lineage: `../../00-standards-foundation/source-map.md` and `../../01-field-guide/source-to-concept-crosswalk.md`;
- operating docs: `../../02-operating-system/change-control-packets.md`, `../../02-operating-system/activation-thresholds.md`, `../../02-operating-system/thin-evidence-spine.md`;
- CM docs: `../../02-operating-system/configuration-management.md`, `../../02-operating-system/controlled-items.md`, `../../02-operating-system/baselines.md`;
- reference code implementing the C-001 path guard;
- implementation artifacts, tests/evals, approvals, release notes, and monitoring signals for C-002/C-003 expansion.

---

## 7. Overhead trap

Keep the example compact.

Do not:

- add a full Nuclear packet before a Standard packet is proven;
- invent a large application just to make the template look complete;
- cite every source in every artifact;
- claim that tests prove broad safety/security properties they do not test;
- turn approval gates into rubber stamps;
- use “compliance” language as proof of engineering quality.

Use evidence status labels instead: `pass`, `fail`, `gap`, `planned`, `deferred`, `not applicable`.

---

## 8. Exit criteria for the worked example v0

The example v0 is complete when:

1. a reader can inspect the packet without reading the whole repo;
2. the selected mode and activation triggers are explicit;
3. C-001 has at least one complete basis → design feature → test/evidence → release signal chain;
4. remaining claims are clearly marked as planned/gap/deferred, not silently assumed;
5. release readiness includes rollback and monitoring;
6. source lineage points to public source families, not proprietary standards;
7. the example contains no formal compliance claim.

---

## 9. Source-lineage note

This example is an original Git-native workflow inspired by public sources already mapped in the Nuclear-grade source foundation:

- DOE-STD-1073-2016: configuration/change discipline;
- DOE-STD-1189-2016 and DOE-STD-3024-2011: design basis and design-description maturation;
- NRC public software regulatory-guide family: lifecycle, V&V, requirements, configuration management, and test documentation concepts;
- NIST SP 800-218: secure software development practices;
- NIST SP 800-161, CISA SBOM, SLSA, and OpenSSF: dependency/supply-chain evidence;
- NIST AI RMF: AI risk and trustworthiness framing;
- CISA Secure by Design and OWASP ASVS/Top 10: secure product and verification prompts;
- NASA software/systems engineering and lessons-learned sources: lifecycle discipline and OPEX loop.

This example does not implement, certify, or claim compliance with DOE, NRC, NASA, NIST, CISA, OpenSSF, OWASP, SLSA, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, or any other standard.

---

## 10. Next expansion paths

1. Add a C-002 evidence chain for approved external API/tool calls.
2. Add a C-003 evidence chain for human approval gates.
3. Add durable audit-log evidence only when the example includes a runtime that needs it.
4. Add activated Nuclear-mode extensions only when an example claim genuinely needs them.
