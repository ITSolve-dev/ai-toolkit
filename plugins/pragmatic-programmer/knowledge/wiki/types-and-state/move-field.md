---
title: Move a field to the record that changes with it
category: types-and-state
summary: "A field of record B is passed alongside record A at every call (quote(contract, customer.discountRate)), or a method updating A also writes a field of B to keep them in step, or the same field is updated in several structures at once: move it to the one record it belongs with."
tags: [rule, data-structures, refactoring, encapsulation]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's Move Field moves a field from one record or class to another once it turns out to sit in the wrong place. He grounds it in the claim that "the strength of a program is really founded on its data structures" (*Refactoring*, 2nd ed., ch. 8, PDF p. 235). Poor structures produce code whose job is merely dealing with the poor data (p. 235), and blemishes left in place "will confuse my thinking and complicate my code far into the future" (p. 235).

## Rule

When a field belongs with another record, move it there, and change its users to reach it through the target (p. 236). Fowler expects initial data design to be wrong often, even with experience and with techniques such as domain-driven design: "A design decision that is reasonable and correct one week can become wrong in another" (p. 235).

## Sign in code

Fowler names three (p. 235):

- A field of one record is passed to a function every time another record is passed to it, as in `quote(contract, customer.discountRate)` at every call site.
- A change to one record forces a change to a field in another record. In code in front of the reader this shows as a method that updates record A and also writes a field of record B to keep the two in step; that wording is this wiki's. Without such a method the sign needs the change history.
- The same field is updated in several structures, so one logical update is several writes.

This wiki assigns the neighbouring cases as follows. A field that already lives in an existing record but always travels with one other record is [[move-field]]. Loose variables or parameters for which no structure exists yet are [[group-related-data-into-a-structure]]. Where callers read several fields of one existing object and the routine's job is about that object, [[pass-what-the-routine-uses]] owns the signature; where those fields form a value the source object does not model on its own (a range or a period held as two fields of a plan), [[group-related-data-into-a-structure]] owns it. A routine that takes the whole object but reads one field is [[pass-what-the-routine-uses]]. A field whose value can be computed from the record it would join is [[stored-derived-data]].

## When not to apply

- **The move changes behaviour.** Moving a per-instance field onto a shared object (account interest rate to account type) is a refactoring only if every instance already holds the value the shared object would give: "if there's an account with a different interest rate, it's no longer a refactoring" (p. 240). Check the data first, or run with an assertion or a log for a while (p. 240).
- This wiki adds: a record whose shape is fixed by an external schema or by the project's persistence mapping keeps its fields; the move then happens behind it, in the class that wraps the record.

## Repair

Before the steps: where the field's current uses block the move, Fowler first refactors those usage patterns, then moves (p. 236). A bare record with many direct readers and writers makes the move "decidedly more tricky", though still valuable (p. 239); his first step there is to encapsulate the record into a class ([[replace-direct-data-manipulation-with-adt]]), and for an immutable field he writes both fields and migrates the reads gradually (p. 239).

1. Encapsulate the source field behind accessors, then test.
2. Create the field and its accessors in the target.
3. Make sure the source can reach the target, through an existing field, a method or a new field (permanent or temporary).
4. Point the source accessors at the target field. If the target is shared, first make the setter write both and add an assertion that they agree ([[assert-the-impossible]]), then switch over. Test.
5. Remove the source field and test.

The accessors are what make this safe. Their clients keep working while the storage moves, which is why Fowler calls the refactoring easier with classes (p. 236). In his example the move failed at first because the constructor set the rate before it created the contract. He reverted, slid the statement below the construction ([[slide-statements]]) and redid the move (p. 238).

## Before and after

```
class Customer
  field name
  field discountRate
  field contract = new CustomerContract(today)

  becomePreferred(): discountRate = discountRate + 0.03
  applyDiscount(amount): return amount - amount * discountRate

// every renewal call, wherever a contract is in hand
function renew(contract, customer)
  return quote(contract, customer.discountRate)
```

```
class CustomerContract
  field startDate
  field discountRate

class Customer
  field name
  field contract

  discountRate(): return contract.discountRate
  setDiscountRate(r): contract.discountRate = r
  becomePreferred(): setDiscountRate(discountRate() + 0.03)
  applyDiscount(amount): return amount - amount * discountRate()

function renew(contract)
  return quote(contract)
```

## Source

Fowler, *Refactoring*, 2nd ed., ch. 8, Move Field, PDF pp. 235-241 ([[fowler-refactoring]]): the motivation, the three signs, the mechanics, the shared-object limit, the usage-pattern step and the bare-record procedure. This wiki's own parts are the code-visible wording of the second sign, the schema and persistence limit, the before/after pair (which adds the renewal call to show the first sign) and the assignment against neighbouring pages.
