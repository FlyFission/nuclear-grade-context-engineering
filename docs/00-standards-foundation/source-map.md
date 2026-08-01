# Source Map

**Purpose:** List the public, open, linkable sources that Nuclear-grade may cite directly. These sources document the lineage behind its open software-native synthesis and reference implementation.

**Repo posture:** Nuclear-grade is a teaching method for software engineering. It is built on public sources. It does not claim to meet DOE, NRC, IAEA, CNSC, ONR, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, NASA, NIST, CISA, OpenSSF, OWASP, or any other framework.

**Use rule:** A source can shape public templates only when two things are true. First, it is public, open, and linkable. Second, the resulting artifact is an authored software adaptation that states its lineage and claims neither conceptual priority nor compliance merely because the implementation text or code is new.

---

## Classification and status

| Classification | Meaning | Public repo use |
|---|---|---|
| Core | Foundational to Nuclear-grade doctrine. | May be cited in source-lineage notes and field-guide docs when status is `verified-public`. |
| Supporting | Useful for specific concepts or examples. | Cite where directly relevant; do not over-center. |
| Context-only | Useful industry/background awareness, but not direct template lineage. | Mention sparingly, if public. |
| Excluded as direct input | Paywalled/proprietary/copyrighted or risky for template derivation. | Do not cite as source lineage; do not derive templates. |

| Status | Meaning |
|---|---|
| verified-public | Public page/link checked and suitable for source-lineage use. |
| public-url-needed | Known source or source family, but not direct template lineage until an official public URL/current version is verified. |
| supporting-context | Publicly reachable or useful as context, but not a core direct lineage source for v0 templates. |
| excluded-direct | Do not use as direct source lineage. |

The confidence fields say how well a source family fits this repo. They do not say anything about meeting a standard.

---

## Tier 0 - Boundary / Repo-Safety Sources

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Notes |
|---|---|---:|---|---|---:|---|
| Nuclear-grade disclaimer | `../../DISCLAIMER.md` | Core | verified-public | Prevent overclaiming; clarify educational/inspired-by nature. | High | Must be visible from README/quickstart. |
| Public citation strategy | `public-citation-strategy.md` | Core | verified-public | Controls what can be cited and how. | High | Internal repo governance. |
| Do-not-cite-directly list | `do-not-cite-directly.md` | Core | verified-public | Prevents paywalled/proprietary template lineage. | High | Especially important for ASME/EPRI/IEEE/IEC/ISO/ANSI/ANS/NEI. |

---

## Tier 1 - DOE / CFR Nuclear Engineering Backbone

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| 10 CFR 830 Subpart A, Quality Assurance Requirements | https://www.ecfr.gov/current/title-10/chapter-III/part-830/subpart-A | Core | verified-public | Public QA backbone: work processes, records, assessment, correction, graded quality concepts. | High | Field-guide concepts only; no compliance claims. |
| 10 CFR 830 Subpart B, Safety Basis Requirements | https://www.ecfr.gov/current/title-10/chapter-III/part-830/subpart-B | Core | verified-public | Safety-basis logic: hazards, controls, authorization/evidence posture. | High | Design basis and assurance-case analogies. |
| 10 CFR 50 Appendix B, QA Criteria | https://www.ecfr.gov/current/title-10/chapter-I/part-50/appendix-Appendix%20B%20to%20Part%2050 | Core | verified-public | Public nuclear QA criteria reference. | High | High-level inspiration for traceability, design control, corrective action, records. |
| DOE quality assurance program page / DOE O 414.1E context | https://www.energy.gov/ehss/quality-assurance | Core | verified-public | DOE QA program logic; graded approach; assessment/corrective action/software quality context. | Medium-high | Cite the public DOE page for concept lineage; do not claim implementation of DOE O 414.1E. |
| DOE quality assurance policy and directives page | https://www.energy.gov/ehss/quality-assurance-policy-and-directives | Supporting | verified-public | Public DOE QA directives context. | Medium | Useful context; direct lineage should prefer CFR and public DOE QA page. |
| DOE-HDBK-1028-2009, Human Performance Improvement Handbook | https://www.energy.gov/ehss/articles/doe-hdbk-1028-2009 | Core | verified-public | Human performance tools: questioning attitude, task preview, pause when unsure, self-checking, procedure use, validate assumptions, communication, verification practices, turnover, operating experience, decision making, and change management. | High | Source lineage for HPI overlays, Question phase, questioning-attitude, turnover, self-check, OPEX, and review practices; no HPI program or compliance claim. |
| DOE-STD-1073-2016, Configuration Management | https://www.energy.gov/ehss/articles/doe-std-1073-2016 | Core | verified-public | Configuration discipline, design requirements, approved configuration, change impact, drift. | High | One of the primary translation anchors. |
| DOE-STD-1189-2016, Integration of Safety into Design | https://www.energy.gov/ehss/articles/doe-std-1189-2016 | Core | verified-public | Lifecycle integration, safety/design/project gates, early basis, design maturation. | High | Source for lifecycle/gate doctrine. |
| DOE-STD-3024-2011, Content of SDDs | https://www.energy.gov/ehss/articles/doe-std-3024-2011 | Core | verified-public | FDD/SDD logic: requirements, basis, interfaces, design features, graded rigor. | High | Source for design description analogies. |
| DOE-STD-3009-2014, Nonreactor Nuclear Facility DSA | https://www.energy.gov/ehss/articles/doe-std-3009-2014 | Core | verified-public | Hazard analysis, accident/failure analysis, control selection, DSA/TSR style evidence logic. | High | Source for failure-mode and assurance-case concepts. |
| DOE O 413.3B, Program and Project Management for Capital Assets | https://www.energy.gov/projectmanagement/directives | Core | verified-public | Critical decisions, project lifecycle, independent reviews, baseline maturity. | Medium-high | Use for stage-gate analogy without compliance claims. |
| DOE Work Breakdown Structure Handbook | https://www.energy.gov/projectmanagement/articles/department-energy-work-breakdown-structure-handbook | Core | verified-public | Product-oriented WBS, the 100% rule, common element structures, the WBS dictionary. | High | Primary lineage for `breaking-down-the-work`; product-decomposition concepts only; no compliance claim. |
| NNSA SD 413.3-4, Program Requirements Document | NNSA/DOE official public link not yet recorded in this repo | Supporting | public-url-needed | PRD development logic: mission, requirements, basis, project controls. | Medium | Discovery/context only for v0; not direct template lineage until official public URL is recorded. |
| DOE-STD-3007-2017, Criticality Safety Evaluations | https://www.energy.gov/ehss/articles/doe-std-3007-2017 | Supporting | verified-public | Evaluation discipline, conservative assumptions, consequence-driven analysis. | Medium | Supporting only; too domain-specific for core UX. |
| 10 CFR Part 21, Reporting of Defects and Noncompliance | https://www.ecfr.gov/current/title-10/chapter-I/part-21 | Supporting | verified-public | Outward duty (§21.21) to evaluate a discovered defect and notify affected parties, not only fix it locally. | Medium-high | Concept lineage for the outward-reporting clause when a defect is found in a shared or supplied artifact; no compliance claim. |
| DOE-HDBK-1230-2019, Commercial Grade Dedication Application Handbook | https://www.standards.doe.gov/standards-documents/1200/1230-bhdbk-2019 | Supporting | verified-public | Acceptance discipline for items not built under the program: identify the few critical characteristics, choose an acceptance method, verify them independently. | Medium-high | Concept lineage for the outside-artifact acceptance structure in `vetting-outside-code-and-models`; complements NIST SP 800-161. Translated to software vocabulary; the label is not reused and no compliance is claimed (see `do-not-cite-directly.md`). |

