# OPEX Record — MCP v2 compatibility break

## Event

- Date: 2026-07-30
- Source: MCP Python SDK v2.0.0 release and failed `mcp-smoke` on PR #89
- Affected baseline: optional MCP integration introduced by PR #42
- Summary: `pip install mcp` began resolving to v2, which renamed `FastMCP` to
  `MCPServer`; the existing unbounded extra could no longer build the shipped server.

## Learning and action

| Finding | Weak or missing control | Impact | Action | Verification | Owner | Due / trigger |
|---|---|---|---|---|---|---|
| A lower bound did not preserve the v1 API contract across a major release. | The dependency declared `mcp>=1.0` without an upper compatibility bound. | Fresh optional-extra installs failed while the base package remained unaffected. | Bound the existing implementation to `mcp>=1.0,<2`; keep v2 migration separate. | Install the extra in a clean environment and run `tests/test_mcp_server.py`; require GitHub `mcp-smoke` to pass. | FlyFission | Revisit only with a deliberate v2 migration PR. |

## Required links

- Baseline record: `.nuclear/changes/integrations-cross-tool-install/ship.md`
- Related packet / issue / incident: `.nuclear/changes/integrations-cross-tool-install/`; PR #89 failed MCP smoke
- Verification evidence: `.nuclear/changes/integrations-cross-tool-install/verification.md`; MCP Python SDK v2.0.0 release and this PR's `mcp-smoke`

## Exit criteria

- Fresh optional-extra installs resolve to a compatible v1 release.
- The MCP smoke test passes without weakening or removing it.
- Migration to v2 remains an explicit, separately reviewed compatibility change.

## Source-lineage note

This operating lesson records a dependency compatibility correction against the
[MCP Python SDK v2.0.0 release](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0).
It makes no claim of formal assurance, compliance, safety, security, or regulatory adequacy.