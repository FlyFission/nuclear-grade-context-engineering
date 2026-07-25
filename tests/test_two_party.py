"""Tests for nuclear_grade.two_party (two-party integrity gate).

Synthetic packets only: the authorship data this gate needs does not exist in
real packets yet (that gap is the point of the accompanying change packet).
"""

from __future__ import annotations

from pathlib import Path

from nuclear_grade.two_party import check_two_party

CLAIM_TABLE = (
    "## Claim-to-evidence table\n"
    "| Claim ID | method | criteria | Result status | link | gap |\n"
    "|---|---|---|---|---|---|\n"
)
AUTH_HEADER = (
    "## Claim authorship\n"
    "| Claim ID | Evidence author | Verified by |\n"
    "|---|---|---|\n"
)


def _packet(tmp_path: Path, claim_rows: str, authorship: str = "") -> Path:
    body = "# Verification\n\n" + CLAIM_TABLE + claim_rows + "\n" + authorship
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    return tmp_path


def test_distinct_parties_ok(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | - |\n",
        AUTH_HEADER + "| C-001 | agent:claude | ben |\n",
    )
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert messages == []


def test_self_verified_claim_blocks(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | - |\n",
        AUTH_HEADER + "| C-001 | ben | ben |\n",
    )
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("independent second party" in m for m in messages)


def test_missing_authorship_table_is_flagged(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("two-party integrity cannot be confirmed" in m for m in messages)


def test_empty_verifier_blocks(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | - |\n",
        AUTH_HEADER + "| C-001 | ben |  |\n",
    )
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("empty" in m for m in messages)


def test_non_pass_claim_needs_no_second_party_yet(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | gap | e | tbd |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert messages == []
