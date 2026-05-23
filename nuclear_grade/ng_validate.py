"""Minimal Nuclear-grade packet validator.

Checks structure and evidence visibility. It does not decide engineering adequacy,
safety, security, or compliance.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


QUICK_MODE = "quick"
STANDARD_MODE = "standard"
REQUIRED_QUICK_FILES = ("risk.md", "proof.md")
REQUIRED_STANDARD_FILES = ("risk.md", "basis.md", "plan.md", "trace.md", "verification.md", "ship.md")
STANDARD_ONLY_FILES = tuple(name for name in REQUIRED_STANDARD_FILES if name != "risk.md")
REQUIRED_SECTIONS = ("Required links", "Exit criteria", "Source-lineage note")
EVIDENCE_STATUSES = ("pass", "fail", "gap", "deferred", "not applicable", "planned")
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PROHIBITED_CLAIMS = (
    "NQA-1 compliant",
    "ASME compliant",
    "EPRI compliant",
    "IEEE compliant",
    "IEC compliant",
    "ISO compliant",
    "ANSI/ANS compliant",
    "NEI compliant",
    "NRC compliant",
    "DOE compliant",
    "NASA compliant",
    "NIST compliant",
    "CISA compliant",
    "certified quality assurance program",
    "regulatory approval",
    "commercial-grade dedication package",
    "formal V&V",
    "formal verification and validation",
    "NQA-1 evidence",
    "NQA-1 record",
    "quality-assurance record",
    "safety-basis evidence",
    "procurement evidence",
)
BOUNDARY_PREFIXES = (
    "no ",
    "not ",
    "do not ",
    "does not ",
    "is not ",
    "not a ",
    "no formal ",
    "no compliance",
    "without ",
)


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    messages: list[str]


def validate_packet(packet: str | Path) -> ValidationResult:
    packet_path = Path(packet)
    messages: list[str] = []

    if not packet_path.exists():
        return ValidationResult(False, [f"packet does not exist: {packet_path}"])
    if not packet_path.is_dir():
        return ValidationResult(False, [f"packet is not a directory: {packet_path}"])

    mode = detect_packet_mode(packet_path)
    required_files = REQUIRED_QUICK_FILES if mode == QUICK_MODE else REQUIRED_STANDARD_FILES

    for name in required_files:
        if not (packet_path / name).exists():
            messages.append(f"missing required file: {name}")

    for md_file in sorted(packet_path.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        _check_required_sections(md_file, text, messages)
        _check_prohibited_claims(md_file, text, messages)
        _check_source_lineage(md_file, text, messages)
        _check_relative_links(packet_path, md_file, text, messages)

    evidence_file = packet_path / ("proof.md" if mode == QUICK_MODE else "verification.md")
    if evidence_file.exists():
        evidence_text = evidence_file.read_text(encoding="utf-8")
        if not _contains_status(evidence_text):
            messages.append(f"{evidence_file.name} must include at least one evidence status")

    ship = packet_path / "ship.md"
    if ship.exists():
        ship_text = ship.read_text(encoding="utf-8")
        for phrase in ("rollback", "monitoring", "release decision"):
            if phrase not in ship_text.lower():
                messages.append(f"ship.md must mention {phrase}")

    return ValidationResult(not messages, messages)


def detect_packet_mode(packet: str | Path) -> str:
    return _detect_mode(Path(packet))


def _detect_mode(packet_path: Path) -> str:
    if any((packet_path / name).exists() for name in STANDARD_ONLY_FILES):
        return STANDARD_MODE

    risk = packet_path / "risk.md"
    if risk.exists():
        risk_text = risk.read_text(encoding="utf-8").lower()
        if re.search(r"\bmode:\s*(standard|nuclear|incident|research board|release)\b", risk_text):
            return STANDARD_MODE

    return QUICK_MODE


def _check_required_sections(md_file: Path, text: str, messages: list[str]) -> None:
    for section in REQUIRED_SECTIONS:
        if section.lower() not in text.lower():
            messages.append(f"{md_file.name} missing required section: {section}")


def _check_source_lineage(md_file: Path, text: str, messages: list[str]) -> None:
    if "source-lineage note" not in text.lower():
        return
    if "source-map.md" not in text and "http://" not in text and "https://" not in text:
        messages.append(f"{md_file.name} source-lineage note must reference source-map.md or a public URL")


def _check_relative_links(packet_path: Path, md_file: Path, text: str, messages: list[str]) -> None:
    for match in MARKDOWN_LINK_PATTERN.finditer(text):
        target = match.group(1).strip()
        if _is_external_or_anchor(target):
            continue

        target_path = target.strip("<>").split("#", 1)[0]
        if not target_path:
            continue

        if not (md_file.parent / target_path).exists():
            rel_file = md_file.relative_to(packet_path)
            messages.append(f"{rel_file} has broken relative link: {target}")


def _is_external_or_anchor(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith(("http://", "https://", "mailto:"))
        or lowered.startswith("#")
    )


def _check_prohibited_claims(md_file: Path, text: str, messages: list[str]) -> None:
    lowered = text.lower()
    for phrase in PROHIBITED_CLAIMS:
        phrase_lower = phrase.lower()
        start = 0
        while True:
            index = lowered.find(phrase_lower, start)
            if index == -1:
                break
            context = lowered[max(0, index - 40) : index]
            if not _is_boundary_context(context):
                messages.append(f"{md_file.name} contains prohibited compliance claim: {phrase}")
            start = index + len(phrase_lower)


def _is_boundary_context(context: str) -> bool:
    compact = re.sub(r"\s+", " ", context).strip()
    return any(compact.endswith(prefix.strip()) or prefix in compact[-25:] for prefix in BOUNDARY_PREFIXES)


def _contains_status(text: str) -> bool:
    lowered = text.lower()
    return any(re.search(rf"\b{re.escape(status)}\b", lowered) for status in EVIDENCE_STATUSES)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Nuclear-grade change packet.")
    parser.add_argument("packet", type=Path, help="Path to .nuclear/changes/<slug>/")
    args = parser.parse_args(argv)

    result = validate_packet(args.packet)
    if result.ok:
        print(f"OK: {args.packet}")
        return 0

    print(f"FAILED: {args.packet}")
    for message in result.messages:
        print(f"- {message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
