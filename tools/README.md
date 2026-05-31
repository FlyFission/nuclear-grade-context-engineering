# Tools

This folder holds the small, local tools for working with Nuclear-grade change records.

## `nuclear-grade.yaml`

`nuclear-grade.yaml` is a plain, readable list of what the project ships. The `ng doctor` command checks that this file is present. Keep it in step with the `skills/`, `commands/`, and `templates/` folders so the list never quietly falls out of date.

## `ng.py`

The main helper:

```bash
python tools/ng.py init [repo] [--dry-run] [--yes]
python tools/ng.py new <slug> --mode quick|standard [--repo .] [--force]
python tools/ng.py validate <packet>
python tools/ng.py doctor [repo]
python tools/ng.py list
python tools/ng.py status [repo]
```

`ng.py` needs no extra packages. It hands the actual checking of a change record to `ng_validate.py`. The `doctor` command also checks the heavier change templates and the "golden path" templates used by the questioning-attitude workflow.

The installable version of this tool lives in `nuclear_grade/`. `tools/ng.py` is the in-repo copy that the docs point to.

## `ng_validate.py`

Checks small (Quick) and standard change records for:

- the files each mode requires;
- the required sections;
- evidence status labels;
- a rollback plan, what to monitor, and a clear release decision;
- a note on where the ideas come from;
- broken local Markdown links;
- a few wording patterns that would over-claim compliance.

Run it:

```bash
python tools/ng_validate.py .nuclear/changes/<slug>/
```

Example:

```bash
python tools/ng_validate.py docs/03-worked-examples/ai-agent-tool-permissions/.nuclear/changes/add-agent-tool-permissions
```

The checker tells you whether the evidence is present and well-structured. It does not decide safety, security, adequacy, or compliance.

## A note on limits

These tools check structure and whether evidence is visible. They do not create formal V&V, compliance, certification, or any safety, security, regulatory, or production guarantee.
