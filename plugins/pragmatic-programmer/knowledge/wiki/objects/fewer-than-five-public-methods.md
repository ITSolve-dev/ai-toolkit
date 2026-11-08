---
title: Fewer than five public methods
category: objects
summary: "A class exposing five or more public or protected methods (constructors and private methods not counted) is too large: check whether its fields split into groups used by disjoint sets of methods, and split it along that line."
tags: [rule, class-size, cohesion, interface]
paradigm: oop
sources: [elegant-objects, code-complete]
created: 2026-11-03
updated: 2026-11-06
---

Bugayenko measures the size of a class by the number of its public and protected methods, not by its line count, and puts the limit at fewer than five (*Elegant Objects*, section 3.1, p. 115). He gives two examples of why line count misleads: a 50-line class with 20 methods is not small, while a class with one public method and 20 private ones he would not call very large (p. 115).

The number is admittedly arbitrary. The author says there is no special reason for five, that the right number cannot be determined, and that it is not an absolute constant; its job is to make the reader feel that the upper bound exists and is low: «не десять, не двадцать, даже не семь» (p. 115; checked against the page image). The working instruction is to stop between the fourth and the fifth method and ask whether the class still has a single area of responsibility (pp. 115-116).

## Rule

Keep the number of public and protected methods of a class below five. Constructors and private methods do not count (p. 115). When a class reaches five, treat it as needing refactoring and check whether it still has one responsibility (pp. 115-116).

The book is inconsistent at exactly five: the title and p. 115 accept fewer than five and call for refactoring if there are more, while p. 116 says not to let the count exceed five. This wiki treats five as the point to stop and check (pp. 115-116), and more than five as the book's refactoring trigger.

The book argues four gains from a small public surface (p. 116):

- **Fewer mistakes.** Three methods are easier to keep consistent with each other than ten.
- **Maintainability.** Every public method is an entry point into the object, so fewer entry points make a problem easier to isolate.
- **Cohesion.** The book defines cohesion as every method using every property. If one property is used only by two methods and another only by three others, the class consists of two barely connected parts (p. 116). A small class is more likely to have every method touch every property.
- **Verifiability.** A class with one public method can be tested completely; with ten, the tests are either too large or never written (p. 116).

This wiki reads the cohesion argument as the actionable part: the count is a trigger to look, and the field-usage split is what tells you where to cut.

*Code Complete* sets no number for methods. McConnell advises keeping as few as possible per class, since a study found more methods per class meant more defects, though other factors outweighed it (p. 146).

## Sign in code

- A class declares five or more public or protected methods, constructors and accessors excluded.
- Stronger sign, from the book's cohesion definition: the fields of the class partition into groups, and each group is read or written only by its own subset of methods (p. 116).

This wiki assigns the neighbouring cases as follows. This page owns the count of public methods. A split of the fields into groups used by disjoint methods is owned by [[class-interface-coherent-abstraction]] at any method count; [[fewer-than-five-public-methods]] owns the count and applies that page's split. The number of fields and constructor parameters is [[keep-objects-small]]; the line count is [[class-size]]. A class over the line limit with five or more public methods is [[fewer-than-five-public-methods]]. A class over the line limit with fewer is [[class-size]], and this wiki reports it only where its private methods fall into groups over disjoint fields. Methods that only return or set one field are not counted by [[fewer-than-five-public-methods]]. A class whose public methods are only accessors over its fields is [[no-getters-and-setters]]. Methods in an interface that are derivable from its other methods are [[small-interface-with-smart-class]].

## When not to apply

The book itself says five is not absolute (p. 115). The following limits are this wiki's own reasoning, not the book's:

- A type whose purpose is a wide interface that cannot be split without breaking callers, such as an implementation of an interface imposed by a platform or library (a collection, a stream). The count then reflects the imposed interface, not the class's design. The interface itself may still be the problem, but the implementing class is not where to fix it.
- A class at five or six methods whose every method uses every field: the stronger sign is absent, and splitting would separate code that changes together. The count alone does not justify a split.
- A smart class ([[small-interface-with-smart-class]]) that collects shortcuts over one interface: every method uses the one wrapped object, so the stronger sign is absent; the author calls such classes auxiliary tools rather than ideal objects (p. 113).
- A data transfer object or framework-bound class whose accessors the framework requires: the convention governs, and accessors are [[no-getters-and-setters]]'s question.
- Where the project's convention sets a different threshold, the convention governs; the book's number is a heuristic, by its own author's account.

## Repair

The book says only to split the class (pp. 115-116). This wiki's procedure:

1. List each field and the public methods that touch it.
2. If the methods fall into groups over disjoint fields, extract each group with its fields into its own class.
3. If the original class must keep its interface for callers, let it hold the new objects and delegate, and plan to retire it.
4. If no disjoint grouping exists, reconsider whether some methods are convenience variants of one another and can be moved to a smart class or a decorator (see [[small-interface-with-smart-class]], [[composable-decorators]]).

## Before and after

```
class Account
  field balance
  field history
  field emailAddress
  field smtpServer

  public deposit(amount)      // balance, history; returns a new Account
  public withdraw(amount)     // balance, history; returns a new Account
  public statement()          // history
  public notify(text)         // emailAddress, smtpServer
  public remind(date)         // emailAddress, smtpServer
```

Five public methods, none of them an accessor, and two field groups used by disjoint methods.

```
class Account
  field balance
  field history
  public deposit(amount)      // returns a new Account
  public withdraw(amount)     // returns a new Account
  public statement()

class Mailbox
  field emailAddress
  field smtpServer
  public send(text)
  public remind(date)
```

Each class now has fewer than five public methods and every method uses the fields of only one class. An `Account` that also carried a `changeEmail(addr)` setter would not count it here; that setter is [[no-getters-and-setters]] and [[immutable-objects]].

## Source

- [[elegant-objects]], section 3.1, pp. 115-116: the metric (public and protected methods), the number five and its admitted arbitrariness, the exclusion of constructors and private methods, the four gains, the definition of cohesion as every method using every property. Section 2.9, p. 113, for smart classes as auxiliary tools.
- [[code-complete]], Russian edition, p. 146: as few methods as possible per class, and the defect study.
- This wiki's own: the exclusion of accessors, the reading of exactly five, the stronger sign as a test, the assignment of neighbouring cases, all limits, the repair procedure, the pseudocode pair.
