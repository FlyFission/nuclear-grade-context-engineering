"""Release-identity consistency check.

One version must mean one thing everywhere it is declared: `pyproject.toml`, the
plugin manifests (including the `nuclear-grade-guard` plugin), `CITATION.cff`, a
dated `CHANGELOG.md` section, and (at release time) the git tag. CI runs this
without `--tag` so drift is caught on every PR; the release workflow runs it with
`--tag` so a tag that disagrees with the files it ships never publishes.

    python -m nuclear_grade.release [--repo .] [--tag v0.6.0]

It checks that the declarations agree. It does not decide whether a release is
ready; that is the ship-readiness record's job.
"""

from __future__ import annotations

import argparse
import json
import re
import tomllib
from pathlib import Path

MANIFESTS = (
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "plugins/nuclear-grade-guard/.claude-plugin/plugin.json",
)
_CHANGELOG_SECTION = r"^## \[{version}\] - (\d{{4}}-\d{{2}}-\d{{2}})\s*$"


def _citation_field(text: str, field: str) -> str | None:
    match = re.search(rf'^{field}:\s*"?([^"\n]+)"?\s*$', text, re.MULTILINE)
    return match.group(1).strip() if match else None


def check_release(repo: Path, tag: str | None = None) -> list[str]:
    problems: list[str] = []
    version = tomllib.loads((repo / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]

    for manifest in MANIFESTS:
        path = repo / manifest
        if not path.is_file():
            problems.append(f"missing manifest: {manifest}")
            continue
        declared = json.loads(path.read_text(encoding="utf-8")).get("version")
        if declared != version:
            problems.append(f"{manifest} version {declared!r} != pyproject {version!r}")

    citation = (repo / "CITATION.cff").read_text(encoding="utf-8")
    if _citation_field(citation, "version") != version:
        problems.append(f"CITATION.cff version {_citation_field(citation, 'version')!r} != pyproject {version!r}")

    changelog = (repo / "CHANGELOG.md").read_text(encoding="utf-8")
    section = re.search(_CHANGELOG_SECTION.format(version=re.escape(version)), changelog, re.MULTILINE)
    if section is None:
        problems.append(f"CHANGELOG.md has no dated `## [{version}] - YYYY-MM-DD` section")
    elif _citation_field(citation, "date-released") != section.group(1):
        problems.append(
            f"CITATION.cff date-released {_citation_field(citation, 'date-released')!r} "
            f"!= CHANGELOG {version} date {section.group(1)!r}"
        )

    if tag is not None and tag != f"v{version}":
        problems.append(f"tag {tag!r} != expected 'v{version}'")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--tag", default=None, help="Release tag to check, e.g. v0.6.0.")
    args = parser.parse_args(argv)
    problems = check_release(args.repo, args.tag)
    if problems:
        print("FAILED: release identity")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("OK: release identity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
