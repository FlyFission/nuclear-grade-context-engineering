# Starter kits

Copy-paste-ready directories for the three most common adoption contexts. Each kit is a thin
shape, not a full vendored snapshot — you keep the skill files in their original locations (or
copy the ones your kit lists) and avoid maintaining duplicate copies as the framework evolves.

| Kit | Trigger | What it gives you |
|---|---|---|
| [`core/`](core/) | Every project | The seven core habits + an `AGENTS.md` skeleton + a `.nuclear/charter.md` skeleton + Quick-mode packet pointers. The base every other kit extends. |
| [`agent-authority/`](agent-authority/) | Your agent has write / run / network / approval authority over its own working set | Core + the Agent-authority cluster + a context-pack template + a pre-filled PR template that names the rung-ladder. |
| [`public-claims/`](public-claims/) | Your repo makes public claims about safety, security, compliance, licensing, or provenance | Core + the Claims-discipline cluster + a `BOUNDARY-WORDING.md` derived from `docs/00-standards-foundation/` + a DISCLAIMER skeleton. |

Each kit's `README.md` carries a five-line "drop this into your repo" command and lists the skills it expects you to copy.

See [`../CORE.md`](../CORE.md) for the decision matrix that picks the right kit, and the always-on packaging rule (vendor each chosen skill as a file; in always-on context put a one-line pointer per skill — not a fat doctrine block).

## Source-lineage note

These kits are an original packaging of patterns from this repository. They do not create assurance or any guarantee about how a system should behave. See [`../DISCLAIMER.md`](../DISCLAIMER.md).
