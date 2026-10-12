# Plan — ADR governance lessons and landscape benchmark

## Build sequence

1. REQ-001: in `nuclear_grade/mcp_server.py`, import `MCPServer` and fall back to `FastMCP`; set the `pyproject.toml` extra to `mcp>=1.0,<3`; give `mcp-smoke` a matrix over both majors.
2. REQ-002: add `nuclear_grade/receipt.py` and `--json` on `validate`; add `tests/test_receipt.py`.
3. REQ-003: add `concurrency`, the Python 3.13 leg, and the `CI gate` job to `.github/workflows/ci.yml`.
4. REQ-004: add `.github/dependabot.yml`.
5. Update `CHANGELOG.md`, `ROADMAP.md`, `validators.md`, `cli-reference.md`, and the `source-map.md` Tier 6 row.

Non-goals: version bump, tags, release workflow, new skills, and validation semantics.

## Proof commands

```bash
git diff --check
python -m pytest -q
python -m ruff check .
python tools/ng.py doctor .
python tools/ng.py tokens .
python tools/ng.py validate .nuclear/changes/adr-governance-benchmark --strict-custody
# REQ-001, 1.x leg, in a clean venv:
pip install "mcp>=1.0,<2" pytest && python -m pytest tests/test_mcp_server.py -q
```

## Required links

- Basis: [`basis.md`](basis.md)
- Trace: [`trace.md`](trace.md)
- Verification: [`verification.md`](verification.md)

## Exit criteria

Every proof command passes before commit. The CI matrix and gate are confirmed on the PR run.

## Source-lineage note

The plan applies patterns mapped in [`source-map.md`](../../../docs/00-standards-foundation/source-map.md). It makes no compliance claim.
