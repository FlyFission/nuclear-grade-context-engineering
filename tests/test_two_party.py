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


def test_multi_letter_claim_with_description_is_checked(tmp_path):
    pkt = _packet(
        tmp_path,
        "| REQ-001 workspace boundary | m | c | pass | e | - |\n",
        AUTH_HEADER + "| REQ-001 workspace boundary | ben | ben |\n",
    )
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("REQ-001" in m and "independent second party" in m for m in messages)


def test_qualified_row_does_not_drop_base_pass_status(tmp_path):
    # A base `pass` row and a later qualified row normalize to the same id;
    # the weaker qualified status must not overwrite the load-bearing pass,
    # or the independence check would be silently skipped.
    pkt = _packet(
        tmp_path,
        "| REQ-001 | m | c | pass | e | - |\n"
        "| REQ-001 (live install) | m | c | deferred | e | - |\n",
        AUTH_HEADER + "| REQ-001 | ben | ben |\n",
    )
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("REQ-001" in m and "independent second party" in m for m in messages)


def test_missing_authorship_table_is_flagged(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("no authorship or custody row" in m for m in messages)


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


# --- custody-record source and validator wiring ---------------------------

import shutil  # noqa: E402

from nuclear_grade.ng_validate import validate_packet  # noqa: E402
from nuclear_grade.two_party import ClaimParty, parse_claim_status  # noqa: E402

WORKED = (
    Path(__file__).resolve().parents[1]
    / "docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions"
)


def _copy_worked(tmp_path: Path) -> Path:
    dest = tmp_path / "pkt"
    shutil.copytree(WORKED, dest)
    return dest


def test_suffixed_claim_ids_are_parsed():
    statuses = parse_claim_status(CLAIM_TABLE + "| C-004a | m | c | pass | e | - |\n")
    assert statuses == {"C-004a": "pass"}


def test_custody_and_authorship_rows_are_not_read_as_claims():
    text = (
        CLAIM_TABLE + "| C-001 | m | c | gap | e | - |\n\n"
        "## Evidence custody and coupling\n### Custody record\n"
        "| Evidence ID | Claim ID | Decisive? | Artifact | Change actor | Verified by |\n|---|---|---|---|---|---|\n"
        "| E-001 | C-001 | yes | pass | a | b |\n\n"
        + AUTH_HEADER + "| C-009 | a | pass |\n"
    )
    assert parse_claim_status(text) == {"C-001": "gap"}


def test_custody_self_check_is_not_a_second_party(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {"C-001": [ClaimParty("custody E-001", "maintainer", "ben", "maintainer", "self-check")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert any("self-check evidence only" in m for m in messages)


def test_custody_independent_row_satisfies(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {
        "C-001": [
            ClaimParty("custody E-001", "maintainer", "maintainer", "maintainer", "self-check"),
            ClaimParty("custody E-002", "ci", "ben", "maintainer", "independent reproduction"),
        ]
    }
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert messages == []


def test_placeholder_verifier_counts_as_empty(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {
        "C-001": [
            ClaimParty("custody E-001", "a", "no separate verifier; reproducible command only", "a", "diverse verification")
        ]
    }
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert any("empty" in m for m in messages)


def test_strict_fails_closed_without_claim_table(tmp_path):
    (tmp_path / "verification.md").write_text("# Verification\n\nAll good: pass.\n", encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages, required=True)
    assert any("nothing to check" in m for m in messages)


def test_default_mode_ignores_packets_without_authorship_table(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    messages: list[str] = []
    check_two_party(pkt, messages, required=False)
    assert messages == []


def test_default_mode_enforces_declared_authorship_table(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | - |\n",
        AUTH_HEADER + "| C-001 | ben | Ben |\n",
    )
    messages: list[str] = []
    check_two_party(pkt, messages, required=False)
    assert any("independent second party" in m for m in messages)


def test_worked_example_passes_default_but_fails_two_party():
    # The teaching example is honestly a self-check; the default validator keeps
    # accepting it, and --two-party refuses to call it independently verified.
    assert validate_packet(WORKED, require_custody=True).ok
    strict = validate_packet(WORKED, require_custody=True, require_two_party=True)
    assert not strict.ok
    assert any("C-001" in m and "verifier is empty" in m for m in strict.messages)


def test_worked_example_passes_two_party_with_independent_custody_row(tmp_path):
    pkt = _copy_worked(tmp_path)
    vfile = pkt / "verification.md"
    text = vfile.read_text(encoding="utf-8")
    custody_row = (
        "| E-002 | C-001 / C-004a | yes | reviewer re-ran pytest from a clean clone | "
        "AI-assisted maintainer process | second reviewer | second reviewer | second reviewer | "
        "second reviewer | second reviewer | second reviewer | second reviewer |\n"
    )
    profile_row = (
        "| E-002 | separated; a different person | partially separated; read the packet | "
        "partially separated; same tests | partially separated; reviewer owns the verdict | "
        "separated; own machine | independent reproduction | admitted; see `ship.md` |\n"
    )
    anchor_custody = "| E-001 | C-001 / C-004a | yes |"
    head, tail = text.split(anchor_custody, 1)
    first_line, rest = tail.split("\n", 1)
    text = head + anchor_custody + first_line + "\n" + custody_row + rest
    anchor_profile = "| E-001 | **coupled**"
    head, tail = text.split(anchor_profile, 1)
    first_line, rest = tail.split("\n", 1)
    text = head + anchor_profile + first_line + "\n" + profile_row + rest
    vfile.write_text(text, encoding="utf-8")
    result = validate_packet(pkt, require_custody=True, require_two_party=True)
    assert result.ok, result.messages


def test_two_party_requires_standard_packet(tmp_path):
    (tmp_path / "risk.md").write_text("## Selected mode\n- **Mode:** Quick\n", encoding="utf-8")
    result = validate_packet(tmp_path, require_two_party=True)
    assert any("requires a Standard packet" in m for m in result.messages)


# --- regressions from the independent review of this wiring -----------------
# Each case below passed `--two-party` (or failed an honest packet) before the
# fix; they are kept so the rule cannot quietly regress.

import pytest  # noqa: E402

SELF_CHECK = {"C-001": [ClaimParty("custody E-001", "a", "no separate verifier", "a", "self-check")]}


@pytest.mark.parametrize(
    "row",
    [
        "| C-001 | m | c | **pass** | e | - |",
        "| C-001 | m | c | pass (local) | e | - |",
        "| C-001 | m | c | pass — 4 passed | e | - |",
        "| `C-001` | m | c | pass | e | - |",
        "| **C-001** | m | c | pass | e | - |",
        "| C-001: workspace boundary | m | c | pass | e | - |",
        "| [C-001](trace.md) | m | c | pass | e | - |",
    ],
)
def test_formatted_rows_are_still_read(tmp_path, row):
    pkt = _packet(tmp_path, row + "\n| C-002 | m | c | deferred | e | - |\n")
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=SELF_CHECK)
    assert any("C-001" in m for m in messages), messages


@pytest.mark.parametrize(
    "verifier",
    ["TBD.", "none.", "(none)", "self", "the author", "same process", "?", "<reviewer>", "a."],
)
def test_placeholder_or_actor_spellings_are_not_second_parties(tmp_path, verifier):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {"C-001": [ClaimParty("custody E-001", "x", verifier, "a", "independent reproduction")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert any("C-001" in m for m in messages), verifier


def test_multi_actor_cell_excludes_each_actor(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {
        "C-001": [ClaimParty("custody E-001", "x", "agent:claude", "ben + agent:claude", "independent reproduction")]
    }
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert any("change actor" in m for m in messages)


def test_authorship_cannot_override_custody_self_check(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + "| C-001 | a | ben |\n")
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=SELF_CHECK)
    assert any("C-001" in m for m in messages)


def test_authorship_verifier_cannot_be_a_packet_change_actor(tmp_path):
    pkt = _packet(
        tmp_path,
        "| C-001 | m | c | pass | e | - |\n| C-002 | m | c | pass | e | - |\n",
        AUTH_HEADER + "| C-002 | agent:claude | Maintainer |\n",
    )
    parties = {"C-001": [ClaimParty("custody E-001", "ci", "ben", "maintainer", "independent reproduction")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert any("C-002" in m and "change actor" in m for m in messages), messages
    assert not any("C-001" in m for m in messages)


def test_tables_without_claim_and_status_columns_are_ignored(tmp_path):
    body = (
        "| C-001 | m | c | pass | e | - |\n\n"
        "## Commands\n| Method | Command | Result |\n|---|---|---|\n| E2E smoke | make e2e | pass |\n"
        "| SHA256 digest matches | sha256sum | pass |\n"
    )
    pkt = _packet(tmp_path, body, AUTH_HEADER + "| C-001 | agent:claude | ben |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert messages == []


def test_unreadable_status_fails_strict(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | passed locally | e | - |\n", AUTH_HEADER + "| C-001 | a | ben |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("cannot read it" in m for m in messages)


def test_custody_claim_missing_from_claim_table_fails(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | gap | e | - |\n")
    parties = {"C-007": [ClaimParty("custody E-001", "a", "ben", "a", "independent reproduction")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert any("C-007" in m and "no claim-to-evidence row" in m for m in messages)


def test_authorship_only_packet_can_pass_strict_without_custody(tmp_path):
    pkt = _copy_worked(tmp_path)
    vfile = pkt / "verification.md"
    text = vfile.read_text(encoding="utf-8")
    start = text.index("## Evidence custody and coupling")
    end = text.index("## Security / dependency")
    authorship = AUTH_HEADER + "| C-001 | agent:claude | ben |\n| C-004a | agent:claude | ben |\n\n"
    vfile.write_text(text[:start] + authorship + text[end:], encoding="utf-8")
    result = validate_packet(pkt, require_two_party=True)
    assert result.ok, result.messages
