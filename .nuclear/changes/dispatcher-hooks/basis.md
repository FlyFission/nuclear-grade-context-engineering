# Standard Basis

**Purpose:** State what must stay true for the advisory dispatcher hooks to be safe, honest, and reviewable.

---

## Change context

- Slug: dispatcher-hooks
- Related risk record: `risk.md`
- Owner: FlyFission
- Date: 2026-06-08
- Decision this basis supports: ship two advisory, opt-in session hooks.

## Mission / need

The directive dispatcher exists as a skill (advisory, auto-loaded). Adopters who want it *always-on* — injected every session and on every prompt — need hooks. Hooks are executable code, so they must add no exfiltration surface, must not auto-activate, and must not overclaim.

## Protected outcomes

| Protected outcome | Why it matters | Evidence needed |
|---|---|---|
| The hooks reach no network and run no subprocess | An in-session hook is your own process and could exfiltrate | network-ban test over hook sources |
| The injected text is static and never the prompt | Prevents instruction-laundering through the hook | no-prompt-echo test |
| The hooks are opt-in, not auto-activated | Keeps the no-hooks install the default (F2) | no `hooks/hooks.json` shipped; HOOKS.md enable step |
| No enforcement/assurance overclaim | The hooks are advisory (rung 1) | honesty note in the preamble + HOOKS.md |

## Unacceptable outcomes

| Unacceptable outcome | Consequence | Prevent / detect / mitigate |
|---|---|---|
| A hook phones home | Secret/SSH/env exfiltration | network-ban test (`socket`/`urllib`/`requests`/`http`/`subprocess`/...) |
| A hook echoes the user's prompt | Injected text laundered into context | no-prompt-echo test |
| Hooks auto-activate on plugin install | No-hooks default broken (F2) | ship no `hooks/hooks.json`; document manual enable |
| The preamble drifts from CORE.md | The router teaches a stale matrix | CORE.md cluster-sync test |
| Injection markers in the preamble | The preamble itself becomes an attack | injection-firewall test (F4) |

## Assumptions, constraints, and invalidation triggers

| Assumption / constraint | Fact / assumption / unknown | Basis or source | Invalidation trigger | Owner |
|---|---|---|---|---|
| `SessionStart`/`UserPromptSubmit` inject via `hookSpecificOutput.additionalContext` | fact | official Claude Code hooks docs | hook I/O schema change | FlyFission |
| Plugin `hooks/hooks.json` auto-activates; omitting it keeps hooks opt-in | fact | official docs | plugin hook-discovery change | FlyFission |
| A live Claude Code session is not exercised here | fact | no Claude Code runtime in CI | n/a | FlyFission |

## Grounding status

| Statement | Fact / assumption / unknown / source claim / local proof / decision authority | Evidence or source | Decision impact |
|---|---|---|---|
| The hooks emit valid, static, zero-network output | local proof | hook smoke-run + tests | Supports ship |
| The hooks inject as intended in a live session | unknown (deferred) | needs a live Claude Code session | Ship with residual risk; maintainer smoke-test |

## Interfaces and trust boundaries

- Internal interfaces affected: none (standalone scripts).
- External services/APIs affected: none — the hooks make no network calls.
- Data classes affected: none.
- Human approval boundaries: maintainer reviews executable code + runs a live session.
- AI/model/tool authority boundaries: unchanged — advisory injection, no blocking, no new authority.

## Derived requirements or claims

| ID | Requirement / claim | Basis | Design feature or control | Evidence planned |
|---|---|---|---|---|
| REQ-001 | THE SessionStart hook SHALL inject a static routing preamble (classify-first + two-speed + clusters + honesty) | always-on dispatcher | `session_start.py` PREAMBLE constant | smoke-run + test |
| REQ-002 | THE UserPromptSubmit hook SHALL inject a static line and SHALL NOT echo the prompt | no instruction-laundering | static CLASSIFY_LINE; drains stdin unused | no-echo test |
| REQ-003 | THE hooks SHALL be pure standard library with no network or subprocess use | no exfiltration surface | imports limited to `json`, `sys` | network-ban test |
| REQ-004 | THE hooks SHALL be opt-in (no auto-activation) | preserve no-hooks default (F2) | ship no `hooks/hooks.json` | absence check + HOOKS.md |
| REQ-005 | THE preamble SHALL stay in sync with CORE.md and within budget | no stale matrix / no bloat | cluster-sync + length tests | tests |

## Design outline

| Section | Covered? | Where it lives |
|---|---|---|
| Overview — what changes and why | yes | this basis + `risk.md` |
| Architecture — shape and major parts | yes | two stdin→JSON scripts + HOOKS.md |
| Components and interfaces — boundaries above | yes | `Interfaces and trust boundaries` |
| Data models — shapes, classes, ownership | n/a | no data models |
| Error handling — failure paths and responses | yes | `Unacceptable outcomes`; stdin drain is exception-guarded |
| Testing strategy — how each claim is checked | yes | `verification.md` |

## Required links

- Risk record: `risk.md`
- Verification record: `verification.md`
- Ship record: `ship.md`
- Product requirement / issue / ADR / design doc: the approved revised dispatcher design + F2/F4.
- Source lineage, if cited: not cited.

## Exit criteria

- The builder and reviewer can answer "what must stay true?"
- The protected outcomes and the outcomes to prevent are stated plainly.
- Important assumptions each have a trigger that would prove them wrong.
- The evidence needs flow into `verification.md`.

## Source-lineage note

Original Nuclear-grade record inspired by public ideas on human performance improvement and secure software supply chains, mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
