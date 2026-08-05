---
title: When to Use DDD (and Tactical Modeling)
category: foundations
summary: Decision heuristics for whether a project deserves the DDD investment at all, and whether a given subdomain deserves the extra cost of the tactical patterns — apply it to complex, strategically important domains, not everywhere.
tags: [heuristic, decision-rule, core-domain, subdomain, tactical-design, transaction-script]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

DDD carries a real up-front cost of time and thought, so it should be applied *deliberately* — to
domains where the investment pays off — not by default. Two nested decisions are involved: (1) does
this project deserve DDD at all, and (2) does this particular [[subdomain]] deserve the heavier
**tactical patterns** ([[aggregate]]s, [[entity]]s, [[value-object]]s, **Services**,
[[domain-event]]s)?

## Guiding principle: simplify the complex, invest where it matters

> "Use DDD to model a complex domain in the simplest possible way. Never use DDD to make your solution
> more complex." (raw L922)

DDD concentrates effort on what distinguishes the business: "You invest in the nontrivial, the more
complex stuff, the most valuable and important stuff that promises to return the greatest dividends"
(raw L918). That high-value model is the [[core-domain]]; significant Supporting [[subdomain]]s come
second; easily replaceable areas get little. Because "complex" is subjective, Vernon suggests judging
instead whether the system is **nontrivial** — a threshold that differs by company maturity and team
capability (raw L924).

## Whether to do DDD at all: the scorecard

Vernon offers a **DDD Scorecard** (Table 1.1): score each row that describes your project, tally the
points, and "if it's 7 or higher, seriously consider using DDD" (raw L926). The deeper lesson the
exercise teaches: get good at judging simplicity vs. complexity *early*, because "once we make a major
architectural decision and get several use cases deep in development, we are usually stuck with it"
(raw L940).

## Whether to invest in tactical modeling

Tactical modeling "is generally more complex than strategic modeling" (raw L1512), so it needs
justification (raw L1522–1528):

- **Core Domain Bounded Context** — strategically vital, not well understood, needs experimentation
  and longevity: strongly use the tactical patterns as an investment in the future, staffed with the
  best developers.
- **Judge from *your* business's viewpoint.** "A domain that may become a Generic Subdomain or
  Supporting Subdomain to its consumers may actually be a Core Domain to your business" (raw L1524) —
  if it is your chief initiative, treat it as your [[core-domain]] regardless of how customers see it.
- **Innovative Supporting Subdomain that cannot be bought** — if the model is genuinely innovative
  (adds business value, captures special knowledge, not merely technically interesting) and must
  endure for years, tactical patterns can be worthwhile — but this still does not make it the Core
  Domain.

Where the team is highly experienced and comfortable with modeling, trust their case-by-case judgment
(raw L1530).

## Detailed decision parameters

More granular questions to settle the call (raw L1534–1550):

- Are domain experts available, and are you committed to forming a team around them?
- Is the domain simple *now* but likely to grow in complexity? Refactoring **Transaction Script** into
  a behavioural [[domain-model]] later is often impractical.
- Will tactical DDD make integration with other [[bounded-context]]s easier?
- Will Transaction Script *really* be less code? "Many times Transaction Script requires as much or
  more code" because domain complexity was underestimated during planning (raw L1540).
- Do timeline and critical path allow for the tactical overhead?
- Will a Core Domain investment protect the system from disruptive architectural change? ("Domain
  models are often enduring while architectural influences tend to be more disruptive", raw L1544) —
  Transaction Script leaves it exposed.
- Could the application be replaced by an off-the-shelf solution tomorrow? If so, why build it custom?
- Team skill level and availability of DDD enablers (ORM, Aggregate persistence, an Event Store, a
  supporting framework).

This list is unprioritized; ultimately "it is the business customer, not the object practitioners and
technologists, who must be pleased" (raw L1552).

## Countering the "DDD is heavy" objection

The cost concern is real but overstated: DDD is meant to fit any agile framework and lean on "rather
rapid test-first refinements of a real software model" (raw L1556) rather than heavy up-front design.
A new [[entity]] or [[value-object]] is grown test-first — client-style test, minimal object to
compile, refactor toward proper behavioural signatures, implement until green, then demonstrate to
domain experts to confirm it honours the current [[ubiquitous-language]] (raw L1558–1566).

## Related failure mode

Beware [[ddd-lite]]: picking a subset of the tactical patterns "without giving full attention to
discovering, capturing, and enhancing the Ubiquitous Language" and bypassing [[bounded-context]]s and
[[context-map|Context Mapping]] (raw L1604). It can have benefits but generally far less reward than
including strategic design.

## Related

- [[domain-driven-design]] — what the investment buys and how the halves fit.
- [[core-domain]], [[subdomain]] — where to concentrate the tactical effort.
- [[domain-model]] — the behavioural model the tactical patterns build.
- [[ddd-lite]] — the shortcut that skips strategic design.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
