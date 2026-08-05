# Basis: Matt skill lifecycle and flow adaptation

## Change context

- Slug: `matt-skill-lifecycle-and-flow`
- Related risk record: `risk.md`
- Owner: FlyFission maintainer
- Date: 2026-08-05
- Decision: whether this branch is ready for PR review.

## Mission / need

Nuclear-grade has stronger evidence, custody, decision, and release controls than the compared external skill system. It needs a smaller and more explicit skill-product surface: prerequisite discovery before classification, lifecycle and invocation ownership, executable catalog routing evaluation, aggregate context budgets, a measured compact-body pilot, and concrete engineering on-ramps inside the existing control loop.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| Evidence and decision receipts remain intact | They are Nuclear-grade's differentiated assurance spine | skill contract and decision-receipt tests |
| Promoted distribution is explicit | Beta/deprecated material must not silently auto-route | lifecycle and package parity tests |
| Routing evidence is not overstated | Manifest validity is not live retrieval evidence | scorer output, docs boundary, no efficacy claim |
| Existing installs remain compatible | Current skill and command surfaces are public | generated projection and package tests |
| Human merge/release authority remains separate | PR creation is not release authorization | `ship.md` and PR wording |

## Unacceptable outcomes

| Unacceptable outcome | Hazard kind | Consequence | Prevent / detect / mitigate |
|---|---|---|---|
| Read-only discovery is blocked by the router | insufficiency | risk classification is guessed from thin context | router contract and regression test |
| A beta or deprecated skill ships by default | fault | unproven skill enters routing surface | lifecycle validator and package tests |
| Routing scorer ignores extra loaded skills | fault | over-triggering appears successful | exact-set metrics and adversarial tests |
| Aggregate context grows through many compliant files | insufficiency | catalog becomes cognitively expensive | product-level token budgets and mutation tests |
| Compact skill drops a decision control | fault | context savings weaken evidence or authority | old/new contract checks, command parity, behavior fixtures |
| Workflow additions create a second operating system | insufficiency | agents face more ceremony and aliases | one crosswalk; adapters inside existing beats |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Status | Basis | Invalidation trigger | Owner |
|---|---|---|---|---|
| JSON is the safest dependency-free semantic registry | assumption | Python stdlib and cross-host readability | a supported host requires YAML-only metadata | maintainer |
| Existing YAML lists can remain compatibility projections | assumption | preserves current consumers | a projection cannot be checked exactly | maintainer |
| No current main skill is beta/deprecated | fact | frozen catalog inspection | branch adds a new status | maintainer |
| Live model routing is manual/release-candidate evidence, not deterministic CI | constraint | API cost and nondeterminism | stable hermetic runner becomes available | maintainer |
| Only a compact pilot is in scope | constraint | PR reviewability and PR #85 limits | user requests full rollout after pilot evidence | maintainer |

## Interfaces and trust boundaries

- Internal interfaces: catalog schema, CLI install profiles, command generator, token report, routing scorer, skill contract, public workflow templates.
- External services: GitHub push/PR/CI after local verification.
- Human approval boundaries: maintainer reviews and merges; this branch may only prepare and request review.
- AI/model authority: implementation agents may edit the isolated branch and run local checks; they may not merge, release, or claim independent human validation.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | The router permits bounded read-only preflight and requires mode declaration before mutation or external side effect. | evidence-led classification | revised skill, tests, docs | focused and full pytest |
| REQ-002 | One host-neutral registry records status, invocation, role, command, and path for every skill. | explicit invocation/lifecycle | `skill-catalog.json` plus validator | lifecycle tests and doctor |
| REQ-003 | Only promoted skills enter default/full installs and plugin-discoverable promoted paths; beta/deprecated states have fail-closed rules. | no catalog leakage | lifecycle helpers and package tests | synthetic negative tests |
| REQ-004 | Catalog routing scenarios compare exact expected skill sets and report precision, recall, exact matches, false positives, and misses. | retrieval separate from behavior | executable scorer and overlap scenarios | scorer tests and manifest run |
| REQ-005 | Aggregate profile/catalog budgets complement per-file maxima. | product context economy | token report and budget gates | mutation tests and live token run |
| REQ-006 | A compact pilot uses progressive disclosure without changing command semantics or decision receipts. | measured compression | command assets/references and generator fallback | command parity, token delta, output fixtures |
| REQ-007 | Existing workflow gains prototype, decision-frontier, tracer-bullet/TDD, two-axis review, phase-boundary context, and deep-seam on-ramps without new mandatory phases. | concrete build mechanics | doctrine/template edits | public-doc tests and review |
| REQ-008 | The eight control points, eleven beats, PRO/PROVE, and work phases have one explicit crosswalk. | reduce translation overhead | `WORKFLOWS.md` crosswalk | public-doc test |
| REQ-009 | Every canonical/generated/documented surface remains synchronized and current package checks pass. | release integrity | projection tests and full gate | full pre-PR commands |

## Design outline

- Architecture: `skill_catalog.py` is the deep module for parsing and validating registry semantics. Existing YAML surfaces remain compatibility projections checked against it.
- Components: lifecycle registry, CLI filters, command generator, routing scorer, token budget extension, compact skill assets, workflow templates.
- Error handling: malformed/duplicate IDs, invalid statuses/invocations/roles, missing replacements, unknown commands, unknown routed skills, incomplete observed runs, and budget violations fail with diagnostics.
- Testing strategy: RED tests for every new failure path, focused tests during implementation, full suite after final edit, independent Standards and Spec reviews.

## Required links

- `risk.md`
- `plan.md`
- `trace.md`
- `verification.md`
- `ship.md`

## Exit criteria

- REQ-001 through REQ-009 are traced and verified or explicitly blocked.
- No public statement treats structural checks as proof of engineering adequacy, safety, compliance, or efficacy.

## Source-lineage note

The design selectively adapts public skill-workflow patterns mapped in `docs/00-standards-foundation/source-map.md` and retains Nuclear-grade's existing evidence-custody and authority boundaries. No compliance or formal assurance claim is made.
