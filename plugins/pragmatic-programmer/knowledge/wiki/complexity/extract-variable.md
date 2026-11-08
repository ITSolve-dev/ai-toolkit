---
title: Extract Variable or a function, and Inline Variable
category: complexity
summary: "One return or assignment combines several unnamed sub-calculations with operators and constants, often under a comment spelling out the formula (price is base price - discount + shipping): name the parts with immutable locals, or with methods when the parts are built from an object's own fields; the other way, a local assigned once and read once whose name says no more than its expression."
tags: [decision-rule, expressions, naming, refactoring, readability]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Extract Variable** (formerly Introduce Explaining Variable) names part of a complex expression by assigning it to a local. **Inline Variable** (formerly Inline Temp) is its inverse. Fowler adds a decision to the extraction: once a part deserves a name, how far should the name reach, and should it be a variable or a function (*Refactoring*, 2nd ed., ch. 6, PDF pp. 135-141).

## Rule

Local variables "give me an ability to name a part of a more complex piece of logic" (PDF p. 136). They also give a debugger or a print statement a place to attach (PDF p. 136).

The decision (PDF p. 136):

- The name means something **only inside the current function**: Extract Variable.
- The name **makes sense in a broader context**: make it a function, so other code can use it without repeating the expression. Inside a class this is cheap, so Fowler does it at once. Where it is a lot of work, he leaves the variable and promotes it later with Replace Temp with Query ([[replace-temp-with-query]]).

Inside a class, Fowler calls the shared names "one of the great benefits of objects": every part of the calculation becomes available to any code that works with the object (PDF p. 140).

The inverse: inline a variable when "the name doesn’t really communicate more than the expression itself", or when the variable gets in the way of refactoring the code around it (PDF p. 140).

## Sign in code

- A single return or assignment that combines several sub-calculations with operators and constants, none of them named, often with a comment that spells out the formula (`// price is base price - quantity discount + shipping`).
- Inside a class, such an expression built only from the object's own fields. This wiki reads that as the sign that the names belong to the object: the repair is a method, not a local.
- For the inverse: `x = a.b` followed by a single read of `x`, where `x` is no clearer than `a.b`.

This wiki assigns the neighbouring cases as follows. A single expression that combines several sub-calculations, none written twice, is [[extract-variable]]; an identical subexpression written two or more times is [[name-repeated-subexpression]]; a chain of field hops or dereferences is [[explaining-variable]]. A compound boolean condition is [[name-complex-conditions]]. A local that blocks the split of a long function, or a derivation repeated in locals of several methods, is [[replace-temp-with-query]]. A name like `temp` or `x` on an intermediate value is [[temporary-variable-names]].

## When not to apply

- **The expression has side effects.** Both directions require it to be free of them (PDF pp. 136, 140). This wiki gives the reason: naming the expression moves the point where it is evaluated, and inlining a variable read twice repeats the effect.
- **The variable is assigned more than once.** Inline Variable assumes a single assignment; Fowler checks it by declaring the variable immutable first and testing (PDF p. 140).
- **Promotion costs too much now.** A function would be better, but where making it is a lot of work a local is an acceptable interim step (PDF p. 136).
- **A short expression that already reads as its meaning** (`total - discount`). This limit is this wiki's own: a name adds a line and no meaning.

## Repair

Extract Variable (PDF p. 136): check that the expression has no side effects; declare an *immutable* variable set to a copy of the expression; replace the expression with the variable and test; replace further occurrences one at a time, testing after each. When the last part of a formula has a name, delete the comment that described it, because it "no longer says anything the code doesn’t say" (PDF p. 138).

Inside a class: extract each part as a method instead, following the same order.

Inline Variable (PDF p. 140): check the right-hand side has no side effects; declare the variable immutable and test; replace references one at a time and test; remove the declaration.

## Before and after

```
function price(order)
    // price is base price - quantity discount + shipping
    return order.quantity * order.itemPrice
         - max(0, order.quantity - 500) * order.itemPrice * 0.05
         + min(order.weight * SHIPPING_RATE, 100)
```

```
function price(order)
    basePrice        = order.quantity * order.itemPrice
    quantityDiscount = max(0, order.quantity - 500) * order.itemPrice * 0.05
    shipping         = min(order.weight * SHIPPING_RATE, 100)
    return basePrice - quantityDiscount + shipping
```

The same calculation inside a class, where the names belong to the object:

```
class Order
    price()            = basePrice() - quantityDiscount() + shipping()
    basePrice()        = quantity * itemPrice
    quantityDiscount() = max(0, quantity - 500) * itemPrice * 0.05
    shipping()         = min(weight * SHIPPING_RATE, 100)
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Extract Variable" and "Inline Variable", PDF pp. 135-141: the variable-or-function decision, the debugger remark, the benefit of objects, the side-effect and single-assignment checks, the immutable declaration, the comment removal and the reasons to inline. This wiki's own: the signs, the reading of the class case as a signal for a method, the reason given for the side-effect limit, the short-expression limit, the assignments against neighbouring pages, and the pseudocode.
