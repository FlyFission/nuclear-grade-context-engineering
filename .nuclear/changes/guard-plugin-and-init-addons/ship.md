# Ship: Guard plugin, deny-rule comparison, and `init` add-ons

## Release decision

**Decision: defer to human review.** The change is a local commit only. Nothing is pushed, and merge authority stays with the maintainer. Every new path is opt-in and reversible. The release stance does not change: no version bump and no tag. Because the guard plugin pins `version` to 0.6.0, users who install it get later gate changes only after a version bump.

Residual risk:

- E-001 to E-005 are self-checks by the AI agent that wrote the change. A CI run on a clean runner and a human reading HOOKS.md and the diff are the less-coupled checks still to come.
- E-007 is a gap: no live Claude Code session has run the plugin gate. The loader reports the hook, which is necessary and still short of proof.
- The new gate rules are text matches and can be defeated, like the existing ones. An agent that runs `nuclear-grade init --yes` can still overwrite `.nuclear/charter.md` from the shell; that predates this change and is not gated.
- A missing `python3` with the guard installed blocks every matched tool call. That is the intended fail-closed behavior, and INSTALL.md and HOOKS.md say how to remove the plugin.
- `init --hook` rewrites `.claude/settings.json` with two-space indentation when it adds the entry.

## Rollback

Revert the commit. Adopters run `/plugin uninstall nuclear-grade-guard@nuclear-grade`, or delete the gate entry and `.claude/hooks/pre_tool_use.py` that `init --hook` added. Nothing else holds state.

## Monitoring

Watch for false-positive asks on `.claude/plugins` paths, for reports that the plugin hook did not load, and for Claude Code changes to the plugin `hooks.json` format, `onFailure`, or exec form. If the host format changes, update the plugin, HOOKS.md, and `gate_hook_entry` together; the agreement test will flag a partial update.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

A human reviews the diff and HOOKS.md, CI passes on a clean runner, and the maintainer makes the merge decision.

## Source-lineage note

This is a repository change decision. It makes no compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
