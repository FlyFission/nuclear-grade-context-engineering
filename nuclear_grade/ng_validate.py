"""Small Nuclear-grade change-record checker.

Checks structure and whether evidence is visible. It does not decide engineering
adequacy, safety, security, or compliance.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

PLACEHOLDER_MARKER = "NUCLEAR-GRADE-PLACEHOLDER"
# A packet deliberately abandoned with a recorded rationale carries this marker.
# `ng status` reports such a packet as `closed` (a terminal state), not as needing
# attention. See the closing-stale-packets skill.
CLOSURE_MARKER = "NUCLEAR-GRADE-CLOSED"
# A genuine closure is the marker followed by a colon and a substantive rationale
# on the same line, matching the shape the skill and CLI docs require. A bare
# marker, or the marker merely mentioned in prose, does not count -- otherwise a
# packet could be suppressed from `ng status` without recording why it was dropped.
# Horizontal whitespace only (`[^\S\n]`): the rationale must be on the SAME line as
# the marker. A plain `\s*` would let the match cross a newline and grab the next
# line's text, so a bare marker followed by normal content would falsely qualify.
CLOSURE_NOTE_PATTERN = re.compile(
    rf"^[^\S\n]*{re.escape(CLOSURE_MARKER)}:[^\S\n]*\S.*$", re.MULTILINE
)


def has_closure_note(text: str) -> bool:
    """True when text carries a `NUCLEAR-GRADE-CLOSED:` line with a real rationale."""

    return CLOSURE_NOTE_PATTERN.search(text) is not None
QUICK_MODE = "quick"
STANDARD_MODE = "standard"
UNSPECIFIED_MODE = "unspecified"
REQUIRED_QUICK_FILES = ("risk.md", "proof.md")
REQUIRED_STANDARD_FILES = ("risk.md", "basis.md", "plan.md", "trace.md", "verification.md", "ship.md")
STANDARD_ONLY_FILES = tuple(name for name in REQUIRED_STANDARD_FILES if name != "risk.md")
REQUIRED_SECTIONS = ("Required links", "Exit criteria", "Source-lineage note")
EVIDENCE_STATUSES = ("pass", "fail", "gap", "deferred", "not applicable", "planned")
COUPLING_PROFILE_AXES = ("actor", "context", "mechanism", "authority", "resource")
EVIDENCE_CUSTODY_ROLES = ("generated", "selected", "transformed", "captured", "retained", "presented")
COUPLING_VALUES = ("coupled", "partially separated", "separated")
RECORD_ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*-[0-9][A-Za-z0-9._-]*$")
DECISIVE_VALUES = {"yes", "no"}
EVIDENCE_CLASSIFICATIONS = {
    "self-check",
    "independent reproduction",
    "diverse verification",
    "direct witnessing",
}
AUTHORITY_RAW_STATES = {"observed", "bounded_absence", "unknown", "disputed"}
DECISION_RIGHTS = {
    "prepare",
    "recommend",
    "verify",
    "validate",
    "verdict",
    "accept",
    "apply",
    "reopen",
    "close",
}
AUTHORITY_RESULTS = {
    "agent_authorized",
    "human_required",
    "separate_control_required",
    "dual_authority_required",
    "blocked_pending_evidence",
    "prohibited_for_agent",
    "indeterminate",
}
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
EMPTY_PROMPT_PATTERN = re.compile(
    r"^\s*-\s+[^|\n:][^:\n]*?:\s*$|^\s*(?:Claim|Question|Answer|Decision|Rationale):\s*$",
    re.MULTILINE,
)
EMPTY_TABLE_CELL_PATTERN = re.compile(r"\|[ \t]*\|")
MODE_DECLARATION_PATTERN = re.compile(
    r"##\s*Selected\s*mode\b[\s\S]{0,400}?(?:\*\*Mode:\*\*|Mode:)\s*(quick|standard|nuclear|incident|research board|release)",
    re.IGNORECASE,
)

# Fixed phrases retained for noun-only items the verb-stem matcher will not catch.
PROHIBITED_CLAIMS = (
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

# Paraphrase patterns. The entity (NQA-1, ASME, NRC, ...) and a positive-claim
# verb stem must be adjacent (within a few tokens). Negation gates handled
# separately by _is_boundary_context and _sentence_has_boundary.
_ENTITY = (
    r"NQA[- ]?1|ASME|EPRI|IEEE(?:\s+\d+)?|IEC(?:\s+\d+)?|ISO(?:\s+\d+)?|"
    r"ANSI(?:/ANS)?|ANS\s+\d+|NEI|NRC|DOE|NASA|NIST|CISA|"
    r"10\s*CFR(?:\s*\d+)?(?:\s+Appendix\s+[A-Z])?"
)
PARAPHRASE_PATTERNS = (
    # "meets NQA-1 requirements", "conforms to IEEE 829", "satisfies 10 CFR 50",
    # "complies with ASME"
    re.compile(
        r"\b(?:meets?|conform(?:s|ing)?\s+to|compl(?:y|ies)\s+with|"
        r"satisf(?:y|ies|ied|ying)|"
        r"implements?\s+\w*\s*(?:per|to)\s+(?:requirements?\s+of\s+)?)\s+"
        r"(?:" + _ENTITY + r")\b",
        re.IGNORECASE,
    ),
    # "<entity> compliant", "<entity> qualified", "<entity> certified",
    # "fully ASME qualified"
    re.compile(
        r"\b(?:" + _ENTITY + r")\s*[-/]?\s*"
        r"(?:compliant|qualified|certified|approved|conformant)\b",
        re.IGNORECASE,
    ),
    # "audited to NRC standards"
    re.compile(r"\baudited\s+to\s+(?:" + _ENTITY + r")\b", re.IGNORECASE),
    # "implements quality assurance per NQA-1"
    re.compile(
        r"\bimplements?\s+quality\s+assurance\s+per\s+(?:" + _ENTITY + r")\b",
        re.IGNORECASE,
    ),
    # "regulator-approved", "regulator approved"
    re.compile(r"\bregulator[- ]?approved\b", re.IGNORECASE),
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
    "inspired by",
    "influenced by",
    "does not claim",
    "do not claim",
    "not implementing",
    "no claim of",
    "no claim to",
    "is not implementing",
)


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    messages: list[str]


def validate_packet(
    packet: str | Path,
    *,
    require_custody: bool = False,
    require_authority: bool = False,
) -> ValidationResult:
    packet_path = Path(packet)
    messages: list[str] = []

    if not packet_path.exists():
        return ValidationResult(False, [f"packet does not exist: {packet_path}"])
    if not packet_path.is_dir():
        return ValidationResult(False, [f"packet is not a directory: {packet_path}"])

    declared = _declared_mode(packet_path)
    if declared == UNSPECIFIED_MODE:
        messages.append(
            "risk.md must include a `## Selected mode` section with `- **Mode:** Quick` or `- **Mode:** Standard`"
        )

    mode = _detect_mode(packet_path)
    required_files: tuple[str, ...]
    if declared == UNSPECIFIED_MODE and mode == UNSPECIFIED_MODE:
        required_files = ("risk.md",)
    else:
        effective = mode if mode != UNSPECIFIED_MODE else declared
        required_files = REQUIRED_QUICK_FILES if effective == QUICK_MODE else REQUIRED_STANDARD_FILES

    for name in required_files:
        if not (packet_path / name).exists():
            messages.append(f"missing required file: {name}")

    for md_file in sorted(packet_path.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        if PLACEHOLDER_MARKER in text:
            messages.append(
                f"{md_file.name} still contains the placeholder marker; fill the packet and remove the marker line before validation can pass."
            )
        _check_required_sections(md_file, text, messages)
        _check_unfilled_template_prompts(md_file, text, messages)
        _check_prohibited_claims(md_file, text, messages)
        _check_source_lineage(md_file, text, messages)
        _check_relative_links(packet_path, md_file, text, messages)
        _check_mission_anchor(md_file, text, messages)
        _check_unresolved_clarifications(md_file, text, messages)

    effective_mode = mode if mode != UNSPECIFIED_MODE else declared
    if require_authority and effective_mode == QUICK_MODE:
        messages.append("strict authority requires a Standard packet")
    authority_file = packet_path / "decision-authority.md"
    if effective_mode == STANDARD_MODE and require_authority:
        if not authority_file.exists():
            messages.append("missing required file: decision-authority.md")
        else:
            _check_decision_authority(
                authority_file,
                authority_file.read_text(encoding="utf-8"),
                messages,
            )

    if effective_mode != UNSPECIFIED_MODE:
        evidence_file = packet_path / ("proof.md" if effective_mode == QUICK_MODE else "verification.md")
        if evidence_file.exists():
            evidence_text = evidence_file.read_text(encoding="utf-8")
            if not _contains_status(evidence_text):
                messages.append(f"{evidence_file.name} must include at least one evidence status")
            if effective_mode == STANDARD_MODE:
                _check_evidence_custody(
                    evidence_file,
                    evidence_text,
                    messages,
                    required=require_custody or require_authority,
                )

    ship = packet_path / "ship.md"
    if ship.exists():
        ship_text = ship.read_text(encoding="utf-8")
        for phrase in ("rollback", "monitoring", "release decision"):
            if phrase not in ship_text.lower():
                messages.append(f"ship.md must mention {phrase}")

    return ValidationResult(not messages, messages)


def detect_packet_mode(packet: str | Path) -> str:
    mode = _detect_mode(Path(packet))
    return QUICK_MODE if mode == UNSPECIFIED_MODE else mode


def _declared_mode(packet_path: Path) -> str:
    """Return the explicitly declared mode from risk.md, or UNSPECIFIED.

    Unlike _detect_mode, never falls back to file-presence inference.
    """

    risk = packet_path / "risk.md"
    if not risk.exists():
        return UNSPECIFIED_MODE
    risk_text = risk.read_text(encoding="utf-8")
    match = MODE_DECLARATION_PATTERN.search(risk_text)
    if not match:
        return UNSPECIFIED_MODE
    declared = match.group(1).lower()
    return QUICK_MODE if declared == "quick" else STANDARD_MODE


def _detect_mode(packet_path: Path) -> str:
    declared = _declared_mode(packet_path)
    if declared != UNSPECIFIED_MODE:
        return declared

    if any((packet_path / name).exists() for name in STANDARD_ONLY_FILES):
        return STANDARD_MODE

    return UNSPECIFIED_MODE


def _check_required_sections(md_file: Path, text: str, messages: list[str]) -> None:
    for section in REQUIRED_SECTIONS:
        if section.lower() not in text.lower():
            messages.append(f"{md_file.name} missing required section: {section}")


def _check_unfilled_template_prompts(md_file: Path, text: str, messages: list[str]) -> None:
    if EMPTY_PROMPT_PATTERN.search(text) or EMPTY_TABLE_CELL_PATTERN.search(_table_body(text)):
        messages.append(
            f"{md_file.name} has unfilled template prompts; use concrete text, `not applicable`, `deferred`, or `gap`"
        )


def _table_body(text: str) -> str:
    rows = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if set(stripped.replace("|", "").replace(":", "").strip()) <= {"-"}:
            continue
        rows.append(line)
    return "\n".join(rows)


def _check_source_lineage(md_file: Path, text: str, messages: list[str]) -> None:
    if "source-lineage note" not in text.lower():
        return
    if "source-map.md" not in text and "http://" not in text and "https://" not in text:
        messages.append(f"{md_file.name} source-lineage note must reference source-map.md or a public URL")


MISSION_ANCHOR_CONCEPTS = (
    ("objective", ("objective", "mission", "goal")),
    ("success/done criterion", ("success", "done", "acceptance", "criteri")),
    (
        "non-goals / forbidden directions",
        ("non-goal", "non goal", "out of scope", "out-of-scope", "forbidden", "do not", "not in scope"),
    ),
)


def _check_mission_anchor(md_file: Path, text: str, messages: list[str]) -> None:
    """Advisory: only runs when a `## Mission anchor` section is present.

    A usable anchor names an objective, a success/done criterion, and explicit
    non-goals (the anti-drift teeth). Matching is by keyword family so authors
    are not forced into exact labels. Emptiness of individual prompts is already
    caught by _check_unfilled_template_prompts.
    """

    lowered = text.lower()
    if "## mission anchor" not in lowered:
        return

    section = _section_text(text, "## mission anchor")
    scannable = _strip_code_blocks(section).lower()
    for label, synonyms in MISSION_ANCHOR_CONCEPTS:
        if not any(token in scannable for token in synonyms):
            messages.append(f"{md_file.name} Mission anchor present but missing a {label}")


def _check_unresolved_clarifications(md_file: Path, text: str, messages: list[str]) -> None:
    if "[NEEDS CLARIFICATION]" in _strip_code_blocks(text):
        messages.append(
            f"{md_file.name} has an unresolved [NEEDS CLARIFICATION] marker; resolve it or record it as a labeled gap before ship"
        )


def _check_evidence_custody(
    md_file: Path,
    text: str,
    messages: list[str],
    *,
    required: bool,
) -> None:
    """Structurally lint a Standard packet's declared custody and coupling.

    This checks record consistency, not authenticated identity, semantic adequacy,
    or substantive independence. `required=False` keeps legacy packets valid while
    still rejecting a partial disclosure; `--strict-custody` requires the section.
    """

    heading = "## evidence custody and coupling"
    if heading not in text.lower():
        if required:
            messages.append(
                f"{md_file.name} missing required section: Evidence custody and coupling"
            )
        return

    section = _strip_code_blocks(_section_text(text, heading))
    if r"\|" in section:
        messages.append(
            f"{md_file.name} evidence custody tables do not support escaped pipe characters"
        )
        return
    tables = _markdown_tables(section)
    custody_required = (
        "evidence id",
        "claim id",
        "decisive",
        "artifact raw result",
        "change actor",
        "generated by",
        "selected by",
        "transformed summarized by",
        "executed captured by",
        "retained by",
        "presented by",
        "verified witnessed by",
    )
    profile_required = (
        "evidence id",
        "actor",
        "context",
        "mechanism",
        "authority",
        "resource",
        "classification",
        "admissibility residual risk disposition",
    )
    custody = _find_markdown_table(tables, custody_required)
    profile = _find_markdown_table(tables, profile_required)

    if custody is None:
        messages.append(
            f"{md_file.name} evidence custody section missing the custody table or required headers"
        )
    if profile is None:
        messages.append(
            f"{md_file.name} evidence custody section missing the coupling-profile table or required headers"
        )
    if custody is None or profile is None:
        return

    custody_headers, custody_rows = custody
    profile_headers, profile_rows = profile
    if not custody_rows:
        messages.append(f"{md_file.name} evidence custody table must include at least one evidence row")
        return
    if not profile_rows:
        messages.append(f"{md_file.name} coupling-profile table must include at least one profile row")
        return

    custody_index = {_normalize_table_label(value): index for index, value in enumerate(custody_headers)}
    profile_index = {_normalize_table_label(value): index for index, value in enumerate(profile_headers)}
    custody_ids: set[str] = set()
    decisive_ids: set[str] = set()
    custody_controls: dict[str, tuple[str, str, str, str, str]] = {}

    for row in custody_rows:
        if len(row) != len(custody_headers):
            messages.append(
                f"{md_file.name} evidence custody row has {len(row)} cells; expected {len(custody_headers)}"
            )
        evidence_id = _table_value(row, custody_index, "evidence id")
        claim_id = _table_value(row, custody_index, "claim id")
        decisive = _table_value(row, custody_index, "decisive").lower()
        artifact = _table_value(row, custody_index, "artifact raw result")
        change_actor = _table_value(row, custody_index, "change actor")
        generated_by = _table_value(row, custody_index, "generated by")
        selected_by = _table_value(row, custody_index, "selected by")
        transformed_by = _table_value(row, custody_index, "transformed summarized by")
        captured_by = _table_value(row, custody_index, "executed captured by")
        retained_by = _table_value(row, custody_index, "retained by")
        presented_by = _table_value(row, custody_index, "presented by")
        verified_by = _table_value(row, custody_index, "verified witnessed by")
        if not evidence_id:
            messages.append(f"{md_file.name} evidence custody row missing Evidence ID")
            continue
        if not RECORD_ID_PATTERN.fullmatch(evidence_id):
            messages.append(f"{md_file.name} invalid Evidence ID: {evidence_id}")
        claim_ids = [item.strip() for item in re.split(r"[,;/]", claim_id) if item.strip()]
        if not claim_ids or any(not RECORD_ID_PATTERN.fullmatch(item) for item in claim_ids):
            messages.append(
                f"{md_file.name} evidence {evidence_id} has invalid Claim ID declaration"
            )
        if decisive not in DECISIVE_VALUES:
            messages.append(
                f"{md_file.name} evidence {evidence_id} decisive value must be yes or no"
            )
        required_values = (
            ("artifact/raw result", artifact),
            ("change actor", change_actor),
            ("generated by", generated_by),
            ("selected by", selected_by),
            ("transformed/summarized by", transformed_by),
            ("executed/captured by", captured_by),
            ("retained by", retained_by),
            ("presented by", presented_by),
            ("verified/witnessed by", verified_by),
        )
        for label, value in required_values:
            if not value:
                messages.append(f"{md_file.name} evidence {evidence_id} missing {label}")
        if evidence_id in custody_ids:
            messages.append(f"{md_file.name} duplicate evidence custody ID: {evidence_id}")
        custody_ids.add(evidence_id)
        custody_controls[evidence_id] = (
            change_actor,
            generated_by,
            selected_by,
            presented_by,
            verified_by,
        )
        if decisive in {"yes", "true"}:
            decisive_ids.add(evidence_id)

    profile_ids: set[str] = set()
    for row in profile_rows:
        if len(row) != len(profile_headers):
            messages.append(
                f"{md_file.name} coupling-profile row has {len(row)} cells; expected {len(profile_headers)}"
            )
        evidence_id = _table_value(row, profile_index, "evidence id")
        if not evidence_id:
            messages.append(f"{md_file.name} coupling-profile row missing Evidence ID")
            continue
        if not RECORD_ID_PATTERN.fullmatch(evidence_id):
            messages.append(f"{md_file.name} invalid coupling-profile Evidence ID: {evidence_id}")
        if evidence_id in profile_ids:
            messages.append(f"{md_file.name} duplicate coupling profile ID: {evidence_id}")
        profile_ids.add(evidence_id)
        axis_values: dict[str, str] = {}
        for axis in COUPLING_PROFILE_AXES:
            cell = _table_value(row, profile_index, axis)
            value, basis = _parse_coupling_cell(cell)
            if value is None:
                messages.append(
                    f"{md_file.name} evidence {evidence_id} has invalid {axis} coupling; use coupled, partially separated, or separated"
                )
            elif not basis:
                messages.append(
                    f"{md_file.name} evidence {evidence_id} {axis} coupling must include a basis"
                )
            else:
                axis_values[axis] = value

        classification = _table_value(row, profile_index, "classification").lower()
        matched_class = classification if classification in EVIDENCE_CLASSIFICATIONS else None
        if matched_class is None:
            messages.append(
                f"{md_file.name} evidence {evidence_id} has invalid classification"
            )
        disposition = _table_value(
            row, profile_index, "admissibility residual risk disposition"
        ).lower()
        if not disposition:
            messages.append(
                f"{md_file.name} evidence {evidence_id} missing admissibility/residual-risk disposition"
            )
        if axis_values.get("actor") == "coupled" and matched_class not in {None, "self-check"}:
            messages.append(
                f"{md_file.name} evidence {evidence_id} has coupled actor axis and must be classified as self-check"
            )
        controls = custody_controls.get(evidence_id)
        if controls and matched_class not in {None, "self-check"}:
            change_actor, generated_by, selected_by, presented_by, verified_by = controls
            normalized_actor = change_actor.casefold().strip()
            if not verified_by or verified_by.casefold().strip() == normalized_actor:
                messages.append(
                    f"{md_file.name} evidence {evidence_id} classified as {matched_class} must declare a verifier/witness distinct from the change actor"
                )
            actor_controls_decisive_path = normalized_actor and all(
                value.casefold().strip() == normalized_actor
                for value in (generated_by, selected_by, presented_by)
            )
            if actor_controls_decisive_path:
                messages.append(
                    f"{md_file.name} evidence {evidence_id} generated, selected, and presented by the change actor must be classified as self-check"
                )
        if matched_class == "self-check" and evidence_id in decisive_ids:
            if "ship.md" not in disposition:
                messages.append(
                    f"{md_file.name} self-check evidence {evidence_id} must link its admissibility or residual-risk disposition to ship.md"
                )

    for evidence_id in sorted(custody_ids - profile_ids):
        messages.append(f"{md_file.name} evidence {evidence_id} has no matching coupling profile")
    for evidence_id in sorted(profile_ids - custody_ids):
        messages.append(f"{md_file.name} coupling profile {evidence_id} has no matching custody row")


def _check_decision_authority(md_file: Path, text: str, messages: list[str]) -> None:
    """Structurally lint an activated evidence-conditioned authority record."""

    required_sections = (
        "Decision episode",
        "Evidence basis",
        "Decision-right allocation",
        "Derived authority result",
        "Reopen and closure controls",
    )
    lowered = text.lower()
    for section in required_sections:
        if f"## {section.lower()}" not in lowered:
            messages.append(f"{md_file.name} missing required section: {section}")

    episode_section = _section_text(text, "## decision episode")
    episode_fields = {
        "decision id": ("decision id",),
        "action": ("candidate / action", "action"),
        "action identity": ("action identity",),
        "policy version": ("policy version",),
        "reversible": ("reversible",),
        "consequence if wrong": ("consequence if wrong",),
    }
    for field, labels in episode_fields.items():
        value = _first_authority_bullet_value(episode_section, labels)
        if _authority_value_is_unfilled(value):
            messages.append(f"{md_file.name} missing {field}")

    if "## decision-right allocation" not in lowered:
        return

    tables = _markdown_tables(_strip_code_blocks(text))
    evidence_table = _find_markdown_table(
        tables,
        ("evidence id", "raw state", "scope basis", "intended use v&v status", "custody profile link"),
    )
    rights_table = _find_markdown_table(
        tables,
        (
            "decision right",
            "proposed actor",
            "evidence ids",
            "policy standing gate",
            "required authority",
            "transfer trigger",
        ),
    )
    if evidence_table is None:
        messages.append(f"{md_file.name} missing the evidence-basis table or required headers")
    if rights_table is None:
        messages.append(f"{md_file.name} missing the decision-right table or required headers")
    if evidence_table is None or rights_table is None:
        return

    evidence_headers, evidence_rows = evidence_table
    rights_headers, rights_rows = rights_table
    if not evidence_rows:
        messages.append(
            f"{md_file.name} evidence-basis table must include at least one evidence row"
        )
    if not rights_rows:
        messages.append(
            f"{md_file.name} decision-right table must include at least one decision row"
        )
    evidence_index = {
        _normalize_table_label(value): index for index, value in enumerate(evidence_headers)
    }
    rights_index = {
        _normalize_table_label(value): index for index, value in enumerate(rights_headers)
    }
    evidence_states: dict[str, str] = {}
    referenced_ids: set[str] = set()
    for row in evidence_rows:
        if len(row) != len(evidence_headers):
            messages.append(
                f"{md_file.name} evidence-basis row has {len(row)} cells; expected {len(evidence_headers)}"
            )
        evidence_id = _table_value(row, evidence_index, "evidence id")
        raw_state = _table_value(row, evidence_index, "raw state").lower()
        scope = _table_value(row, evidence_index, "scope basis")
        intended_use = _table_value(row, evidence_index, "intended use v&v status")
        custody_link = _table_value(row, evidence_index, "custody profile link")
        if not RECORD_ID_PATTERN.fullmatch(evidence_id) or not evidence_id.startswith("E-"):
            messages.append(f"{md_file.name} invalid Evidence ID: {evidence_id}")
        if raw_state not in AUTHORITY_RAW_STATES:
            messages.append(
                f"{md_file.name} invalid raw state for evidence {evidence_id}: {raw_state}"
            )
        for label, value in (
            ("scope or basis", scope),
            ("intended use or V&V status", intended_use),
            ("custody or profile link", custody_link),
        ):
            if _authority_value_is_unfilled(value):
                messages.append(f"{md_file.name} evidence {evidence_id} missing {label}")
        if raw_state == "bounded_absence":
            scope_normalized = scope.lower()
            placeholder_or_negation = re.search(
                r"\b(?:unbounded|tbd|todo|replace|pending)\b|"
                r"\bnot\s+(?:a\s+)?finite\s+scope\b|"
                r"\b(?:no|without)\s+(?:finite\s+)?(?:scope|time(?:\s+boundary)?)\b",
                scope_normalized,
            )
            if (
                "finite scope" not in scope_normalized
                or "time" not in scope_normalized
                or placeholder_or_negation is not None
            ):
                messages.append(
                    f"{md_file.name} bounded_absence for evidence {evidence_id} requires finite scope and time boundary"
                )
        if evidence_id in evidence_states:
            messages.append(f"{md_file.name} duplicate evidence basis ID: {evidence_id}")
        evidence_states[evidence_id] = raw_state
        referenced_ids.add(evidence_id)

    rights_seen: set[str] = set()
    right_authorities: dict[str, str] = {}
    right_evidence: dict[str, set[str]] = {}
    for row in rights_rows:
        if len(row) != len(rights_headers):
            messages.append(
                f"{md_file.name} decision-right row has {len(row)} cells; expected {len(rights_headers)}"
            )
        right = _table_value(row, rights_index, "decision right").lower()
        proposed_actor = _table_value(row, rights_index, "proposed actor")
        declarations = _table_value(row, rights_index, "evidence ids")
        policy_basis = _table_value(row, rights_index, "policy standing gate")
        authority = _table_value(row, rights_index, "required authority").lower()
        transfer_trigger = _table_value(row, rights_index, "transfer trigger")
        if right not in DECISION_RIGHTS:
            messages.append(f"{md_file.name} invalid decision right: {right}")
        if right in rights_seen:
            messages.append(f"{md_file.name} duplicate decision right: {right}")
        rights_seen.add(right)
        if authority not in AUTHORITY_RESULTS - {"indeterminate"}:
            messages.append(
                f"{md_file.name} invalid required authority for {right}: {authority}"
            )
        for label, value in (
            ("proposed actor", proposed_actor),
            ("policy/standing gate", policy_basis),
            ("transfer trigger", transfer_trigger),
        ):
            if _authority_value_is_unfilled(value):
                messages.append(f"{md_file.name} decision right {right} missing {label}")
        row_evidence_ids = {
            item.strip()
            for item in re.split(r"[,;/]", declarations)
            if item.strip() and item.strip().lower() != "not applicable"
        }
        if not row_evidence_ids:
            messages.append(f"{md_file.name} decision right {right} missing evidence IDs")
        for evidence_id in sorted(row_evidence_ids - evidence_states.keys()):
            messages.append(
                f"{md_file.name} decision right {right} evidence {evidence_id} has no evidence-basis row"
            )
        referenced_ids.update(row_evidence_ids)
        right_evidence[right] = row_evidence_ids
        right_authorities[right] = authority

    for missing_right in sorted(DECISION_RIGHTS - rights_seen):
        messages.append(f"{md_file.name} missing decision right: {missing_right}")

    verification = md_file.parent / "verification.md"
    verification_text = verification.read_text(encoding="utf-8") if verification.exists() else ""
    verification_tables = _markdown_tables(_strip_code_blocks(verification_text))
    custody_table = _find_markdown_table(
        verification_tables,
        ("evidence id", "decisive"),
    )
    verification_ids: set[str] = set()
    decisive_by_id: dict[str, bool] = {}
    if custody_table is not None:
        custody_headers, custody_rows = custody_table
        custody_index = {
            _normalize_table_label(value): index for index, value in enumerate(custody_headers)
        }
        for row in custody_rows:
            evidence_id = _table_value(row, custody_index, "evidence id")
            decisive = _table_value(row, custody_index, "decisive").lower()
            if evidence_id in verification_ids:
                messages.append(
                    f"verification.md duplicate custody declaration for evidence {evidence_id}"
                )
            verification_ids.add(evidence_id)
            decisive_by_id[evidence_id] = decisive == "yes"
    for evidence_id in sorted(referenced_ids - verification_ids):
        messages.append(
            f"{md_file.name} evidence {evidence_id} is not declared in verification custody"
        )
    for right, evidence_ids in sorted(right_evidence.items()):
        for evidence_id in sorted(evidence_ids & verification_ids):
            if not decisive_by_id.get(evidence_id, False):
                messages.append(
                    f"{md_file.name} decision right {right} evidence {evidence_id} is not marked decisive in verification custody"
                )

    profile_table = _find_markdown_table(
        verification_tables,
        ("evidence id", "classification"),
    )
    classifications: dict[str, str] = {}
    if profile_table is not None:
        profile_headers, profile_rows = profile_table
        profile_index = {
            _normalize_table_label(value): index for index, value in enumerate(profile_headers)
        }
        classifications = {
            _table_value(row, profile_index, "evidence id"): _table_value(
                row, profile_index, "classification"
            ).lower()
            for row in profile_rows
        }
    derived_result = ""
    derived_section = _section_text(text, "## derived authority result")
    if not derived_section:
        messages.append(f"{md_file.name} missing required section: Derived authority result")
    else:
        for label in (
            "decision right evaluated",
            "basis",
            "derived by",
            "recorded at",
        ):
            value = _authority_bullet_value(derived_section, label)
            if _authority_value_is_unfilled(value):
                messages.append(f"{md_file.name} missing {label}")
        result_match = re.search(
            r"(?im)^-\s*(?:\*\*Result:\*\*|Result:)\s*`?([a-z_]+)`?\s*$",
            derived_section,
        )
        if result_match is None:
            messages.append(f"{md_file.name} missing derived authority Result")
        else:
            derived_result = result_match.group(1).lower()
            if derived_result not in AUTHORITY_RESULTS:
                messages.append(
                    f"{md_file.name} invalid derived authority result: {derived_result}"
                )
            apply_authority = right_authorities.get("apply")
            non_clearing_overrides = {
                "blocked_pending_evidence",
                "prohibited_for_agent",
                "indeterminate",
            }
            if apply_authority == "agent_authorized":
                non_clearing_overrides |= {
                    "human_required",
                    "separate_control_required",
                    "dual_authority_required",
                }
            if (
                apply_authority in AUTHORITY_RESULTS
                and derived_result != apply_authority
                and derived_result not in non_clearing_overrides
            ):
                messages.append(
                    f"{md_file.name} derived result {derived_result} is incompatible with apply allocation {apply_authority}"
                )

    if derived_result == "agent_authorized":
        for evidence_id in sorted(right_evidence.get("apply", set())):
            raw_state = evidence_states.get(evidence_id)
            if raw_state in {"unknown", "disputed"}:
                messages.append(
                    f"{md_file.name} {raw_state} evidence {evidence_id} cannot clear agent_authorized"
                )
            if classifications.get(evidence_id) == "self-check":
                messages.append(
                    f"{md_file.name} self-check evidence {evidence_id} cannot clear agent_authorized"
                )

    reopen_section = _section_text(text, "## reopen and closure controls")
    for label in (
        "reopen authority",
        "reopen trigger",
        "superseded decision handling",
        "close authority",
        "closure evidence",
        "interim expiry",
    ):
        value = _authority_bullet_value(reopen_section, label)
        if _authority_value_is_unfilled(value):
            messages.append(f"{md_file.name} missing {label}")
    closure_evidence = _authority_bullet_value(reopen_section, "closure evidence")
    closure_ids = set(re.findall(r"\bE-[0-9][A-Za-z0-9._-]*\b", closure_evidence))
    if not _authority_value_is_unfilled(closure_evidence) and not closure_ids:
        messages.append(f"{md_file.name} closure evidence must name an Evidence ID")
    for evidence_id in sorted(closure_ids - evidence_states.keys()):
        messages.append(
            f"{md_file.name} closure evidence {evidence_id} has no evidence-basis row"
        )


def _first_authority_bullet_value(section: str, labels: tuple[str, ...]) -> str:
    for label in labels:
        value = _authority_bullet_value(section, label)
        if value:
            return value
    return ""


def _authority_bullet_value(section: str, label: str) -> str:
    escaped = re.escape(label)
    match = re.search(
        rf"(?im)^-\s*(?:\*\*{escaped}:\*\*|{escaped}:)\s*(.*?)\s*$",
        section,
    )
    return match.group(1).strip() if match else ""


def _authority_value_is_unfilled(value: str) -> bool:
    normalized = re.sub(r"[`*_]", "", value).strip().lower()
    if not normalized:
        return True
    if normalized in {"unknown", "pending", "none", "not applicable", "n/a"}:
        return True
    return bool(re.search(r"\b(?:replace|tbd|todo)\b", normalized))


def _markdown_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    """Parse simple pipe-delimited Markdown tables used by packet templates."""

    lines = text.splitlines()
    tables: list[tuple[list[str], list[list[str]]]] = []
    index = 0
    while index + 1 < len(lines):
        header_line = lines[index].strip()
        separator_line = lines[index + 1].strip()
        if not header_line.startswith("|") or not _is_table_separator(separator_line):
            index += 1
            continue
        headers = _table_cells(header_line)
        rows: list[list[str]] = []
        index += 2
        while index < len(lines) and lines[index].strip().startswith("|"):
            cells = _table_cells(lines[index].strip())
            rows.append(cells)
            index += 1
        tables.append((headers, rows))
    return tables


def _table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_table_separator(line: str) -> bool:
    if not line.startswith("|"):
        return False
    cells = _table_cells(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def _normalize_table_label(value: str) -> str:
    plain = re.sub(r"[`*_?]", "", value.lower())
    plain = re.sub(r"[/–—-]+", " ", plain)
    return re.sub(r"\s+", " ", plain).strip()


def _find_markdown_table(
    tables: list[tuple[list[str], list[list[str]]]],
    required: tuple[str, ...],
) -> tuple[list[str], list[list[str]]] | None:
    for headers, rows in tables:
        normalized = {_normalize_table_label(header) for header in headers}
        if all(label in normalized for label in required):
            return headers, rows
    return None


def _table_value(row: list[str], index: dict[str, int], label: str) -> str:
    position = index.get(label)
    if position is None or position >= len(row):
        return ""
    return re.sub(r"[*`]", "", row[position]).strip()


def _parse_coupling_cell(cell: str) -> tuple[str | None, str]:
    plain = re.sub(r"[*`]", "", cell).strip().lower()
    if "/" in plain:
        return None, ""
    match = re.fullmatch(
        r"(partially separated|separated|coupled)\s*[:;,\-–—]\s*(\S.*)",
        plain,
    )
    if not match:
        return None, ""
    return match.group(1), match.group(2).strip()


def _section_text(text: str, heading_lower: str) -> str:
    """Return the body of a `## Heading` section (case-insensitive) up to the next H2 or end."""

    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower() == heading_lower:
            start = i
            break
    if start is None:
        return ""
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return "".join(lines[start:end])


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


def check_internal_links(repo: Path, files: list[str]) -> list[str]:
    """Check that internal markdown links in `files` resolve from each file's directory.

    External URLs (http(s)://, mailto:) and pure anchors (#section) are ignored.
    Returns a list of failure messages, one per broken link.
    """

    failures: list[str] = []
    for relative_name in files:
        md_file = repo / relative_name
        if not md_file.exists():
            continue
        text = md_file.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_PATTERN.finditer(text):
            target = match.group(1).strip()
            if _is_external_or_anchor(target):
                continue
            target_path = target.strip("<>").split("#", 1)[0]
            if not target_path:
                continue
            if not (md_file.parent / target_path).exists():
                failures.append(f"{relative_name} has broken relative link: {target}")
    return failures


def _is_external_or_anchor(target: str) -> bool:
    lowered = target.lower()
    return (
        lowered.startswith(("http://", "https://", "mailto:"))
        or lowered.startswith("#")
    )


def _check_prohibited_claims(md_file: Path, text: str, messages: list[str]) -> None:
    """Detect literal compliance claims and paraphrases.

    Two passes:
    1. Fixed-phrase scan for stable phrases (e.g. "formal V&V", "NQA-1 record").
    2. Paraphrase regex pass: a compliance entity adjacent to a positive-claim
       verb stem (compliant, qualified, satisfies, conforms to, ...). A
       paragraph-aware negation gate suppresses "inspired by", "does not claim",
       and similar boundary prose. Fenced code blocks are skipped because they
       are commonly used to quote example phrases.
    """

    scannable = _strip_code_blocks(text)
    lowered = scannable.lower()

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

    for pattern in PARAPHRASE_PATTERNS:
        for match in pattern.finditer(scannable):
            m_start = match.start()
            context_before = lowered[max(0, m_start - 60) : m_start]
            if _is_boundary_context(context_before):
                continue
            if _has_paragraph_disclaimer(scannable, m_start):
                continue
            snippet = match.group(0).strip()
            messages.append(
                f"{md_file.name} contains prohibited compliance claim (paraphrase): {snippet}"
            )


def _strip_code_blocks(text: str) -> str:
    """Replace fenced code block contents with whitespace of equal length so
    indices remain stable but the scanner does not flag quoted examples.
    """

    pattern = re.compile(r"(?ms)^```.*?$.*?^```\s*$")

    def _blank(match: re.Match[str]) -> str:
        return re.sub(r"\S", " ", match.group(0))

    return pattern.sub(_blank, text)


def _has_paragraph_disclaimer(text: str, index: int) -> bool:
    """Walk back to the start of the current paragraph or section and check for
    a disclaimer marker that scopes the claim as not-implied.
    """

    section_start = max(
        text.rfind("\n\n", 0, index),
        text.rfind("\n## ", 0, index),
        text.rfind("\n### ", 0, index),
    )
    paragraph = text[max(0, section_start) : index].lower()
    markers = (
        "out of scope",
        "non-goals",
        "non-goal",
        "anti-goal",
        "unacceptable outcome",
        "what we don't",
        "what we do not",
        "we do not claim",
        "we don't claim",
        "no claim",
        "is implying",
        "would imply",
        "wording that implies",
        "anything that implies",
        "any claim that",
        "any wording that",
        "must not imply",
        "do not imply",
        "does not imply",
        "stop or escalate",
        "escalation triggers",
        "avoids compliance",
        "avoid compliance",
        "out-of-bounds",
        "is not a compliance",
        "not a compliance",
        "is not nrc",
        "inspired by",
        "influenced by",
        "no formal",
    )
    return any(marker in paragraph for marker in markers)


def _is_boundary_context(context: str) -> bool:
    compact = re.sub(r"\s+", " ", context).strip().lower()
    return any(compact.endswith(prefix.strip()) or prefix in compact[-40:] for prefix in BOUNDARY_PREFIXES)


def _contains_status(text: str) -> bool:
    lowered = text.lower()
    return any(re.search(rf"\b{re.escape(status)}\b", lowered) for status in EVIDENCE_STATUSES)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a Nuclear-grade change packet.")
    parser.add_argument("packet", type=Path, help="Path to .nuclear/changes/<slug>/")
    parser.add_argument(
        "--strict-custody",
        action="store_true",
        help="Require a complete evidence-custody and five-axis coupling disclosure for Standard packets.",
    )
    parser.add_argument(
        "--strict-authority",
        action="store_true",
        help="Require and validate an evidence-conditioned decision-authority record for Standard packets.",
    )
    args = parser.parse_args(argv)

    result = validate_packet(
        args.packet,
        require_custody=args.strict_custody,
        require_authority=args.strict_authority,
    )
    if result.ok:
        print(f"OK: {args.packet}")
        return 0

    print(f"FAILED: {args.packet}")
    for message in result.messages:
        print(f"- {message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
