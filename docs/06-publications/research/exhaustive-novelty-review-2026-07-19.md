# Exhaustive Novelty and Competitiveness Review

**Manuscript:** *From Context to Accountable Acceptance* v0.2
**Date:** 2026-07-19
**Decision standard:** Publishable novelty, not patent novelty or proof of priority

## Executive verdict

### Is the current paper novel?

**Narrowly, yes. Broadly, no.**

The paper is not novel as a lifecycle, governance method, evidence packet, controlled review workflow, claim--evidence record, consequence-graded approval system, provenance mechanism, or separation between a proposed action and authorization to execute it. Those areas are occupied by configuration management, IV&V, professional self-review doctrine, assurance cases, software delegation contracts, artifact-gate research, runtime agent governance, supply-chain attestations, and industrial platforms such as Palantir.

The defensible residual is:

> AI-assisted software acceptance should explicitly model **who controlled the generation, selection, transformation, and presentation of decisive evidence**, because a protected gate can remain epistemically coupled to the actor whose change it evaluates.

The manuscript's strongest original-looking abstraction is not the lifecycle and not verdict/apply-clearance. It is the combination of:

1. **evidence self-authorship** as an agent-specific form of self-review and correlated-error risk;
2. a multidimensional **actor--evidence coupling profile** spanning actor, context, mechanism, authority, and resource;
3. consequence-dependent requirements on that coupling; and
4. a testable prediction about reviewer defect detection under separated versus actor-controlled evidence.

This is enough for an arXiv discussion preprint, a position paper, an artifact paper, or a practice-oriented venue. It is not yet enough for a strong empirical software-engineering main track.

### Is it competitive with Palantir?

Not as a platform. Palantir's Ontology, Foundry, and AIP already provide a much broader operational layer connecting semantic objects, actions, permissions, branch proposals, review policies, scenarios, transactionally applied actions, action logs, context, tools, and complete agent traces.

The manuscript can compete on a narrower open abstraction that Palantir's public documentation does not foreground: **evidence custody and actor--evidence coupling at the software-acceptance boundary**.

## Review method

The protocol is recorded in `exhaustive-review-protocol-2026-07-19.md`.

### Discovery sources

- OpenAlex
- Crossref
- DBLP
- arXiv API
- Semantic Scholar where the public API did not rate-limit
- official NIST, NASA, NRC, DOE, IESBA, GitHub, Palantir, in-toto, SLSA, OPA, and Cedar sources
- direct Crossref/arXiv metadata for close 2026 work
- citation/reference snowballing where fresh records exposed usable references

### Search coverage

- 18 broad concept queries across bibliographic APIs
- 10 targeted arXiv governance, coding-agent, context, provenance, verifier, reward-hacking, and assurance queries
- 8 targeted arXiv self-evaluation and self-preference queries
- focused follow-up searches for artifact gates, acceptance evidence, decision authority, AI-generated tests, residual risk, evidence custody, actor--evidence coupling, and self-review threats
- deep inspection of Palantir Ontology, action criteria, action logs, proposal review, scenario apply, AIP Chatbot Studio, session logging, and observability

### Screening volume

- 699 deduplicated candidates from the broad bibliographic sweep
- 246 deduplicated candidates from targeted arXiv governance and assurance searches
- 187 deduplicated candidates from self-evaluation and self-preference searches
- **1,087 unique titles** across those datasets after cross-dataset title normalization
- 73 high-relevance records in the first focused shortlist
- additional direct inclusions discovered through exact-title, official-site, and reference-following searches

Raw records are preserved under `docs/06-publications/research/data/`.

### Limits

This is a high-effort structured review, not a formally registered systematic review. Scopus and Web of Science were not directly queried because no licensed API access was available. ACM and IEEE coverage came through Crossref, OpenAlex, DBLP, direct DOI records, and official pages rather than authenticated database interfaces. Google and Bing blocked automated search. The configured Firecrawl search/extract backend had no remaining credit, so primary APIs and direct source retrieval were used.

