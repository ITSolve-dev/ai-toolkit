---
title: Introduce Special Case (Null Object)
category: objects
summary: "Several clients compare one field to the same sentinel value (\"unknown\", null, an empty marker) and most give it the same answer (the same placeholder name, default plan or zero), or skip a write when it holds: move that answer into one special-case object with the normal interface."
tags: [rule, special-case, null-object, duplication, conditionals, polymorphism]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's *Refactoring* (2nd ed., ch. 10, PDF pp. 320-338) treats repeated checks for one special value as a form of duplicated code. When many users of a data structure test for one value and then mostly do the same thing, he moves that shared reaction into a single **special-case element** that answers like the normal one. The second edition renames the first edition's *Introduce Null Object*, because null is only one common special value: "Null Object is a special case of Special Case" (p. 321).

## Rule

If many parts of the code react the same way to one particular value of a field, put that reaction in one place: an object with the same interface as the normal value, which returns the common answers. Most special-case checks then become plain calls (pp. 320-321). Fowler names the trigger as the combination "widespread testing for a special case, plus a common response" (p. 323).

It takes three forms, chosen by what the clients do with the value (p. 321; examples pp. 329 and 333):

- **A class with methods** when clients need behaviour or write to the value.
- **A literal record** filled with the needed values when clients only read data.
- **A transform** that replaces the special value inside a record structure when the data arrives as plain records.

## Sign in code

- The same field is compared to the same sentinel (a magic string such as `"unknown"`, `null`, an empty marker) in several clients, each in its own `if` or ternary.
- In most of those places the branch taken on the sentinel gives the same default: the same placeholder name, the same default plan, zero.
- Writers guard a setter call with "if not special". That guard is the same reaction to the same value, applied to writes.

One comparison in one place is not the sign. The sign is that the comparison and its answer repeat across clients. This condition is this wiki's wording of Fowler's trigger.

This wiki assigns the neighbouring cases as follows. One sentinel value compared by several clients that mostly give it the same default answer is [[introduce-special-case]]. A method that returns a raw null for a not-found result is [[never-return-null]], which owns the return statement; where its callers repeat one default, this page supplies the replacement. The choice between a null object, an option type and an exception once null is gone is [[null-object-or-optional]]. An option type unwrapped with one default at several call sites is [[null-object-or-optional]]; a sentinel value (null, a magic string or number) compared at several clients is [[introduce-special-case]]. A special case tested in several functions of one calculation, where the case has behaviour of its own rather than a default, is [[polymorphism-or-type-switch]]. A field left null whose nullness decides what kind of object this is is [[null-field-hides-another-class]].

## When not to apply

- **The clients' responses differ.** The pattern pays off only when *most* clients do the same thing; where each client handles the special value differently, a special-case object has no common answer to hold. Fowler notes that among many clients there is always one that needs something different (p. 328). Such a client keeps an explicit check against the object's `isUnknown` property; that check is legitimate and is not a residue to remove (p. 329).
- **Absence is an error, not a case.** This wiki adds: if the special value means the program is in a bad state that should stop or be reported, a special-case object that returns defaults hides the failure. The repair is then a check at the boundary or an assertion ([[assert-the-impossible]], [[crash-early]]), not a quiet default.
- **Clients only read: a literal record is enough.** Fowler calls the class a fair bit of work for what is really a simple value (p. 329), and when clients only read he uses the literal form instead. He still usually prefers a class (p. 333).

## Repair

Fowler's mechanics (pp. 321-322), with the safety step that makes them incremental:

1. Add a special-case check property (`isUnknown`) to the normal subject, returning false.
2. Create the special-case object with only that property, returning true.
3. Extract the scattered comparison into a function (`isUnknown(x)`, [[extract-function]]) and move every client onto it, one at a time, testing after each; the general technique, with its trap for unexpected values, is [[extract-before-changing-many-callers]].
4. Make the container return the special-case object instead of the sentinel, either from its getter or by running the data through a transform.
5. Change the comparison function to use the check property, then test.
6. With Combine Functions into Class or Combine Functions into Transform, move each common response into the special-case object. Each client's conditional then becomes a plain access.
7. Inline the comparison function where a check is still needed ([[inline-function]]), and remove it once no caller remains ([[remove-dead-code]]).

Design points from the example:

- **Writes** that clients used to skip become a setter on the special case that does nothing: "I let the setter be called, but it does nothing" (p. 327).
- **Related objects** returned by a special case are usually special cases themselves (p. 328). An unknown customer returns a null payment history whose delinquency is 0, so clients never chain into the sentinel.
- **Immutability:** "Special-case objects are value objects, and thus should always be immutable, even if the objects they are substituting for are not" (p. 327). A literal should be frozen. Fowler still usually prefers a class (p. 333).
- **Inheritance is optional.** Fowler does not subclass `Customer` in JavaScript but says he would in statically typed languages (p. 324). This wiki leaves that choice to the project's language.

## Before and after

```
// before: four clients, same sentinel, mostly the same answer
customer = site.customer
name   = (customer == "unknown") ? "occupant" : customer.name
plan   = (customer == "unknown") ? plans.basic : customer.billingPlan
if customer != "unknown" then customer.billingPlan = newPlan
weeks  = (customer == "unknown") ? 0 : customer.paymentHistory.weeksDelinquent
```

```
// after
class UnknownCustomer
  isUnknown          -> true
  name               -> "occupant"
  billingPlan        -> plans.basic
  set billingPlan(p) -> ignore
  paymentHistory     -> NullPaymentHistory   // weeksDelinquent -> 0

Site.customer -> (raw == "unknown") ? UnknownCustomer() : raw

name  = customer.name
plan  = customer.billingPlan
customer.billingPlan = newPlan
weeks = customer.paymentHistory.weeksDelinquent

// the one client that differs keeps an explicit, legitimate check
label = customer.isUnknown ? "unknown occupant" : customer.name
```

The "after" compares to the sentinel in only one place, the container's getter. The remaining `isUnknown` check is the exception the limits allow.

## Source

Fowler, *Refactoring*, 2nd ed., ch. 10, "Introduce Special Case", PDF pp. 321-338 ([[fowler-refactoring]]): the motivation, the rename from Null Object, the three forms, the mechanics, the do-nothing setter, related special cases, immutability, the one divergent client and the class-versus-literal remark. This wiki's own: the "absence is an error" limit, the remark that one comparison alone is not the sign, the assignment against neighbouring pages and the pseudocode. Page numbers are from the `<!-- p. N -->` markers.
