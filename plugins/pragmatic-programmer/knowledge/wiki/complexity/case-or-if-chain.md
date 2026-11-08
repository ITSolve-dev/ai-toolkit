---
title: Case statement or if-then-else chain
category: complexity
summary: "A switch on a selector derived by dropping information from the real data (first letter of a command, a truncated code), so different inputs share a label; or an if-else-if chain of four or more arms, each doing different work, that tests one simple variable for equality against constants: switch on simple categorical data only, chain otherwise."
tags: [decision-rule, conditionals, switch, if-else, dispatch]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The book's last key point for chapter 15 is that control constructs are not interchangeable and that each piece of code should get the one that fits it best (p. 358). For multi-way branches it gives a test in both directions: use a `case` where the language supports it and the data is simple, and fall back to an `if`-`then`-`else` chain where the data is not.

## Rule

- **Toward case.** Where the language offers a `case` that handles strings, enumerations or ranges, use it in place of an `if`-`then`-`else` chain: it is easier to write and to read (p. 352). The checklist asks whether an `if`-`then`-`else`-`if` sequence is the best implementation or a `case` would be better (p. 357).
- **Toward the chain.** Use `case` for simple data that is easy to split into categories; for data that is not simple, use `if`-`then`-`else` chains. Do not fabricate a phony variable just to be able to use `case` (p. 354).

The book's failure case: a command interpreter switches on the first character of what the user typed. `copy` correctly calls `Copy()`, but so do «cement overshoes, clambake или cellulite» (p. 354), and the `default` error check only catches a wrong first letter, never a wrong command. The repair tests the whole string in an `if`-`else if` chain (pp. 354-355).

The book notes the counterpoint in a margin: assigning a complex expression to a well-named boolean variable or function can improve readability (p. 354). This wiki reads the distinction as: a derived variable is fine when it *names* the decision without losing information; it is phony when it *drops* information the decision depends on.

## Sign in code

- `selector = derive(input)` immediately before `switch (selector)`, where `derive` truncates, hashes or samples the input (first character, prefix, length, first word) so that different inputs map to the same label.
- A `default` whose message claims to catch invalid input, over a selector from which invalid input cannot be told apart from valid.
- In the other direction: an `if`-`else if` chain of four or more arms, each doing different work, where each test compares the *same* simple variable for equality or range against constants, in a language whose `case` supports those comparisons.

This wiki assigns the neighbouring cases as follows. A chain whose arms all have the same shape and differ only in data is [[drive-repeated-dispatch-from-a-table]], which replaces both the chain and the `case` with a table. A branch whose arms each call one routine and do nothing else is [[drive-repeated-dispatch-from-a-table]] when the key-to-routine map is the whole of the logic; arms that do different work around their calls are [[case-or-if-chain]]. A branch on an object's runtime type is [[avoid-introspection-and-casting]], and a switch on a type tag that calls a type-specific method in each arm is [[polymorphism-or-type-switch]]. This page owns the choice between `case` and chain for a branch over data whose arms do different work.

## When not to apply

The book's own condition: the language's `case` must support the comparison. C++ and Java support only ordinal types one value at a time, and some scripting languages have no `case` (p. 353). This wiki's own limits:

- A selector derived by a function that classifies without loss (every input maps to exactly one meaningful category, and the classifier rejects what fits none) is not phony. A parser that returns a command enum, or an error, is the usual repair, not a violation.
- Arms that test different variables or compound conditions are a chain by nature; do not force them into a `case`.

## Repair

1. If the selector loses information, switch on the full value, or test the full value in an `if`-`else if` chain, as the book does.
2. Better, where many such commands exist: parse the input into a closed type first (rejecting unknown input there), then `case` on that type, so the `default` really catches what was not planned.
3. If a chain tests one simple variable against constants and the language's `case` handles them, rewrite it as a `case` with one label per value.

## Before and after

```
action = userCommand[0]
switch action:
    case 'c': clipboard.put(selection)
    case 'd': buffer.remove(cursor); redraw()
    case 'h': showHelp(topicAt(cursor))
    default:  inputError(INVALID_COMMAND)
```

After: repair 2. The parser rejects unknown input, so the `default` catches only what was not planned.

```
command = parseCommand(userCommand)     // COPY, DELETE, HELP, or an input error
switch command:
    case COPY:   clipboard.put(selection)
    case DELETE: buffer.remove(cursor); redraw()
    case HELP:   showHelp(topicAt(cursor))
    default:     internalError("unhandled command", command)
```

Where the language's `case` accepts the full value (strings), switching on `userCommand` itself is also a repair. Where it does not, the book's repair is an `if`-`else if` chain over the full string (pp. 354-355); that chain is then outside the third sign, which needs a `case` that supports the comparison.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.1, p. 352 (prefer `case` where supported); section 15.2, pp. 353-355 (language support, the phony selector and its repair, the margin counterpoint); checklist and key points, pp. 357-358. The "names vs drops information" criterion, the parse-to-closed-type repair, the arm-count threshold, the assignment against the neighbouring pages, the limits, the setting note under the pair and the pseudocode are this wiki's own.
