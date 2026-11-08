---
title: Good enough or a broken window
category: change
summary: "Decides whether to report a flaw in working code: a floor breach, or a page's sign with that page's conditions met, makes it a broken window; an unmet condition is reported as a question; a change of form with no named violation means stop."
tags: [decision-rule, good-enough, quality, review, broken-windows]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The book says both to repair every broken window and to stop before spoiling a good program. Taken alone, each licenses the wrong review note: the first turns any preference into a defect, the second excuses any shortcut. This page decides between [[broken-windows]] and [[know-when-to-stop]] on a specific piece of code.

## Rule

The book draws the line itself. «Слово "подходящий" совсем не подразумевает небрежно или плохо написанный код.» (p. 40). A floor applies to every system: it meets its users' requirements and basic standards of performance, privacy and security (p. 40). Cutting that floor is not good-enough; the book calls it unprofessional to «нарушать элементарные правила проектирования, чтобы уложиться в крайний срок» (p. 41). Above the floor, how good is good enough is the users' call: «Включайте в требования к системе вопрос о ее качестве» (p. 41).

This wiki turns that into a test with two questions, asked in order.

1. Does the thing break the floor, or does a rule page of this wiki apply with its sign present and that page's own conditions for a verdict met? Then it is a window. Report it as a defect. Some pages say that their sign only raises a question, or name what a verdict needs. Where such a condition is unmet, report the construct and what must be checked, as that page asks, and do not call it a defect.
2. If not, does a stated requirement or a failing input call for the change? If neither does, stop. Whatever value the change has is an option for whoever owns the requirement, not a defect.

## Sign in code

The window side has a construct to point at: user input reaching a query unescaped, a secret in a log line, a loop unbounded over outside data, a case a stated requirement names with no branch for it, or the sign of a rule page with that page's conditions met. The stop side is a relation between two versions of the code: the proposed change preserves behaviour, and no construct in the old version can be named by any page. A review note with no such construct and no failing input belongs to the stop side, however reasonable it sounds.

## When not to apply

- High-stakes software. For a pacemaker, an autopilot or a widely distributed low-level library the book says the choice is limited (p. 41). This wiki reads that as a higher floor: a note that would be an option elsewhere becomes a defect there.
- A project states its own bar, such as a latency budget. That bar replaces the second question. This limit is this wiki's own.
- Two rule pages conflict with each other. This test does not arbitrate between them. This limit is this wiki's own.

## Repair

For a window, fix it or board it up as [[broken-windows]] says. For a stop, drop the change. If it may still be worth having, record it as an option and leave it out of the defects, so that the person who owns the quality requirement can weigh it.

## Before and after

```
// before: two review notes on one function
function find_users(name):
    // note 1: name reaches the query unescaped
    sql = "select * from users where name = '" + name + "'"
    // note 2: this loop could be a one-line map
    result = []
    for row in run(sql):
        result.add(to_user(row))
    return result
```

```
// after: note 1 breaks the security floor and is fixed;
// note 2 names no rule and the behaviour stays, so the loop is left as written
function find_users(name):
    result = []
    for row in run("select * from users where name = ?", name):
        result.add(to_user(row))
    return result
```

## Source

[[pragmatic-programmer]], Topics 3 and 5, pp. 35, 40-42. The floor, the verdict on cutting design rules for a deadline, the idea that quality is a requirements question and the high-stakes limit are the book's. The book does not set its two rules against each other. The two-question test, the signs, the option-not-defect reporting, the two limits marked as such and the pseudocode are this wiki's own.
