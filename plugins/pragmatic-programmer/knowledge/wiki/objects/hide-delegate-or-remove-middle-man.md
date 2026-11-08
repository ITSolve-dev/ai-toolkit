---
title: Hide the delegate or remove the middle man
category: objects
summary: "A class whose public methods are mostly one-line forwards to the same field, in the domain's own vocabulary, adding nothing (middle man); also a client reaching two steps through B's accessor to call C (a.b().c()), and the decision whether B should hide C or step aside."
tags: [decision-rule, delegation, encapsulation, interfaces, middle-man]
paradigm: oop
sources: [code-complete, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

*Code Complete* lists two opposite refactorings for the same three classes. *Hide delegate*: class A calls both B and C when A should call only B, and B should call C. *Remove middle man*: A calls B only so that B calls C, and A could call C directly (pp. 562-563). For removing a middle man, McConnell's decider is whether delegating through B improves or degrades the integrity of B's interface (p. 563); for hiding a delegate, he asks what the right abstraction of A's interaction with B is (pp. 562-563).

## Rule

Ask what the right abstraction of A's interaction with B is (pp. 562-563). If calling C is B's responsibility, hide C behind B. If B's role is only to redirect calls, consider removing it and calling C directly (p. 555). The book adds that a class reduced to doing very little should be deleted and its responsibilities spread to other classes (pp. 555, 562).

Larman's *Applying UML and Patterns* places the two-step reach on the scale of the Law of Demeter: `sale.getPayment().getTenderedAmount()` talks to one stranger and is "very slightly fragile", and of that example he says "Realistically, this is unlikely to be a problem" (25.4, p. 595). His repair is the hide-delegate direction, an operation on the familiar such as `sale.getTenderedAmountOfPayment()`, and he names its cost as new public operations on the familiar (p. 596). This wiki reads that cost as the point where this page's other direction applies: a familiar that fills with such pass-throughs is turning into a middle man. The longer reaches are [[train-wreck]].

Fowler's *Refactoring* treats the two as opposite smells joined by their repairs. **Message Chains**: a client asks one object for another, then that one for a third, and so on, "as a long line of getThis methods, or as a sequence of temps"; "Navigating this way means the client is coupled to the structure of the navigation" (2nd ed., ch. 3, Message Chains, PDF p. 95). **Middle Man**: delegation is part of encapsulation but can go too far, when "half the methods" of a class's interface delegate to another class (Middle Man, PDF p. 96). The repair of the first produces the second: hiding every link of a chain often turns every intermediate object into a middle man (PDF p. 95). Fowler's preferred move avoids that: see what the end object is used for, and move that work down the chain (PDF p. 95).

The catalogue entries **Hide Delegate** and **Remove Middle Man** (ch. 7, PDF pp. 216-221) give the reasoning for each direction. For hiding: "If the delegate changes its interface, changes propagate to all the clients of the server that use the delegate"; with a delegating method on the server, changes "propagate only to the server and not to the clients" (PDF p. 217). His example `aPerson.department.manager` "reveals to the client how the department class works and that the department is responsible for tracking the manager" (PDF p. 218). For removing: "Every time the client wants to use a new feature of the delegate, I have to add a simple delegating method to the server" (PDF p. 219). He says the smell "often pops up when people get overenthusiastic about following the Law of Demeter", which he would rather call "the Occasionally Useful Suggestion of Demeter" (PDF p. 219). The chapter introduction names the cost of overdoing the first: "too much hiding leads to bloated interfaces" (PDF p. 183).

## Sign in code

- **Middle man:** half or more of the public methods of a class are one-line forwards to the same field, under the domain's names, and the class holds no rule or state of its own.
- **Delegate not hidden:** the same reach through B's accessor to call C is written at two or more call sites in the code under review. With more than two steps [[train-wreck]] owns the sign; a two-step reach (`a.b().c()`) is owned by [[hide-delegate-or-remove-middle-man]]. Where that two-step chain sits on the left of an assignment or inside a loop, its naming stays with [[explaining-variable]]. This page also owns the choice of repair once either is found.

This wiki assigns the neighbouring cases as follows. A wrapper whose forwards mirror a container's or library's API, so its interface mixes that vocabulary with the domain's, is [[mixed-abstraction-levels-in-interface]]. A class that has no fields and exists only to call one method on another object's data is [[class-with-only-data-or-only-behaviour]]. A class that forwards every method of a parent it should not inherit from is [[delegate-to-services]].

## When not to apply

*Code Complete* states no limit. Larman gives one:

- **The link from B to C is stable**, as in a standard library's structure or a mature part of the code. A two-step reach is then not a finding: of his one-stranger example Larman says it is "unlikely to be a problem", and protecting against it "is not always necessary"; it depends on the instability of the object structure (25.4, pp. 595-596).

The following are this wiki's own.

- A forwarding class that exists as a deliberate boundary, such as an adapter over a third-party API or a decorator, is not a middle man even if it forwards; see [[hide-third-party-apis]] and [[composable-decorators]].
- Removing a middle man exposes C to A. Where the project's conventions keep C behind B (a store, a gateway), keep B.
- Delegation that hides how work is done is the purpose of encapsulation. Fowler's example is a director asked whether she is free for a meeting, who delegates the question to her diary: the caller need not know whether she keeps a diary, a device or a secretary (Middle Man, PDF p. 96). This wiki reads that as: a few forwarding methods are not a middle man, which is why the sign asks for half or more of the public methods, Fowler's own measure (Middle Man, PDF p. 96).

- **No fixed amount of hiding.** Fowler: "It’s hard to figure out what the right amount of hiding is", and "A good encapsulation six months ago may be awkward now" (ch. 7, PDF p. 219). A mixture is legitimate: "Some delegations may be so common that I’d like to keep them to make client code easier to work with", and "reasonable people can differ on what works best" (PDF p. 221). This wiki reads that as: one delegating method, or one two-step reach, is not a finding on its own; report a direction only where half or more of the server's interface is forwards, or where the same reach appears at two or more call sites in front of the reader.

## Repair

For a hidden-delegate case, add the operation A needs to B and implement it by calling C, and drop A's knowledge of C. For a middle man, let A hold C, delete the forwarding methods, and delete B if nothing remains.

Fowler's mechanics (ch. 7, PDF pp. 217, 220). Hide Delegate: for each method on the delegate, add a delegating method on the server (this wiki limits it to the methods clients use); move clients to it, testing after each change; when no client needs the delegate, remove the server's accessor for it. Remove Middle Man: add a getter for the delegate; replace each client call of a delegating method with a call through that getter, testing after each; delete the delegating methods no longer called. With automated tools, encapsulate the delegate field and inline each delegating method, which updates all callers at once ([[inline-function]]).

Fowler's refinements (PDF pp. 95-96):

- For a chain, Hide Delegate at whichever point helps, not at every point. Often better: Extract Function on the code that uses the end object, then Move Function to push it down the chain ([[move-function]]). If several clients of one object want to navigate the rest of the way, add one method that does it.
- For a middle man with only a few idle forwards, Inline Function into the callers. If the middle man adds behaviour of its own, Replace Superclass with Delegate or Replace Subclass with Delegate folds it into the real object.

## Before and after

```
// before: B only forwards
class Contact:
    field customer
    method name():   return customer.name()
    method email():  return customer.email()

contact.email()
```

```
// after: the middle man is gone
customer.email()
```

The other direction, a two-step reach owned by this page:

```
// before: A reaches through B, at two call sites
manager = employee.department().manager()
approver = employee.department().manager()
```

```
// after: B hides the delegate
manager = employee.manager()
approver = employee.manager()
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 24.2, p. 555, and section 24.3, pp. 562-563. The two refactorings, the decider and the advice on a class that does too little are the book's, paraphrased. Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 25.4, PDF pp. 595-596: the one-stranger example, its fragility grade, the stability remark and the stability limit, the repair and its cost. This wiki's own for that part: reading the cost as the turn towards a middle man. The signs, the assignments against neighbouring pages (including the two-step split with [[train-wreck]]), the limits and the pseudocode are this wiki's own. Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Message Chains", PDF p. 95, and "Middle Man", PDF pp. 95-96: the two smells, coupling to the navigation, half the methods delegating, the middle man produced by hiding every link, the move down the chain, the diary example and the repairs. This wiki's own for that part: the reading of the diary example as a limit, and keeping the existing two-step split with [[train-wreck]] in place of a count of Fowler's. Ch. 7, "Hide Delegate" and "Remove Middle Man", PDF pp. 216-221, and the chapter introduction, p. 183: the propagation argument, the department example, the cost of forwarding, the Law of Demeter remark, the no-fixed-amount limit, the bloated-interface cost and both mechanics. This wiki's own for that part: the threshold for reporting a finding (two or more call sites), and limiting Hide Delegate's mechanics to the methods clients use.
