---
title: Replace subclass with delegate
category: objects
summary: "Subclasses that cover one axis of variation while a second axis is needed (combination subclasses such as YoungWealthy), or code that rebuilds an object as another subclass to change its kind at run time (copying fields into a new PremiumX and re-pointing references); move the varying behaviour into a delegate held by a field."
tags: [rule, inheritance, delegation, composition, state, strategy, refactoring]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Replace Subclass with Delegate moves the behaviour that a subclass adds or overrides into a separate object that the former superclass holds in a field and calls ([[fowler-refactoring]], ch. 12, PDF pp. 424-447). Fowler links it to the Gang of Four's State and Strategy patterns: both rely on the host delegating to a separate hierarchy (PDF p. 425). See [[strategy-for-varying-algorithms]].

## Rule

Inheritance is the natural way to express behaviour that varies by category, and Fowler uses it first. He names two downsides that justify replacing it with delegation:

- **One axis only.** Inheritance is "a card that can only be played once" (PDF p. 424). If people vary by age category and by income level, there can be subclasses for one axis, not for both.
- **Close coupling.** "Any change I want to make to the parent can easily break children" (PDF p. 425). This gets worse when parent and child live in different modules owned by different teams. See [[inheritance-weakens-encapsulation]].

In the worked example a third reason drives the change: the object has to switch kind at run time, by a method such as `aBooking.bePremium()`. This matters when the object is referred to from many places and cannot simply be rebuilt (PDF p. 429).

A second reason to subclass that would cut across the existing subclasses (wild against captive birds in Fowler's example, PDF p. 437) can be read only from a stated requirement, not from the code. This wiki therefore raises no finding for it without such a requirement; with one, the downside of one axis applies.

Fowler does not read "Favor object composition over class inheritance" as inheritance considered harmful. He uses inheritance often, partly because he knows he can apply this refactoring later, reaches for it first, "and move onto delegation when it starts to rub badly" (PDF p. 425). He closes the section by restating the slogan as "Favor a judicious mixture of composition and inheritance over either alone" (PDF p. 447).

## Sign in code

- **Combination subclasses:** classes named for pairs of values on two axes (`YoungWealthy`, `YoungPoor`, `SeniorWealthy`), or the same override repeated across subclasses that differ on the other axis.
- **Kind changed by rebuilding:** code that changes an object's kind by building an instance of another subclass, copying the old fields across and re-pointing the references to it. A type-code field next to the subclasses, which callers set to switch behaviour, is the same sign.

This wiki assigns the neighbouring shapes as follows. A switch over a type code with no subclasses yet is [[polymorphism-or-type-switch]]. A type code with no subclasses yet, whose value changes during the object's life, is [[replace-type-code-with-subclasses]] (indirect form); subclasses that already exist, where the object must change kind at run time, are [[replace-subclass-with-delegate]]. A context class that branches over a policy setting is [[strategy-for-varying-algorithms]]. An explicit class check on the delegate (`if delegate is ParrotDelegate`) is [[avoid-introspection-and-casting]]; Fowler says of it, "It’s almost never a good idea to use an explicit class check like this" (PDF p. 443). An `extends` clause with none of the signs above is classified on [[choose-an-alternative-to-inheritance]].

## When not to apply

- Neither downside bites: one axis of variation, no change of kind at run time, parent and children kept together. Fowler is explicit: "This is one of those refactorings where I don’t feel that refactoring alone improves the code. Inheritance handles this situation very well, whereas using delegation involves adding dispatch logic, two-way references, and thus extra complexity" (PDF pp. 435-436). The change pays only when run-time switching or freeing inheritance for another purpose outweighs that cost (PDF p. 436).
- Inheritance that already works stays, provided there are good tests to catch a subclass broken by a change to its parent (PDF p. 429).
- The sources disagree. [[choose-an-alternative-to-inheritance]] reports *The Pragmatic Programmer*'s stance against inheritance, while Fowler uses inheritance first. This wiki resolves it per setting: where the hierarchy is inside one module and has one axis, Fowler's default holds and no finding is raised. Where a downside named above shows in the code, both books call for delegation.
- A rebuilt object is fine where replacing it is natural, as when a new HTTP response replaces the old data (PDF p. 429).

## Repair

Fowler's mechanics (PDF pp. 425-426):

1. If the subclass constructors have many callers, put them behind factory functions first ([[factory-function-over-constructor]]).
2. Create an empty delegate class. Its constructor takes the subclass-only data and, usually, a back-reference to the host.
3. Add a delegate field to the host. Set it in the factory function, or in the constructor if the constructor can tell reliably which delegate to create.
4. Move the subclass methods to the delegate one at a time. Route access to host data through the back-reference. In the host method, dispatch to the delegate when it is present.
5. When the subclass is empty, make the factory return the host, and delete the subclass.

Three details from the worked examples:

- **The call to super.** A subclass method that extends the parent's version cannot become `host.basePrice()` inside the delegate, because that dispatches straight back to the delegate and recurses forever. Either extract the base calculation into a private host method that the delegate calls, or turn the delegate method into an extension hook (`extendBasePrice(base)`) that the host calls with its own result. Fowler slightly prefers the hook, "as it’s a bit smaller" (PDF p. 434).
- **A method that only one variant has.** Forcing the default into every delegate duplicates it. Fowler's cure is, in his word, "naturally", inheritance: extract a superclass of the delegates, holding the defaults and the back-reference (PDF p. 444).
- **No null delegate.** Once that delegate superclass exists, the host always holds a delegate (the default kind when no variant applies). The host methods become plain one-line calls with no guard, and which behaviour varies with the variant is visible at a glance (PDF pp. 444-445). The remaining delegate hierarchy is more tightly scoped, covering just the data and functions that vary with that axis (PDF p. 446).

## Before and after

```
class Ticket
    field event
    method price(): return event.price
    method canRefund(): return daysToEvent() > 7

class VipTicket extends Ticket
    field perks
    method price(): return super.price() + perks.fee
    method canRefund(): return true

-- upgrade: rebuild the object and re-point every reference to it
upgraded = new VipTicket(old.event, perks)
replaceEverywhere(old, upgraded)
```

```
class Ticket
    field event
    field tier = new StandardTier(this)
    method upgrade(perks): tier = new VipTier(this, perks)
    method basePrice(): return event.price
    method price(): return tier.extendPrice(basePrice())
    method canRefund(): return tier.canRefund()

class StandardTier
    field ticket
    method extendPrice(base): return base
    method canRefund(): return ticket.daysToEvent() > 7

class VipTier extends StandardTier
    field perks
    method extendPrice(base): return base + perks.fee
    method canRefund(): return true
```

In the "after", the kind changes in place, there are no copied fields or re-pointed references, and no host method checks for a null delegate or tests a class. The "before" would fall within this page's limits only if upgrading at run time were not required, and here it is.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed. (Addison-Wesley, 2018), ch. 12, Replace Subclass with Delegate, PDF pp. 424-447: the two downsides of inheritance, the reading of the GoF principle, State and Strategy, the mechanics, the Booking example (run-time switch to premium, the super-call wrinkle and both fixes, the method present only on the subclass, the verdict that the refactoring alone does not improve the code), and the Bird example (several subclasses, the class-check smell, the delegate superclass, the default delegate, the tighter scope, the restated slogan). This wiki's own: the signs as worded (combination subclasses, rebuilding to change kind, the type-code field), the reading of a second reason to subclass as needing a stated requirement, the owner assignments, the per-setting resolution against [[choose-an-alternative-to-inheritance]], and the Ticket pseudocode.
