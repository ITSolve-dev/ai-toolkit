---
title: Limit fan-out
category: structure
summary: "A routine calls more than about seven distinct modules, classes or services, or a class's method bodies reach more than about seven collaborator types beyond the types of its fields."
tags: [rule, fan-out, fan-in, coupling, complexity]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Fan-out** is the number of other classes (or routines) a given class (or routine) uses. **Fan-in** is the number of others that use it. McConnell lists low-to-medium fan-out and high fan-in among the internal characteristics of a good design (p. 78).

## Rule

Keep fan-out low to medium. McConnell writes that high fan-out «(более семи) говорит о том, что класс использует большое число других классов и, возможно, слишком сложен» (p. 78). He cites research (Card and Glass 1990; Basili, Briand and Melo 1996) finding low fan-out beneficial both for the routines a routine calls and for those a class calls (p. 78, paraphrase). High fan-in is the complementary goal: many classes use a given low-level utility class, so the system makes good use of shared helpers (p. 78, paraphrase).

The class chapter returns to the same count. McConnell cites Basili, Briand and Melo (1996), in which «число дефектов в коде класса статистически коррелирует с общим числом методов, вызываемых классом» (p. 146), and in which defects also rose with the number of classes used (p. 146). He asks to minimise the number of different routines a class calls (p. 146), and in general to minimise a class's collaboration with other classes: the kinds of objects it creates, the methods it calls directly on them, and the calls on objects those return (p. 147). The last of these is owned by [[train-wreck]]. The same study found more methods per class correlated with more defects, but other factors weighed more: deep inheritance, many methods called from the class, strong coupling between classes (p. 146); this wiki reads that as advice to balance these factors rather than chase one.

## Sign in code

- A routine that calls more than about seven distinct other modules, classes or services.
- A class whose method bodies and created instances together reference more than about seven distinct collaborator types beyond the types of its fields.

The threshold of seven is the source's. Which references count is this wiki's reading: count the collaborators the reader has to understand to follow the code. Calls to standard-library primitives, value types (strings, dates, money, collections) and the class's own private helpers are not counted.

This wiki assigns the neighbouring cases as follows. A class with more fields than the threshold of [[keep-objects-small]] for its setting (four, or about seven) or a constructor with more than five parameters is [[keep-objects-small]], which owns those counts. The number of collaborators a routine calls, or a class's method bodies reach beyond its fields, is [[limit-fan-out]]. A class too long in lines is [[class-size]].

## When not to apply

These limits are this wiki's own; the source gives the threshold and no exceptions.

- **Composition roots and wiring code** (the main function, a dependency-injection module, a router table) exist to connect many parts. Their fan-out is their job, provided they hold no logic.
- **Thin coordinators**: a routine whose every line is one call to a step at one level of abstraction, with no branching and no data shaping between the calls, may exceed seven while staying easy to read; splitting it only scatters the sequence.
- A correlation is not a proof that fan-out causes defects. This wiki treats the count as a place to look, not a verdict.
- A facade or a mapper whose purpose is to present many collaborators as one has high fan-out by design, like the wiring code above.
- Fan-in is not to be raised by funnelling unrelated callers through one "utility" class. That trades fan-out for a low-cohesion grab bag.

## Repair

This wiki's own:

1. Group the collaborators by which steps use them. Clusters that serve one sub-task become a routine or class that owns those collaborators.
2. If several collaborators are always used together in the same order, put them behind one object that offers the combined operation.

## Before and after

```
function placeOrder(order)
    inventory.reserve(order); warehouseApi.schedule(order)
    total = pricing.base(order)
    total = taxRules.apply(order, total)
    total = discounts.apply(order, total)
    if fraudCheck.verify(order, total).suspicious then
        auditLog.write("fraud hold", order.id); return
    payments.charge(order, total)
    mailer.send(order.email, ...)
    if order.phone then smsSender.send(order.phone, ...)
    auditLog.write("order placed", order.id)
```

```
function placeOrder(order)
    stock.reserve(order)                        // inventory, warehouseApi
    receipt = checkout.charge(order)            // pricing, tax, discounts, fraud, payments
    notifications.orderPlaced(order, receipt)   // mailer, sms, audit
```

The "after" has a fan-out of three, and each new collaborator fans out to two to five others of one concern.

## Source

[[code-complete]], ch. 5, section 5.2, Russian edition, p. 78; ch. 6, pp. 146-147 (the defect study, minimising routines called and collaboration). The rule, the threshold of seven, fan-in and the research citation are the source's. The counting rules, the assignment of neighbouring cases, the limits (including the correlation and facade limits), the repair and the pair are this wiki's own. Related: [[managing-complexity]], [[coupling]].
