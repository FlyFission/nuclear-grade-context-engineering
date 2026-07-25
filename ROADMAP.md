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
- Retrievable memory store over `.nuclear/`: the optional MCP server already ships validation, doctor, status, and new-record tools; the future step is letting agents query past risk and decision records before proposing changes — opt-in, preserving deterministic CI as the default. When it graduates from discipline to a retrievable store, the production-memory patterns to draw on (episodic/working memory, graph-backed memory, MemGPT/Letta) are surveyed in the sources named in `docs/02-operating-system/durable-memory.md`.
- Optional semantic check above the deterministic validator: an opt-in LLM-as-Judge layer that asks whether the code satisfies `proof.md`. Per-change LLM auditing is the principled non-default (see `docs/02-operating-system/validators.md` line 3); opt-in is the principled extension.
- GitHub template repository (`nuclear-grade-starter`) so adopters can click "Use this template" for the Agent-authority kit (see `starter-kit/`).
- Richer status reports for active packets.
- Checks for release mode and incident mode once those patterns settle.
- Optional repeatable checking for HPI records, once real use proves the templates.

## Research-driven next steps

The 2026-07-19 novelty review narrowed the product center from a broad governance workflow to an
open implementation of **evidence custody and actor–evidence coupling in software acceptance**.
The next work should deepen that seam rather than add another generic approval framework.

1. **Finish the custody migration.** Keep `--strict-custody` opt-in while existing Standard packets
   migrate, then make the disclosure the default in the next breaking validator release.
2. **Protect raw evidence.** Add adapters for out-of-band CI, attestations, immutable or append-only
   result retention, and independent rerun receipts. Preserve the boundary: integrity and
   provenance do not prove adequacy or independence.
3. **Add a derived acceptance graph.** Build an optional local index over existing packet records:
   candidate → claim → evidence → custody → verifier → verdict → clearance → baseline → revalidation
   trigger. Markdown and Git remain the source of truth; the graph is a query and policy surface,
   not a Palantir clone or mandatory database.
4. **Make consequence policy executable.** Let teams declare minimum acceptable coupling profiles
   for named claim classes, then report dominance, incomparability, gaps, and required escalation
   without reducing the profile to one score.
5. **Run the blinded study.** Compare ordinary prompting, structured actor-authored evidence, and
   independently generated or witnessed evidence. Measure false acceptance, defect detection,
   reviewer calibration, evidence sufficiency, disagreement, decision time, and cost.
6. **Obtain external review.** Recruit software-assurance, empirical-SE, provenance, and AI-agent
   governance reviewers before making efficacy or venue-strength claims.
7. **Harden decision custody beyond records.** Bind approval to canonical action, policy, evidence,
   and V&V identities; issue scoped and expiring apply capabilities; consume or revoke them on use;
   and reject evidence swaps, payload mutation, replay, stale evidence, close without required lineage,
   and reuse of acceptance after reopen or supersession. The optional `decision-authority.md` and
   `--strict-authority` check are the structural first slice, not cryptographic or runtime enforcement.

### Deliberate non-goals

- Competing with Palantir, Foundry, or AIP on enterprise ontology or platform breadth.
- Claiming that ontology, provenance, authorization, workflow gates, human approval, or audit logs
  are novel.
- Replacing qualified engineering judgment with an automated coupling score.

## Not on the current roadmap

- We do not claim formal V&V, compliance, certification, safety, security, or regulatory adequacy.
- Replacing qualified legal, compliance, security, safety, or engineering review.
- Building a regulated quality assurance program from this public repo alone.

## Source-lineage note

This roadmap shows where an original, public-source-inspired workflow is headed. It is not a promise to meet any external standard.
