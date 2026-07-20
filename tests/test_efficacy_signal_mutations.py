from pathlib import Path

import pytest

from nuclear_grade import efficacy

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "evals" / "cases"


def _remove_phrase_case_insensitive(text: str, phrase: str) -> str:
    lowered = text.lower()
    needle = phrase.lower()
    out = []
    cursor = 0
    while True:
        index = lowered.find(needle, cursor)
        if index == -1:
            out.append(text[cursor:])
            return "".join(out)
        out.append(text[cursor:index])
        cursor = index + len(phrase)


@pytest.mark.parametrize("case", efficacy.load_cases(CASES_DIR), ids=lambda case: case.id)
def test_every_all_of_phrase_is_required(case):
    """Dropping one conjunctive phrase must break that signal.

    This prevents a signal from scoring as present when only nearby generic prose remains.
    """

    artifact = ROOT / case.artifact
    section = efficacy.extract_section(artifact.read_text(encoding="utf-8"), case.section)
    assert section is not None

    for signal in case.signals:
        for phrase in signal.all_of:
            assert phrase.lower() in section.lower(), (
                f"{case.id} signal {signal.name!r} all_of phrase not present: {phrase!r}"
            )

            mutated = _remove_phrase_case_insensitive(section, phrase)

            assert not signal.present_in(mutated), (
                f"{case.id} signal {signal.name!r} still passes after removing {phrase!r}"
            )


@pytest.mark.parametrize("case", efficacy.load_cases(CASES_DIR), ids=lambda case: case.id)
def test_any_of_signal_fails_when_all_alternatives_are_removed(case):
    """Removing every accepted alternative must break an alternative signal."""

    artifact = ROOT / case.artifact
    section = efficacy.extract_section(artifact.read_text(encoding="utf-8"), case.section)
    assert section is not None

    for signal in case.signals:
        if not signal.any_of:
            continue

        present_alternatives = [
            phrase for phrase in signal.any_of if phrase.lower() in section.lower()
        ]
        assert present_alternatives, (
            f"{case.id} signal {signal.name!r} has no any_of alternatives present"
        )

        mutated = section
        for phrase in signal.any_of:
            mutated = _remove_phrase_case_insensitive(mutated, phrase)

        assert not signal.present_in(mutated), (
            f"{case.id} signal {signal.name!r} still passes after removing all any_of alternatives"
        )