---

## Tier 1b - Cross-Jurisdiction Graded-Approach References (concept-only)

The graded approach is the repo's central organizing principle and is already anchored to DOE (Tier 1: 10 CFR 830 and the DOE QA page). These international and foreign-regulator statements of the same idea are recorded for **concept lineage only** — they sharpen the cross-jurisdiction definition in `../01-field-guide/source-to-concept-crosswalk.md`. They are **not** direct template lineage, and nothing here claims compliance with IAEA, CNSC, or ONR. URLs are marked `public-url-needed` until a current official public link is verified in-repo (same rule as the NNSA row above).

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Notes |
|---|---|---:|---|---|---:|---|
| IAEA Safety Glossary | official IAEA publication page not yet verified in-repo | Supporting | public-url-needed | Graded approach as control measures commensurate with likelihood, consequence, and risk. | Medium | Concept-only; verify public URL before any direct citation. |
| IAEA GSR Part 2, Leadership and Management for Safety | official IAEA publication page not yet verified in-repo | Supporting | public-url-needed | The management system is developed and applied using a graded approach, with documented grading criteria. | Medium | Concept-only; no compliance claim. |
| CNSC REGDOC-3.5.3, Regulatory Fundamentals | official CNSC page not yet verified in-repo | Supporting | public-url-needed | Graded approach scales analysis, documentation depth, and scope of action to risk, facility characteristics, and performance history. | Medium | Concept companion for the performance-history modulator (load-bearing lineage stays DOE-HDBK-1028 / NASA Lessons Learned). |
| ONR graded-approach guidance (IRR17) | official ONR page not yet verified in-repo | Supporting | public-url-needed | Sets the level of analysis, documentation, and actions needed to comply with safety requirements; low/medium/high pathways. | Medium | Concept-only; no compliance claim. |

---

## Tier 2 - NRC Public Nuclear Software Assurance Anchors

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| NRC RG 1.152 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-152/ | Core | verified-public | Computers in nuclear safety systems; digital assurance/security concerns. | High | Nuclear-software bridge. |
| NRC RG 1.168 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-168/ | Core | verified-public | V&V, reviews, audits for digital computer software. | High | Verification/review doctrine. |
| NRC RG 1.169 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-169/ | Core | verified-public | Software configuration management plans. | High | Software CM source lineage. |
| NRC RG 1.170 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-170/ | Core | verified-public | Software test documentation. | High | Verification-ledger/test-evidence concepts. |
| NRC RG 1.171 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-171/ | Core | verified-public | Software unit testing. | High | Test-quality concepts. |
| NRC RG 1.172 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-172/ | Core | verified-public | Software requirements specifications. | High | Requirements-to-tests traceability. |
| NRC RG 1.173 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-173/ | Core | verified-public | Software lifecycle processes. | High | Lifecycle doctrine. |
| NRC RG 1.187 | https://www.nrc.gov/reading-rm/doc-collections/reg-guides/power-reactors/rg/01-187/ | Core | verified-public | V&V of commercial nuclear power plant safety-system software. | Medium-high | Use carefully; public, but formal nuclear scope. |
| NUREG/BR-0167 | https://www.nrc.gov/reading-rm/doc-collections/nuregs/brochures/br0167/index | Core | verified-public | Software QA program and guidelines. | Medium-high | Public software QA anchor for concept lineage. |
| NUREG/CR-6101 | https://www.nrc.gov/reading-rm/doc-collections/nuregs/contract/cr6101/index | Core | verified-public | Software reliability/safety in protection systems. | Medium-high | Supporting high-integrity software concepts. |
| NUREG/CR-6263 | https://www.nrc.gov/about-nrc/regulatory/research/digital | Supporting | supporting-context | High-integrity software for nuclear power plants. | Medium | Public NRC research table context for v0; record direct NUREG page when verified. |
| NUREG/CR-6734 | https://www.nrc.gov/reading-rm/doc-collections/nuregs/contract/cr6734/index | Core | verified-public | Software requirements guidelines. | Medium-high | Requirements/specification concepts. |
| NUREG/CR-6303, Diversity and Defense-in-Depth Analyses | https://www.nrc.gov/reading-rm/doc-collections/nuregs/contract/cr6303/index | Supporting | verified-public | System/I&C-level diversity-and-defense-in-depth method; a multi-attribute diversity taxonomy (design, equipment, functional, signal, human). | Medium-high | Added lineage for the independent-control-layers concept (controls must fail independently); system-level, not a software-diversity standard; no compliance claim. |

**Important:** NRC software sources are the clearest public link from nuclear work to software work. Give them a strong place in source lineage. But keep the templates original, and never claim they meet a standard.

---

