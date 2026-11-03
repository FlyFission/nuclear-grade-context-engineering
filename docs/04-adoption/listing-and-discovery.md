# Listing and discovery

How to get the Nuclear-grade skills into official, discoverable directories — beyond
installing from this repo with `ng install` (see [`../../INTEGRATIONS.md`](../../INTEGRATIONS.md)).

Two directories and one community list are worth submitting to today; the rest are
deferred or not a fit. Steps
marked **(repo)** are done here in this repository; steps marked **(you)** are manual
actions only a repository owner can take — a web form, or a PR to a repo this project does
not control.

## Claude Code — community plugin directory

Highest reach, lowest effort: this repo is already a valid Claude plugin marketplace.

- **(repo, done)** `claude plugin validate .` passes — the same validation the review
  pipeline runs — so no code change is needed to be submission-ready.
- **(you)** Submit at <https://platform.claude.com/plugins/submit> (individual authors, via
  the Console) or through claude.ai admin settings (Team/Enterprise). Choose a category in
  the form. Directory: <https://github.com/anthropics/claude-plugins-community>.
- After review and automated safety screening, the plugin is mirrored to the community
  marketplace; users then install with:

  ```bash
  /plugin marketplace add anthropics/claude-plugins-community
  /plugin install nuclear-grade@claude-community
  ```

## OpenAI Codex — openai/skills catalog

Community skills live in `skills/.experimental/<name>/` and install by URL; OpenAI may
later promote them to the curated tier. Codex reads only `name` + `description` for
routing, and the flagship skill already complies — but metadata compliance is not enough to
*work*.

The flagship skill is a **router**: its body points at repo-local artifacts
(`.nuclear/charter.md`, `WORKFLOWS.md`/`CORE.md`, the `python tools/ng.py` CLI). Installed from
the catalog **without this repository**, those targets are missing and the router dead-ends. A
single catalog skill cannot carry the charter, the docs, and the CLI, so treat this entry as a
**discovery pointer that bootstraps the repo**, not a self-contained skill.

- **(you)** Fork <https://github.com/openai/skills>, then add a folder:

  ```text
  skills/.experimental/using-nuclear-grade/
  ├── SKILL.md      # this repo's skills/using-nuclear-grade/SKILL.md + the bootstrap step below
  └── LICENSE.txt   # copy this repo's MIT LICENSE
  ```

- **(you)** Prepend a **bootstrap step** to the published `SKILL.md`: before it routes, have it
  install the full repo (clone it, or `ng install` from a local checkout) so the charter,
  `WORKFLOWS.md`/`CORE.md`, and the `ng` CLI it references exist. Without this, the catalog entry
  routes users into missing files.
- **(you)** Open a PR to `openai/skills` describing the skill and linking back here.
- Start with the single router skill — it is the entry point. Follow up with the Core 7 if
  it gets traction; submitting all skills at once fits their per-skill catalog poorly.

> This project's tooling cannot open that PR for you — `openai/skills` is outside its
> repository scope, so the fork and PR are your steps.

## Community list — awesome-ai-plugins

A curated, community-maintained README list run by Hashgraph Online (HOL), not a platform
directory: it adds discovery, not an install channel. The maintainers invited this listing in
[issue #105](https://github.com/FlyFission/nuclear-grade-context-engineering/issues/105).

- **Fit.** It belongs under **Community Plugins → Agent Skills**. The list's
  [`CONTRIBUTING.md`](https://github.com/hashgraph-online/awesome-ai-plugins/blob/main/CONTRIBUTING.md)
  requires one-sentence entries, alphabetical order within a section, recent activity, and,
  for Agent Skills, a README that documents tested install steps and supported clients.
- **(repo, done)** The root [`README.md`](../../README.md) documents the Claude Code install
  (Quick start) and names the supported clients (the opening summary, and the "Who it is for"
  line), with per-tool detail in [`INSTALL.md`](../../INSTALL.md) and
  [`INTEGRATIONS.md`](../../INTEGRATIONS.md).
- **(you)** Edit the list's
  [`README.md`](https://github.com/hashgraph-online/awesome-ai-plugins/edit/main/README.md)
  and add this line to Agent Skills, in alphabetical position:

  ```markdown
  - [nuclear-grade-context-engineering](https://github.com/FlyFission/nuclear-grade-context-engineering) - Agent skills, command prompts, and change-record templates that keep AI-assisted software work questioned, controlled, and reviewable.
  ```

- **(you)** In the PR body, give what their guide asks for: a one-line description, the repo
  link, the target section (Agent Skills), and a short verification note, such as
  `claude plugin validate .` passing and the README's one-command validator run.
- **Trust note.** The list runs its own source scan and publishes a "trust score" (their
  guide requires a normalized score of at least 75 before merge). That score is the list's
  own third-party signal. Do not cite it here as an assurance, security, or quality claim.
- After merge, close issue #105 with a link to the merged PR.

> This project's tooling cannot open that PR for you: `hashgraph-online/awesome-ai-plugins`
> is outside its repository scope, so the edit and the PR are your steps.

## Deferred / not a fit

- **MCP Registry** (registry.modelcontextprotocol.io, `mcp-publisher`): viable for the
  optional MCP server, but it needs a published package (e.g. on PyPI) plus namespace
  ownership and is still in preview. Revisit once the package is published.
- **VS Code Marketplace**: requires repackaging as a full VS Code *extension* (`vsce`), not
  skill files — out of proportion for this.
- **GitHub Copilot**: no clear public submission path for standalone skills as of writing.

## Verify before you submit

- Re-confirm the Claude form's fields and the `openai/skills` layout against current docs;
  both ecosystems move quickly.
- `claude plugin validate .` should still pass at submission time.

## Source-lineage note

This page records the public submission processes of third-party directories, captured from
their official docs and linked above. It makes no compliance, certification, or assurance
claim; see [`../../DISCLAIMER.md`](../../DISCLAIMER.md).
