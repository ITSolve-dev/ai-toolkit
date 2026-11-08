---
title: Avoid type casts
category: types-and-state
summary: "A value is forced from one type into another to get it past the type checker: read back from a generic store (void*, Object, any, an untyped map) and cast to its real type at the point of use, the same cast repeated at several call sites around one interface, or a reinterpretation that silences a reported type error."
tags: [rule, casting, type-checking, defensive-programming]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* tells C programmers «Избегайте преобразования типов» (p. 325) and gives a reason that is not specific to C. A cast stops the compiler checking whether the types match, which the book calls a hole in the armour of defensive programming. A program that needs many casts probably has a mismatch in its design, and the book asks for the design to be revisited before the casts are kept (p. 325). In the same place it advises explicit pointer types instead of a generic `void*` or `char*`: with a specific type the compiler can warn about mismatched types and bad conversions, and with a generic one it cannot (p. 325).

## Rule

Keep values in types the checker can verify. Redesign before adding casts. Where a conversion cannot be avoided, the book makes it explicit, as in its `(NODE_PTR) calloc(...)`, which shows what the memory is for (p. 325). Confining it to one place is this wiki's own addition.

## Sign in code

- A value passes through a generic type (`void*`, `Object`, `any`, an untyped map) and is cast back to its real type at the point of use.
- The same cast recurs at several call sites around one interface.
- A cast or reinterpretation silences a type error the checker reported.

This wiki assigns the neighbouring case as follows. A cast of a parameter to a narrower type than it is declared with, or a cast that follows a type test and makes a method behave differently by runtime type, is [[avoid-introspection-and-casting]]. A cast of a value read back from a generic store or interface, or a reinterpretation that only gets a value past the checker, is this page.

## When not to apply

The limits below are this wiki's own:

- A numeric conversion that is the actual operation (a rounding, a widening) is not a hole in the checking.
- Code at a boundary where the data arrives untyped (deserialisation, a foreign-function call, a memory allocator) has to assign a type somewhere. That one checked conversion is where it belongs; the sign is a cast repeated beyond it. See [[convert-input-at-entry]].

## Repair

1. Give the interface the specific type its users need, so that callers stop casting.
2. Where many casts cluster around one interface, treat it as the design mismatch the book describes and change the interface or the data's type.
3. Confine any remaining conversion to one function at the boundary, with a check.

## Before and after

```
function store(key, value: any)
function load(key): any

node = (Node) load("head")
count = (int) load("count")
```

```
record ListState { head: Node, count: int }

function store_state(state: ListState)
function load_state(): ListState

state = load_state()
node = state.head
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 13.2 ("Pointers in C"), p. 325: explicit pointer types instead of default ones, explicit conversion where needed, avoiding casts, and the cast as a hole in defensive programming that suggests a design mismatch. The book states this for C. Carrying it to other typed code is this wiki's own reading, as are the signs, the assignment against [[avoid-introspection-and-casting]], the limits, confining a conversion to one place, the repair steps and the pseudocode.
