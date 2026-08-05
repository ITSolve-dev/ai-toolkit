---
name: design-aggregates
description: >-
  Use when deciding what belongs inside an aggregate and where its boundary falls — which
  objects must stay transactionally consistent, which entity is the root, and what gets
  referenced by id instead.
---

# Design aggregates

An aggregate is a transactional consistency boundary. The question is never which objects
belong together, but which must be consistent together — and what rule forces it.

## Steps

1. **Confirm the context.** Aggregates are found inside one bounded context. If that boundary
   is unsettled, it comes first.

2. **Elicit the invariants with the user, not from the code.** For each candidate rule apply
   two tests: could it be enforced *without* putting these objects in one transaction — if so
   it is not a true invariant; and is making it consistent the job of the user performing this
   operation, or of someone else afterwards — the second answer means eventual consistency.
   Whether a delay is tolerable is a domain fact. Ask; never assume.

   When there is nobody to ask — an unattended run — do not stop there. Proceed under the most
   likely reading, mark every assumed fact as unconfirmed, and put those assumptions where they
   cannot be missed. Returning questions and nothing else is not an answer either.

3. **Delegate the heavy pass.** Dispatch `domain-driven-guide:domain-modeler` with the confirmed
   invariants and the scope. It fetches the rules of thumb and their reasoning from the base and
   returns the smallest cluster that still holds each invariant, its root, what is referenced by
   identity rather than held, and which rules move outside the boundary.

4. **Test the result against the operations.** If any operation still needs two aggregates
   changed atomically, the boundary is wrong or a concept in the language is missing. Treat it
   as evidence, not as licence for a wider transaction.

5. **State every deviation as a decision.** Breaking a rule of thumb is legitimate for reasons
   the sources enumerate. Breaking one without saying so is how a boundary rots.

## Deliver

**Pass the agent's work through — its citations and its diagram — instead of restating it.**
Every decision reaches the user with the page it rests on. Summarising the citations away in
the last step destroys the one thing that separates this from a confident guess, and redrawing
the diagram yourself spends the context the delegation was meant to save.

Decisions, then a Mermaid `classDiagram`: each root marked as such, its members composed into
it, and cross-boundary references drawn as identity references rather than containment.

Alongside it, state plainly what is now eventually consistent and by what mechanism. That is
the half of the design a diagram cannot carry.
