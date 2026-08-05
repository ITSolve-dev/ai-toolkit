---
name: model-entities-and-value-objects
description: >-
  Use when modelling the tactical building blocks — deciding whether a concept is an entity or
  a value object, how identity is generated, what stays immutable, where validation lives, and
  when behaviour belongs in a domain service instead. Trigger on "entity or value object",
  "value object", "should this have an id", "where do I put this validation", "primitive
  obsession", "domain service".
---

# Model entities and value objects

The classification belongs to a concept *in a context*, not to the concept itself. The same
idea can be an entity in one context and a value in another.

## Steps

1. **Scope the concepts, and name the context** they are being modelled in.

2. **Ask the identity question, per concept.** Does the domain need to tell one instance from
   another and follow it through change? If value equality suffices, it is a value object. The
   confirming test is replacement: what can be swapped whole rather than mutated is a value.

3. **Default to value object, and know why the default leans.** The bias is deliberate and
   rests on the cost of being wrong: an unnecessary wrapper is cheap to undo, while treating a
   value as an entity because storage gives it a key is not. When persistence is what pushes
   toward entity, that is precisely the pressure to resist.

4. **Delegate the heavy pass.** Dispatch `domain-driven-guide:domain-modeler` with the concept
   list and the context. It fetches the tests from the base and returns the classification per
   concept with its reasoning, an identity strategy wherever the answer is entity, and where
   behaviour and validation belong.

5. **Watch for the third answer.** Some concepts are neither — the behaviour has no natural
   owner, or construction itself is the problem. Do not force the binary.

## Deliver

**Pass the agent's work through — its citations and its diagram — instead of restating it.**
Every decision reaches the user with the page it rests on. Summarising the citations away in
the last step destroys the one thing that separates this from a confident guess, and redrawing
the diagram yourself spends the context the delegation was meant to save.

Decisions per concept, then a Mermaid `classDiagram` marking each type with its stereotype and
showing which values are held as properties of which entities.

Where the sources hold more than one position — validation placement is the clearest case —
present both and the choice they turn on, rather than picking one silently.
