---
title: Tramp data
category: functions
summary: "A parameter that a routine never reads itself and only hands on to the next call, repeated across two or more levels of a call chain."
tags: [rule, parameters, abstraction, coupling]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Tramp data is data passed to a routine only so that it can pass it to another routine (Page-Jones, 1988; p. 555). McConnell does not condemn it outright: «Это не всегда плохо» (p. 555). His test is whether passing it fits the abstraction of each routine's interface.

## Rule

For every routine the data passes through, ask whether that parameter is consistent with the abstraction the routine's interface presents. If it is, the passing is fine; if not, find a way to make each routine's interface more consistent (p. 555).

## Sign in code

A parameter that a routine's body never reads except to hand it to a call, repeated across two or more levels of the call chain.

This wiki assigns the neighbouring cases as follows. This page owns a parameter that only passes through. A parameter the body neither reads nor passes on is [[remove-unused-parameters]]; a long list is [[limit-parameter-count]]; a whole object where a few fields would do is [[pass-what-the-routine-uses]].

## When not to apply

- The book's own limit: the parameter is part of what each intermediate routine is about (p. 555). This wiki's example is a cancellation token or deadline threaded through a request pipeline, which is part of every step's contract.

## Repair

These moves are this wiki's own; the book only asks for a more consistent interface. Move the routine that needs the data closer to where the data originates; or let the top caller build the collaborator that needs the data and pass the collaborator instead; or fold the data into an object that the intermediate routines legitimately operate on. Do not make the data global instead: this wiki reads that as worse, since [[global-data]] owns that shape and tramp data is the visible form of the same dependency.

## Before and after

```
// before: format and layout never use locale, they only pass it on
function report(data, locale):  return format(data, locale)
function format(data, locale):  return layout(data, locale)
function layout(data, locale):  return money(data.total, locale)
```

```
// after: the locale is used where it arrives; format works on the total itself
function report(data, locale):
    total = money(data.total, locale)
    return format(data, total)
function format(data, total):  return header(data) + line(total)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 24.2, p. 555, citing Page-Jones (1988). The definition, the "not always bad" limit and the abstraction test are the book's. The two-level threshold of the sign, the assignment against neighbouring pages, the pipeline example, the comparison with globals, the repairs and the pseudocode are this wiki's own.
