---
title: Choose an alternative to inheritance
category: objects
summary: "An extends clause to be classified: is the subclass passed where the parent is expected, does it call the parent's methods, or do sibling classes carry the same code?"
tags: [decision-rule, inheritance, interfaces, delegation, mixins]
paradigm: oop
sources: [pragmatic-programmer, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

The book offers three replacements for class inheritance: interfaces and protocols, delegation, and mixins and traits (p. 202, p. 207). It says each can fit better depending on the circumstances, and leaves the choice to the goal. This page turns that remark into a test to run on an `extends` clause.

## Rule

Choose by what the inheritance was doing. The book's criterion is the goal: exchanging type information, adding functionality, or using shared methods. Then, as everywhere in programming, «пользоваться той методикой, которая лучше всего выражает ваши намерения» (p. 207).

The book gives the three goals and the three techniques without pairing them. The pairing below is this wiki's reading, built from the book's three separate tips.

| The inheritance was doing this | Use | Page |
|---|---|---|
| Letting objects be used through one type | Interface | [[prefer-interfaces-for-polymorphism]] |
| Giving a class another class's ability | Delegation | [[delegate-to-services]] |
| Sharing the same methods among several classes | Mixin | [[mixins-share-functionality]] |

One inheritance can do more than one of these, and the answers then combine.

## Sign in code

This page has no defect sign of its own. This wiki does not take an `extends` clause on a concrete class as a finding alone, because it fits any subclass. It asks three questions of a clause that [[inheritance-tax]], [[delegate-to-services]] or [[prefer-interfaces-for-polymorphism]] has raised:

- Is a subclass instance passed to code typed by the parent, or stored in a collection of the parent type? That is the type use.
- Do the subclass's methods call parent methods to do their work, or do its callers use parent methods on it? That is the ability use.
- Do two or more subclasses, or classes outside the hierarchy, carry or call the same methods? That is the sharing use.

The first and third questions need a search of the callers and of the sibling classes, and this wiki gives no verdict on them without one.

An `extends` clause whose is-a sentence is false because the subclass is a whole and the parent one of its parts is [[containment-or-inheritance]]; one where the sentence is true, or where the parent is a framework class, is classified on [[choose-an-alternative-to-inheritance]] and [[delegate-to-services]]. A subclass whose fields identify one instance while its parent describes the kind is [[replace-superclass-with-delegate]]. Combination subclasses over two axes, or an object rebuilt as another subclass to change its kind at run time, are [[replace-subclass-with-delegate]]; Fowler, who uses inheritance first, and *The Pragmatic Programmer* are resolved per setting on those two pages ([[fowler-refactoring]], ch. 12).

## When not to apply

The book's wording runs from «вы не должны больше пользоваться наследованием» (p. 202) to a heading saying that inheritance is rarely the answer (p. 207), and it names no case for keeping it. The limits below are this wiki's own.

- When none of the three questions gets a yes, no replacement is called for. The clause may simply be unnecessary, and removing it is the repair.
- The cases listed on [[inheritance-tax]] under its own limits stand here too: a parent designed for extension, or one module owning both sides.
- The language lacks one of the three. The choice is then made from what the language has.
- Fowler, who reaches for inheritance first (*Refactoring*, ch. 12, PDF p. 418), keeps it where two conditions hold: every parent method applies to the child, and every child instance is a valid parent instance (PDF p. 448). This wiki resolves the disagreement by setting: in a project that uses inheritance, an `extends` clause meeting both conditions is kept, as on [[extract-superclass]]; in a project that prefers composition, the three questions decide.

## Repair

1. Answer the three questions for the `extends` clause.
2. Apply the technique for each yes.
3. Remove the `extends` once nothing depends on the parent type or its methods.

The book's prompt for this is to pause at the next subclass and ask whether interfaces, delegation or mixins would reach the goal, and whether that reduces coupling (p. 207).

## Before and after

```
class Notifier
    method deliver(msg): ...
    method log(msg): ...

class EmailNotifier extends Notifier      -- passed as Notifier: type use
    method send(msg):
        log(msg)                          -- called by both subclasses: sharing use
        deliver(msg)                      -- parent does its work: ability use

class SmsNotifier extends Notifier
    method send(msg):
        log(msg)
        gateway.push(msg)
```

```
interface Notifier
    method send(msg)

mixin Logged
    method log(msg): ...

class EmailNotifier implements Notifier with Logged
    field mailer                          -- ability held by delegation
    method send(msg):
        log(msg)
        mailer.deliver(msg)

class SmsNotifier implements Notifier with Logged
    method send(msg):
        log(msg)
        gateway.push(msg)
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 31, pp. 202, 207. The three alternatives, the goals and the criterion of expressing intent are the book's. The pairing of goals to techniques, the reading that a clause alone is no finding, the three questions, the limits and the repair steps are this wiki's own. The pseudocode is this wiki's. The sentence at p. 202 is reported as printed in the Russian edition and read literally.

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 12, Extract Superclass, PDF p. 418, and Replace Superclass with Delegate, PDF p. 448: inheritance tried first and the two conditions for keeping it; otherwise only the cross-reference to the delegate refactorings, whose per-setting resolution is on those pages. This wiki's own: the resolution by project setting in the last limit.
