# Standard Verification Record

**Purpose:** Record the evidence that the changes hold and that nothing regressed.

**Activation threshold:** Standard mode: charter, public doctrine, a skill, a command, and a template change.

**Minimum useful version:** An evidence table with commands, status, and named gaps.

---

## Evidence

| Evidence area | Status | Command / method | Notes |
|---|---|---|---|
| Full test suite | pass | `python -m pytest -q` | On the reconciled tree (PR #43 on `main`): 181 passed with PyYAML installed (CI installs it); 180 passed + 1 skipped without PyYAML — `test_scaffold_ci_emits_parseable_yaml` skips via `pytest.importorskip("yaml")`. `test_command_parity.py` confirms the edited skill `## Prompt` and the regenerated `ng-learn` card match the golden fixture byte-for-byte |
| Token budget | pass | `python tools/ng.py tokens .` | `OK: token budget`; the new doc and additions stay within budget |
| Repo health | pass | `python tools/ng.py doctor .` | `OK: Nuclear-grade doctor` |
| Packet validation | pass | `python tools/ng.py validate .nuclear/changes/glean-nuclear-leadership` | required files present; no placeholders; links resolve; statuses present |
| Boundary wording | pass | manual read of new and edited docs | no prohibited compliance phrase; each new/edited public doc keeps a source-lineage note and "No compliance claim is made" |
| Cross-link resolution | pass | manual link check | durable-memory ↔ context-window-discipline, authority-and-intent, and leadership-doc links resolve |
| Source mapping | pass | manual check against `source-map.md` | every concept maps to a Tier 1/3/8/9 source already in the map; no IAEA/WANO/INSAG citation added |

## Gaps and limits

| Gap / limit | Impact | Disposition | Owner | Recheck trigger |
|---|---|---|---|---|
| Doctrine quality is partly review-based | Tests prove structure, not that the wording is the best translation | mitigate | FlyFission | PR review or future OPEX |
| Independent review pending | Local checks pass; a second reviewer has not yet read the doctrine | planned | FlyFission | PR review |

## Required links

- `risk.md`
- `trace.md`
- `ship.md`

## Exit criteria

- Each evidence area has a status and a command or method.
- Gaps are named with a disposition, an owner, and a recheck trigger.

## Source-lineage note

Original Nuclear-grade verification record inspired by public software-assurance and verification sources mapped in `docs/00-standards-foundation/source-map.md` and `docs/01-field-guide/source-to-concept-crosswalk.md`. No compliance claim is made.
