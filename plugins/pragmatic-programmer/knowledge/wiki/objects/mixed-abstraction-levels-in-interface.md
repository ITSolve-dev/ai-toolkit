---
title: Mixed abstraction levels in a class interface
category: objects
summary: "A class's public methods mix domain-level operations with operations of the container or library it is built on (`AddEmployee` beside `FirstItem`, `NextItemInList`), often because it inherits from the container or a wrapper re-exposes the whole wrapped API."
tags: [rule, abstraction, inheritance, encapsulation, class-interface]
paradigm: oop
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

## Rule

A class interface should present a consistent level of abstraction. McConnell's example is `EmployeeCensus`, which inherits from `ListContainer` and exposes both `AddEmployee`/`RemoveEmployee` (the employee level) and `NextItemInList`/`FirstItem`/`LastItem` (the list level). It thus represents two ADTs (pp. 131-132). Such mixtures arise when a programmer implements a class with a container or other library class and does not hide that fact. Whether the container is part of the abstraction is the question to ask. Usually it is an implementation detail to hide (p. 132).

The usual defence is that inheriting the container gives polymorphism with outside search or sort routines. McConnell answers that it fails the main test for inheritance: does the inheritance model only an "is a" relationship? An `EmployeeCensus` is not a `ListContainer`. If search or sort is part of its abstraction, those capabilities should be explicit, consistent parts of its own interface (pp. 132-133).

McConnell compares inconsistent public methods to cracks in a submarine hatch: water does not pour through as through an open hatch, but the boat sinks later. As the program changes, mixed levels make it less and less understandable (p. 133).

A related point from the same section: **know which abstraction the class implements.** McConnell's team needed a grid control but used a spreadsheet control, about 150 methods against 15, to get coloured cells. The wrapper written to hide the substitution faithfully exposed all 150 methods. It should have exposed the 15 grid methods plus one for colouring cells. Exposing all 150 risked having to support all of them after a few implementation changes (p. 133).

## Sign in code

- A domain class inherits from a collection, map or library base class, and callers use the inherited generic methods (`first`, `next`, `get(i)`, `put(k,v)`) as well as the domain ones.
- Public method names use two vocabularies: domain nouns (`Employee`) beside container or library nouns (`Item`, `Node`, `Row`, `List`).
- A wrapper or adapter class's public method list mirrors the wrapped container's or library's API one to one, including methods the project does not need, instead of the abstraction the wrapper was written to present.

This wiki assigns the neighbouring cases as follows. [[class-interface-coherent-abstraction]] owns classes that mix unrelated purposes; this page owns classes that mix levels of one purpose, domain and mechanism. A fragment where both the purposes and the vocabularies differ goes first to that page. Whether the `extends` clause itself should be inheritance at all is classified by [[choose-an-alternative-to-inheritance]]; this page owns the interface the inheritance leaks. A wrapper whose forwards mirror a container's or library's API, so its interface mixes that vocabulary with the domain's, is [[mixed-abstraction-levels-in-interface]]; a pure forwarder with no such leak is [[hide-delegate-or-remove-middle-man]].

## When not to apply

- The class really is a specialised container, with the "is a" relationship holding (a `SortedList` is a `List`), so the container operations are its abstraction. This limit is this wiki's application of the book's "is a" test.
- The language's collection protocols, such as iteration or indexing, are part of the house convention for every domain collection. Then a domain-named iteration over employees is the consistent level, while exposing the underlying container's own API is not. This limit is this wiki's own.
- A thin pass-through wrapper whose only job is to isolate a vendor dependency for later replacement may at first expose the API the project actually calls. Even then it should expose only those calls, not the whole vendor API. This limit is this wiki's own.

## Repair

1. Replace inheritance from the container with a private member of that type (composition).
2. Rename the needed container operations into the class's own vocabulary (`FirstEmployee`, `NextEmployee`).
3. Make any needed search or sort an explicit operation of the class.
4. For a wrapper, list the operations the callers need and expose only those.

## Before and after

```
// before
class EmployeeCensus extends ListContainer
  addEmployee(e); removeEmployee(e)
  // inherited: firstItem(), nextItemInList(), lastItem()
```

```
// after
class EmployeeCensus
  addEmployee(e); removeEmployee(e)
  firstEmployee(); nextEmployee(); lastEmployee()
  private employees: ListContainer
```

## Related

- [[storage-independent-names]]
- [[semantic-encapsulation-violation]]
- [[abstraction]]

## Source

[[code-complete]], ch. 6.2, Russian edition, pp. 131-133. The third sign, all three limits (the first applying the book's "is a" test), and the owner assignments are this wiki's own reasoning.
