---
title: Framework intrusion
category: structure
summary: "Application code must create or reach objects in a way a library dictates, or business functions open and commit transactions themselves."
tags: [rule, third-party, decoupling, decorator]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A tool or library can reduce [[orthogonality]] by forcing its needs into your code. The book asks of each adopted toolkit, even one from other team members, what unwanted changes in your code it may bring (p. 74). This page concerns the shape a library imposes on code that is otherwise yours; where a vendor's calls sit is [[hide-third-party-apis]].

## Rule

Keep third-party concerns out of application code. The book's test case is object persistence: if the scheme is transparent it is orthogonal, and if objects must be created or accessed in a special way, it is not (p. 74). The authors add that interfaces to outside components should stay confined to small parts of the system, so nothing ties you to one vendor, product or platform (p. 72). It adds that separating such details from your code is a further benefit, which as printed eases later changes by the vendors of the tools (p. 74).

## Sign in code

- Application objects have to be created through a library's factory, or extend a library's base class, in order to work with it.
- Transaction begin and end, or similar cross-cutting calls, appear inside functions that perform the business work.

A vendor's client, query dialect or exception type named outside one adapter class, in code that also holds business logic or in the application's own signatures, is [[hide-third-party-apis]], not this page. For a required base class, the repair by holding a service instead of extending is [[delegate-to-services]].

## When not to apply

The limits are this wiki's own, since the source states none:

- A small program, or code whose whole purpose is to drive that library, has no independent logic to protect, and a wrapper would be cost with no return.
- Where a library is adopted as a long-term foundation on purpose, the decision is recorded and the wrapper is not worth maintaining. This rule then has nothing to report.

## Repair

- Confine the third-party calls to one adapter class, as [[hide-third-party-apis]] sets out.
- Add cross-cutting behaviour from outside the working function, as a decorator. The book's example is EJB, where transaction boundaries are declared in annotations outside the methods, so one body of code runs unchanged in different transaction environments (p. 74). It adds that the style works in nearly any language and needs no framework, only discipline (p. 74).

## Before and after

Before:

```
function transfer(source, target, amount)
    tx = store.begin()
    source.withdraw(amount)
    target.deposit(amount)
    tx.commit()
```

After:

```
function transfer(source, target, amount)
    source.withdraw(amount)
    target.deposit(amount)

function in_transaction(work)
    return function(args)
        tx = store.begin()
        result = work(args)
        tx.commit()
        return result

transfer_atomically = in_transaction(transfer)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 10, pp. 72 and 74, via [[pragmatic-programmer]]. This wiki's own: the signs beyond the book's persistence test, the limits, and the pseudocode. The sentence on p. 74 about that further benefit is reported as printed, and this page rests nothing on it: the case for confining vendors comes from p. 72.
