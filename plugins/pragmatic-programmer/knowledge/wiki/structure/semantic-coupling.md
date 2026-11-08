---
title: Semantic coupling
category: structure
summary: "A caller relies on what a callee does inside rather than on its interface: it passes a literal (true/false, an int code, an enum member, a string such as \"premium\") that selects which branch of the callee runs, or builds an argument only partly because it knows which fields the callee reads."
tags: [rule, coupling, control-flag, partial-initialization, hidden-assumptions, flag-arguments, remove-flag-argument]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

Semantic coupling is McConnell's name for the case where one module uses not a syntactic element of another but semantic knowledge of how it works inside; he calls it «Самый коварный тип сопряжения» (p. 98). The danger he names: «изменение кода в используемом модуле может так нарушить работу использующего модуля, что компилятор этого не определит» (p. 99), and the failures that follow are subtle and are not traced back to the change, so debugging becomes Sisyphean (p. 99).

Fowler treats the control flag as its own refactoring, **Remove Flag Argument**, formerly Replace Parameter with Explicit Methods (*Refactoring*, 2nd ed., ch. 11, PDF pp. 350-356). He adds a test for what is a flag at all, a reason beyond readability, and a disagreement with McConnell's limit that this page resolves below.

## Rule

A caller may depend on what a module's interface states, and on nothing it knows about the module's internals. The book gives five examples (p. 99); this page owns two of them, and three have owners elsewhere:

| Book's example | Owner |
|---|---|
| Module 1 passes a control flag that tells Module 2 what to do | this page |
| Module 1 passes an object initialised only for the three of its seven methods it knows Module 2 uses | this page |
| Module 2 uses global data after Module 1 has changed it | [[global-data]] |
| Module 2 skips the documented `Initialize()` because it knows `Routine()` calls it | [[semantic-encapsulation-violation]] |
| Module 2 downcasts the base object it was given, knowing it is really a derived one | [[avoid-introspection-and-casting]] |

The cases of semantic coupling: a documented call the caller skips, or another class's constant it borrows, because it knows the implementation belongs to [[semantic-encapsulation-violation]]; a reliance on runtime type to [[avoid-introspection-and-casting]]; on shared mutable state to [[global-data]]; a reliance on what the callee does with a value the caller passes belongs to [[semantic-coupling]].

On the control flag the book has its own limit: if Module 2 defines a specific data type for the flag (an enumeration or an object), this kind of coupling is probably fine (p. 99).

Fowler defines a flag argument as "a function argument that the caller uses to indicate which logic the called function should execute" (PDF p. 351), and prefers an explicit function for each task (PDF p. 352). His reasons (PDF p. 352): his first route into an API is the list of its functions, and flags hide the differences between the calls available; once a function is chosen, the reader still has to discover which flag values exist; a boolean is worse, because in a call one cannot tell what `true` means. Explicit functions also help tooling, which can then tell a call of the premium logic from a call of the regular logic.

**What makes it a flag.** Fowler gives two conditions, both required (PDF p. 352): callers set the value to a literal, not to data flowing through the program; and the callee uses the argument to steer its own control flow, not as data it passes on. He repeats: "A flag argument isn’t just the presence of a boolean value; it’s that the boolean is set with a literal rather than data" (PDF p. 355).

**Disagreement with McConnell, resolved per setting.** McConnell's limit holds that a flag with its own declared type is probably fine; Fowler counts enum members and strings as flag arguments too (`bookConcert(aCustomer, CustomerType.PREMIUM)`, PDF p. 352). This wiki resolves it by what the caller holds:

- The caller writes the value as a literal: it already knows which behaviour it wants, and an enum only fixes the meaning of `true`, not the hidden list of behaviours. Fowler's repair holds: explicit functions.
- The value arrives as data (read from input, computed as `determineIfRush(anOrder)`): Fowler has no problem with the signature (PDF p. 355), and McConnell's declared enumeration is the right form for that parameter ([[enum-instead-of-codes-and-flags]]).

## Sign in code

