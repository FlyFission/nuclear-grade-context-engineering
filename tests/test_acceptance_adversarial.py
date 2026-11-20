"""Adversarial fixtures for the acceptance path.

These tests attack the receipt and its acceptance block the way a careless or motivated
author would, and check that each attack produces a distinct, named result. They are
organized by the property under test, not by a target count:

| Property             | Attack                                                              |
|----------------------|---------------------------------------------------------------------|
| input binding        | a receipt for other bytes, added or removed files, another commit  |
| receipt integrity    | a receipt or any proposition in its acceptance block edited         |
| freshness            | an approval or artifact that outlives a change (known gaps, xfail)  |
| evidence status      | fail, gap, planned, deferred, and decorated status cells           |
| claim completeness   | a declared claim with no verification row; free-text claim rows     |
| authority            | forged approval text; any "approved" or single-boolean verdict      |
| consumer consistency | CLI text, CLI JSON, exit codes, and the MCP string agree            |
| compatibility        | a version 1 or hand-built receipt never reads as eligible           |
| positive behavior    | a clean record stays usable; the worked example stays valid         |

Two cases are documented limits, not detections. A fabricated external citation passes,
because only an external verifier can judge it; the contract says so by reporting that no
independence check ran. Approval replay and out-of-packet evidence swaps are marked
``xfail(strict=True)``: they flip to a failure the day someone implements decision custody
(ROADMAP item 7), which forces this file to be updated.
"""

from __future__ import annotations

import json
import random
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path

import pytest

from nuclear_grade import receipt as receipts
from nuclear_grade.mcp_server import validate_change_record
from nuclear_grade.ng_validate import EVIDENCE_STATUSES, ValidationResult
from tests.test_ng_cli import run_ng
from tests.test_ng_validate import minimal_quick_packet, minimal_standard_packet
from tests.test_receipt import WORKED_EXAMPLE, receipt_for

ELIGIBILITY_STATES = {
    "blocked",
    "undetermined",
    "open_to_decision",
    "open_to_decision_with_open_items",
}
VERIFICATION_ROW = "| C-001 | pass | test |"


def eligibility(packet: Path, **strict: bool) -> str:
    return receipt_for(packet, **strict)["acceptance"]["release_eligibility"]["state"]


def set_status(packet: Path, status: str) -> None:
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8").replace(VERIFICATION_ROW, f"| C-001 | {status} | test |"),
        encoding="utf-8",
    )


def append(packet: Path, name: str, text: str) -> None:
    path = packet / name
    path.write_text(path.read_text(encoding="utf-8") + text, encoding="utf-8")


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-c", "user.email=t@example.com", "-c", "user.name=t", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


# ---- input binding -----------------------------------------------------------------------


