# Skill and Workflow Comparison

**Purpose:** Test whether Nuclear-grade skills and workflows help more than simple prompting across realistic AI-assisted software work.

**Status:** Qualitative sandbox evaluation. This is not a benchmark, user study, safety claim, security claim, compliance claim, or formal assurance result.

## Method

Each trial used the same scenario facts in two ways:

1. **Simple prompt path:** Ask an agent to do the task directly, with normal review expectations.
2. **Nuclear-grade path:** Apply the relevant skill and workflow artifacts before deciding what to build, prove, defer, or release.

The comparison scores are reviewer judgments from the produced artifacts, not independent empirical measurements.

Scoring:

| Score | Meaning |
|---|---|
| 1 | Weak; reviewer cannot rely on it. |
| 2 | Some useful output, but important gaps are hidden. |
| 3 | Usable with reviewer correction. |
| 4 | Strong; most decision-useful information is visible. |
| 5 | Strong and compact; decision, evidence, and gaps are clear. |

Overhead is scored separately:

| Score | Meaning |
|---|---|
| 1 | Almost no process cost. |
| 3 | Noticeable but manageable cost. |
| 5 | Heavy cost; probably unjustified unless consequence is high. |

## Use Cases

| ID | Scenario | Simple prompt | Nuclear-grade application | Result |
|---|---|---|---|---|
| U1 | Tiny README wording fix | "Fix the typo and make sure nothing else changes." | Quick change with `classifying-change-risk`, `creating-change-packets`, and `proving-claims`. | Simple prompting is nearly enough; Quick is useful only when a durable review record is desired. |
| U2 | Agent workspace write boundary | "Add a guard so the agent can only write inside the workspace." | Questioning attitude, Standard packet, controlled items, context pack, claim proof, ship review. | Nuclear-grade found negative tests and non-claims that simple prompting tends to miss. |
| U3 | Dependency security update | "Bump `requests` and run tests." | Standard packet, controlled item, impact screen, claim proof, ship review, baseline trigger. | Nuclear-grade separated behavior evidence from advisory evidence and produced a valid "do not ship" decision when advisory proof was missing. |
| U4 | Public assurance wording rewrite | "Make the README sound credible and enterprise-ready." | Source-lineage check, license/assurance boundary check, impact screen, Standard packet. | Nuclear-grade prevented overclaiming and turned marketing language into bounded evidence language. |
| U5 | Prompt/model baseline for an agent tool | "Update the agent prompt/model and release it." | Controlled configuration workflow, baseline record, impact screen, proof, release readiness. | Nuclear-grade made prompt/model drift, eval proof, and revalidation triggers visible. |
| U6 | Handoff an agent to fix a validator issue | "Fix the validator bug." | Context pack, questioning attitude, classification, Quick-or-Standard decision, proof obligation. | Nuclear-grade reduced authority ambiguity and stopped the agent from broad repo edits. |

## Coverage Matrix

Every published skill was exercised in at least two use cases.

| Skill | U1 | U2 | U3 | U4 | U5 | U6 |
|---|---:|---:|---:|---:|---:|---:|
| `questioning-attitude` |  | x | x | x | x | x |
| `using-nuclear-grade` | x | x | x | x | x | x |
| `identifying-controlled-items` |  | x | x |  | x |  |
| `screening-change-impact` |  | x | x | x | x |  |
| `baselining-configuration` |  |  | x |  | x |  |
| `classifying-change-risk` | x | x | x | x | x | x |
| `creating-change-packets` | x | x | x | x |  | x |
| `packing-agent-context` |  | x | x |  |  | x |
| `proving-claims` | x | x | x |  | x | x |
| `reviewing-ship-readiness` |  | x | x |  | x |  |
| `checking-source-lineage` |  |  |  | x | x |  |
| `checking-license-and-assurance-boundaries` |  |  |  | x | x |  |

Every published workflow was exercised in at least two use cases.

| Workflow | U1 | U2 | U3 | U4 | U5 | U6 |
|---|---:|---:|---:|---:|---:|---:|
| Questioning attitude |  | x | x | x | x | x |
| Quick change | x |  |  |  |  | x |
| Standard change |  | x | x | x |  | x |
| Controlled configuration |  | x | x |  | x |  |
| Agent authority change |  | x |  |  | x | x |
| Release readiness |  | x | x |  | x |  |
| Source/legal check |  |  |  | x | x |  |

