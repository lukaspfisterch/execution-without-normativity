# Execution Without Normativity

A foundational paper on execution without implicit normativity.  
It defines the conceptual constraints underlying KL and DBL.

If you are looking for an overview or motivation, start here:  
→ https://github.com/lukaspfisterch/deterministic-boundary-layer

If you are looking for axioms and proofs, continue below.

**Execution Without Normativity** is a minimal axiomatic theory of deterministic execution and observation.

It defines:
- atomic execution events
- an append-only, totally ordered execution stream
- a strict separation between deterministic projections and observational artifacts

The model is intentionally non-normative.  
It avoids governance, policy, decision logic, and domain semantics by design.

---

## Positioning

This paper defines a **minimal execution substrate**.

It is intentionally non-normative.  
Governed or policy-bearing architectures may build on this model,  
but such layers are explicitly **out of scope** here.

The PDF is the **authoritative specification**.  
This README is descriptive only.

---

## Authoritative specification

- **Execution Without Normativity – v1.0 (PDF)**  
  [paper/main.pdf](paper/main.pdf)

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
