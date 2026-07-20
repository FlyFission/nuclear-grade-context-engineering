# All-28 Skill Efficacy Evaluation

Date: 2026-07-04
Repo: `nuclear-grade-context-engineering`
Branch: `alfred/skill-audit-efficacy-20260704`

## Executive conclusion

All 28 skills are now covered by deterministic routing and output benchmark cases. The corpus is structurally benchmarkable, and the strongest skills are likely to add real value over prompt-only when they force a decision or artifact that a generic prompt often omits: escalation, release disposition, controlled-item scope, claim/evidence status, incident command, downstream notification, or terminal packet disposition.

This report is deliberately conservative: it does **not** claim live model efficacy until recorded prompt-only vs skill-loaded transcripts are captured and scored. It does, however, identify where each skill is most likely to earn its keep, where it may tie prompt-only, and what should be amended before or after live Gate 2.

## What changed for all-28 evaluation coverage

- Expanded `evals/skill-routing-cases.jsonl` from 8 seed cases to **152 deterministic routing cases** covering all 28 skills.
  - Cases are derived from the repo prompt bank.
  - Every skill has positive trigger cases and near-miss negative cases.
- Expanded `evals/skill-output-cases.jsonl` from 3 seed cases to **28 deterministic output cases**, one per skill.
  - Each case has explicit required signals and forbidden signals.
  - The output scorer validates all referenced skills against `skills/*/SKILL.md`.
- Re-ran static audit after the expansion.

## Commands and verification

```bash
python tools/ng_skill_route_score.py --cases evals/skill-routing-cases.jsonl --skills-dir skills
```

Result:

```text
Loaded 152 routing case(s) from evals/skill-routing-cases.jsonl
No observed routes supplied; manifest is well-formed.
```

```bash
python - <<'PY'
from tools.ng_skill_output_score import load_cases, validate_case_skills
from pathlib import Path
cases=load_cases(Path('evals/skill-output-cases.jsonl'))
validate_case_skills(cases, Path('skills'))
print(f'Loaded {len(cases)} output case(s); all skill references valid')
print(f'Skills covered: {len({s for c in cases.values() for s in c.skill_set})}')
PY
```

Result:

```text
Loaded 28 output case(s); all skill references valid
Skills covered: 28
```

```bash
python tools/ng_skill_audit.py --root . \
  --jsonl evals/skill-static-audit/2026-07-04/skill-audit.jsonl \
  --markdown evals/skill-static-audit/2026-07-04/skill-audit.md
```

Result:

```text
Audited 28 skills
Wrote evals/skill-static-audit/2026-07-04/skill-audit.jsonl
Wrote evals/skill-static-audit/2026-07-04/skill-audit.md
```

## Scoring interpretation

| Label | Meaning |
|---|---|
| High likely lift | Skill has a concrete decision/artifact that prompt-only commonly misses. Prioritize live A/B. |
| Medium likely lift | Skill is useful, but a strong prompt-only checklist may tie it. Test compression/ablation. |
| Low/uncertain likely lift | Skill may be mostly reference/process prose unless live cases show decision movement. |

Primary measured win condition for Gate 2 should be **decision movement**, not polish: did the skill alter mode, escalation, ship/block/defer, evidence bar, artifact completeness, or downstream obligation?

## Per-skill evaluation and recommendations

