---
title: Problem Space and Solution Space
category: subdomains
summary: Two complementary views in strategic assessment — the problem space (the Core Domain plus the Subdomains it needs, analyzed with Subdomains) and the solution space (the concrete Bounded Contexts that realize it).
tags: [concept, problem-space, solution-space, strategic-design, subdomain, bounded-context, assessment]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Every Domain has "both a problem space and a solution space." (raw L1824) Separating them is how DDD
steers a strategic initiative before any code is written — the tools differ for each view.

## Problem space — assessed with Subdomains

"The problem space is the parts of the Domain that need to be developed to deliver a new
[[core-domain]]… your problem space is the combination of the Core Domain and the [[subdomain]]s it
must use." (raw L1826) Its purpose is exploratory: "Subdomains allow us to rapidly view different parts
of the Domain that are necessary to solve a specific problem." (raw L1826) The set of subdomains in
play changes from project to project because each project explores a different strategic problem.

Problem-space assessment questions (high-level but thorough) (raw L1842–L1850):

- What is the name of, and vision for, the strategic Core Domain?
- Which concepts belong in the Core Domain?
- What Supporting and Generic Subdomains are necessary?
- Who should do the work in each area, and can the right teams be assembled?

## Solution space — realized with Bounded Contexts

"The solution space is one or more [[bounded-context]]s, a set of specific software models… the Bounded
Context is a specific solution, a realization view, once developed." (raw L1828) Here you reason in
terms of each context's [[ubiquitous-language]] and the integrations between them.

Solution-space assessment questions (raw L1860–L1878): what assets already exist and are reusable; what
must be acquired or built; how things integrate and what integration is still needed; the required
effort and probability of success; where the Ubiquitous Languages differ completely versus overlap; how
shared terms are mapped/translated between contexts; and which context holds the Core Domain and which
tactical patterns will model it.

## The alignment goal — and brownfield reality

"It is a desirable goal to align Subdomains one-to-one with Bounded Contexts. Doing so expressly
segregates domain models into well-defined areas of business by objective, melding the problem space
with the solution space." (raw L1830) This is achievable in a greenfield effort. In legacy systems —
often a [[big-ball-of-mud]] — subdomains instead *intersect* contexts. An **assessment view** lets you
conceptually divide one large context into multiple subdomains, or span several contexts within one
subdomain. A monolithic ERP is "strictly speaking… a single Bounded Context," yet it is useful to treat
its inventory and purchasing modules as distinct *Inventory* and *Purchasing* Subdomains for analysis
(raw L1832). "You can't change the world of bad software design" — expect to analyze multiple implicit
models inside a single brown context (raw L1890).

## The perspective shift between the spaces

A subdomain in the problem space and a context in the solution space need not coincide. From the
viewpoint of the company building an inventory system, "in the solution space the geographical mapping
service is not part of the Inventory Context, although in the problem space it is considered part of the
Inventory Subdomain" (raw L1894) — the mapping service's Ubiquitous Language is mutually exclusive with
Inventory's, so it is a separate [[bounded-context]].

## Related

- [[subdomain]] — the problem-space building block.
- [[core-domain]] — the centre of the problem space.
- [[bounded-context]] — the solution-space realization.
- [[context-map]] — the solution-space assessment of how contexts relate.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