The field is moving unusually quickly. Several highly relevant works were posted in June and July 2026, days or weeks before this review. Priority should therefore be stated cautiously even after this sweep.

## Most consequential prior-art findings

### 1. Professional self-review threat predates the paper

The International Ethics Standards Board for Accountants defines a self-review threat as arising when a professional evaluates or relies on work previously performed by themselves or their firm.

**Implication:** evidence self-authorship is not a wholly unprecedented epistemic idea. The contribution is its agent-specific formulation and operationalization for AI-assisted software acceptance.

### 2. LLM self-preference provides direct empirical mechanism evidence

Research shows that LLM evaluators can recognize and favor their own generations, that same-family generator/evaluator relationships can leak preferences, and that harmful self-preference persists when models generate incorrect answers.

Important sources include:

- Panickssery, Bowman, and Feng, *LLM Evaluators Recognize and Favor Their Own Generations*;
- Wataoka, Takahashi, and Ri, *Self-Preference Bias in LLM-as-a-Judge*;
- Li et al., *Preference Leakage*; and
- Yang et al., *Quantifying and Mitigating Self-Preference Bias of LLM Judges*.

**Implication:** the manuscript now has empirical lineage for correlated generator/evaluator bias. It should not imply that the general risk of self-evaluation is newly discovered.

### 3. AI-generated tests are already treated as candidate evidence

Pollner's peer/professional T&E article, *Human Oversight for AI-Generated Test Artifacts*, argues that generated tests are not self-validating evidence, identifies false confidence from volume and weak assertions, and proposes risk-scaled independent review before acceptance into an official evidence base.

**Implication:** the manuscript's underlying concern is strongly validated but no longer differentiable merely by saying AI-generated tests require independent acceptance.

### 4. Artifact-aware software-delivery evaluation is occupied

Ravuru's *Artifact Gate Evaluation for AI-Assisted Software Delivery* compares prompt-to-code, spec-driven, and artifact-aware workflows using eight synthetic tasks and deterministic evaluators. It argues that behavior checks and artifact gates expose lifecycle evidence differences that code/lint checks miss.

**Implication:** the manuscript's twelve-scenario comparison, packet/artifact gates, and signal harness are not a novelty anchor.

### 5. Delegation contracts already improve reviewability

*Software Delegation Contracts* uses 64 coding-agent runs and 192 blinded model-based reviews. Contracts and evidence bundles improved reviewability rather than objective correctness, with token and time costs.

**Implication:** reviewability and evidence-bundle benefits already have a stronger empirical anchor than this manuscript's formative inspection.

### 6. Claim--evidence review structures are occupied

*From Traceability to Reviewability* organizes intent, criteria, actions, completion claims, verification evidence, gaps, and rework constraints. Its controlled three-condition study reports improved detection of hidden intent--completion gaps.

Compliance-by-construction argument graphs and assurance-case research already model structured claims, evidence, reasoning constraints, provenance, defeaters, and official decision records.

**Implication:** the acceptance-record schema cannot carry a novelty claim by itself.

### 7. Evidence packages and external verification are occupied

EATF-MultiRoot builds AI-agent evidence packages, a multi-root verifier, reasoned verdicts, offline validation, issuer trust, replay protection, and algorithm-migration cases.

in-toto, SLSA, Sigstore, and GitHub artifact attestations already provide supply-chain provenance, signed claims, and tamper-evident or transparency-log-backed records.

**Implication:** evidence package integrity and provenance are prior art. The manuscript's contribution must concern evidence adequacy and coupling, not merely traceability.

### 8. Runtime authorization is crowded

Runtime Governance for AI Agents, Aegis, AgentBound, OPA, Cedar, Palantir action criteria, and similar systems evaluate identity, context, path, proposed action, delegated authority, constitutions/contracts, or policy before execution.

**Implication:** apply-clearance is useful vocabulary but not a standalone contribution.

### 9. Decision assurance directly links evidence to authority

