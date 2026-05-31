# Core Source Rationale

**Purpose:** Explain why Nuclear-grade starts from this public-source foundation, and how each source family helps build a software-native operating model.

Nuclear-grade is not trying to recreate nuclear compliance. It takes the lasting engineering habits that make high-stakes work reliable. Then it turns those habits into light, Git-native software workflows.

---

## The foundation thesis

The right foundation is not one standard. It is a stack of public sources, each layered on the last:

```text
DOE/CFR → design basis, QA, configuration, safety-basis, project gates
NRC software guidance → nuclear software lifecycle, requirements, V&V, CM, test evidence
NIST/CISA → modern cyber, software, AI, and supply-chain risk
NASA → high-reliability software/systems engineering and lessons learned
OpenSSF/OWASP/SLSA → practical open software security and supply-chain evidence
```

This mix is strong because each family covers a different way things go wrong.

---

## Why DOE/CFR sources are core

DOE and CFR sources give Nuclear-grade its backbone for high-stakes engineering:

- **10 CFR 830 Subpart A** anchors public QA ideas: management responsibility, work processes, records, assessment, and correction.
- **10 CFR 830 Subpart B** anchors safety-basis logic: find the hazards, set the controls, and keep the authorization and evidence in order.
- **10 CFR 50 Appendix B** gives public nuclear QA criteria that readers can check without paying for a standard.
- **DOE public quality-assurance pages and 10 CFR 830 Subpart A** add DOE quality-program background, including graded quality and software quality ideas. They do this without turning Nuclear-grade into a DOE compliance workflow.
- **DOE-STD-1073** gives the spine for keeping the approved version under control: the approved configuration, the design requirements, configuration drift, and change impact.
- **DOE-STD-1189** gives the design lifecycle: build safety in early, mature the design basis over time, and line up project, design, and safety work.
- **DOE-STD-3024** gives the logic for design descriptions (FDD and SDD): requirements, basis, design features, interfaces, evidence, and depth that scales with risk.
- **DOE-STD-3009** gives the logic for hazard analysis and picking controls: what can go wrong, how bad it is, which controls matter, and what evidence backs them.
- **DOE O 413.3B public project-management materials** give the logic for project gates: mission need, requirements, baselines, maturity, and independent review. NNSA PRD materials stay discovery and context only until an official public source is on record.

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

The NRC software RG and NUREG group is the clearest public bridge between nuclear expectations and real software work.

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

This keeps Nuclear-grade from being just "nuclear-flavored process." It ties the software pieces to public nuclear software assurance references.

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

Nuclear-grade must work for modern enterprise software, not just nuclear comparisons.

NIST and CISA sources add:

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

NIST SP 800-161 matters most here. Dependency trust is one of the repo's most useful and most widely shared ideas.

---

## Why NASA sources are core

NASA sources add public, high-reliability software and systems engineering practice. They do this without needing a nuclear-specific compliance frame.

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

NASA is also easier for most GitHub readers to approach than nuclear-only sources.

---

## Why OpenSSF/OWASP/SLSA sources are supporting-core

These sources make Nuclear-grade useful right away for GitHub-native development.

They add:

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

They should back the practical templates and validators. DOE, NRC, NASA, and NIST supply the deeper doctrine.

---

## Why paywalled/proprietary standards are excluded as direct inputs

Nuclear-grade must be public, linkable, and safe for GitHub readers.

So it must not build public templates from:

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

This is not because those sources do not matter in industry. They do. It is because a public teaching repo needs source lineage that anyone can check, and it must not copy or closely reword proprietary structures.

---

## Why this foundation is sufficient to build outward

The foundation covers the main parts of enterprise-grade software rigor:

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

No single source family covers all of this. The full stack does.

---

## Guardrail for future expansion

Before you add a source to the core foundation, ask:

1. Is it public, open, and linkable?
2. Does it cover a foundational part that nothing else covers yet?
3. Does it change the operating model in a real way?
4. Can the repo translate it without claiming compliance?
5. Does it cut risk or improve decisions for software teams?

If the answer is no, keep it as supporting or context, or leave it out.