## Tier 3 - NIST / CISA Federal Software, Cyber, AI, and Supply-Chain Anchors

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| NIST SP 800-218, Secure Software Development Framework | https://csrc.nist.gov/publications/detail/sp/800-218/final | Core | verified-public | Secure software development practices. | High | Secure-by-default evidence spine. |
| NIST SP 800-160 Vol. 1 | https://csrc.nist.gov/publications/detail/sp/800-160/vol-1/final | Core | verified-public | Systems security engineering. | High | Security-as-engineering doctrine. |
| NIST SP 800-160 Vol. 2 | https://csrc.nist.gov/publications/detail/sp/800-160/vol-2/final | Core | verified-public | Cyber-resilient systems. | High | Resilience/failure/recovery concepts. |
| NIST SP 800-53 | https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final | Supporting-core | verified-public | Controls/evidence language. | High | Use as control vocabulary, not checklist bloat. |
| NIST SP 800-161 | https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final | Core | verified-public | Cyber supply-chain risk management. | High | Dependency trust basis. |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | Core | verified-public | AI risk/trustworthiness framing. | High | AI-assisted development controls. |
| NIST Cybersecurity Framework 2.0 | https://www.nist.gov/cyberframework | Supporting-core | verified-public | Govern/identify/protect/detect/respond/recover. | High | Useful operating vocabulary. |
| CISA Secure by Design | https://www.cisa.gov/securebydesign | Core | verified-public | Practical product security accountability. | High | Release readiness/security posture. |
| CISA KEV Catalog | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | Supporting | verified-public | Operational dependency/security awareness. | High | Dependency revalidation triggers. |
| CISA SBOM guidance | https://www.cisa.gov/sbom | Supporting-core | verified-public | SBOM transparency/dependency evidence. | High | Dependency trust basis and release readiness. |
| NIST AI 600-1, Generative AI Profile | https://doi.org/10.6028/NIST.AI.600-1 | Supporting | verified-public | Generative-AI risk profile; names that some risks are unknown and others known but hard to estimate. | Medium-high | Concept lineage for functional insufficiency (harm with no fault; the known/unknown frontier); complements NIST AI RMF; no compliance claim. |

---

## Tier 4 - NASA High-Reliability Software and Systems Anchors

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| NASA Software Engineering Handbook / NASA-HDBK-2203 | https://swehb.nasa.gov/ | Core | verified-public | Practical public software lifecycle guidance. | High | Requirements, design, testing, reviews, lifecycle. |
| NPR 7150.2, NASA Software Engineering Requirements | https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2 | Core | verified-public | Software engineering requirements and lifecycle. | High | Source for software lifecycle concepts. |
| NASA-STD-8739.8, Software Assurance and Software Safety | https://standards.nasa.gov/standard/nasa/nasa-std-87398 | Core | verified-public | Software assurance and software safety. | High | Assurance/evidence/independent review concepts. |
| NASA Systems Engineering Handbook | https://www.nasa.gov/reference/nasa-systems-engineering-handbook/ | Core | verified-public | Requirements, interfaces, V&V, technical reviews. | High | Systems thinking and lifecycle. |
| NASA Lessons Learned | https://llis.nasa.gov/ | Supporting-core | verified-public | OPEX/corrective-action learning loop. | High | OPEX and post-release learning. |
| NASA SWE-141, Software Independent Verification and Validation | https://swehb.nasa.gov/display/SWEHBVD/SWE-141+-+Software+Independent+Verification+and+Validation | Supporting | verified-public | Independence framed on three axes — technical, managerial, and financial — scaled to software consequence. | Medium-high | Concept lineage for naming the financial/budget axis of agent independence (a verifier whose budget the builder controls is captured); complements the existing control-stack note; no compliance claim. |
| NASA SWE-136, Software Tool Accreditation | https://swehb.nasa.gov/display/SWEHBVD/SWE-136+-+Software+Tool+Accreditation | Supporting | verified-public | Tools must not insert undetected errors; accreditation rigor scales with software class. | Medium-high | Concept lineage for qualifying a tool or agent you rely on to catch errors, proportional to that reliance; no compliance claim. |
| NASA "A Practical Tutorial on MC/DC" (NTRS 20010057789) | https://ntrs.nasa.gov/citations/20010057789 | Supporting | verified-public | Structural-coverage hierarchy: statement, decision, and modified condition/decision coverage. | Medium | Concept lineage for grading proof depth by mode (coverage rigor scales with consequence); no compliance claim. |
| NASA/CR-2015-218982, Application of SAE ARP4754A | https://ntrs.nasa.gov/citations/20160001634 | Supporting | verified-public | Public walk-through of functional hazard assessment and top-down/bottom-up failure analysis that set assurance level before build. | Medium | Concept lineage for deriving a change's grade two directions (worst-credible outcome and if-this-fails blast radius); no compliance claim. |

---

## Tier 5 - Open Software Assurance / Supply-Chain / Application Security Anchors

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| SLSA | https://slsa.dev/ | Supporting-core | verified-public | Build provenance and supply-chain integrity. | High | Release readiness, provenance. |
| OpenSSF Scorecard | https://github.com/ossf/scorecard | Supporting-core | verified-public | Dependency/project health signals. | High | Dependency trust basis. |
| OpenSSF S2C2F | https://github.com/ossf/s2c2f | Supporting-core | verified-public | Secure supply-chain consumption. | High | Dependency intake/review. |
| SPDX | https://spdx.dev/ | Supporting | verified-public | SBOM/license identity. | High | Dependency records. |
| CycloneDX | https://cyclonedx.org/ | Supporting | verified-public | SBOM/vulnerability/dependency metadata. | High | Dependency records. |
| OWASP ASVS | https://owasp.org/www-project-application-security-verification-standard/ | Supporting-core | verified-public | Appsec verification. | High | Verification criteria. |
| OWASP SAMM | https://owasp.org/www-project-samm/ | Supporting | verified-public | Secure software maturity model. | High | Roadmap/maturity context. |
| OWASP Top 10 | https://owasp.org/www-project-top-ten/ | Supporting | verified-public | Common appsec risk awareness. | High | Failure-mode prompts. |
| 18F Engineering Guide | https://engineering.18f.gov/ | Supporting | verified-public | Public government software delivery habits. | High | Usability/adoption/de-risking. |
| 18F De-risking Government Technology | https://derisking-guide.18f.gov/ | Supporting | verified-public | Incremental delivery/de-risking. | High | Anti-overhead adoption strategy. |
| EARS (Easy Approach to Requirements Syntax), Mavin | https://alistairmavin.com/ears/ | Supporting | verified-public | Controlled requirement grammar: ubiquitous / event (WHEN) / state (WHILE) / optional (WHERE) / unwanted (IF-THEN) trigger→response shapes for testable, unambiguous requirements. | High | Concept lineage for the requirement-grammar note in `basis.md` and `spec.md`; serves the operational-unambiguity charter article; public method page; no compliance claim. |

---

## Tier 6 — Agentic-AI Operations Sources

