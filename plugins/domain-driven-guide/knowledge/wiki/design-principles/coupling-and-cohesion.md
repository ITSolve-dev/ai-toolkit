---
title: Coupling and Cohesion
category: design-principles
summary: Coupling is when you can't change one component without risking another; cohesion is when coupled elements genuinely belong together. Local coupling backed by high cohesion is healthy; global coupling without cohesion grows superlinearly into a Ball of Mud.
tags: [concept, coupling, cohesion, big-ball-of-mud, abstraction, boundaries, design-principles, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

**Coupling** measures how much changing one part of a system forces changes in another. **Cohesion** measures how much the elements grouped together actually belong together. They are the working vocabulary for deciding *where to draw boundaries* — the question that sits underneath every DDD boundary decision, from [[bounded-context]] splits to [[aggregate]] boundaries to the [[anticorruption-layer]].

## Definition

> When we're unable to change component A for fear of breaking component B, we say that the components have become *coupled*. (raw L1517)

Coupling is not intrinsically bad. It has a local face and a global face, and they point in opposite directions.

**Locally, coupling is good** — it is what "working together" looks like:

> Locally, coupling is a good thing: it's a sign that our code is working together, each component supporting the others, all of them fitting in place like the gears of a watch. In jargon, we say this works when there is high *cohesion* between the coupled elements. (raw L1518..1521)

High cohesion is the justification for the coupling: the parts change together *because they are about the same thing*. This is exactly why an [[aggregate]] clusters the objects that must stay consistent together, and why a [[bounded-context]] draws a line around a model that shares one [[ubiquitous-language]].

**Globally, coupling is a liability:**

> Globally, coupling is a nuisance: it increases the risk and the cost of changing our code, sometimes to the point where we feel unable to make any changes at all. This is the problem with the Ball of Mud pattern: as the application grows, if we're unable to prevent coupling between elements that have no cohesion, that coupling increases superlinearly until we are no longer able to effectively change our systems. (raw L1523)

The distinguishing symptom of the **[[big-ball-of-mud|Ball of Mud]]** failure mode is coupling *between elements that have no cohesion* — parts that are wired together but are not about the same thing. The cost is not linear: it grows superlinearly, until change becomes practically impossible.

## The remedy: abstract away the details

> We can reduce the degree of coupling within a system ... by abstracting away the details. (raw L1525)

Inserting a simpler [[abstractions|abstraction]] between two subsystems cuts the *number of kinds* of dependencies the caller has on the callee. With many arrows (many kinds of dependency), a change to system B is likely to ripple back into system A. With one simpler abstraction in between, A depends only on the abstraction:

> The abstraction serves to protect us from change by hiding away the complex details of whatever system B does — we can change the arrows on the right without changing the ones on the left. (raw L1541..1543)

## Why this matters for DDD

Most DDD boundary patterns are, at root, cohesion/coupling decisions:

- A **[[bounded-context]]** is a cohesion boundary — it groups a model whose parts change together and firewalls it from models that do not, so global coupling between contexts stays low.
- An **[[aggregate]]** boundary encloses the objects that must be consistent together (high cohesion) and treats everything outside as loosely coupled (reference by identity, eventual consistency).
- An **[[anticorruption-layer]]** is a deliberately inserted abstraction that stops another context's model from leaking coupling into yours.
- The **[[repository]]** is an abstraction over storage that decouples the domain model from persistence details — see [[decoupling-domain-logic-from-infrastructure]].

The heuristic to carry: *coupling is only worth its cost where cohesion is high.* Where you find coupling without cohesion, that is where a boundary or an abstraction belongs.

## Related

- [[abstractions]] — the tool that reduces coupling by hiding detail.
- [[decoupling-domain-logic-from-infrastructure]] — coupling/cohesion applied to the domain–infrastructure seam.
- [[big-ball-of-mud]] — the failure of unchecked coupling without cohesion.
- [[bounded-context]] · [[aggregate]] · [[anticorruption-layer]] · [[repository]] — DDD boundaries that are coupling decisions.
- [[web-page-cosmic-python-book]] — source summary (Ch. 3, "A Brief Interlude: On Coupling and Abstractions").
