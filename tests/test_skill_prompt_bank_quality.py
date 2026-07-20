import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from tests.test_skill_contracts import EXPECTED_SKILLS

ROOT = Path(__file__).resolve().parents[1]
PROMPT_BANK = ROOT / "docs" / "05-reference" / "skill-evaluation.md"

SKILL_HEADING_RE = re.compile(r"^### `(?P<skill>[a-z0-9-]+)`$", re.MULTILINE)
PROMPT_RE = re.compile(
    r"^- Should (?P<kind>trigger|not trigger): (?P<prompt>.+)$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class PromptCase:
    skill: str
    should_trigger: bool
    prompt: str


def load_prompt_cases() -> list[PromptCase]:
    text = PROMPT_BANK.read_text(encoding="utf-8")
    headings = list(SKILL_HEADING_RE.finditer(text))
    cases: list[PromptCase] = []

    for index, heading in enumerate(headings):
        skill = heading.group("skill")
        start = heading.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[start:end]

        for match in PROMPT_RE.finditer(block):
            cases.append(
                PromptCase(
                    skill=skill,
                    should_trigger=match.group("kind") == "trigger",
                    prompt=match.group("prompt").strip(),
                )
            )

    return cases


def test_prompt_bank_parses_to_expected_skill_cases():
    cases = load_prompt_cases()
    by_skill: dict[str, list[PromptCase]] = defaultdict(list)
    for case in cases:
        by_skill[case.skill].append(case)

    assert set(by_skill) == EXPECTED_SKILLS

    for skill in EXPECTED_SKILLS:
        positives = [case for case in by_skill[skill] if case.should_trigger]
        negatives = [case for case in by_skill[skill] if not case.should_trigger]

        assert len(positives) >= 3, f"{skill} needs at least 3 should-trigger prompts"
        assert len(negatives) >= 2, f"{skill} needs at least 2 should-not-trigger prompts"


def test_prompt_bank_has_no_exact_duplicate_prompts_with_conflicting_labels():
    labels_by_prompt: dict[str, set[bool]] = defaultdict(set)
    for case in load_prompt_cases():
        labels_by_prompt[case.prompt.lower()].add(case.should_trigger)

    conflicts = {
        prompt: labels for prompt, labels in labels_by_prompt.items() if labels == {True, False}
    }

    assert not conflicts, f"prompt(s) have conflicting trigger labels: {sorted(conflicts)}"


def test_prompt_bank_prompts_do_not_name_their_target_skill():
    violations = []

    for case in load_prompt_cases():
        normalized_prompt = case.prompt.lower()
        skill_words = case.skill.replace("-", " ")
        if case.skill in normalized_prompt or skill_words in normalized_prompt:
            violations.append((case.skill, case.prompt))

    assert not violations, (
        "prompt bank contains tautological prompts that name their own target skill: "
        + repr(violations)
    )


def test_positive_prompts_are_not_all_generic_workflow_requests():
    generic_terms = (
        "use nuclear-grade",
        "walk this",
        "review this",
        "prepare",
        "create",
        "update this",
    )

    by_skill: dict[str, list[PromptCase]] = defaultdict(list)
    for case in load_prompt_cases():
        by_skill[case.skill].append(case)

    weak = []
    for skill, cases in by_skill.items():
        positives = [case.prompt.lower() for case in cases if case.should_trigger]
        non_generic = [
            prompt for prompt in positives if not any(prompt.startswith(term) for term in generic_terms)
        ]
        if not non_generic:
            weak.append(skill)

    assert not weak, f"skills lack a non-generic should-trigger prompt: {weak}"
