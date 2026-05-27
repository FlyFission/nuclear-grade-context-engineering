# Supplier Trust Record

**Purpose:** Record intended use, evidence, gaps, compensating controls, and revalidation triggers for dependencies, models, APIs, SaaS tools, generated artifacts, or vendor claims.

**Activation threshold:** Use when an external item affects evidence, permissions, data, credentials, release posture, or public trust.

**Minimum useful version:** Identity, intended use, consequence if wrong, source claims, repo-observed evidence, controls, gaps, and revalidation trigger.

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

- Intended use is explicit and narrower than or equal to available evidence.
- Vendor/source claims are separated from local proof.
- Gaps flow into verification and release decision records.

## Source-lineage note

Original Nuclear-grade template inspired by public vendor-oversight, software supply-chain, AI-risk, change-management, and verification source families mapped in the repo. No compliance claim is made.
