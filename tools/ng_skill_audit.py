#!/usr/bin/env python3
"""Deterministic skill-readiness audit for Nuclear-grade skills.

This is deliberately static. It does not claim skills outperform a prompt-only
baseline; it checks whether each skill is structurally ready for live A/B tests
and whether the repo has the prompt-bank scaffolding needed to test it fairly.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

REQUIRED_SECTIONS = (
    "## Overview",
    "## Decision contract",
    "## When to Use",
    "## When Not to Use",
    "## Inputs",
    "## Process",
    "## Outputs",
    "## Verification",
    "## Escalation",
    "## Common Rationalizations",
    "## Red Flags",
    "## Source-lineage note",
)

DECISION_LABELS = (
    "Claim checked:",
    "Artifact observed:",
    "Decision affected:",
    "Failure class:",
    "Next action:",
)

DECISION_TIER_RE = re.compile(r"Decision affected:\*{0,2}\s*(block|warn|observe)\b", re.IGNORECASE)
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
HEADING_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)


@dataclass(frozen=True)
class SkillAudit:
    name: str
    path: str
    score: int
    verdict: str
    line_count: int
    estimated_tokens: int
    description_chars: int
    trigger_prompts: int
    negative_prompts: int
    issues: tuple[str, ...]
    warnings: tuple[str, ...]
    strengths: tuple[str, ...]


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')
    return fields


def estimate_tokens(text: str) -> int:
    # Conservative-enough markdown token estimate for relative budgeting.
    return max(1, round(len(text) / 4))


def section_body(text: str, heading: str) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    following = text[start + len(heading) :]
    match = re.search(r"\n##\s+", following)
    if match:
        return following[: match.start()]
    return following


def count_prompt_bank(skill_name: str, prompt_bank: str) -> tuple[int, int]:
    heading = f"### `{skill_name}`"
    if heading not in prompt_bank:
        return 0, 0
    block = prompt_bank.split(heading, 1)[1].split("\n### `", 1)[0]
    return block.count("Should trigger:"), block.count("Should not trigger:")


def audit_skill(path: Path, root: Path, prompt_bank: str) -> SkillAudit:
    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    name = frontmatter.get("name", path.parent.name)
    issues: list[str] = []
    warnings: list[str] = []
    strengths: list[str] = []
    score = 100

    if not frontmatter:
        issues.append("missing YAML frontmatter")
        score -= 20
    if frontmatter.get("name") != path.parent.name:
        issues.append("frontmatter name does not match folder name")
        score -= 12
    description = frontmatter.get("description", "")
    if not (80 <= len(description) <= 500):
        issues.append("description outside 80-500 character contract")
        score -= 8
    if not any(marker in description.lower() for marker in ("do not use", "not for", "skip when", "avoid when")):
        issues.append("description lacks explicit negative trigger clause")
        score -= 8
    if ": " in description:
        issues.append("description contains colon-space, unsafe in single-line YAML scalar")
        score -= 5

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]
    if missing_sections:
        issues.append("missing required sections: " + ", ".join(missing_sections))
        score -= min(30, 3 * len(missing_sections))
    else:
        strengths.append("all required skill-contract sections present")

    missing_labels = [label for label in DECISION_LABELS if label not in text]
    if missing_labels:
        issues.append("decision contract missing labels: " + ", ".join(missing_labels))
        score -= min(20, 4 * len(missing_labels))
    elif DECISION_TIER_RE.search(text):
        strengths.append("machine-checkable decision contract present")
    else:
        issues.append("decision contract lacks block/warn/observe tier")
        score -= 10

    line_count = len(text.splitlines())
    estimated = estimate_tokens(text)
    if line_count > 500:
        issues.append(f"skill exceeds 500-line contract ({line_count} lines)")
        score -= 20
    elif line_count > 350:
        warnings.append(f"large skill: {line_count} lines; consider moving detail into references/")
        score -= 3
    if estimated > 2500:
        warnings.append(f"high token cost estimate: {estimated} tokens")
        score -= 3

    verification = section_body(text, "## Verification")
    if len(re.findall(r"^[-*] ", verification, flags=re.MULTILINE)) < 3:
        warnings.append("verification section has fewer than three checklist bullets")
        score -= 4
    else:
        strengths.append("verification section is checklist-like")

    rationalizations = section_body(text, "## Common Rationalizations")
    red_flags = section_body(text, "## Red Flags")
    if len(re.findall(r"^[-*] ", rationalizations, flags=re.MULTILINE)) < 2:
        warnings.append("common rationalizations section may be too thin for hard-case eval generation")
        score -= 4
    if len(re.findall(r"^[-*] ", red_flags, flags=re.MULTILINE)) < 2:
        warnings.append("red flags section may be too thin for hard-case eval generation")
        score -= 4

    trigger_prompts, negative_prompts = count_prompt_bank(name, prompt_bank)
    if trigger_prompts < 3 or negative_prompts < 2:
        issues.append(
            f"prompt bank coverage too low: {trigger_prompts} trigger, {negative_prompts} negative prompts"
        )
        score -= 12
    elif trigger_prompts >= 4:
        strengths.append("prompt bank includes extra trigger prompts beyond the minimum")

    headings = [heading.strip() for heading in HEADING_RE.findall(text)]
    if len(headings) != len(set(headings)):
        warnings.append("duplicate second-level headings found")
        score -= 2

    score = max(0, min(100, score))
    if issues:
        verdict = "fix-before-live-ab"
    elif score >= 92:
        verdict = "ready-for-independent-live-ab"
    elif score >= 80:
        verdict = "usable-needs-tightening"
    elif score >= 65:
        verdict = "weak-needs-rewrite-before-ab"
    else:
        verdict = "poor-prioritize-rewrite-or-prune"

    return SkillAudit(
        name=name,
        path=str(path.relative_to(root)),
        score=score,
        verdict=verdict,
        line_count=line_count,
        estimated_tokens=estimated,
        description_chars=len(description),
        trigger_prompts=trigger_prompts,
        negative_prompts=negative_prompts,
        issues=tuple(issues),
        warnings=tuple(warnings),
        strengths=tuple(strengths),
    )


def write_jsonl(path: Path, audits: list[SkillAudit]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for audit in audits:
            handle.write(json.dumps(asdict(audit), sort_keys=True) + "\n")


def write_markdown(path: Path, audits: list[SkillAudit]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    total = len(audits)
    average = sum(audit.score for audit in audits) / total if total else 0
    verdict_counts: dict[str, int] = {}
    for audit in audits:
        verdict_counts[audit.verdict] = verdict_counts.get(audit.verdict, 0) + 1

    lines = [
        "# Nuclear-grade Skill Static Audit",
        "",
        "This deterministic audit checks whether each `skills/*/SKILL.md` file is structurally ready for independent prompt-only vs skill-loaded A/B testing. It is a structural completeness gate, not proof of efficacy or measured lift. A 100 here can still tie or lose against prompt-only in live runs.",
        "",
        "## Summary",
        "",
        f"- Skills audited: {total}",
        f"- Average structural completeness score: {average:.1f}/100",
        f"- Minimum structural completeness score: {min((audit.score for audit in audits), default=0)}",
        f"- Maximum structural completeness score: {max((audit.score for audit in audits), default=0)}",
        "- Verdicts:",
    ]
    for verdict, count in sorted(verdict_counts.items()):
        lines.append(f"  - `{verdict}`: {count}")

    lines.extend(
        [
            "",
            "## Skill table",
            "",
            "| Skill | Score | Verdict | Lines | Est. tokens | Eval prompts | Issues / warnings |",
            "|---|---:|---|---:|---:|---:|---|",
        ]
    )
    for audit in sorted(audits, key=lambda item: (item.score, item.name)):
        notes = "; ".join(audit.issues + audit.warnings) or "—"
        lines.append(
            f"| `{audit.name}` | {audit.score} | `{audit.verdict}` | {audit.line_count} | "
            f"{audit.estimated_tokens} | {audit.trigger_prompts}+/{audit.negative_prompts}- | {notes} |"
        )

    lines.extend(["", "## Recommended use", ""])
    lines.extend(
        [
            "1. Treat `fix-before-live-ab` as a hard stop for live benchmark budget.",
            "2. Treat `ready-for-independent-live-ab` only as eligibility for measurement; prioritize live A/B on PR-pilot ties/losses, overlap pairs, and thin-margin wins.",
            "3. Keep this audit in CI as a cheap guard, but never cite the score as measured skill lift.",
            "4. Pair this report with live route/output manifests and raw transcripts before claiming a skill improves over prompt-only.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--jsonl", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    prompt_bank_path = root / "docs" / "05-reference" / "skill-evaluation.md"
    prompt_bank = prompt_bank_path.read_text(encoding="utf-8") if prompt_bank_path.exists() else ""
    audits = [audit_skill(path, root, prompt_bank) for path in sorted((root / "skills").glob("*/SKILL.md"))]
    write_jsonl(args.jsonl, audits)
    write_markdown(args.markdown, audits)
    print(f"Audited {len(audits)} skills")
    print(f"Wrote {args.jsonl}")
    print(f"Wrote {args.markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
