# Execution Without Normativity

Execution Without Normativity is a minimal axiomatic theory of deterministic execution and observation. It defines atomic execution events, an append-only ordered execution stream, and a strict separation between deterministic projections and observational artifacts. The model is intentionally non-normative and avoids governance, policy, or domain semantics.

## Positioning

This paper defines a minimal execution substrate.
It is intentionally non-normative.
Governed or normative architectures may build on this model,
but such layers are explicitly out of scope here.

The paper (PDF) is the authoritative specification.
This README is descriptive only.

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
- .github/workflows/build-paper.yml