## Comparative Scores

| Use case | Path | Decision clarity | Hidden risk discovery | Evidence quality | Useful ship/defer decision | Overhead |
|---|---|---:|---:|---:|---:|---:|
| U1 README wording fix | Simple prompt | 4 | 2 | 3 | 3 | 1 |
| U1 README wording fix | Nuclear-grade | 4 | 3 | 4 | 3 | 2 |
| U2 workspace write boundary | Simple prompt | 3 | 2 | 2 | 2 | 1 |
| U2 workspace write boundary | Nuclear-grade | 5 | 5 | 5 | 4 | 4 |
| U3 dependency security update | Simple prompt | 3 | 2 | 2 | 2 | 1 |
| U3 dependency security update | Nuclear-grade | 5 | 4 | 4 | 5 | 4 |
| U4 public assurance wording | Simple prompt | 3 | 1 | 2 | 2 | 1 |
| U4 public assurance wording | Nuclear-grade | 5 | 5 | 4 | 4 | 3 |
| U5 prompt/model baseline | Simple prompt | 2 | 2 | 2 | 2 | 1 |
| U5 prompt/model baseline | Nuclear-grade | 5 | 5 | 4 | 5 | 4 |
| U6 validator agent handoff | Simple prompt | 3 | 2 | 3 | 3 | 1 |
| U6 validator agent handoff | Nuclear-grade | 4 | 4 | 4 | 4 | 3 |

## Trial Notes

### U1: Tiny README Wording Fix

Simple prompting is competitive. The change is local, reversible, and easy to inspect. Nuclear-grade adds value only when the team wants a durable record that the change was docs-only and no public assurance language shifted.

Best mode: Quick.

Outcome: Nuclear-grade should stay lightweight here. A full Standard packet would be ceremony.

### U2: Agent Workspace Write Boundary

Simple prompting usually asks for a guard and tests. It may produce a happy-path check and one traversal check, but it often does not force a release reviewer to distinguish what is proven from what is not proven.

Nuclear-grade improved the result by naming:

- controlled item: workspace guard and write authority;
- proof claim: writes stay inside the approved root;
- negative tests: traversal, absolute escape, symlink escape, and denied-action audit visibility;
- non-claims: not a production sandbox, not full agent security, not regulated-use adequacy;
- release decision: ship only as a scoped worked example with residual risk.

Best mode: Standard with Agent authority change and Controlled configuration workflows.

Outcome: Nuclear-grade clearly beats simple prompting.

### U3: Dependency Security Update

Simple prompting tends to collapse the task into "bump dependency and run tests." That can hide the difference between runtime compatibility and advisory posture.

Nuclear-grade improved the result by separating:

- behavior proof;
- dependency/advisory proof;
- lockfile or build evidence;
- rollback plan;
- revalidation trigger;
- ship decision.

Best mode: Standard with Controlled configuration and Release readiness workflows.

Outcome: Nuclear-grade is worth the overhead when dependency trust matters.

### U4: Public Assurance Wording

Simple prompting can make public docs sound more confident than the evidence supports. This is especially risky for a repo using high-consequence source lineage.

Nuclear-grade improved the result by forcing:

- source-map linkage;
- public-source status check;
- "inspired by" wording instead of "satisfies";
- explicit non-compliance and non-assurance boundaries;
- impact screening across README, templates, commands, skills, and validator wording.

Best mode: Standard with Source/legal check workflow.

Outcome: Nuclear-grade is strongly justified for public methodology claims.

### U5: Prompt/Model Baseline

Simple prompting tends to treat prompt/model updates as content edits. Nuclear-grade treats them as controlled configuration because they change agent behavior.

Nuclear-grade improved the result by requiring:

- prompt/model identity;
- accepted baseline;
- eval or review evidence;
- rollback to previous prompt/model state;
- re-baseline trigger when model, tool authority, prompt, or eval changes.

Best mode: Controlled configuration plus Release readiness.

Outcome: Nuclear-grade is strongly justified for agent behavior surfaces.

### U6: Validator Agent Handoff

Simple prompting gives the agent broad authority: inspect code, edit files, run tests, and "fix it." That may work, but the allowed scope is implicit.

Nuclear-grade improved the handoff by naming:

