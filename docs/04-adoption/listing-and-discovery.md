# Listing and discovery

How to get the Nuclear-grade skills into official, discoverable directories — beyond
installing from this repo with `ng install` (see [`../../INTEGRATIONS.md`](../../INTEGRATIONS.md)).

Two directories are worth submitting to today; the rest are deferred or not a fit. Steps
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
