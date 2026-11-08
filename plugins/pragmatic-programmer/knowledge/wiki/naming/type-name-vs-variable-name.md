---
title: Variable name more specific than its type name
category: naming
summary: "A variable or parameter named after its type alone (widget: Widget, account: Account, aCustomer: Customer, list: List), so it says what kind of thing it holds but not which one or what for."
tags: [decision-rule, naming, types, objects]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A type and an instance of it need distinct names. McConnell compares five ways to keep them apart (*Code Complete*, Russian edition, pp. 265-266):

1. a variable that differs from its type in the case of the first letter (`Widget widget`);
2. a type written all in capitals (`WIDGET widget`);
3. a type prefixed with `t_`;
4. a variable prefixed with `a` (`aWidget`);
5. a variable more specific than its type (`Widget employeeWidget`).

## Rule

The test is whether the variable can be named for its role. McConnell calls every option a trade-off and uses option 5 in the book, because it reads most clearly to a reader who does not know the naming convention (p. 266). «Вариант 5 заставляет тщательно обдумывать имя каждой переменной.» (p. 266), and the result is usually more understandable code.

He weighs the other options as follows (pp. 265-266):

- Case-only (option 1) is common, but some programmers find it awkward: such names carry «слишком малое психологическое и визуальное различие» (p. 265). It also breaks in a language that ignores case.
- All-capitals types (option 2) collide with the convention for constants.
- A type prefix (option 3) works in every language, but some programmers dislike prefixes for aesthetic reasons.
- A variable prefix (option 4) has to be applied to every instance, instead of once to the class name.

## Sign in code

A variable or parameter whose name is just its type's name, lower-cased or with an article (`widget: Widget`, `aCustomer: Customer`, `list: List`), in a scope where its role could be stated. Typical cases, by this wiki's reading, are a scope that holds more than one instance of the type (`account` beside `destination`), or a routine whose purpose gives the instance a role (`sender`, `recipient`, `pendingOrders`).

This wiki assigns the neighbouring cases as follows. A variable whose name is its type's name is this page's. A name that is just its value's type (`list` holding a List) is [[type-name-vs-variable-name]], even where it also shadows a built-in; a built-in or library name reused for a value of another kind is [[misleading-or-arbitrary-names]]. A broad domain label that is not the type's name (`user` for the buyer) is [[name-by-role]]. Two names that differ only in case but stand for **different concepts**, not a type and its instance, are [[names-differ-by-more-than-a-character]]. A digit appended to the type-named variable (`account`, `account2`) is [[numbered-names]].

## When not to apply

- McConnell's own limit: sometimes the widget really is just a generic widget. Inventing a role then produces something like `genericWidget`, which reads worse than plain `widget` (p. 266). A generic routine that handles any instance of the type, with only one in scope, may use the type's name.
- The project's or language's established convention overrides the choice among options 1-4. McConnell tells the reader to follow the language's naming conventions (p. 267); see [[naming-conventions]].

## Repair

Name the variable for its role in this code, and keep the type name for the type. If the role cannot be named because the code is truly generic over the type, keep the plain name.

## Before and after

```
function transfer(account: Account, destination: Account, money: Money):
    account.debit(money)
    destination.credit(money)
```

```
function transfer(source: Account, target: Account, amount: Money):
    source.debit(amount)
    target.credit(amount)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 265-267 ([[code-complete]]). The five options, their trade-offs, the book's use of option 5 and the `genericWidget` limit come from the book. The sign's 'more than one instance or a nameable role' condition, the split with [[name-by-role]] and the transfer example are this wiki's own.
