---
title: Reference or value for a nested object
category: objects
summary: "A holder's setter writes a field of a nested object only that holder refers to (this.phone.areaCode = x: make it a value), or every holder constructs its own copy of the same logical record from one id and some code then updates one copy (new Customer(data.customerId) per order: make it a shared reference)."
tags: [decision-rule, value-object, reference, immutability, equality]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler pairs **Change Reference to Value** and its inverse **Change Value to Reference**: a nested object can be treated as a reference, updated in place and shared, or as a value, replaced whole when anything in it changes (*Refactoring*, 2nd ed., ch. 9, PDF pp. 281-288).

## Rule

The deciding question is whether a change to the inner object must be seen by every holder.

- **No:** treat it as a value: immutable, replaced on change, compared by its fields. Fowler: value objects "are generally easier to reason about, particularly because they are immutable" (PDF pp. 281-282), and an immutable value can be passed out without worrying that it might change without the enclosing object being aware (p. 282). They are "especially useful in distributed and concurrent systems" (p. 282).
- **Yes:** treat it as a reference: one object per logical entity, obtained from a repository. With copies, "I then have to find all the copies and update them all. If I miss one, I'll get a troubling inconsistency in my data" (PDF p. 286).
- **Never updated:** both approaches are reasonable; memory from copies is, like any performance issue, relatively rare (PDF p. 285).

## Sign in code

Towards a value:

- The holder exposes setters that reach into the inner object (`set officeAreaCode(x) { this.phone.areaCode = x }`), and only that holder refers to it. Fowler's example arises from an Extract Class whose old parent still holds update methods for the new object (PDF p. 283).

Towards a reference:

- Each holder constructs its own instance from the same identifier (`this.customer = new Customer(data.customerId)` in every order), and some code updates or enriches one of those instances, so five orders for customer 123 give five customer objects that can diverge (PDF p. 287).

This wiki assigns the neighbouring cases as follows. A holder's setter that writes a field of a nested object only that holder refers to, and copies of one logical record built per holder from one id, are [[reference-or-value]]. Other fields reassigned after construction are [[immutable-objects]]. A function that writes fields of a plain record or element it received as an argument is [[do-not-mutate-input-data]]; a method that calls a mutator on an object it received, or a class whose fields are reassigned after construction, is [[immutable-objects]]. How a value class compares and hashes is [[object-equality]]. Copying versus sharing on assignment is [[prefer-deep-copy]].

## When not to apply

- Not towards a value when the object is meant to be shared so that any change to it is visible to all its collaborators (PDF p. 282).
- Not towards a value when the class cannot be made immutable: Fowler's first mechanical step is checking that it can (p. 282); reading that step as a limit is this wiki's.
- Not towards a reference when the data is never updated: copies are then harmless (p. 285).
- This wiki notes, as a setting rather than a prescription: whether a concept is an entity with identity in the business domain is decided by domain modelling, which is `domain-driven-guide`'s; this page judges only the code-level symptom of copies drifting or of setters reaching through.

## Repair

**Reference to value** (PDF pp. 282-285):

1. Make the inner class immutable: move field setting into the constructor and remove its setters (Remove Setting Method).
2. Turn each holder's delegating setter into a reassignment that builds a new inner object from the new field and the current others.
3. Give the class value-based equality over its fields, and override the hash function with it so hashed collections work ([[object-equality]]).
4. Test equality with two independently constructed objects; Fowler also recommends tests for non-equal values, other types and null (p. 285).

**Value to reference** (PDF pp. 286-288):

1. Create, or reuse, a repository that hands out one instance per id.
2. Change the holders' constructors to obtain the instance from it. Test after each.
3. If the repository is pre-populated, an unknown id becomes an error rather than a new object (p. 288).
4. Trade-off: a global repository couples the constructor to a global. Fowler: "like a powerful drug, they can be beneficial in small doses but a poison if used too much" (p. 288); pass the repository as a constructor parameter if that worries you (p. 288). See [[global-data]].

## Before and after

Towards a value:

```
class Person
  set officeAreaCode(code) -> this.phone.areaCode = code
class TelephoneNumber
  set areaCode(code) -> this.areaCode = code
```

```
class Person
  set officeAreaCode(code) -> this.phone = new TelephoneNumber(code, this.phone.number)
class TelephoneNumber
  constructor(areaCode, number)
  equals(other) -> other is TelephoneNumber and areaCode == other.areaCode and number == other.number
  hash()        -> hash(areaCode, number)
```

Towards a reference:

```
class Order
  constructor(data) -> this.customer = new Customer(data.customerId)
```

```
class Order
  constructor(data, customers) -> this.customer = customers.register(data.customerId)
```

## Source

Fowler, *Refactoring*, 2nd ed., ch. 9, Change Reference to Value and Change Value to Reference, PDF pp. 281-288 ([[fowler-refactoring]]). The deciding question, both signs as shown in the book's examples, the limits, the mechanics, the equality-test advice and the global-repository trade-off are the book's. The assignment against neighbouring pages, the domain-modelling boundary and the reading of the immutability check as a limit are this wiki's own. The pseudocode is this wiki's; passing the repository into the constructor in the second pair follows the book's suggestion rather than its listing.

Related: [[immutable-objects]], [[stored-derived-data]].
