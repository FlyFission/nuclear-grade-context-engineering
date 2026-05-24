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
