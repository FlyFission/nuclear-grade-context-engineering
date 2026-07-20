# Related-work and contribution matrix

**Status:** Working research note for the Nuclear-grade Context Engineering white-paper discussion draft<br>
**Date:** 2026-07-19<br>
**Scope:** Public, linkable primary sources and direct project artifacts reviewed for contribution boundaries. This is a focused review, not an exhaustive systematic literature review or a priority search.

## Decision summary

The broad categories **accountable context engineering**, **persistent governed context**, **provenance**, **human governance**, **spec-driven agent workflows**, **trust-boundary collaboration**, and **decision separation** all have adjacent or direct prior art. The white paper should not claim those categories.

The most defensible contribution remains the implemented combination of:

1. a consequence-graded acceptance lifecycle for trust-bearing AI-assisted changes;
2. the self-modification versus self-authorship boundary;
3. actor–evidence independence scaled by consequence;
4. the agent operating envelope as controlled configuration;
5. Verdict versus apply-clearance for separating engineering judgment from present execution authorization; and
6. a Git-native change packet and evidence spine that operationalize those distinctions.

Each should be presented as an **original synthesis, operational formulation, translation, or implementation contribution**, not a claim of priority or demonstrated superiority.

## Matrix

| Source | Direct contribution of the source | Material overlap with Nuclear-grade | What Nuclear-grade may still claim safely |
|---|---|---|---|
| [Mei et al., *A Survey of Context Engineering for Large Language Models*](https://arxiv.org/abs/2507.13334), 2025 | Broad taxonomy covering context retrieval, processing, management, generation, and evaluation | Establishes context engineering as a broad systems field rather than a FlyFission category | A narrow specialization around acceptance and authority, not a new definition of context engineering |
| [Anthropic, “Effective context engineering for AI agents”](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025 | Smallest sufficient high-signal context, retrieval, memory, tools, compaction, and subagent patterns | Overlaps minimum-sufficient context, context hygiene, and tool-aware agent design | Consequence-scaled acceptance discipline rather than context-window performance guidance |
| [Xu et al., “Everything is Context”](https://arxiv.org/abs/2512.05470), 2025 | Persistent file-system abstraction for governed context, access control, provenance, traceability, auditable transitions, and human verification roles | Directly limits any broad claim to accountable/governed context, durable context artifacts, or auditable context lifecycles | Git-native acceptance control, actor–evidence independence, and graded trust-bearing gates |
| [`AGENTS.md` open format](https://github.com/agentsmd/agents.md) | Repository-local instructions and concrete commands for coding agents | Standing repository context and scoped instructions are established practice | Authority-bearing context packs and controlled operating envelopes as part of an acceptance method |
| [OpenAI, “Harness engineering”](https://openai.com/index/harness-engineering/) | Repository harness, concise navigational instructions, executable feedback, and agent-legible environment design | Overlaps repository-as-system, executable checks, and instructions as navigation | Evidence independence, graded acceptance, and explicit decision/authorization states |
| [Anthropic, “Effective harnesses for long-running agents”](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), 2025 | Durable progress artifacts, Git history, incremental execution, end-to-end tests, and self-verification across context windows | Strong precedent for persistent state, clean handoffs, and actor self-checks | Controlled change records and independent acceptance evidence; self-verification remains actor-authored evidence |
| [Yang et al., “SWE-agent”](https://arxiv.org/abs/2405.15793v3), 2024 | Shows that agent–computer interface design materially affects repository navigation, editing, testing, and task performance | Establishes tools, commands, observations, and environment shape as engineered parts of agent behavior | Explicit permission/scope/state-transition limits and change control for the full operating envelope |
| [OpenAI and SWE-bench, “Introducing SWE-bench Verified”](https://openai.com/index/introducing-swe-bench-verified/), 2024/2025 | Human-screened tasks, external tests, and reproducible benchmark execution | Benchmark-level precedent for solver/evidence separation and evaluator scrutiny | Graded use of external or independently reproduced evidence in routine change acceptance |
| [OpenAI, “Why we no longer evaluate SWE-bench Verified”](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified), 2026 | Reports contamination and test defects that weakened the benchmark as a frontier-model judge | Shows that independent execution does not guarantee valid evidence | Evaluation integrity, provenance, freshness, and explicit limits alongside actor–evidence independence |
| [Gloaguen et al., “Evaluating AGENTS.md”](https://arxiv.org/abs/2602.11988), v2 2026 | Empirical evaluation of repository context files; standing context is not automatically beneficial and may increase cost | Supports Nuclear-grade’s minimum-sufficient-context and subtraction posture | The acceptance method itself; do not infer efficacy from this study |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Specify–plan–tasks–implement workflow and executable spec-driven development surfaces | Requirements decomposition, staged artifacts, commands, and gates are prior art | Consequence grading, independence architecture, controlled baseline, and operational clearance distinctions |
| [Zhang and Sun, “Knowledge-Based Pull Requests”](https://arxiv.org/abs/2606.26721), 2026 | Human-confirmed knowledge package crosses a trust boundary; project-side gate precedes regeneration; knowledge acceptance and code integration are separated | Very close on trust boundaries, evidence packages, human decision authority, project-controlled implementation, and separating decisions | Generalized acceptance lifecycle beyond external collaboration; actor–evidence independence; configuration control of agent envelopes; Verdict versus apply-clearance for present action authorization |
| [DOE-STD-1073-2016](https://www.energy.gov/ehss/articles/doe-std-1073-2016) | Configuration identification, change control, status accounting, assessment, and controlled baselines | Foundational lineage for controlled items, baselines, change records, and configuration status | Translation of prompts/models/tools/evals/instructions into an agent operating envelope; Git-native implementation |
| [NRC RG 1.169 Rev. 1](https://www.nrc.gov/docs/ML1235/ML12355A642.pdf) and [RG 1.168 Rev. 2](https://www.nrc.gov/docs/ML1307/ML13073A210.pdf) | Configuration-management plans plus verification, validation, review, and audit guidance for safety-system digital software | Establishes CM, lifecycle discipline, and independent review as prior art; constrains nuclear/compliance wording | Public-source-inspired software-workflow translation only; no compliance or regulatory claim |
| [NASA SWE-141](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation) and [NASA-STD-8739.8B](https://standards.nasa.gov/standard/NASA/NASA-STD-87398) | Software IV&V and assurance/safety requirements; independence includes technical, managerial, and financial dimensions | Establishes independence as more than separate execution or role labels | Model/context/common-brief diversity and protected verification budget as an agent-specific operational translation; do not call it formal IV&V |
| [NIST SP 800-53A Rev. 5](https://doi.org/10.6028/NIST.SP.800-53Ar5) | Assessment procedures for separation of duties and independent verification of plans and evidence | Direct prior art for independent assessment evidence | Self-authorship as an AI-agent failure pattern and graded independently reproduced/authored evidence |
| [NASA SWE-136](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) | Tool accreditation for an intended use | Tool reliance, scope, version, limits, and acceptance are established ideas | Qualification-inspired agent reliance records; never call an AI tool “qualified” without a project-specific formal process |
| [NIST SSDF 1.1](https://doi.org/10.6028/NIST.SP.800-218) | Secure-development practices and evidence-bearing process outcomes | Secure lifecycle and verification are established | A method-specific acceptance spine; no security or assurance certification claim |
| [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) | Govern–Map–Measure–Manage risk framework and socio-technical governance | Human governance, documentation, and risk management are established | A Git-native change-acceptance implementation for AI-assisted software work |
| [NIST SP 800-160 Vol. 1](https://doi.org/10.6028/NIST.SP.800-160v1r1) and [Vol. 2](https://doi.org/10.6028/NIST.SP.800-160v2r1) | Systems-security engineering, assurance reasoning, trustworthiness, and resilience concepts | Assurance cases, claims/evidence reasoning, and engineered trustworthiness are prior art | Bounded design contribution applying claim-matched evidence to agent-assisted change acceptance |
| [OMG SACM 2.3](https://www.omg.org/spec/SACM/) and [GSN Standard Version 3](https://scsc.uk/gsn-standard) | Formal claims–argument–evidence structures, assumptions, constraints, and reasoning | Assurance cases and claims-to-evidence traceability are mature prior art | A deliberately thin Git-native implementation profile; not a replacement for a formal assurance case |
| [DOE-HDBK-1230-2019](https://www.energy.gov/ehss/articles/doe-hdbk-1230-2019) | Critical-characteristics acceptance of external items/services, including intended-use evidence and acceptance methods | External supplier/artifact acceptance patterns are prior art | A software-native model/API/dataset trust record; do not call it commercial-grade dedication |
| [NASA-STD-7009B](https://standards.nasa.gov/standard/nasa/nasa-std-7009) | Acceptance criteria and approval by delegated technical authority for model/simulation use | Implementer, reviewer, approver, and use authority are distinct functions | Agent permission-to-decision-rights mapping and present apply-clearance; authority separation itself is not new |
| [Buhl et al., “Safety Cases for Frontier AI”](https://arxiv.org/abs/2410.21572), 2024 | Safety-case structures and research agenda for frontier AI | Claims/arguments/evidence for AI safety are prior art | Nuclear-grade is a workflow-control method, not a safety case and not evidence of model safety |
| [Gohar et al., “CoDefeater”](https://arxiv.org/abs/2407.13717), 2024 | LLM-assisted discovery of defeaters in assurance cases | Questioning claims and seeking counterevidence are established | Repository-level questioning-attitude implementation; no claim to invent defeater analysis |
| [DOE-HDBK-1028-2009](https://www.energy.gov/ehss/articles/doe-hdbk-1028-2009) | Human-performance practices including task preview, self-checking, peer checking, independent verification, turnover, and learning | Questioning attitude, graded rigor, and learning loops derive from established high-consequence practice | Translation and packaging for AI-assisted software workflows |

## Closest-equivalence tests

### “This is just governed context in files”

**Closest source:** Xu et al.

**Response:** That critique defeats any broad claim to persistent, governed, traceable, or accountable context. Nuclear-grade is narrower: it controls how a proposed change crosses trust-bearing acceptance gates, how evidence independence is graded, and how an accepted state becomes a baseline.

### “This is just spec-driven development with more records”

**Closest source:** GitHub Spec Kit and similar agent workflows.

**Response:** Specification and staged implementation are components. The additional claim is not document quantity; it is authority classification, consequence grading, claim-matched evidence, actor–evidence independence, controlled configuration, and separate Verdict/apply-clearance states.

### “This is Knowledge-Based Pull Requests generalized”

**Closest source:** Zhang and Sun.

**Response:** KPR is the closest reviewed workflow-level neighbor. It focuses on knowledge crossing an external collaboration trust boundary and project-side regeneration. Nuclear-grade applies to internal and external consequential changes, including agent configuration and operational actions; its sharper proposed seams are self-authorship, independence rungs, controlled operating envelopes, and current apply-clearance. The paper should state the overlap plainly and avoid claiming that evidence packages, human gates, or decision separation are unique.

### “This is ordinary configuration management”

**Closest sources:** DOE-STD-1073-2016 and NRC guidance.

**Response:** The underlying CM concepts are not new. The contribution is the identification of prompts, models, tools, evals, repository instructions, permissions, and approval boundaries as one controlled agent operating envelope, plus an implementation designed for ordinary Git workflows.

### “Separate agents already provide independent review”

**Closest sources:** multi-agent workflows and ordinary IV&V concepts.

**Response:** Nuclear-grade explicitly rejects role labels as sufficient evidence of independence. It distinguishes actor independence, evidence provenance, mechanism diversity, and authority. Whether this exact self-authorship boundary has direct prior art remains an open search question.

## Contribution-claim guardrail

### Supported for the discussion draft

- “original synthesis”
- “consequence-graded acceptance method”
- “operational formulation”
- “software-native translation”
- “Git-native implementation”
- “feasibility demonstration”
- “author-judged qualitative comparison”
- “invites independent replication and prior-art correction”

### Not supported

- “first” or “first framework”
- “novel accountable context engineering” as a broad category
- “proven” or “validated methodology”
- “reduces defects,” “improves safety,” or “outperforms”
- “nuclear-compliant,” “safety-grade,” “formal V&V,” or “regulator-ready”
- any implication that passing repository checks establishes operational efficacy

## Remaining targeted search questions

1. Is “self-authorship” already used in software assurance or agent-evaluation literature for an actor generating the evidence consumed by its own gate?
2. Has actor–evidence independence been formalized separately from actor/reviewer independence in autonomous-agent systems?
3. Do deployment-authorization frameworks already distinguish an engineering verdict from current execution/apply clearance using equivalent state semantics?
4. Which agent-governance systems treat model, prompt, tools, retrieval, permissions, evals, and approval policy as one controlled configuration item?
5. What adoption-cost and independent-evaluation designs would allow comparison without turning Nuclear-grade into a compliance-proxy checklist?

These open questions should remain visible until an external reviewer or systematic search closes them.
