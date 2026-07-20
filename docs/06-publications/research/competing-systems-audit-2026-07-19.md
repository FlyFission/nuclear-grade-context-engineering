# Competing Systems and High-Assurance Practice Audit

**Review date:** 2026-07-19
**Target:** *From Context to Accountable Acceptance* v0.2

## Summary

The surrounding control mechanisms are mature. Protected branches, independent assessment, policy-as-code, authorization engines, software-supply-chain attestations, trace logs, assurance cases, and enterprise ontologies all precede this manuscript. None should be presented as novel.

The remaining technical gap is narrower: conventional controls usually ask whether an action, artifact, identity, or provenance statement satisfies policy. They do not necessarily ask whether the actor that produced the candidate state also controlled the decisive evidence and narrative consumed by the acceptance decision.

## Control families

| Control family | Representative primary source | What it establishes | What it does not establish |
|---|---|---|---|
| Protected review workflow | GitHub protected branches and rulesets | Required reviews, status checks, signed commits, merge queues, deployment success, push restrictions, and bypass rules | That tests, summaries, or risk narratives are independent of the change actor |
| Policy as code | Open Policy Agent | Decouples policy decisions from enforcement and evaluates structured input against declarative policy | That structured input is true, complete, or independently produced |
| Authorization language | Cedar | Separates authorization logic and evaluates principal, action, resource, and context | That the evidence motivating an authorized request is adequate |
| Supply-chain step provenance | in-toto | Makes steps, actors, and ordering in a software supply chain transparent | Semantic correctness of claims or independence of evidence generation |
| Software provenance | SLSA | Verifiable information about where, when, and how an artifact was produced | Whether an artifact should be accepted or whether its claims are true |
| Cryptographic artifact attestation | GitHub artifact attestations / Sigstore | Signed provenance claims and, for public repositories, an immutable transparency-log record | Attestation verification alone; GitHub explicitly states that generating attestations alone provides no security benefit unless they are verified |
| Assurance cases | SACM, GSN, safety/ethics assurance research | Structured claim--argument--evidence reasoning and defeater analysis | Automatic protection against an actor generating both a candidate and its supporting argument/evidence |
| Professional independence | IESBA Code | A self-review threat occurs when a professional evaluates or relies on work previously performed by themselves or their firm | Agent-specific implementation or software-change acceptance controls |
| Independent verification and validation | NASA, NRC, NIST assessment guidance | Lifecycle independence, separation of duties, independent evidence, review, and audit | A compact model of hidden coupling between nominally distinct AI agents, prompts, model families, context, and resources |
| Runtime agent governance | Runtime Governance for AI Agents; Aegis; AgentBound | Mediates proposed actions against identity, path, policy, organizational state, delegated authority, constitutions/contracts, or quorum; may generate governance receipts | Acceptance of a new software baseline as a distinct lifecycle decision, though the overlap with apply-clearance is substantial |
| Enterprise operational ontology | Palantir Ontology/AIP | Semantics, governed actions, permissions, proposal review, scenarios, apply rules, action logs, and agent traces | Explicit consequence-scaled evidence-independence requirements |

## Important prior-art findings

### Professional self-review threat is conceptual lineage

The International Ethics Standards Board for Accountants defines a self-review threat as occurring when a professional evaluates or relies on work previously performed by themselves or their firm. Evidence self-authorship is therefore not a wholly unprecedented epistemic idea. Its defensible novelty is the agent-specific formulation and its operationalization for coupled software-change and evidence-production workflows.

Source: https://www.ethicsboard.org/iesba-code

### Gate integrity and input integrity are different

GitHub branch protection, OPA, Cedar, and Palantir submission criteria can prevent unauthorized actions or require checks. They cannot prove that actor-selected tests, summaries, omissions, or risk characterizations are adequate. This supports the manuscript's problem framing but prevents any novelty claim over gates or policy enforcement themselves.

### Provenance and truth are different

