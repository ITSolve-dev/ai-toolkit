---
title: The test is the first client of the code
category: testing
summary: "A function reads the wall clock, or a test's setup outweighs what it checks: think through the test first and change the signature until that setup disappears. A read of a global is global-data."
tags: [rule, testing, coupling, design-for-test]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-03
---

Thinking through how a function will be tested, before its body exists, puts the author in the caller's seat and exposes coupling while the signature is still cheap to change. The book's position is that the value of testing lies less in catching bugs than in this feedback on the code.

## Rule

Before writing a function, work out how it would be tested, and change its interface to what that test needs. The book opens with a deliberate provocation: «Тестирование предназначено не для выявления программных ошибок» (p. 265). It holds that the main benefit arrives when tests are thought about and written, not when they run (p. 265), and it calls the test the «первый пользователь вашего кода» (p. 266).

A function tightly bound to other code is hard to test because the whole environment has to be prepared before it can be called, so making code easy to test reduces its coupling (pp. 266-267). A second effect concerns understanding: code written on a partial grasp of the task, with boundary and error handling added as they come up, ends up about five times as long as it should be, full of conditionals and special cases. Thinking about boundary conditions first can reveal patterns that simplify the function, and thinking about error conditions shapes its structure (p. 267). The book's summary tip is «Проектируйте с учетом тестирования» (p. 273).

The worked example is a query for frequent viewers. Before any code exists, asking how to test it produces two API changes: the database is passed in instead of being a global, and the unclear qualifying field becomes a parameter (pp. 265-266).

## Sign in code

- A function reads the wall clock instead of receiving the time as an argument.
- A test's setup builds infrastructure unrelated to the behaviour its assertions check, and the setup is longer than the assertions.
- A function opens with a run of special cases, each guarding one boundary value, where the test inputs show that one general rule would cover them.

This wiki assigns the neighbouring cases as follows. A function that reads a global or a singleton connection, and a test that patches or assigns one first, are [[global-data]], which owns that sign and shares this page's repair. An environment variable read in a reusable module is [[do-not-rely-on-unguaranteed-context]]. A test that must open a form or simulate a click is [[logic-testable-without-ui]]. Setup that exists only to supply values a computation reads, such as a file created for a few strings, is [[process-values-not-their-source]]. This page owns the clock, setup with none of those causes, and the question asked before a function exists. A read of the wall clock is [[test-is-first-client]], whatever its syntax, except a zero-field class whose methods read the clock, which is [[global-data]] (*Elegant Objects*' `Year`). Any other static call is decided by whether it reaches a mutable external resource ([[global-data]]) or not ([[no-static-methods]]).

## When not to apply

- This wiki leaves a clock or environment read alone when no test's outcome depends on it, such as a timestamp on a log line. Passing it in adds a parameter for nothing.
- The outermost wiring of a program has to touch real resources. This wiki reads that as the place where dependencies are created, and injecting them further only moves the problem.
- The book calls its second change, the field-name parameter, cheating: «придется пойти на обман» (p. 266). It also says the parameter may let the function change later, and it counts the change as added flexibility (p. 266). This wiki departs from the second half: the parameter is a stop-gap for an unclear requirement and not a pattern, and once the requirement settles, a parameter that no caller varies should go away.

## Repair

1. List what the test would have to set up, and mark everything the behaviour under test does not depend on.
2. Turn each hidden input (connection, clock, configuration) into a parameter.
3. If a choice is unsettled, expose it as a parameter for now and remove it when the requirement is known.
4. Write the boundary and error cases down as tests first, and look for a single rule that covers them before adding branches.

## Before and after

Before: the test cannot run without a global database and depends on today's date.

```
function overdue_invoices():
    return GLOBAL_DB.query(invoices where due < now())
```

After: both hidden inputs are parameters, and the test states them.

```
function overdue_invoices(db, today):
    return db.query(invoices where due < today)

test overdue_invoices_finds_past_due:
    db = memory_db([invoice(due = 2 Jan), invoice(due = 9 Jan)])
    assert count(overdue_invoices(db, 3 Jan)) == 1
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 265-267, 273. This wiki's own: the signs (clock, setup length, the run of special cases), the assignment of neighbouring cases, the limits on incidental reads and program wiring, the departure from the book on the field-name parameter, repair steps 1, 2 and 4, and the pseudocode. Related: [[test-the-contract]], [[test-driven-development]], [[global-data]], [[logic-testable-without-ui]].