def test_receipt_is_bound_to_the_bytes_it_was_issued_for(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    assert receipts.verify_receipt(receipt_for(packet), packet)["state"] == "bound"


def test_a_changed_file_makes_the_receipt_stale(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    append(packet, "verification.md", "\nA late edit.\n")
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "stale"
    assert any("verification.md changed" in reason for reason in verdict["reasons"])


def test_an_added_file_makes_the_receipt_stale(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    (packet / "extra.md").write_text("late addition\n", encoding="utf-8")
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "stale"
    assert any("extra.md is in the packet" in reason for reason in verdict["reasons"])


def test_a_removed_file_makes_the_receipt_stale(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    (packet / "plan.md").unlink()
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "stale"
    assert any("plan.md" in reason and "no longer" in reason for reason in verdict["reasons"])


def test_a_receipt_from_another_commit_is_stale_when_the_commit_is_expected(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-qm", "base")
    issued = receipt_for(packet)
    issued_at = git(tmp_path, "rev-parse", "HEAD")
    assert receipts.verify_receipt(issued, packet, expected_commit=issued_at)["state"] == "bound"
    wrong = "0" * 40
    verdict = receipts.verify_receipt(issued, packet, expected_commit=wrong)
    assert verdict["state"] == "stale"
    assert "provenance.git.commit" in verdict["checked"]
    assert any(issued_at in reason for reason in verdict["reasons"])


def test_something_that_is_not_a_receipt_is_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    for junk in ({}, {"schema": "something-else"}, {"schema": receipts.RECEIPT_SCHEMA}, [], None):
        assert receipts.verify_receipt(junk, packet)["state"] == "invalid"


# ---- receipt integrity -------------------------------------------------------------------


def test_a_receipt_whose_file_list_was_edited_is_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    issued["inputs"]["files"][0]["sha256"] = "0" * 64
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert "edited after it was issued" in verdict["reasons"][0]


def test_an_edited_acceptance_block_is_invalid_even_when_the_bytes_match(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    set_status(packet, "gap")
    issued = receipt_for(packet)
    assert issued["acceptance"]["release_eligibility"]["state"] == "blocked"
    issued["acceptance"]["release_eligibility"] = {"state": "open_to_decision", "reasons": []}
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert "release_eligibility" in verdict["reasons"][0]


def test_an_edited_structural_verdict_is_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    (packet / "plan.md").write_text("# Plan\n\nNOT FILLED\n", encoding="utf-8")
    issued = receipt_for(packet)
    if issued["acceptance"]["structural_validity"]["state"] == "valid":
        pytest.skip("this edit did not break the structure")
    issued["acceptance"]["structural_validity"]["state"] = "valid"
    assert receipts.verify_receipt(issued, packet)["state"] == "invalid"


def test_an_artifact_inside_the_packet_cannot_be_swapped_unnoticed(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    (packet / "test-output.txt").write_text("12 passed\n", encoding="utf-8")
    issued = receipt_for(packet)
    (packet / "test-output.txt").write_text("12 passed (edited)\n", encoding="utf-8")
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "stale"
    assert any("test-output.txt changed" in reason for reason in verdict["reasons"])


@pytest.mark.parametrize(
    ("proposition", "forged"),
    [
        ("authorized_decision", {"state": "approved"}),
        ("apply_permission", {"state": "allowed"}),
        ("independence", {"state": "declared_checks_run", "checks": {"custody": True}, "note": "x"}),
        ("claim_support", {"state": "recognized", "rows": [], "weakest_status": "pass"}),
        ("evidence_integrity", {"state": "verified"}),
        ("note", "Approved."),
    ],
)
def test_every_edited_proposition_makes_the_receipt_invalid(tmp_path, proposition, forged):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    issued["acceptance"][proposition] = forged
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert any(f"acceptance.{proposition}" in reason for reason in verdict["reasons"])


def test_flipping_the_structural_verdict_of_an_invalid_packet_is_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    (packet / "plan.md").unlink()
    issued = receipt_for(packet)
    assert issued["ok"] is False
    issued["ok"] = True
    issued["messages"] = []
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert any(reason.startswith("ok ") for reason in verdict["reasons"])
    assert any(reason.startswith("messages ") for reason in verdict["reasons"])


@pytest.mark.parametrize(
    ("field", "forged"),
    [
        ("ok", False),
        ("ok_scope", "release approval"),
        ("messages", ["nothing to see"]),
        ("mode", "quick"),
        ("strict", {"custody": "yes", "authority": False, "two_party": False}),
        ("evidence_statuses", {"pass": 9}),
        ("open_evidence_items", 0),
        ("boundary", "This receipt is an approval."),
    ],
)
def test_every_derived_top_level_field_is_checked(tmp_path, field, forged):
    packet = minimal_standard_packet(tmp_path)
    set_status(packet, "gap")
    issued = receipt_for(packet, custody=True)
    assert issued[field] != forged
    issued[field] = forged
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert any(reason.startswith(f"{field} ") for reason in verdict["reasons"])


def test_lowering_only_the_strict_flags_is_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet, custody=True)
    assert issued["strict"]["custody"] is True
    issued["strict"] = {"custody": False, "authority": False, "two_party": False}
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert any("acceptance.independence" in reason for reason in verdict["reasons"])


def test_a_consistent_downgrade_of_the_declared_checks_is_truthful_and_must_be_read(tmp_path):
    """Documented limit: verification shows a receipt matches these bytes under the checks it declares.

    A receipt rewritten to declare that no custody check ran, with every dependent field to match, says
    so honestly. It does not say a check ran that did not. A consumer that requires a check must read
    `strict` itself; `verify_receipt` cannot know which checks a consumer requires.
    """
    packet = minimal_standard_packet(tmp_path)
    honest = receipt_for(packet)  # issued without --strict-custody
    assert honest["strict"]["custody"] is False
    assert honest["acceptance"]["independence"]["state"] == "not_checked"
    assert receipts.verify_receipt(honest, packet)["state"] == "bound"
    strict_issued = receipt_for(packet, custody=True)
    assert strict_issued["acceptance"]["independence"]["state"] == "declared_checks_run"
    assert strict_issued["strict"]["custody"] is True


def test_a_field_the_contract_does_not_define_makes_the_receipt_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    issued["approved"] = True
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert any("approved is not a field" in reason for reason in verdict["reasons"])


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("generated_at", "2020-01-01T00:00:00+00:00"),
        ("packet", "somewhere/else"),
        ("provenance", {"validator_version": "other"}),
        ("before_review", False),
        ("receipt_binding", {"state": "bound"}),
    ],
)
def test_where_and_when_fields_are_context_and_not_verified(tmp_path, field, value):
    """Documented limit: these say where and when a receipt was issued, not what it concludes.

    A consumer that needs a commit or time must ask for it: `--expect-commit` checks the commit.
    """
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    issued[field] = value
    assert receipts.verify_receipt(issued, packet)["state"] == "bound"


@pytest.mark.parametrize("version", [0, 3, 99, True, "2", 2.0, None, "missing"])
def test_an_unsupported_receipt_version_is_invalid_not_bound(tmp_path, version):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    if version == "missing":
        del issued["schema_version"]
    else:
        issued["schema_version"] = version
    # edit the verdict and the block too: nothing about an unsupported receipt may verify
    issued["ok"] = not issued["ok"]
    issued["acceptance"]["release_eligibility"] = {"state": "open_to_decision", "reasons": []}
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert "unsupported receipt schema version" in verdict["reasons"][0]


def test_a_version_1_receipt_still_verifies_its_file_bindings_and_is_never_eligible(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    issued["schema_version"] = 1
    assert receipts.verify_receipt(issued, packet)["state"] == "bound"
    assert receipts.verify_receipt(issued, packet)["checked"] == ["inputs.files", "inputs.digest"]
    assert receipts.is_open_to_decision(issued) is False
    append(packet, "plan.md", "\nlate edit\n")
    assert receipts.verify_receipt(issued, packet)["state"] == "stale"


def test_a_receipt_relabelled_with_another_version_never_reads_as_eligible(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    assert receipts.is_open_to_decision(issued) is True
    for version in (1, 3):
        issued["schema_version"] = version
        assert receipts.is_open_to_decision(issued) is False


def test_an_added_key_in_the_acceptance_block_makes_the_receipt_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    issued["acceptance"]["approved"] = True
    verdict = receipts.verify_receipt(issued, packet)
    assert verdict["state"] == "invalid"
    assert any("acceptance.approved" in reason for reason in verdict["reasons"])


def test_a_version_2_receipt_with_its_acceptance_block_removed_is_invalid(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    del issued["acceptance"]
    assert receipts.verify_receipt(issued, packet)["state"] == "invalid"
    issued["acceptance"] = "open_to_decision"
    assert receipts.verify_receipt(issued, packet)["state"] == "invalid"


# ---- freshness: known gaps, kept visible -------------------------------------------------


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="Decision custody is not implemented (ROADMAP item 7): nothing binds an approval to a candidate digest.",
)
def test_an_approval_does_not_survive_a_material_change(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    append(packet, "ship.md", "\n- **Approved by:** maintainer\n")
    set_status(packet, "pass")
    after_change = receipt_for(packet)
    assert after_change["acceptance"]["authorized_decision"]["state"] in {"stale", "invalidated", "reopened"}


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="The receipt digests only files inside the packet; a raw artifact kept elsewhere can be swapped unnoticed.",
)
def test_an_artifact_outside_the_packet_cannot_be_swapped_unnoticed(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    outside = tmp_path / "raw-results.txt"
    outside.write_text("12 passed\n", encoding="utf-8")
    append(packet, "verification.md", f"\nRaw result: {outside.name}\n")
    issued = receipt_for(packet)
    outside.write_text("0 passed, 12 failed\n", encoding="utf-8")
    assert receipts.verify_receipt(issued, packet)["state"] != "bound"


# ---- evidence status ---------------------------------------------------------------------


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        ("pass", "open_to_decision"),
        ("deferred", "open_to_decision_with_open_items"),
        ("gap", "blocked"),
        ("fail", "blocked"),
        ("planned", "blocked"),
    ],
)
def test_each_declared_status_maps_to_one_eligibility(tmp_path, status, expected):
    packet = minimal_standard_packet(tmp_path)
    set_status(packet, status)
    assert eligibility(packet) == expected


def test_a_decorated_status_cell_is_read_not_ignored(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    set_status(packet, "pass — see the log")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["rows"] == [{"id": "C-001", "status": "pass"}]
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"


def test_quick_packet_gap_blocks_and_pass_does_not(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    assert eligibility(packet) == "open_to_decision"
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8").replace("Status: pass", "Status: gap"), encoding="utf-8")
    assert eligibility(packet) == "blocked"
    assert receipt_for(packet)["acceptance"]["claim_support"]["state"] == "not_applicable"


# ---- claim completeness ------------------------------------------------------------------


def test_a_declared_claim_with_no_verification_row_blocks(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    basis = packet / "basis.md"
    basis.write_text(
        basis.read_text(encoding="utf-8").replace(
            "| C-001 | Demo claim | Test |\n", "| C-001 | Demo claim | Test |\n| C-002 | The load-bearing claim | Test |\n"
        ),
        encoding="utf-8",
    )
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == ["C-002"]
    assert acceptance["release_eligibility"]["state"] == "blocked"
    assert any("C-002" in reason for reason in acceptance["release_eligibility"]["reasons"])


def declare(packet: Path, row: str) -> None:
    basis = packet / "basis.md"
    basis.write_text(
        basis.read_text(encoding="utf-8").replace(
            "| C-001 | Demo claim | Test |\n", f"| C-001 | Demo claim | Test |\n{row}\n"
        ),
        encoding="utf-8",
    )


@pytest.mark.parametrize("cell", ["**C-002**", "`C-002`", "__C-002__", "_C-002_", "[C-002](plan.md)", "**C-002** Critical"])
def test_markdown_in_a_declared_id_cannot_hide_a_missing_claim(tmp_path, cell):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, f"| {cell} | Critical claim | Test |")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == ["C-002"]
    assert acceptance["release_eligibility"]["state"] == "blocked"


@pytest.mark.parametrize(
    "heading",
    [
        "## Derived requirements or claims",
        "  ## Derived requirements or claims",
        "   ## Derived requirements or claims",
        "## Derived requirements  or claims",
        "##   Derived requirements or claims",
        "## Derived requirements or claims ##",
        "## DERIVED REQUIREMENTS OR CLAIMS",
        "Derived requirements or claims\n------------------------------",
    ],
)
def test_the_claims_heading_is_read_the_way_the_validator_reads_it(tmp_path, heading):
    packet = minimal_standard_packet(tmp_path)
    basis = packet / "basis.md"
    text = basis.read_text(encoding="utf-8")
    assert "## Derived requirements or claims" in text
    text = text.replace("## Derived requirements or claims", heading)
    text = text.replace("| C-001 | Demo claim | Test |\n", "| C-001 | Demo claim | Test |\n| C-002 | Critical | Test |\n")
    basis.write_text(text, encoding="utf-8")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == ["C-002"]
    assert acceptance["release_eligibility"]["state"] == "blocked"


def test_a_declared_row_with_no_readable_id_is_undetermined_not_absent(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "| The safety claim | Critical claim | Test |")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["unreadable_declarations"] == 1
    assert acceptance["release_eligibility"]["state"] == "undetermined"
    assert "no readable claim id" in acceptance["release_eligibility"]["reasons"][0]


def test_header_and_separator_rows_are_not_declarations(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    basis = packet / "basis.md"
    basis.write_text(
        basis.read_text(encoding="utf-8")
        + "\n| ID | Second table | Notes |\n|:---|:---:|---:|\n| C-001 | Same claim again | Test |\n",
        encoding="utf-8",
    )
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["unreadable_declarations"] == 0
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"


def test_a_formatted_id_in_the_verification_table_is_still_a_claim_row(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8").replace(VERIFICATION_ROW, "| **C-001** | pass | test |"),
        encoding="utf-8",
    )
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["rows"] == [{"id": "C-001", "status": "pass"}]
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"


@pytest.mark.parametrize("header", ["Result status", "Verdict", "Outcome", "Disposition", "Check"])
@pytest.mark.parametrize(
    ("status", "expected"),
    [
        ("fail", "blocked"),
        ("gap", "blocked"),
        ("planned", "blocked"),
        ("deferred", "open_to_decision_with_open_items"),
        ("pass", "open_to_decision"),
    ],
)
def test_a_recorded_status_counts_whatever_the_column_is_called(tmp_path, header, status, expected):
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8")
        .replace("| Claim | Result status | Evidence link |", f"| Claim | {header} | Evidence link |")
        .replace(VERIFICATION_ROW, f"| C-001 | {status} | test |"),
        encoding="utf-8",
    )
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["release_eligibility"]["state"] == expected
    assert acceptance["evidence_status"]["state"] == ("complete" if status == "pass" else "open")
    assert receipts.verify_receipt(receipt_for(packet), packet)["state"] == "bound"


@pytest.mark.parametrize(
    ("declaration", "expected"),
    [
        ("- **Status:** **gap**", "blocked"),
        ("- **Status:** **fail**", "blocked"),
        ("- **Status:** **planned**", "blocked"),
        ("- Status: *gap*", "blocked"),
        ("- Status: `gap`", "blocked"),
        ("- **Status**: **deferred**", "open_to_decision_with_open_items"),
        ("- **Status:** **pass**", "open_to_decision"),
        ("- Status: pass", "open_to_decision"),
    ],
)
def test_emphasis_around_a_quick_status_cannot_hide_it(tmp_path, declaration, expected):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8").replace("- Status: pass", declaration), encoding="utf-8")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["release_eligibility"]["state"] == expected
    assert acceptance["evidence_status"]["state"] == ("complete" if expected == "open_to_decision" else "open")


def test_a_record_with_no_readable_status_is_undetermined_not_eligible():
    """Defense in depth: valid structure and zero readable statuses must never read as eligible."""
    nothing_read = dict.fromkeys(EVIDENCE_STATUSES, 0)
    for mode, support in (("quick", {"state": "not_applicable", "rows": []}), ("standard", {"state": "recognized", "rows": []})):
        verdict = receipts._release_eligibility(ValidationResult(True, []), mode, nothing_read, support)
        assert verdict["state"] == "undetermined", mode
        assert "no evidence status declaration could be read" in verdict["reasons"][0]


@pytest.mark.parametrize("heading", ["### Additional claims", "#### Deeper still", "### Safety claims"])
def test_a_subsection_of_the_claims_section_is_still_scanned(tmp_path, heading):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, f"\n{heading}\n\n| ID | Requirement | Evidence |\n|---|---|---|\n| C-002 | Critical | Test |")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == ["C-002"]
    assert acceptance["release_eligibility"]["state"] == "blocked"


@pytest.mark.parametrize("heading", ["## Assumptions", "# Appendix"])
def test_a_sibling_or_ancestor_section_is_not_scanned_for_claims(tmp_path, heading):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, f"\n{heading}\n\n| ID | Note |\n|---|---|\n| A-001 | not a claim |\n| Free text | still not a claim |")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == []
    assert acceptance["claim_support"]["unreadable_declarations"] == 0
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"


def with_claim_rows(packet: Path, rows: str, header: str = "Verdict") -> None:
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8")
        .replace("| Claim | Result status |", f"| Claim | {header} |")
        .replace(VERIFICATION_ROW, f"{VERIFICATION_ROW}\n{rows}"),
        encoding="utf-8",
    )


@pytest.mark.parametrize(
    "cell",
    [
        "fail",
        "**fail**",
        "`fail`",
        "_fail_",
        "FAIL",
        "Fail",
        "fail (local)",
        "**fail** (local)",
        "fail — see the log",
        "fail - see the log",
        "fail. See the log.",
        "fail: it broke",
        "fail; pass",
        "pass; fail",
        "gap",
        "**gap**",
        "planned",
        "**planned**",
    ],
)
def test_a_decorated_failure_in_a_claim_row_blocks_whatever_the_header(tmp_path, cell):
    packet = minimal_standard_packet(tmp_path)
    with_claim_rows(packet, f"| C-002 | {cell} | test |")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["release_eligibility"]["state"] == "blocked"
    assert acceptance["evidence_status"]["state"] == "open"
    assert receipts.verify_receipt(receipt_for(packet), packet)["state"] == "bound"


@pytest.mark.parametrize("cell", ["pass", "**pass**", "PASS", "pass (CI)", "pass — see the log", "pass: all green", "not applicable"])
def test_a_decorated_pass_in_a_claim_row_does_not_block(tmp_path, cell):
    packet = minimal_standard_packet(tmp_path)
    with_claim_rows(packet, f"| C-002 | {cell} | test |")
    assert receipt_for(packet)["acceptance"]["release_eligibility"]["state"] == "open_to_decision"


@pytest.mark.parametrize("cell", ["pass all four tests", "must pass before release", "a gap in coverage", "failing"])
def test_prose_that_mentions_a_status_word_is_not_a_status(tmp_path, cell):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "| C-002 | Critical | Test |")
    with_claim_rows(packet, f"| C-002 | {cell} | test |")
    acceptance = receipt_for(packet)["acceptance"]
    assert {"id": "C-002", "status": "pass"} not in acceptance["claim_support"]["rows"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == ["C-002"]
    assert acceptance["release_eligibility"]["state"] == "blocked"
    assert "no readable verification row" in " ".join(acceptance["release_eligibility"]["reasons"])


@pytest.mark.parametrize(
    ("expected", "verdict", "state"),
    [
        ("pass", "fail", "blocked"),
        ("pass", "**fail**", "blocked"),
        ("pass", "gap", "blocked"),
        ("pass", "planned (CI)", "blocked"),
        ("fail", "pass", "blocked"),
        ("pass", "deferred", "open_to_decision_with_open_items"),
        ("pass", "pass", "open_to_decision"),
        ("pass", "not applicable", "open_to_decision"),
    ],
)
def test_a_row_is_only_as_strong_as_its_weakest_status_cell(tmp_path, expected, verdict, state):
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8")
        .replace("| Claim | Result status | Evidence link |", "| Claim | Expected | Verdict | Evidence link |")
        .replace("|---|---|---|\n| C-001 | pass | test |", f"|---|---|---|---|\n| C-001 | {expected} | {verdict} | test |"),
        encoding="utf-8",
    )
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["release_eligibility"]["state"] == state
    assert receipts.verify_receipt(receipt_for(packet), packet)["state"] == "bound"


@pytest.mark.parametrize(
    ("declared", "fenced", "state"),
    [
        ("- Status: unknown", "- Status: pass", "undetermined"),
        ("- Status: unknown", "- **Status:** **pass**", "undetermined"),
        ("- Status: gap", "- Status: pass", "blocked"),
        ("- Status: pass", "- Status: fail", "open_to_decision"),
        ("- Status: pass", "- Status: gap", "open_to_decision"),
    ],
)
@pytest.mark.parametrize("fence", ["```", "~~~"])
def test_a_fenced_status_example_is_never_evidence(tmp_path, declared, fenced, state, fence):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(
        proof.read_text(encoding="utf-8").replace("- Status: pass", declared) + f"\n{fence}markdown\n{fenced}\n{fence}\n",
        encoding="utf-8",
    )
    assert receipt_for(packet)["acceptance"]["release_eligibility"]["state"] == state


def test_a_fenced_claim_table_in_a_standard_packet_is_never_evidence(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    append(packet, "verification.md", "\n```markdown\n| Claim | Result status | Evidence link |\n|---|---|---|\n| C-001 | fail | example |\n```\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"
    assert acceptance["evidence_status"] == {"state": "complete", "open_items": 0}


@pytest.mark.parametrize(
    "hidden",
    [
        "<!-- | C-002 | pass | example only | -->",
        "<!--\n| C-002 | pass | example only |\n-->",
        "<!-- retired\n| C-002 | pass | old |\n   still a comment -->",
        "<!--\n| C-002 | pass | never closed |",
    ],
)
def test_an_html_comment_cannot_satisfy_a_declared_claim(tmp_path, hidden):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "| C-002 | Critical | Test |")
    append(packet, "verification.md", f"\n{hidden}\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == ["C-002"]
    assert acceptance["release_eligibility"]["state"] == "blocked"


def test_a_comment_closed_on_its_own_line_hides_nothing_after_it(tmp_path):
    """CommonMark: the line holding `-->` ends the HTML block, so a second `<!--` on it is inert."""
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "| C-002 | Critical | Test |")
    append(packet, "verification.md", "\n<!-- a --> <!--\n\n| C-002 | pass | real, and visible |\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == []


def test_a_commented_declaration_is_not_a_declaration(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "<!--\n| C-009 | Retired claim | x |\n| Free text | nor this | x |\n-->")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == []
    assert acceptance["claim_support"]["unreadable_declarations"] == 0
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"


@pytest.mark.parametrize(
    ("declared", "hidden", "state"),
    [
        ("- Status: unknown", "<!-- - Status: pass -->", "undetermined"),
        ("- Status: unknown", "<!--\n- Status: pass\n-->", "undetermined"),
        ("- Status: unknown", "<!--\n- **Status:** **pass**", "undetermined"),
        ("- Status: gap", "<!-- - Status: pass -->", "blocked"),
        ("- Status: pass", "<!-- - Status: fail -->", "open_to_decision"),
    ],
)
def test_a_commented_status_is_never_evidence(tmp_path, declared, hidden, state):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8").replace("- Status: pass", declared) + f"\n{hidden}\n", encoding="utf-8")
    assert receipt_for(packet)["acceptance"]["release_eligibility"]["state"] == state


@pytest.mark.parametrize(
    "mention",
    [
        "Note: `<!--` inside inline code is text.",
        "Note: ``<!-- also `tick` -->`` is text.",
        "```\n<!-- inside a fence\n```",
    ],
)
def test_a_comment_marker_in_code_is_text_and_hides_nothing(tmp_path, mention):
    """The trap this repository has hit before: an `<!--` in code must not open a comment."""
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "| C-002 | Critical | Test |")
    append(packet, "verification.md", f"\n{mention}\n\n| C-002 | pass | real |\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == []
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"


def quick_with(tmp_path, declared: str, tail: str) -> str:
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8").replace("- Status: pass", declared) + tail, encoding="utf-8")
    return receipt_for(packet)["acceptance"]["release_eligibility"]["state"]


@pytest.mark.parametrize(
    "tail",
    [
        "\n<!--\n```\n-->\n- Status: gap\n",
        "\n<!-- ``` -->\n- Status: gap\n",
        "\n<!--\n~~~\n-->\n- Status: gap\n",
        "\n<!-- ````md -->\n- Status: gap\n",
        "\n```\n<!--\n```\n- Status: gap\n",
        "\n~~~\n<!--\n~~~\n- Status: gap\n",
    ],
)
def test_a_fence_marker_in_a_comment_and_a_comment_marker_in_a_fence_hide_nothing(tmp_path, tail):
    """The failure a review found: each context must not be able to mis-open the other."""
    assert quick_with(tmp_path, "- Status: pass", tail) == "blocked"
    assert quick_with(tmp_path, "- Status: unknown", tail) == "blocked"


def test_a_fence_marker_in_a_comment_hides_a_later_failure_in_a_standard_packet_no_longer(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "| C-002 | Critical | Test |")
    append(packet, "verification.md", "\n<!--\n```\n-->\n\n| C-002 | fail | real |\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert {"id": "C-002", "status": "fail"} in acceptance["claim_support"]["rows"]
    assert acceptance["release_eligibility"]["state"] == "blocked"


@pytest.mark.parametrize(
    ("tail", "construct"),
    [
        ("\n- Status: pass\n```\n- Status: fail\n", "never closed"),
        ("\n<!--\n- Status: pass\n", "never closed"),
        ("\nx <!-- start\n- Status: pass\n", "not closed on the line where it opens"),
        ("\nx <!-- a\nb --> y\n- Status: pass\n", "not closed on the line where it opens"),
        ("\n- <!--\n- Status: pass\n-->\n", "inside a quote or list item"),
        ("\n> <!--\nStatus: pass\n-->\n", "inside a quote or list item"),
        ("\n- ```\n  Status: pass\n  ```\n", "inside a quote or list item"),
        ("\n    - Status: pass\n", "indented text that mentions a status"),
        ("\n\t- Status: pass\n", "indented text that mentions a status"),
        ("\n<pre>\n- Status: pass\n</pre>\n", "raw HTML block"),
        ("\n<script>\nStatus: pass\n</script>\n", "raw HTML block"),
        ("\n`two\nStatus: pass\nlines`\n", "code span that continues"),
        ("\n<!-- a --> <!--\n- Status: pass\n", "left open on the line that closes"),
        ("\n</details>\n```\nStatus: pass\n  ```\n", "raw HTML block that contains a fence"),
    ],
)
def test_a_construct_the_reader_cannot_read_faithfully_withholds_eligibility(tmp_path, tail, construct):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8") + tail, encoding="utf-8")
    eligibility = receipt_for(packet)["acceptance"]["release_eligibility"]
    assert eligibility["state"] == "undetermined"
    assert any(construct in reason for reason in eligibility["reasons"])


def test_a_stray_comment_opener_does_not_hide_a_later_failure(tmp_path):
    """Reading a stray `<!--` as a comment to the end of the file would lose a real failure."""
    assert quick_with(tmp_path, "- Status: pass", "\nx <!-- start\n\n- Status: gap\n") == "blocked"


def test_a_tag_name_in_a_code_span_is_text_outside_a_raw_html_paragraph(tmp_path):
    """A record that talks about `<pre>` or `<script>` in code must stay readable, as one real record here does."""
    assert quick_with(tmp_path, "- Status: pass", "\nThe note mentions `<pre>` and `<script>` in code.\n") == "open_to_decision"
    assert quick_with(tmp_path, "- Status: pass", "\n| CX-1 | a literal `<!--` and `<pre>` | yes |\n") == "open_to_decision"


def test_the_same_mention_inside_a_raw_html_paragraph_is_a_real_tag(tmp_path):
    """Backticks are not code spans in a raw HTML block, so the tag is real and hides what follows."""
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8") + "\n<details>\nmention `<script>` here\n- Status: gap\n", encoding="utf-8")
    eligibility = receipt_for(packet)["acceptance"]["release_eligibility"]
    assert eligibility["state"] in {"blocked", "undetermined"}  # never eligible; blocked if the gap is also read
    assert any("raw HTML block" in reason for reason in eligibility["reasons"])


@pytest.mark.parametrize(
    "example",
    [
        "Example syntax: `Status: pass`.",
        "see `- Status: pass` here",
        "`Status: pass`",
        "Use `**Status:** pass` like this.",
        "``Status: pass``",
        "a `<!-- Status: pass` b",
    ],
)
@pytest.mark.parametrize(("declared", "state"), [("- Status: unknown", "undetermined"), ("- Status: gap", "blocked")])
def test_a_status_example_in_a_code_span_is_never_evidence(tmp_path, example, declared, state):
    assert quick_with(tmp_path, declared, f"\n{example}\n") == state


@pytest.mark.parametrize("value", ["- Status: `pass`", "- **Status:** `pass`", "- __Status:__ pass"])
def test_a_value_alone_in_code_or_emphasis_is_still_a_declaration(tmp_path, value):
    assert quick_with(tmp_path, value, "") == "open_to_decision"


@pytest.mark.parametrize(
    ("tail", "state"),
    [
        ("\n__Status:__ gap\n", "blocked"),
        ("\nStat<!-- c -->us: gap\n", "blocked"),
        ("\nStatus: <!-- c --> gap\n", "blocked"),
        ("\n- [x] Status: gap\n", "blocked"),
        ("\n**Status: pass.** see [the risk record](risk.md) and `code`.\n", "open_to_decision"),
    ],
)
def test_comments_inside_a_label_and_underscore_emphasis_are_read_as_a_page_shows_them(tmp_path, tail, state):
    assert quick_with(tmp_path, "- Status: pass", tail) == state


@pytest.mark.parametrize(
    "tail",
    [
        "\nStatus&#58; gap\n",
        "\n<b>Status:</b> gap\n",
        "\n<code>Status: pass</code>\n",
        "\n![Status: fail](img.png)\n",
        '\n[link](http://x "Status: gap")\n',
        '\n[ref]: http://x "Status: pass"\n',
        "\n[Status: pass](http://x)\n",
        "\n\\<!-- Status: gap -->\n",
    ],
)
def test_a_status_label_beside_markup_the_reader_does_not_interpret_withholds_eligibility(tmp_path, tail):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(proof.read_text(encoding="utf-8") + tail, encoding="utf-8")
    eligibility = receipt_for(packet)["acceptance"]["release_eligibility"]
    assert eligibility["state"] in {"blocked", "undetermined"}
    assert any("markup the reader does not interpret" in reason or "raw HTML" in reason for reason in eligibility["reasons"])


def test_a_top_level_fence_is_not_closed_by_a_list_item_line(tmp_path):
    visible = receipts._evidence_view("```md\n\n- ```\nStatus: deferred\n")
    assert "deferred" not in visible


# Documents from a differential fuzz against a CommonMark renderer (markdown-it-py), with the statuses the
# rendered page shows. The reader may differ from the page only if it reports that it could not read the
# file faithfully. These are plain data, so the check runs without the third-party parser.
RENDERED_CORPUS = [
    ("    - Status: fail\n", []),
    ("x <!-- start\n- Status: gap\n", ["gap"]),
    ("<!--\n```\n-->\n- Status: gap\n", ["gap"]),
    ("<!-- ``` -->\n- Status: gap\n", ["gap"]),
    ("~~~\n<!--\n~~~\n- Status: gap\n", ["gap"]),
    ("```\n<!--\n```\n- Status: gap\n", ["gap"]),
    ("- Status: pass\n```\n- Status: fail\n", ["pass"]),
    ("```md\n\n<!-->\n- ```\nStatus: deferred\n", []),
    ("<!-- a --> <!--\n- Status: gap\n", []),
    ("`two\nStatus: deferred\nlines`\n", []),
    ("</details>\n```\nStatus: gap\n  ```\n", ["gap"]),
    ("<pre>\n- Status: pass\n", []),
    ("- <!--\n- Status: gap\n-->\n", []),
    ("> <!--\nStatus: fail\n-->\n", []),
    ("\t- Status: gap\n", []),
    ("- Status: **gap**\n", ["gap"]),
    ("Status: `pass`\n", []),
    ("x <!-- a\nb --> y\n- Status: fail\n", ["fail"]),
    ("<!--->\n- Status: gap\n", ["gap"]),
    ("<!-->\n- Status: gap\n", ["gap"]),
    ("text <!-- a --> text\n- Status: gap\n", ["gap"]),
    ("a `<!--` b\n- Status: gap\n", ["gap"]),
    ("<!--\n- Status: pass\n-->\n- Status: gap\n", ["gap"]),
    ("<!-- - Status: pass -->\n- Status: gap\n", ["gap"]),
    ("<details>\nmention `<script>` and `<style>`\n- Status: gap\n", []),
    ("mention `<pre>` in code\n- Status: gap\n", ["gap"]),
    ("text <pre> text\n- Status: gap\n", []),
    ("| CX-18 | A literal `<!--` and `<pre>` in code | yes |\n- Status: gap\n", ["gap"]),
    ("Example syntax: `Status: pass`.\n- Status: gap\n", ["gap"]),
    ("see `- Status: gap` and `Status: fail` here\n", []),
    ("__Status:__ gap\n", ["gap"]),
    ("Stat<!-- c -->us: gap\n", ["gap"]),
    ("Status: <!-- c --> gap\n", ["gap"]),
    ("\\<!-- Status: gap -->\n", ["gap"]),
    ("`<!-- Status: gap`\n- Status: fail\n", ["fail"]),
    ("Status&#58; gap\n", ["gap"]),
    ("<b>Status:</b> gap\n", ["gap"]),
    ("<code>Status: pass</code>\n", []),
    ("![Status: fail](img.png)\n", []),
    ('[link](http://x "Status: gap")\n', []),
    ('[ref]: http://x "Status: pass"\n', []),
    ("**Status: pass.** see [plan](plan.md)\n", ["pass"]),
    ("- [x] Status: pass\n", ["pass"]),
    ("[Status: pass](http://x)\n", ["pass"]),
]
_STATUS_LINE = re.compile(r"Status[*_]*:[*_]*\s*[*_]*\s*([a-z]+)", re.IGNORECASE)


@pytest.mark.parametrize(("document", "rendered"), RENDERED_CORPUS)
def test_the_reader_matches_the_rendered_page_or_says_it_cannot(document, rendered):
    view, notes = receipts._scan_evidence(document)
    assert sorted(_STATUS_LINE.findall(view)) == rendered or notes


_FUZZ_LINES = [
    "- Status: gap", "- Status: pass", "- Status: fail", "Status: deferred", "", "text", "```", "~~~", "````", "```md",
    "<!--", "-->", "<!-- note -->", "<!-- ``` -->", "<!-- - Status: pass -->", "a `<!--` b", "x <!-- start", "end --> y",
    "   ```", "    - Status: fail", "> - Status: gap", "- <!-- c -->", "- <!--", "> <!--", "> ```", "- ```", "  ```",
    "  - Status: gap", "1. Status: fail", "# Heading", "---", "text <!-- a --> text", "<!-->", "<!--->",
    "- Status: **gap**", "text <pre> text", "mention `<pre>` in code", "mention `<script>` and `<style>`", "<pre>", "</pre>", "<script>", "</script>", "<div>", "</div>", "\t- Status: gap",
    "Heading", "=======", "| C-001 | Status: gap |", "`two", "lines`", "Status: `pass`", "<span>Status: fail</span>",
    "Example syntax: `Status: pass`.", "see `- Status: gap` and `Status: fail` here", "- Status: `pass`", "`Status:` pass",
    "[Status: pass](http://x)", '[link](http://x "Status: gap")', "![Status: fail](img.png)", "## Status: gap",
    "__Status:__ gap", "**Status:** gap", "Status&#58; gap", "<b>Status:</b> gap", "<code>Status: pass</code>",
    "\\<!-- Status: gap -->", "`<!-- Status: gap`", "``Status: pass``", "- [ ] Status: gap", "- [x] Status: pass",
    "[ref]: http://x \"Status: pass\"", "Status: gap <!-- c --> more", "Status: <!-- c --> gap", "Stat<!-- c -->us: gap",
    "STATUS: gap", "Status:  gap", "<details>", "</details>", "<style>", "</style>", "<textarea>", "</textarea>",
]


class _RenderedText(HTMLParser):
    _BLOCK = {"p", "li", "ul", "ol", "td", "th", "tr", "table", "blockquote", "pre", "code", "div", "details",
              "summary", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "br", "script", "style", "textarea", "span"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_code = 0
        self.text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self._BLOCK:
            self.text.append("\x00")
        self.in_code += tag in ("pre", "code")

    def handle_endtag(self, tag):
        if tag in ("pre", "code") and self.in_code:
            self.in_code -= 1
        if tag in self._BLOCK:
            self.text.append("\x00")

    def handle_data(self, data):
        if not self.in_code:
            self.text.append(data)


def test_the_reader_never_silently_disagrees_with_a_commonmark_renderer():
    """Differential fuzz. Runs where markdown-it-py is installed; the corpus above covers the rest."""
    markdown_it = pytest.importorskip("markdown_it")
    renderer = markdown_it.MarkdownIt("commonmark", {"html": True})
    silent = []
    for seed in range(4):
        rng = random.Random(seed)
        for _ in range(1000):
            document = "\n".join(rng.choice(_FUZZ_LINES) for _ in range(rng.randint(2, 9))) + "\n"
            page = _RenderedText()
            page.feed(renderer.render(document))
            rendered = sorted(_STATUS_LINE.findall("".join(page.text)))
            view, notes = receipts._scan_evidence(document)
            if sorted(_STATUS_LINE.findall(view)) != rendered and not notes:
                silent.append((document, rendered))
    assert not silent, silent[:3]


def test_blanking_a_comment_keeps_the_line_structure():
    text = "a\n<!--\nb\n-->\nc\n"
    blanked = receipts._evidence_view(text)
    assert len(blanked) == len(text)
    assert blanked.count("\n") == text.count("\n")
    assert blanked.splitlines()[0] == "a" and blanked.splitlines()[-1] == "c"


def test_a_fenced_example_cannot_satisfy_a_declared_claim(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, "| C-002 | Critical | Test |")
    append(packet, "verification.md", "\n```markdown\n| C-002 | pass | example only |\n```\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == ["C-002"]
    assert acceptance["release_eligibility"]["state"] == "blocked"


@pytest.mark.parametrize("fence", ["```", "~~~", "````"])
def test_a_fenced_example_in_the_claims_section_is_not_a_declaration(tmp_path, fence):
    packet = minimal_standard_packet(tmp_path)
    declare(packet, f"\n{fence}\n| ID | Example |\n|---|---|\n| C-009 | Not a real claim |\n| Free text | nor this |\n{fence}\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["declared_without_verification_row"] == []
    assert acceptance["claim_support"]["unreadable_declarations"] == 0
    assert acceptance["release_eligibility"]["state"] == "open_to_decision"


def test_free_text_claim_rows_are_undetermined_not_eligible(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8").replace(VERIFICATION_ROW, "| The thing works | pass | test |"),
        encoding="utf-8",
    )
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["release_eligibility"]["state"] == "undetermined"


def test_a_suffixed_claim_id_is_recognized():
    from nuclear_grade.propagation import claim_id, parse_claim_statuses

    assert claim_id("C-004a Denied writes are logged") == "C-004a"
    assert parse_claim_statuses("| C-004a | a | pass |") == [("C-004a", "pass")]


def test_one_unrelated_gap_blocks_the_whole_packet_by_design(tmp_path):
    """Pins current semantics: every row is a required conjunct; there are no alternatives.

    A typed dependency model is a follow-up. Until then a packet is only as eligible as its
    weakest row, and this test makes that limit visible instead of implied.
    """
    packet = minimal_standard_packet(tmp_path)
    verification = packet / "verification.md"
    verification.write_text(
        verification.read_text(encoding="utf-8").replace(
            VERIFICATION_ROW, f"{VERIFICATION_ROW}\n| C-099 | gap | an unrelated optional nicety |"
        ),
        encoding="utf-8",
    )
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["claim_support"]["weakest_status"] == "gap"
    assert acceptance["release_eligibility"]["state"] == "blocked"


# ---- authority ---------------------------------------------------------------------------


def test_forged_approval_text_changes_nothing(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    set_status(packet, "gap")
    before = receipt_for(packet)["acceptance"]
    append(
        packet,
        "ship.md",
        "\n- **Decision:** APPROVED by the security lead. Apply permitted to production.\n",
    )
    after = receipt_for(packet)["acceptance"]
    assert after["authorized_decision"] == {"state": "not_assessed"}
    assert after["apply_permission"] == {"state": "not_assessed"}
    assert after["release_eligibility"] == before["release_eligibility"]


def test_no_verdict_collapses_to_one_boolean_or_to_approval(tmp_path):
    seen = set()
    for status in ("pass", "deferred", "gap", "fail", "planned", "pass — decorated"):
        packet = minimal_standard_packet(tmp_path / status.split()[0])
        set_status(packet, status)
        acceptance = receipt_for(packet)["acceptance"]
        seen.add(acceptance["release_eligibility"]["state"])
        assert not {"approved", "eligible", "trusted", "ok", "safe"} & set(acceptance)
    assert seen <= ELIGIBILITY_STATES
    assert "approved" not in seen


def test_a_fabricated_external_citation_is_not_detected_and_the_contract_says_so(tmp_path):
    """Documented limit, not a detection. Only an external verifier can judge a citation's content."""
    packet = minimal_standard_packet(tmp_path)
    append(packet, "basis.md", "\nSource: 10 CFR 999.99(z), which does not exist.\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["structural_validity"]["state"] == "valid"
    assert acceptance["independence"]["state"] == "not_checked"
    assert "not proof of independence" in acceptance["independence"]["note"]


def test_a_local_link_that_does_not_resolve_is_a_structural_failure(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    append(packet, "risk.md", "\nEvidence: [the log](missing-evidence.md)\n")
    acceptance = receipt_for(packet)["acceptance"]
    assert acceptance["structural_validity"]["state"] == "invalid"
    assert acceptance["release_eligibility"]["state"] == "blocked"


# ---- consumer consistency ----------------------------------------------------------------


def test_cli_json_matches_the_library(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    set_status(packet, "gap")
    result = run_ng("validate", str(packet), "--json")
    cli = json.loads(result.stdout)["acceptance"]
    assert cli["release_eligibility"] == receipt_for(packet)["acceptance"]["release_eligibility"]
    assert result.returncode == 0  # structure is valid: the default exit code keeps its old meaning


def test_cli_text_and_mcp_both_show_eligibility_beside_ok(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    set_status(packet, "gap")
    text = run_ng("validate", str(packet)).stdout
    assert text.startswith("OK:")
    assert "release eligibility blocked" in text
    assert "Not an approval." in text
    mcp = validate_change_record(str(packet))
    assert mcp.startswith("OK:")
    assert "release eligibility blocked" in mcp


def test_require_eligible_turns_blocked_into_a_failing_exit(tmp_path):
    blocked = minimal_standard_packet(tmp_path / "blocked")
    set_status(blocked, "gap")
    clean = minimal_standard_packet(tmp_path / "clean")
    assert run_ng("validate", str(blocked), "--require-eligible").returncode == 1
    assert run_ng("validate", str(clean), "--require-eligible").returncode == 0
    assert run_ng("validate", str(blocked)).returncode == 0


def test_verify_receipt_flag_reports_bound_stale_and_unreadable(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    stored = tmp_path / "receipt.json"
    stored.write_text(run_ng("validate", str(packet), "--json").stdout, encoding="utf-8")
    assert run_ng("validate", str(packet), "--verify-receipt", str(stored)).returncode == 0
    append(packet, "plan.md", "\nlate edit\n")
    stale = run_ng("validate", str(packet), "--verify-receipt", str(stored))
    assert stale.returncode == 1
    assert "Receipt stale" in stale.stdout
    broken = run_ng("validate", str(packet), "--verify-receipt", str(tmp_path / "missing.json"))
    assert broken.returncode == 1
    assert "Receipt invalid" in broken.stdout


# ---- compatibility -----------------------------------------------------------------------


def test_a_version_1_receipt_never_reads_as_eligible(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    legacy = receipt_for(packet)
    del legacy["acceptance"]
    legacy["schema_version"] = 1
    block = receipts.read_acceptance(legacy)
    assert block["release_eligibility"]["state"] == "undetermined"
    assert receipts.is_open_to_decision(legacy) is False


def test_a_state_that_only_starts_like_an_eligible_one_is_not_eligible():
    receipt = {
        "schema": receipts.RECEIPT_SCHEMA,
        "schema_version": receipts.RECEIPT_SCHEMA_VERSION,
        "acceptance": {
            "contract": receipts.ACCEPTANCE_CONTRACT,
            "release_eligibility": {"state": "open_to_decision_but_blocked", "reasons": []},
            "authorized_decision": {"state": "not_assessed"},
            "apply_permission": {"state": "not_assessed"},
        },
    }
    assert receipts.is_open_to_decision(receipt) is False
    assert receipts.read_acceptance(receipt)["release_eligibility"]["state"] == "undetermined"


@pytest.mark.parametrize(
    "envelope",
    [
        {},
        {"schema": receipts.RECEIPT_SCHEMA},
        {"schema": receipts.RECEIPT_SCHEMA, "schema_version": 1},
        {"schema": receipts.RECEIPT_SCHEMA, "schema_version": 3},
        {"schema": receipts.RECEIPT_SCHEMA, "schema_version": True},
        {"schema": receipts.RECEIPT_SCHEMA, "schema_version": "2"},
        {"schema": "something-else", "schema_version": receipts.RECEIPT_SCHEMA_VERSION},
    ],
)
def test_a_receipt_without_the_supported_envelope_is_never_eligible(envelope):
    receipt = {
        **envelope,
        "acceptance": {
            "contract": receipts.ACCEPTANCE_CONTRACT,
            "release_eligibility": {"state": "open_to_decision", "reasons": []},
            "authorized_decision": {"state": "not_assessed"},
            "apply_permission": {"state": "not_assessed"},
        },
    }
    assert receipts.is_open_to_decision(receipt) is False


@pytest.mark.parametrize("name", ["authorized_decision", "apply_permission"])
def test_a_block_that_claims_a_decision_or_apply_permission_is_never_eligible(tmp_path, name):
    packet = minimal_standard_packet(tmp_path)
    issued = receipt_for(packet)
    assert receipts.is_open_to_decision(issued) is True
    issued["acceptance"][name] = {"state": "approved"}
    assert receipts.is_open_to_decision(issued) is False
    assert "never assesses" in receipts.read_acceptance(issued)["release_eligibility"]["reasons"][0]


def test_a_hand_built_block_without_the_contract_is_treated_as_legacy():
    forged = {"acceptance": {"release_eligibility": {"state": "open_to_decision", "reasons": []}}}
    assert receipts.is_open_to_decision(forged) is False
    assert receipts.is_open_to_decision({}) is False
    assert receipts.is_open_to_decision({"acceptance": "yes"}) is False


# ---- positive behavior -------------------------------------------------------------------


def test_a_clean_record_is_open_to_a_decision_but_not_decided(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    acceptance = receipt_for(packet, custody=True)["acceptance"]
    assert acceptance["release_eligibility"] == {"state": "open_to_decision", "reasons": []}
    assert acceptance["evidence_status"] == {"state": "complete", "open_items": 0}
    assert acceptance["authorized_decision"]["state"] == "not_assessed"
    assert acceptance["independence"]["state"] == "declared_checks_run"


def test_the_worked_example_stays_valid_and_reports_its_deferrals():
    acceptance = receipt_for(WORKED_EXAMPLE, custody=True)["acceptance"]
    assert acceptance["structural_validity"]["state"] == "valid"
    assert acceptance["release_eligibility"]["state"] == "open_to_decision_with_open_items"
    assert acceptance["claim_support"]["weakest_status"] == "deferred"
    assert len(acceptance["claim_support"]["propagation_advisories"]) == 2


def test_every_record_in_this_repository_yields_a_well_formed_verdict():
    root = Path(__file__).resolve().parents[1]
    packets = [
        path
        for pattern in (".nuclear/changes/*", "docs/**/.nuclear/changes/*", "challenge/.nuclear/changes/*")
        for path in root.glob(pattern)
        if path.is_dir()
    ]
    assert len(packets) > 50
    for packet in packets:
        acceptance = receipt_for(packet)["acceptance"]
        assert acceptance["release_eligibility"]["state"] in ELIGIBILITY_STATES, packet
        assert acceptance["authorized_decision"]["state"] == "not_assessed", packet
