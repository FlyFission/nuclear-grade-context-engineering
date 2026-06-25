# Glossary

Plain-language decoding of Nuclear-grade terms and idioms. The skills and docs use a dense, idiomatic register; this page is the translation layer so the workflow is legible to readers who are newer to the vocabulary or to English.

## Core terms

| Term | Plain meaning |
|---|---|
| Packet | A small folder of Markdown files (`.nuclear/changes/<slug>/`) that records one change: what it is, why it matters, what proves it, and the release decision. |
| Mode | How much rigor a change earns: Quick (tiny), Standard (consequential), or a stronger human-reviewed pattern. |
| Quick mode | Low-consequence, reversible work with obvious proof and no new trust boundary. Two files: `risk.md`, `proof.md`. |
| Administrative floor | Below Quick. A purely administrative, instantly reversible change that crosses no trust boundary (typo, comment, dead link, doc-only bump). No packet — the commit message is the record. Any trust boundary, dependency, public claim, or hard-to-reverse step lifts it to at least Quick. |
| Standard mode | Work with user, data, dependency, permission, AI-authority, or release consequence. Six files. |
| Controlled item | Anything whose approved state matters to trust: code, prompts, models, dependencies, docs, releases, tools. |
| Baseline | The accepted state of controlled items at a decision point, plus what would make it stale. |
| Mission anchor | The objective, success criteria, and explicit non-goals a change traces back to. Guards against drift. |
| Charter | The durable, non-negotiable principles of how all work here is done, independent of any one change. |
| Evidence status | A label on a claim: `pass`, `fail`, `gap`, `deferred`, `not applicable`, or `planned`. |
| HPI overlay | A small control behavior (brief, self-check, turnover, verify, decide, learn) layered on a change only when it changes the work. |
| OPEX | Operating experience: turning a near miss, bad handoff, or review surprise into a durable control update. |
| Turnover | Handing unfinished work to another agent or person with state, remaining scope, authority limits, and open evidence. |
| Context pack | A focused briefing for an agent: role, authority, evidence obligations, forbidden actions, stop conditions. |
| Source lineage | A note saying which public sources influenced a concept, without claiming compliance with them. |
| Attention budget | The finite capacity a model has to use what is in its context window; every token spends some of it. |
| Context rot | Slow decay in a model's recall and focus as its context window fills up across turns. |
| Context poisoning | A wrong or hallucinated "fact" enters the context early and keeps getting cited as if verified. |
| Context confusion | Too many tools or irrelevant documents in scope, so the agent picks the wrong one. |
| Context clash | Two sources in the context contradict each other and the agent oscillates or loops. |
| Context collapse | Re-summarizing a long-lived document over and over until its useful detail is gone. |
| Brevity bias | Compression that keeps fluent prose but drops the load-bearing specifics (commands, limits, exact wording). |
| Stage contract | An explicit interface for one workflow stage or delegable slice: its Inputs (exact sections), Process, Outputs, the gate that accepts it, and what is deterministic vs model-mediated. Minimal form is a stage `CONTEXT.md`; full form is `templates/standard/stage-contract.md`. |
| Control plane vs execution plane | The control plane is the interpretable, reviewable layer (Git, markdown, stage contracts, baselines); the execution plane is where work and side effects happen (tools, agents, CI, durable runtimes). Stage contracts live in the control plane; the gate that enforces them sits in the execution plane. |
| Determinism posture | A disclosure of what a stage can reproduce and what it cannot: the model id, prompt, and temperature/seed for model-mediated steps, and which steps are replayable vs human-judgment. A disclosure, not a guarantee that a model step repeats. |
| Actor-evidence independence | At a trust-bearing gate, the evidence must have an author independent of the actor, or be reproducible by an independent party. The dual of the self-modification boundary: that one stops the agent editing its gate; this one stops it being the sole author of the gate's input. |
| Self-authored evidence | Evidence, a narrative, or a decision the actor produced about its own work. It is a claim to be verified, not the verification — a confident error produces it just as readily as a sound change does. |
| Independence rung | How independent the author of a gate's input is from the actor, on a 1–5 ladder (1 = the actor narrates; 5 = an independent human authors or witnesses it). Match the rung to the consequence, like the enforcement rungs. |

## Idioms used in the skills

| Idiom | What it actually means |
|---|---|
| "Rigor must earn its keep" | Only add a control if it changes a decision, reduces cost, or increases trust. Otherwise cut it. |
| "Earns its keep" (an abstraction) | A wrapper or layer must remove more complexity than it adds, or delete it. |
| "Drift theater" | Restating the mission without honestly re-checking whether the current action still serves it. Going through the motions. |
| "Postmortem theater" | Writing an incident review that changes no durable control. Motion without learning. |
| "A small erosion is a finding, not a rounding error" | Do not wave off a minor drop in standards; record it as a real issue. |
| "Bad news travels up intact" | Report problems immediately and without softening them. |
| "Prefer boring over clever" | Direct, obvious code beats clever indirection that is hard to read later. |
| "Prefer deletion over rearrangement" | The strongest fix for complexity is removing structure, not moving it around. |
| "Green CI is not a release argument" | Passing tests do not, by themselves, justify shipping. |
| "Confidence is not a source" | An agent sounding sure is not evidence; verify the fact. |
| "Front door" (questioning attitude) | The first skill to apply before building: challenge assumptions. |
| "Normalization of deviance" | Letting standards slip one accepted exception at a time until the exception is the norm. |

## Source-lineage note

This glossary is an original plain-language aid for the Nuclear-grade workflow. It does not create formal V&V, compliance, certification, safety, security, or regulatory adequacy.