These sources shape how we attack-test agents, trace what they do, and profile them. They are supporting context only. The repository assembles them into an open, tool-agnostic reference workflow. You do not need NIM, a GPU, W&B, or NeMo to use the skills and templates.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| NVIDIA Safety for Agentic AI blueprint | https://github.com/NVIDIA-AI-Blueprints/safety-for-agentic-ai | Supporting | supporting-context | Adversarial risk taxonomy (prompt injection, jailbreak, authority escalation, tool misuse, unsafe output, retrieval poisoning, data exfiltration); evaluate → harden → re-evaluate lifecycle; before/after posture records. | High | Conceptual influence for `stress-testing-agent-changes` skill and adversarial class vocabulary; no compliance, penetration-test, or safety certification claim. |
| Garak LLM vulnerability scanner | https://github.com/leondz/garak | Supporting | supporting-context | Open-source probe-based adversarial testing of LLMs; risk categories; reproducible vulnerability scan reports. | High | Adversarial class taxonomy; no compliance claim. |
| NVIDIA NeMo Guardrails | https://github.com/NVIDIA-NeMo/Guardrails | Supporting | supporting-context | Runtime guardrail orchestration: input, output, retrieval, dialog, and topic rails; jailbreak detection; content safety; configuration as code. | High | Rail-type vocabulary for adversarial class selection and agent authority model; no compliance claim. |
| W&B Weave traceability | https://wandb.ai/site/weave | Supporting | supporting-context | Trace-tree observability: span-per-call, auto-logging of inputs/outputs/metadata/latency/cost, audit lineage, reproducibility, evaluation loops. | High | Conceptual influence for `recording-what-an-agent-did` skill and trace-as-evidence vocabulary; no compliance or audit-certification claim. |
| NVIDIA NeMo Agent Toolkit (AIQ) | https://github.com/NVIDIA/NeMo-Agent-Toolkit | Supporting | supporting-context | Framework-agnostic agent profiling (token/latency/cost per step to workflow level), offline evaluation harness, OpenTelemetry-compatible observability exporters (Phoenix, Weave, Langfuse, LangSmith). | High | Reference model for evidence-spine detail and skill-evaluation rubric; influence for future runnable `evals/` suite; no compliance claim. |
| OpenTelemetry distributed tracing | https://opentelemetry.io/ | Supporting | supporting-context | Vendor-neutral structured spans, parent-child trace relationships, context propagation, semantic conventions for LLM/agent instrumentation. | High | Structured span vocabulary for `recording-what-an-agent-did` and `execution-trace.md`; no compliance claim. |
| Safety Cases for Frontier AI (arXiv:2410.21572) | https://arxiv.org/abs/2410.21572 | Supporting | verified-public | Structured claim → argument → evidence assurance argument for AI systems. | Medium-high | Concept lineage for a release safety-case argument with named defeaters; no compliance claim. |
| CoDefeater: LLMs to find defeaters in assurance cases (arXiv:2407.13717) | https://arxiv.org/abs/2407.13717 | Supporting | verified-public | The defeater hunt: enumerate reasons an assurance argument could be false. | Medium | Concept lineage for the "what would make this argument false?" step in release readiness; no compliance claim. |
| Capability-based scaling trends for LLM red-teaming (arXiv:2505.20162) | https://arxiv.org/abs/2505.20162 | Supporting | verified-public | Fixed-capability probes miss the unknown-unsafe frontier as systems improve. | Medium | Concept lineage for scenario discovery beyond known attack classes (functional insufficiency); no compliance claim. |
| OpenAI Model Spec, chain of command | https://model-spec.openai.com/2025-09-12.html | Supporting | verified-public | Authority hierarchy and the rule to ignore untrusted data by default. | Medium-high | Concept lineage for treating retrieved pages, tool output, issues, and logs as evidence data rather than operating authority; no model-specific dependency. |
| OWASP LLM01: Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | Supporting | verified-public | Direct and indirect prompt-injection risk, including malicious content in external data. | Medium-high | Concept lineage for the instruction-smuggling failure mode in `context-window-discipline.md`; no appsec compliance claim. |
| IESBA Code and self-review threat | https://www.ethicsboard.org/iesba-code | Supporting | verified-public | Professional-independence doctrine: evaluating or relying on prior work can create a self-review threat. | High | Conceptual ancestor for evidence self-authorship; use to concede that the generic independence problem predates AI. |
| Panickssery et al., "LLM Evaluators Recognize and Favor Their Own Generations" (arXiv:2404.13076) | https://arxiv.org/abs/2404.13076 | Supporting | verified-public | Empirical evidence that model evaluators can recognize and prefer their own outputs. | High | Mechanism evidence for actor/evaluator coupling; not proof of software-safety benefit. |
| Li et al., "Preference Leakage: A Contamination Problem in LLM-as-a-judge" (arXiv:2502.01534) | https://arxiv.org/abs/2502.01534 | Supporting | verified-public | Generator/evaluator preference leakage and correlated model-family effects. | High | Mechanism evidence for the context and mechanism axes of the coupling profile. |
| Schmalbach, "Software Delegation Contracts" (arXiv:2606.17099) | https://arxiv.org/abs/2606.17099 | Supporting | verified-public | Measures reviewability of AI coding-agent work through delegation-contract structure. | High | Close prior art for reviewable agent handoffs; custody and multidimensional coupling are the narrower extension. |
| Kang, "Governed AI-Assisted Engineering" (arXiv:2606.22484) | https://arxiv.org/abs/2606.22484 | Supporting | verified-public | Graduated human oversight for agentic code generation in regulated domains. | High | Close prior art for consequence-graded governance and human oversight; prevents broad novelty claims for graded rigor. |
| Sulpovar et al., "ContextNest" (arXiv:2607.02116) | https://arxiv.org/abs/2607.02116 | Supporting | verified-public | Verifiable context governance for autonomous agents. | Medium-high | Adjacent context-governance work; reinforces that governed context is not the novel center. |
| Kaptein et al., "Runtime Governance for AI Agents: Policies on Paths" (arXiv:2603.16586) | https://arxiv.org/abs/2603.16586 | Supporting | verified-public | Runtime policy enforcement over agent action paths. | High | Prior art for runtime authorization and apply-time policy; verdict/apply separation remains an implementation primitive. |
| Wang et al., "From Agent Traces to Trust" (arXiv:2606.04990) | https://arxiv.org/abs/2606.04990 | Supporting | verified-public | Survey of agent evidence tracing and execution provenance. | High | Provenance and trace lineage; reinforces that trace linkage is not semantic adequacy or evidence custody. |
| Pollner et al., "Human Oversight for AI-Generated Test Artifacts" | https://itea.org/journals/volume-47-2/human-oversight-for-ai-generated-test-artifacts/ | Supporting | verified-public | AI-generated tests are candidate artifacts, not self-validating evidence; oversight should scale to risk. | High | Close prior art for generated-test custody and independent review; Nuclear-grade extends the question across the complete acceptance evidence path. |
| Kawas, "Decision Assurance for AI-Enabled Mission Systems" | https://doi.org/10.61278/itea.47.2.1005 | Supporting | verified-public | Connects test evidence to operational decision authority. | High | Close lineage for evidence-to-authority reasoning and for treating verdict/apply-clearance as established-adjacent. |
| Ravuru, "Artifact Gate Evaluation for AI-Assisted Software Delivery" | https://doi.org/10.2139/ssrn.6940958 | Supporting | verified-public | Controlled comparison of prompt-to-code, specification-driven, and artifact-aware delivery. | Medium-high | Prevents novelty claims for artifact-gate workflows or the current twelve-scenario design inspection. |
| Ming et al., "From Traceability to Reviewability" | https://doi.org/10.2139/ssrn.7030983 | Supporting | verified-public | Intent-anchored claim/evidence structures for reviewing agent-generated software work. | High | Close reviewability prior art; custody and multidimensional coupling remain the narrower Nuclear-grade seam. |
| Kaul et al., "Behavioral Governance for Autonomous AI Agents: The AgentBound Framework" (arXiv:2606.30970) | https://arxiv.org/abs/2606.30970 | Supporting | verified-public | Behavioral constraints and runtime governance for autonomous agents. | Medium-high | Adjacent agent-governance prior art; not direct custody lineage. |
| Parasuraman, Sheridan, and Wickens, "A Model for Types and Levels of Human Interaction with Automation" | https://doi.org/10.1109/3468.844354 | Supporting | verified-public | Allocates information acquisition, analysis, decision selection, and action implementation across automation levels. | High | Prior art for function allocation and autonomy levels; blocks novelty claims for an agent/human authority ladder. |
| Scerri, Pynadath, and Tambe, "Towards Adjustable Autonomy for the Real World" | https://doi.org/10.1613/jair.1037 | Supporting | verified-public | Conditional transfer-of-control strategies between agents and humans under timing and coordination constraints. | High | Closest scholarly collision for authority transfer; Nuclear-grade must differentiate through evidence-conditioned episode records, not generic handoff. |
| Horvitz, "Principles of Mixed-Initiative User Interfaces" | https://doi.org/10.1145/302979.303030 | Supporting | verified-public | Uncertainty- and utility-conditioned initiative, consultation, and deferral. | High | Prior art for dynamic human/agent initiative; a pause or escalation alone is not novel custody. |
| Santoni de Sio and van den Hoven, "Meaningful Human Control over Autonomous Systems" | https://doi.org/10.3389/frobt.2018.00015 | Supporting | verified-public | Tracking relevant human reasons and tracing outcomes to responsible humans. | High | Prior control/accountability foundation; a structural record does not by itself establish meaningful human control. |
| Singh, Cobbe, and Norval, "Decision Provenance: Harnessing Data Flow for Accountable Systems" | https://doi.org/10.1109/ACCESS.2018.2887201 | Supporting | verified-public | Decision-pipeline provenance, inputs, processing, entities, interconnections, downstream effects, and accountability. | High | Closest provenance collision; the narrower repository seam is policy-relative evidence custody joined to explicit software decision rights. |
| Elish, "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction" | https://doi.org/10.17351/ests2019.260 | Supporting | verified-public | Shows how nominally nearby humans can absorb blame despite distributed or ineffective control. | High | Blocks the inference that human approval proves evidence access, authority, time, or effective intervention capability. |
| W3C PROV-DM and PROV-O | https://www.w3.org/TR/prov-dm/ | Supporting | verified-public | Standard entities, activities, agents, derivation, responsibility, time, and provenance bundles. | High | Adopt for lineage mapping; provenance does not itself establish evidence sufficiency, independence, or decision authority. |
| OMG Structured Assurance Case Metamodel 2.2 | https://www.omg.org/spec/SACM/2.2/PDF | Supporting | verified-public | Structured claims, arguments, evidence assets, participants, activities, and evidence provenance. | High | Prior art for assurance structure; Nuclear-grade is an operational decision-record profile, not a new assurance metamodel. |
| Palantir Ontology, proposals, scenarios, actions, and observability documentation | https://www.palantir.com/docs/foundry/ontology/overview/ | Context-only | supporting-context | Broad operational semantic layer joining governed state, actions, permissions, review, logs, scenarios, and agent traces. | High | Industrial analogue and architecture inspiration only; not direct template lineage and not a platform Nuclear-grade claims to replace. |
| Sonar, 2026 State of Code Developer Survey | https://www.sonarsource.com/state-of-code-developer-survey-report.pdf | Supporting | public-url-needed | Prevalence of AI-authored code and the verification gap: ~42% of committed code AI-generated or significantly assisted (respondents project ~65% by 2027), 96% do not fully trust it to be functionally correct, ~48% always verify before committing, 38% report reviewing AI code costs more effort than reviewing a colleague's. | Medium-high | Prevalence evidence for the AI-era note in `../01-field-guide/leadership-and-high-reliability.md`, `../02-operating-system/quality-verdict-accountability.md`, and the coupling failure in `../02-operating-system/actor-evidence-independence.md`. **Self-reported survey by a code-quality vendor, not measured telemetry**; the vendor sells verification tooling the finding favors — disclose that wherever it is cited. Establishes prevalence, not mechanism; no efficacy or compliance claim. |

