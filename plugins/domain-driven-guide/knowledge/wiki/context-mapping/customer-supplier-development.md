---
title: Customer-Supplier Development
category: context-mapping
summary: An upstream/downstream relationship where the upstream 'supplier' commits to the downstream 'customer's' needs — downstream priorities are negotiated into upstream planning.
tags: [pattern, context-mapping, upstream-downstream, team-relationship, integration, customer-supplier]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Customer-Supplier Development** is the cooperative form of an [[upstream-downstream]] relationship.
"When two teams are in an upstream-downstream relationship, where the upstream team may succeed
independently of the fate of the downstream team, the needs of the downstream team come to be addressed
in a variety of ways." (raw L2479)

## Definition

Downstream priorities factor into upstream planning. The teams negotiate and budget tasks for
downstream requirements "so that everyone understands the commitment and schedule." (raw L2479) The
defining feature is the **supplier's commitment** to serve the customer — an obligation absent in a
[[conformist]] relationship. *(Definition largely quoted from Evans, raw L2473.)*

## When to use it

Use it when the upstream team is *willing and able* to accommodate the downstream team. SaaSOvation
deliberately chose Customer-Supplier roles: "There's no way that SaaSOvation's management will allow one
team to force others to be Conformists." (raw L2499) The reasoning is that Customer-Supplier "requires
commitment on the part of the Supplier to provide support for the Customer," which fosters the
inter-team relationships the company needs to succeed (raw L2499).

## Trade-offs and failure modes

The relationship needs give-and-take: "Customers aren't always right, and so some give-and-take must
exist." (raw L2499) The central failure mode is a Customer-Supplier relationship that is *assumed but
never agreed*: if the upstream team has no real motivation to provide for you, altruistic promises go
unfulfilled and the relationship silently collapses into [[conformist]] (raw L2415, L2481). Drawing a
[[context-map]] early is the guard against discovering that collapse late in the project.

## Related

- [[upstream-downstream]] — the axis this cooperative relationship sits on.
- [[conformist]] — what it degrades into when the supplier won't commit.
- [[partnership]] — the symmetric high-coordination alternative.
- [[context-map]] — where the relationship is surfaced and its assumptions checked.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
