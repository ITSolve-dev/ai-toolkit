---
title: Resource acquisition and release order
category: functions
summary: "Two code paths take the same locks or resources in different orders, or resources that refer to each other are released in the order they were acquired."
tags: [rule, resources, deadlock]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

When a routine holds more than one resource, the basic allocate-use-release pattern of [[finish-what-you-start]] needs two additions (p. 159).

## Rule

- Release resources in the opposite order to allocation, so nothing is left dangling when one resource holds references to another (p. 159).
- Where the same set of resources is allocated in different places, allocate them in the same order everywhere. This reduces the chance of deadlock: if process A holds resource 1 and wants resource 2 while process B holds 2 and wants 1, both wait forever (p. 159).

## Sign in code

- Two routines acquire the same pair of locks, files or connections in different orders.
- Acquiring by argument order, `lock(a); lock(b)`, so a call with swapped arguments reverses the order.
- A resource is released while a later-acquired one that refers to it is still open, such as closing a connection before the statement created from it.

## When not to apply

- This wiki infers from the book's reason, that nothing is left dangling (p. 159), that release order matters only where one resource refers to another, so independent resources may be released in any order. The book's wording carries no such condition.
- This wiki adds that a thread holding only one lock at a time has no ordering to keep.
- This wiki also notes that code which tries a lock and backs off on failure avoids the wait that the same-order rule prevents, at the cost of retry logic.

## Repair

Choose one global order, for example by a stable key, and acquire through a helper that applies it. Nest the scopes so that release order follows automatically.

## Before and after

```
# before
function transfer(from, to):
    from.mutex.protect:
        to.mutex.protect:
            move_funds(from, to)
```

```
# after
function transfer(from, to):
    first, second = ordered_by_id(from, to)
    first.mutex.protect:
        second.mutex.protect:
            move_funds(from, to)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: p. 159 for the rule and its reasoning. The second and third signs, the limits, the repair and the example are this wiki's own.
