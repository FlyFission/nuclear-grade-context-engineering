# Baselines

**Purpose:** This file says how Nuclear-grade writes down an accepted, controlled state.

## Baseline rule

A baseline is the identified state accepted for reliance under a recorded decision, evidence set, residual risks, and revalidation triggers. Agreement records the accepted state and decision basis; it does not establish that the state is objectively correct. Git history helps locate the state, while the baseline record explains why reliance was authorized and when that reliance must be reconsidered.

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

This baseline model is an open Git-native translation of public configuration-management and lifecycle concepts mapped in `../00-standards-foundation/source-map.md`. It does not create formal assurance or compliance.