| Skill | Likely lift | Why it probably adds value | Main efficacy risk | Recommended repo update |
|---|---:|---|---|---|
| `breaking-down-the-work` | Medium-high | Forces WBS 100% rule, non-overlap, outline IDs, dictionary entries, and delegation-ready slices. | Expert prompt-only WBS may tie; overlaps with folder architecture and briefing. | Add a sharper WBS-only vs delegated-slice boundary; benchmark full skill vs compressed WBS checklist because token cost is high. |
| `briefing-an-agent` | High | Binds agent authority, goal, evidence, forbidden actions, and stop conditions. | Still near `handing-off-work` for resumed/partial work. | Add a one-line discriminator: greenfield/pre-action context pack here; partial-state responsibility transfer goes to `handing-off-work`. |
| `checking-legal-and-safety-wording` | Medium | Prevents public overclaims around safety, warranty, compliance, adequacy, and license scope. | Phrase matching may miss semantic overclaim; overlaps with source claims. | Add semantic red-flag examples: production-ready, enterprise-grade, safe by design, compliant workflow, formally verified. |
| `checking-release-readiness` | High | Forces a single ship/block/defer/ship-with-risk verdict tied to residual risk, rollback, monitoring, and evidence status. | Can be blurred with `proving-claims`. | Add explicit sequence: use `proving-claims` for trace construction, then this skill for the release verdict. |
| `checking-source-claims` | Medium | Separates source lineage, influence, local proof, and external authority. | Close to legal/safety wording; may under-escalate compliance wording. | Add deterministic source-status taxonomy: verified-public, supporting-context, public-url-needed, excluded-direct. |
| `checking-what-a-change-affects` | High | Catches stale docs/tests/templates/commands/validators/runtime surfaces that prompt-only often misses. | Can become whole-repo inventory; overlaps with controlled-item selection. | State that this skill assigns update/leave/defer/block actions for impacted items; `choosing-what-to-control` only names tracked items. |
| `choosing-what-to-control` | Medium | Names approved-state surfaces before change/release. | May list too much and may tie a direct checklist prompt. | Add excluded examples and keep it to approved-state tracking, not downstream update decisions. |
| `closing-stale-packets` | High | Strong repo-specific terminal-state behavior with `NUCLEAR-GRADE-CLOSED:` and safe deletion rules. | Deletion can be too aggressive if intent/ownership is unknown. | Add invariant: unknown intent or non-empty packet means close/escalate, not delete. |
| `creating-change-records` | Medium-high | Produces validator-facing structure, files, links, status labels, and receipts. | May become clerical if `ng new` templates already carry most value; overlaps with mode/proof/release decisions. | Keep boundary tight; add a stronger forbidden-output note: do not choose mode, prove claims, or issue ship verdict. |
| `deciding-who-decides` | High | Moves irreversible/thin-evidence/protected actions from agent edge to named human gate. | Overlaps with intent and double-check skills. | Require named role/person for escalations, not just “human.” Add protected categories examples. |
| `declaring-intent` | Medium-high | Forces intent, expected result, falsifying signal, abort criteria, rollback, and review window before critical action. | Overlaps with double-checking target/state. | Clarify primary hazard: reviewer challenge before execution. Add rollback evidence/status as required field. |
| `double-checking-before-acting` | High | Prevents wrong-target/wrong-state actions and missing after-action proof. | Could become generic caution; overlaps with intent. | Add compact discriminator: immediate target/state/action verification belongs here; pre-action rationale challenge belongs to `declaring-intent`. |
| `handing-off-work` | Medium-high | Captures changed conditions, remaining scope, proof gaps, and incoming-owner confirmation. | Can become ordinary summary or context pack. | Make incoming-owner restatement a hard output requirement. |
| `learning-from-experience` | Medium-high | Converts near misses/incidents into durable control updates, not just retrospectives. | Overlaps with incident response, deficiency tracking, shared-defect reporting. | Add routing triage: live harm → incident; standing unresolved → deficiency; shared artifact → shared-defect; durable lesson → this. |
| `organizing-project-folders` | Medium | Applies folder architecture, one-home rule, safe naming, WBS mapping, and disposition notes. | Highest token-cost concern; may tie a concise architecture prompt. | Compress or split references unless live A/B proves full-body lift. Require respect for existing framework conventions. |
| `proving-claims` | High | Forces claim/evidence/status/gap/non-claim trace and guards against self-attested proof. | Known overlap with release/source/legal/check-record skills. | Make independence rung/status a required trace column; keep “no ship decision” boundary prominent. |
| `questioning-attitude` | Medium-high | Forces decision question, assumptions, unknowns, and the one fact that would change the decision. | Very broad; may become generic skepticism without action. | Compress around unique output: decision question + load-bearing assumptions + decision-changing fact + next routing step. |
| `rating-change-risk` | High | Produces Quick/Standard/stronger mode and evidence obligation; prevents underrated trust-boundary changes. | Complexity may yield inconsistent mode choices; overlaps with workflow router. | Add ordered tripwire table and clarify administrative-floor examples are non-claim-bearing. |
| `recording-a-known-good-version` | Medium | Captures accepted baseline identity, evidence, controlled items, and invalidation triggers. | May be simple enough for prompt-only; can be invoked too early. | Require exact rebuild identity and accepted-version evidence; clarify sequence after control/impact/release decisions. |
| `recording-what-an-agent-did` | High | Converts raw agent log into consequential steps, approvals, tool calls, decision points, and verification links. | Can become noisy transcription; telemetry may be unavailable. | Add consequential-step filter: file writes, external calls, side-effect commands, approvals, failed/retried commands, scope-changing decisions. |
| `reporting-shared-defects` | High | Adds outward notification/downstream-consumer obligation that local bug-fix prompts often omit. | Overlaps with deficiency tracking and OPEX; can over-trigger on local-only bugs. | Add first gate: shared/supplied artifact? consumers known/foreseeable? live incident? |
| `responding-to-incidents` | High | Forces stabilize-first commander model, fact/hypothesis separation, reversible action, cadence, and owned actions. | Can trigger on historical postmortems. | Add incident phase states: declared, stabilizing, stable/live phase closed, post-incident follow-up. |
| `reviewing-code-quality` | Medium-high | Adds deletion-first maintainability review and honest verdict beyond functional correctness. | Can duplicate normal code review and soft thresholds reduce determinism. | Require each finding to classify delete/simplify/justify keep. Clarify verdict is maintainability, not test correctness. |
| `staying-on-mission` | High | Catches scope drift, loops, standard erosion, and repeated low-progress work. | Broad overlap with questioning/risk/code-quality/handoff. | Fix output decision set so labels are exact; require anchor-exists/provisional-anchor gate. |
| `stress-testing-agent-changes` | High | Forces adversarial classes, probe intent, expected safe behavior, outcome, and leftover risk for agent power changes. | Can imply formal security audit; simulations may be too weak. | Add minimum attack classes by trigger and a `not tested` status separate from `uncertain`. |
| `tracking-deficiencies` | High | Turns normalized chronic problems into owned, aged, dispositioned register entries. | Can trigger for brand-new bugs that should just be fixed. | Add persistence gate and allowed dispositions: fix-by, risk-accepted, duplicate/merged, not-a-deficiency. |
| `using-nuclear-grade` | Mixed-high | Valuable first router for mode and evidence path before side effects. | Broadest overuse risk; can suppress more specific skills. | Add “provisional mode after read-only discovery” rule and deterministic routing table from tripwire to downstream skill cluster. |
| `vetting-outside-code-and-models` | High | Separates vendor claims from local evidence and maps outside item to intended use, limits, acceptance, and revalidation. | Overlaps with stress-testing and source-claims; dev-only exception can be abused. | Add trust-impact gate: dev-only but CI/release-affecting still triggers. Require characteristic → acceptance method → evidence → gap table. |

