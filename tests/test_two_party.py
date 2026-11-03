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


# --- regressions from the Codex review of PR #124 ---------------------------


def test_multi_verifier_cell_naming_only_the_actors_is_not_a_second_party(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    same = {"C-001": [ClaimParty("custody E-002", "x", "agent:claude + ben", "ben + agent:claude", "independent reproduction")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=same)
    assert any("C-001" in m for m in messages)
    other = {"C-001": [ClaimParty("custody E-002", "x", "agent:claude + carol", "ben + agent:claude", "independent reproduction")]}
    messages = []
    check_two_party(pkt, messages, custody_parties=other)
    assert messages == []


@pytest.mark.parametrize("cell", ["*C-001*", "_C-001_", "~C-001~"])
def test_single_emphasis_claim_ids_are_still_checked(tmp_path, cell):
    pkt = _packet(tmp_path, f"| {cell} | m | c | pass | e | - |\n| C-004a | m | c | deferred | e | - |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m for m in messages), messages


def test_single_emphasis_status_is_read(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | *pass* | e | - |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m and "no authorship or custody row" in m for m in messages)


def test_pass_row_without_a_readable_id_fails_strict(tmp_path):
    pkt = _packet(tmp_path, "| see above | m | c | pass | e | - |\n| C-004a | m | c | deferred | e | - |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("no readable Claim ID" in m for m in messages)


# --- R-9 and identity aliases (external reviews of PR #124) -----------------


def test_self_generated_second_party_must_be_disclosed_in_ship(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    hidden = {"C-001": [ClaimParty("custody E-002", "agent:claude", "agent:claude", "ben", "independent reproduction", "admitted")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=hidden)
    assert any("generated and verified its own evidence" in m for m in messages)
    disclosed = {"C-001": [ClaimParty("custody E-002", "agent:claude", "agent:claude", "ben", "independent reproduction",
                                      "admitted; reproducer generated its own re-run, see ship.md")]}
    messages = []
    check_two_party(pkt, messages, custody_parties=disclosed)
    assert messages == []


def test_separate_generator_and_verifier_needs_no_disclosure(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {"C-001": [ClaimParty("custody E-002", "ci", "carol", "ben", "independent reproduction", "admitted")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert messages == []


@pytest.mark.parametrize("alias", ["Claude", "claude-opus-5.5", "agent:claude-reviewer", "assistant", "me", "the agent"])
def test_aliases_of_the_actor_or_generic_agents_are_not_second_parties(tmp_path, alias):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {"C-001": [ClaimParty("custody E-002", "ci", alias, "agent:claude", "independent reproduction", "see ship.md")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert any("C-001" in m for m in messages), alias


# --- second Codex and Copilot review round on PR #124 -----------------------


@pytest.mark.parametrize("verifier", ["no verifier", "No reviewer yet", "not reviewed", "unverified", "ben + N/A", "ben + n / a"])
def test_negative_phrases_and_split_placeholders_name_no_second_party(tmp_path, verifier):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + f"| C-001 | ben | {verifier} |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m for m in messages), verifier


@pytest.mark.parametrize("wrap", [("<!--\n", "-->\n"), ("```markdown\n", "```\n"), ("~~~\n", "~~~\n")])
def test_commented_or_fenced_authorship_does_not_count(tmp_path, wrap):
    opening, closing = wrap
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", opening + AUTH_HEADER + "| C-001 | ben | carol |\n" + closing)
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m and "no authorship or custody row" in m for m in messages)


def test_claim_table_without_outer_pipes_is_read(tmp_path):
    body = (
        "# Verification\n\nClaim ID | Result status\n--- | ---\nC-001 | pass\n\n"
        + CLAIM_TABLE
        + "| C-004a | m | c | deferred | e | - |\n"
    )
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages)
    assert any("C-001" in m for m in messages)


def test_conflicting_authorship_rows_fail_closed(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + "| C-001 | ben | ben |\n| C-001 | ben | carol |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("conflicting Claim authorship rows" in m for m in messages)
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + "| C-001 | ben | carol |\n| C-001 | ben | carol |\n")
    messages = []
    check_two_party(pkt, messages)
    assert messages == []


def test_empty_authorship_heading_opts_in_by_default(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", "## Claim authorship\n\nTBD\n")
    messages: list[str] = []
    check_two_party(pkt, messages, required=False)
    assert any("C-001" in m for m in messages)


def test_mixed_verifier_cell_keeps_the_independent_witness(tmp_path):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n")
    parties = {"C-001": [ClaimParty("custody E-002", "alice", "alice + carol", "ben", "independent reproduction", "admitted")]}
    messages: list[str] = []
    check_two_party(pkt, messages, custody_parties=parties)
    assert messages == []


@pytest.mark.parametrize("wrap", [("<!--\n", "-->\n\n"), ("```markdown\n", "```\n\n")])
def test_hidden_custody_section_supplies_no_second_party(tmp_path, wrap):
    # Codex on 931448b: a custody record inside a comment or fence still passed.
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
    for anchor, row in (("| E-001 | C-001 / C-004a | yes |", custody_row), ("| E-001 | **coupled**", profile_row)):
        head, tail = text.split(anchor, 1)
        first_line, rest = tail.split("\n", 1)
        text = head + anchor + first_line + "\n" + row + rest
    assert validate_packet_text(pkt, vfile, text).ok  # visible: passes
    start = text.index("## Evidence custody and coupling")
    end = text.index("## Security / dependency")
    hidden = text[:start] + wrap[0] + text[start:end] + wrap[1] + text[end:]
    result = validate_packet_text(pkt, vfile, hidden)
    assert not result.ok


def validate_packet_text(pkt, vfile, text):
    vfile.write_text(text, encoding="utf-8")
    return validate_packet(pkt, require_custody=True, require_two_party=True)


# --- forwarded Gemini review: vendor paths in model identities ---------------


@pytest.mark.parametrize(
    "author, verifier",
    [
        ("agent: anthropic/claude-3.5-sonnet", "anthropic/claude-3.5-sonnet"),
        ("claude-3.5-sonnet", "anthropic/claude-3.5-sonnet"),
        ("agent:claude", "openrouter/claude-opus"),
    ],
)
def test_vendor_path_prefix_is_not_a_second_party(tmp_path, author, verifier):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + f"| C-001 | {author} | {verifier} |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m for m in messages), (author, verifier)


@pytest.mark.parametrize("verifier", ["carol", "ben / carol", "ben + carol", "openai/gpt-reviewer"])
def test_distinct_verifiers_still_pass_with_slashes(tmp_path, verifier):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + f"| C-001 | ben | {verifier} |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert messages == [], verifier


# --- Codex on c164d8b --------------------------------------------------------


def test_longer_outer_fence_is_not_closed_by_an_inner_fence(tmp_path):
    hidden = "````markdown\n```markdown\n" + AUTH_HEADER + "| C-001 | ben | carol |\n```\n````\n"
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", hidden)
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m and "no authorship or custody row" in m for m in messages)


@pytest.mark.parametrize("conj", ["AND", "And", "and"])
def test_actor_conjunction_splits_in_any_case(tmp_path, conj):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + f"| C-001 | ben {conj} agent:claude | agent:claude |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m for m in messages), conj


@pytest.mark.parametrize(
    "text",
    [
        "a\n```\nx\n```\nb\n",
        "````md\n```\ninner\n```\n````\nafter\n",
        "~~~\n```\n~~~\nafter\n",
        "  ```py\ncode\n  ```\n",
        "```\nunclosed\n",
        "``` `not a fence`\ntext\n",
        "````\n```\nstill hidden\n",
    ],
)
def test_fence_stripping_matches_the_validator(text):
    # The two parsers must agree on what is hidden, or a declaration could be
    # visible to one and hidden from the other.
    from nuclear_grade.ng_validate import _strip_code_blocks
    from nuclear_grade.two_party import _visible

    assert _visible(text) == _strip_code_blocks(text)


# --- Codex on a6867fa: read claims generously, declarations strictly ---------


def _indent(block: str) -> str:
    return "".join("    " + line + "\n" for line in block.splitlines())


def test_indented_authorship_example_does_not_count(tmp_path):
    example = "Example:\n\n" + _indent(AUTH_HEADER + "| C-001 | ben | carol |")
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", example)
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m and "no authorship or custody row" in m for m in messages)


def test_indented_custody_section_supplies_no_second_party(tmp_path):
    pkt = _copy_worked(tmp_path)
    vfile = pkt / "verification.md"
    text = vfile.read_text(encoding="utf-8")
    start = text.index("## Evidence custody and coupling")
    end = text.index("## Security / dependency")
    vfile.write_text(text[:start] + _indent(text[start:end]) + "\n" + text[end:], encoding="utf-8")
    result = validate_packet(pkt, require_custody=True)
    assert not result.ok
    assert any("missing required section: Evidence custody and coupling" in m for m in result.messages)


def test_claim_row_missing_its_status_cell_fails_strict(tmp_path):
    body = "# V\n## Claims\n| Claim ID | Result status |\n|---|---|\n| C-001 |\n| C-004a | deferred |\n"
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages)
    assert any("C-001" in m and "cannot read it" in m for m in messages)


# --- Codex on a50edba: one pass for comments and fences ----------------------

_T = "| Claim ID | Result status |\n|---|---|\n"


@pytest.mark.parametrize(
    "between",
    [
        "<!--\n```md\n-->\n",          # fence opener inside a comment
        "```\n<!--\n```\n",            # comment opener inside a fence
        "text <!-- ``` --> more\n",    # fence marker inside an inline comment
        "<!-- a --> ~~~ <!-- b\n-->\n",
    ],
)
def test_markers_inside_the_other_context_cannot_hide_visible_claims(tmp_path, between):
    body = "# V\n## A\n" + _T + "| C-004a | deferred |\n\n" + between + "\n## B\n" + _T + "| C-001 | pass |\n"
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages)
    assert any("C-001" in m for m in messages), between


def test_visible_keeps_text_around_an_inline_comment():
    from nuclear_grade.two_party import _visible

    out = _visible("keep <!-- hide --> keep\n```\nhidden\n```\nshown\n")
    assert out.split() == ["keep", "keep", "shown"]
    assert out.count("\n") == 5


# --- Codex on 9b920ee: no markup can hide a claim ----------------------------


@pytest.mark.parametrize(
    "wrap",
    [
        ("Use `<!--` to open a comment.\n\n", "\nClose with `-->`.\n"),
        ("<!--\n", "-->\n"),
        ("```\n", "```\n"),
        ("", ""),
    ],
)
def test_claims_are_read_from_the_raw_file(tmp_path, wrap):
    body = (
        "# V\n## A\n" + _T + "| C-004a | deferred |\n\n" + wrap[0]
        + "## B\n" + _T + "| C-001 | pass |\n" + wrap[1]
    )
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages)
    assert any("C-001" in m for m in messages), wrap


@pytest.mark.parametrize(
    "prose, counts",
    [
        ("Docs mention `<!--` in inline code.\n\n", True),     # code span: text
        ("An unclosed <!-- opener mid-line.\n\n", True),       # no closer: literal
        ("<!--\n", False),                                     # block comment to EOF
        ("Inline <!-- hidden --> comment.\n\n", True),
    ],
)
def test_comment_markers_follow_markdown_rules_for_declarations(tmp_path, prose, counts):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", prose + AUTH_HEADER + "| C-001 | ben | carol |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert (messages == []) is counts, (prose, messages)


def test_this_change_record_passes_strict_custody():
    # It once failed: a literal `<!--` in its own review log hid its custody
    # section. Keep the packet that ships the parser valid under its own rules.
    packet = Path(__file__).resolve().parents[1] / ".nuclear" / "changes" / "independent-review-and-fact-checking"
    result = validate_packet(packet, require_custody=True)
    assert result.ok, result.messages


def test_pass_row_cut_short_before_its_claim_cell_fails_strict(tmp_path):
    # Codex on 9b920ee: status column first, then a row that ends before its claim cell.
    body = "# V\n## Claims\n| Result status | Claim ID |\n|---|---|\n| pass |\n| deferred | C-004a |\n"
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages)
    assert any("no readable Claim ID" in m for m in messages)


# --- Codex on 4e951a1: authorship roles come from headers --------------------


def test_reordered_authorship_columns_are_read_by_header(tmp_path):
    swapped = "## Claim authorship\n| Claim ID | Verified by | Evidence author |\n|---|---|---|\n"
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", swapped + "| C-001 | TBD | agent:claude |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m for m in messages)
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", swapped + "| C-001 | carol | agent:claude |\n")
    messages = []
    check_two_party(pkt, messages)
    assert messages == []


def test_authorship_table_with_unrecognized_headers_declares_nothing(tmp_path):
    vague = "## Claim authorship\n| Claim ID | Person A | Person B |\n|---|---|---|\n"
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", vague + "| C-001 | ben | carol |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m and "no authorship or custody row" in m for m in messages)


@pytest.mark.parametrize("verifier", ["ben + agent:TBD", "agent:self", "agent: assistant", "human:none", "agent:<reviewer>", "ben + reviewer:N/A"])
def test_role_prefixed_placeholders_name_no_second_party(tmp_path, verifier):
    # Codex on 8e23443: a role prefix hid a placeholder.
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + f"| C-001 | ben | {verifier} |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert any("C-001" in m for m in messages), verifier


@pytest.mark.parametrize("verifier", ["agent:carol-bot", "human:carol", "ben + human:carol"])
def test_role_prefixed_real_names_still_count(tmp_path, verifier):
    pkt = _packet(tmp_path, "| C-001 | m | c | pass | e | - |\n", AUTH_HEADER + f"| C-001 | ben | {verifier} |\n")
    messages: list[str] = []
    check_two_party(pkt, messages)
    assert messages == [], verifier


def test_pipe_free_body_row_does_not_end_a_delimited_table(tmp_path):
    # Codex on ff6f7f2: GitHub Markdown keeps a pipe-free line as a one-cell row.
    body = (
        "# V\n\nClaim ID | Result status\n--- | ---\nC-001\nC-002 | pass\n\n"
        "## Other\n" + _T + "| C-004a | deferred |\n"
    )
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages)
    assert any("C-002" in m for m in messages), messages
    assert any("C-001" in m and "cannot read it" in m for m in messages), messages


@pytest.mark.parametrize("between", ["## Claims | local\n", "### Claims | local\n", "> note | x\n", ""])
def test_block_start_with_a_pipe_ends_the_previous_table(tmp_path, between):
    # Codex on b37030d: a heading containing a pipe was absorbed into the table above it.
    body = (
        "# V\n| Meta | Value |\n|---|---|\n| owner | ben |\n" + between
        + "| Claim ID | Result status |\n|---|---|\n| C-001 | pass |\n\n"
        "## Other\n" + _T + "| C-004a | deferred |\n"
    )
    (tmp_path / "verification.md").write_text(body, encoding="utf-8")
    messages: list[str] = []
    check_two_party(tmp_path, messages)
    assert any("C-001" in m for m in messages), (between, messages)
