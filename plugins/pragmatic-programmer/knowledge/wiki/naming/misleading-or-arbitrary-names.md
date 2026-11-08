---
title: A name must not mean something else, or nothing at all
category: naming
summary: "A name that already means something different (FALSE as an abbreviation, a well-known constant or a language or standard-library name reused for another thing) or that has no relation to what it holds (margaret, pookie, fred, a pet name)."
tags: [rule, naming, misleading-names]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A reader takes a name at its word. McConnell lists three kinds of name that defeat this (*Code Complete*, Russian edition, pp. 277, 279). One borrows a meaning the reader already holds. Another reuses a name the language or its library already gives a meaning. The third carries no meaning at all.

## Rule

- **No misleading names or abbreviations.** «Убедитесь в том, что имя не является двусмысленным.» (p. 277). McConnell's example is that `FALSE` is understood as the opposite of `TRUE`, so using it to abbreviate 'Fig and Almond Season' would be foolish.
- **No reuse of predefined names.** Every language has reserved and predefined names; review the lists from time to time so as not to intrude on them. McConnell's PL/I example `if if = then then then = else; else else = if;` is legal and unreadable. The section's heading names standard types, variables and methods (p. 279), and the checklist repeats it for standard-library routines (p. 280).
- **No names unrelated to the thing.** Names like `margaret` and `pookie` all but guarantee that nobody else understands them. «Не называйте переменные в честь девушки, жены, любимого сорта пива и т. д.» unless those are the program's entities (p. 279).

## Sign in code

- An identifier spelled like a well-known word or constant but used for something else (`FALSE`, `NULL`, `OK` holding a season, a code or a count).
- A local or parameter named like a language built-in or a standard-library name for a value of another kind (`print`, `type`, `string` holding a count), so the original becomes unreachable or ambiguous in that scope.
- A personal or whimsical name with no domain meaning (`fred`, `pookie`, `bob`).

This wiki assigns the neighbouring naming cases as follows. This page owns a name whose ordinary meaning is something else, or that has none. A real word too general for its value (`data`, `value`, `date` for today's date) is [[name-describes-what-the-variable-represents]]. A name the body has outgrown, such as a `get` that writes a file, is [[rename-when-meaning-drifts]]. Two names that differ only by one character or by sound are [[names-differ-by-more-than-a-character]]. A name that is just its value's type (`list` holding a List) is [[type-name-vs-variable-name]], even where it also shadows a built-in; a built-in or library name reused for a value of another kind is [[misleading-or-arbitrary-names]].

## When not to apply

- Where a linter already reports the shadowing, cite the linter, per this wiki's charter on mechanical style. This page adds the case a linter does not see: a reserved meaning (`FALSE`, `OK`) reused for another value.
- This wiki's own limit: a domain term that happens to equal a common word is not misleading when the domain is clear from context, such as `order` in a shop.

## Repair

Rename to a name that states what the value is in the problem domain, and that does not collide with a reserved word, a built-in, or a well-known constant.

## Before and after

```
FALSE = loadSeason('fig-and-almond')
type = fetchCustomers()
for pookie in type:
    notify(pookie)
```

```
figAndAlmondSeason = loadSeason('fig-and-almond')
customers = fetchCustomers()
for customer in customers:
    notify(customer)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 277, 279-280 ([[code-complete]]). The three rules, the FALSE, PL/I and margaret/pookie examples, the heading on standard names (p. 279) and the standard-library checklist item come from the book. The sign list, the split with neighbouring naming pages, the linter limit and the domain-term limit are this wiki's own.
