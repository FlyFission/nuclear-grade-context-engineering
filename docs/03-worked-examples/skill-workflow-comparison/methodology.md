# Methodology

## Purpose

This evaluation asks one practical question: when a user follows Nuclear-grade skills and workflows, do the records they make help a reviewer decide better than a direct prompt would?

It does not ask whether Nuclear-grade makes code safer, secure, compliant, certified, production-ready, or formally verified.

## Trial Design

Each trial uses the same scenario facts in two paths:

1. **Simple prompt path:** a direct coding-agent prompt that a reasonable developer might write.
2. **Nuclear-grade path:** the matching skills and workflows applied to the same facts, producing focused records, evidence duties, gaps, and decisions.

The trial output is not a separate model benchmark. It judges the records: given what was produced, can a reviewer say what changed, why it matters, what evidence exists, what is missing, and whether to ship, defer, block, or save the approved version?

## Scoring Rubric

Four things are scored 1 to 5: how clear the decision is, how well hidden risk is found, how good the evidence is, and how useful it is for a ship-or-defer call.

| Score | Meaning |
|---|---|
| 1 | Weak; the reviewer cannot rely on it. |
| 2 | Some useful output, but important gaps stay hidden. |
| 3 | Usable, but the reviewer has to fix things. |
| 4 | Strong; most of the decision-useful information is visible. |
| 5 | Strong and compact; the decision, the evidence, and the gaps are clear. |

Overhead is scored separately.

| Score | Meaning |
|---|---|
| 1 | Almost no process cost. |
| 2 | Light cost; fine for Quick work. |
| 3 | Noticeable, but manageable. |
| 4 | Heavy, but worth it given the stakes. |
| 5 | Heavy; likely not worth it unless the stakes are high. |

## Bias Controls

- Simple prompting is not set up to fail. It gets reasonable prompts and normal review expectations.
- Nuclear-grade loses points when it adds ceremony that does not help the decision.
- `gap`, `deferred`, and `block` count as useful outputs when they make the decision better.
- The comparison treats "validator passes" as a sign the structure and evidence are visible, not as approval.
- The comparison records where Nuclear-grade should not be used.

## Limits

- No outside panel of people scored the records.
- We did not measure timing, defect rates, or production outcomes.
- The outputs are judgment-based trials, not controlled experiments.
- The results should guide repo design and examples, not become marketing proof.

## Boundary Note

This methodology does not create formal assurance, compliance, certification, safety, security, production suitability, or regulatory adequacy.

## Source-Lineage Note

This method is an original way to evaluate the workflow. It is based on the Nuclear-grade operating model and the public source-lineage limits in `docs/00-standards-foundation/source-map.md`.
