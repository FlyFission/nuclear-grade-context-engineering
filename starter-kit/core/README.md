# Starter kit: Core

Use this when you want the discipline without the full system. The Core 7 habits apply to every
disciplined AI-agent change; ancillary clusters from [`../../CORE.md`](../../CORE.md) layer on
when their triggers fire.

## Drop this into your repo

```bash
# from this repo's root, into your repo at $TARGET:
cp -r starter-kit/core/{AGENTS.md,.nuclear} "$TARGET"/
# then copy the seven core skill files:
for s in questioning-attitude rating-change-risk proving-claims \
         double-checking-before-acting staying-on-mission \
         checking-release-readiness learning-from-experience; do
  mkdir -p "$TARGET/skills/$s"
  cp "skills/$s/SKILL.md" "$TARGET/skills/$s/SKILL.md"
done
# and the two Quick-mode templates:
mkdir -p "$TARGET/templates/quick"
cp templates/quick/{risk.md,proof.md} "$TARGET/templates/quick/"
```

Then fill in the `<fill-in>` markers in `AGENTS.md` and `.nuclear/charter.md`.

## What this kit contains

- [`AGENTS.md`](AGENTS.md) — authority boundaries and a completion standard, derived from this
  repo's own AGENTS.md (its strongest exportable artifact) and trimmed with `<fill-in>` markers.
- [`.nuclear/charter.md`](.nuclear/charter.md) — a five-article charter skeleton: lasting rules
  every change follows.
- [`.nuclear/README.md`](.nuclear/README.md) and an empty `.nuclear/changes/` — the workspace
  skeleton `ng doctor` looks for. Equivalent to what `ng init` would create, so the kit-as-shipped
  passes `ng doctor` without requiring the CLI.

## The Core 7

| Skill | One-liner |
|---|---|
| `questioning-attitude` | The one fact that would change the decision. |
| `rating-change-risk` | Quick / Standard / stronger — the fork that sets every downstream cost. |
| `proving-claims` | Every claim maps to evidence, a gap, or an explicit non-claim. |
| `double-checking-before-acting` | Target / expected / stop, at every irreversible cut-point. |
| `staying-on-mission` | Three-strike anti-drift; re-anchor, escalate, or stop. |
| `checking-release-readiness` | Ship / block / defer / ship-with-named-risk — pick one and back it. |
| `learning-from-experience` | Every surprise updates a control. |

## Always-on packaging rule

In always-on context (CLAUDE.md, system prompt, agent config) put one-line pointers per skill —
not the skill bodies. The bodies load when the skill fires. See [`../../CORE.md`](../../CORE.md)
for the token-audit citation.

## Source-lineage note

This kit packages original patterns from this repository. It does not create assurance. See
[`../../DISCLAIMER.md`](../../DISCLAIMER.md).
