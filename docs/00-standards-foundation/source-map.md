# Source Map

**Purpose:** List the public, open, linkable sources that Nuclear-grade may cite directly. These are also the sources whose ideas can shape its original software workflows.

**Repo posture:** Nuclear-grade is a teaching method for software engineering. It is built on public sources. It does not claim to meet DOE, NRC, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, NASA, NIST, CISA, OpenSSF, OWASP, or any other framework.

**Use rule:** A source can shape public templates only when two things are true. First, it is public, open, and linkable. Second, the workflow we build from it is original, made for software, and claims no compliance.

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

---

## Tier 4 - NASA High-Reliability Software and Systems Anchors

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| NASA Software Engineering Handbook / NASA-HDBK-2203 | https://swehb.nasa.gov/ | Core | verified-public | Practical public software lifecycle guidance. | High | Requirements, design, testing, reviews, lifecycle. |
| NPR 7150.2, NASA Software Engineering Requirements | https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2 | Core | verified-public | Software engineering requirements and lifecycle. | High | Source for software lifecycle concepts. |
| NASA-STD-8739.8, Software Assurance and Software Safety | https://standards.nasa.gov/standard/nasa/nasa-std-87398 | Core | verified-public | Software assurance and software safety. | High | Assurance/evidence/independent review concepts. |
| NASA Systems Engineering Handbook | https://www.nasa.gov/reference/nasa-systems-engineering-handbook/ | Core | verified-public | Requirements, interfaces, V&V, technical reviews. | High | Systems thinking and lifecycle. |
| NASA Lessons Learned | https://llis.nasa.gov/ | Supporting-core | verified-public | OPEX/corrective-action learning loop. | High | OPEX and post-release learning. |

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

These sources shape how we attack-test agents, trace what they do, and profile them. They are supporting context only. The workflows we build from them are original and work with any tool. You do not need NIM, a GPU, W&B, or NeMo to use the skills and templates.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| NVIDIA Safety for Agentic AI blueprint | https://github.com/NVIDIA-AI-Blueprints/safety-for-agentic-ai | Supporting | supporting-context | Adversarial risk taxonomy (prompt injection, jailbreak, authority escalation, tool misuse, unsafe output, retrieval poisoning, data exfiltration); evaluate → harden → re-evaluate lifecycle; before/after posture records. | High | Conceptual influence for `stress-testing-agent-changes` skill and adversarial class vocabulary; no compliance, penetration-test, or safety certification claim. |
| Garak LLM vulnerability scanner | https://github.com/leondz/garak | Supporting | supporting-context | Open-source probe-based adversarial testing of LLMs; risk categories; reproducible vulnerability scan reports. | High | Adversarial class taxonomy; no compliance claim. |
| NVIDIA NeMo Guardrails | https://github.com/NVIDIA-NeMo/Guardrails | Supporting | supporting-context | Runtime guardrail orchestration: input, output, retrieval, dialog, and topic rails; jailbreak detection; content safety; configuration as code. | High | Rail-type vocabulary for adversarial class selection and agent authority model; no compliance claim. |
| W&B Weave traceability | https://wandb.ai/site/weave | Supporting | supporting-context | Trace-tree observability: span-per-call, auto-logging of inputs/outputs/metadata/latency/cost, audit lineage, reproducibility, evaluation loops. | High | Conceptual influence for `recording-what-an-agent-did` skill and trace-as-evidence vocabulary; no compliance or audit-certification claim. |
| NVIDIA NeMo Agent Toolkit (AIQ) | https://github.com/NVIDIA/NeMo-Agent-Toolkit | Supporting | supporting-context | Framework-agnostic agent profiling (token/latency/cost per step to workflow level), offline evaluation harness, OpenTelemetry-compatible observability exporters (Phoenix, Weave, Langfuse, LangSmith). | High | Reference model for evidence-spine detail and skill-evaluation rubric; influence for future runnable `evals/` suite; no compliance claim. |
| OpenTelemetry distributed tracing | https://opentelemetry.io/ | Supporting | supporting-context | Vendor-neutral structured spans, parent-child trace relationships, context propagation, semantic conventions for LLM/agent instrumentation. | High | Structured span vocabulary for `recording-what-an-agent-did` and `execution-trace.md`; no compliance claim. |

---

## Tier 7 — Project Structuring, Decomposition & Agentic-Folder Architecture Sources

These sources shape how we break work into pieces and how we lay out folders and files. They are supporting context only. The workflows we build from them are original, made for software, and work with any tool. The main DOE Work Breakdown Structure Handbook is listed in Tier 1. We claim no compliance with DOE, DoD, NASA, PMI, GAO, NARA, NIST, INCOSE, or ISO.

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

