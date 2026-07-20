# Exhaustive Novelty and Competitiveness Review Protocol

**Project:** *From Context to Accountable Acceptance*
**Review date:** 2026-07-19
**Purpose:** Determine whether the manuscript contains a defensible publishable contribution, identify the closest prior art and competing systems, and assess whether Palantir’s Ontology/Foundry/AIP architecture weakens, complements, or merely inspires the manuscript.

## Meaning of “exhaustive”

This is a best-effort systematic evidence review, not a legal novelty opinion or a guaranteed complete census. Exhaustiveness means:

1. a preregistered question and search-concept matrix;
2. multiple independent scholarly indexes and direct primary sources;
3. backward/forward citation and related-work chaining where APIs expose it;
4. product, standard, specification, and open-source implementation review in addition to papers;
5. deduplication and documented inclusion/exclusion decisions;
6. contribution-by-contribution overlap analysis rather than title matching;
7. explicit recording of inaccessible databases, paywalls, API failures, and negative searches.

No “first” or universal novelty claim will be made from this review.

## Review questions

- **RQ1:** Has prior work already formulated the specific risk that an AI change actor authors the evidence consumed by its acceptance gates while leaving those gates structurally intact?
- **RQ2:** Has prior work operationalized actor–evidence coupling through independent dimensions comparable to actor, context, mechanism, authority, and resource?
- **RQ3:** Has prior work separated a technical acceptance verdict from present authorization to apply an accepted AI-assisted change?
- **RQ4:** Does any prior method or system combine consequence classification, an acceptance-record schema, evidence-independence requirements, explicit risk disposition, baseline formation, apply-clearance, and revalidation?
- **RQ5:** Does Palantir’s Ontology, Foundry, or AIP publicly implement or claim these same contributions, or is the overlap limited to governed operational data/actions and decision workflows?
- **RQ6:** What publication class is justified: practitioner report, discussion/position preprint, systems/artifact paper, or empirical software-engineering paper?

## Candidate contribution set

1. Context for task performance versus context for accountable acceptance.
2. Self-modification versus evidence self-authorship.
3. Five-axis actor–evidence independence profile.
4. Verdict versus apply-clearance.
5. Consequence-graded acceptance-record pattern.
6. Controlled agent operating envelope as configuration.
7. Git-native reference implementation.
8. End-to-end integration of authority, claims, evidence provenance, decision, baseline, and revalidation.

## Search concept families

### A. AI coding and delegated software work

- `AI coding agent reviewability`
- `coding agent acceptance evidence`
- `software delegation contract`
- `agent-generated code independent review`
- `AI-assisted software assurance`
- `LLM coding agent human oversight`
- `agentic software engineering governance`

### B. Evidence coupling and evaluator control

- `self-generated evidence AI agent`
- `actor authored evidence acceptance gate`
- `evidence self-authorship`
- `solver verifier independence`
- `generator evaluator collusion`
- `evaluator manipulation reward hacking`
- `grader hacking agent`
- `process supervision independent verification`
- `common mode failure multi-agent verification`

### C. Provenance, assurance, and trust

- `AI agent execution provenance evidence tracing`
- `assurance case autonomous agent`
- `claims evidence argument AI software`
- `software supply chain attestation independent builder`
- `trusted control plane provenance`
- `independent verification validation AI systems`

### D. Authority, decisions, and runtime governance

- `AI agent runtime governance policy paths`
- `authorization to deploy versus release decision`
- `AI change approval apply authorization`
- `policy as code agent actions`
- `human approval autonomous agent deployment`
- `separation of duties AI engineering`

### E. Configuration and lifecycle governance

- `AI model configuration management baseline revalidation`
- `agent operating envelope configuration`
- `MLOps model governance change control`
- `AI system continuous assurance revalidation`
- `consequence graded software change control`

### F. Ontology and operational decision systems

- `Palantir Ontology actions approvals provenance`
- `Palantir AIP agent governance`
- `operational ontology decision rights writeback`
- `enterprise ontology action authorization`
- `knowledge graph operational decisions agents`

## Sources and access routes

### Scholarly indexes

- arXiv API and primary abstract/PDF pages
- OpenAlex API
- Crossref API
- Semantic Scholar API, if accessible
- DBLP API for computer-science bibliographic corroboration
- ACM Digital Library and IEEE Xplore landing pages when discoverable and accessible
- USENIX, NIST, NASA, DOE, NRC, and standards-body primary pages

### Systems and implementations

- official product documentation and engineering publications;
- official specifications and standards;
- public repositories and release documentation;
- public patents only when directly relevant to a claimed architecture.

### Palantir scope

- official Palantir documentation for Ontology, Foundry, and AIP;
- official architecture, security, lineage, actions/functions, branching/scenario, workflow, and agent-governance documentation;
- public technical papers, filings, or patents when they describe relevant mechanisms.

## Date and language bounds

- No lower date bound for foundational assurance, configuration-management, ontology, provenance, or human-factors literature.
- Emphasis on 2018–2026 for AI agents, coding agents, MLOps, and runtime governance.
- English-language titles/abstracts/full texts, plus English metadata for non-English work where available.
- Search cutoff: 2026-07-19.

## Inclusion criteria

Include a work or system when it materially addresses at least one candidate contribution and provides enough primary evidence to characterize the overlap. Include older foundational work when it establishes that a supposedly new component is prior art.

## Exclusion criteria

Exclude:

- generic AI ethics or governance with no software/agent acceptance mechanism;
- generic RAG/context optimization without provenance, authority, acceptance, or decision state;
- marketing claims lacking architectural detail, except as evidence of product positioning;
- duplicate versions, retaining the latest primary record and noting published versions;
- commentary that cannot be traced to a primary source;
- works whose only overlap is the word “ontology,” “context,” “evidence,” or “governance.”

## Evidence extraction fields

For each included item:

- exact title, authors/owner, year, type, identifier, and primary URL;
- contribution and implementation claims;
- empirical design and evidence strength;
- overlap with each candidate contribution;
- closest-equivalence judgment: none, vocabulary, component, substantial, or potentially novelty-destroying;
- manuscript action: cite, differentiate, narrow, remove, test, or no change;
- confidence and evidence-access limitation.

## Decision rules

- **Component prior art** does not defeat an original synthesis claim.
- **Novelty-destroying overlap** requires one prior work/system to contain substantially the same claimed formulation or integrated mechanism, not merely adjacent terminology.
- A product’s implementation can constrain novelty even if it lacks an academic paper, but public documentation must support the comparison.
- A testable new label for a known phenomenon is weak novelty unless it changes measurement, design, or decision practice.
- Publication competitiveness depends separately on conceptual differentiation, implementation quality, empirical evidence, and venue fit.

## Planned outputs

1. systematic academic-prior-art review;
2. Palantir competitive analysis;
3. competing-systems/high-assurance matrix;
4. deduplicated candidate-source register and search log;
5. contribution ledger with confidence ratings;
6. blunt competitiveness and publication-class verdict;
7. manuscript changes only where the evidence alters the contribution boundary.
