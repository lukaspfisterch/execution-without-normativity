# Execution Without Normativity

[![Execution Without Normativity DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19600773.svg)](https://doi.org/10.5281/zenodo.19600773)
[![DBL DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19600832.svg)](https://doi.org/10.5281/zenodo.19600832)
[![build-paper](https://github.com/lukaspfisterch/execution-without-normativity/actions/workflows/build-paper.yml/badge.svg)](https://github.com/lukaspfisterch/execution-without-normativity/actions/workflows/build-paper.yml)

A foundational paper about the most minimal mechanics of execution.

This repository describes **what it means for something to be executed at all**,
before questions of meaning, correctness, policy, or governance are introduced.

If you are looking for the companion governance paper built on top of this
execution substrate, start here:  
https://github.com/lukaspfisterch/dbl-paper

If you are looking for axioms and proofs, continue below.

---

## Conceptual frame

Execution in this model is purely structural:
a state exists, an event occurs, and a new state exists.
No meaning, correctness, or purpose is assumed.

The guiding question is:

> What is the smallest structure required so that execution can exist at all?

---

## What this paper is about

**Execution Without Normativity** is a minimal axiomatic theory of deterministic
execution and observation.

It defines:

- atomic execution events
- an append-only, totally ordered execution stream
- a strict separation between deterministic projections and observational artifacts

The model is intentionally **non-normative**.

It avoids:
- governance
- policy
- decision logic
- domain semantics

by design.

---

## Positioning

This paper defines a **minimal execution substrate** and is best read as a
foundational reference document for later governance-layer work.

It does **not** decide what should happen.  
It does **not** evaluate outcomes.  
It does **not** attach meaning to execution.

Governed or policy-bearing architectures may build on this model,
but such layers are explicitly **out of scope** here.

The companion `dbl-paper` repository is one such governance-layer extension.

This repository answers only one question, stated above.

The PDF is the **authoritative specification**.  
This README is descriptive only.

---

## Why such an extreme model?

In most IT systems today, execution is tightly coupled with:
- meaning
- correctness assumptions
- policy decisions
- implicit normativity

This project intentionally goes in the opposite direction.

It is an extreme counterexample:
a model where execution exists without meaning,
without evaluation,
and without judgment.

Not because this is how most systems should be built,
but because without such a counterexample,
it is impossible to see where normativity actually enters a system.

---

## Authoritative specification

- **Execution Without Normativity – v1.0 (PDF)**  
  [paper/main.pdf](paper/main.pdf)

*(Warning: formal, axiomatic, and intentionally dense.)*

---

## Build

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/main.tex
```

---

## Scope and non-goals

This work explicitly does not address:

- governance, policy, or decision logic
- domain semantics or application-level meaning
- correctness beyond structural and deterministic properties
- side-channel guarantees
- distributed consensus, replication, or fault tolerance

---

## Repository layout

- paper/main.tex
- paper/sections/
- paper/refs.bib
- paper/latexmkrc
- .github/workflows/build-paper.yml