- A parameter whose value selects a branch inside the callee, passed as a bare literal: a bool or int (`process(order, true)`, `render(doc, 2)`, Fowler's `deliveryDate(anOrder, true)`, PDF p. 353), or an enum member or string written at the call site.
- The same function called from several places with different literals in the same position, and the callee branches on that parameter.
- An argument constructed with some fields left empty or default, at a call site that then passes it to one consumer; or a comment like "only X and Y are used". This page owns the partly built argument at the call site; the routine's signature that invites it is [[pass-what-the-routine-uses]].

This wiki assigns the flag case as follows. An argument the callee branches on is [[no-public-constants]] when it is a public enum or constant shared across classes, whatever the call site writes; otherwise, written as a literal at the call site it is [[semantic-coupling]], and flowing in as data its type is [[enum-instead-of-codes-and-flags]]. An argument the callee stores, filters on or passes on is [[enum-instead-of-codes-and-flags]]. The repair of [[no-public-constants]], a class per behaviour, agrees with this page's. A control flag passed as a bare literal at the call site is [[semantic-coupling]], which owns the call site. Where an integer or boolean code selects which of several unrelated jobs a routine body does, [[routine-cohesion]] owns the body and the repair is one routine per job; where the code names a value the routine handles in one way, [[enum-instead-of-codes-and-flags]] owns it. A literal code passed to a constructor that only stores it is [[factory-function-over-constructor]]; a literal passed to a routine whose body branches on it is [[semantic-coupling]].

## When not to apply

- The flag's value flows in as data at every call site (Fowler, PDF p. 355); a declared type with named values is then the right form (the book's limit, p. 99). The callee's body may still deserve its conditional decomposed, but the signature stays.
- The callee does not branch on the argument but passes it on as data (Fowler, PDF p. 352).
- **Several flags in one function.** Fowler grants that flags can have a place there, since explicit functions for every combination would multiply; he also calls it a signal of a function doing too much, to be split into simpler composable functions (PDF p. 352). This wiki reads that as: do not apply the repair mechanically; the owner is then [[routine-cohesion]].
- This wiki adds: a boolean whose meaning is a property of the data (`includeArchived`) rather than a choice of algorithm reads at the call site and is a weaker case; name it at the call site.
- Partial construction is the callee's documented contract (a builder, a patch object whose absent fields mean "unchanged").

## Repair

- For a control flag passed as a literal: split the callee into one routine per behaviour so the caller names what it wants. Fowler's mechanics (PDF pp. 352-356): create an explicit function per flag value. If the callee dispatches on the flag at its top, extract each branch. If the flag is tangled through the body, layer thin wrappers instead (`rushDeliveryDate(o) = deliveryDate(o, true)`), which he calls partial applications written in program text. Replace each literal-passing call with a call to the explicit function. If no caller passes the parameter as data, remove the original, restrict its visibility, or rename it to warn against direct use (his `deliveryDateHelperOnly`); if some callers pass data, keep the original for them and support both interfaces.
- For a flag whose value arrives as data: give it a declared enumeration.
- For a partly built argument: change the callee to take what it uses (see [[pass-what-the-routine-uses]]) or make the type impossible to construct incomplete.

## Before and after

```
function export(report, flag: int)
    if flag == 1 then writeCsv(report)
    else if flag == 2 then writePdf(report)

export(report, 2)

customer = Customer(name = n)      -- address, tier left empty
sendGreeting(customer)              -- caller knows only name is read
```

```
function exportCsv(report)
function exportPdf(report)

exportPdf(report)

function sendGreeting(name: String)
sendGreeting(n)
```

## Source

[[code-complete]], section 5.3, Russian edition, pp. 98-99. The five examples, the enumeration limit and the reasoning are the book's. [[fowler-refactoring]], ch. 11, Remove Flag Argument, PDF pp. 350-356: the definition, the two conditions, the discoverability and tooling reasons, enum and string flags, the several-flags limit, both mechanics and mixed callers are Fowler's. The resolution of the disagreement between the two books by whether the caller holds a literal or data is this wiki's own; the ownership table, the flag splits with [[routine-cohesion]] and [[enum-instead-of-codes-and-flags]], the signs (including their narrowing of the book's control flag to one passed as a bare literal), the fourth and fifth limits and the repairs are this wiki's own. Related: [[coupling]], [[temporal-coupling]].
