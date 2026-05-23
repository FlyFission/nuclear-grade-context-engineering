# Core Source Rationale

**Purpose:** Explain why Nuclear-grade starts from this public-source foundation and how each source family contributes to a software-native operating model.

Nuclear-grade is not trying to recreate nuclear compliance. It is extracting the durable engineering habits that make high-consequence work reliable, then translating those habits into lightweight, Git-native software workflows.

---

## The foundation thesis

The right foundation is not one standard. It is a layered public-source spine:

```text
DOE/CFR → design basis, QA, configuration, safety-basis, project gates
NRC software guidance → nuclear software lifecycle, requirements, V&V, CM, test evidence
NIST/CISA → modern cyber, software, AI, and supply-chain risk
NASA → high-reliability software/systems engineering and lessons learned
OpenSSF/OWASP/SLSA → practical open software security and supply-chain evidence
```

This combination is strong because each family covers a different failure mode.

---

## Why DOE/CFR sources are core

DOE and CFR sources give Nuclear-grade the high-consequence engineering backbone:

- **10 CFR 830 Subpart A** anchors public QA concepts: management responsibility, work processes, records, assessment, and correction.
- **10 CFR 830 Subpart B** anchors safety-basis logic: identify hazards, define controls, and maintain authorization/evidence discipline.
- **10 CFR 50 Appendix B** provides public nuclear QA criteria that readers can verify without paywalled standards.
- **DOE public quality-assurance pages and 10 CFR 830 Subpart A** add DOE quality-program context, including graded quality and software quality concepts, without turning Nuclear-grade into a DOE compliance workflow.
- **DOE-STD-1073** gives the configuration management spine: approved configuration, design requirements, configuration drift, and change impact.
- **DOE-STD-1189** gives the design lifecycle: integrate safety early, mature design basis over time, and coordinate project/design/safety work.
- **DOE-STD-3024** gives FDD/SDD design-description logic: requirements, basis, design features, interfaces, evidence, and graded depth.
- **DOE-STD-3009** gives hazard analysis and control-selection logic: what can go wrong, how bad, what controls matter, and what evidence supports them.
- **DOE O 413.3B public project-management materials** give project gate logic: mission need, requirements, baselines, maturity, and independent review. NNSA PRD materials remain discovery/context until an official public source is recorded.

Software translation:

```text
design basis
configuration discipline
change impact screening
assumption registers
failure-mode reviews
release readiness evidence
OPEX learning loops
```

---

## Why NRC software sources are core

The NRC software RG/NUREG cluster is the most direct public bridge between nuclear expectations and actual software work.

It covers:

- software requirements;
- software lifecycle;
- software unit testing;
- test documentation;
- configuration management;
- V&V;
- reviews and audits;
- high-integrity software;
- software QA;
- software reliability and safety.

This prevents Nuclear-grade from being merely “nuclear-flavored process.” It grounds the software pieces in public nuclear software assurance references.

Software translation:

```text
requirements-to-tests traceability
verification ledgers
software lifecycle phase gates
independent review by consequence
configuration-controlled evidence
```

---

## Why NIST/CISA sources are core

Nuclear-grade must work for modern enterprise software, not just nuclear analogies.

NIST/CISA sources add:

- secure software development;
- systems security engineering;
- cyber resilience;
- supply-chain risk management;
- AI risk management;
- secure-by-design product accountability;
- vulnerability and SBOM awareness.

Software translation:

```text
dependency trust basis
AI-assisted development controls
secure release readiness
supply-chain evidence
vulnerability revalidation triggers
```

NIST SP 800-161 is especially important because dependency trust is one of the repo's most viral and useful concepts.

---

## Why NASA sources are core

NASA sources add public, high-reliability software and systems engineering practice without requiring nuclear-specific compliance framing.

They support:

- requirements discipline;
- systems engineering;
- technical reviews;
- verification and validation;
- software assurance;
- software safety;
- lessons learned.

Software translation:

```text
technical review packets
assurance evidence
handoff and OPEX records
system-level thinking
```

NASA is also more approachable for broad GitHub readers than nuclear-only sources.

---

## Why OpenSSF/OWASP/SLSA sources are supporting-core

These sources make Nuclear-grade immediately relevant to GitHub-native development.

They contribute:

- build provenance;
- dependency scoring;
- supply-chain consumption practices;
- SBOM structures;
- application security verification;
- maturity models;
- common vulnerability classes.

Software translation:

```text
release evidence
dependency assurance
security verification
provenance-aware shipping
```

They should support practical templates and validators, while DOE/NRC/NASA/NIST provide the deeper doctrine.

---

## Why paywalled/proprietary standards are excluded as direct inputs

Nuclear-grade must be public, linkable, and safe for GitHub readers.

Therefore, it must not derive public templates from:

```text
ASME NQA-1
EPRI reports
IEEE standards
IEC standards
ISO standards
ANSI/ANS standards
NEI documents
proprietary utility manuals
```

This is not because those sources are unimportant in industry. It is because a public educational repo needs verifiable public lineage and must not reproduce or closely paraphrase proprietary structures.

---

## Why this foundation is sufficient to build outward

The foundation covers the major dimensions of enterprise-grade software rigor:

| Dimension | Source family |
|---|---|
| Design basis | DOE-STD-1189, DOE-STD-3024, DOE-STD-3009 |
| Configuration discipline | DOE-STD-1073, NRC RG 1.169 |
| QA/process discipline | 10 CFR 830A, 10 CFR 50 App B, DOE public quality-assurance materials |
| Safety/hazard logic | 10 CFR 830B, DOE-STD-3009, NASA safety/software assurance |
| PRD/project gates | DOE O 413.3B public project-management materials; NNSA PRD context when publicly verified |
| Software lifecycle | NRC RG 1.168–1.173, NASA SWEHB/NPR 7150.2 |
| Cyber/AI/supply chain | NIST/CISA, OpenSSF, OWASP, SLSA |
| OPEX learning | NASA Lessons Learned, DOE operating feedback concepts |

No single source family covers all of this. The stack does.

---

## Guardrail for future expansion

Before adding a source to the core foundation, ask:

1. Is it public/open/linkable?
2. Does it cover a foundational dimension not already covered?
3. Does it materially change the operating model?
4. Can the repo translate it without making compliance claims?
5. Does it reduce risk or improve decisions for software teams?

If not, keep it as supporting/context or exclude it.
