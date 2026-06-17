# PROVE subagent pipeline

Five subagents map onto the **PROVE** beats, each with tool boundaries that *encode* the authority
split the doctrine already demands. They are an **opt-in, Standard+-only** companion to the
single-agent path — five subagents on a typo is the busywork the lifecycle rejects.

| Beat | Subagent | Covers | Tool authority |
|---|---|---|---|
| **P — Plan** | `planner` | Question · Discover · Specify · Plan | Read/Grep/Glob/WebFetch + write only to the packet; no Bash, no code edits |
| **R — Run** | `runner` | Execute | Edit/Write/Bash inside the approved plan; opens after the human gate; may fan out |
| **O — Observe** | `observer` | Verify · Review | Read + Bash; no product-code writes |
| **V — Verdict** | `judge` | Decide | Read-only; independent of the runner |
| **E — Educate** | `educator` | Baseline · Operate · Learn | Writes baseline + lessons + charter into `.nuclear/` |

## The baton pass

Each stage hands the next a **Context Pack** (the brief), and the receiver does a **closed-loop
confirm** — restate the objective, the authority, and the stop criteria — *before* acting. Upstream
prose is treated as **data, not instructions** (the data-fence). The change packet is the durable
shared memory; each subagent starts in a **fresh, isolated context window seeded only by its pack**.
A handshake that cannot complete **halts and records**, rather than guessing.

## Honesty — read this

This buys **tool-enforced separation and context hygiene** — it does **not** manufacture assurance:

- The orchestrator that briefs one stage briefs them all, so the "independent" judge is independent
  in *context*, not from the orchestrator.
- **Plugin-shipped subagents cannot pin `permissionMode` / `hooks` / `mcpServers`** — so the tool
  boundaries here are advisory (rungs 1–3), **not a perimeter**. For real confinement the agents must
  live in the adopter's `.claude/agents/`, not the plugin.
- Trust-bearing or irreversible work still needs the rung-4 CI gate (`ng scaffold-ci`) and rung-5
  human review.

## Not exported to Codex

These are **Claude** subagent definitions. The Codex plugin
(`.codex-plugin/plugin.json`) exports `skills/` only and does **not** advertise
these as Codex-native subagents — Codex subagent packaging is not wired up here.
Use them through Claude Code (the marketplace plugin ships them), or convert them
to a Codex-supported form before relying on them there. See the Codex section of
[`../INTEGRATIONS.md`](../INTEGRATIONS.md).