in-toto, SLSA, Sigstore, and GitHub attestations provide stronger identity, linkage, origin, build, and tamper-evidence properties. They do not establish semantic correctness, sufficient test coverage, independent reasoning, or acceptance authority. The manuscript correctly treats provenance as one axis rather than as proof.

### Runtime authorization and apply-clearance heavily overlap

Aegis, AgentBound, policy engines, Palantir scenario application, and the ITEA Decision Assurance Framework all separate generated proposals or evidence from execution authority. Verdict/apply-clearance is useful terminology inside the manuscript, but it is not a standalone research novelty.

## AI-specific adjacent systems discovered

| Work/system | Evidence level | Material overlap | Effect on claims |
|---|---|---|---|
| *Artifact Gate Evaluation for AI-Assisted Software Delivery* | Single-author SSRN preprint with eight synthetic tasks and deterministic evaluation | Compares prompt-to-code, spec-driven, and artifact-aware workflows; evaluates lifecycle evidence and artifact gates | Removes novelty from the manuscript's artifact-gate comparison and formative evaluation design |
| *Human Oversight for AI-Generated Test Artifacts* | Professional T&E journal article | AI-generated tests are candidate artifacts, not self-validating evidence; proposes risk-scaled oversight and human acceptance | Strong prior art for the underlying evidence problem; the manuscript's distinction must extend beyond test artifacts |
| *Decision Assurance for AI-Enabled Mission Systems* | Professional T&E journal article | Links evidence to confidence, decision rights, authority boundaries, and continuous reassessment | Verdict/apply-clearance and revalidation are translations, not novel concepts |
| *From Traceability to Reviewability* | SSRN preprint with a controlled three-condition study | Organizes intent, criteria, actions, claims, evidence, gaps, and rework constraints; improves hidden-gap detection | Strong overlap with acceptance records and reviewer-facing claim/evidence organization |
| *Software Delegation Contracts* | Controlled pilot, arXiv preprint | Bounded authority, returned work package, acceptance context, evidence bundles, reviewability | Closest coding-agent empirical precedent |
| EATF-MultiRoot | Reproducible artifact/preprint | AI-agent evidence packages, multiple trust roots, offline verifier, reasoned verdicts | Strong prior art for evidence-package integrity and external verification, not for software acceptance semantics |
| AgentBound | Reference architecture/preprint | Independent authorities, action contracts, signed governance receipts, replay verification | Strong overlap with actor/authority separation and apply governance |
| Aegis | Sandbox evaluation/preprint | Trusted decision layer, server-resolved provenance, fail-closed action control, quorum settlement | Strong overlap with apply control; less overlap with baseline acceptance |
| Compliance-by-Construction Argument Graphs | Conceptual preprint | Claim/evidence formal arguments, validation constraints, provenance ledger | Removes novelty from a generic acceptance graph or claim/evidence ontology |

## Strategic conclusion

The manuscript is not competitive as a broad governance method. The market and literature already contain richer platforms, stronger provenance systems, formal policy engines, assurance-case formalisms, and multiple acceptance-oriented agent workflows.

It can be competitive as a narrower contribution:

1. naming **evidence self-authorship** as an agent-specific form of self-review and correlated-error risk;
2. modeling **actor--evidence coupling** across actor, context, mechanism, authority, and resource dimensions;
3. applying that model to acceptance of AI-assisted software changes; and
4. testing whether evidence separation changes reviewer defect detection and calibration.

The first three are a position/design contribution. The fourth is what would make the work competitive at a strong empirical software-engineering venue.

## Primary sources

- GitHub, "About protected branches," https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub, "Artifact attestations," https://docs.github.com/en/actions/concepts/security/artifact-attestations
- Open Policy Agent, documentation, https://www.openpolicyagent.org/docs/latest/
- Cedar Policy, reference guide, https://docs.cedarpolicy.com/
- in-toto, https://in-toto.io/
- SLSA v1.2, "Provenance," https://slsa.dev/spec/v1.2/provenance
- IESBA, "International Code of Ethics for Professional Accountants," https://www.ethicsboard.org/iesba-code
- Palantir comparison: `palantir-comparison-2026-07-19.md`
