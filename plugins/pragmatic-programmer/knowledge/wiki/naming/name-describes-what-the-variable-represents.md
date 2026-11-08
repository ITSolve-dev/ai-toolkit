---
title: A variable's name fully and accurately describes what it represents
category: naming
summary: "A variable name that is a real word but does not say which quantity it holds: too general for its value (date for today's date, current, total among several totals, data, value) or naming the computer mechanics instead of the problem quantity (inputRec, calcVal)."
tags: [rule, naming, variables]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell calls this the most important principle of variable naming. A name should fully and accurately describe the thing the variable stands for. He argues that the variable and its name are one thing, so the name decides much of how well the variable does its job (*Code Complete*, Russian edition, p. 253). His method: say in words what the variable represents, and that phrase is often the best name. Such a name needs no decoding, cannot be mistaken for anything else, and is easy to remember because it matches the concept (p. 253).

## Rule

- **Complete and accurate.** The name says what quantity it holds, not just its general kind. In the book's table, `date` looks fine but is wrong when the value is today's date, and `current` does not say what is current. `currentDate` and `todaysDate` are right (p. 254).
- **Specific.** «Имена должны быть максимально конкретны.» (p. 254). Names general enough to serve more than one purpose (`x`, `temp`, `i`) carry less information than they could and are usually bad (p. 254).
- **Oriented to the problem, not to the solution.** «Хорошее имя в большей степени выражает что, а не как.» (p. 254). The book's pairs: `inputRec` against `employeeData`, `bitFlag` against `printerReady`, `calcVal` against `sum`. In each pair the first name speaks of computing and the second of the problem (pp. 254–255).
- **No numbered siblings.** Even once you know what `x` means, `x1` and `x2` say nothing about how the two relate (p. 255). This wiki keeps that case on [[numbered-names]].

How long a name should be is a separate question; see [[name-length-matches-scope]].

## Sign in code

- A name that is true of the value but too general for it: `date` for today's date, `total` where several totals are in scope, `current` with no noun.
- A name that is a filler word with no quantity in it: `data`, `value`, `rec`, `obj`.
- A name made of programming terms (`input`, `rec`, `buf`, `val`, `calc`) where the variable holds a quantity from the problem: an employee, a balance, a printer state.
- A practical test from the book's example: a reader asked to print one particular quantity cannot tell which variable holds it (p. 253).

This wiki assigns the neighbouring naming cases as follows. This page owns a name that does not say which quantity it holds. A name that says the right kind of thing but not its narrower role in this scope (`user` for the buyer) is [[name-by-role]]. A parameter with a generic name and a primitive type whose unit cannot be read is [[name-by-role]]. A variable named `temp`, `tmp`, `x` or similar for an intermediate value is [[temporary-variable-names]]. Siblings told apart by a digit are [[numbered-names]]. A name containing `flag` is [[status-variable-not-flag]]. A one-to-three-letter name on a wide scope is [[name-length-matches-scope]], and `i`, `j`, `k` are [[loop-index-names]].

## When not to apply

- Loop indexes and other variables used for a few lines: a short name is a deliberate signal there. See [[name-length-matches-scope]] and [[loop-index-names]].
- Code whose problem domain is the computation itself, such as a buffer manager, a parser or a numeric kernel. There the "computer" words are the problem's vocabulary, and `buffer` or `token` is a problem name. This limit is this wiki's own reasoning; the book does not state it.
- Well-known variables of a formula (`a`, `b`, `c` of a quadratic) are the problem's own names when the code transcribes that formula. This wiki's reading; the book does not discuss it.

## Repair

1. Say in words what the variable holds, e.g. "the amount of this month's new purchases".
2. Make that phrase the name, then shorten it to a practical length without dropping the part that tells it apart from its neighbours (`newPurchases`, `monthlyTotal`).
3. Replace a computing word with the problem's word wherever the value belongs to the problem.

## Before and after

```
date = clock.today()
data = loadEmployee(id)
calcVal = data.salary + data.bonus
if date > data.reviewDate
    schedule(data, calcVal)
```

```
todaysDate = clock.today()
employee = loadEmployee(id)
annualPay = employee.salary + employee.bonus
if todaysDate > employee.reviewDate
    schedule(employee, annualPay)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.1, pp. 253–255 ([[code-complete]]): the principle, the method of stating the variable's meaning in words, the table of good and bad names, the specificity rule and problem orientation. The signs are this wiki's adaptation of the book's examples, and the assignment against the neighbouring naming pages is this wiki's own. The limits for computational domains and formula variables are this wiki's own. The pseudocode is this wiki's own.