## Priority update queue

### P0: Update before expensive live A/B

These have high overlap or token-cost risk that could distort the benchmark.

1. `using-nuclear-grade`
   - Add provisional read-only discovery rule.
   - Add downstream routing table.
2. `rating-change-risk`
   - Add ordered tripwire table.
   - Clarify administrative floor vs Quick vs Standard-plus.
3. `briefing-an-agent` / `handing-off-work`
   - Add reciprocal discriminator and hard incoming-owner confirmation.
4. `proving-claims` / `checking-release-readiness` / `checking-source-claims` / `checking-legal-and-safety-wording`
   - Add source/legal/release/proof boundary sequence and required independence/source-status columns.
5. `organizing-project-folders`
   - Run compressed-skill ablation; refactor if no lift over concise checklist.

### P1: Update after first all-28 live run if measured weak

- `choosing-what-to-control`
- `recording-a-known-good-version`
- `reviewing-code-quality`
- `questioning-attitude`
- `breaking-down-the-work`

These are useful but may tie a strong prompt-only checklist. Let measured decision movement decide whether to compress, split, or keep full.

### P2: Keep mostly as-is; test with fixture-backed cases

- `closing-stale-packets`
- `responding-to-incidents`
- `reporting-shared-defects`
- `tracking-deficiencies`
- `stress-testing-agent-changes`
- `vetting-outside-code-and-models`
- `recording-what-an-agent-did`
- `double-checking-before-acting`
- `deciding-who-decides`

These have crisp decision/artifact obligations and are likely to show lift if the benchmark cases include realistic traps.

## Recommended live Gate 2 design

Use the repo-native route/output manifests for corpus coverage, then run the live agent trials as SkillsBench-style task packages. See `docs/05-reference/skillsbench-adoption-plan.md`.

Run all 28 skills through the same matrix:

1. **Routing:** 152 route cases.
   - Score top-1 and top-3 loaded skill accuracy.
   - Penalize over-triggering on negative cases.
2. **Output:** 28 output cases.
   - For each case, run at least 3 repetitions per variant.
   - Variants:
     - naive prompt-only
     - best-practice prompt-only
     - equal-token generic checklist
     - skill description only
     - full skill
     - compressed skill ablation for high-token skills
     - irrelevant-skill control
3. **SkillsBench / BenchFlow task packages:** create compositional tasks with `task.md`, sandbox environment, bundled skills, oracle, and verifier scripts for realistic artifact-producing work.
   - Use SkillsBench for reproducible with-skill/no-skill execution.
   - Keep the Nuclear-grade deterministic scorers for route/output regression scoring of recorded transcripts.
4. **Scoring:** deterministic required/forbidden signals first, verifier reward second, then blinded pairwise review only for ties.
5. **Decision bit:** record whether the skill changed a real outcome: mode, escalation, ship/defer/block, evidence bar, owner, downstream notification, terminal state, or artifact completeness.
6. **Acceptance thresholds:**
   - Keep as control: skill beats best-practice prompt on decision movement or prevents fatal miss in hard cases.
   - Compress: skill ties prompt-only but has useful checklist content.
   - Refactor: skill loses, over-triggers, or mostly rewords prompt-only output.
   - Relocate to docs: near-zero decision movement after hard-case retest.

## Final recommendation

Proceed to Gate 2 live A/B with the new all-28 manifests, but do not market the current branch as “skills proven effective.” The correct claim is:

> The 28-skill corpus is now structurally complete and fully instrumented for independent live A/B evaluation. Static and independent review indicate high likely value for the majority of skills, with specific overlap and compression risks identified before live execution.

The repo should next implement the P0 clarifications above, then run recorded live A/B transcripts through the existing route/output scorers.
