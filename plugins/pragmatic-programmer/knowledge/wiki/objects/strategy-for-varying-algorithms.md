---
title: Strategy for varying algorithms or policies
category: objects
summary: "A method holds an if/switch chain over a policy setting (discount type, pricing rule, scoring mode), each arm computing the same result by a different algorithm with its own parameters stored on the context; give each variant its own class behind one interface held by the context."
tags: [rule, strategy, gof, polymorphism, protected-variations, conditional]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Strategy is the GoF pattern for a policy that comes in several related variants and changes over time. Larman's example is sale pricing: 10% off everything in one period, $10 off totals over $200 in another. His problem statement asks how to design for "varying, but related, algorithms or policies" and for "the ability to change these algorithms or policies"; the solution is to "Define each algorithm/policy/strategy in a separate class, with a common interface" (26.7, p. 613).

## Rule

- Each variant is a class implementing one interface, such as `ISalePricingStrategy.getTotal(sale)`.
- The **context** object, here `Sale`, holds a reference to its strategy and delegates part of its work to it (p. 614). The reference is declared as the interface, "so that any implementation of the interface can be bound to the attribute" (p. 615).
- The context passes itself to the strategy. Larman calls it common, and "usually required", that the context pass `this`, so the strategy can collaborate with it, for example to read the pre-discount total (p. 614). The decision this raises about passing a whole object is on [[pass-what-the-routine-uses]].
- Strategies are often created by a factory (p. 617), which can choose the class and read its parameters, such as the discount percentage, from an external store (pp. 615-616). See [[factory-object-for-creation]].

Larman sums it up: "Strategy builds on Polymorphism and interfaces to allow pluggable algorithms" and provides [[protected-variations]] with respect to changing algorithms (p. 617). Several strategies that apply at once are combined with [[composite-same-interface-as-part]].

## Sign in code

This wiki's reading of the sign:

- One method contains an `if`/`switch` chain over a policy kind (`discountType == "PERCENT"`, `"ABSOLUTE"`, `"SENIOR"`), each arm computing the same result differently.
- Variant-specific parameters (percentage, threshold, amount off) sit as fields on the context, and most of them are unused for any given variant.
- The same policy kind is tested again in other methods of the context.

This wiki assigns the neighbouring cases as follows. A branch whose key names what kind of thing the switched-on object is (a shape, a square, a transaction) is [[polymorphism-or-type-switch]]; a branch whose key names a policy the object applies to compute one result, with that policy's parameters stored as fields of the object, is [[strategy-for-varying-algorithms]]. A branch whose key names which third-party product is configured, its arms calling that product's own API, is [[hide-third-party-apis]]; a branch whose arms only choose which concrete class to instantiate is [[factory-object-for-creation]]. A branch whose arms differ only in the values they use is [[drive-repeated-dispatch-from-a-table]]. A strategy interface with one implementation is [[do-not-force-a-design-pattern]]. A switch over a control state that the object's own methods reassign is [[switch-on-state-vs-state-pattern]]; a switch over a type code fixed for the object's life is [[polymorphism-or-type-switch]].

## When not to apply

- There are two stable variants and no sign of more. A conditional is shorter and is read in one place. This limit is this wiki's own; Larman's case is a policy known to change often.
- The variants differ only in a number, such as a percentage. Then one class with a parameter is the strategy, and no hierarchy is needed. This wiki infers this from Larman's own design, where several of the four policies are "really just 'percentage discount' strategies" (26.8, p. 618).
- In code written in a functional style, a function value passed in plays the part of the strategy object. The rule holds, but the class hierarchy does not. This is this wiki's reading.

## Repair

1. Extract an interface for the varying computation, taking the context as a parameter.
2. Move each arm into a class implementing it, and move that variant's parameters into the class.
3. Give the context a field of the interface type, and replace the conditional with a delegating call.
4. Choose and create the strategy in a factory or at construction, not inside the context's method.

## Before and after

```
class Sale
  field discountType
  field percent
  field threshold
  field amountOff
  method getTotal()
    t = preDiscountTotal()
    if discountType == "PERCENT" return t * (1 - percent)
    if discountType == "ABSOLUTE" and t > threshold return t - amountOff
    return t
```

```
interface PricingStrategy
  method getTotal(sale)

class PercentDiscount implements PricingStrategy
  field percent
  method getTotal(sale)  return sale.preDiscountTotal() * (1 - percent)

class AbsoluteDiscountOverThreshold implements PricingStrategy
  field threshold
  field amountOff
  method getTotal(sale)
    t = sale.preDiscountTotal()
    return t > threshold ? t - amountOff : t

class Sale
  field pricing: PricingStrategy
  method getTotal()  return pricing.getTotal(this)
```

## Source

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.7, PDF pp. 613-617, and 26.8, PDF p. 618. The problem, the solution, the context passing `this`, the interface-typed reference and creation by factory are Larman's. The signs, the owner assignments, the limits and the pseudocode are this wiki's own, except that the second limit is inferred from his percentage-discount remark.
