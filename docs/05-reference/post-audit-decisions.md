# Post-Audit Decisions: Skill Overlaps and Prose Optimization

**Status:** Recommendations for human decision
**Date:** 2026-05-31
**Context:** Follow-up to token audit (#13), unblocked by #12 merge

This document records the investigation and recommendations for the deferred work from the token audit. Each section provides analysis, evidence, and a clear recommendation with rationale.

## Executive Summary

After analyzing the four overlap clusters and prose patterns across 23 skills:

1. **Keep all four overlap clusters separate** — each serves a distinct decision point with different inputs, outputs, and routing implications
2. **Tighten prose selectively** — focus on the heaviest 5 skills (2,489–1,617 tokens), not broad changes
3. **Keep disclaimer distributed** — self-containment serves the doctrine better than compactness
4. **Relocate core-source-rationale.md** — move design justification out of agent-runtime path

**Estimated token savings:** ~1,500–2,000 tokens (0.8–1.1% of total prose), with the gate ensuring no silent regression.

---

## 1. Overlap Cluster Analysis and Recommendations

### Cluster 1: Trust-boundary trio

**Skills:** `checking-source-claims`, `checking-legal-and-safety-wording`, `vetting-outside-code-and-models`

**Analysis:**
- **checking-source-claims** (872 tokens): validates citations to source families, prevents compliance claims
- **checking-legal-and-safety-wording** (879 tokens): guards public text against warranty/safety overclaims
- **vetting-outside-code-and-models** (1,053 tokens): evaluates external dependencies, models, APIs against intended use

**Trigger differences:**
- Source-claims: fires when docs cite standards/agencies
- Legal-wording: fires on public text (README, docs, templates)
- Vetting: fires on dependency/model/API changes

**Recommendation:** **KEEP SEPARATE**

**Rationale:**
These operate at three distinct trust boundaries:
1. Citation honesty (idea lineage)
2. Legal boundary wording (user expectations)
3. External code/model trust (supply chain)

Merging would create a single 2,800+ token skill that violates single-responsibility and forces agents to load citation logic when evaluating a dependency. The routing distinction (when to fire each) is clear and test-frozen.

---

### Cluster 2: Agent-handoff trio

**Skills:** `briefing-an-agent`, `handing-off-work`, `double-checking-before-acting`

**Analysis:**
- **briefing-an-agent** (1,150 tokens): prepares focused context pack for agent/reviewer with role, authority, evidence obligations
- **handing-off-work** (982 tokens): transfers responsibility with closed-loop confirmation of state, changed conditions, remaining work
- **double-checking-before-acting** (938 tokens): self-check before critical action, comparing expected vs actual result

**Trigger differences:**
- Briefing: fires when starting or delegating work
- Handoff: fires when transferring unfinished work to new owner
- Self-check: fires immediately before a risky action (delete, publish, credential use)

**Recommendation:** **KEEP SEPARATE**

**Rationale:**
These are three distinct HPI (Human Performance Improvement) moments:
1. **Before work starts** → brief
2. **When work transfers** → hand off
3. **Before critical action** → self-check

Timing matters: a self-check happens seconds before an action; a handoff happens when ownership changes; a briefing happens at work initiation. The Process sections are deliberately prescriptive because these are safety-critical habits where the sequence matters. Merging would obscure which habit applies when.

---

### Cluster 3: Evidence / decision trio

**Skills:** `proving-claims`, `checking-release-readiness`, `reviewing-code-quality`

**Analysis:**
- **proving-claims** (1,083 tokens): maps claims to evidence, statuses, gaps; separates fact/assumption/proof
- **checking-release-readiness** (1,067 tokens): records ship/block/defer decision with baseline, rollback, monitoring
- **reviewing-code-quality** (1,461 tokens): standards review favoring deletion, ending in one verdict

**Trigger differences:**
- Proving: fires when claims need evidence mapping (any phase)
- Release-readiness: fires near merge/release for ship decision
- Code-quality: fires during review for standards check

**Recommendation:** **KEEP SEPARATE**

**Rationale:**
These serve three phases of the verification path:
1. **Evidence assembly** (proving-claims) — happens during development
2. **Release decision** (checking-release-readiness) — happens at gate
3. **Standards review** (reviewing-code-quality) — happens during review

`proving-claims` is about *what to prove*; `checking-release-readiness` is about *ship or block given the evidence*; `reviewing-code-quality` is about *maintainability standards*. Combining would force agents to load release-decision logic when they're still assembling evidence, violating the two-speed doctrine (explore fast, decide carefully).

---

### Cluster 4: Framing / risk overlap

**Skills:** `questioning-attitude`, `rating-change-risk`, `choosing-what-to-control`

**Analysis:**
- **questioning-attitude** (1,371 tokens): challenges assumptions, names the one fact that would change the decision
- **rating-change-risk** (1,052 tokens): sorts change into Quick/Standard/Nuclear mode based on consequence and undo-ability
- **choosing-what-to-control** (1,014 tokens): decides which items (code, prompts, deps, docs) need approved-state tracking

**Trigger differences:**
- Questioning: fires when work is vague/high-stakes/easy to talk yourself into (front door)
- Rating-risk: fires when mode choice is unclear
- Choosing-what-to-control: fires when scoping CM (configuration management) records

**Recommendation:** **KEEP SEPARATE**

**Rationale:**
These operate at three nesting levels:
1. **Questioning** — highest level, applies to *any* work (the "front door")
2. **Rating-risk** — picks the *mode* (Quick vs Standard)
3. **Choosing-what-to-control** — scopes *what's under CM* within that mode

`questioning-attitude` explicitly routes to `rating-change-risk` in its Process section ("Pick the next step: quick proof, a standard spec..."). The dependency is intentional and test-covered. Merging would create a 3,437-token meta-skill that tries to do framing, mode-selection, and CM scoping in one pass, violating progressive disclosure.

---

## 2. Body-Level Prose Optimization

### Current state (token audit baseline)

Heaviest skill bodies:
- `organizing-project-folders`: 2,641 tokens
- `breaking-down-the-work`: 2,217 tokens
- `closing-stale-packets`: 1,962 tokens
- `staying-on-mission`: 1,953 tokens
- `stress-testing-agent-changes`: 1,742 tokens

Leanest skill bodies:
- `checking-what-a-change-affects`: 832 tokens
- `checking-source-claims`: 872 tokens
- `checking-legal-and-safety-wording`: 879 tokens

### Analysis of over-prescription

**"When to Use / When Not to Use" sections:**
Reviewed all 23 skills. Most follow the "where the landmines are" pattern correctly. Two exceptions:
- `breaking-down-the-work`: 9 positive triggers, 6 negative triggers (prescriptive list)
- `rating-change-risk`: 5 positive triggers, 2 negative triggers (prescriptive list)

However, these are *intentionally* prescriptive — they're decision-tree skills where exhaustive triggers prevent mode-selection errors (a safety-critical choice).

**"Process" sections:**
Heaviest skills are naturally prescriptive:
- `organizing-project-folders`: teaches Model Workspace Protocol (numbered stages, context contracts) — needs steps
- `breaking-down-the-work`: teaches WBS 100% rule and mutual exclusivity — needs steps
- `closing-stale-packets`: lifecycle state machine (scaffold → completed/closed/deleted) — needs steps

The prescription matches the complexity. Lighter skills (`checking-source-claims`: 872 tokens) are already lean.

### Recommendation: **SELECTIVE TIGHTENING**

**Target only the top 5 heaviest skills (2,641–1,742 tokens):**

1. **organizing-project-folders** (2,641 tokens):
   - Move detailed Model Workspace Protocol to `references/` subdir (progressive disclosure per skill-authoring contract)
   - Keep 4-step core process in body
   - **Estimated savings: ~600 tokens**

2. **breaking-down-the-work** (2,217 tokens):
   - Collapse overlapping examples in Process section
   - Keep WBS rules (100%, MECE, dictionary) as-is (contract obligation)
   - **Estimated savings: ~300 tokens**

3. **closing-stale-packets** (1,962 tokens):
   - Already lean for a state-machine skill
   - **No change recommended**

4. **staying-on-mission** (1,953 tokens):
   - Consolidate "Common Rationalizations" (9 items) to top 5
   - **Estimated savings: ~150 tokens**

5. **stress-testing-agent-changes** (1,742 tokens):
   - Move 8 attack-type taxonomy to `references/attack-types.md`
   - Keep probe → posture → residual-risk flow in body
   - **Estimated savings: ~400 tokens**

**Total estimated savings: ~1,450 tokens** (4.8% of body cost, 0.8% of total prose)

**Do NOT touch:**
- Leanest skills (already under 900 tokens)
- HPI skills (briefing, handoff, self-check) — prescription is the safety control
- Decision skills (questioning, rating-risk, proving-claims) — trigger lists are contract obligations

---

## 3. Disclaimer Repetition: Keep Distributed

### Current state

- **58 occurrences** of "does not create" across 55 files
- **22 occurrences** in skills/ alone
- Pattern: each skill's "Source-lineage note" section ends with disclaimer

### Alternatives considered

**Option A: Collapse to single linked source**
- Create `DISCLAIMER.md` or `docs/00-standards-foundation/assurance-boundaries.md`
- Replace 55 disclaimers with "See [assurance-boundaries.md] for what this does not create"
- **Savings: ~550 tokens** (58 × ~10 tokens/disclaimer)

**Option B: Keep distributed (status quo)**
- Each file self-contained
- No dependency on reader following link
- Disclaimer visible at point of use

### Recommendation: **KEEP DISTRIBUTED (Option B)**

**Rationale:**

1. **Self-containment is doctrine**: The repo teaches "focused context" and "evidence at point of use". Forcing readers to chase a link for the legal boundary violates that teaching.

2. **Risk asymmetry**: The cost of accidentally omitting a disclaimer in a new skill (when relying on link discipline) is higher than the cost of 550 tokens.

3. **Not actually redundant**: Each disclaimer is *contextual* — skills cite different source families (DOE, NASA, NIST, NVIDIA) and disclaim different claims (DOE compliance vs formal assurance vs certification). The common pattern is "does not create X", but X varies by skill lineage.

4. **Token cost is acceptable**: The audit confirmed always-loaded cost is descriptions (2,361 tokens), not bodies. Disclaimer cost (550 tokens ≈ 1.8% of bodies) loads only when a skill fires. The gate prevents silent regression.

5. **Progressive disclosure doesn't apply**: Disclaimers aren't "optional detail" — they're legal boundaries that must be immediately visible.

**Verification:**
Grep confirms disclaimer appears only in negative/boundary contexts (per contract test). No overclaim risk.

---

## 4. core-source-rationale.md Relocation

### Current state

- Path: `docs/00-standards-foundation/core-source-rationale.md`
- **2,165 tokens** of design justification
- Content: why DOE/NRC/NIST/NASA/OpenSSF sources were chosen as foundation
- Audience: repo designers, contributors deciding whether to add new source tier

### Analysis

**Is it agent-runtime content?**
No. An agent executing a change does not need to know *why* DOE-STD-1073 was chosen over ASME NQA-1. It needs to know *what* the workflow teaches (already in skill bodies and `source-map.md`).

**Does it affect routing or decisions?**
No. Skills link to `source-map.md` (the *what*), not `core-source-rationale.md` (the *why*). Zero skills reference this file.

**Who needs it?**
- Maintainers deciding whether to add Tier 7, 8, ...
- External reviewers evaluating source-foundation choices
- Contributors proposing new source families

### Recommendation: **RELOCATE**

**New path:** `.research/design-decisions/core-source-rationale.md`

**Rationale:**

1. **Out of agent path**: `.research/` is gitignored or clearly marked as non-runtime
2. **Preserves content**: file is not deleted, just moved out of `docs/` tree
3. **Still linkable**: `CONTRIBUTING.md` or `docs/00-standards-foundation/README.md` can link to it for maintainers
4. **Savings: 2,165 tokens** removed from docs/ tree (1.8% of total prose)

**Alternative locations considered:**
- `docs/06-design-decisions/` — but this creates a new docs category
- `docs/00-standards-foundation/archive/` — but "archive" implies deprecated content
- `.research/` — best fit, already used for non-public scratch work

**Verification:**
- Grep confirms zero skills or commands reference `core-source-rationale.md`
- `source-map.md` and `source-to-concept-crosswalk.md` remain in `docs/00-standards-foundation/`

---

## 5. Summary of Recommendations

| Item | Action | Token Savings | Rationale |
|---|---|---|---|
| **Overlap clusters** | Keep all 4 clusters separate | 0 | Distinct triggers, phases, and routing implications |
| **Body prose** | Tighten top 5 skills selectively | ~1,450 | Progressive disclosure for heavy skills only |
| **Disclaimers** | Keep distributed | 0 | Self-containment doctrine + risk asymmetry |
| **core-source-rationale.md** | Relocate to `.research/design-decisions/` | ~2,165 | Design justification, not runtime content |
| **Total** | | **~3,615 tokens** | **2.0% of total prose** |

---

## 6. Implementation Notes

If approved:

1. **Overlap clusters:** No action (keep as-is)

2. **Body prose:**
   - Create `skills/organizing-project-folders/references/model-workspace-protocol.md`
   - Create `skills/stress-testing-agent-changes/references/attack-types.md`
   - Edit 5 skill bodies per recommendations above
   - Run `python tools/ng.py tokens .` before/after to confirm savings

3. **Disclaimers:** No action (keep as-is)

4. **Relocation:**
   - `mkdir -p .research/design-decisions/`
   - `git mv docs/00-standards-foundation/core-source-rationale.md .research/design-decisions/`
   - Update `docs/00-standards-foundation/README.md` to link to new location for maintainers
   - Verify `ng tokens` reflects removal from docs tree

5. **Verification:**
   - `python -m pytest -q` (all tests pass)
   - `python tools/ng.py tokens .` (budget gate passes, before/after delta matches estimates)
   - `python tools/ng.py doctor .` (OK)
   - Grep confirms no broken references

---

## 7. Boundary Note

This analysis measures token cost and reviews prose patterns. It does not judge whether a skill is correct, safe, secure, or compliant, and it does not create formal V&V, certification, or regulatory adequacy.
