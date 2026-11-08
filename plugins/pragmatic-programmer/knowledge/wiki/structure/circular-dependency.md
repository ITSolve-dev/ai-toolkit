---
title: Circular dependency
category: structure
summary: "A method of class A calls class B and a method of B calls back into A's concrete type, so neither can be built or tested without the other."
tags: [rule, coupling, dependency-direction, testability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell lists circular dependency as a subtler barrier to [[information-hiding]]: a method of class A calls a method of class B, and a method of B calls one of A (p. 92).

## Rule

«Избегайте таких зависимостей» (p. 92). The book's reason is testing: neither class can be tested until at least part of the other is implemented (p. 92). This wiki adds the reading for information hiding: two classes in a cycle cannot keep secrets from each other, since each must know enough of the other to call it, so in effect they are one module with two names.

## Sign in code

- Class A references class B, and B references A's concrete type.
- A passes `this` to B, and B calls back methods of A's concrete type.
- A cycle through three or more classes, each calling the next (this wiki's extension of the book's two-class case).

Cycles between modules or packages follow the project's architecture and are out of this wiki's scope; this page covers classes and their calls.

## When not to apply

- The callback goes through an interface owned by B (B defines `Listener`, A implements it): B's code then depends on its own abstraction, not on A. This wiki reads that as the usual repair, not a violation.
- Two types that are deliberately one unit, in the same file or package and never tested apart (a node and its tree's internal iterator), cost the book's price only nominally. This wiki's judgement, not the book's.

## Repair

Break the cycle in one of three ways: move the part both need into a third class both depend on; have the lower module declare an interface for what it calls back, and let the upper one implement it; or merge the two if they are really one responsibility.

## Before and after

```
class Order
    function total()
        return pricing.priceFor(this)

class Pricing
    function priceFor(order: Order)
        return sum(order.lines) - order.customer.discount()
    function onRateChange()
        for o in openOrders: o.recalculate()    -- calls back into Order
```

```
interface RateListener               -- declared by Pricing
    function onRateChange()

class Pricing
    listeners: list of RateListener
    function priceFor(lines, discount)
        return sum(lines) - discount
    function rateChanged()
        for l in listeners: l.onRateChange()

class Order implements RateListener  -- registers with pricing
    function total()
        return pricing.priceFor(lines, customer.discount())
    function onRateChange()
        recalculate()
```

## Source

[[code-complete]], section 5.3, Russian edition, p. 92. The rule and the testing reason are the book's; the information-hiding reading, the signs beyond two classes, the scope note on module cycles, the limits, the repairs and the pseudocode are this wiki's own.
