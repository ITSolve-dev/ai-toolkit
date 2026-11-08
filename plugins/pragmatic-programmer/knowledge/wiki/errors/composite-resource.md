---
title: Composite resource
category: errors
summary: "Several acquisitions in a row followed by `if a and b`, or nested try/rescue with a give_back per resource, in the caller: partial acquisition leaks resources and the business logic disappears behind cleanup."
tags: [rule, concurrency, transactions, compensation]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

When an operation needs two resources, all-or-nothing has to be somebody's job. Leaving it to the caller buries the logic; giving it to either resource puts it in the wrong place. The book's answer is to treat the combination as a resource in its own right.

## Rule

The book's case adds ice cream to pie. The naive caller takes a slice and then finds no ice cream, and is left holding a slice no other customer can now get (p. 224). The compensating version nests error handling around each acquisition and gives resources back. The book's verdict: «Выяснить, что он действительно делает, не так-то просто, поскольку бизнес-логика скрывается в нем за служебными операциями.» (p. 224)

Moving the code into one of the two resources is rejected too (p. 225). This wiki's reason is that neither owns the pair. The book says to treat the combination «как отдельный ресурс» and move the code to a new module, so that the order either succeeds or fails: «выполнить его заказ либо удастся, либо не удастся» (p. 225).

A module per combination does not scale. The book expects each composite item to hold references to its components, with one generic method acquiring a resource for each reference (p. 225).

## Sign in code

The first two shapes come from the book's listings; the third is this wiki's own.

- Consecutive acquisitions from different resources, then a joint test, with no give-back when the test fails.
- Nested error handling with one give-back per acquired resource, wrapped around a single business call.
- Compensation only in the exception handler: the branch where a later resource is merely unavailable releases nothing.

## When not to apply

These limits are this wiki's own, except where cited.

- A partial result is useful, so there is nothing to undo.
- The resources sit behind one real transaction, such as one database. Use that transaction rather than a hand-written module.
- One combination with one caller may not justify a generic mechanism, though the book's concern runs the other way, against a module per combination (p. 225).

## Repair

1. Name the combination as a resource, with a method that either delivers everything or nothing.
2. Let composite items reference their components, and keep one generic acquiring method.
3. Reduce the caller to one call, and run the business action inside the composite's scope, so that a failure in the action also gives the parts back.

Steps 1 and 2 follow the book (p. 225). Step 3 is this wiki's own: the book's generic method stops at acquisition.

The compensation does not vanish. The book does not say how the new module achieves all-or-nothing; this wiki notes that the same give-back logic moves there, where it is at least in one place and apart from the business logic. If the module holds several locks at once, they need a consistent order, a point the chapter does not discuss. See [[resource-acquisition-order]].

## Before and after

```
seat = seats.reserve_if_free(flight)
if seat:
    try:
        meal = meals.reserve_if_available(flight)
        if meal:
            try:
                issue_ticket(seat, meal)
            on error:
                meals.release(meal)
                raise
        else:
            seats.release(seat)
    on error:
        seats.release(seat)
        raise
```

```
function with_all(components, flight, action):
    taken = []
    try:
        for component in components:
            part = component.take_if_available(flight)
            if not part:
                give_back(taken)
                return false
            taken.append(part)
        action(taken)
    on error:
        give_back(taken)
        raise
    return true

// caller
with_all(fare.components, flight, parts -> issue_ticket(parts))
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: the naive and compensating versions, p. 224; the separate resource and the generic method, p. 225.

This wiki's own: the reason neither resource can hold the code, the third shape under `## Sign in code`, the limits apart from the cited concern, step 3, and the note on where the compensation goes. The pseudocode is this wiki's own. Related: [[check-then-act-must-be-atomic]], [[lock-belongs-to-the-resource]].