These sources shape how people and AI agents are directed, how authority and intent are handled, and how teams stay honest and recover from failure. They are concept lineage only. The workflows built from them are original and software-native. We claim no compliance with any program, and we reproduce no proprietary book.

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
from them — `docs/02-operating-system/context-window-discipline.md` — is original and
tool-agnostic. Benchmark numbers from these papers are their claims on their benchmarks, not
promises about any workload. No compliance claim is made.

| Source | Public link | Classification | Status | Role in Nuclear-grade | Confidence | Direct repo use |
|---|---|---:|---|---|---:|---|
| Anthropic, Effective context engineering for AI agents | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Supporting | supporting-context | Attention budget; context rot; smallest set of high-signal tokens; compaction, structured notes, sub-agents; just-in-time retrieval. | High | Concept lineage for context-window discipline and context-pack budgets; no compliance claim. |
| LangChain context-engineering documentation | https://docs.langchain.com/oss/python/langchain/context-engineering | Supporting | supporting-context | Context lifetimes (runtime config vs per-run state vs cross-run store); write/select/compress/isolate strategies; model vs tool vs lifecycle context. | High | Lifetime-separation vocabulary in `context-window-discipline.md`; no framework dependency or compliance claim. |
| Neo4j, What is context engineering in AI agents? A practical guide | https://neo4j.com/blog/agentic-ai/what-is-context-engineering/ | Supporting | supporting-context | Select/structure/deliver framing; traceable retrieval paths (graph traversals as citable evidence). | Medium-high | Background framing only; no graph-database dependency. |
| Breunig, How Long Contexts Fail | https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html | Supporting | supporting-context | Failure-mode taxonomy: context poisoning, distraction, confusion, clash. | High | Failure-mode names in `context-window-discipline.md`; no compliance claim. |
| Chroma, Context Rot research report | https://research.trychroma.com/context-rot | Supporting | supporting-context | Measured recall degradation as input token count grows, even on simple tasks. | High | Evidence behind the finite-context premise; no compliance claim. |
| Liu et al., Lost in the Middle (arXiv 2307.03172, TACL) | https://arxiv.org/abs/2307.03172 | Supporting | verified-public | Position effects: recall is strongest at the start and end of long contexts, weakest in the middle. | High | Lineage for placement-and-ordering rules; no compliance claim. |
| Agentic Context Engineering (ACE) (arXiv 2510.04618) | https://arxiv.org/abs/2510.04618 | Supporting | verified-public | Contexts as evolving playbooks; names brevity bias and context collapse; incremental delta updates beat wholesale rewrites. | High | Lineage for the append-only-deltas rule on durable records; no compliance claim. |
| LLMLingua family (LLMLingua / LongLLMLingua / LLMLingua-2) | https://github.com/microsoft/LLMLingua | Supporting | supporting-context | Prompt compression up to ~20x on benchmarks with small accuracy loss; query-aware reordering for long contexts. | High | Evidence that prose compresses well; caveat lineage for compress-with-care; no tooling dependency. |
| cAST: structural chunking via Abstract Syntax Tree (arXiv 2506.15655) | https://arxiv.org/abs/2506.15655 | Supporting | verified-public | AST-aligned chunking (one function/class per retrieval unit) improves code retrieval and generation. | High | Lineage for retrieve-code-by-structure guidance; no indexing-stack requirement. |
| LongCodeZip (arXiv 2510.00446) | https://arxiv.org/abs/2510.00446 | Supporting | verified-public | Function/block-boundary code compression; much lower safe compression ratios for code than for prose. | High | Caveat lineage: code and exact logic are loss-sensitive under compression; no compliance claim. |

These sources shape how an agent's working context is budgeted and kept honest. Nothing more.
They add no framework, vendor, or database dependency, and no governance or compliance machinery.

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
proprietary QA/procurement/utility manuals
```

You may mention these only as broad industry background, and only when they are public and you need to. They must not shape the structure or the wording of any template.

Regulated and quality-managed industries often use formal consensus standards such as ASME NQA-1 and ISO 9001 for quality assurance, assessment, and corrective action. Nuclear-grade names them only as high-level industry background; it does not reproduce them, derive any template or workflow from them, and claims no compliance or lineage with them. The assessment-and-correction concepts in this repo trace instead to the public sources above (10 CFR 830 Subpart A, the DOE QA page, and DOE O 413.3B).
