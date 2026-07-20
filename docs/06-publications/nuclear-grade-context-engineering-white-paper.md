# From Context to Control

## A Graded, Evidence-First Method for Consequential AI-Assisted Software Changes

### The Nuclear-grade Context Engineering White Paper

**Discussion Draft v0.1 — superseded**<br>
**Ben Huffer, FlyFission Consulting Group**<br>
**19 July 2026**

> **Superseded:** This practitioner draft preserves the v0.1 argument for editorial history. The current manuscript is *Who Authored the Evidence? Actor–Evidence Coupling in AI-Assisted Software Acceptance* under `docs/06-publications/arxiv/`. It replaces the ordinal independence rungs with a five-axis partial-order profile, incorporates the expanded prior-art review, and treats the twelve scenarios as formative design inspection rather than efficacy evidence.

**Assessed repository baseline:** [`FlyFission/nuclear-grade-context-engineering`](https://github.com/FlyFission/nuclear-grade-context-engineering), commit `7144831`<br>
**Paper source and implementation:** [public repository](https://github.com/FlyFission/nuclear-grade-context-engineering)<br>
**License:** The repository is MIT-licensed. Final publication terms for this paper remain to be selected.

> **Status and boundary.** This is a discussion draft for editorial and technical review. Nuclear-grade is an educational software-engineering method inspired by public high-consequence engineering, software-assurance, cybersecurity, systems-engineering, and context-engineering sources. It is not a compliance framework, certification product, regulated quality-assurance program, safety analysis, regulatory submittal, or substitute for qualified engineering, legal, security, safety, or compliance review.

---

# Abstract

AI coding agents no longer only suggest code. They inspect repositories, modify files, call tools, change prompts and dependencies, generate tests, summarize their own work, and increasingly prepare or execute release actions. This broad authority creates a control problem that task-oriented context engineering does not fully answer. A context can help an agent complete a task while still leaving unclear what the agent was authorized to change, which claims matter, who authored the evidence, what decision the evidence supports, and which accepted state should remain under control.

This paper presents **Nuclear-grade Context Engineering**, a graded, Git-native method for engineering the context around consequential AI-assisted software changes. The method specializes context engineering for **accountability** as well as capability. It combines a questioning attitude, consequence-scaled change records, controlled agent operating envelopes, claim-to-evidence traceability, explicit release decisions, configuration baselines, and learning from operation. Its central distinction is **actor–evidence independence**: preventing an agent from editing its own gate is insufficient when that agent also authors the evidence, review narrative, and risk framing the gate consumes. At trust-bearing gates, the load-bearing evidence should instead be independently reproducible or independently authored, with the degree of independence scaled to consequence.

The public repository implements the method through Markdown change packets, context packs, skills, command prompts, role-separated agent instructions, a Python command-line interface and validator, tests, continuous integration, starter kits, and worked examples. A twelve-scenario author-judged comparison and a mechanical signal-presence harness provide preliminary design evidence, not controlled proof of effectiveness. The contribution claimed here is therefore an **original synthesis, operational formulation, and implementation**, not the invention of configuration management, independent verification, graded rigor, assurance arguments, or context engineering as individual ideas. The paper closes with limitations and a research agenda for blinded, independently scored evaluation.

**Keywords:** context engineering; AI coding agents; configuration management; evidence; independent verification; agent authority; software assurance; change control; human oversight

---

# Executive summary

The current generation of coding agents can produce a plausible change and a plausible explanation of why that change is correct in the same run. This creates an unusually coherent failure mode. If the agent is wrong, the error can propagate into the code, the tests it selected, the evidence it summarized, the pull-request narrative it wrote, and the release recommendation it framed. A conventional review gate may remain formally present while receiving no information independent of the reasoning process that produced the change.

Nuclear-grade addresses that problem with three commitments:

1. **Fast exploration, slow acceptance.** Drafts remain cheap and disposable. Rigor rises when work becomes a promise: a public claim, a controlled item, an accepted baseline, a release decision, or a change to what an agent may do.
2. **Minimum sufficient control.** The method uses the smallest packet and the fewest controls that can honestly support the decision. Low-stakes work should remain light. Consequential work earns deeper evidence and more independent review.
3. **Independent evidence at trust-bearing gates.** An actor's narration of its own result is a claim about evidence, not the independent verification of that evidence. The load-bearing claim should be checked through a reproducible mechanism, an out-of-band verifier, or a human whose authority and budget are not controlled by the actor.

The method is carried by a lifecycle:

```text
Question → Discover → Specify → Plan → Execute → Verify → Review
         → Decide → Baseline → Operate → Learn
```

The lifecycle is not intended to create eleven meetings or eleven documents. A purely administrative, instantly reversible change can remain below the packet threshold. A Quick change uses two short files. A Standard change uses a six-file evidence spine. Stronger records activate only when consequence, uncertainty, outside trust, autonomous authority, or irreversibility earns them.

The resulting contribution is best understood as **context for accountable acceptance**: a narrower specialization within context engineering. Most adjacent work asks what information helps a model perform or how context should be governed. Nuclear-grade also asks:

- What is the agent allowed to do?
- Which items must remain under control?
- Which claims carry the decision?
- Who authored the evidence relative to the actor?
- What would falsify or reopen the decision?
- Who may decide that the candidate is acceptable?
- Is an accepted change also authorized to be applied now?
- Which baseline records the state people agreed to trust?

The repository demonstrates that this approach can be expressed as ordinary version-controlled artifacts and executable checks. It does not establish that the method reduces defects, improves safety, or outperforms other workflows in production. Those remain empirical questions.

---

# 1. The accountability gap

## 1.1 Coding agents change more than code

A modern coding-agent session can read a repository, infer conventions, draft a specification, edit product code, add tests, run commands, fetch packages, call APIs, revise documentation, and prepare a release summary. The context that shapes this work is not limited to a prompt. It includes repository instructions, retrieved files, tool schemas, permissions, memory, current state, examples, and the immediate task.

That broader understanding of context is now common in context-engineering literature and practice. Public surveys describe the inference-time payload in terms such as instructions, knowledge, tools, memory, state, and queries.[1] Anthropic emphasizes the finite nature of model attention and the value of the smallest set of high-signal tokens that can produce the desired behavior.[2] Repository-instruction formats such as `AGENTS.md`, and spec-driven projects such as GitHub Spec Kit and Product Requirements Prompt workflows, make task instructions and validation steps durable inside the codebase.[3][4][5]

These approaches address an important problem: agents fail when the information needed for the task is absent, disordered, stale, conflicting, or too diffuse. But better task context does not by itself answer the governance question created by agent authority. A complete blueprint can still authorize too much. A validation gate can still test the wrong claim. A long trace can still be selected and narrated by the actor whose work it is meant to validate.

The key distinction is between **context for performance** and **context for accountable acceptance**. The first helps the agent produce a result. The second helps a reviewer determine whether the result should become a trusted state.

## 1.2 The review loop can manufacture persuasive evidence

In a typical AI-assisted path, one agent may:

```text
interpret the request
  → design the change
  → implement the change
  → choose or write tests
  → run the checks
  → summarize the evidence
  → explain the residual risk
  → recommend merge or release
```

Each step can be reasonable in isolation. The coupling is the problem. When one reasoning process produces both the candidate and the case for accepting the candidate, agreement between them carries less information than it appears to carry.

This is not primarily a deception problem. An honest agent that is wrong can create a wrong implementation, a test that misses the same misunderstanding, and a coherent explanation of why both are correct. Fluency turns correlation into persuasion. The review process may retain a gate in form while losing independence in substance.

Nuclear-grade names this the **self-authorship boundary**. It is the dual of the more familiar self-modification boundary:

| Failure path | What the agent controls | Example | Primary defense |
|---|---|---|---|
| Self-modification | The gate itself | The agent edits the test, CI workflow, or approval rule until the work passes | Put the gate outside the actor's writable set |
| Self-authorship | The information consumed by the gate | The agent writes the evidence, narrative, and risk call that say its change is correct | Make the evidence independently reproducible or independently authored |

A control the agent cannot edit is necessary, but it is not sufficient if the agent wrote everything that flows into that control. This leads to the paper's central proposition:

> **At a trust-bearing gate, the load-bearing evidence should have an author independent of the actor, or be reproducible by an independent party. The actor's narration of its own evidence is a claim, not the independent verification of that claim.**

## 1.3 Acceptance is where the rigor belongs

The answer is not to make every coding task heavy. Agents are useful partly because they make exploration cheap. A method that requires a formal review package for a typo or a disposable prototype destroys the value it is supposed to protect.

The more precise boundary is acceptance. Work becomes trust-bearing when it creates or changes something another person, system, customer, or future maintainer will rely on. Examples include:

- a public or contractual claim;
- a permission, prompt, model, dependency, or tool that changes agent behavior;
- an accepted configuration baseline;
- a release recommendation;
- a data, payment, security, or operational behavior;
- a difficult-to-reverse design decision;
- an authorization to take a real-world action.

Nuclear-grade therefore uses two speeds: fast candidate work and slower acceptance. The transition between them is explicit rather than rhetorical.

---

# 2. Related work and contribution boundary

## 2.1 Established foundations

The method deliberately builds on established ideas. Its novelty does not depend on pretending those ideas are new.

**Configuration management and baselines.** Public DOE and NRC sources describe configuration management as preserving consistency among requirements or design basis, the current configuration, and associated records.[6][7] In ordinary software, Git provides version history, but a commit alone does not state why a version was accepted, what evidence supported it, which gaps were accepted, or what event requires revalidation.

**Lifecycle discipline, verification, and independent review.** NASA's public software-engineering requirements and handbook material address lifecycle evidence, independent verification and validation, and tool qualification.[8][9] NRC software regulatory guides address software lifecycle processes, requirements, testing, verification and validation, and configuration management.[10] Nuclear-grade treats these as conceptual lineage, not requirements it implements.

**Secure software and AI risk.** NIST's Secure Software Development Framework provides public secure-development practices, while the NIST AI Risk Management Framework organizes AI risk work around govern, map, measure, and manage functions.[11][12] NIST SP 800-160 emphasizes systems-security engineering, trustworthy systems, and resilience.[13]

**Assurance arguments.** Safety- and assurance-case literature uses structured claims, arguments, evidence, and defeaters. Recent work has explored safety cases for frontier AI and the use of language models to identify defeaters in assurance cases.[14][15] Nuclear-grade does not claim to create a formal assurance or safety case. It adopts the narrower discipline of making decision-bearing claims and their evidence visible.

**Graded rigor and human performance.** High-consequence engineering commonly scales controls to consequence and uses practices such as questioning assumptions, task preview, self-checking, independent verification, turnover, and learning from operating experience. DOE-HDBK-1028-2009 is a central public source for these Human Performance Improvement concepts.[16]

Each of these components is prior art. The paper's claim is not their invention.

## 2.2 Adjacent context-engineering and coding-agent work

Context engineering has developed along at least two complementary tracks. Research surveys organize memory, retrieval, context-window behavior, tool use, state, compaction, and observability.[1] Practitioner projects make coding-agent work more reliable through repository instructions, staged specifications, reusable skills, examples, and validation loops.[3][4][5]

The overlap with Nuclear-grade is substantial:

- repository instructions define standing behavior;
- specifications make intent durable;
- validation gates connect implementation to executable checks;
- examples and skills make context reusable;
- role-separated agents can divide planning, execution, and review;
- observability records what an agent did.

Recent first-party engineering accounts and empirical work on repository-level instructions also reinforce a useful boundary: more standing instruction is not automatically better. Concise navigation, repository-specific exceptions, executable feedback, and evidence-bearing tools can be more valuable than a monolithic overview.[17][18]

Agent-harness and benchmark work adds another boundary. Anthropic's long-running-agent harness uses durable progress files, Git history, incremental work, and end-to-end self-verification.[22] SWE-agent shows that the agent–computer interface materially shapes repository behavior and task performance.[23] SWE-bench Verified introduced human-screened tasks and tests outside the solving agent, a useful benchmark-level precedent for actor–evidence separation.[24] OpenAI later stopped using the benchmark for frontier-model evaluation because contamination and flawed tests had weakened the judge itself.[25] Independent execution helps, but it cannot rescue stale, invalid, or compromised evidence.

Two recent papers are particularly close to the governance side of this work. Xu et al. propose a persistent file-system abstraction for governed context, including access control, provenance, traceability, auditable state transitions, and human roles in verification.[20] Zhang and Sun's Knowledge-Based Pull Requests separate an external knowledge package from project-side code generation and distinguish knowledge acceptance from implementation integration across a trust boundary.[21] These works materially overlap any broad claim that accountable context, durable provenance, human governance, or decision separation is unique to Nuclear-grade.

Nuclear-grade occupies a narrower point on this map. It does not attempt to be a complete context taxonomy, a memory system, a retrieval framework, a contribution gateway, or a one-shot feature-development workflow. It treats those as neighboring capability mechanisms. Its specialization is a consequence-graded acceptance lifecycle for trust-bearing changes: explicit authority before action, claim-matched evidence, actor–evidence independence at selected gates, controlled agent operating envelopes, and a distinction between an engineering verdict and present authorization to apply an action.

## 2.3 Contribution ledger

The contribution is best bounded as follows:

| Candidate contribution | Classification in this paper | Safe treatment |
|---|---|---|
| Configuration management, baselines, traceability, independent verification, graded rigor | Established prior art | Credit public sources; do not claim invention |
| Repository instructions, context packs, spec-driven development, validation gates | Established or adjacent practice | Describe overlap and difference |
| Accountable or governed context engineering | Shared direction in adjacent work | Credit context-governance, provenance, and human-control work; do not claim the broad category |
| Context for accountable acceptance | Original synthesis and narrower specialization | Define around trust-bearing decisions, not generic context governance; avoid a priority claim |
| Self-modification versus self-authorship | Original operational formulation pending broader review | Present precisely; invite falsification and prior-art correction |
| Actor–evidence independence rungs | Original software-native translation and method element | Ground in IV&V and segregation-of-duty lineage |
| Prompts, models, tools, evals, and instructions as a controlled operating envelope | Configuration-management translation and implementation contribution | Credit CM; show the agent-specific application |
| Verdict versus apply-clearance | Operational state-model refinement | Present as a useful distinction, not a universal standard |
| Git-native change packets and executable checks | Implementation contribution | Demonstrate through repository artifacts |
| PRO/PROVE mnemonic | Pedagogy and branding | Use as a handle, not evidence of novelty |

The result is a systems contribution: an original composition and operationalization of established disciplines around a specific failure mode in AI-assisted software work.

---

# 3. Design requirements

Nuclear-grade was designed against six requirements.

## 3.1 Preserve the speed of exploration

The method must not make expensive controls the default. Candidate work should remain easy to create, inspect, discard, and retry. Administrative changes that cross no trust boundary need no packet. Low-stakes changes should use a compact proof record. Stronger artifacts activate only when they change a decision.

## 3.2 Make authority explicit before action

An agent's context should state not only what outcome is desired, but what the agent may read, write, execute, call, claim, approve, and release. It should also state what requires human approval and what condition forces the agent to stop.

For unattended agents, “ask first” is not a useful runtime control because no human may be present to answer. The operational form must be **block, record, and escalate**.

## 3.3 Tie evidence to the claim and decision

A green test suite is evidence about the behavior that suite exercises. It is not a general release decision. Each load-bearing claim should identify:

- the protected outcome or requirement;
- the control or design feature intended to satisfy it;
- the evidence type and status;
- the gap or residual risk;
- the decision the evidence supports.

Evidence labels such as `pass`, `fail`, `gap`, `deferred`, and `not applicable` reduce the temptation to let missing evidence disappear into prose.

## 3.4 Break common-cause coupling at trust-bearing gates

A second check is valuable only to the extent that it can fail differently from the first. Two runs of the same model with the same brief and method may be redundant without being independent. Nuclear-grade therefore asks which diversity axis changed: model family, context, mechanism, authority, or human judgment.

## 3.5 Keep the accepted state under control

Prompts, models, tools, permissions, eval sets, instructions, dependencies, and public claims can change system behavior as materially as code. When their accepted version matters, they should be treated as controlled items with evidence, a decision, a baseline, and revalidation triggers.

## 3.6 Learn from operation without rewriting history

Incidents, near misses, drift, review surprises, and user confusion should change a lasting control: a requirement, test, monitor, threshold, template, skill, or baseline. A lesson that remains only in chat is not an operating improvement.

---

# 4. The Nuclear-grade method

## 4.1 One lifecycle, several levels of detail

The full lifecycle is:

```text
Question → Discover → Specify → Plan → Execute → Verify → Review
         → Decide → Baseline → Operate → Learn
```

The same path can be compressed into **PROVE**—Plan, Run, Observe, Verdict, Educate—or into **PRO**—Plan, Run, Operate. The mnemonic is not the method's intellectual contribution. Its value is navigational: users can zoom from a three-part mental model to the full set of decision points without switching frameworks.

| Phase | Decision question | Minimum useful output |
|---|---|---|
| Question | What decision must the evidence support, and what assumption could change it? | Decision question, doubts, stop conditions |
| Discover | What repo facts, prior records, and sources matter? | Bounded source and state inventory |
| Specify | What must remain true? | Requirements, protected outcomes, unacceptable outcomes |
| Plan | How will controlled state change? | Steps, authority, affected items, rollback, proof |
| Execute | Did the actor stay inside the approved plan and authority? | Candidate diff, actions, deviations |
| Verify | What evidence supports each important claim? | Tests, evals, reviews, status, gaps |
| Review | Can a skeptical reviewer decide from primary artifacts? | Claim-to-evidence and work-product review |
| Decide | Should the candidate become accepted? | Ship, block, defer, or accept-with-risk verdict |
| Baseline | What accepted state is now controlled? | Version, included items, evidence, gaps, recheck triggers |
| Operate | What signals show drift or failure? | Monitoring and incident triggers |
| Learn | What lasting control changes because of operation? | OPEX/corrective update or explicit closure |

The lifecycle is an information model, not a meeting schedule. Several phases can be represented in a few lines for a small change.

## 4.2 Graded modes

The method scales the artifact spine to the stakes.

| Level | Typical use | Artifact spine | Review expectation |
|---|---|---|---|
| Administrative floor | Typo, comment, dead link; instantly reversible; no trust boundary | Commit message only | Normal diff review |
| Quick | Local, reversible, easy to prove, no new trust boundary | `risk.md`, `proof.md` | Reviewer reruns the proof |
| Standard | User-visible or lasting change; dependency, data, permission, prompt, model, agent authority, or release impact | `risk.md`, `basis.md`, `plan.md`, `trace.md`, `verification.md`, `ship.md` | Important claims linked to evidence and an explicit decision |
| Stronger/Nuclear subset | Severe, silent, difficult-to-reverse, high-uncertainty, external-trust, or autonomous action | Standard plus only the records earned by the risk | Independent review scaled to consequence |
| Incident/Research Board/Release | Operational failure, major uncertainty, or release-bearing decision | Specialized record with the relevant evidence and decision | Human ownership and explicit closure |

This graded structure is essential to the method's economics. Nuclear-grade should lose to a direct prompt on tiny work if the comparison is overhead. The framework earns its cost only where the cost of missing a hidden risk, authority boundary, evidence gap, or rollback condition is larger.

## 4.3 Change packets as the Git-native object

The central implementation object is a folder:

```text
.nuclear/changes/<change-slug>/
```

A Standard packet contains:

```text
risk.md
basis.md
plan.md
trace.md
verification.md
ship.md
```

The packet does not replace the pull request, issue tracker, tests, or CI. It links them around one decision. `risk.md` selects the mode. `basis.md` states what must remain true. `plan.md` bounds the build and rollback. `trace.md` connects the claim to the implementation and evidence. `verification.md` records evidence type, status, independence, and gaps. `ship.md` records the verdict, residual risk, rollback, monitoring, handoff, and baseline trigger.

Links are preferred to copies. The packet is useful when a reviewer can move from intent to evidence and decision in minutes. It has failed when it becomes a junk drawer or repeats the repository.

## 4.4 Context packs as authority-bearing task context

A context pack is a task-specific view of the packet and the repository. It can carry:

```text
role
mode
objective and mission anchor
current phase and resume point
affected files
allowed and forbidden actions
surface classifications
required evidence
approval gates
stop conditions
relevant source lineage
open gaps
next action
```

This makes the context payload accountable. Instructions, knowledge, tools, memory, state, and query are still present, but they are arranged around a bounded task and decision. The pack says what the agent should ignore as well as what it should read.

## 4.5 Controlled agent operating envelopes

Traditional configuration management is often applied to source code, binaries, requirements, interfaces, and release artifacts. Agentic software adds behavior-driving surfaces:

- system and repository prompts;
- model identifiers and settings;
- tool lists and schemas;
- permissions and credentials policy;
- eval cases and scoring rubrics;
- agent skills and command prompts;
- retrieval rules, memory, and context packs;
- release and approval instructions.

Nuclear-grade treats these as part of the **agent operating envelope** when changes to them can alter trusted behavior. A useful baseline records the accepted versions, the evidence behind acceptance, the gaps carried forward, and the trigger that requires a new check.

---

# 5. Actor–evidence independence

## 5.1 Why self-checks are not independent checks

Self-checking remains useful. An agent should inspect its diff, run tests, verify targets, and expose errors before asking for review. The problem arises when a self-check is allowed to stand in for the independent evidence the consequence requires.

Nuclear-grade distinguishes five rungs:

| Rung | Gate input | Main weakness | Suitable use |
|---|---|---|---|
| 1 | Actor narrates: “tests pass; change is correct” | The actor can be wrong fluently | Drafting only |
| 2 | Actor supplies primary artifacts it selected | Selection can be stale, incomplete, or fabricated | Reversible local work |
| 3 | Independent party reruns a deterministic check and reads the output | The check itself may not address the claim | Low-stakes reproducible evidence |
| 4 | Independent verifier or out-of-band CI authors decisive evidence | Shared brief or orchestrator can still create common-cause bias | Trust-bearing work inside a controlled environment |
| 5 | Independent human witnesses/authors decisive evidence and owns the decision | Human error or rubber-stamping remains possible | Irreversible or external-trust decisions |

These rungs are not an assurance scale and do not assign a regulatory class. They make a simpler fact visible: who authored the evidence relative to the actor, and what could make both fail together?

## 5.2 Independence has several axes

NASA's public IV&V material describes technical, managerial, and financial dimensions of independence.[8] Applied to AI-assisted work:

- **Technical independence** asks whether the check uses a different mechanism or merely repeats the builder's method.
- **Managerial independence** asks whether the reviewer can set scope and block acceptance independently of the thing under review.
- **Budget independence** asks whether time or token limits can starve the verifier into a shallow pass.

The budget translation matters for agents. A verifier that must fit into the actor's remaining context window or that can be terminated when it becomes inconvenient is not fully independent. It may be separate in name and captured in operation.

Independence also requires diversity. A unit test, a type checker, and a human domain review can fail in different ways. Three agents using the same model, prompt, retrieved context, and rubric may express one blind spot three times. The question is not “how many reviewers?” but “which common-cause path was broken?”

## 5.3 The actor's evidence remains valuable—properly labeled

The method does not discard actor-generated traces, test output, or explanations. They are useful inputs to review. The distinction is epistemic:

- “I ran this command and it passed” is a claim about evidence.
- Raw output tied to a commit is a primary artifact selected by the actor.
- A reviewer rerunning the command raises independence.
- Out-of-band CI the actor cannot rewrite raises enforcement and independence further.
- A human decision owner remains necessary where the consequence or external trust requires one.

This framing prevents a common overcorrection. Not every claim needs a second model or human witness. Independence rises with the consequence carried by the claim.

## 5.4 A biased judge remains a separate failure mode

Independent authorship is not sufficient when the judge is systematically biased. LLM-as-judge work identifies position, verbosity, self-preference, confidence, sycophancy, scale, and exemplar-distribution effects. Nuclear-grade therefore treats evaluation integrity as a complementary control:

- randomize order where order can influence a pairwise judgment;
- prefer anchored labels over unbounded scores;
- judge primary artifacts rather than the actor's preferred conclusion;
- withhold the actor's recommendation when it would bias the judge;
- use disagreement to escalate instead of averaging it away;
- reserve panels and meta-judges for decisions where they earn their cost.

A separate agent reading the same biased brief is not automatically an independent verifier. Role separation helps only when tool boundaries, context boundaries, decision rights, and common-cause risks are real.

---

# 6. Authority and state

## 6.1 Surface classification

Before an agent acts, reachable surfaces can be classified:

| Surface class | Agent authority | Examples |
|---|---|---|
| Locked | May not modify | Gate, required CI, approval policy, protected tests |
| Editable under review | May change through the normal change flow | Product code, draft docs, candidate packet |
| Append-only | May extend but not rewrite prior entries | Logs, deficiencies, operating lessons |
| Human-controlled | May not change | Credentials, final release decision, governing charter |

A gate in the actor's editable set is advisory. An append-only log that the actor can rewrite is not append-only. Classification makes the authority model concrete enough to review.

## 6.2 Plan authority and build authority are different

During Question, Specify, and Plan, an agent can remain read-only over product code while writing only to the change record. Build authority opens after a human-approved or out-of-band plan gate. This temporal separation prevents a planner from silently becoming an implementer before the constraints are accepted.

The same logic applies later. Execute produces a candidate, not an accepted state. Verify and Review produce evidence and analysis, not the final authorization. Decide accepts, blocks, or defers the candidate.

## 6.3 Verdict and apply-clearance are different states

A release **Verdict** answers:

> On the evidence, is this candidate correct enough and worthwhile enough to become the accepted version?

**Apply-clearance** answers:

> May this accepted change be applied now, under the current approvals, external state, maintenance window, and operational policy?

The states often align in ordinary software and diverge in consequential operation. A freeze window can close. An approval can lapse. External state can change after verification. A rollback path can become unavailable. A correct change can therefore be worth releasing without being authorized for immediate application.

A ship verdict is not a standing authorization. Clearance is time- and context-sensitive and belongs to the operator or policy owner. This distinction becomes increasingly important as agents move from preparing changes to acting on external systems.

---

# 7. Implementation

The public repository implements the method as a tool-agnostic set of ordinary files plus small executable checks.

## 7.1 Repository surfaces

The public baseline assessed for this draft includes:[19]

- a canonical lifecycle, modes, authority model, configuration-management model, and source foundation;
- Quick, Standard, and optional stronger templates;
- reusable agent skills with trigger conditions, inputs, outputs, verification, and stop rules;
- paste-ready command prompts;
- role instructions for Plan, Run, Observe, Verdict, and Educate stages;
- starter kits for adopting only the needed subset;
- a Python package and CLI;
- a structural validator, repository doctor, token-budget audit, and efficacy signal checker;
- tests and continuous integration;
- a public worked example and qualitative comparison records;
- citation metadata and explicit disclaimer boundaries.

The CLI and validator check structure, links, status fields, placeholder removal, and boundary wording. They do not determine whether an engineering claim is true. That limit is intentional. Structural lint can expose missing evidence; it cannot replace engineering judgment.

## 7.2 Tool-agnostic by design

The method is represented primarily in Markdown and Git so it can be used with different coding agents, editors, CI systems, model providers, and orchestration frameworks. Tool-specific packaging can improve ergonomics, but the evidence record should survive the replacement of any one model or agent runtime.

This is a configuration-management choice as much as a portability choice. The accepted claim, evidence link, and decision should not disappear when a chat session expires or a vendor changes an API.

## 7.3 Minimum sufficient context as a measured constraint

The repository treats context as a cost and failure surface. Always-loaded instructions are kept short; deeper skill bodies load when their trigger fires. Token audits measure prose surfaces, and the framework explicitly rejects adding doctrine that does not improve execution, verification, review, or decision quality.

This is where accountability and context efficiency reinforce one another. A focused context pack makes authority and evidence easier to see while reducing unrelated material that can distract or conflict with the task.

---

# 8. Worked example: agent tool permissions

The repository's principal worked example changes what an AI agent may do. The candidate agent may read approved project context, write only under an approved workspace, call approved APIs using scoped credentials, request human approval for exceptional actions, and emit tool-use evidence. It may not write outside the workspace, use traversal or symlink tricks to escape, call arbitrary APIs, misuse credentials, bypass approvals, or conceal denied actions.

The change is Standard rather than Quick because it crosses an authority boundary. The controlled items include permissions, prompts, tools, credentials policy, evals, and logs. The packet contains:

```text
risk.md
basis.md
plan.md
trace.md
verification.md
ship.md
adversarial-review.md
```

The evidence chain is deliberately narrow:

| Claim | Control | Evidence | Status |
|---|---|---|---|
| C-001: writes stay inside the approved workspace | Normalize paths, reject traversal, enforce allowlist, log denial | Pytest covers allowed write, `../` traversal, absolute path, and symlink escape | Pass |
| C-002: external calls require approved tools and scoped credentials | Proposed registry and credential binding | Future unit and integration tests | Deferred |
| C-003: high-impact actions require approval | Proposed policy engine and immutable approval record | Future scenario evaluation | Deferred |
| C-004: denied actions are observable | Structured denial events | Denied-write tests cover the C-001 path; broader evidence remains open | Partial pass |

This example demonstrates three method properties.

First, the mode is selected by authority and consequence, not by the size of the code diff. Second, one complete claim-to-evidence chain is preferred over a wide table of implied assurance. Third, deferred claims remain visible rather than borrowing confidence from the passing workspace-boundary test.

What the example does **not** prove is equally important. It does not show that the service is broadly secure, production-ready, compliant, or safe. It proves the tested workspace-boundary behavior on the sample implementation and exposes the claims that remain open.

---

# 9. Preliminary evaluation

## 9.1 Twelve artifact-comparison scenarios

The repository contains twelve paired scenarios comparing a reasonable direct-prompt path with the corresponding Nuclear-grade records. The scenarios include a tiny README fix, an agent workspace boundary, a dependency update, public assurance wording, a prompt/model baseline, an agent handoff, payment-webhook idempotency, a data-retention migration, a release cut, an incident regression, external API permission, and a source-citation adoption document.

Each artifact pair was scored from one to five on:

- decision clarity;
- hidden-risk discovery;
- evidence quality;
- ship-or-defer usefulness;
- overhead, scored separately.

The qualitative results show the intended pattern. On the tiny documentation fix, the two paths were within one point on every decision-quality axis, and the Nuclear-grade path added overhead. On scenarios involving authority, data, payments, release posture, prompt/model baselines, or public assurance wording, the Nuclear-grade artifacts surfaced more decision-relevant structure and scored higher under the author's rubric. The stronger path also cost more overhead in every case.

These scores are **author-judged design evidence**. They are not a blinded experiment, a model benchmark, an independent panel result, or evidence of reduced defects. No production outcomes, review time, completion time, token cost, or inter-rater agreement were measured. The repository states these limits directly and invites replication.

## 9.2 Mechanical signal-presence harness

A small efficacy harness reads selected trial artifacts and checks whether required decision signals remain present. Examples include bounded file-write authority, adversarial proof claims, separation of source inspiration from satisfied requirements, credential boundaries, rollback, monitoring, and residual-risk ownership.

The harness is useful as a regression guard: an example cannot silently drop a decision element without failing the check. It is reproducible and extensible. It does not assess whether the element is handled adequately in a real system, and it does not mechanize the direct-prompt comparison.

## 9.3 What the evidence supports

The current public evidence supports the following bounded conclusions:

- the method is coherent enough to be represented as reusable artifacts;
- the implementation is runnable and testable;
- the worked example demonstrates one claim-to-evidence path and visible gaps;
- the qualitative scenarios illustrate where the method is intended to add decision structure and where it is intended to be unnecessary;
- the signal harness protects selected examples from losing named decision elements.

The evidence does not establish safety, security, compliance, production suitability, defect reduction, or superiority over other development methods.

---

# 10. Adoption and overhead

## 10.1 Start with the decision, not the framework

A team should not adopt the entire repository before it has a consequential change. The first question is:

> What decision must the evidence support, and what fact would change that decision?

For a reversible local edit, the answer may be one proof command. For an authority-changing feature, the answer may require a basis, boundary tests, independent evidence, rollback, monitoring, and an explicit decision owner.

## 10.2 Triggers matter more than inventory

Nuclear-grade skills and records are intended to load by trigger:

- a public claim triggers source and boundary review;
- agent write or network authority triggers an authority model and adversarial proof;
- a dependency triggers intended-use and trust evidence;
- data or payment changes trigger stronger rollback and monitoring;
- a release triggers a Verdict, residual-risk disposition, and apply-clearance;
- an incident triggers stabilization, fact-versus-hypothesis discipline, and lasting corrective action.

This keeps the method from becoming a checklist whose mere completion is mistaken for assurance.

## 10.3 Organizational fit

The method is most likely to help teams that:

- use coding agents with file, command, network, or release authority;
- produce changes that customers or downstream teams rely on;
- need a durable explanation of why a prompt, model, dependency, or release was accepted;
- work in security-sensitive, mission-critical, infrastructure, financial, healthcare, industrial, or regulated-adjacent environments;
- want stronger review without adopting a tool-specific orchestration platform.

It is less useful for disposable prototypes, tiny reversible edits, or teams unwilling to maintain the accepted baseline and act on operating lessons.

## 10.4 The framework can fail by accretion

A method about minimum sufficient control can defeat itself by continuously adding templates, terms, gates, and instructions. The repository therefore treats subtraction as an improvement. A record or rule should remain only if it changes execution, evidence, review, decision quality, or operational learning.

This is not merely an ergonomics preference. Excess context can dilute the unusual constraints that matter, increase inference cost, create conflicting instructions, and consume reviewer attention. The control system must protect itself from becoming the dominant source of noise.

---

# 11. Limitations and threats to validity

## 11.1 Novelty is bounded, not absolute

This paper claims an original synthesis, operational formulation, and implementation. It does not claim that no prior work has combined any subset of these concepts. The context-engineering and agent-governance fields are moving quickly, terminology is unstable, and relevant practices may appear in internal systems or recent publications not represented in the current source map.

The self-modification/self-authorship distinction and the narrower framing of context for accountable acceptance should therefore be treated as falsifiable contribution claims subject to continued prior-art review.

## 11.2 The evaluation is not independent

The author designed the scenarios, produced or curated the artifacts, and scored the comparison. This creates confirmation risk even with explicit bias controls. The same project also authored the mechanical signal definitions. Transparency makes the evidence inspectable; it does not make it independent.

## 11.3 Artifact quality is not operational outcome

A better change record may improve a reviewer's decision without improving the underlying implementation. Conversely, a poor record may accompany correct code. Future studies must measure whether the method changes omission detection, review accuracy, time, cost, escaped defects, rollback quality, or operational outcomes.

## 11.4 Independence can be simulated rather than achieved

Separate agents can share a model, prompt, retrieved context, orchestrator, evaluation rubric, and budget owner. This reduces some direct coupling while preserving common-cause failure. Tool labels such as “reviewer” and “judge” should not be mistaken for technical, managerial, or budget independence.

## 11.5 Human gates can rubber-stamp

A human owner is not a guarantee. Review quality depends on competence, time, authority, incentives, access to primary evidence, and willingness to block. Nuclear-grade can expose these conditions but cannot manufacture them.

## 11.6 Public source lineage is intentionally incomplete

The project uses public, open, linkable sources for direct lineage and excludes paywalled or proprietary standards from template derivation. This improves reproducibility and licensing clarity but means the method is not a comprehensive representation of nuclear, safety-critical, or quality-assurance practice.

## 11.7 “Nuclear-grade” can miscalibrate readers

The name signals a standard of care and the author's professional lineage. It can also sound like a formal quality or regulatory claim. The repository and this paper therefore state repeatedly that the method does not implement or certify compliance and should be renamed in local adoption if the branding would create false assurance.

---

# 12. Research agenda

A second-stage empirical paper should freeze a tagged method version and preregister a controlled protocol.

## 12.1 Core study design

1. Select six to ten scenarios across the graded modes, including low-stakes tasks where the method is expected to lose on overhead.
2. Hold scenario facts, model/tool access, and stopping conditions constant across a direct-prompt path and a Nuclear-grade path.
3. Generate complete artifacts and remove path-identifying branding where feasible.
4. Randomize presentation order and blind independent reviewers to the treatment.
5. Use multiple reviewers with relevant software, security, agent-engineering, and high-consequence experience.
6. Score decision clarity, omission/hidden-risk detection, evidence adequacy, release-decision correctness, and inappropriate confidence.
7. Measure reviewer time, agent time, token/cost overhead, disagreement, and inter-rater reliability.
8. Publish prompts, artifacts, rubric, exclusions, failures, and negative results.

## 12.2 Specific research questions

- Does actor–evidence independence reduce acceptance of changes containing deliberately seeded, correlated implementation-and-evidence defects?
- Which independence axis—different mechanism, different model, independent CI, or human review—produces the greatest marginal benefit at a given cost?
- At what consequence threshold does the Standard packet improve decision quality enough to justify its overhead?
- Does explicit Verdict/apply-clearance state reduce stale or context-inappropriate deployment actions?
- Do configuration baselines for prompts, models, tools, and evals improve drift detection and incident reconstruction?
- Which packet fields are frequently unused and should be removed?

## 12.3 Field evidence

Longitudinal adoption studies could examine whether teams:

- record and close evidence gaps rather than hiding them;
- detect agent-authority drift earlier;
- preserve release rationale across staff and model changes;
- improve rollback and incident learning;
- reduce review time after the method becomes familiar;
- continue to scale rigor rather than defaulting to the heaviest mode.

The framework should be revised or reduced when evidence shows that a control does not change decisions or outcomes.

---

# 13. Conclusion

Coding agents make candidate work cheap. They also make it cheap to generate a coherent case for accepting that work. The resulting risk is not only that an agent can make a mistake. It is that one reasoning process can produce the mistake, the test that misses it, the evidence summary that conceals it, and the release narrative that makes it persuasive.

Nuclear-grade Context Engineering responds by treating context as part of a control system. The task context includes authority, controlled items, claims, evidence duties, stop conditions, and decision state. Rigor rises when work becomes trust-bearing. Evidence is tied to the claim it supports. The accepted version is baselined with its gaps and revalidation triggers. Lessons from operation update lasting controls.

The central seam is actor–evidence independence. Keeping a gate outside the actor's writable set closes self-modification; keeping the actor from solely authoring the gate's input closes self-authorship. Neither creates assurance, and both can fail through common-cause bias or weak human review. They do, however, make a consequential question visible:

> **What information at this gate did not come from the same process that produced the change?**

That question is the paper's proposed extension to the context-engineering conversation. Context should help an agent perform, but consequential context should also help a reviewer decide what to trust.

The current repository demonstrates a coherent, implemented method and provides transparent preliminary design evidence. Independent effectiveness evidence remains open. The appropriate next step is therefore not a broad assurance claim, but public technical review, replication, and a controlled empirical study.

---

# Appendix A. Compact practitioner model

## A.1 The minimum decision record

For any consequential AI-assisted change, answer:

```text
Decision: What are we deciding?
Basis: What must remain true?
Authority: What may the agent do, and where must it stop?
Change: What candidate state was produced?
Evidence: What supports each load-bearing claim, and who authored it?
Verdict: Should the candidate become accepted?
Clearance: May it be applied now?
Baseline: What state is trusted, with which gaps and recheck triggers?
Learning: What operating signal will change a lasting control?
```

## A.2 Five review questions

1. Could the actor edit the gate?
2. Did the actor author all information the gate consumed?
3. Which common-cause path could make the change and its evidence wrong together?
4. Is the release Verdict being mistaken for current apply-clearance?
5. What accepted baseline and revalidation trigger remain after the decision?

---

# References

1. Lingrui Mei et al., “A Survey of Context Engineering for Large Language Models,” arXiv:2507.13334v2, 2025; with the related public *Awesome Context Engineering* curation repository. [arXiv](https://arxiv.org/abs/2507.13334) · [Repository](https://github.com/Meirtz/Awesome-Context-Engineering). Accessed 2026-07-19.
2. Anthropic, “Effective context engineering for AI agents,” September 29, 2025. [Article](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Accessed 2026-07-19.
3. `AGENTS.md`, “a simple, open format for guiding coding agents,” README commit `557da8b`, December 10, 2025. [Pinned repository revision](https://github.com/agentsmd/agents.md/tree/557da8b39c6f5b4dee2239df09a6ab97a82ff4df).
4. GitHub, *Spec Kit: Spec-Driven Development toolkit*, release `v0.13.0`, July 17, 2026. [Pinned release](https://github.com/github/spec-kit/tree/v0.13.0).
5. Cole Medin, *Context Engineering Intro* and Product Requirements Prompt workflow. [Repository](https://github.com/coleam00/context-engineering-intro). Accessed 2026-07-19.
6. U.S. Department of Energy, *DOE-STD-1073-2016, Configuration Management*. [Public source](https://www.energy.gov/ehss/articles/doe-std-1073-2016).
7. U.S. Nuclear Regulatory Commission, *Regulatory Guide 1.169 Rev. 1, Configuration Management Plans for Digital Computer Software Used in Safety Systems of Nuclear Power Plants*, July 2013. [Official PDF](https://www.nrc.gov/docs/ML1235/ML12355A642.pdf).
8. NASA Software Engineering Handbook, *SWE-141: Software Independent Verification and Validation*, aligned to NPR 7150.2D. [Official handbook requirement](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695499/SWE-141+-+Software+Independent+Verification+and+Validation).
9. NASA Software Engineering Handbook, *SWE-136: Software Tool Accreditation*, aligned to NPR 7150.2D. [Official handbook requirement](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation).
10. U.S. Nuclear Regulatory Commission, *Regulatory Guide 1.168 Rev. 2, Verification, Validation, Reviews, and Audits for Digital Computer Software Used in Safety Systems of Nuclear Power Plants*, July 2013. [Official PDF](https://www.nrc.gov/docs/ML1307/ML13073A210.pdf).
11. National Institute of Standards and Technology, *Secure Software Development Framework (SSDF) Version 1.1*, NIST SP 800-218, 2022. [DOI](https://doi.org/10.6028/NIST.SP.800-218).
12. National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 2023. [DOI](https://doi.org/10.6028/NIST.AI.100-1).
13. National Institute of Standards and Technology, *Systems Security Engineering*, NIST SP 800-160 Volumes 1 and 2. [Volume 1 Rev. 1 DOI](https://doi.org/10.6028/NIST.SP.800-160v1r1) · [Volume 2 Rev. 1 DOI](https://doi.org/10.6028/NIST.SP.800-160v2r1).
14. Marie Davidsen Buhl et al., “Safety Cases for Frontier AI,” arXiv:2410.21572v1, 2024. [arXiv](https://arxiv.org/abs/2410.21572).
15. Usman Gohar, Michael C. Hunter, Robyn R. Lutz, and Myra B. Cohen, “CoDefeater: Using LLMs To Find Defeaters in Assurance Cases,” arXiv:2407.13717v2, 2024. [arXiv](https://arxiv.org/abs/2407.13717).
16. U.S. Department of Energy, *DOE-HDBK-1028-2009, Human Performance Improvement Handbook*. [Public source](https://www.energy.gov/ehss/articles/doe-hdbk-1028-2009).
17. Ryan Lopopolo, OpenAI, “Harness engineering: leveraging Codex in an agent-first world,” February 11, 2026. [Article](https://openai.com/index/harness-engineering/).
18. Thibaud Gloaguen et al., “Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?”, arXiv:2602.11988v2, revised June 23, 2026. [arXiv](https://arxiv.org/abs/2602.11988).
19. FlyFission, *Nuclear-grade Context Engineering* public repository and source foundation. [Repository](https://github.com/FlyFission/nuclear-grade-context-engineering) · [Source map](https://github.com/FlyFission/nuclear-grade-context-engineering/blob/main/docs/00-standards-foundation/source-map.md) · [Disclaimer](https://github.com/FlyFission/nuclear-grade-context-engineering/blob/main/DISCLAIMER.md).
20. Xiwei Xu, Robert Mao, Quan Bai, Xuewu Gu, Yechao Li, and Liming Zhu, “Everything is Context: Agentic File System Abstraction for Context Engineering,” arXiv:2512.05470v1, 2025. [arXiv](https://arxiv.org/abs/2512.05470).
21. Xinyu Zhang and Weiwei Sun, “Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge Collaboration,” arXiv:2606.26721v1, 2026. [arXiv](https://arxiv.org/abs/2606.26721).
22. Justin Young, Anthropic, “Effective harnesses for long-running agents,” November 26, 2025. [Article](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
23. John Yang et al., “SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering,” arXiv:2405.15793v3; NeurIPS 2024. [arXiv](https://arxiv.org/abs/2405.15793v3).
24. OpenAI and the SWE-bench collaboration, “Introducing SWE-bench Verified,” August 13, 2024; updated February 24, 2025. [Article](https://openai.com/index/introducing-swe-bench-verified/).
25. OpenAI, “Why we no longer evaluate SWE-bench Verified,” February 23, 2026. [Article](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified).

---

## Author and drafting note

Ben Huffer is the founder of FlyFission Consulting Group and the author/maintainer of Nuclear-grade Context Engineering. This discussion draft was prepared with AI-assisted research, drafting, editing, and local verification. The human author retains responsibility for the contribution claims, source interpretation, final wording, and any decision to publish. AI-generated material is not treated as independent verification of the method or the manuscript.
