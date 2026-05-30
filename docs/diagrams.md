# Nuclear-grade Diagrams

Visual maps of the workflow. These are the canonical source for the diagrams embedded across the public docs; update them here and mirror changes where they are referenced.

Diagrams are Mermaid so they render natively on GitHub, stay diffable in version control, and need no build step. Treat each diagram as a controlled item: when the lifecycle, modes, or skill set change, update the matching diagram in the same change.

---

## 1. Core lifecycle

The full lifecycle. The short launch version is `Question -> Specify -> Execute -> Verify -> Decide`.

```mermaid
flowchart LR
    Q[Question] --> D[Discover] --> S[Specify] --> P[Plan]
    P --> E[Execute] --> V[Verify] --> R[Review]
    R --> Dec{Decide}
    Dec -->|ship / defer| B[Baseline] --> O[Operate] --> L[Learn]
    Dec -->|block| P
    L -.feeds future basis.-> Q
```

---

## 2. Mode decision tree

Which packet mode a change earns. Rigor scales with consequence, not effort tolerance.

```mermaid
flowchart TD
    Start([Change request]) --> Q1{Local, reversible,<br/>obvious proof,<br/>no new trust boundary?}
    Q1 -->|yes| Quick[Quick packet<br/>risk.md + proof.md]
    Q1 -->|no| Q2{User / data / dep /<br/>permission / AI authority /<br/>release consequence?}
    Q2 -->|yes| Standard[Standard packet<br/>6 files]
    Q2 -->|severe, silent,<br/>irreversible, external trust| Strong[Human-reviewed<br/>stronger mode]
    Q2 -->|already went wrong| Incident[Incident pattern]
```

---

## 3. Skill-relationship graph

How the skills compose. `using-nuclear-grade` is the single way in and the router; the main path is the per-change pipeline; the heavier overlays switch on only when the stakes call for them.

```mermaid
flowchart TD
    UNG([using-nuclear-grade<br/>router / entry point])
    UNG --> QA[questioning-attitude]
    QA --> CCR[rating-change-risk]
    CCR -->|controlled config touched| ICI[choosing-what-to-control]
    CCR --> CCP[creating-change-records]
    ICI --> SCI[checking-what-a-change-affects]
    CCP --> PC[proving-claims]
    PC --> RSR[checking-release-readiness]
    RSR --> BC[recording-a-known-good-version]
    BC --> LFO[learning-from-experience]
    LFO -.durable control update.-> QA

    subgraph overlays[heavier overlays - switch on by consequence]
      PAC[briefing-an-agent]
      TOW[handing-off-work]
      SCA[double-checking-before-acting]
      TAE[recording-what-an-agent-did]
      RTA[stress-testing-agent-changes]
      CMD[staying-on-mission]
      RCQ[reviewing-code-quality]
      CSP[closing-stale-packets]
    end

    CCP -.delegate / resume.-> PAC
    PAC --> TOW
    CCP -.critical action.-> SCA
    RSR -.new agent authority.-> RTA
    RSR -.execution path matters.-> TAE
    QA -.long drifting session.-> CMD
    PC -.standards drift in diff.-> RCQ
    LFO -.stale packet sweep.-> CSP
```

---

## 4. Packet artifact-dependency graph

How a Standard packet's records depend on each other. Later records point back to the basis they depend on; operating lessons feed forward into the next change. The text form lives in [`00-standards-foundation/artifact-dependency-graph.md`](00-standards-foundation/artifact-dependency-graph.md).

```mermaid
flowchart TD
    intent[Change intent] --> consequence[Consequence classification]
    consequence --> basis[Design basis<br/>basis.md]
    basis --> items[Controlled items]
    items --> plan[Implementation plan<br/>plan.md]
    plan --> trace[Traceability<br/>trace.md]
    trace --> verify[Verification<br/>verification.md]
    verify --> baseline[Baseline record]
    baseline --> ship[Release readiness<br/>ship.md]
    ship --> opex[Operating signals / OPEX<br/>opex.md]
    opex -.feeds forward.-> basis
```

---

## Source-lineage note

These diagrams are an original visual restatement of the Nuclear-grade workflow, influenced by public lifecycle, configuration-management, and software-assurance sources mapped in [`00-standards-foundation/source-map.md`](00-standards-foundation/source-map.md). They do not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
