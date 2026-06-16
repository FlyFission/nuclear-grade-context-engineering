# CLI Reference

**Purpose:** Document the `tools/ng.py` helper, which needs no extra dependencies.

## Commands

```bash
python tools/ng.py init [repo] [--dry-run] [--yes]
python tools/ng.py new <slug> --mode quick|standard [--repo .] [--force]
python tools/ng.py validate <packet>
python tools/ng.py doctor [repo]
python tools/ng.py list
python tools/ng.py status [repo]
python tools/ng.py eval [repo]
python tools/ng.py decisions [repo] [--all]
```

## Behavior

- `init` creates `.nuclear/README.md` and `.nuclear/changes/`.
- `new` copies Quick or Standard templates from the target repo when they are there. If not, it copies them from this Nuclear-grade checkout.
- `validate` hands off to `tools/ng_validate.py`.
- `doctor` checks a Nuclear-grade distribution repo for public files, contracts, and templates. In a target repo that has been set up, it checks `.nuclear/README.md` and `.nuclear/changes/`.
- `list` shows what is available: modes, skills, commands, packet files, CM files (records for keeping the approved version under control), golden-path files, and optional templates. That includes turnover, self-check, and supplier-trust records.
- `status` lists active packets, the mode it detects for each, and a health tag: `ok` (it validates), `closed` (deliberately retired with a written reason, carrying a `NUCLEAR-GRADE-CLOSED:` marker line), `scaffold` (an untouched draft that still has the placeholder marker), or `invalid` (fails validation for some other reason). `ok` and `closed` are finished states; only `scaffold` and `invalid` count toward the "needs attention" reminder, so abandoned half-filled drafts stay visible while honestly closed packets are left alone. See the `closing-stale-packets` skill.
- `eval` scores the worked-example artifacts in `evals/cases/` for the decision signals they claim to teach, and exits non-zero if any worked example dropped a required signal. It checks that the named decision elements are present, not that the work is engineering-correct, safe, or compliant. See `docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md`.
- `decisions` is the **operator receipt**: it rolls up every skill's `## Decision contract` and prints the `block` and `warn` signals (the one decision each skill can move and its tier), keeping `observe`-tier skills in telemetry so the receipt does not become audit-the-audit. `--all` also lists the telemetry rows. It is the generated, single-source view a reviewer scans instead of reading 27 skills; the per-skill receipt stays the source of truth. See `docs/05-reference/skill-authoring-contract.md`.

## Boundary note

The command-line tool checks structure and whether evidence is visible. It does not decide engineering adequacy, safety, security, compliance, regulatory adequacy, or formal verification.

## Source-lineage note

This reference documents the local tooling for an original workflow built from public sources. It does not create formal assurance.
