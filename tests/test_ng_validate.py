from pathlib import Path

from tools.ng_validate import validate_packet

ROOT = Path(__file__).resolve().parents[1]


COMMON_TAIL = """
## Required links

- `risk.md`
- `source-map.md`

## Exit criteria

- Done.

## Source-lineage note

Original workflow mapped in `docs/00-standards-foundation/source-map.md`. No compliance claim is made.
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def minimal_quick_packet(root: Path) -> Path:
    packet = root / ".nuclear" / "changes" / "quick-demo"
    write(packet / "risk.md", "# Risk\n\n## Selected mode\n\n- **Mode:** Quick\n" + COMMON_TAIL)
    write(
        packet / "proof.md",
        "# Proof\n\n## Result\n\n- Status: pass\n- Evidence link: `risk.md`\n" + COMMON_TAIL,
    )
    return packet


def minimal_standard_packet(root: Path) -> Path:
    packet = root / ".nuclear" / "changes" / "standard-demo"
    write(packet / "risk.md", "# Risk\n\n## Selected mode\n\n- **Mode:** Standard\n" + COMMON_TAIL)
    write(
        packet / "basis.md",
        "# Basis\n\n## Derived requirements or claims\n\n| ID | Requirement / claim | Evidence planned |\n|---|---|---|\n| C-001 | Demo claim | Test |\n"
        + COMMON_TAIL,
    )
    write(packet / "plan.md", "# Plan\n\n## Build sequence\n\n1. Do the work.\n" + COMMON_TAIL)
    write(packet / "trace.md", "# Trace\n\n## Trace summary\n\n| ID | Status |\n|---|---|\n| C-001 | pass |\n" + COMMON_TAIL)
    write(
        packet / "verification.md",
        "# Verification\n\n## Evidence status legend\n\nUse: `pass`, `fail`, `gap`, `deferred`, `not applicable`.\n\n| Claim | Result status | Evidence link |\n|---|---|---|\n| C-001 | pass | test |\n"
        + COMMON_TAIL,
    )
    write(
        packet / "ship.md",
        "# Ship\n\n## Release decision\n\n- **Decision:** ship with residual risk\n\n## Evidence status summary\n\n| Area | Status | Link |\n|---|---|---|\n| Verification | pass | verification.md |\n\n## Rollback / restore plan\n\n- Revert the change.\n\n## Monitoring and post-release checks\n\n- Watch validation output.\n"
        + COMMON_TAIL,
    )
    return packet


def test_quick_packet_with_required_files_sections_and_status_passes(tmp_path):
    packet = minimal_quick_packet(tmp_path)

    result = validate_packet(packet)

    assert result.ok, result.messages


def test_quick_packet_missing_proof_fails(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    (packet / "proof.md").unlink()

    result = validate_packet(packet)

    assert not result.ok
    assert any("missing required file: proof.md" in message for message in result.messages)


def test_standard_packet_with_required_files_sections_and_statuses_passes(tmp_path):
    packet = minimal_standard_packet(tmp_path)

    result = validate_packet(packet)

    assert result.ok, result.messages


def test_standard_packet_missing_required_file_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    (packet / "trace.md").unlink()

    result = validate_packet(packet)

    assert not result.ok
    assert any("missing required file: trace.md" in message for message in result.messages)


def test_packet_with_broken_relative_markdown_link_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    with (packet / "basis.md").open("a", encoding="utf-8") as handle:
        handle.write("\n[missing](missing.md)\n")

    result = validate_packet(packet)

    assert not result.ok
    assert any("basis.md has broken relative link: missing.md" in message for message in result.messages)


def test_source_lineage_without_source_map_or_public_url_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    write(
        packet / "basis.md",
        "# Basis\n\n## Required links\n\n- `risk.md`\n\n## Exit criteria\n\n- Done.\n\n## Source-lineage note\n\nOriginal internal rationale only.\n",
    )

    result = validate_packet(packet)

    assert not result.ok
    assert any("basis.md source-lineage note must reference source-map.md or a public URL" in message for message in result.messages)


def test_packet_with_prohibited_compliance_claim_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    with (packet / "basis.md").open("a", encoding="utf-8") as handle:
        handle.write("\nThis change is NRC compliant.\n")

    result = validate_packet(packet)

    assert not result.ok
    assert any("prohibited compliance claim" in message for message in result.messages)


def test_packet_with_prohibited_formal_v_and_v_claim_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    with (packet / "verification.md").open("a", encoding="utf-8") as handle:
        handle.write("\nThis packet is formal V&V evidence.\n")

    result = validate_packet(packet)

    assert not result.ok
    assert any("prohibited compliance claim" in message for message in result.messages)


def test_boundary_context_for_prohibited_phrase_passes(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    with (packet / "basis.md").open("a", encoding="utf-8") as handle:
        handle.write("\nThis repo is not NRC compliant.\n")

    result = validate_packet(packet)

    assert result.ok, result.messages


def test_verification_without_status_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    write(
        packet / "verification.md",
        "# Verification\n\n## Claim-to-evidence table\n\nEvidence exists but no status words.\n"
        + COMMON_TAIL,
    )

    result = validate_packet(packet)

    assert not result.ok
    assert any("verification.md must include at least one evidence status" in message for message in result.messages)


def test_placeholder_marker_blocks_validation(tmp_path):
    packet = minimal_quick_packet(tmp_path)
    proof = packet / "proof.md"
    proof.write_text(
        "<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->\n"
        + proof.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    result = validate_packet(packet)

    assert not result.ok
    assert any(
        "proof.md still contains the placeholder marker" in message
        for message in result.messages
    )


def test_unfilled_quick_template_fails(tmp_path):
    packet = tmp_path / ".nuclear" / "changes" / "quick-template"
    packet.mkdir(parents=True)
    for name in ("risk.md", "proof.md"):
        write(packet / name, (ROOT / "templates" / "quick" / name).read_text(encoding="utf-8"))

    result = validate_packet(packet)

    assert not result.ok
    assert any("has unfilled template prompts" in message for message in result.messages)


def test_unfilled_standard_template_fails(tmp_path):
    packet = tmp_path / ".nuclear" / "changes" / "standard-template"
    packet.mkdir(parents=True)
    for name in ("risk.md", "basis.md", "plan.md", "trace.md", "verification.md", "ship.md"):
        write(packet / name, (ROOT / "templates" / "standard" / name).read_text(encoding="utf-8"))

    result = validate_packet(packet)

    assert not result.ok
    assert any("has unfilled template prompts" in message for message in result.messages)


def test_packet_without_mode_declaration_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    risk_text = (packet / "risk.md").read_text(encoding="utf-8")
    stripped = risk_text.replace("## Selected mode\n\n- **Mode:** Standard\n", "")
    (packet / "risk.md").write_text(stripped, encoding="utf-8")

    result = validate_packet(packet)

    assert not result.ok
    assert any("Selected mode" in message for message in result.messages)


def test_long_label_empty_prompt_is_detected(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    with (packet / "basis.md").open("a", encoding="utf-8") as handle:
        handle.write("\n- " + ("A" * 200) + ":\n")

    result = validate_packet(packet)

    assert not result.ok
    assert any("has unfilled template prompts" in message for message in result.messages)


PARAPHRASES_THAT_MUST_FAIL = (
    "This system meets NQA-1 requirements.",
    "The release is fully ASME qualified.",
    "Our tests conform to IEEE 829.",
    "The packet satisfies 10 CFR 50 Appendix B.",
    "We implement quality assurance per NQA-1.",
    "This deployment has been audited to NRC standards.",
    "The product is regulator-approved.",
)


def test_paraphrased_compliance_claims_all_fail(tmp_path):
    for index, phrase in enumerate(PARAPHRASES_THAT_MUST_FAIL):
        packet = minimal_standard_packet(tmp_path / f"case-{index}")
        basis = packet / "basis.md"
        text = basis.read_text(encoding="utf-8")
        marker = "## Source-lineage note"
        idx = text.find(marker)
        new_text = text[:idx] + f"## Independent assertion\n\n{phrase}\n\n" + text[idx:]
        basis.write_text(new_text, encoding="utf-8")

        result = validate_packet(packet)

        assert not result.ok, f"Expected failure for paraphrase: {phrase}"
        assert any(
            "prohibited compliance claim" in message for message in result.messages
        ), f"No prohibited-claim message for: {phrase}; got {result.messages}"


BOUNDARY_PHRASES_THAT_MUST_PASS = (
    "This work is inspired by NQA-1 concepts.",
    "Influenced by ASME structure, not aligned with it.",
    "We do not claim IEEE conformance.",
    "This repo is not NRC compliant and does not claim to be.",
    "No formal V&V is implied by this packet.",
)


def test_boundary_paraphrases_all_pass(tmp_path):
    for index, phrase in enumerate(BOUNDARY_PHRASES_THAT_MUST_PASS):
        packet = minimal_standard_packet(tmp_path / f"case-{index}")
        basis = packet / "basis.md"
        text = basis.read_text(encoding="utf-8")
        marker = "## Source-lineage note"
        idx = text.find(marker)
        new_text = text[:idx] + f"## Boundary statement\n\n{phrase}\n\n" + text[idx:]
        basis.write_text(new_text, encoding="utf-8")

        result = validate_packet(packet)

        assert result.ok, (
            f"Expected pass for boundary phrase: {phrase}; got messages: {result.messages}"
        )


FILLED_MISSION_ANCHOR = (
    "## Mission anchor\n\n"
    "- Objective: ship the drift control feature.\n"
    "- Success criteria: validator and tests pass; packet validates.\n"
    "- Non-goals: no contract rewrite; out of scope is changing the description rule.\n\n"
)


def _insert_before_tail(text: str, block: str) -> str:
    marker = "## Required links"
    idx = text.find(marker)
    return text[:idx] + block + text[idx:]


def test_filled_mission_anchor_passes(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    risk = packet / "risk.md"
    risk.write_text(_insert_before_tail(risk.read_text(encoding="utf-8"), FILLED_MISSION_ANCHOR), encoding="utf-8")

    result = validate_packet(packet)

    assert result.ok, result.messages


def test_mission_anchor_missing_non_goals_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    anchor = (
        "## Mission anchor\n\n"
        "- Objective: ship the feature.\n"
        "- Success criteria: tests pass.\n\n"
    )
    risk = packet / "risk.md"
    risk.write_text(_insert_before_tail(risk.read_text(encoding="utf-8"), anchor), encoding="utf-8")

    result = validate_packet(packet)

    assert not result.ok
    assert any("Mission anchor present but missing a non-goals" in m for m in result.messages)


def test_mission_anchor_absent_is_not_checked(tmp_path):
    packet = minimal_standard_packet(tmp_path)

    result = validate_packet(packet)

    assert result.ok, result.messages
    assert not any("Mission anchor" in m for m in result.messages)


def test_unresolved_clarification_marker_fails(tmp_path):
    packet = minimal_standard_packet(tmp_path)
    with (packet / "basis.md").open("a", encoding="utf-8") as handle:
        handle.write("\nOpen question: [NEEDS CLARIFICATION] which API version applies.\n")

    result = validate_packet(packet)

    assert not result.ok
    assert any("[NEEDS CLARIFICATION]" in m for m in result.messages)


# Internal link checker -----------------------------------------------------

from tools.ng_validate import check_internal_links  # noqa: E402


def test_check_internal_links_passes_when_targets_resolve(tmp_path):
    write(tmp_path / "a.md", "see [b](b.md)")
    write(tmp_path / "b.md", "ok")

    failures = check_internal_links(tmp_path, ["a.md"])

    assert failures == []


def test_check_internal_links_flags_missing_target(tmp_path):
    write(tmp_path / "a.md", "see [missing](does-not-exist.md)")

    failures = check_internal_links(tmp_path, ["a.md"])

    assert len(failures) == 1
    assert "does-not-exist.md" in failures[0]
    assert "a.md" in failures[0]


def test_check_internal_links_ignores_anchors(tmp_path):
    write(tmp_path / "a.md", "[here](#section) and [also](other.md#section)")
    write(tmp_path / "other.md", "ok")

    failures = check_internal_links(tmp_path, ["a.md"])

    assert failures == []


def test_check_internal_links_ignores_external_urls(tmp_path):
    write(
        tmp_path / "a.md",
        "[http](http://example.com) [https](https://example.com) [mail](mailto:x@y.z)",
    )

    failures = check_internal_links(tmp_path, ["a.md"])

    assert failures == []


def test_check_internal_links_resolves_relative_to_each_file(tmp_path):
    # nested file links to a sibling; should resolve to docs/sibling.md, not <root>/sibling.md
    write(tmp_path / "docs" / "nested.md", "[sibling](sibling.md)")
    write(tmp_path / "docs" / "sibling.md", "ok")

    failures = check_internal_links(tmp_path, ["docs/nested.md"])

    assert failures == []


def test_check_internal_links_skips_files_that_do_not_exist(tmp_path):
    # Files in the list that don't exist on disk are silently skipped --
    # the existence check is the doctor's REQUIRED_PUBLIC_FILES job, not this checker's.
    failures = check_internal_links(tmp_path, ["never-created.md"])

    assert failures == []
