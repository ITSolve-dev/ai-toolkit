---
title: Alternative classes with different interfaces
category: objects
summary: "Two classes that do the same job, used where one could stand in for the other, expose that job under different method names or parameter orders (sendMail(to, body) beside deliver(body, number)), so callers must know which one they hold."
tags: [rule, substitution, interfaces, polymorphism]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's **Alternative Classes with Different Interfaces**: one of the main benefits of classes is substitution, one class swapping in for another, "But this only works if their interfaces are the same" (ch. 3, Alternative Classes with Different Interfaces, PDF p. 97).

## Rule

Give interchangeable classes the same interface.

## Sign in code

Two classes used in the same role, such as values of one variable or field, or arguments to one routine, whose methods do the same thing under different names or parameter orders (`sendMail(to, body)` beside `deliver(body, number)`).

This wiki assigns the neighbouring cases as follows. A caller that tests the runtime type to pick which method to call is [[avoid-introspection-and-casting]]; where the types it tests do the same job under different method names, the repair is on [[alternative-classes-with-different-interfaces]], which owns the mismatched pair of classes. A switch on a type code repeated in several places is [[polymorphism-or-type-switch]].

## When not to apply

The source gives no limit. The limits below are this wiki's own.

- Classes that look alike but are not used in one role, because they serve different callers for different reasons, need no common interface. Forcing one is [[coincidental-duplication]] at the level of a type.
- Where either class belongs to a library the project does not own, it cannot be renamed: give both an adapter to one interface instead ([[hide-third-party-apis]]).

## Repair

1. Change Function Declaration to make the methods match.
2. If that is not enough, keep moving behaviour into the classes with Move Function until the protocols match.
3. If that leads to duplication, Extract Superclass (PDF p. 97). Where the language allows it, this wiki prefers a shared interface to a superclass when the classes share no implementation ([[prefer-interfaces-for-polymorphism]]).

## Before and after

```
class SmtpSender: method sendMail(to, body)
class SmsGateway: method deliver(body, number)

if channel is SmtpSender: channel.sendMail(addr, text)
else: channel.deliver(text, addr)
```

```
interface Notifier: method send(recipient, text)
class SmtpSender implements Notifier
class SmsGateway implements Notifier

channel.send(addr, text)
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 3, "Alternative Classes with Different Interfaces", PDF p. 97. The sign as worded, the assignments against neighbouring pages, both limits, the interface preference in step 3 and the pseudocode are this wiki's own.
