import json
from pathlib import Path

from nuclear_grade.badge import build_badge, summarize
from nuclear_grade.cli import packet_health
from tests.test_ng_cli import run_ng
from tests.test_ng_validate import minimal_quick_packet, minimal_standard_packet


def test_empty_repo_badge(tmp_path):
    assert build_badge(summarize(tmp_path, packet_health))["message"] == "none yet"


def test_clean_records_are_green(tmp_path):
    minimal_quick_packet(tmp_path)
    badge = build_badge(summarize(tmp_path, packet_health))
    assert badge == {"schemaVersion": 1, "label": "evidence records", "message": "1 · 0 open items", "color": "brightgreen"}


def test_open_gaps_are_shown_not_hidden(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8").replace(
            "| C-001 | pass | test |\n", "| C-001 | pass | test |\n| C-002 | gap | none |\n"
        ),
        encoding="utf-8",
    )
    badge = build_badge(summarize(tmp_path, packet_health))
    assert badge["color"] == "yellow"
    assert badge["message"] == "1 · 1 open items"


def test_invalid_records_turn_red_and_closed_ones_are_excluded(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    (packet / "proof.md").unlink()
    closed = tmp_path / ".nuclear" / "changes" / "dropped"
    closed.mkdir(parents=True)
    (closed / "risk.md").write_text("NUCLEAR-GRADE-CLOSED: superseded by quick-demo\n", encoding="utf-8")

    summary = summarize(tmp_path, packet_health)
    assert summary["closed"] == 1
    badge = build_badge(summary)
    assert badge["color"] == "red"
    assert badge["message"] == "1 · 1 need attention"


def test_badge_never_claims_certification(tmp_path):
    minimal_quick_packet(tmp_path)
    text = json.dumps(build_badge(summarize(tmp_path, packet_health))).lower()
    for word in ("certified", "compliant", "approved", "passing", "safe"):
        assert word not in text


def test_cli_writes_badge_file(tmp_path):
    minimal_quick_packet(tmp_path)
    out = tmp_path / ".nuclear" / "badge.json"
    result = run_ng("badge", str(tmp_path), "--out", str(out))
    assert result.returncode == 0, result.stderr
    assert json.loads(Path(out).read_text(encoding="utf-8"))["schemaVersion"] == 1


def test_quick_record_with_a_gap_is_not_green(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8").replace("- Status: pass", "- Status: gap"), encoding="utf-8")
    badge = build_badge(summarize(tmp_path, packet_health))
    assert badge["color"] == "yellow"
    assert badge["message"] == "1 · 1 open items"


def test_record_with_no_readable_status_is_not_shown_as_zero_open(tmp_path):
    """Review finding: `- The proof remains planned` validated, and the badge said 0 open items in green."""
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8").replace("- Status: pass", "- The proof remains planned"), encoding="utf-8")
    assert packet_health(packet) == "ok"
    badge = build_badge(summarize(tmp_path, packet_health))
    assert badge["color"] == "red"
    assert badge["message"] == "1 · 1 need attention"


def test_valid_record_with_a_closure_note_is_excluded(tmp_path):
    """Review finding: a validating packet with a closure note still counted as active."""
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8") + "\nNUCLEAR-GRADE-CLOSED: superseded by another change.\n", encoding="utf-8")
    assert packet_health(packet) == "closed"
    assert build_badge(summarize(tmp_path, packet_health))["message"] == "none yet"
