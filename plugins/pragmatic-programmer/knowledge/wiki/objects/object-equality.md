---
title: Define how a class compares, instead of trusting the default
category: objects
summary: "A value-like class (meaning lies wholly in its fields) defines no equality while code compares instances with == or uses them in sets or as keys; an equality that compares sub-objects by reference where their contents matter; or an equality with no matching hash."
tags: [rule, equality, comparison, references, value-objects]
paradigm: any
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Comparing objects runs into the same problem as copying them. Comparing one reference with another, «вы сравните только ссылки, а не то, на что они указывают» (ch. 3, p. 85). To compare two objects properly the code has to follow their trees of references (p. 86). The copying side of the same problem is [[prefer-deep-copy]].

## Rule

Languages usually supply a default comparison, «Но, как это обычно бывает, не следует полагаться на такой механизм» (p. 86). When designing a class, the book says, consider giving it a comparison function that works the way you need (p. 86). Its class-design guidelines repeat the point for copying and comparison together: you may not want or be able to rely on a simple bitwise copy or comparison, so time goes into designing how the class's objects are copied and compared (ch. 5, p. 108).

This wiki adds the deciding question: does the class have identity, or is it defined by its value? Whether the concept is an entity or a value is the domain model's decision, made with the domain-driven-guide plugin; this page takes it as given and checks that the equality matches it. An object with identity (one account, one connection) may correctly compare by reference. An object that is its value (an amount of money, a date range) needs an equality over the fields that define it, and only those. This wiki's reasoning: with the default, two equal values are reported different, so a lookup in a set or map misses and a duplicate is stored.

## Sign in code

- A value-like class, whose meaning lies entirely in its fields, that defines no equality, while code compares its instances with `==` or puts them in sets or uses them as keys.
- An equality method that compares references of sub-objects where it should compare their contents.
- An equality defined without a matching hash, in a language whose hashed collections need both.

This wiki assigns the neighbouring cases as follows. A key mutated after insertion, or a hash computed from fields that can change, is [[mutable-hash-key]]. Which fields an equality compares, whether written as a method or as an overloaded `==`, is [[object-equality]]; an overloaded operator whose effect departs from what the symbol means (removing, mutating, registering) is [[operator-overloading-meaning]]. This page owns a class whose comparison is missing or compares the wrong things.

## When not to apply

- Objects whose identity is the point: entities, resources, services. Reference equality is correct there, and content equality would merge distinct things.
- Records or data classes for which the language already generates field-wise equality. The generated version still has to cover exactly the defining fields.
- Code that never compares or hashes the class: no comparison is owed until one is used.

## Repair

Decide whether the class is about identity or about value. For a value class, write an equality over the defining fields that compares sub-objects by content, recursively where needed, and keep hashing consistent with it.

## Before and after

```
class DateRange
  field start
  field end

a = new DateRange(d1, d2)
b = new DateRange(d1, d2)
if a == b          // false: different references
  ...
```

```
class DateRange
  field start
  field end
  method equals(other)
    return start equals other.start and end equals other.end
  method hash()
    return combine(hash(start), hash(end))

if a.equals(b)     // true
  ...
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 3, pp. 85-86, and ch. 5, p. 108, via [[object-oriented-thought-process]]: that comparing references is not comparing contents, that the default should not be trusted, and that a class should offer its own comparison. This wiki's own: the identity/value criterion and its reasoning, the signs (the hash sign included), the owner split, the limits, the repair and the pseudocode.
