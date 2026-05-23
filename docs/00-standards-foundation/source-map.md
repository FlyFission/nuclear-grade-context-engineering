# Source Map

**Purpose:** Identify the public, open, linkable sources that Nuclear-grade may cite directly or use as source lineage for original software workflows.

**Repo posture:** Nuclear-grade is an educational, public-source-inspired software engineering methodology. It does not claim compliance with DOE, NRC, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, NASA, NIST, CISA, OpenSSF, OWASP, or any other framework.

**Use rule:** A source can shape public templates only when it is public/open/linkable and the resulting workflow is original, software-native, and non-compliance-claiming.

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

Confidence fields are about source-family fit for this repo, not compliance adequacy.

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
| DOE-HDBK-1028-2009, Human Performance Improvement Handbook | https://www.energy.gov/ehss/articles/doe-hdbk-1028-2009 | Core | verified-public | Human performance tools: questioning attitude, pause when unsure, validate assumptions, reviews, operating experience, change management. | High | Source lineage for Question phase and questioning-attitude skill; no HPI program or compliance claim. |
| DOE-STD-1073-2016, Configuration Management | https://www.energy.gov/ehss/articles/doe-std-1073-2016 | Core | verified-public | Configuration discipline, design requirements, approved configuration, change impact, drift. | High | One of the primary translation anchors. |
| DOE-STD-1189-2016, Integration of Safety into Design | https://www.energy.gov/ehss/articles/doe-std-1189-2016 | Core | verified-public | Lifecycle integration, safety/design/project gates, early basis, design maturation. | High | Source for lifecycle/gate doctrine. |
| DOE-STD-3024-2011, Content of SDDs | https://www.energy.gov/ehss/articles/doe-std-3024-2011 | Core | verified-public | FDD/SDD logic: requirements, basis, interfaces, design features, graded rigor. | High | Source for design description analogies. |
| DOE-STD-3009-2014, Nonreactor Nuclear Facility DSA | https://www.energy.gov/ehss/articles/doe-std-3009-2014 | Core | verified-public | Hazard analysis, accident/failure analysis, control selection, DSA/TSR style evidence logic. | High | Source for failure-mode and assurance-case concepts. |
| DOE O 413.3B, Program and Project Management for Capital Assets | https://www.energy.gov/projectmanagement/directives | Core | verified-public | Critical decisions, project lifecycle, independent reviews, baseline maturity. | Medium-high | Use for stage-gate analogy without compliance claims. |
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

**Important:** NRC software sources are the most direct public nuclear-to-software bridge. They should be prominent in source lineage, but templates must remain original and non-compliance-claiming.

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

These may be mentioned only as high-level industry context when public and necessary. They must not shape template structure or language.
