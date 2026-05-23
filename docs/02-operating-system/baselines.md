# Baselines

**Purpose:** Define how Nuclear-grade records accepted controlled configuration state.

## Baseline rule

A baseline is the approved state of selected controlled items at a decision point. Git history helps identify the state, but the baseline record explains why it is acceptable and when it must be revisited.

## Minimum useful baseline

Record:

- baseline name and date;
- commit, PR, release, package, or artifact identity;
- controlled items included and excluded;
- linked basis, impact, verification, review, and ship records;
- accepted gaps and residual risks;
- revalidation and re-baseline triggers.

## Use when

- a Standard packet ships;
- a public doc, skill, command, template, validator, or source map changes;
- prompts, models, dependencies, tools, permissions, evals, or release artifacts become trust-bearing;
- operation reveals drift from the approved state.

## Source-lineage note

This baseline model is an original Git-native translation of public configuration-management and lifecycle concepts mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
