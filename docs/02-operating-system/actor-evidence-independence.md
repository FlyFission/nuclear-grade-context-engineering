# Evidence Custody and Actor–Evidence Coupling

**Purpose:** Prevent a change actor from clearing an acceptance gate solely by controlling the evidence path that feeds it.

> A confident error can clear every gate for which it also wrote, selected, or framed the input.

This is a software-agent translation of an established self-review problem. Professional assurance, independent V&V, separation of duties, assurance cases, provenance systems, and LLM-evaluator-bias research are prior art. Nuclear-grade's contribution is narrower: make custody and coupling visible in repository-native software-change records and scale admissibility to consequence.

The filename remains `actor-evidence-independence.md` for link compatibility. The canonical model is now a multidimensional coupling profile, not an ordinal independence ladder.

---

## 1. The failure

The normal single-agent path is often:

1. the agent changes the candidate state;
2. the same agent chooses or writes the checks;
3. it executes or reports those checks;
4. it selects what results to retain;
5. it summarizes the evidence;
6. it frames the risk and release narrative;
7. a gate consumes that narrative.

The gate may be protected from direct editing and still receive no signal that escaped the actor's reasoning, omissions, or incentives. The resulting packet can be complete, persuasive, traceable, and wrong.

This does not mean agent-produced evidence is useless. It means its custody and residual coupling must be visible before a reviewer decides how much weight to give it.

---

## 2. Self-modification and evidence custody are different

| Boundary | Self-modification | Evidence custody |
|---|---|---|
| Question | Can the actor change the gate? | Can the actor control what the gate knows? |
| Typical failure | Editing the test or policy until the change passes | Generating, selecting, summarizing, or suppressing the evidence used to accept the change |
| Example | "Ships green by editing its own test" | "Ships green by writing a convincing trace for a change that does not work" |
| Primary defense | Put the gate outside the actor's writable set | Expose custody and introduce consequence-appropriate separation in the evidence path |

Closing either boundary without the other leaves a coupled acceptance path.

---

## 3. Evidence custody

For each trust-bearing claim, record who controlled these roles:

| Custody role | Question |
|---|---|
| Generated | Who created the evidence item or test artifact? |
| Selected | Who decided which checks, cases, samples, and outputs were shown? |
| Transformed | Who filtered, normalized, scored, compressed, or summarized the raw result? |
| Executed / captured | Who controlled the environment and captured the result? |
| Retained | Who could preserve, overwrite, omit, or delete adverse evidence? |
| Presented | Who wrote the narrative or claim-to-evidence mapping the decider received? |

A hash can show that retained bytes did not change. Provenance can show how an artifact was produced. Neither proves that omitted evidence did not exist, that the test addressed the claim, or that custody was independent.

---

## 4. Actor–evidence coupling profile

Independence is not one ladder. A human witness may share the actor's context and incentives; two agents may use different prompts but the same model and tests; an external model may still be starved by a budget the actor controls. Record five axes separately.

Use `coupled`, `partially separated`, or `separated`, followed by a concrete basis.

| Axis | Coupled when... | Separation evidence |
|---|---|---|
| **Actor** | the change actor also generates or witnesses the decisive evidence | a distinct verifier generates, reruns, or directly witnesses the decisive result |
| **Context** | the verifier receives only the actor's framing, summary, or selected packet | the verifier reconstructs scope and checks from source requirements, candidate state, and raw artifacts |
| **Mechanism** | actor and verifier share the same tests, oracle, model family, prompts, tools, or execution path | diverse tests, independent oracle, different model/tool path, or direct observation addresses correlated failure |
| **Authority** | the actor controls evidence scope, thresholds, sufficiency, verdict, or apply decision | those controls are owned by a reviewer, policy, protected CI, or operator outside the actor's authority |
| **Resource** | the actor controls verifier budget, runtime, credentials, environment, storage, or publication of adverse results | resources and result retention are protected from actor suppression or starvation |

The profiles form a **partial order**. One profile dominates another only when it is no more coupled on every axis and more separated on at least one. Do not add the axes, average them, or call a human review automatically superior to diverse deterministic verification.

---

## 5. Named evidence patterns

These are patterns, not assurance levels:

- **Actor narrative:** the actor reports that its own work is correct. Useful as a claim inventory; not independent evidence.
- **Actor-selected primary artifacts:** raw diffs, logs, screenshots, or traces chosen by the actor. Better inspectability; selection remains coupled.
- **Independent reproduction:** another party reruns a deterministic check against identified inputs and environment. Actor coupling falls, but a weak or actor-authored oracle may remain.
- **Diverse verification:** a separate verifier uses a materially different test, oracle, model/tool path, context reconstruction, or failure-mode analysis.
- **Direct witnessing:** a reviewer observes the decisive behavior or state transition. This can strengthen actor and authority separation while still sharing organizational or mechanism risk.

Name the pattern used, then record the five-axis profile. The pattern is not a substitute for the profile.

---

## 6. Scale admissibility to consequence

### Administrative floor

No packet is required only for purely administrative, instantly reversible work that crosses no trust boundary. The commit remains the record.

### Quick

Actor-produced evidence may be proportionate when the change is low consequence and easy to reverse. Record enough custody for the reviewer to know whether the proof is only narration, and prefer a command or artifact the reviewer can rerun.

### Standard

For each load-bearing claim:

- record the custody roles and five-axis profile;
- expose any shared tests, model family, context, environment, authority, and budget;
- use at least one signal that is not solely the actor's narrative or selected summary;
- keep the verdict owner explicit and separate current apply clearance from evidentiary sufficiency;
- carry unacceptable coupling as a named gap or residual risk rather than silently counting it as independent.

### High-consequence, irreversible, or external-trust work

Define the minimum acceptable profile before execution. Usually this requires multiple forms of separation: independent context reconstruction, diverse mechanisms, protected result retention, authority outside the change actor, and qualified human ownership of the decision. The exact profile is consequence-specific; this repository does not assign a regulatory class or create formal V&V.

---

## 7. The three coupled acceptance points

### Verify

The actor can choose tests that pass, omit adverse cases, transform outputs, or summarize a failing result as acceptable.

**Control:** preserve raw artifacts, record custody, and add independent reproduction or diverse verification where consequence warrants it.

### Review / verdict

A separate judge can still inherit the actor's framing, share its model family, use the same weak oracle, or receive too little budget to challenge the packet.

**Control:** record the judge's coupling profile, provide source requirements and raw evidence where appropriate, preserve disagreement, and block when the judge lacks room or authority to decide.

### Apply

A correct verdict can become stale when the candidate, target, authority, environment, maintenance window, or external state changes.

**Control:** retain verdict as an evidence judgment and re-check apply clearance against the exact candidate and current conditions.

---

## 8. What the PROVE roles do and do not prove

The planner, runner, observer, judge, and educator roles make custody seams visible and can reduce accidental context carryover. They do not manufacture independence by naming separate agents.

Ask:

- Were the roles briefed by the same orchestrator?
- Did they share the same model family, tests, tools, context, or execution environment?
- Could the actor edit the verifier's instructions or evidence store?
- Did the actor control the verifier's time, token budget, credentials, or ability to publish a failure?
- Did an out-of-band CI or human reviewer actually own the trust-bearing decision?

Tool separation is useful evidence about the profile. It is not a security perimeter or a guarantee of correctness.

---

## 9. Reviewer questions

For every load-bearing claim:

1. What exact candidate state is being accepted?
2. What evidence is decisive?
3. Who generated, selected, transformed, captured, retained, and presented it?
4. What is the actor–evidence coupling profile on all five axes?
5. Which correlated failures remain?
6. Why is that profile admissible for this consequence?
7. Who owns the evidence verdict?
8. What current conditions control apply clearance?
9. What event invalidates the evidence, verdict, clearance, or accepted baseline?

---

## Exit criteria

- Every trust-bearing claim exposes its decisive evidence and custody roles.
- The five coupling axes are recorded separately; no scalar independence score or rung is used.
- Actor-authored evidence is labeled honestly as a self-check unless another party independently reproduces or witnesses it.
- Any coupling below the consequence-specific requirement is a visible gap, residual risk, or blocker.
- The verdict owner and apply-clearance owner are explicit.
- Revalidation triggers are recorded.

## Source-lineage note

This is an original software-native operational synthesis informed by public work on professional self-review threats, independent V&V, assurance cases, AI-generated test review, LLM evaluator self-preference, provenance, and software-supply-chain attestations. Sources are mapped in `docs/00-standards-foundation/source-map.md`. It does not create compliance, formal V&V, safety, security, certification, or regulatory adequacy.
