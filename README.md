# Execution Without Normativity

Execution Without Normativity is a minimal axiomatic theory of deterministic execution and observation. It defines atomic execution events, an append-only ordered execution stream, and a strict separation between deterministic projections and observational artifacts. The model is intentionally non-normative and avoids governance, policy, or domain semantics.

## Positioning

This paper defines a minimal execution substrate.
It is intentionally non-normative.
Governed architectures can be built on top of it, but are out of scope.

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/main.tex
```

## Scope and non-goals

- no governance, policy, or decision logic
- no domain semantics or application examples
- no claims about correctness or meaning
- no side-channel guarantees
- no distributed consensus or fault tolerance

## Repository layout

- paper/main.tex
- paper/sections/
- paper/refs.bib
- paper/latexmkrc
- notes/roadmap.md
- .github/workflows/build-paper.yml
