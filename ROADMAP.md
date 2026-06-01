# Nuclear-grade Roadmap

Nuclear-grade Public v0 is a workflow you can use today, not a finished platform.

## Public v0

- Get-started-fast onboarding and a work breakdown (WBS).
- Quick and Standard templates.
- Templates for keeping the approved version under control (CM).
- A checker for Quick and Standard records.
- The local `tools/ng.py` command-line tool.
- Skills and paste-ready command prompts.
- One worked example, checked by tests.
- A public source foundation and boundary docs.
- HPI add-ons (small habits from Human Performance Improvement) for AI agents: questioning, briefing the work, self-checking, handing off, choosing how to verify, deciding on the careful side, trust checks, and learning from real operation (OPEX).

## v0.1

- Fuller briefing-pack examples.
- Better examples for controlled items and baselines.
- More record checks for a complete trace.
- Better link checks across the public docs.
- Starter policies for teams adopting packet review in pull requests.
- Sandbox-backed examples for handoff, self-check, OPEX, and trust in dependencies, models, and APIs.

## v0.2

- More worked examples for API controls and human approval steps.
- Optional packaging for specific agent platforms.
- Cross-tool renderers: official `.cursorrules`, Claude-Code-skill, Aider-conventions, and Copilot-instructions exports that consume the same `SKILL.md` source of truth, so the same discipline reads natively in each IDE.
- Optional MCP server over `.nuclear/`: agents query past risk and decision records before proposing changes; opt-in, preserves deterministic CI as the default.
- Optional semantic check above the deterministic validator: an opt-in LLM-as-Judge layer that asks whether the code satisfies `proof.md`. Per-change LLM auditing is the principled non-default (see `docs/02-operating-system/validators.md` line 3); opt-in is the principled extension.
- GitHub template repository (`nuclear-grade-starter`) so adopters can click "Use this template" for the Agent-authority kit (see `starter-kit/`).
- Richer status reports for active packets.
- Checks for release mode and incident mode once those patterns settle.
- Optional repeatable checking for HPI records, once real use proves the templates.

## Not on the current roadmap

- We do not claim formal V&V, compliance, certification, safety, security, or regulatory adequacy.
- Replacing qualified legal, compliance, security, safety, or engineering review.
- Building a regulated quality assurance program from this public repo alone.

## Source-lineage note

This roadmap shows where an original, public-source-inspired workflow is headed. It is not a promise to meet any external standard.
