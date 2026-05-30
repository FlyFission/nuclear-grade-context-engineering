# Supplier Trust Record

<!-- NUCLEAR-GRADE-PLACEHOLDER: replace every field below with real content, then delete this line so validation can pass. -->

**Purpose:** Record the intended use, the evidence, the gaps, the controls that make up for them, and the re-check triggers for dependencies, models, APIs, SaaS tools, generated files, or vendor claims.

**Activation threshold:** Use when an outside item affects the evidence, permissions, data, credentials, release stance, or public trust.

**Minimum useful version:** the identity, the intended use, the consequence if it is wrong, the source claims, the evidence you saw in the repo, the controls, the gaps, and the re-check trigger.

---

## Change context

- Slug:
- Owner:
- Date:
- Related risk record: `risk.md`
- Related basis record: `basis.md`

## External item identity

| Item | Provider/source | Version/model/API surface | Intended use | Controlled item affected |
|---|---|---|---|---|
| | | | | |

## Trust screen

| Question | Answer | Evidence / gap |
|---|---|---|
| What happens if this item is wrong, unavailable, compromised, or changed? | | |
| What data, credential, permission, or network access is involved? | | |
| Which vendor/source claims are being relied on? | | |
| What repo-observed evidence supports the intended use? | | |
| What compensating controls limit trust? | | |
| What revalidation trigger applies? | | |

## Release impact

- Ship posture:
- Residual trust gaps:
- Owner:
- Decision record:

## Required links

- `risk.md`
- `basis.md`
- `verification.md`
- `ship.md` or `decision.md`
- Advisory / changelog / provider docs / local eval evidence:

## Exit criteria

- The intended use is stated plainly and stays within what the evidence supports.
- The vendor and source claims are kept apart from local proof.
- The gaps flow into the verification and release-decision records.

## Source-lineage note

Original Nuclear-grade template inspired by public source families on vendor oversight, software supply chain, AI risk, change management, and verification, mapped in the repo. No compliance claim is made.
