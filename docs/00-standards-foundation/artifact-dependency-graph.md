# Artifact Dependency Graph

**Purpose:** Define the canonical dependency order among Nuclear-grade artifacts so templates do not become isolated forms.

**Thesis:** Nuclear-grade is the control system for frontier AI software engineering. It channels AI/LLM horsepower through design basis, configuration discipline, traceability, verification, and release readiness without token/process waste.

**Boundary:** This is an educational operating model inspired by public, linkable sources. It is not a DOE, NRC, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, NASA, NIST, CISA, OpenSSF, OWASP, or SLSA compliance framework.

---

## 1. Canonical dependency chain

```text
Mission need / change intent
-> consequence classification
-> design basis
-> requirements / protected outcomes
-> controlled items
-> assumptions + operating envelope
-> design features / controls
-> implementation plan
-> dependency trust basis
-> change impact screen
-> verification plan
-> traceability record
-> baseline record
-> release readiness
-> operating signals
-> OPEX / corrective action
-> basis update, re-baseline, or closure
```

The chain is directional: later records should point backward to the basis they depend on, and operating lessons should feed forward into future changes.

---

## 2. Packet-level artifact graph

### Quick mode

```text
risk.md
└── proof.md
```

Use Quick mode when a change is low consequence, reversible, easy to verify, and does not alter external trust, data handling, permissions, or operational behavior.

| Artifact | Depends on | Feeds | Minimum useful version | Exit criteria |
|---|---|---|---|---|
| `risk.md` | Change intent | `proof.md` | One-sentence scope, consequence, reversibility, proof command | Reviewer can see why Quick mode is enough. |
| `proof.md` | `risk.md`, diff | PR/release note | Command/eval/check run plus result | Evidence matches the declared risk. |

### Standard mode

```text
risk.md
├── basis.md
│   ├── plan.md
│   ├── trace.md
│   └── verification.md
└── ship.md
```

Use Standard mode when the change affects user-visible behavior, important dependencies, operational posture, data handling, tool permissions, model/prompt behavior, or durable architecture.

| Artifact | Depends on | Feeds | Minimum useful version | Exit criteria |
|---|---|---|---|---|
| `risk.md` | Change intent | all packet files | consequence, reversibility, exposure, independent-review trigger | Mode selection is justified. |
| `basis.md` | `risk.md`, source map when relevant | plan, trace, verification, ship | mission, unacceptable outcomes, assumptions, constraints | Builder and reviewer share the same design intent. |
| `plan.md` | `basis.md` | implementation | steps, affected files, rollback strategy | Work can proceed without re-discovering scope. |
| `trace.md` | `basis.md`, requirements, implementation | verification, ship | claim → design feature → evidence rows for important claims | No important claim is orphaned. |
| `verification.md` | `basis.md`, `trace.md` | ship | test/eval/review commands, acceptance criteria, results | Evidence is reproducible or gap-labeled. |
| `ship.md` | risk, basis, verification, unresolved gaps | release | baseline, risks, rollback, monitoring, handoff | Release decision is evidence-backed. |

### Nuclear mode

```text
risk.md
├── controlled-glossary.md
├── design-basis.md
│   ├── assumption-register.md
│   ├── product-design-description.md
│   ├── system-design-description.md
│   ├── dependency-trust-basis.md
│   ├── change-impact-screen.md
│   └── traceability.md
├── verification-ledger.md
├── independent-review.md
├── release-readiness.md
├── handoff.md
└── opex.md
```

Use Nuclear mode only when activated by high consequence, high uncertainty, external trust, irreversible impact, regulated-adjacent use, important autonomy, sensitive data, safety/security significance, or enterprise diligence needs.

### Activated CM records

```text
controlled-items.md
├── change-impact.md
├── baseline.md
├── variance.md
└── opex.md
```

Use CM records when the important question is not only "what evidence proves this change?" but "what controlled state is accepted, what did it affect, and when must it be revalidated?"

---

## 3. Artifact activation thresholds

