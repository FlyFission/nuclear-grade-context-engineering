# Observation recipes

How to turn a produced artifact into something you can actually look at, per type. The skill (`../SKILL.md`) requires a *direct* observation of the delivered output; this catalog is the how. Loaded only when the skill needs it.

The governing rule for every entry: **use whatever the project's own toolchain already provides.** These are patterns, not mandated tools. If no way to observe the real output exists in the current environment (no renderer, no viewer, no network), that is an INCONCLUSIVE tooling gap to escalate -- never a pass inferred from the source.

## Raster image (PNG, JPG, WEBP)

- Open the file and read it directly at full resolution. Read tools that accept images render it visually.
- Check the whole frame, not a thumbnail: labels, legends, axis ticks, overlaps, clipping at edges, color rendering.

## Vector image (SVG, EPS)

- The source is XML, not the artifact. Rasterize it first, then read the raster: a headless browser, `rsvg-convert`, `inkscape --export`, `cairosvg`, or the project's own build step.
- Confirm fonts actually resolve after rasterization -- a missing font substitutes silently and only shows in the render.

## PDF (reports, papers, exports, books)

- Rasterize each relevant page to an image and read the pages: `pdftoppm`, `pdftocairo`, `pdf2image`, or `mutool draw`. Reading the PDF's extracted text is not observing the page -- pagination, overflow, figure placement, and table breaks are invisible to a text extract.
- Walk every page that the change could affect, not just page one. Page-break defects appear at boundaries.

## Built web UI (component, page, app)

- Render it and screenshot it headless (the pre-installed Chromium via Playwright, or the project's e2e harness), then read the screenshot.
- Observe the actual viewport a consumer uses, and the affected states -- not just the default. A source-correct component can still render broken.

## Compiled app or binary (desktop, CLI, mobile)

- Run it and capture the real behavior: the CLI's actual stdout/stderr and exit code, a screenshot of the desktop or mobile UI, the produced file it writes.
- Observe the output of running it, not the build log. "Build succeeded" is a claim about the process, not the product.

## Deployed endpoint or service

- Fetch the real response from the running service and read the actual body, status, and headers -- not the deploy config or the handler source.
- Exercise the affected paths and inputs a consumer hits, including an error path where the spec defines one.

## Exported dataset (CSV, XLSX, JSON, Parquet)

- Open the exported file and spot-check rows, types, encodings, null handling, and totals against the spec -- the export step can corrupt what the query returned correctly.
- Confirm the row/column counts and a few known values, not just that the file exists and parses.

## Diagram from a markup language (Mermaid, Graphviz, PlantUML)

- Render the markup to an image and read the image; the markup text is the source, not the diagram. Overlapping nodes, cut edges, and unreadable labels appear only in the render.
- If a validating renderer is available (e.g. a Mermaid validate-and-render step), use it -- a syntactically valid diagram can still lay out wrong.

## When no observation is possible

If the environment cannot produce something to look at -- the renderer is missing, the service is unreachable, the toolchain will not run here -- stop and return INCONCLUSIVE naming exactly what is missing and who can run it. Do not substitute a source read for the observation and call it verified.
