---
title: Subdomain
category: subdomains
summary: A distinct sub-area of a business Domain; DDD classifies each subdomain as Core, Supporting, or Generic to concentrate investment where excellence actually matters.
tags: [concept, subdomain, strategic-design, core-domain, supporting-subdomain, generic-subdomain, problem-space]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Domain** in the broad sense is "what an organization does and the world it does it in" (raw L1666).
Almost every domain decomposes into **Subdomains**: "There are different functions that make any
business successful, so it's advantageous to think about each of those business functions separately"
(raw L1674). DDD deliberately rejects a single all-encompassing enterprise model in favour of separate
models per subdomain (raw L1670).

A subdomain need not be a large model. "Sometimes a Subdomain can be as simple as a set of algorithms
that, while essential to the business solution, are not part of the distinguished Core Domain" — such
simple subdomains can be separated from the Core using **Modules** rather than a heavyweight subsystem
(raw L1708).

## The three-way classification

Every subdomain is one of three kinds — the classification drives how much you invest and where you
demand excellence:

- **[[core-domain]]** — "of primary importance to the success of the organization." The business must
  *excel* here; it gets the best people and most of the DDD effort (raw L1754).
- **Supporting Subdomain** — models "some aspect of the business that is essential, yet not Core" and
  is "somewhat specialized" (raw L1756). You build it because no off-the-shelf option fits well enough.
- **Generic Subdomain** — "captures nothing special to the business, yet is required for the overall
  business solution" (raw L1756). It is replaceable: you "could replace this Subdomain with any
  off-the-shelf… system as long as it fulfills your basic business needs" (raw L1886).

A critical caveat: "Being Supporting or Generic doesn't mean unimportant. These kinds of Subdomains are
important to the success of the business, yet there is no need for the business to excel in these
areas." (raw L1756)

## Classification is relative to perspective

The same capability can be classified differently by different organizations. A geographical mapping
service is a **Generic** subdomain to the retailer who consumes it, but "from the point of view of the
external business organization that develops and offers the mapping service… mapping is a Core Domain"
(raw L1896). Likewise a **Generic** off-the-shelf part can operate in a **Supporting** fashion when
paired with custom work: an ERP purchasing module is generically replaceable, "but being used along
with the new Purchasing Context in the Purchasing Subdomain makes it work in a Supporting fashion" (raw
L1886). In the SaaSOvation examples, CollabOvation is a *Supporting Subdomain* to ProjectOvation (raw
L2331), while Identity & Access is a *Generic Subdomain* to the contexts that consume it (raw L2309).

## Relationship to Bounded Contexts

Subdomains are a **problem-space** tool; [[bounded-context]]s are the **solution-space** realization
(see [[problem-space-and-solution-space]]). The desirable goal is a one-to-one alignment of subdomain
to context — achievable in greenfield work — but "a single Bounded Context does not necessarily fall
within only a single Subdomain" (raw L1720), and legacy/brownfield systems commonly show subdomains
intersecting contexts.

## Related

- [[core-domain]] — the kind that earns the DDD investment.
- [[bounded-context]] — the solution-space realization of a subdomain.
- [[problem-space-and-solution-space]] — the two views subdomains and contexts belong to.
- [[blending-models-in-one-context]] — what happens when subdomain concerns are not separated.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