**Vendor-affiliation note.** The Sonar survey row above and the code-cleanliness study in Tier 9 come from the same commercial vendor, and both findings favor that vendor's product category. Neither has been independently replicated. They are cited because they are public, linkable, and the best available evidence on their questions — and the affiliation is disclosed at every citation point, which is the same custody discipline `../02-operating-system/actor-evidence-independence.md` asks of everyone else's evidence.

**Status note.** Both rows are held at `public-url-needed`, not `verified-public`, on purpose. The status table above defines `verified-public` as *the public page/link checked* — and the environment that added these rows was blocked from reaching the hosts, so the URLs were never fetched. The figures are corroborated across independent secondary coverage, which supports the *numbers* but does not discharge the *link-checked* requirement; those are different claims, and the status label means the second one. Promote both rows to `verified-public` once a reviewer with unrestricted egress confirms the URLs. Tracked as a gap in `.nuclear/changes/quality-verdict-accountability/verification.md` (V-14).

---

## Tier 7 — Project Structuring, Decomposition & Agentic-Folder Architecture Sources

These sources shape how we break work into pieces and how we lay out folders and files. They are supporting context only. The repository's implementation is an open software-native synthesis that works with any tool. The main DOE Work Breakdown Structure Handbook is listed in Tier 1. We claim no compliance with DOE, DoD, NASA, PMI, GAO, NARA, NIST, INCOSE, or ISO.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| Model Workspace Protocol / Interpretable Context Methodology (Van Clief and McDermott) | https://arxiv.org/abs/2603.16021 | Supporting | verified-public | Folder structure as agentic architecture: numbered stage folders, layered context, per-stage Inputs/Process/Outputs contracts, scripts for mechanical work, a human review gate per stage. | High | Conceptual influence for `organizing-project-folders` and the agentic-folder worked example; MIT-licensed public paper; no compliance claim. |
| MIL-STD-881F, Work Breakdown Structures for Defense Materiel Items | https://www.dau.edu/cop/mwt/documents/mil-std-881f-work-breakdown-structures-defense-material-items | Supporting | verified-public | Product-oriented decomposition, the 100% rule, WBS levels, the WBS dictionary, no-overlap, common elements. | High | Concept lineage for `breaking-down-the-work`; DoD standard hosted publicly by DAU; no compliance claim. |
| NASA WBS Handbook (NASA/SP-2016-3404) | https://ntrs.nasa.gov/citations/20180000844 | Supporting | verified-public | Product hierarchy, WBS dictionary, traceability, level-of-detail. | High | Decomposition and dictionary lineage; no compliance claim. |
| GAO-20-195G, Cost Estimating and Assessment Guide | https://www.gao.gov/products/gao-20-195g | Supporting | verified-public | WBS as the foundation of a credible estimate; the WBS dictionary. | High | Estimate-basis lineage for the dictionary size field; no compliance claim. |
| NARA Bulletin 2015-04, Appendix B, File Naming and Folder Structure Guidance | https://www.archives.gov/records-mgmt/bulletins/2015/2015-04-appendix-b.html | Supporting | verified-public | Folder-to-disposition mapping; records-management folder discipline; platform-safe naming. | Medium-high | Lineage for folder disposition notes and naming in `organizing-project-folders`; no compliance claim. |
| NIST Electronic File Organization Tips | https://www.nist.gov/document/electronicfileorganizationtips-2016-03pdf | Supporting | verified-public | Lowercase alphanumeric plus hyphen/underscore, ISO-8601 dates, single-period extension, depth and path limits. | High | Naming-rule lineage for `organizing-project-folders`; no compliance claim. |
| DoDAF (DoD Architecture Framework) | https://dodcio.defense.gov/library/dod-architecture-framework/ | Context-only | supporting-context | Functional vs product decomposition; architecture viewpoints. | Medium | High-level decomposition-perspective awareness only; no compliance claim. |
| PMI Practice Standard for WBS; INCOSE SE Handbook; ISO 21500/21502/15489 | membership or paywalled; ISO on the do-not-cite-directly list | Excluded as direct input | excluded-direct | 100% rule, MECE, 8/80, work package, cohesion/coupling, records-management framing. | Medium | Transferable principles encoded as original workflow only; do not cite as template lineage or derive structure from these texts. |

