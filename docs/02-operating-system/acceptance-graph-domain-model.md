# Acceptance Graph and Domain Model

**Purpose:** Define the optional operational model that can be derived from Nuclear-grade's existing Git-native records. The graph makes acceptance state, evidence custody, authority, and revalidation queryable without replacing Markdown or Git as the source of truth.

**Status:** Design specification. No database or platform dependency is required.

## Why this exists

The current packet is readable, reviewable, and portable, but its relationships are mostly implicit in links and tables. The expanded novelty review and Palantir comparison suggest a useful next step: preserve the open record format while deriving a machine-queryable model of the acceptance decision.

The value is not "using an ontology." Operational ontologies, knowledge graphs, workflow engines, authorization systems, provenance records, and action logs are established. The useful Nuclear-grade specialization is the evidence-custody and actor–evidence-coupling semantics attached to software acceptance.

## Source-of-truth rule

1. Markdown packet files, protected CI artifacts, attestations, and Git identity remain authoritative records.
2. A graph or index is a **derived projection**. It can be rebuilt and discarded.
3. The projection records source paths and stable identifiers for every node and edge.
4. A query result is not a verdict, clearance, or proof of adequacy.
5. No graph mutation silently changes the accepted baseline or authority record.

## Core entities

| Entity | Identity | Required properties |
|---|---|---|
| CandidateChange | packet slug + candidate digest | scope, repository, candidate revision, consequence class, status |
| Claim | packet + claim ID | statement, load-bearing flag, acceptance criteria, status |
| EvidenceItem | stable artifact ID or digest | type, source URI/path, produced time, environment, raw/derived flag, integrity metadata |
| CustodyEvent | evidence + role + actor + time | role, actor, mechanism, source record, transformation description |
| Actor | stable human/service/agent identity | kind, organization, model/tool identity when relevant, authority reference |
| VerificationMechanism | stable mechanism ID | test/oracle/tool/model/prompt lineage, version, execution path |
| CouplingProfile | claim + candidate + evaluation time | actor, context, mechanism, authority, resource values and basis |
| Verdict | candidate + verdict ID | scope, admitted evidence, decision, owner, conditions, time, expiry/invalidation rule |
| ApplyClearance | candidate + target + clearance ID | authority, target state, approvals, window, policy result, time, expiry |
| Baseline | repository/product + baseline ID | accepted candidate digest, verdict, clearance if applicable, effective time |
| RevalidationTrigger | trigger ID | watched condition, affected records, required response, owner |
| Policy | policy ID + version | consequence scope, minimum coupling profile, required evidence patterns, authority rules |
| TargetState | target ID + observed revision | environment, configuration revision, relevant external-state digest |

## Core relationships

| Relationship | From → To | Meaning |
|---|---|---|
| proposes | CandidateChange → Baseline | candidate intends to replace or extend this accepted state |
| asserts | CandidateChange → Claim | candidate acceptance depends on the claim |
| supports / contradicts | EvidenceItem → Claim | admitted evidentiary relationship, not automatic truth |
| generated / selected / transformed / captured / retained / presented | Actor → EvidenceItem | evidence-custody role |
| usedMechanism | EvidenceItem → VerificationMechanism | production or verification path |
| profiles | CouplingProfile → Claim | coupling assessment for this claim and candidate |
| comparesActor | CouplingProfile → Actor | change actor relative to evidence path |
| admits | Verdict → EvidenceItem | evidence considered by the verdict |
| decides | Actor → Verdict | verdict owner |
| authorizes | Actor or Policy → ApplyClearance | present authority to apply |
| appliesTo | ApplyClearance → CandidateChange / TargetState | exact candidate-target pair authorized now |
| accepts | Baseline → CandidateChange | accepted state transition |
| invalidates | RevalidationTrigger → EvidenceItem / Verdict / ApplyClearance / Baseline | prior reliance is stale when the trigger fires |
| governedBy | CandidateChange / Verdict / ApplyClearance → Policy | policy version used for the decision |

## Coupling profile

Each axis takes one of three values:

```text
coupled < partially separated < separated
```

The five-axis vector is:

```text
(actor, context, mechanism, authority, resource)
```

Profiles form a partial order. Profile A dominates B only when A is at least as separated on every axis and more separated on at least one. Incomparable profiles remain incomparable; the system must not hide the tradeoff in an average.

A policy defines a minimum vector for a named consequence and claim class. The evaluator can report:

- meets minimum;
- dominated by minimum;
- incomparable with minimum and needs human disposition;
- missing axis or basis;
- policy version unavailable or stale.

It must not report "safe," "independent," or "approved" from the vector alone.

## Acceptance invariants

