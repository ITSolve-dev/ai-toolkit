---
title: IDs to Objects
category: types-and-state
summary: "An identifier (customerId, itemId) entering from input is passed deeper through business methods as a bare number or string and looked up again in several of them, or logic about the thing is written as functions of its id; turn it into the object it names where it enters."
tags: [rule, ids-to-objects, primitive-obsession, information-expert]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Larman names this a common idiom of experienced object designers that has no pattern name: transform "keys and IDs for things into true objects". The transformation "often takes place shortly after an ID or key enters the domain layer ... from the UI layer", and he proposes the name "IDs to Objects" (26.8, p. 625). His examples are a `customerID` turned into a `Customer` by asking the `Store`, and an `itemID` turned into a `ProductDescription` (p. 625).

## Rule

Convert the identifier into the object it identifies once, where it enters, and pass the object onward. Larman's reason: a true object "encapsulates a set of information about the customer, and ... can have behavior", and it "frequently becomes beneficial and flexible as the design grows, even if the designer does not originally perceive a need for a true object" (p. 625). The lookup itself goes to the class that knows all instances, by Information Expert, here the `Store` (p. 625). See [[information-expert]].

## Sign in code

This wiki's reading of the sign:

- A method signature deep in the business code takes `customerId: int` or `itemId: string`, and its body begins by looking the entity up, while a caller on the same path has already looked it up or the id travels on to another lookup.
- The same id is looked up again in several methods along one call path.
- Logic about the thing (eligibility, discount category) is written as functions of the id rather than as methods of an object.

This wiki assigns the neighbouring cases as follows. A raw text value such as `"yes"` or `"42"` carried and compared as text is [[convert-input-at-entry]]; an identifier carried as a bare value and looked up repeatedly is [[ids-to-objects]]. An id a routine never reads and only hands on is [[tramp-data]]. Ids of two different entities sharing one primitive type, so one can be assigned to the other, is [[replace-primitive-with-class]]. Using a phone number or email as the key is [[externally-controlled-identifier]].

## When not to apply

- At a boundary where only the identifier crosses, such as a message to another process, a stored reference, or a reference between aggregates by id. Passing the id there is deliberate. This limit is this wiki's own; how aggregates refer to each other is domain modelling, which the charter gives to `domain-driven-guide`.
- The code only forwards the id and never uses the thing. Loading the object would cost a lookup for nothing. This limit is this wiki's own.
- Larman's reason is a forecast: the object "frequently becomes beneficial". This wiki does not let the sign depend on that forecast: it fires only where the code already looks the id up repeatedly or computes about the thing from its id.

## Repair

1. At the point where the id enters (a controller or the first business method that receives it), look up the object through the class that holds all of them.
2. Change the downstream signatures to take the object.
3. Move logic written as functions of the id onto the object.

## Before and after

```
class Register
  method enterCustomerForDiscount(customerId)
    sale.applyCustomerDiscount(customerId)

class Sale
  method applyCustomerDiscount(customerId)
    if customerRepo.find(customerId).isSenior() ...
    category = customerRepo.find(customerId).category
```

```
class Register
  method enterCustomerForDiscount(customerId)
    customer = store.getCustomer(customerId)
    sale.applyCustomerDiscount(customer)

class Sale
  method applyCustomerDiscount(customer)
    if customer.isSenior() ...
```

## Source

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.8, PDF p. 625. The idiom, its proposed name, where the conversion happens, the reason and the Store lookup are Larman's. The signs, the owner assignments, the limits and the pseudocode are this wiki's own.
