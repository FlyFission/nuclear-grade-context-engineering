"""Tests for nuclear_grade.propagation (evidence-trust propagation gate).

Self-contained: builds synthetic packets in a tmp dir, no dependency on repo
packets or machine paths.
"""

from __future__ import annotations

from pathlib import Path

from nuclear_grade.propagation import (
    check_promotion,
    effective_status,
    parse_claim_statuses,
)

TABLE_HEADER = (
    "## Claim-to-evidence table\n"
    "| Claim ID | method | criteria | Result status | link | gap |\n"
    "|---|---|---|---|---|---|\n"
)


def _packet(tmp_path: Path, rows: str, deferred: str = "") -> Path:
    body = "# Verification\n\n" + TABLE_HEADER + rows + "\n" + deferred
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    return tmp_path


def test_effective_status_is_the_minimum():
    assert effective_status(["pass", "pass"]) == "pass"
    assert effective_status(["pass", "fail"]) == "fail"
    assert effective_status(["pass", "gap"]) == "gap"
    assert effective_status(["not applicable", "pass"]) == "pass"
    assert effective_status(["not applicable"]) == "not applicable"


def test_parse_reads_claim_and_status():
    text = (
        TABLE_HEADER
        + "| C-001 | m | c | pass | e | - |\n"
        + "| REQ-002 keeps writes bounded | m | c | gap | e | tbd |\n"
    )
    assert parse_claim_statuses(text) == [("C-001", "pass"), ("REQ-002", "gap")]


def test_all_pass_promotes(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | None |\n| C-002 | m | c | pass | e | None |\n",
    )
    messages: list[str] = []
    check_promotion(pkt, messages)
    assert messages == []


def test_one_fail_taints_the_packet(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | None |\n| C-002 | m | c | fail | e | broke |\n",
    )
    messages: list[str] = []
    check_promotion(pkt, messages)
    assert any("C-002" in m and "taints" in m for m in messages)


def test_silent_gap_blocks(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | gap | e | tbd |\n")
    messages: list[str] = []
    check_promotion(pkt, messages)
    assert any("C-001" in m for m in messages)


def test_bare_deferred_blocks_without_recorded_reason(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | deferred | e | later |\n")
    messages: list[str] = []
    check_promotion(pkt, messages)
    assert any("recorded reason" in m for m in messages)


def test_acknowledged_deferred_promotes(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | None |\n| C-002 | m | c | deferred | e | later |\n",
        deferred="## Deferred items\n\n- C-002: parked pending vendor data; tracked in issue 12.\n",
    )
    messages: list[str] = []
    check_promotion(pkt, messages)
    assert messages == []


def test_multi_letter_deferred_id_is_acknowledged(tmp_path):
    pkt = _packet(
        tmp_path,
        "| REQ-003 integration | m | c | planned | e | later |\n",
        deferred="## Deferred items\n\n- REQ-003: waiting for schema normalization.\n",
    )
    messages: list[str] = []
    check_promotion(pkt, messages)
    assert messages == []


def test_no_verification_file_is_noop(tmp_path):
    messages: list[str] = []
    check_promotion(tmp_path, messages)
    assert messages == []