These sources shape how we break work down and keep folders in order. Nothing more. They do not add governance, CI, supply-chain, or compliance machinery. That work belongs to the other tiers and skills.

---

## Tier 8 — Leadership, Human-Performance, and High-Reliability Operating Culture

These sources shape how people and AI agents are directed, how authority and intent are handled, and how teams stay honest and recover from failure. They are concept lineage only. The repository adapts them into an open software-native workflow. We claim no compliance with any program, and we reproduce no proprietary book.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| Rickover, "Doing a Job" (public speech text) | https://govleaders.org/rickover.php | Supporting | verified-public | Ownership with technical depth; give authority early but stay responsible; face facts; write it down. | High | Concept lineage for charter ownership/technical-depth articles and `critical-systems.md`; no program claim. |
| Rickover, "Paper Reactors, Real Reactors" (1953 memo) | https://whatisnuclear.com/rickover.html | Supporting | verified-public | Real responsibility and physical reality discipline an engineer in ways a paper design never does. | Medium-high | Concept lineage for face-facts and evidence-over-persuasion framing; no program claim. |
| NRC Safety Culture Policy Statement (nine traits) | https://www.nrc.gov/about-nrc/safety-culture/sc-policy-statement | Supporting | verified-public | Public safety-culture traits: questioning attitude, personal accountability, environment for raising concerns, decision-making. | High | Concept lineage for charter integrity/questioning/stop-work articles; pure .gov; preferred over member-only trait documents. |
| SUBSAFE program (public NAVSEA history) | https://www.navsea.navy.mil/ | Supporting | supporting-context | Quality program after the USS Thresher loss; five pillars: work discipline, material control, documentation, compliance verification, culture. | Medium-high | Concept lineage for `critical-systems.md` Tier 0 framing; history/public-affairs sources only; no program claim. |
| Navy "Get Real, Get Better" / Culture of Excellence (public Navy) | https://www.mynavyhr.navy.mil/ | Supporting | supporting-context | Honest self-assessment: actual vs standard condition, where red, root cause, owner, verify improvement. | Medium | Concept lineage for the Get-Real retro structure in `learning-from-experience`; public Navy framing; no program claim. |
| Naval Doctrine Publications NDP-1 / NDP-6 (mission command) | https://www.govinfo.gov/ | Supporting | supporting-context | Decentralized execution by commander's intent; act on purpose when the plan changes; disciplined initiative; mutual trust. | Medium-high | Concept lineage for "authority to information" and clarity-as-alignment; public doctrine; no program claim. |
| David Marquet, intent-based leadership / leader-leader (Turn the Ship Around!, Leadership Is Language) | https://davidmarquet.com/ | Supporting | supporting-context | Push authority to the information; the "I intend to" ladder; leaders create leaders; control + competence + clarity. | High | Concept inspiration only, paraphrased — NOT direct template lineage; the books are copyrighted. Listed on `do-not-cite-directly.md`. |
| Google SRE book (free public edition) | https://sre.google/books/ | Supporting | verified-public | SLOs, error budgets, incident response, control loops; the 100%-reliability caution. | High | Supporting context for `incident-response.md`; reliability framing only; no program claim. |
| DORA / State of DevOps research | https://dora.dev/ | Supporting | verified-public | Delivery metrics (lead time, deploy frequency, change fail rate, recovery time); warning against gaming metrics; AI as amplifier. | High | Concept lineage for the metrics-with-cautions note; metrics framing only; no dashboard claim. |

These sources direct how work is led and how teams stay honest. They do not add governance, CI, supply-chain, or compliance machinery, and David Marquet's books are paraphrased as inspiration only, never reproduced or used as template lineage.

---

## Tier 9 — Context-Engineering Mechanics Sources

