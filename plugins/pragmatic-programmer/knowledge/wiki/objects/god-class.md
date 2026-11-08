---
title: God class
category: objects
summary: "A class that reads and writes the data of several other classes through their getters and setters and decides for them, while those classes hold data and little behaviour."
tags: [rule, responsibilities, god-class, encapsulation]
paradigm: oop
sources: [code-complete, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

«Избегайте создания классов, которые все знают и все могут» (p. 152).

## Rule

If a class retrieves and sets data of other classes with `Get()` and `Set()`, meddling in their business and telling them what to do, ask whether its functionality should be implemented in those classes instead of in a god class (p. 152, after Riel, 1996).

Larman describes the same shape as coupling minimised to excess: a few incohesive, bloated, complex active objects that do all the work, over many "passive zero-coupled objects that act as simple data repositories" (17.12, p. 446). His reason against it is the poor [[cohesion]] of the active objects. He traces one cause to copying people's duties onto the software object named after them: a Cashier object that does almost everything (18.5, p. 501); see [[responsibility-driven-design]].

## Sign in code

A class whose methods mostly call getters on objects of other classes, compute, and call setters on those same objects, where the other classes have few methods beyond accessors.

This wiki splits the neighbouring case as follows. One method doing this to one object is [[tell-dont-ask]]; this page owns the class that does it across many collaborators, which is a distribution of responsibility rather than one call site. A field-less class whose methods all take the same one record and read or write only its fields, while the record has only fields or accessors, is [[class-with-only-data-or-only-behaviour]]; where its methods each read and write several data-only classes, [[god-class]] owns it; a single method of an otherwise sound class that reads another object and writes back is [[tell-dont-ask]]. The data holders it works on are [[no-getters-and-setters]]. This page applies to classes other than the one that receives the program's incoming requests or system operations: where the class is a UI event handler or code-behind that computes business results, [[logic-testable-without-ui]] owns the sign; where the class receives the program's incoming requests or system operations, [[controller]] owns it; where any other class reads and decides for several data-only classes, [[god-class]] owns it. A single read-only computation from one other class's data is [[information-expert]].

Fowler and Beck's **Large Class** smell (*Refactoring*, 2nd ed., ch. 3, PDF pp. 96-97) is about how much a class holds, not about whose data it decides on, so this wiki routes it elsewhere: too many fields, or fields sharing a prefix, are [[keep-objects-small]], and too many lines are [[class-size]]. They call a class with too much code "a prime breeding ground for duplicated code, chaos, and death" (PDF p. 97). This page keeps the class that decides for others.

## When not to apply

- A mapper or serializer whose job is to move data between representations reads many objects' data by purpose.
- This wiki adds: in code that keeps data and functions apart on purpose (records plus functions over them), functions over records are the design, not a god class; that is `paradigm: fp` territory.

## Repair

Move each decision into the class whose data it uses; the former god class keeps only coordination, or disappears.

## Before and after

```
// Employee, Account, TaxRecord and Ledger hold only getters and setters
class Payroll
    pay(e: Employee, a: Account):
        e.setPay(e.getHours() * e.getRate())
        a.setBalance(a.getBalance() + e.getPay())
    withhold(e: Employee, t: TaxRecord):
        t.setWithheld(t.getWithheld() + e.getPay() * t.getRate())
    book(e: Employee, l: Ledger):
        l.setTotal(l.getTotal() + e.getPay())
```

```
class Employee  { monthlyPay(): Money }
class Account   { deposit(m: Money) }
class TaxRecord { withhold(pay: Money) }
class Ledger    { record(pay: Money) }
class Payroll
    run(e, a, t, l):
        pay = e.monthlyPay()
        a.deposit(pay)
        t.withhold(pay)
        l.record(pay)
```

## Source

- [[code-complete]], p. 152: the rule and the question to ask.
- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 17.12, PDF p. 446 (coupling minimised to excess), and 18.5, PDF p. 501 (the Cashier doing almost everything).
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Large Class", PDF pp. 96-97. The routing of that smell to [[keep-objects-small]] and [[class-size]] is this wiki's own.
- This wiki's own: the sign, the splits against [[tell-dont-ask]] and [[class-with-only-data-or-only-behaviour]], the limits, the repair and the pseudocode, including the classes in the pair.

Related: [[reasons-to-create-a-class]], [[class-with-only-data-or-only-behaviour]].
