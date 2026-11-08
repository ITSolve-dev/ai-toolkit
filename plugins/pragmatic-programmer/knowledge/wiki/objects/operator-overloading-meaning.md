---
title: An overloaded operator keeps the meaning readers expect
category: objects
summary: "An operator overload whose body departs from what the symbol means for values of that kind: + that removes or subtracts, an operator that mutates its operand where the built-in one returns a new value, or an arithmetic overload that combines mismatched units without a check."
tags: [rule, operator-overloading, interfaces, least-surprise]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Some languages let a class redefine operators. Weisfeld shows the accepted uses, `+` for joining strings and for adding matrices, then the extreme case: nothing stops `+` being made to subtract, so that `5 + 6` yields -1 (ch. 3, pp. 83-84). Overloading is powerful, but «он может откровенно сбивать с толку тех, кто читает и сопровождает код» (p. 83). He notes that Java, .NET and Objective-C do not allow it, apart from `+` for strings; Java's designers, he supposes, judged it not worth the cost (p. 84). [[coupling-hidden-in-language-features]] lists operator overloading among the features whose coupling does not show at the call site.

## Rule

The book's instruction: if you overload operators, «позаботьтесь о соответствующем документировании и комментировании, чтобы люди, которые будут использовать ваш класс, не запутались» (p. 84). This wiki reads it more strictly: an overload is justified only when it carries the operator's established meaning for the type, as matrix `+` does. This wiki holds that documentation cannot rescue an operator that means something else, because a reader at the call site sees the symbol, not the comment; a named method is the repair.

## Sign in code

- An operator overload whose body does something other than the symbol's conventional meaning for values of that kind: `+` that removes, `<<` used to register a listener.
- An overloaded operator that changes one of its operands where the built-in operator returns a new value.
- An arithmetic operator overloaded on a type with units that combines mismatched units without a check.

This wiki assigns the neighbouring cases as follows. Which fields an equality compares, whether written as a method or as an overloaded `==`, is [[object-equality]]; an overloaded operator whose effect departs from what the symbol means (removing, mutating, registering) is [[operator-overloading-meaning]].

## When not to apply

- Mathematical and value types where the operator's meaning carries over directly: vectors, matrices, money, durations.
- Conventions the language or the project fixes, such as `+` for strings, or `<<` for streams where that is the language's idiom. The project's convention decides.

## Repair

Replace the surprising overload with a method whose name states the operation (`merge`, `subscribe`, `withoutItem`). Keep the operator only where its usual meaning carries over, and document what it does with edge cases.

## Before and after

```
class Inventory
  operator +(item)
    items.remove(item)     // "+" takes the item out, in place
    return this

stock = stock + returnedItem
```

```
class Inventory
  method withoutItem(item)
    return new Inventory(items minus item)

stock = stock.withoutItem(returnedItem)
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 3, pp. 83-84, via [[object-oriented-thought-process]]: the string and matrix examples, `+` turned into subtraction, the warning about confusion, what Java, .NET and Objective-C chose, and the advice to document. This wiki's own: the stricter reading that documentation does not excuse a changed meaning and its reasoning, the signs, the owner split, the limits, the repair to a named method and the pseudocode.
