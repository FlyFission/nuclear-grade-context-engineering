# Methodology

## Purpose

This evaluation asks a practical repo-readiness question: when a user applies Nuclear-grade skills and workflows, do the resulting artifacts help a reviewer make a better decision than a direct prompt would?

It does not ask whether Nuclear-grade makes code objectively safer, secure, compliant, certified, production-ready, or formally verified.

## Trial Design

Each trial uses the same scenario facts in two paths:

1. **Simple prompt path:** A direct coding-agent prompt that a reasonable developer might write.
2. **Nuclear-grade path:** The relevant skills and workflows applied to the same facts, producing bounded records, proof obligations, gaps, and decisions.

The trial output is not an independent model benchmark. It is an artifact evaluation: given the produced records, can a reviewer answer what changed, why it matters, what evidence exists, what is missing, and whether to ship, defer, block, or baseline?

## Scoring Rubric

Decision clarity, hidden risk discovery, evidence quality, and ship/defer usefulness are scored 1 to 5.

| Score | Meaning |
|---|---|
| 1 | Weak; reviewer cannot rely on it. |
| 2 | Some useful output, but important gaps are hidden. |
| 3 | Usable with reviewer correction. |
| 4 | Strong; most decision-useful information is visible. |
| 5 | Strong and compact; decision, evidence, and gaps are clear. |

Overhead is scored separately.

| Score | Meaning |
|---|---|
| 1 | Almost no process cost. |
| 2 | Light cost; appropriate for Quick work. |
| 3 | Noticeable but manageable cost. |
| 4 | Heavy but justified by consequence. |
| 5 | Heavy; likely unjustified unless consequence is high. |

## Bias Controls

- Simple prompting is not straw-manned. It gets reasonable prompts and normal review expectations.
- Nuclear-grade is penalized when it creates ceremony without decision value.
- `gap`, `deferred`, and `block` are counted as useful outputs when they improve the decision.
- The comparison treats "validator passes" as structure/evidence visibility, not approval.
- The comparison records where Nuclear-grade should not be used.

## Limits

- No independent human panel scored the records.
- No timing, defect-rate, or production outcome measurement was collected.
- Scenario outputs are qualitative artifact trials, not controlled experiments.
- Results should guide repo design and examples, not become marketing proof.

## Boundary Note

This methodology does not create formal assurance, compliance, certification, safety, security, production suitability, or regulatory adequacy.

## Source-Lineage Note

This method is an original workflow-evaluation method based on the Nuclear-grade operating model and public source-lineage boundaries in `docs/00-standards-foundation/source-map.md`.