- role: builder/verifier;
- affected files;
- allowed commands;
- forbidden actions;
- evidence required before completion;
- stop condition when the change affects public docs or validator semantics.

Best mode: Quick if the validator fix is local and reversible; Standard if public validation semantics change.

Outcome: Nuclear-grade improves agent control, especially when multiple agents or long threads are involved.

## Skill-by-Skill Findings

| Skill | What worked | What did not |
|---|---|---|
| `questioning-attitude` | Best public hook. It found assumption gaps before build work in U2, U3, U4, U5, and U6. | It is overkill for U1 unless public wording or trust claims are involved. |
| `using-nuclear-grade` | Useful as an orchestration skill that routes to mode, packet, evidence, and decision. | It should stay concise; if it tries to explain the whole system every time, it becomes onboarding drag. |
| `identifying-controlled-items` | Strong for prompts, dependencies, public docs, validators, and agent permissions. | It should warn against whole-repo inventories; change-specific control lists are enough. |
| `screening-change-impact` | Caught stale docs, validator, template, and release-record risks. | It adds cost on isolated Quick changes. |
| `baselining-configuration` | Valuable for dependency, prompt/model, and release state. | Not useful before evidence is accepted; premature baselines create fake certainty. |
| `classifying-change-risk` | Prevented "small diff" rationalizations in U2, U3, U4, and U6. | Needs concrete examples in docs so users do not argue mode from vibes. |
| `creating-change-packets` | Made review artifacts durable and easy to validate. | Blank templates must not validate; the validator now catches unfilled prompts. |
| `packing-agent-context` | Reduced agent authority ambiguity and token waste. | Needs a one-screen example for common coding-agent handoff. |
| `proving-claims` | Most important quality upgrade: claims narrowed to evidence. | Users may need examples showing `gap` and `deferred` are valid statuses, not failures of the method. |
| `reviewing-ship-readiness` | Turned "tests passed" into a real ship/defer/block decision. | Heavy for non-release Quick work. |
| `checking-source-lineage` | Essential for public credibility and hostile reading. | Should avoid drowning users in source details; link to source map instead. |
| `checking-license-and-assurance-boundaries` | Prevented MIT/license permission from becoming implied assurance. | Must stay practical; it is not legal advice. |

## Workflow Findings

| Workflow | Best fit | Weak fit |
|---|---|---|
| Questioning attitude | Vague, consequential, public, or agent-authority work. | Tiny obvious edits. |
| Quick change | Docs typos, local reversible test edits, small cleanup with one proof. | Anything with user, dependency, data, agent authority, or release consequence. |
| Standard change | Agent permissions, dependency changes, public claims, validator behavior. | Purely local edits with obvious proof. |
| Controlled configuration | Prompts, models, tools, dependencies, public docs, validators, releases. | One-off scratch work. |
| Agent authority change | Any write, command, network, credential, approval, or release authority. | Explanation-only tasks. |
| Release readiness | Merges/releases with trust posture, rollback, monitoring, or residual risk. | Local unmerged work. |
| Source/legal check | Public docs, methodology claims, source lineage, assurance language. | Private code changes with no public claim. |

## Bottom Line

Nuclear-grade does not beat simple prompting on every task. It should not try to.

It wins when the change has one or more of these properties:

- AI agent authority;
- dependency or supply-chain trust;
- public assurance/source-lineage wording;
- prompt/model/tool configuration drift;
- release or rollback consequence;
- evidence gaps that must be accepted, deferred, or blocked.

Simple prompting is still better for tiny, local, reversible work when the proof is obvious and no durable review record is needed.

## Recommendations

1. Keep Quick mode very small and explicitly legitimate.
2. Add more one-screen examples for context packs, dependency updates, and prompt/model baselines.
3. Teach `gap` and `deferred` as first-class outcomes.
4. Keep "Questioning attitude" as the flagship hook.
5. Position Nuclear-grade as consequence-scaled evidence discipline, not universal process.

## Boundary Note

This comparison evaluates workflow usefulness for software review. It does not prove safety, security, compliance, certification, formal verification, formal validation, production suitability, or regulatory adequacy.

## Source-Lineage Note

This evaluation is an original Nuclear-grade adoption artifact using the repo operating model and public-source lineage summarized in `docs/00-standards-foundation/source-map.md`.
