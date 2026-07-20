# arXiv-style preprint source

This directory contains the academic preprint version of Nuclear-grade Context Engineering.

## Main files

- `paper.tex` — top-level LaTeX source
- `references.bib` — BibTeX database
- `paper.bbl` — generated bibliography for arXiv portability (created during verified build)
- `arxiv-metadata.txt` — copy-ready submission metadata
- `ARXIV-CHECKLIST.md` — official-source packaging and submission checklist

## Local build used for this draft

The source uses conventional `article`-class LaTeX and common TeX Live packages. It was designed to compile without shell escape, local absolute paths, custom fonts, or unpublished style files.

Verified local command:

```bash
tectonic -X compile --keep-intermediates --keep-logs paper.tex
```

Tectonic is used only as the local compiler. Before submission, compile a clean unpack with arXiv's selected TeX Live release and inspect arXiv's generated PDF.

## arXiv upload package

The minimal source archive should contain:

```text
paper.tex
paper.bbl
references.bib
```

The figures are drawn with TikZ inside `paper.tex`, so there are no external image dependencies. Do not include the locally generated PDF, `.aux`, `.log`, `.out`, or other intermediates in the source upload.

## Publication posture

This is a discussion preprint, not an accepted or peer-reviewed paper. The repository implementation and current evidence do not establish defect reduction, improved safety, formal assurance, regulatory compliance, or superiority.
