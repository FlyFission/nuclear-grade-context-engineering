# Artifact Dependency Graph

**Purpose:** Show the order in which the Nuclear-grade records depend on each other. This keeps each template from becoming a lone form with no link to the rest.

**Main idea:** Nuclear-grade is the steering system for serious AI software work. It puts the power of AI and large language models (LLMs) to good use through a few steps. State the design reasons. Keep the approved version under control. Trace each claim to its proof. Run verification and validation (V&V). Check that the work is ready to ship. It does all this without wasting tokens or adding busywork.

**Limits:** This is a teaching model. It draws on public sources you can link to. It is not a compliance framework for DOE, NRC, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, NASA, NIST, CISA, OpenSSF, OWASP, or SLSA.

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

The chain runs one way. Later records should point back to the reasons they rest on. And lessons from real operation (OPEX) should feed forward into future changes.


---

## 2. Packet-level artifact graph

### Quick mode

```text
risk.md
└── proof.md
```

Use Quick mode when a change is low stakes and easy to undo. It must be easy to check. And it must not change outside trust, how data is handled, permissions, or how the system runs.

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

Use Standard mode when the change touches any of these: what users see, important dependencies, how the system runs, how data is handled, tool permissions, model or prompt behavior, or long-lived design.

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

Use Nuclear mode only when one of these is true: high stakes, high uncertainty, outside trust, an effect you cannot undo, use near regulated work, an agent that acts on its own in important ways, sensitive data, weight for safety or security, or a need to meet enterprise due diligence.

### Activated CM records

```text
controlled-items.md
├── change-impact.md
├── baseline.md
├── variance.md
└── opex.md
```

Use these records for keeping the approved version under control (configuration management, or CM). Reach for them when the key question is not only "what evidence proves this change?" but also "which approved version did we accept, what did it touch, and when must we check it again?"

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
- Writing design descriptions before the risk rating shows why they are needed.
- Building big trace tables for tiny changes instead of linking the few claims that matter.
- Treating a passing test suite as proof you are ready to ship, with no rollback plan, no monitoring, and no listed assumptions.
- Asking an AI agent to read every source document instead of the packet and the short source-map excerpt that apply.
- Filling in evidence after the release instead of gathering it as the work goes.

---

## 6. Source-lineage note

This graph is an original operating model built for software. Its ideas come from these public sources.

- Keeping the approved version under control and controlling design changes: [DOE-STD-1073-2016](https://www.energy.gov/ehss/articles/doe-std-1073-2016).
- Building safety into the design as the work moves through stages: [DOE-STD-1189-2016](https://www.energy.gov/ehss/articles/doe-std-1189-2016).
- Writing design descriptions: [DOE-STD-3024-2011](https://www.energy.gov/ehss/articles/doe-std-3024-2011).
- Public ideas about a safety basis and quality assurance (QA): [10 CFR 830 Subpart A](https://www.ecfr.gov/current/title-10/chapter-III/part-830/subpart-A), [10 CFR 830 Subpart B](https://www.ecfr.gov/current/title-10/chapter-III/part-830/subpart-B), and [10 CFR 50 Appendix B](https://www.ecfr.gov/current/title-10/chapter-I/part-50/appendix-Appendix%20B%20to%20Part%2050).
- Public nuclear software ideas about the software lifecycle, verification and validation, and keeping the approved version under control: NRC RG 1.168–1.173 and RG 1.187 landing pages listed in `source-map.md`.
- Modern software, cyber, and supply-chain sources: [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final), [NIST SP 800-161](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final), [CISA Secure by Design](https://www.cisa.gov/securebydesign), [CISA SBOM](https://www.cisa.gov/sbom), [SLSA](https://slsa.dev/), and [OpenSSF Scorecard](https://github.com/ossf/scorecard).
- High-reliability software and systems sources: [NASA Software Engineering Handbook](https://swehb.nasa.gov/), [NASA-STD-8739.8](https://standards.nasa.gov/standard/nasa/nasa-std-87398), and [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/nasa-systems-engineering-handbook/).

Do not cite this graph from the paid or proprietary standards listed in `do-not-cite-directly.md`, and do not build it on them.
