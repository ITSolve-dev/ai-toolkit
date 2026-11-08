---
title: Avoid type introspection and casting
category: objects
summary: "`instanceof` / type checks or casts on a parameter make a method behave differently per runtime type, hiding a dependency on a second type that the signature does not show."
tags: [rule, instanceof, casting, coupling, interfaces, overloading]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-07
---

*Elegant Objects* (section 3.7) forbids checking an object's type at run time (`instanceof`, `Class.cast()` and their equivalents) and casting it to a narrower type. The book's example is a `size(Iterable)` that takes a shortcut when the argument happens to be a `Collection`, a move that looks like an optimisation and that the book calls repulsive (p. 195).

## Rule

Paraphrased from pp. 195-200:

- Branching on the runtime type treats objects differently by what they are instead of letting the object decide how to do what it was asked (p. 197).
- Technically, it raises coupling: the method depends on two types, `Iterable` and `Collection`, not one, and the second dependency is hidden. Nothing in the signature shows it, so to use the method efficiently a caller has to read its source to learn that a `Collection` is treated differently (p. 197).
- A cast is the same thing: it forces an object to obey a contract «под выполнением которого он не подписывался» (p. 197). The book's analogy: asking a plumber to fix the printer "if you happen to be a computer person too" builds an expectation that is in no contract, so the next supplier or the next employee breaks it (pp. 197-199). Such unwritten agreements damage maintainability (p. 199).
- The author extends the ban to every downcast and to casting `Object` to an interface (replies on p. 199).
- How an incoming object is treated «должно быть отражено в сигнатуре метода и нигде больше» (author's reply, p. 199): if a caller passes a `List` declared as `Iterable`, that is the caller's decision, and the method should not reach for `size()` behind it (p. 200).
- Reflection in general is called worse still, since code that can be modified by other code at run time is a nightmare to read, but the book sets it aside as not specifically about OOP (p. 195).

## Sign in code

- A type test on a parameter or field (`x instanceof T`, `type(x) == T`, `x is T`, a `switch` on a class name) followed by a branch that treats the types differently.
- A cast of a parameter to a narrower type than declared (`(Collection) items`), with or without a preceding type test.

This wiki assigns the neighbouring cases as follows. This page owns a branch or cast on the runtime type of an object. A cast of a parameter to a narrower type than it is declared with, or a cast that follows a type test and makes a method behave differently by runtime type, is this page; a cast of a value read back from a generic store or interface, or a reinterpretation that only gets a value past the checker, is [[avoid-type-casts]]. A branch whose key is an object's runtime type or class name is [[avoid-introspection-and-casting]], however many arms. A type test on a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]]; a type test on a class that has real behaviour of its own is [[avoid-introspection-and-casting]]. An explicit class check on a delegate (`if delegate is ParrotDelegate`), left over from [[replace-subclass-with-delegate]], is [[avoid-introspection-and-casting]]. [[drive-repeated-dispatch-from-a-table]] owns a branch over a data value. A base class that exists only so unrelated classes share a type is [[prefer-interfaces-for-polymorphism]]. A type test that only corrects or reinterprets the result of a base method, such as flipping its sign for one subtype, is [[liskov-substitution-principle]], whose repair is in the hierarchy. The cases of semantic coupling: a documented call the caller skips, or another class's constant it borrows, because it knows the implementation belongs to [[semantic-encapsulation-violation]]; a reliance on runtime type to [[avoid-introspection-and-casting]]; on shared mutable state to [[global-data]]; a reliance on what the callee does with a value the caller passes belongs to [[semantic-coupling]]. A caller that tests the runtime type to pick which method to call is [[avoid-introspection-and-casting]]; where the types it tests do the same job under different method names, the repair is on [[alternative-classes-with-different-interfaces]], which owns the mismatched pair of classes.

## When not to apply

The book allows no exceptions. The limits below are this wiki's own:

- **Closed sum types with exhaustive matching** (a tagged union, a sealed hierarchy matched by the compiler). The variants are part of the declared type, so the dependency is not hidden; this is the normal functional style and is a different shape from probing an open interface. The page is `paradigm: oop` for that reason.
- **Equality and similar language protocols** that receive an untyped argument by contract (`equals(Object)`), and **deserialization or input boundaries** where untyped data must be classified once. Keep the check at that single point.
- **The object arrives typed only by an interface the project does not own, and the caller cannot know the concrete type**, so neither overloading nor separate names can be chosen. Keep the test at that single point.

## Repair

1. Put each case in the signature: overload the method (`size(Collection)` and `size(Iterable)`), so the compiler chooses (p. 197). In a language without overloading, give the methods different names (`sizeOfIterable`, `sizeOfCollection`) and let the caller choose (p. 197).
2. Where you own the interface, add the operation to it so every implementation answers it uniformly, as a commenter proposes for `Iterable` itself (Ross William Drew, pp. 199-200); the author agrees it confirms his point (p. 199). This wiki prefers this repair where possible, because, as the commenter notes, overloads only move the `instanceof` choice up the call stack when callers hold the wider type (p. 200).
3. Remove a cast by declaring the parameter as the type you need.

## Before and after

```
size(items: Iterable) ->
  if items is Collection
    return (items as Collection).size()
  count = 0
  for each item in items: count = count + 1
  return count
```

```
size(items: Collection) -> return items.size()

size(items: Iterable) ->
  count = 0
  for each item in items: count = count + 1
  return count
```

The "before" probes an open interface, not a closed sum type, so the limits do not exempt it. The "after" has no type test and no cast; each dependency is in a signature.

## Source

- [[elegant-objects]], section 3.7, pp. 195-200: the `size` example and reflection aside (p. 195), discrimination by type and hidden coupling (p. 197), overloading and named methods (p. 197), casting as an unsigned contract and the plumber analogy (pp. 197-199), the author's replies on downcasts and the signature (p. 199), the commenter's counter-proposal (pp. 199-200). Quotations are transcribed from a noisy OCR layer and must be checked against the page image.
- This wiki's own: the signs' wording beyond the book's operators, the assignment of neighbouring cases, every item under *When not to apply*, the preference for repair 2, and the pseudocode pair.
