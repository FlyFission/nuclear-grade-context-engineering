# SkillsBench Adoption Plan for Nuclear-grade Skill Efficacy

Date: 2026-07-04

## Conclusion

SkillsBench is a better fit for the **live execution layer** of Nuclear-grade skill efficacy testing than a custom one-off runner, but it should not replace the repository's deterministic contract/readiness checks.

Use both:

1. **Repo-native checks** prove the 28 skills are structurally benchmarkable: contracts, trigger/negative prompt coverage, token budget, command parity, and deterministic route/output manifests.
2. **SkillsBench / BenchFlow task packages** should run the live with-skill vs no-skill experiments in isolated, reproducible environments with oracle solutions and verifier scripts.

In other words: keep the current static/readiness harness as Gate 1; adopt SkillsBench-style task packages for Gate 2.

## What SkillsBench adds that this repo should use

SkillsBench contributes several pieces that are stronger than the current custom harness:

- **Native `task.md` task packages** with prompt, environment, skills, oracle, and verifier colocated.
- **Docker/sandbox-backed execution** so tasks are repeatable and not coupled to a developer workstation.
- **Oracle-first discipline**: oracle must pass before agent evaluation.
- **Verifier-first scoring**: output is checked by scripts, not vibes.
- **Built-in with-skill / no-skill experiment mode** via BenchFlow.
- **Task metadata and taxonomy** for difficulty, interface, modality, task type, and skill type.
- **No-skill vs with-skill comparison** as a first-class contribution requirement.

## What this repo should keep

The Nuclear-grade repo still needs its own layer because these skills are assurance/process skills, not just domain procedural helpers.

Keep:

- `tools/ng_skill_audit.py` for structural readiness.
- `evals/skill-routing-cases.jsonl` for all-28 trigger and near-miss routing checks.
- `evals/skill-output-cases.jsonl` for required/forbidden decision-signal scoring.
- `tools/ng_skill_route_score.py` and `tools/ng_skill_output_score.py` for deterministic regression scoring of recorded transcripts.
- `python tools/ng.py eval .` and `python tools/ng.py tokens .` for repo-native contract and token discipline.

## Recommended hybrid benchmark architecture

```text
Gate 1: Repo-native readiness
  skills/*/SKILL.md
  docs/05-reference/skill-evaluation.md
  evals/skill-routing-cases.jsonl
  evals/skill-output-cases.jsonl
  tools/ng_skill_audit.py
  tools/ng_skill_route_score.py
  tools/ng_skill_output_score.py

Gate 2: SkillsBench live task packages
  evals/skillsbench/tasks/<task-id>/
    task.md
    environment/
      Dockerfile
      skills/<skill-name>/SKILL.md
      fixtures...
    oracle/solve.sh
    verifier/test.sh
    verifier/test_outputs.py

Gate 3: Analysis and repo amendments
  scored with-skill/no-skill transcripts
  deterministic route/output scores
  per-skill decision-movement rate
  keep / compress / refactor / relocate recommendation
```

## Mapping Nuclear-grade skills to SkillsBench tasks

Do not create one toy task per skill if the task is only a questionnaire. SkillsBench is most valuable when the agent must produce or modify an artifact that a verifier can check.

Recommended task families:

| Task family | Skills tested | Verifier target |
|---|---|---|
| Packet repair and closure | `creating-change-records`, `closing-stale-packets`, `checking-release-readiness` | Packet files, status labels, validation receipt, terminal closure marker |
| Public claim hardening | `checking-source-claims`, `checking-legal-and-safety-wording`, `proving-claims` | README/doc rewritten to remove overclaims; trace rows preserve source boundaries |
| Agent authority incident | `deciding-who-decides`, `declaring-intent`, `double-checking-before-acting`, `responding-to-incidents` | Decision record escalates protected action; incident timeline separates facts/hypotheses |
| Drift and chronic-risk control | `staying-on-mission`, `tracking-deficiencies`, `learning-from-experience`, `reporting-shared-defects` | Register/OPEX/notification artifacts with owner, trigger, and durable control update |
| Outside dependency/model review | `vetting-outside-code-and-models`, `stress-testing-agent-changes`, `recording-what-an-agent-did` | Trust screen, adversarial probe table, consequential agent-run trace |
| Project decomposition and layout | `breaking-down-the-work`, `organizing-project-folders`, `briefing-an-agent`, `handing-off-work` | WBS, folder map, context pack, handoff record with exact required fields |
| Workflow router and risk mode | `using-nuclear-grade`, `rating-change-risk`, `choosing-what-to-control`, `checking-what-a-change-affects`, `recording-a-known-good-version` | Mode declaration, controlled items, impact actions, accepted baseline record |

