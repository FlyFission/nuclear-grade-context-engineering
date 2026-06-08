# Standard Risk

**Purpose:** Sort the dispatcher-hooks change by risk, justify Standard mode, and name the records turned on.

---

## Change identity

- Slug: dispatcher-hooks
- PR / issue: Add advisory, opt-in SessionStart + UserPromptSubmit dispatcher hooks
- Owner: FlyFission
- Date: 2026-06-08
- Current lifecycle phase: Decide
- Current work phase: accept
- Summary: Add two **advisory, opt-in** session hooks that make the directive dispatcher always-on: `hooks/session_start.py` injects a static routing preamble (classify-first + two-speed + the cluster map + an honesty note), and `hooks/user_prompt_submit.py` injects one static classification reminder. Both are **pure standard library, zero network, static output**. They are **not auto-activated** — this repo ships no `hooks/hooks.json`, so installing the plugin does not turn them on; the no-hooks install stays the default (security finding F2). `HOOKS.md` declares behavior, the security guarantee, and the manual enable step. `tests/test_hooks.py` guards the network ban, the no-prompt-echo property, the injection firewall, the budget, and CORE.md cluster-sync. The blocking PreToolUse gate is a deliberately-deferred separate tier.

## Mission anchor

- Objective: make the dispatcher always-on as opt-in hooks, with zero exfiltration surface and no overclaim.
- Success criteria: the hooks inject the static guidance, never echo the prompt, are pure-stdlib/zero-network, are opt-in, and are guarded by tests; the suite is green.
- Non-goals / forbidden directions: no auto-activation; no network/subprocess in hooks; no PreToolUse blocking gate (separate tier); no enforcement claim.
- Drift check: re-anchor / escalate / stop when an action stops serving the objective.
- Traces to: the approved plan (revised dispatcher; F2 no-hooks-default; F4 static-injection).

## Questioning-attitude summary

- Decision question: can the always-on dispatcher ship as hooks without adding an exfiltration surface or auto-activating?
- Evidence that would change the decision: a hook reaching the network, echoing the prompt, or auto-activating on plugin install.
- Assumptions that changed the mode: even advisory, opt-in hooks are executable code that runs in adopter sessions — a security-relevant surface — so Standard.
- Facts still needing validation: the live injection behavior on a real Claude Code session (verified here by the documented hook I/O contract + structure, not a live session).
- Stop or hold conditions: stop if a hook would need the network, echo untrusted input, auto-activate, or block tools.

## Affected configuration items

| Item | Type | Why it matters | Link |
|---|---|---|---|
| `hooks/session_start.py` | Hook (executable) | Injects the routing preamble | `hooks/session_start.py` |
| `hooks/user_prompt_submit.py` | Hook (executable) | Injects the classification reminder | `hooks/user_prompt_submit.py` |
| `HOOKS.md` | Doc | Declares behavior, security, enable steps | `HOOKS.md` |
| `tests/test_hooks.py` | Test | Guards the security + behavior properties | `tests/test_hooks.py` |

## Threshold screen

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Consequence | medium | Executable code that runs in adopter sessions; but advisory, opt-in, and static-output. |
| Reversibility | high | Delete the hooks + HOOKS.md + test; adopters disable by removing the settings.json entry. |
| Detectability | high | Network-ban, no-echo, firewall, sync, and budget tests; visible injected text. |
| Exposure | medium | Public; the hooks run on machines of adopters who opt in. |
| Uncertainty | low | Deterministic; the only unproven step is a live Claude Code session. |
| Dependency trust | low | Pure standard library; zero network; no new dependency. |
| AI authority | low | Advisory injection; the hooks cannot block or grant authority. |

## HPI work-mode screen

| Work mode / precursor | Present? | Control |
|---|---|---|
| Routine, repeated action where it is easy to stop paying attention | no | self-check / proof |
| Known procedure where following the steps matters | yes | packet path / deviation note |
| New or uncertain work where the assumptions may be wrong | yes | questioning attitude / research / review |
| Work that was interrupted, resumed, or handed off | no | turnover / context pack |
| A high-stakes critical action | no | self-check / peer-check / independent verification |

## Selected mode

- Mode: Standard
- Why this mode: it ships executable code that runs in adopter sessions — a security-relevant surface the review treated as critical — even though it is advisory and opt-in.
- Why lighter mode is not enough: Quick fits local reversible docs; executable hooks on adopter machines warrant a basis, plan, trace, and release decision.
- Why heavier mode is not yet required: advisory, opt-in, pure-stdlib, zero-network, static-output, reversible; the higher-risk blocking gate is deferred.

## Activated artifacts

| Artifact | Activated? | Reason | Owner |
|---|---|---|---|
| `questioning-attitude.md` | no | Captured inline in this risk record. | FlyFission |
| `basis.md` | yes | The security + behavior properties that must hold. | FlyFission |
| `verification.md` | yes | Evidence for the hook behavior + the guarantees. | FlyFission |
| `ship.md` | yes | Release decision for executable code. | FlyFission |
| `turnover.md` | no | Same agent continues; no handoff. | FlyFission |
| `self-check.md` | no | No irreversible critical action. | FlyFission |
| `supplier-trust.md` | no | No external dependency/model/API trust decision. | FlyFission |
| Nuclear subset record | no | Stakes below Nuclear. | FlyFission |

## Immediate evidence obligations

- Minimum evidence before build: the hook I/O contract (SessionStart/UserPromptSubmit) and F2/F4 hardening.
- Minimum evidence before merge/release: zero-network + no-echo + injection-firewall + sync + budget tests green; `pytest`/`ruff`/`doctor`/`tokens`/`validate` green.
- Independent review needed? yes; why: a maintainer should review executable code shipped to adopters and run a live session once.

## Required links

- Packet: `.nuclear/changes/dispatcher-hooks/`
- `basis.md`
- `verification.md`
- `ship.md`
- Source-map/crosswalk references if source lineage is invoked: not invoked.

## Exit criteria

- The mode is justified.
- The artifacts turned on are named.
- Important risks, assumptions, and evidence due are recorded here, not hidden in chat or commit messages.

## Source-lineage note

Original Nuclear-grade record inspired by public sources on human performance improvement, secure software supply chains, and graded rigor, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
