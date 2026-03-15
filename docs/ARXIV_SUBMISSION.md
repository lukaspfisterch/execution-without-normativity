# arXiv Submission

This document is the practical checklist for submitting `Execution Without Normativity` to arXiv.

## Target

- Primary category: `cs.LO`
- Submission type: TeX source upload, not PDF-only
- arXiv accepts a packaged `.tar` or `.zip` archive for TeX submissions

## Manuscript state

Before submission, confirm:

- `paper/main.tex` has a fixed date
- author line is stable and minimal
- the manuscript builds cleanly from source
- the PDF title, abstract, and references match the intended public version

## Upload contents

Prepare a clean source bundle from `paper/` only.

Include:

- `main.tex`
- `sections/*.tex`
- `refs.bib` or a generated `.bbl`
- any image files actually referenced by the paper
- `latexmkrc` only if needed for local reproduction, not for arXiv itself

Do not include:

- `main.pdf`
- `*.aux`
- `*.log`
- `*.out`
- `*.fls`
- `*.fdb_latexmk`
- other local build artifacts

## Local bundle command

From the repo root:

```bash
python scripts/build_arxiv_bundle.py
```

This writes a clean upload archive under `dist/arxiv/`.

The generated `.zip` file is suitable for arXiv upload. A `.tar` archive would
also be acceptable, but `.zip` is fine.

## Metadata

Set in the arXiv web form:

- title: `Execution Without Normativity: A Minimal Theory of Deterministic Execution and Observation`
- author: `Lukas Pfister`
- abstract: use the abstract from `paper/main.tex`
- category: `cs.LO`
- comments: optional, e.g. `Foundational theory paper; companion implementation stack available on GitHub.`

## Licensing

Choose an arXiv license deliberately at submission time.

If broad downstream reuse is desired, a permissive public license is reasonable.
If the goal is mainly archival timestamping with fewer reuse assumptions, choose the more conservative option offered by arXiv.

## Endorsement

If the account or category requires endorsement, resolve that before planning a same-day submission.

## Final pre-submit check

1. Build the paper once more locally.
2. Verify that the upload bundle contains only source files.
3. Check that references resolve correctly.
4. Preview the arXiv-rendered PDF.
5. Submit only after the preview matches the intended public version.
