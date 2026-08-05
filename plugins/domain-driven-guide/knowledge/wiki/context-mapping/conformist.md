---
title: Conformist
category: context-mapping
summary: A downstream team, facing an upstream team with no motivation to serve it, eliminates translation complexity by slavishly adhering to the upstream model.
tags: [pattern, context-mapping, upstream-downstream, team-relationship, integration, conformist]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Conformist** describes an [[upstream-downstream]] relationship in which the downstream team gives up
its own model and adopts the upstream one wholesale. "When two development teams have an
upstream/downstream relationship in which the upstream team has no motivation to provide for the
downstream team's needs, the downstream team is helpless." (raw L2481)

## Definition

Because the upstream team will not accommodate the downstream team's needs — "altruism may motivate
upstream developers to make promises, but they are unlikely to be fulfilled" — the downstream team
"eliminates the complexity of translation between bounded contexts by slavishly adhering to the model of
the upstream team." (raw L2481) *(Definition largely quoted from Evans, raw L2473.)*

## Trade-offs

What you gain is the elimination of translation cost: there is no mapping layer to build or maintain
because you simply use the upstream model as-is. What you give up is the purity and independence of your
own model — upstream concepts flow directly into your context. The alternative, when you want to keep
your model clean, is an [[anticorruption-layer]], which costs translation code but preserves your
[[ubiquitous-language]].

## When it is (and isn't) appropriate

Conformist is not inherently bad: "It's not that a Conformist relationship is always negative." (raw
L2499) It is a reasonable choice when the upstream model is good enough and building translation would
not pay off. The danger is the **unplanned** Conformist: a team counting on a
[[customer-supplier-development]] relationship is forced into Conformist when the upstream team provides
only what it already has (raw L2415). SaaSOvation explicitly refused to let one team force others into
Conformist, preferring Customer-Supplier commitment (raw L2499).

## Related

- [[upstream-downstream]] — the axis this relationship sits on.
- [[customer-supplier-development]] — the cooperative alternative it collapses from.
- [[anticorruption-layer]] — the way to stay downstream without conforming.
- [[context-map]] — where the risk of an unplanned Conformist is surfaced.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