These sources shape how we budget, order, compress, and retrieve an agent's context window,
and how we name context failure modes. They are supporting context only. The doctrine built
from them — `docs/02-operating-system/context-window-discipline.md` — is an authored synthesis and
tool-agnostic. Benchmark numbers from these papers are their claims on their benchmarks, not
promises about any workload. No compliance claim is made.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| Anthropic, Effective context engineering for AI agents | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Supporting | supporting-context | Attention budget; context rot; smallest set of high-signal tokens; compaction, structured notes, sub-agents; just-in-time retrieval. | High | Concept lineage for context-window discipline and context-pack budgets; no compliance claim. |
| LangChain context-engineering documentation | https://docs.langchain.com/oss/python/langchain/context-engineering | Supporting | supporting-context | Context lifetimes (runtime config vs per-run state vs cross-run store); write/select/compress/isolate strategies; model vs tool vs lifecycle context. | High | Lifetime-separation vocabulary in `context-window-discipline.md`; no framework dependency or compliance claim. |
| Trivedi & Schmitt, "Does Code Cleanliness Affect Coding Agents? A Controlled Minimal-Pair Study" (arXiv:2605.20049) | https://arxiv.org/abs/2605.20049 | Supporting | public-url-needed | Minimal-pair protocol (repositories matched on architecture, dependencies, and external behavior, differing in static-analysis violations and cognitive complexity). Across 660 trials on 33 tasks over six pairs, code cleanliness left pass rate unchanged (<1% difference) while reducing tokens ~7–8%, reasoning effort ~11%, and already-edited-file revisits ~34%. | Medium | Empirical support for the cleanliness-as-context-cost subsection in `../02-operating-system/token-burn-control.md` and the retrieval-cost bullet in `context-window-discipline.md`. **Authors are affiliated with SonarSource, a code-quality vendor whose product the finding favors** — disclose at every citation. One agent, six pairs, their benchmark; a cost-and-attention result, explicitly **not** a capability or pass-rate improvement. No efficacy or compliance claim. |
| Neo4j, What is context engineering in AI agents? A practical guide | https://neo4j.com/blog/agentic-ai/what-is-context-engineering/ | Supporting | supporting-context | Select/structure/deliver framing; traceable retrieval paths (graph traversals as citable evidence). | Medium-high | Background framing only; no graph-database dependency. |
| Breunig, How Long Contexts Fail | https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html | Supporting | supporting-context | Failure-mode taxonomy: context poisoning, distraction, confusion, clash. | High | Failure-mode names in `context-window-discipline.md`; no compliance claim. |
| Chroma, Context Rot research report | https://research.trychroma.com/context-rot | Supporting | supporting-context | Measured recall degradation as input token count grows, even on simple tasks. | High | Evidence behind the finite-context premise; no compliance claim. |
| Liu et al., Lost in the Middle (arXiv 2307.03172, TACL) | https://arxiv.org/abs/2307.03172 | Supporting | verified-public | Position effects: recall is strongest at the start and end of long contexts, weakest in the middle. | High | Lineage for placement-and-ordering rules; no compliance claim. |
| Agentic Context Engineering (ACE) (arXiv 2510.04618) | https://arxiv.org/abs/2510.04618 | Supporting | verified-public | Contexts as evolving playbooks; names brevity bias and context collapse; incremental delta updates beat wholesale rewrites. | High | Lineage for the append-only-deltas rule on durable records; no compliance claim. |
| LLMLingua family (LLMLingua / LongLLMLingua / LLMLingua-2) | https://github.com/microsoft/LLMLingua | Supporting | supporting-context | Prompt compression up to ~20x on benchmarks with small accuracy loss; query-aware reordering for long contexts. | High | Evidence that prose compresses well; caveat lineage for compress-with-care; no tooling dependency. |
| cAST: structural chunking via Abstract Syntax Tree (arXiv 2506.15655) | https://arxiv.org/abs/2506.15655 | Supporting | verified-public | AST-aligned chunking (one function/class per retrieval unit) improves code retrieval and generation. | High | Lineage for retrieve-code-by-structure guidance; no indexing-stack requirement. |
| LongCodeZip (arXiv 2510.00446) | https://arxiv.org/abs/2510.00446 | Supporting | verified-public | Function/block-boundary code compression; much lower safe compression ratios for code than for prose. | High | Caveat lineage: code and exact logic are loss-sensitive under compression; no compliance claim. |
| OpenAI Codex, AGENTS.md guide | https://developers.openai.com/codex/guides/agents-md | Supporting | verified-public | Codex discovers layered `AGENTS.md` guidance from global and project scopes, with nearer files overriding earlier guidance and a default project-doc byte limit. | High | Concept lineage for naming loaded instruction files and precedence in context packs; no tool dependency or endorsement claim. |
| Anthropic Claude Code, memory and CLAUDE.md docs | https://code.claude.com/docs/en/memory | Supporting | verified-public | Claude Code loads `CLAUDE.md` (plus its imports and rules) as project memory; `AGENTS.md` is folded in only when imported or pulled in by `/init`, not read on its own. | High | Concept lineage for treating persistent agent instructions as controlled context, and for recording which file actually wins; no tool dependency or endorsement claim. |
| GitHub Copilot, repository custom instructions | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions | Supporting | verified-public | Repository custom instructions give Copilot project context for understanding, building, testing, and validating changes; GitHub also documents path-specific instruction precedence for `AGENTS.md`. | High | Concept lineage for recording which repo-level agent instructions are in force; no tool dependency or endorsement claim. |
| Awesome-Context-Engineering (Meirtz), survey + arXiv paper | https://github.com/Meirtz/Awesome-Context-Engineering | Supporting | verified-public | Public survey/taxonomy: a context payload decomposed into instructions, knowledge, tools, memory, state, and query; curated memory-system, retrieval, context-scaling, and observability literature. | Medium-high | Concept lineage for the payload-component lens in `context-packs.md` and the production-memory pointer in `durable-memory.md`; named as a peer project in `../01-field-guide/context-engineering-literature-crosswalk.md`; no endorsement or compliance claim. |
| context-engineering-intro (coleam00), PRP template | https://github.com/coleam00/context-engineering-intro | Supporting | verified-public | MIT-licensed template: the Product Requirements Prompt (PRP) loop — research the codebase into a complete blueprint, then execute it against runnable validation gates with self-correction. | Medium | Concept lineage for the "Blueprint and execute" workflow-catalog entry in `../../WORKFLOWS.md`; named as a peer project in `../01-field-guide/context-engineering-literature-crosswalk.md`; no endorsement or compliance claim. |

