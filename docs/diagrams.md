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

## 2. The PROVE path — one path, two zoom levels

The same eleven beats, grouped into a handle you can remember. Zoom out to **PRO** — three moves. Zoom in to **PROVE** — five, with the acceptance gate named on its own. The beats, their order, and the control points are unchanged; this is a label, not a new workflow.

**PRO — the billboard (3):**

```mermaid
flowchart TB
  classDef plan fill:#DCE6FA,stroke:#3A5BA8,color:#12203F;
  classDef run fill:#E4DEF7,stroke:#5B49A6,color:#1E1640;
  classDef emb fill:#DCEFDE,stroke:#2E7D45,color:#102810;
  classDef gate fill:#FFD24D,stroke:#B07400,color:#3A2600,stroke-width:2px;
  subgraph LP["P — PLAN"]
    direction LR
    A1(["Question"]) --> A2(["Discover"]) --> A3(["Specify"]) --> A4(["Plan"])
  end
  subgraph LRUN["R — RUN"]
    direction LR
    B1(["Execute"]) --> B2(["Verify"]) --> B3(["Review"]) --> B4{"Decide"}
  end
  subgraph LOPS["O — OPERATE"]
    direction LR
    C1(["Baseline"]) --> C2(["Operate"]) --> C3(["Learn"])
  end
  A4 --> B1
  B4 -->|"ship / defer"| C1
  B4 -.->|"block"| A4
  C3 -.->|"lessons feed the next basis"| A1
  class A1,A2,A3,A4 plan
  class B1,B2,B3 run
  class B4 gate
  class C1,C2,C3 emb
```

**PROVE — the working map (5):**

```mermaid
flowchart TB
  classDef plan fill:#DCE6FA,stroke:#3A5BA8,color:#12203F;
  classDef run fill:#E4DEF7,stroke:#5B49A6,color:#1E1640;
  classDef obs fill:#D2EBE6,stroke:#248A7E,color:#0E2A26;
  classDef emb fill:#DCEFDE,stroke:#2E7D45,color:#102810;
  classDef gate fill:#FFD24D,stroke:#B07400,color:#3A2600,stroke-width:2px;
  subgraph LP["P — PLAN"]
    direction LR
    Q(["Question"]) --> D(["Discover"]) --> S(["Specify"]) --> PL(["Plan"])
  end
  subgraph LRUN["R — RUN"]
    E(["Execute"])
  end
  subgraph LO["O — OBSERVE"]
    direction LR
    V(["Verify"]) --> RV(["Review"])
  end
  subgraph LV["V — VERDICT"]
    DEC{"Decide"}
  end
  subgraph LE["E — EMBED"]
    direction LR
    B(["Baseline"]) --> OP(["Operate"]) --> L(["Learn"])
  end
  PL --> E --> V
  RV --> DEC
  DEC -->|"ship / defer"| B
  DEC -.->|"block"| PL
  L -.->|"lessons feed the next basis"| Q
  class Q,D,S,PL plan
  class E run
  class V,RV obs
  class DEC gate
  class B,OP,L emb
```

**Crosswalk — how the zoom levels line up:**

| Full path (11 beats) | PROVE — working map (5) | PRO — billboard (3) |
|---|---|---|
| Question · Discover · Specify · Plan | **P** — Plan | **P** — Plan |
| Execute | **R** — Run | **R** — Run |
| Verify · Review | **O** — Observe | ↳ inside Run |
| Decide | **V** — Verdict | ↳ inside Run |
| Baseline · Operate · Learn | **E** — Embed | **O** — Operate |

PROVE and PRO are memory handles for the full eleven-beat path; the [seven control points](../WORKFLOWS.md) are its everyday short form, and the [Core 7](../CORE.md) are always-on habits, not path stages. "PROVE" names the prove-your-claims habit — evidence behind every claim — not formal proof or verification.

---

## 3. Mode decision tree

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

## 4. Skill-relationship graph

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

## 5. Packet artifact-dependency graph

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
