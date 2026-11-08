---
title: Delegate to services
category: objects
summary: "A class extending a framework, persistence or project base class, exposing that class's whole API to its callers while it and they use only a few of its methods (inherited by accident, not is-a); save or query methods on a domain class where the project's convention keeps persistence out of domain classes."
tags: [rule, delegation, composition, inheritance, encapsulation, refused-bequest]
paradigm: oop
sources: [pragmatic-programmer, code-complete, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

When a class needs another's abilities, it should hold a reference and forward, not inherit. Inheritance leads to classes with many methods: a parent has 20, the subclass wants two, and the other 18 stay callable on its objects. The book says such a class «потерял контроль над своим интерфейсом» (p. 204). Frameworks for persistence and user interfaces make this common by requiring components to subclass a base class they supply (p. 204). That demand is one form of [[framework-intrusion]].

## Rule

Delegate work to services, because «отношение СОДЕРЖИТ превосходит отношение ЯВЛЯЕТСЯ» (p. 205). The class keeps a service object and offers only the operations it chooses. Nothing of the service's API reaches its clients, and it can define a new API of its own (p. 204).

The book notes that a wrapper interface could also be written on top of an inherited class, but the inherited API can still be used to go around it. Delegation removes that risk (p. 204).

It then takes the idea further by asking why the class should know how to save itself at all, and whether it must know the business rules. It splits a data class from a record class that wraps it with fetching and saving (p. 205). This wiki reads that split as the book's example, not as a prescription: where persistence lives is a choice of the module's shape, which this wiki takes from the project's convention.

Its data class holds «ничего, кроме сведений об учетной записи» (p. 205), while on p. 170 it faults an object that only holds fields anyone may update. This wiki resolves the two by setting: the split moves storage out, and rules that guard an invariant of the class's fields stay on it, as [[tell-dont-ask]] requires. A class left with plain fields and no invariant is a plain record, which that page does not cover.

*Code Complete* gives the same repair as a pair of inverse refactorings, each with a sign. A subclass that uses only a small fraction of its ancestors' routines usually exists because the base class «по чистой случайности содержит нужные ему методы», not because the subclass is logically a descendant (p. 555). McConnell's repair changes is-a into has-a: make the former superclass a data member of the former subclass and expose only the routines it really needs (pp. 555-556), which also gives a class more control over another's interface (p. 563). Conversely, a class that exposes all the public routines of a member object might as well inherit from it (p. 563).

The two books disagree on that reverse direction: *The Pragmatic Programmer* says delegation should win (p. 205), *Code Complete* allows inheritance when every routine is forwarded. This wiki resolves it per setting. Forwarding everything is a case for inheritance only where the class is substitutable for the delegate in every use and the delegate's class is designed for extension ([[final-or-abstract]], [[inheritance-tax]]). Where the class is a decorator or an adapter that must stay substitutable for a different interface, or where the delegate is a framework or third-party class, keep delegation, because inheriting would expose the delegate's future methods too.

Fowler's *Refactoring* calls the shape **Refused Bequest**: subclasses inherit methods and data they may not want, and "pick just a few to play with" (2nd ed., ch. 3, Refused Bequest, PDF p. 98). He does not follow the traditional reading that the hierarchy is then wrong and every superclass should be abstract, "at least not all the time": the authors subclass to reuse a bit of behaviour all the time and find it a good way of doing business, and "Nine times out of ten this smell is too faint to be worth cleaning" (PDF p. 98). What raises it is refusing the interface rather than the implementation: "We don’t mind refusing implementations—but refusing interface gets us on our high horses" (PDF p. 98). In that case he does not adjust the hierarchy but replaces it with delegation.

## Sign in code

This wiki reads the sign as any of these:

- A class extends a framework base class, and callers invoke the base class's methods directly on it. This page owns that shape. Where the parent is the project's own class, it belongs to [[inheritance-tax]].
- The class and its callers use a few of the parent's public methods, and the rest remain callable on it; *Code Complete* states this sign for any parent, the project's own included (p. 555). For a project parent, a call through the subclass to a parent method is [[inheritance-tax]]; the unused rest of the parent's API is this page's second sign, judged only after a caller search. This wiki gives no verdict on this sign without one. A subclass using few parent methods but substitutable wherever the parent is expected is a legitimate subtype; the sign is accident, not count. This wiki assigns Fowler's strong form, a subclass that refuses the parent's interface, by its shape: an inherited public method overridden to throw or reject is [[liskov-substitution-principle]], and one overridden with an empty body is [[override-that-does-nothing]]. A subclass that reuses parent behaviour but is never used where the parent is expected is this page's first or second sign; Fowler's repair for it, Replace Superclass with Delegate (PDF p. 98), is this page's repair.
- Where the project's convention keeps persistence out of domain classes, save, load or query methods, or SQL, on a domain class are this page's sign; under an active-record convention they are the convention, not a finding. This page owns those methods on a class, and [[class-interface-coherent-abstraction]] defers them here. A free function that mixes a vendor's query dialect with business logic is [[hide-third-party-apis]]. The decision whether a responsibility stays with the class that owns the data or moves to a made-up class is [[pure-fabrication]], which supplies Larman's reasons for moving storage out; this page owns the storage methods on a domain class.

## When not to apply

The book states the cost plainly: «Теперь развязывание действительно достигнуто, хотя и не бесплатно» (p. 205). More code must be written, part of it boilerplate, and all record classes will probably need the same methods such as a finder (p. 205). The limits below are this wiki's own.

- The class should really offer nearly all the parent's interface. Forwarding then only adds lines, unless the point is to keep that interface under control.
- The framework gives no way to work through a delegate. The book's alternative assumes one exists. Keep the required subclass thin instead.
- In a small script with no second caller, the separation between a record and its data has nothing to protect.
- The class should be the parent's subtype in every use, and the parent is designed for extension; see the resolution above.
- The project's convention puts persistence on the domain class (active record, or a framework that requires it). Save and query methods there are the convention, and only the first two signs apply.
- **Refusing only implementation.** A subclass that simply does not use some inherited methods or fields, while it supports the parent's interface, is Fowler's faint form. He would act on it only when it causes confusion and problems, by creating a sibling and pushing the unused code down with Push Down Method and Push Down Field (PDF p. 98). This wiki reads that as: the second sign is reported as a question unless the inheritance is also by accident.

## Repair

1. Replace `extends` with a field holding the service.
2. Add forwarding methods for the operations clients really use, under names that fit the class.
3. Go through callers and see what breaks. Each break shows a piece of the parent's API that was in use.
4. If the project's convention keeps storage out of domain classes, split it into a data class and a record class (p. 205). Keep on the data class any rule that guards an invariant of its fields.
5. If the forwarding repeats across record classes, move it to [[mixins-share-functionality]].

Where a domain class inherits from a container and callers use the container's methods on it, the interface it leaks is owned by [[mixed-abstraction-levels-in-interface]]. A subclass that overrides parent methods to do nothing is [[override-that-does-nothing]], and one that throws 'not supported' is [[liskov-substitution-principle]]. Which alternative fits is decided on [[choose-an-alternative-to-inheritance]]. The coupling cost being avoided is on [[inheritance-tax]].

## Before and after

```
class Invoice extends EntityStore
    field lines

invoice.save()
invoice.delete_where(...)        -- reachable by any client
invoice.raw_query(...)
```

```
class Invoice
    field lines
    field store = EntityStore.for(self)

    method save(): store.save()

invoice.save()
```

A further split, when persistence should leave the class:

```
class Invoice
    field lines
    method add_line(line): ...       -- the rule on lines stays here

class InvoiceRecord
    field invoice
    field store
    method save(): store.save(invoice)
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 31, pp. 204-205, and p. 170 for the object that only holds fields. The rule, its reasoning, the record split and the stated cost are the book's. The resolution by setting, the signs and their assignment against [[hide-third-party-apis]], the limits, the reading of the record split as an example conditional on the project's convention, the active-record limit, the condition opening step 4, repair steps 2 and 3 and the second sentence of step 4 are this wiki's own. The pseudocode is this wiki's.

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]], section 24.2, pp. 555-556, and section 24.3, p. 563: the accident sign, the is-a to has-a refactoring and its reverse. The per-setting resolution of the reverse direction against *The Pragmatic Programmer*, the extension of the second sign to project parents, its split with [[inheritance-tax]] and the substitutability criterion are this wiki's own.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Refused Bequest", PDF p. 98: the smell, the qualified rejection of the traditional reading, the faint and the strong form, and the repairs. This wiki's own for that part: the routing of the strong form to [[liskov-substitution-principle]] and [[override-that-does-nothing]], reading the faint form as a question, and assigning the strong form without a throwing or empty override to this page's signs.
