---
title: Multiple inheritance only for mixins
category: objects
summary: "A class inherits implementation from two or more parents that are not small independent mixins (Displayable, Persistent, Sortable), or from mixins that depend on each other."
tags: [rule, inheritance, multiple-inheritance, mixins]
paradigm: oop
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell compares inheritance to a chainsaw and multiple inheritance to an old chainsaw with a faulty motor and no safety guard: occasionally useful, mostly best kept locked away (p. 145).

## Rule

In the author's experience multiple inheritance is useful mainly for mixins: simple classes that add a set of properties to another class, such as `Displayable`, `Persistent`, `Serializable` or `Sortable` (p. 145). Mixins are almost always abstract and are not instantiated on their own (p. 145). As long as the mixins are truly independent of each other, the classic diamond problem does not arise, and they make a design easier to understand: a reader grasps an object using `Displayable` and `Persistent` more easily than eleven more specific methods (p. 145). «Используйте множественное наследование, только тщательно рассмотрев все альтернативные варианты» (p. 145), weighing its effect on the system's complexity and comprehensibility. He notes Meyer (1997) argues for wide use of multiple inheritance; this page follows McConnell.

## Sign in code

- A class inheriting implementation from two or more parents, at least one of which is concrete or holds state.
- Two mixins of one class where one calls methods or reads state of the other.
- A member name reachable through two parents, resolved by the language's ordering rule.

This wiki assigns the neighbouring cases as follows. Repeated helper methods across siblings, to be gathered into a mixin, are [[mixins-share-functionality]]. The hidden coupling multiple inheritance adds in general is described on [[coupling-hidden-in-language-features]].

## When not to apply

- Inheriting several interfaces with no implementation. The book notes Java and Visual Basic allow multiple inheritance of interfaces only (p. 145); this wiki reads that as outside the warning.
- A language whose idiom for mixins is traits or modules that carry state, where the project convention uses them: the first sign then applies only to two concrete parents. This limit is this wiki's own.

## Repair

Keep one implementation parent and contain the others, or reduce the extra parents to independent stateless mixins.

## Before and after

```
class Invoice extends Document, DatabaseRecord   // both concrete, both have save()
```

```
class Invoice extends Document with Persistable  // Persistable: abstract, no state, independent
    store: RecordStore                           // contained
```

## Source

- [[code-complete]], p. 145: the metaphor, mixins, the diamond condition, the advice, Meyer's opposing view, the interface note.
- This wiki's own: the signs, the owner assignment, both limits (the first reads the book's interface note as a limit), the repair and the pseudocode.
