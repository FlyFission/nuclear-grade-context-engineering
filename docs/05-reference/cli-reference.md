# CLI Reference

**Purpose:** Document the `tools/ng.py` helper, which needs no extra dependencies.

## Commands

```bash
python tools/ng.py init [repo] [--dry-run] [--yes]
python tools/ng.py new <slug> --mode quick|standard [--repo .] [--force]
python tools/ng.py validate <packet> [--strict-custody] [--strict-authority] [--json]
python tools/ng.py doctor [repo]
python tools/ng.py list
python tools/ng.py status [repo]
python tools/ng.py eval [repo]
python tools/ng.py decisions [repo] [--all]
python tools/ng.py badge [repo] [--out .nuclear/badge.json]
python tools/ng.py required-mode [--base REF] [--head REF] [--policy-ref base|head|WORKTREE|REF] [--approvals-json FILE] [--pr-author LOGIN] [--json] [--advisory] [--print-table]
python -m nuclear_grade.release [--repo .] [--tag vX.Y.Z]
```

## Behavior

- `init` creates `.nuclear/README.md` and `.nuclear/changes/`.
- `new` copies Quick or Standard templates from the target repo when they are there. If not, it copies them from this Nuclear-grade checkout.
- `validate` hands off to `tools/ng_validate.py`. For a Standard packet, `--strict-custody` requires evidence IDs, claim IDs, decisive status, raw-artifact references, all custody roles, matching actor/context/mechanism/authority/resource profiles with a basis, a classification, and an admissibility or residual-risk disposition. For a Standard packet, `--strict-authority` also activates strict custody and requires `decision-authority.md`, all nine decision rights, exact links to evidence declared in `verification.md`, allowed raw states and authority values, bounded negative scope, and a derived result compatible with the recorded `apply` allocation or a non-clearing override. Quick packets reject `--strict-authority` instead of silently skipping it. `--json` prints a versioned receipt (packet file digests, packet-scoped git state, validator version, and evidence-status counts) with the same exit code; see `../02-operating-system/validators.md`. These checks establish declared structural consistency only, not identity, truth, authorization, policy adequacy or evaluation, semantic adequacy, effective human control, or substantive independence.
- `doctor` checks a Nuclear-grade distribution repo for public files, contracts, and templates. In a target repo that has been set up, it checks `.nuclear/README.md` and `.nuclear/changes/`.
- `list` shows what is available: modes, skills, commands, packet files, CM files (records for keeping the approved version under control), golden-path files, and optional templates. That includes turnover, self-check, supplier-trust, and decision-authority records.
- `status` lists active packets, the mode it detects for each, and a health tag: `ok` (it passes the configured structural validator; this is not substantive acceptance), `closed` (deliberately retired with a written reason, carrying a `NUCLEAR-GRADE-CLOSED:` marker line), `scaffold` (an untouched draft that still has the placeholder marker), or `invalid` (fails validation for some other reason). `ok` and `closed` are finished states; only `scaffold` and `invalid` count toward the "needs attention" reminder, so abandoned half-filled drafts stay visible while honestly closed packets are left alone. See the `closing-stale-packets` skill.
- `eval` scores the worked-example artifacts in `evals/cases/` for the decision signals they claim to teach, and exits non-zero if any worked example dropped a required signal. It checks that the named decision elements are present, not that the work is engineering-correct, safe, or compliant. See `docs/03-worked-examples/skill-workflow-comparison/efficacy-harness.md`.
- `decisions` is the **operator receipt**: it rolls up every skill's `## Decision contract` and prints the `block` and `warn` signals (the one decision each skill can move and its tier), keeping `observe`-tier skills in telemetry so the receipt does not become audit-the-audit. `--all` also lists the telemetry rows. It is the generated, single-source view a reviewer scans instead of reading 30 skills; the per-skill receipt stays the source of truth. See `docs/05-reference/skill-authoring-contract.md`.

- `badge` writes a shields.io endpoint JSON counting active change records and their open evidence items (fail, gap, deferred, planned) as declared in Status, Result, or Outcome table cells and `Status:` lines; status words in free prose are not read, and a record with no readable declaration counts as needing attention. It turns yellow when items are open and red when a record needs attention. Closed records are left out. It never says certified, compliant, or passing.
- `required-mode` reads a git diff (base to head, or base to the working tree) and `.nuclear/consequence-policy.json` (read from the base by default, so a change cannot loosen the policy that judges it; with no policy file, a built-in default covers `.github/workflows/**` and the gate's own files). Each changed path gets a minimum mode (`none`, `quick`, `standard`, `standard+authority`) from the highest matching rule; claim rules count only net-new, non-negated claim wording. A requirement is covered only by a change record **added in this diff** that is open, declares a high enough mode, names the path in its `risk.md`, and passes `validate` with the flags that mode needs (`--strict-custody` from Standard; `--strict-authority` too for `standard+authority`). `standard+authority`, policy overrides, and the dependency lane also need an APPROVED review from an account other than the PR author and the configured bot identities, read from `--approvals-json` (CI passes the GitHub reviews). Editing the policy itself always requires `standard+authority`. Exit 0 pass, 1 fail (0 with `--advisory`), 2 for a bad ref or malformed policy. `--json` prints a versioned receipt. The result is a mechanical minimum that judgment can raise; it is a structural check, not a finding that the change or its evidence is adequate. `tools/ng_policy_backtest.py` classifies past commits with a candidate policy before it is enforced.
- `python -m nuclear_grade.release` checks that `pyproject.toml`, both plugin manifests, `CITATION.cff`, and a dated `CHANGELOG.md` section declare the same version and date; with `--tag`, that the tag is `v<version>`. See `releasing.md`.

## Boundary note

The command-line tool checks structure and whether evidence is visible. It does not decide engineering adequacy, safety, security, compliance, regulatory adequacy, or formal verification.

## Source-lineage note

This reference documents local tooling for an open reference workflow built from public sources. It does not create formal assurance.
