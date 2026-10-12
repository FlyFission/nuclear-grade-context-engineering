import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from nuclear_grade.ng_validate import validate_packet
from nuclear_grade.receipt import RECEIPT_SCHEMA, RECEIPT_SCHEMA_VERSION, build_receipt
from tests.test_ng_cli import run_ng
from tests.test_ng_validate import minimal_quick_packet, minimal_standard_packet

ROOT = Path(__file__).resolve().parents[1]
WORKED_EXAMPLE = (
    ROOT / "docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions"
)


def receipt_for(packet: Path, **strict: bool) -> dict:
    result = validate_packet(
        packet,
        require_custody=strict.get("custody", False),
        require_authority=strict.get("authority", False),
    )
    return build_receipt(
        packet,
        result,
        strict_custody=strict.get("custody", False),
        strict_authority=strict.get("authority", False),
        validator_version="test",
        now=datetime(2026, 1, 1, tzinfo=UTC),
    )


def test_receipt_shape_and_versioned_schema(tmp_path):
    receipt = receipt_for(minimal_quick_packet(tmp_path))

    assert receipt["schema"] == RECEIPT_SCHEMA
    assert receipt["schema_version"] == RECEIPT_SCHEMA_VERSION
    assert receipt["generated_at"] == "2026-01-01T00:00:00+00:00"
    assert receipt["mode"] == "quick"
    assert receipt["ok"] is True
    assert receipt["messages"] == []
    assert [entry["path"] for entry in receipt["inputs"]["files"]] == ["proof.md", "risk.md"]
    assert "not a signature" in receipt["boundary"]


def test_digest_is_stable_and_changes_when_a_packet_byte_changes(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    first = receipt_for(packet)["inputs"]["digest"]
    assert receipt_for(packet)["inputs"]["digest"] == first

    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8") + "\n", encoding="utf-8")

    assert receipt_for(packet)["inputs"]["digest"] != first


def test_status_counts_surface_open_gaps_on_a_passing_packet(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    text = verification.read_text(encoding="utf-8").replace(
        "| C-001 | pass | test |\n",
        "| C-001 | pass | test |\n| C-002 | gap | none yet |\n| C-003 | deferred | later |\n",
    )
    verification.write_text(text, encoding="utf-8")

    receipt = receipt_for(packet)

    assert receipt["ok"] is True
    assert receipt["evidence_statuses"]["pass"] == 1
    assert receipt["evidence_statuses"]["gap"] == 1
    assert receipt["evidence_statuses"]["deferred"] == 1
    assert receipt["open_evidence_items"] == 2


def test_failed_packet_receipt_keeps_messages(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    (packet / "proof.md").unlink()

    receipt = receipt_for(packet)

    assert receipt["ok"] is False
    assert "missing required file: proof.md" in receipt["messages"]


def test_missing_packet_still_emits_a_receipt(tmp_path):
    receipt = receipt_for(tmp_path / "nope")

    assert receipt["ok"] is False
    assert receipt["mode"] is None
    assert receipt["inputs"]["files"] == []


def test_git_state_reports_packet_scoped_dirtiness(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    git = ["git", "-c", "user.email=t@example.com", "-c", "user.name=t"]
    subprocess.run([*git, "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run([*git, "add", "."], cwd=tmp_path, check=True)
    subprocess.run([*git, "commit", "-q", "-m", "init"], cwd=tmp_path, check=True)

    clean = receipt_for(packet)["provenance"]["git"]
    assert len(clean["commit"]) == 40
    assert clean["packet_dirty"] is False

    (tmp_path / "unrelated.txt").write_text("x", encoding="utf-8")
    assert receipt_for(packet)["provenance"]["git"]["packet_dirty"] is False

    (packet / "proof.md").write_text("changed", encoding="utf-8")
    assert receipt_for(packet)["provenance"]["git"]["packet_dirty"] is True


def test_cli_json_flag_keeps_exit_codes(tmp_path):
    ok = run_ng("validate", str(WORKED_EXAMPLE), "--strict-custody", "--json")
    assert ok.returncode == 0, ok.stdout + ok.stderr
    receipt = json.loads(ok.stdout)
    assert receipt["ok"] is True
    assert receipt["strict"] == {"custody": True, "authority": False}
    assert receipt["evidence_statuses"]["deferred"] >= 1

    packet = minimal_quick_packet(tmp_path)
    (packet / "proof.md").unlink()
    failed = run_ng("validate", str(packet), "--json")
    assert failed.returncode == 1
    assert json.loads(failed.stdout)["ok"] is False


def test_quick_bullet_statuses_are_counted(tmp_path):
    """Review finding: Quick proof.md uses `- Status: gap`; a gap must not read as zero open items."""
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8").replace("- Status: pass", "- Status: gap"), encoding="utf-8")

    receipt = receipt_for(packet)

    assert receipt["ok"] is True
    assert receipt["evidence_statuses"]["gap"] == 1
    assert receipt["open_evidence_items"] == 1


def test_unfilled_status_template_line_is_not_counted(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(
        proof.read_text(encoding="utf-8").replace("- Status: pass", "- Status: pass / fail / gap / not applicable"),
        encoding="utf-8",
    )

    assert receipt_for(packet)["open_evidence_items"] == 0


def test_inline_status_declarations_are_counted(tmp_path):
    """Review finding: `- No score yet. Status: deferred — ...` must count as an open item."""
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(
        proof.read_text(encoding="utf-8") + "\n## Gaps\n\n- No automated score. Status: deferred — optional stretch.\n",
        encoding="utf-8",
    )

    receipt = receipt_for(packet)

    assert receipt["evidence_statuses"]["deferred"] == 1
    assert receipt["open_evidence_items"] == 1


def test_composite_status_cells_count_every_status(tmp_path):
    """Review finding: `pass (local); gap (independent review pending)` hid its gap."""
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8").replace(
            "| C-001 | pass | test |\n", "| C-001 | pass (local); gap (independent review pending) | test |\n"
        ),
        encoding="utf-8",
    )

    receipt = receipt_for(packet)

    assert receipt["evidence_statuses"]["pass"] == 1
    assert receipt["evidence_statuses"]["gap"] == 1
    assert receipt["open_evidence_items"] == 1


def test_status_choice_list_in_a_cell_is_not_counted(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8").replace("| C-001 | pass | test |\n", "| C-001 | pass / fail / gap | test |\n"),
        encoding="utf-8",
    )
    assert receipt_for(packet)["open_evidence_items"] == 0
