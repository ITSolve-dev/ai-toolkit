---
title: Name a thing by its role
category: naming
summary: "A method name states the arithmetic or the mechanism rather than the purpose, a variable carries a generic label, or a primitive parameter leaves its unit unreadable."
tags: [rule, naming, intent]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A name should say what a thing is for in the program, not how it works. Choosing such a name is also a design check, because it forces the question of why the thing exists.

## Rule

The book holds that components should be named for the role they play in the code. Each time something is created, stop and ask «Для чего я это создаю?» (p. 291). The pause lifts the view from the immediate task to the larger picture. Failing to find a fitting name often reveals that the planned next step makes no sense (p. 291).

The reasoning under the rule is the Stroop effect: people read words faster than they do many other things, so a written word takes priority when something is being interpreted, and names should be chosen with that in mind (pp. 291-292). This wiki states the consequence plainly: a reader believes the name before the code.

The book's examples (pp. 292-293):

- A discount method named for deducting a percentage says what it does and not why, and its `amount` parameter leaves open whether the value is absolute or a percentage. Renaming the method for applying a discount states the purpose. Changing the parameter type from a floating-point number to a `Percentage` type documents the expected values, since a caller could otherwise only guess between 0 to 100 and 0.0 to 1.0.
- A variable holding an authentication result is better named for what this person is trying to do, `buyer` or `customer`, than the general `user`. The translation of p. 292 garbles this passage and seems to defend `user`; the exercise on p. 296 settles the intent by proposing the more specific names over the traditional, generic one.

## Sign in code

- A method name names an arithmetic or data operation (`add`, `deduct`, `copy`, `set`) while its receiver or parameters are domain types (a ticket's deadline, an order's price), so the name states the computation on a domain object rather than its purpose.
- A parameter has a generic name (`amount`, `value`, `data`) and a primitive type, so its unit or range cannot be read from the signature. A measure with no unit is judged by where it is declared: a parameter is [[name-by-role]], a stored field or constant is [[representation-that-fits-by-coincidence]], a local is [[comment-data-declarations]]; a line joining two of them goes to the page owning the left-hand side. A parameter whose unit cannot be read from its name is [[name-by-role]]; two parameters of different kinds sharing one primitive, readable or not, are [[replace-primitive-with-class]].
- A variable bears a broad domain label (`user`, `item`, `account`) in a scope where a narrower role is known.

A method that returns a value and is named with a verb belongs to [[builder-and-manipulator-names]], whose repair names what comes back by its role; a method that returns nothing and is named for its mechanism belongs to [[name-by-role]]. A returning method named with a noun for its mechanism belongs to [[name-by-role]] unless it is a general-purpose utility. A class or interface name belongs to [[name-classes-for-what-they-are]]. For a variable, this page owns a name that says the right kind of thing but not its narrower role in this scope (`user` for the buyer); a variable whose name is its type's name (`account: Account`, `aCustomer: Customer`) is [[type-name-vs-variable-name]]; a name that does not say which quantity it holds (`data`, `info`, `date` for today's date) is [[name-describes-what-the-variable-represents]], and `temp`-style names for intermediate values are [[temporary-variable-names]].

## When not to apply

- In a general-purpose utility the mechanism is the role: its receiver and parameters are not domain types. Where the call sites are visible, this wiki adds a check: if they serve several unrelated purposes, an operation name is correct, and if they all serve one, a purpose name is.
- The book exempts branding: projects and teams may have clever, obscure names (p. 293). That concerns products and not identifiers.
- A wrapper type has a cost. This wiki's reading is that a unit in the name (`discount_percent`) can be enough where values cross few boundaries.
- Local convention can override this page; see [[follow-local-naming-culture]].
- This page owns a name that narrows a thing to its role in a scope. Where two names for one thing carry no difference of role, [[one-name-per-concept]] owns the case and the extra name goes.

## Repair

1. Ask what the caller is trying to achieve, and name the method for that.
2. Give an ambiguous primitive a type or a unit in its name.
3. If no honest name comes, treat that as evidence the unit does two things or should not exist, and revisit the design before naming it.

## Before and after

Before: the name says the arithmetic, and the unit of `amount` is a guess.

```
method add_time(amount: number):
    self.due_at = self.due_at + amount

ticket.add_time(30)
```

After:

```
method extend_deadline(extension: Duration):
    self.due_at = self.due_at + extension

ticket.extend_deadline(minutes(30))
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 291-293, 296. This wiki's own: the reading taken of the garbled passage on p. 292, which rests on the exercise on p. 296 of this edition; the stated consequence of the Stroop effect, the signs, the discriminating test, the splits with [[one-name-per-concept]], [[replace-primitive-with-class]], [[representation-that-fits-by-coincidence]], [[comment-data-declarations]], [[builder-and-manipulator-names]] and [[name-classes-for-what-they-are]], the wrapper-type limit, repair step 3's reading and the pseudocode. Related: [[rename-when-meaning-drifts]], [[name-reads-at-the-call-site]].