These sources shape how an agent's working context is budgeted and kept honest. Nothing more.
They add no framework, vendor, or database dependency, and no governance or compliance machinery.

---

## Tier 10 — Project- and AI-Governance Background (named only)

These PMI publications are **paywalled** and are named as **background only** — to help
project-management-literate and enterprise adopters orient. Nothing is derived from them, no text
is reproduced, and no compliance, conformance, certification, PMP, or endorsement claim is made.
The bridge doc is `docs/01-field-guide/pmbok-pmi-ai-crosswalk.md`; it explicitly frames the
relationship as a *rhyme*, not a compliance matrix. PMI is also listed under "Excluded as Direct
Template Lineage" below.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| PMBOK® Guide (6th/7th/8th editions) | https://www.pmi.org/standards/pmbok | Context-only | excluded-direct | Public framing of principles, performance domains, tailoring, and logs/registers that this repo's independent practice rhymes with. | Medium | Named background only in the crosswalk doc; no template lineage, no compliance claim. |
| PMI Standard for AI in Portfolio, Program, and Project Management (2026) | https://www.pmi.org/standards/artificial-intelligence | Context-only | excluded-direct | Public framing of human-in-the-loop AI governance, risk, ethics, data quality, stakeholders, and value for AI project work. | Medium | Named background only in the crosswalk + enterprise-rollout docs; no compliance/conformance claim. |

---

## Tier 11 — Practitioner Context-Engineering Collections

These are public, community-maintained collections and curricula on prompt and context engineering.
They are **secondary / aggregator sources**: useful for orienting in the field and for the ideas
they surface, but **not direct template lineage**. This repo derives no template or wording from
them and claims no lineage to any standard *they* cite. They inform
[`../01-field-guide/context-engineering-landscape.md`](../01-field-guide/context-engineering-landscape.md),
[`../05-reference/reasoning-techniques.md`](../05-reference/reasoning-techniques.md), and
[`../02-operating-system/evaluation-integrity.md`](../02-operating-system/evaluation-integrity.md).
Where they name specific tools or frameworks, those stay **landscape only** (see the tool-posture
rule in the landscape doc). No compliance claim is made.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| dair-ai, Prompt Engineering Guide | https://github.com/dair-ai/Prompt-Engineering-Guide | Supporting | supporting-context | Public prompting-technique taxonomy (zero/few-shot, CoT, self-consistency, generated-knowledge, ReAct, PAL) and judge/bias-mitigation findings (distribution balance, exemplar ordering). | Medium-high | Concept lineage for `reasoning-techniques.md` and the judge-bias taxonomy in `evaluation-integrity.md`; secondary source, no template lineage. |
| Meirtz, Awesome-Context-Engineering (arXiv 2507.13334) | https://github.com/Meirtz/Awesome-Context-Engineering | Supporting | supporting-context | Survey framing: context-as-optimization definition, "context failures are the bottleneck," RAG/memory taxonomies, agent-interop protocols (MCP/A2A/AG-UI). | Medium | Background framing for the landscape doc; survey/aggregator, no template lineage. |
| muratcankoylan, Agent-Skills-for-Context-Engineering | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering | Supporting | supporting-context | Skill anti-overlap routing; harness surface classification (locked/editable/append-only/human-controlled); LLM-judge bias taxonomy and process-reward framing. | Medium-high | Concept lineage for surface classification in `agent-authority-model.md`, judge biases in `evaluation-integrity.md`, and skill routing in `../05-reference/skill-authoring-contract.md`; no template lineage. |
| NeoLabHQ, context-engineering-kit | https://github.com/NeoLabHQ/context-engineering-kit | Supporting | supporting-context | Quantified reliability×token-cost tiers; spec-driven / subagent-driven development; reflexion, meta-judge, process-reward patterns. | Medium | Illustrative external evidence for the reliability/cost framing in the comparison study; reflexion caveat in `reasoning-techniques.md`; benchmark numbers are theirs, not restated as ours. |
| jasontang-ai, Context-Engineering | https://github.com/jasontang-ai/Context-Engineering | Context-only | supporting-context | Progressive curriculum (atoms→molecules→cells→organs) plus speculative "field-physics" framing (neural fields, attractor dynamics, quantum semantics). | Low-medium | Named as landscape; the speculative framing is **explicitly declined** in the landscape doc §3. No template lineage. |
| Boris Cherny (Head of Claude Code, Anthropic), five work archetypes (posted 2026-06-28) | https://x.com/bcherny/status/2071379474277613732 | Supporting | supporting-context | Prototyper / Builder / Sweeper / Grower / Maintainer as patterns of work rather than job titles; they cross the org chart, and the mix shifts by product phase. | Medium | Concept lineage for `../02-operating-system/archetype-lens.md`, attributed by name and paraphrased. **Primary but low-stability source** (social-media post; a Threads mirror exists at https://www.threads.com/@boris_cherny/post/DaJgVFVj2PB/). The mapping from archetype to characteristic drift, mode floor, and skill set is this repository's authored extension and must not be attributed to the original. No template lineage, no compliance claim. |

---

## Context-Only / Do-Not-Overweight Sources

| Source family | Classification | Status | Why |
|---|---|---|---|
| DOE-STD-3007 criticality safety | Supporting | verified-public | Strong evaluation discipline, but nuclear-domain-specific. |
| 10 CFR 50.59 / 50.65 | Context-only | supporting-context | Useful change/maintenance analogies; too power-reactor-specific for core UX. |
| NRC generic letters / information notices on counterfeit items | Context-only | supporting-context | Useful dependency-trust analogies; not core template lineage. |
| Natural phenomena hazards standards | Context-only | supporting-context | Useful hazard mindset; not first-wave source lineage. |

---

## Excluded as Direct Template Lineage

See `do-not-cite-directly.md`. In short:

```text
ASME NQA-1
EPRI reports
IEEE standards
IEC standards
ISO standards
ANSI/ANS standards
NEI documents
PMI publications (PMBOK Guide; the PMI Standard for AI in Portfolio, Program, and Project Management)
proprietary QA/procurement/utility manuals
```

You may mention these only as broad industry background, and only when they are public and you need to. They must not shape the structure or the wording of any template.

Regulated and quality-managed industries often use formal consensus standards such as ASME NQA-1 and ISO 9001 for quality assurance, assessment, and corrective action. Nuclear-grade names them only as high-level industry background; it does not reproduce them, derive any template or workflow from them, and claims no compliance or lineage with them. The assessment-and-correction concepts in this repo trace instead to the public sources above (10 CFR 830 Subpart A, the DOE QA page, and DOE O 413.3B).