1. Every load-bearing claim has a stable identifier and an explicit status.
2. Every decisive evidence item has custody events for generation, selection, transformation, capture, retention, and presentation, or an explicit `unknown` gap.
3. Every load-bearing claim has all five coupling axes and a written basis.
4. A hash or attestation may establish artifact linkage and integrity; it never sets semantic adequacy, independence, identity, or authorization by itself.
5. A verdict names the exact candidate digest, admitted evidence set, owner, conditions, and invalidation rule.
6. Apply clearance names the exact candidate and target state, current approvals, policy version, time window, and expiry.
7. A verdict cannot be treated as apply clearance.
8. A baseline cannot be formed from a stale verdict or lapsed clearance.
9. A fired revalidation trigger removes affected records from current reliance until rechecked.
10. A policy exception is explicit, owned, time-bounded where possible, and visible as residual risk.
11. Derived graph state always links back to the primary record that asserted it.
12. The change actor cannot silently rewrite protected policy, evidence retention, verdict, clearance, or baseline records.

## Useful queries

The graph should answer narrow operational questions:

- Which load-bearing claims are supported only by actor-generated and actor-selected evidence?
- Which verdicts relied on the same model family, tests, context, and resource owner as the change actor?
- Which profiles are below or incomparable with the current policy minimum?
- Which evidence was transformed or summarized without a retained raw artifact?
- Which accepted baselines rely on expired approvals, changed target state, invalidated dependencies, or stale evidence?
- Who could suppress an adverse verifier result?
- Which claims have provenance but no semantic reviewer or independent reproduction?
- Which apply clearances were issued for a candidate digest other than the one currently targeted?
- Which exceptions recur and indicate normalization of deviance?

## Projection from current files

| Current record | Graph projection |
|---|---|
| `risk.md` | CandidateChange consequence and policy scope |
| `basis.md` | Claims and acceptance criteria |
| `trace.md` | claim-to-implementation and claim-to-evidence edges |
| `verification.md` | EvidenceItems, CustodyEvents, VerificationMechanisms, CouplingProfiles |
| `ship.md` | Verdict, ApplyClearance, residual risks, triggers |
| `templates/cm/baseline.md` | Baseline |
| `templates/cm/variance.md` | policy exception / temporary modification |
| `templates/cm/opex.md` | observed event and learning/correction link |
| protected CI / attestations | EvidenceItems plus integrity and execution metadata |

## Staged implementation

### Stage 0 — domain stabilization

- Keep `CONTEXT.md`, the canonical custody doctrine, templates, glossary, and validator vocabulary aligned.
- Dogfood the profile on worked examples and real packets.
- Collect ambiguous cases before freezing a schema.

### Stage 1 — deterministic local projection

- Parse completed Standard packets into versioned JSON.
- Emit validation messages for missing IDs, broken links, incomplete custody, and stale references.
- Add `ng graph --format json|dot` as a derived view; no database.
- Verify round-trip traceability from every JSON object to file and line.

### Stage 2 — consequence policy

- Add a small YAML policy declaring minimum profiles and required evidence patterns by consequence and claim class.
- Implement partial-order comparison and explicit incomparability.
- Add `ng custody <packet>` and `ng policy-check <packet>` reports.
- Keep human disposition for semantic adequacy and incomparable profiles.

### Stage 3 — optional index and integrations

- Add an optional SQLite index or GraphML export for cross-packet queries.
- Expose read-only MCP queries only after the deterministic CLI has stable semantics.
- Add adapters for protected CI, in-toto/SLSA/Sigstore/GitHub attestations, and append-only evidence retention.
- Keep integration facts separate from claims of independence or adequacy.

### Stage 4 — empirical evaluation

- Use the graph to preregister and analyze coupled versus separated evidence conditions.
- Measure false acceptance, defect detection, reviewer calibration, evidence completeness, disagreement, latency, and cost.
- Publish raw scenarios, rubrics, blinded judgments, analysis code, and negative findings.

## Palantir comparison boundary

Palantir's public Ontology, actions, submission criteria, logs, proposals, scenarios, and AIP observability are broad industrial analogues for governed operational state and action. Nuclear-grade should learn from the operational pattern — state plus semantics plus governed mutation — without claiming platform equivalence or copying product vocabulary.

The differentiator pursued here is narrower and vendor-neutral: represent custody and multidimensional coupling of software-acceptance evidence, tie the admissible profile to consequence, and preserve the separation between evidentiary verdict and current apply authority.

## Exit criteria for implementing the graph

Do not start a database or MCP layer until:

- at least three completed Standard packets use the new custody/profile structure;
- the team can name stable entity IDs and distinguish current state from historical events;
- partial-order policy cases, including incomparable profiles, have tests;
- raw evidence retention and source-link rules are explicit;
- the derived-index rule is enforced;
- the feature answers real review questions that Markdown alone makes expensive.

## Source-lineage note

This design is an original repository-native specialization informed by public work on operational ontologies, assurance cases, provenance, policy enforcement, independent V&V, professional self-review threats, and AI evaluator bias, mapped in `docs/00-standards-foundation/source-map.md`. It does not claim ontology novelty, Palantir equivalence, formal V&V, compliance, safety, security, certification, or regulatory adequacy.
