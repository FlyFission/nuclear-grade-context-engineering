# Compliance Boundaries

**Purpose:** Say clearly what Nuclear-grade is, what it is not, and how it stays away from false claims about meeting a standard.

---

## One-sentence boundary

Nuclear-grade is a public, educational way to do software engineering. It borrows ideas from public high-stakes engineering work. It is **not** a compliance program, a quality assurance (QA) program, a safety basis, a licensing basis, a buying basis, or a stand-in for the judgment of a qualified professional.

---

## License boundary

The repo uses the MIT license. Under that license you may reuse, change, publish, distribute, sublicense, and sell it, within the license terms. The license does not create any warranty, support duty, engineering adequacy finding, regulated-work approval, formal V&V record, NQA-1 record, safety basis, procurement basis, quality assurance program, or fitness finding.

Keep this line clear and use it the same way every time:

| Allowed meaning | Not allowed meaning |
|---|---|
| You may reuse the software/docs under MIT terms. | The repo is approved for a regulated or safety-significant use. |
| Public sources influenced the workflow. | The workflow satisfies those sources. |
| Packets help organize evidence for review. | Packets are formal V&V, QA, safety, procurement, or regulatory records. |
| The validator checks structure and overclaiming. | The validator decides safety, security, compliance, or fitness. |

---

## What this repo may claim

Acceptable language:

- “inspired by public high-consequence engineering practices”;
- “influenced by public nuclear and federal software assurance guidance”;
- “software-native translation of design basis, configuration discipline, traceability, verification, and release readiness concepts”;
- “original workflows using public-source lineage”;
- “risk-scaled rigor without unnecessary overhead.”

---

## What this repo must not claim

Do not claim or imply:

- DOE compliance;
- NRC compliance;
- ASME compliance;
- NQA-1 compliance;
- EPRI alignment or endorsement;
- IEEE/IEC/ISO/ANSI/ANS/NEI compliance;
- nuclear licensing adequacy;
- formal V&V adequacy;
- safety-system qualification;
- commercial-grade dedication;
- safety basis acceptability;
- procurement suitability;
- formal QA program approval;
- regulatory approval or endorsement.

---

## Required disclaimer pattern

Use this pattern in the README, in templates, in examples, and in any doc that cites nuclear or federal sources:

> Nuclear-grade is an educational, public-source-inspired software engineering methodology. It does not claim compliance with DOE, NRC, ASME, EPRI, IEEE, IEC, ISO, ANSI/ANS, NEI, NASA, NIST, CISA, OpenSSF, OWASP, SLSA, or any other standard, regulation, or guidance. Use qualified professionals and applicable governing requirements for regulated work.

Short version:

> Inspired by public high-consequence engineering guidance; not a compliance framework.

---

## Compliance-safe naming rules

Prefer:

| Use | Instead of |
|---|---|
| dependency trust basis | commercial-grade dedication |
| release readiness evidence | QA release package |
| independent review by consequence | independent verification required by X |
| design basis for software | safety basis |
| assurance case | documented safety analysis |
| change impact screen | 50.59-like screen |
| source-lineage note | compliance basis |
| configuration discipline | formal configuration management program |

---

## Template boundary

Templates may include:

- purpose;
- activation threshold;
- minimum useful version;
- evidence expected;
- review trigger;
- source-lineage note;
- anti-overhead guidance;
- example outputs.

Templates must not include:

- copied proprietary language;
- “shall” language that imitates regulated obligations;
- compliance matrices;
- certification language;
- regulatory acceptance statements;
- formal dedication claims;
- acceptance criteria that appear to satisfy a specific regulation.

---

## Source boundary

You may use public sources to explain ideas and where they came from. You may not use them to suggest that following Nuclear-grade meets those sources.

Correct:

> This workflow is influenced by public configuration-management concepts in DOE-STD-1073 and public software CM guidance in NRC RG 1.169.

Incorrect:

> This workflow implements DOE-STD-1073 / NRC RG 1.169 configuration management requirements.

---

## Regulated-work warning

Are you doing regulated nuclear, safety-critical, defense, medical, aviation, or other high-stakes work? Then use Nuclear-grade only as a teaching aid. The one exception is when your governing organization has reviewed it and approved it under the rules that apply to you.
