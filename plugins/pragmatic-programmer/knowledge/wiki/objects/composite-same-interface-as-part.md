---
title: "Composite: the group implements the part's interface"
category: objects
summary: "A client holds either one item or a list of the same type (one pricing strategy or several, a command or a macro) and branches on which it has, or several client methods loop over the same collection and fold its results by the same rule; make the group implement the same interface as the single item."
tags: [rule, composite, gof, polymorphism, protected-variations]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Composite is the GoF pattern for treating "a group or composition structure of objects the same way (polymorphically) as a non-composite (atomic) object". The solution is to "Define classes for composite and atomic objects so that they implement the same interface" (26.8, p. 619). Larman applies it to a sale that has several conflicting pricing strategies at once: a senior discount, a preferred-customer discount, a Monday discount and a product promotion.

## Rule

The composite holds a list of objects of the shared interface and implements that interface itself. Its operation combines the inner results by some rule. Larman calls this "a signature feature of a composite object: The outer composite object contains a list of inner objects, and both the outer and inner objects implement the same interface" (p. 620).

The effect on the client is that `Sale` "does not know or care if its pricing strategy is an atomic or composite strategy" (p. 620). The rule for resolving conflicts between strategies, best for the customer or highest price, becomes the composite's subclass. Larman notes that rule could change too (p. 618); this wiki reads it as a variation point of its own.

Two specifics from his design:

- An abstract `CompositePricingStrategy` holds the list and `add`, and each concrete composite, such as `CompositeBestForCustomerPricingStrategy`, implements only the combining rule, here the minimum of the inner totals (pp. 620-621).
- Start with a composite even when only one strategy applies, holding the current store policy (possibly 0%), so later strategies are just added as the scenario reveals them (p. 622).

The pattern is not specific to strategies. Larman names macro commands, commands containing commands, as a common use (p. 626). It is "based on Polymorphism and provides Protected Variations to a client so that it is not impacted if its related objects are atomic or composite" (p. 626). See [[strategy-for-varying-algorithms]] and [[protected-variations]].

## Sign in code

This wiki's reading of the sign:

- A client holds either a single object or a collection of the same type and branches on which it has (`if strategies.size() == 1`, `if x is List`).
- Several client methods each loop over the same collection and fold its results with the same rule (minimum, sum, any-invalid).
- A branch on a policy flag that picks the combining rule is [[strategy-for-varying-algorithms]]; this page owns the loop over several members of one interface.

This wiki assigns the neighbouring cases as follows. A wrapper that holds one object of the same interface and adds one behaviour is [[composable-decorators]]; a wrapper that holds a list of them and combines their results is [[composite-same-interface-as-part]]. A wrapper with the subject's interface that may skip the subject or send the call elsewhere (a cache hit, a failover, a refused permission) is [[proxy]]; one that always calls the subject and adds to what goes in or comes out is [[composable-decorators]].

## When not to apply

- The client really needs to tell the members apart, for example to show each discount separately on a receipt. Hiding the group behind one object removes information the client needs. This limit is this wiki's own.
- There is one place that combines the results and no tree or nesting. A loop in that one place is simpler than a composite class. This limit is this wiki's own.
- The members do not share an operation with the same meaning. Forcing a common interface on them produces methods that the composite or the leaves cannot implement properly ([[liskov-substitution-principle]]). This limit is this wiki's own.
- Larman's advice to start with a composite holding one strategy (p. 622) rests on his scenario already showing several strategies. Where nothing in the code or the brief names a second member, this wiki gives the decision to [[replaceable-code-over-forecast]].

## Repair

1. Make sure the single item has an interface. If not, extract one first.
2. Create a composite class that implements it, holds a list of it, and implements the operation by combining the inner results.
3. If there are several combining rules, make each its own composite subclass, or pass the rule in.
4. Give the client one reference of the interface type and delete its branching and loops.

## Before and after

```
class Sale
  field strategies: List<PricingStrategy>
  method getTotal()
    if strategies.isEmpty() return preDiscountTotal()
    lowest = MAX
    for s in strategies
      lowest = min(lowest, s.getTotal(this))
    return lowest
  method getSavings()
    if strategies.isEmpty() return 0
    lowest = MAX
    for s in strategies
      lowest = min(lowest, s.getTotal(this))
    return preDiscountTotal() - lowest
```

```
class BestForCustomerPricing implements PricingStrategy
  field inner: List<PricingStrategy>
  method add(s)  inner.add(s)
  method getTotal(sale)
    lowest = sale.preDiscountTotal()
    for s in inner
      lowest = min(lowest, s.getTotal(sale))
    return lowest

class Sale
  field pricing: PricingStrategy
  method getTotal()  return pricing.getTotal(this)
  method getSavings()  return preDiscountTotal() - pricing.getTotal(this)
```

## Source

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.8, PDF pp. 618-626. The problem, the solution, the signature feature, the abstract superclass, starting with a composite and the macro-command use are Larman's. The signs, the owner assignments, the limits (including the reading of starting with a composite) and the pseudocode are this wiki's own.