Kawas's *Decision Assurance for AI-Enabled Mission Systems: From Test Evidence to Operational Authority* links evidence to confidence, decision rights, authority boundaries, and continuous reassessment.

**Implication:** verdict/apply-clearance and revalidation must be presented as an adaptation inside this pattern, not as a new decision theory.

### 10. Palantir demonstrates the larger operational architecture

Palantir publicly documents:

- semantic and kinetic Ontology elements;
- governed actions and submission criteria;
- action logs recording user, time, version, context, and edited objects;
- branch proposals with previews, reviewers, approvals, changelogs, and merge;
- scenarios that remain hypothetical until actions are applied transactionally under validation and permissions; and
- AIP traces containing agent version, prompts, retrieved contexts, variables, tools, results, outputs, and errors.

**Implication:** an operational ontology connecting state, actions, decisions, permissions, and traceability is not new. An open acceptance model must differentiate itself through evidence coupling.

## Contribution ledger

| Claimed element | Novelty after review | Publishable role | Required reframing |
|---|---|---|---|
| Context for accountable acceptance | Low-to-moderate framing novelty | Useful problem boundary | Credit delegation contracts, reviewability, decision assurance, Palantir, and assurance cases |
| Evidence self-authorship | Moderate agent-specific novelty; underlying self-review and self-preference are prior art | Principal conceptual hook | Call it an agent-specific synthesis and prediction, not a first discovery |
| Actor--evidence independence profile | Moderate operational novelty | Strongest design contribution | Present as a coupling diagnostic grounded in IV&V, professional independence, common-mode failure, and generator/judge bias |
| Consequence-dependent minimum profile | Low component novelty; useful composition | Part of design method | Do not claim novelty for risk tiers or proportional oversight |
| Verdict versus apply-clearance | Low novelty | Supporting design primitive | Demote from contribution; cite Decision Assurance, runtime governance, and Palantir scenarios |
| Acceptance-record schema | Low novelty | Reproducibility mechanism | Explicitly derive from assurance cases, delegation contracts, claim review, provenance, and CM |
| Git-native packet and lifecycle | Low conceptual novelty; moderate artifact value | Reference implementation | Compete on openness, simplicity, and executability, not conceptual priority |
| Formative twelve-scenario evaluation | Low evidence strength and no novelty | Design history only | Keep in repository or appendix; do not use as the empirical center |
| Falsifiable evidence-separation prediction | Moderate value | Research agenda and bridge to empirical paper | Make the future study the main next contribution |

## Overall competitiveness

### Current v0.2

- **arXiv discussion preprint:** publishable after the new prior art is added and claims are narrowed.
- **Position/workshop paper:** competitive if centered tightly on actor--evidence coupling.
- **Practice-oriented publication:** competitive because the implementation is real and the professional lineage is credible.
- **Artifact track:** potentially competitive if installation, replication, and demonstrations are polished.
- **ICSE/FSE/ASE main research track:** not competitive yet; insufficient independent empirical evidence and too much adjacent conceptual overlap.
- **ICSE SEIP or IEEE Software:** plausible after adding external deployment evidence or a credible practitioner case study.
- **CHASE/HCI-oriented venue:** plausible after a blinded human-review study.

### Novelty rating

- Broad method novelty: **low**
- Problem-framing novelty: **moderate**
- Actor--evidence coupling model: **moderate and defensible**
- Implementation novelty: **moderate as an open artifact**
- Empirical contribution: **currently weak**
- Overall publishability: **yes, with narrow claims**
- Overall high-prestige competitiveness today: **no**

## Recommended intellectual center

The next manuscript should make one claim:

> Provenance and gate protection are insufficient when the change actor controls the evidence path. Acceptance should therefore model actor--evidence coupling and impose consequence-dependent independence constraints on decisive evidence.

Everything else should support that statement.

### Recommended title

> **Who Authored the Evidence? Actor--Evidence Coupling in AI-Assisted Software Acceptance**

