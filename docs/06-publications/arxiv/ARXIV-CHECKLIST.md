# arXiv package checklist

**Scope:** Academic preprint package for *Who Authored the Evidence? Actor–Evidence Coupling in AI-Assisted Software Acceptance*. Following this checklist does not imply arXiv endorsement, moderation approval, or acceptance.

**Official guidance checked:** 2026-07-20.

## Format and processor

- Submit TeX/LaTeX source when TeX source exists; do not substitute a TeX-generated PDF-only upload.
- Prefer `pdflatex`-compatible source. arXiv currently supports TeX Live 2025 and 2023 and lists `pdflatex` and `xelatex` among supported processors.
- Compile against the selected TeX Live release before submission and inspect arXiv's generated PDF.

## Source package

- Include the top-level `paper.tex`, bibliography input or matching `paper.bbl`, and all required figures/styles.
- Use relative paths, legal case-sensitive filenames, and no hidden dependencies.
- Remove generated PDF, `.aux`, `.log`, `.toc`, `.out`, backup files, and unrelated assets from the upload archive.
- This paper uses inline TikZ figures and standard packages; no external figure files or shell escape are intended.

## Bibliography

- Include `references.bib` and the generated `paper.bbl`.
- Ensure the `.bbl` basename matches `paper.tex`.
- Confirm every citation resolves and every bibliography entry used in the source appears in the final PDF.

## Metadata

- Enter title, authors, and abstract separately in arXiv's form.
- Keep abstract metadata at or below 1,920 characters. The prepared abstract is below this limit.
- Select `cs.SE` only if it is the best topical fit.
- Use Comments for page and figure counts and preprint status; leave Journal-ref blank until an actual publication exists.

## Final clean-build gate

- Build from a clean unpack of the exact source archive without shell escape or network-dependent source inputs.
- Inspect logs for missing citations, overfull boxes, substituted fonts, missing figures, or interactive prompts.
- Verify title, author list, abstract, category, comments, license, and every page of arXiv's generated PDF before submission.

## Official sources

- https://info.arxiv.org/help/submit/index.html
- https://info.arxiv.org/help/submit_tex.html
- https://info.arxiv.org/help/submit_pdf.html
- https://info.arxiv.org/help/faq/whytex.html
- https://info.arxiv.org/help/faq/texlive.html
- https://info.arxiv.org/help/faq/mistakes.html
- https://info.arxiv.org/help/policies/format_requirements.html
- https://info.arxiv.org/help/prep.html
