# Artifact review

This procedure covers public evidence, research records, and assets. It records the limits of these updates; it does not certify licenses, privacy, safety, security, or fitness for any use. The [release inventory](release-review.md) records what is included.

## Research records and third-party terms

The research exports omit the copied `abstract` and `summary` fields from four JSON research files under `docs/06-publications/research/data/`. These fields came from arXiv and Crossref records. Source identifiers, titles, authors, links, dates, search provenance, screening scores, and repo-authored annotations remain. The removal is a precaution for unverified reuse terms, not a finding that a particular reuse was unlawful. `tests/test_research_metadata.py` prevents these API text fields from being reintroduced without revisiting this policy.

Follow source links to read the original works. Before adding copied third-party text or assets, record its source, applicable terms, attribution, permitted scope, and any required notices. Preserve a distinction between original project material under MIT and third-party material governed by its own terms. API availability and public readability do not establish redistribution rights. The existing Contributor Covenant attribution identifies adapted material; check its upstream terms when updating it.

## Raw evidence publication

Model transcripts can copy private information from session context. Challenge runs also record commands, stdout/stderr, diffs, environment/tool details, and sometimes user-selected flags. Use a throwaway environment with no unrelated private context when collecting evidence.

Before accepting a pilot, control-ladder, or challenge submission for public inclusion:

1. Obtain the contributor's explicit consent to publish the reviewed artifacts and their chosen attribution. Do not infer consent to disclose unrelated people, systems, or data from participation in a run.
2. Inspect JSON, transcript, diff, and attached assets for credentials, personal contact details, local paths, confidential identifiers, third-party text, and embedded metadata. Separate contextual fictional attack examples from actual data. Prefer reserved example domains in new fixtures.
3. Redact values in a private review copy and retain only the detail needed to assess the result. Record what categories changed and why; do not put removed values in commits, issue comments, logs, or the redaction record.
4. Preserve the distinction between original and published evidence. The challenge runner hashes transcript and diff bytes, so edits require updated hashes and a disclosed redaction/provenance record. Re-score if a redaction could alter interpretation; do not present edited evidence as byte-identical to the original.
5. Run the applicable artifact review checks, then review their coverage and remaining gaps. A passing pattern scan does not establish that the content is safe to publish. Ask the contributor to approve the exact redacted publication copy when the review changes it.

The challenge issue form already asks contributors to remove secrets. Maintainer review remains necessary before copying submissions into the repository. Keep unreviewed raw material out of public issues and commits.

## Historical material

The previous personal-email redaction changed current files only. Earlier commits still contain the original value. Current-tree artifact review, including this change, does not clean old commits, pull-request refs, forks, downloaded clones, release artifacts, or GitHub caches.

The maintainer must coordinate any history rewrite and hosting cleanup: establish affected refs and artifacts privately, arrange collaborator coordination, follow GitHub's sensitive-data removal process where applicable, and request removal of cached views or affected pull-request refs as needed. Recheck published artifacts and reachable refs afterward and record remaining external-copy limitations. Historical copied abstracts need the same explicit scope decision; deleting current fields does not remove old copies. This change does not rewrite history or claim these actions have happened. Never reproduce the personal address in a public cleanup request or report.

## Assets and claims

Keep reproducible sources for generated visuals and demos. The terminal demonstration retains its tape and simulator, and the README labels it as simulated. Metadata inspection does not verify every GIF frame or prove originality. Review the actual rendered publication artifact when it changes.

Public evidence claims must preserve the reported limits: repo-authored scenarios and rubrics, model-family restrictions, non-replication results, and the missing independent study. Redacting a transcript or keeping a provenance record does not create independent evidence or regulated assurance.
