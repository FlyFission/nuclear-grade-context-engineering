# Adjacent-work verification for academic preprint v0.2

Verified: 2026-07-19
Method: primary-source arXiv API records and official project/specification pages. General web search was unavailable because the configured search backend had exhausted its credits; the arXiv API and direct official URLs remained accessible.

## Closest empirical work

### Software Delegation Contracts

- **Title:** *Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work*
- **Author:** Vincent Schmalbach
- **Identifier:** arXiv:2606.17099v1
- **Published:** 2026-06-14
- **Primary URL:** https://arxiv.org/abs/2606.17099
- **Verified result:** 64 agent executions under three conditions; each reviewed by three independent condition-blinded model-based reviewers, producing 192 reviews. All runs passed hidden acceptance checks. Explicit contracts improved reviewability measures rather than objective task outcomes and increased token and wall-clock cost.
- **Manuscript distinction:** Delegation contracts govern an assigned coding run and its returned work package. The revised manuscript addresses consequence classification, evidence-independence profiles, residual-risk disposition, baseline formation, apply-clearance, and revalidation across the broader acceptance lifecycle.

## Graded oversight

### Governed AI-Assisted Engineering

- **Title:** *Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains*
- **Author:** Richard Kang
- **Identifier:** arXiv:2606.22484v2
- **Published:** 2026-06-21; v2 updated 2026-07-04
- **Primary URL:** https://arxiv.org/abs/2606.22484
- **Verified overlap:** A three-tier oversight model classifies work by regulatory impact, customer proximity, reversibility, and data sensitivity and assigns required evidence artifacts.
- **Manuscript consequence:** The revised paper does not claim novelty for graded oversight tiers.

## Governed context

### ContextNest

- **Title:** *ContextNest: Verifiable Context Governance for Autonomous AI Agent*
- **Authors:** Misha Sulpovar, Benn R. Konsynski, Qaish Kanchwala, Gabe Goodhart
- **Identifier:** arXiv:2607.02116v2
- **Published:** 2026-07-02; v2 updated 2026-07-06
- **Primary URL:** https://arxiv.org/abs/2607.02116
- **Verified overlap:** Provenance, version identity, integrity, approved status, point-in-time reconstruction, deterministic selectors, hash-chained history, and traces of context consumption.
- **Manuscript distinction:** ContextNest governs the knowledge eligible for retrieval. The revised paper governs evidence and authority at acceptance of a candidate software state.

## Runtime authority

### Runtime Governance for AI Agents

- **Title:** *Runtime Governance for AI Agents: Policies on Paths*
- **Authors:** Maurits Kaptein, Vassilis-Javed Khan, Andriy Podstavnychy
- **Identifier:** arXiv:2603.16586v1
- **Published:** 2026-03-17
- **Primary URL:** https://arxiv.org/abs/2603.16586
- **Verified overlap:** Policies map agent identity, partial execution path, proposed next action, and organizational state to runtime governance decisions.
- **Manuscript distinction:** Runtime governance controls actions during execution; the revised paper focuses on candidate-state acceptance, baseline formation, and apply-clearance.

## Execution provenance

### From Agent Traces to Trust

- **Title:** *From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents*
- **Authors:** Yiqi Wang, Jiaqi Zhang, Taotao Cai, Zirui Liu, Qingqiang Sun, Zequn Sun, Zhangkai Wu, Manqing Dong, Mingkai Zheng, Xuefei Yin, Yanming Zhu
- **Identifier:** arXiv:2606.04990v4
- **Published:** 2026-06-03; v4 updated 2026-06-28
- **Primary URL:** https://arxiv.org/abs/2606.04990
- **Verified overlap:** Execution provenance as a typed graph and evidence tracing as evidence-support relations connecting retrieval, claims, tools, memory, actions, and outcomes.
- **Manuscript consequence:** The revised paper avoids broad novelty claims over provenance and process accountability.

## Supply-chain trust model

### in-toto

- **Primary URL:** https://in-toto.io/
- **Official description verified:** “A framework to secure the integrity of software supply chains.”
- **Use in manuscript:** Supports the distinction between ordinary repository metadata and supply-chain evidence linked to authorized steps/functionaries.

### SLSA v1.2

- **Primary URLs:**
  - https://slsa.dev/spec/v1.2/
  - https://slsa.dev/spec/v1.2/provenance
  - https://slsa.dev/spec/v1.2/build-requirements
- **Official scope verified:** Provenance and detailed build requirements for producing artifacts at SLSA levels.
- **Use in manuscript:** Supports the distinction between a reviewable Git record and provenance produced under a stronger trusted build/control plane.

## Editorial conclusion

All five research works named in the supplied feedback were verified. The descriptions were substantially accurate. *Software Delegation Contracts* is the most important omission in v0.1 and is now treated as the closest empirical comparison. The v0.2 novelty claim is correspondingly narrower: evidence self-authorship as a falsifiable acceptance problem, a multidimensional actor–evidence coupling profile, and verdict/apply-clearance within a Git-native reference pattern.
