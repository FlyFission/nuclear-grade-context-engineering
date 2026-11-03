# Ship: Menu descriptions for the command cards

## Release decision

**Decision: defer to human review.** The change goes up as a draft pull request, and merge authority stays with the maintainer. The release stance does not change: no version bump and no tag.

Residual risk:

- Claude can no longer call an `ng-*` card on its own. The paired skills still load on their own; if the maintainer wants the cards callable too, remove one line from the generator and regenerate.
- No live session has opened the `/` menu with the plugin installed (gap E-006).

## Rollback

Revert the commit and run `python tools/ng.py gen-commands`. Nothing else holds state.

## Monitoring

Watch for reports that a command no longer runs on its own, and for Claude Code changes to command frontmatter.

## Required links

- Risk: [`risk.md`](risk.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

A human reviews the diff, CI passes on a clean runner, and the maintainer makes the merge decision.

## Source-lineage note

This is a repository change decision. It makes no compliance, certification, safety, security, or regulatory-assurance claim. See [`source-map.md`](../../../docs/00-standards-foundation/source-map.md).