## Minimal SkillsBench task package pattern for this repo

```text
evals/skillsbench/tasks/ng-public-claim-hardening/
  task.md
  environment/
    Dockerfile
    README.md
    sources/
    skills/
      checking-source-claims/SKILL.md
      checking-legal-and-safety-wording/SKILL.md
      proving-claims/SKILL.md
  oracle/
    solve.sh
  verifier/
    test.sh
    test_outputs.py
```

`task.md` should ask for the end state, not name the skills. Example:

```markdown
---
schema_version: '1.3'
metadata:
  difficulty: medium
  category: critical-infrastructure
  subcategory: assurance-documentation
  task_type: [analysis, writing]
  modality: [text]
  interface: [terminal]
  skill_type: [domain-procedure]
verifier:
  type: test-script
  timeout_sec: 900.0
agent:
  timeout_sec: 900.0
environment:
  network_mode: no-network
  os: linux
  cpus: 1
  memory_mb: 4096
  storage_mb: 10240
---

Harden `/root/README.md` for public release. Preserve accurate source lineage,
remove unsupported assurance/compliance/safety claims, and write a trace table to
`/root/claim-trace.md` showing which claims are supported, narrowed, or removed.
```

Verifier should check concrete outputs, for example:

- forbidden phrases are absent as positive claims;
- source rows are present;
- unsupported claims are removed or narrowed;
- trace statuses use allowed vocabulary;
- no claim says the workflow is certified, compliant, formally verified, or safe.

## Recommended command sequence for a pilot

In a clean clone of SkillsBench or after adding compatible task packages:

```bash
uv tool install "benchflow>=0.6.2,<0.7"
uv sync --locked
bench tasks check evals/skillsbench/tasks/ng-public-claim-hardening
bench eval run --tasks-dir evals/skillsbench/tasks/ng-public-claim-hardening --agent oracle --sandbox docker
bench eval run --tasks-dir evals/skillsbench/tasks/ng-public-claim-hardening --agent claude-agent-acp --model <model> --skill-mode no-skill
bench eval run --tasks-dir evals/skillsbench/tasks/ng-public-claim-hardening --agent claude-agent-acp --model <model> --skill-mode with-skill --skills-dir evals/skillsbench/tasks/ng-public-claim-hardening/environment/skills/
```

Exact agent identifiers may depend on local BenchFlow/agent integration configuration.

## Adoption decision

Adopt SkillsBench as follows:

1. Keep current all-28 route/output manifests as the skill-corpus map.
2. Build **7 compositional SkillsBench tasks** covering the 28 skills in realistic clusters.
3. For each task, run oracle, no-skill, with-skill, and optionally compressed-skill ablation.
4. Feed recorded outputs back through `ng_skill_output_score.py` where applicable.
5. Use verifier reward plus deterministic decision-signal scores to classify each skill:
   - keep as control,
   - compress,
   - refactor boundary,
   - relocate to docs.

## Risks and cautions

- SkillsBench tasks are stronger when output artifacts can be deterministically checked. Some Nuclear-grade skills are routing/decision skills, so verifiers must check records and decisions, not only final prose.
- Do not leak skill names in task prompts. Let skill invocation behavior be measured.
- Do not bake the answer into bundled skills. Skills should be reusable procedure, not task-specific solution keys.
- The with-skill result should beat both naive no-skill and best-practice prompt-only; otherwise the skill may be a reference doc or compressed checklist candidate.
- BenchFlow agent support and command names may drift; pin versions in this repo once the pilot is working.
