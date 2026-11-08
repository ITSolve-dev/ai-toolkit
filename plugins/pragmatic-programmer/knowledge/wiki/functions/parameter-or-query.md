---
title: Pass a value or let the function find it
category: functions
summary: "A call passes a value the callee could compute from another of its parameters or from its own fields (order.discountedPrice(base, order.discountLevel)); or, the other way, a method meant to be referentially transparent reads a mutable object it reaches through a field, so the same call returns different results: move the value out of or into the parameter list."
tags: [decision-rule, parameters, referential-transparency, dependencies, replace-parameter-with-query, replace-query-with-parameter]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler gives a pair of inverse refactorings, **Replace Parameter with Query** and **Replace Query with Parameter** (*Refactoring*, 2nd ed., ch. 11, PDF pp. 362-370), and calls the choice between them a decision about the allocation of responsibility around the program that is "neither easy nor immutable" (PDF p. 367). This page is the test between them.

This wiki assigns the neighbouring cases as follows. A value the callee could derive from another of its parameters or from its own object is [[parameter-or-query]]; several values unpacked from one record and passed instead of the record is [[pass-what-the-routine-uses]]. A body that reaches a module-level name, static field, singleton or external resource is [[global-data]], whose repair is to pass the value in; this page supplies the stepwise mechanics for that repair.

## Rule

Fowler's premise: "The parameter list to a function should summarize the points of variability of that function" (PDF p. 363). A parameter whose value the function could determine for itself is a form of duplication and burdens the caller (PDF p. 363). The other way, a reference inside the body to something the function should not depend on is moved to a parameter, shifting to the caller the responsibility of resolving it (PDF p. 366).

The deciding questions, in Fowler's terms:

- **Is the responsibility appropriate in the body?** His habit is to simplify life for callers by moving work into the body, but only where that responsibility belongs there (PDF p. 363).
- **Would the query add an unwanted dependency?** That is the most common reason against Replace Parameter with Query: the body would have to reach a program element he would rather it stayed ignorant of, new or one he wants to remove (PDF p. 363).
- **Would referential transparency be lost or gained?** He would not replace a parameter with access to a mutable global (PDF p. 364); a function that reads a non-transparent element in its scope is itself not transparent, which a parameter fixes (PDF pp. 366-367).

The safest case for the query is a parameter derived from another parameter: "There’s rarely any point in passing two parameters if one can be determined from the other" (PDF p. 364).

## Sign in code

Toward a query (this page's sign):

- A call passes both an object, or the receiver, and a value computed from that same object (`order.discountedPrice(base, order.discountLevel)`, PDF p. 365).
- A call passes two values of which one is computed from the other at every call site.

Toward a parameter:

- A method of an otherwise immutable class reads a mutable object it reaches through a field or a captured reference, so that the same call on the same object can return different results. This sign as worded is this wiki's. Where what the body reaches is module-level or static (Fowler's `thermostat` in `HeatingPlan.targetTemperature`, PDF pp. 367-368), the finding is [[global-data]]'s.

## When not to apply

- Not a query when the value would come from a mutable global, or when reaching it adds a dependency the function should not have (PDF pp. 363-364).
- Not a query when callers pass a value that differs from the derivation on purpose (an override, a value from a different moment). This limit is this wiki's own.
- Not a parameter when the cost to callers outweighs the gain: the caller now has to figure out how to provide the value (PDF p. 367). Fowler says the tension between long repetitive parameter lists and coupling through shared scope is not something he "can reliably get right" (PDF p. 366), so the point is to be able to change it cheaply either way.

## Repair

Replace Parameter with Query (PDF p. 364): if needed, extract the parameter's calculation into a function; replace references to the parameter in the body with that expression, testing after each; remove the parameter with [[change-function-declaration]].

Replace Query with Parameter (PDF p. 367): Extract Variable on the query; Extract Function on the rest of the body under a searchable temporary name; inline the variable; inline the original function into its callers; rename the new function to the original name.

Fowler names the trade-off: after the second, the calling code looks more unwieldy than before, which is the price of the reduced coupling (PDF p. 370). The gain in his example is more than decoupling: on an immutable class the method became referentially transparent, and a class whose methods all are is much easier to test and reason about (PDF p. 370).

## Before and after

```
class Order
    discountLevel()
        return self.quantity > 100 ? 2 : 1
    discountedPrice(base, level)
        return level == 2 ? base * 0.90 : base * 0.95

total = order.discountedPrice(base, order.discountLevel())
```

```
class Order
    discountLevel()
        return self.quantity > 100 ? 2 : 1
    discountedPrice(base)
        return self.discountLevel() == 2 ? base * 0.90 : base * 0.95

total = order.discountedPrice(base)
```

## Source

- [[fowler-refactoring]], ch. 11, Replace Parameter with Query, PDF pp. 362-365, and Replace Query with Parameter, PDF pp. 366-370: the premise on parameter lists, the deciding questions, the safest case, referential transparency, both mechanics, the trade-off and the immutable-class gain.
- This wiki's own: arranging the two refactorings as one decision with three questions, the signs as worded, the routing of module-level reads to [[global-data]], the deliberate-override limit, and the pseudocode pair, after the book's order example.