Alternative, more systems-oriented:

> **Evidence Custody in AI-Assisted Software Acceptance: A Git-Native Model of Actor--Evidence Coupling**

### Recommended contribution structure

1. **Problem formulation:** evidence self-authorship as an agent-specific self-review and common-mode failure.
2. **Coupling model:** actor, context, mechanism, authority, and resource dimensions, with explicit non-ordinal profiles.
3. **Acceptance constraint:** consequence-dependent admissibility rules for decisive evidence.
4. **Open reference implementation:** Git-native representation and checks.
5. **Empirical protocol:** preregistered study of detection, calibration, cost, and failure modes.

Verdict/apply-clearance, lifecycle stages, packet names, baselines, and revalidation should be implementation primitives, not headline contributions.

## Palantir-inspired opportunity

The useful lesson from Palantir is not to imitate its ontology vocabulary. It is to turn static documents into an operational model with typed entities, relationships, actions, and enforceable transitions.

A future **acceptance ontology** could define:

### Entities

- candidate change;
- claim;
- evidence item;
- evidence producer;
- verifier;
- mechanism;
- context source;
- controlled resource;
- authority;
- verdict;
- apply clearance;
- accepted baseline; and
- revalidation trigger.

### Relationships

- authored;
- selected;
- transformed;
- executed;
- witnessed;
- controls;
- shares context with;
- shares model family with;
- funds or allocates resources to;
- verifies;
- accepts;
- authorizes application; and
- invalidates.

### Enforceable invariants

- every decisive claim has admitted evidence;
- admitted evidence carries provenance and custody information;
- consequence class determines prohibited coupling paths;
- verdict authority and apply authority are explicit;
- an expired or invalidated evidence item cannot support current reliance;
- revalidation triggers move a baseline out of relied-upon status; and
- logs and signatures establish linkage, not truth.

This would be a valuable systems implementation. It would not be novel merely because it is an ontology; its novelty would depend on the evidence-coupling semantics and enforcement rules.

## What would make the research ten times stronger

### 1. Run the external blinded study

Use seeded plausible defects and at least three conditions:

1. ordinary issue/prompt workflow;
2. contract or artifact-bundle workflow with actor-authored evidence; and
3. matched workflow with independently produced or independently witnessed decisive evidence.

Measure:

- defect and omission detection;
- false acceptance;
- reviewer confidence calibration;
- evidence sufficiency;
- decision time;
- reviewer disagreement;
- cost; and
- which independence dimensions drive any effect.

This isolates the manuscript's claim from the already-demonstrated reviewability benefit of contracts and artifact bundles.

### 2. Implement custody, not just provenance

Represent who generated, selected, transformed, and presented each evidence item, plus shared model, prompt, context, toolchain, authority, and resource dependencies. A hash says what bytes existed; custody describes who controlled the epistemic path.

### 3. Prove the implementation enforces the model

Add machine-checkable invariants, negative fixtures, replay tests, and examples where nominally separate agents fail because they share model/context/resource dependencies.

### 4. Obtain outside scholarly review

Seek at least one reviewer from each of:

- empirical software engineering;
- software/system assurance or IV&V;
- human factors/automation bias; and
- agent governance or AI evaluation.

### 5. Publish the negative cases

Show when independence adds cost without changing a decision, when deterministic tools outperform extra agents, and when separated agents remain too correlated to help.

## Final decision

**Do not abandon the paper. Narrow it.**

The exhaustive review does not show that the work is unpublishable. It shows that the original novelty budget was allocated to the wrong places. The lifecycle, packets, risk tiers, claim records, provenance, review gates, and verdict/apply distinction belong to a well-developed surrounding landscape.

The real opportunity is sharper:

> Treat the custody and coupling of acceptance evidence as a first-class property of AI-assisted software change control.

That is novel enough for a serious discussion preprint and a useful open artifact. With a blinded external study showing that coupling predicts missed defects or false acceptance, it could become a strong empirical software-engineering contribution.
