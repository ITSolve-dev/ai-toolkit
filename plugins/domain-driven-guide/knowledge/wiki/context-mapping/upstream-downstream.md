---
title: Upstream / Downstream Relationship
category: context-mapping
summary: The directional relationship between two integrated Bounded Contexts — the upstream model influences the downstream one, which depends on it; the axis underlying Customer-Supplier, Conformist, OHS and ACL.
tags: [concept, context-mapping, integration, autonomy, dependency, upstream-downstream]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

When two [[bounded-context]]s integrate, one is usually **upstream** and the other **downstream**. On a
[[context-map]] this is called out with the labels **U** and **D** at each end of a relationship, which
makes the vertical positioning of the contexts less important though still visually useful (raw L2569).

## The river metaphor

Vernon's mental model: "Upstream models have influences on downstream models, as activities on a river
that occur upstream tend to have impacts on populations downstream" (raw L2569). A city dumping
pollutants upstream feels little effect itself, while downstream cities suffer — so changes and failures
propagate *down* the dependency.

Crucially, the upstream team may succeed *independently of the fate of the downstream team*. That
asymmetry is exactly what makes several context-mapping patterns necessary: it drives whether the
downstream team gets a cooperative [[customer-supplier-development]] relationship or is left
[[conformist]] and helpless.

## Direction is not prestige

A Context Map is not a system-architecture diagram, so the most important context need not sit at the
top or centre. In SaaSOvation's map the *Agile Project Management Context* — the current [[core-domain]]
— sits at the bottom, visually signaling that "the core model is downstream of the others" (raw L2567).
The *Identity and Access Context* is furthest upstream, influencing both the Collaboration and Agile PM
contexts; Collaboration is in turn upstream of Agile PM because the agile model depends on collaboration
services (raw L2577).

## Downstream still needs autonomy

Being downstream does not mean surrendering independence. "ProjectOvation will operate as autonomously
as is practical… We must design in ways to drastically limit direct real-time dependencies" (raw
L2577). A downstream context cannot be *entirely* independent of upstream models, but it should minimize
real-time coupling — see [[bounded-context-autonomy]]. The typical division of labour: upstream
publishes via [[open-host-service]] + [[published-language]]; downstream protects itself with an
[[anticorruption-layer]].

## Related

- [[context-map]] — where the U/D direction is drawn.
- [[customer-supplier-development]], [[conformist]] — the two asymmetric relationships this axis
  produces.
- [[partnership]] — the symmetric alternative when neither side is purely upstream.
- [[open-host-service]], [[published-language]], [[anticorruption-layer]] — the integration division of
  labour.
- [[bounded-context-autonomy]] — how a downstream context stays usable.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
