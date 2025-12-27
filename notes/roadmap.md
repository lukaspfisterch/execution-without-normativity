# Roadmap (out of scope)

This paper is intentionally minimal. The following topics are explicitly out of scope for the current draft and may be addressed later:

- formal semantics for domain meaning or correctness
- normative decision systems or governance layers
- policy languages or rule systems
- domain-specific execution examples
- distributed consensus and fault tolerance
- side-channel resistance and covert channel analysis
- implementation-level canonicalization or hashing details

Recent changes:
- defined authoritative execution inputs $I_{\text{exec}}$ and their boundary against observations
- made $\pi$ explicit as $\pi(V; I_{\text{exec}})$ in the formal model and axioms
- added a lemma that observations cannot expand $I_{\text{exec}}$