| Trigger | Activated artifacts | Why |
|---|---|---|
| User-visible behavior changes | Standard packet | Preserve intent, acceptance criteria, and release evidence. |
| External API, package, model, SaaS, or data dependency becomes important | `dependency-trust-basis.md` or Standard `basis.md` section | State intended use, trust evidence, compensating controls, and revalidation triggers. |
| AI/agent gains write, execution, network, approval, or data access | Standard packet plus AI-control fields; Nuclear if high consequence | Tool authority must be bounded and independently checked. |
| Requirements could be misunderstood or stale | `basis.md`, `trace.md` | Make claims navigable from need to evidence. |
| Failure is hard to detect, hard to reverse, or high impact | Nuclear packet subset | Stronger basis, independent review, release and OPEX records. |
| Incident, escaped defect, near miss, or eval failure | Incident/OPEX record | Feed lessons back into design basis, tests, monitors, and thresholds. |
| Release affects customers, operations, security posture, or trust claims | `ship.md` or `release-readiness.md` | Ship only when evidence, rollback, monitoring, and handoff are explicit. |
| Prompt, model, tool, dependency, source-lineage, validator, release, or public-doc state becomes trust-bearing | CM records | Preserve accepted state and revalidation triggers. |

---

## 4. Required links by artifact family

| Artifact family | Required backward links | Required forward links |
|---|---|---|
| Risk / classification | change intent, affected assets | selected mode, activated artifacts |
| Basis / design basis | source map if relevant, assumptions, constraints | requirements, design features, verification needs |
| Plan | basis, affected files/components | implementation tasks, rollback path |
| Trace | requirements/protected outcomes, design features | evidence, runtime signal, owner/status |
| Verification | trace rows, acceptance criteria | test/eval result, gap, release decision |
| Baseline | controlled items, impact, verification, review | release readiness, variance, revalidation trigger |
| Ship / release readiness | verification, unresolved risks, baseline | rollback, monitoring, handoff, OPEX trigger |
| OPEX / corrective action | incident/release/runtime signal | basis update, test update, control update |

---

## 5. Overhead traps

- Starting in Nuclear mode by default.
- Writing design descriptions before a risk classification explains why they are needed.
- Building trace matrices for trivial changes instead of linking the few important claims.
- Treating a passing test suite as release readiness without rollback, monitoring, or assumptions.
- Asking an AI agent to read every source document instead of the relevant packet and source-map excerpt.
- Backfilling evidence after release rather than collecting it as the work proceeds.

---

## 6. Source-lineage note

This graph is an original software-native operating model. Its public lineage comes from:

- DOE configuration management and design-control logic: [DOE-STD-1073-2016](https://www.energy.gov/ehss/articles/doe-std-1073-2016).
- DOE safety-in-design lifecycle/gate logic: [DOE-STD-1189-2016](https://www.energy.gov/ehss/articles/doe-std-1189-2016).
- DOE SDD/FDD design-description logic: [DOE-STD-3024-2011](https://www.energy.gov/ehss/articles/doe-std-3024-2011).
- Public nuclear safety-basis/QA concepts: [10 CFR 830 Subpart A](https://www.ecfr.gov/current/title-10/chapter-III/part-830/subpart-A), [10 CFR 830 Subpart B](https://www.ecfr.gov/current/title-10/chapter-III/part-830/subpart-B), and [10 CFR 50 Appendix B](https://www.ecfr.gov/current/title-10/chapter-I/part-50/appendix-Appendix%20B%20to%20Part%2050).
- Public nuclear software lifecycle/V&V/CM source family: NRC RG 1.168–1.173 and RG 1.187 landing pages listed in `source-map.md`.
- Modern software/cyber/supply-chain anchors: [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final), [NIST SP 800-161](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final), [CISA Secure by Design](https://www.cisa.gov/securebydesign), [CISA SBOM](https://www.cisa.gov/sbom), [SLSA](https://slsa.dev/), and [OpenSSF Scorecard](https://github.com/ossf/scorecard).
- High-reliability software/systems anchors: [NASA Software Engineering Handbook](https://swehb.nasa.gov/), [NASA-STD-8739.8](https://standards.nasa.gov/standard/nasa/nasa-std-87398), and [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/nasa-systems-engineering-handbook/).

Do not cite or derive this graph from paywalled/proprietary standards families listed in `do-not-cite-directly.md`.
