---
title: Drive repeated dispatch from a table
category: complexity
summary: "An if or switch chain of four or more arms over a key, all of one shape, branches nested over several enums whose every leaf assigns a constant, or an if/else-if chain of compound boolean conditions over the same few inputs (a and not c, a and b and c) whose every branch assigns a category: use a lookup table indexed by those inputs and one access or loop. Branches on a state machine's state are the state-machine pages, not this one."
tags: [rule, table-driven, duplication, dispatch, lookup-table, state-machine, boolean-logic]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

Where many cases differ only in their data, the variation can move into a table and the control flow can shrink to one access or one generic loop. *The Pragmatic Programmer* uses the form twice: a command interpreter and a generic state machine. *Code Complete* gives the general case: nearly anything chosen by logic can be chosen by a table; in simple cases the logic is simpler, and tables gain as the logic grows (p. 404 of [[code-complete]]).

## Rule

Put what varies per case in a table and keep the logic fixed.

**Selecting a value.** McConnell's first case classifies characters through a three-branch boolean chain and replaces it with `charTypeTable[inputChar]`: «Вы поместили знания, доступные программе, в данные, а не в логику: в таблицу, а не в условия if.» (p. 405). A twelve-arm `ElseIf` over the month becomes one array of days per month. Adding leap years adds one index to the access, while the `if` version would grow again (pp. 406-407). Nested branches over several factors become a table with several dimensions. The book's insurance rate branches on gender, then marital status, then smoking, then age, and a rate table indexed by all four factors replaces the whole tree with one access (pp. 407-409). The book notes that a separate array per age is the obvious first improvement, and that a table over all the factors is the better one (pp. 408-409).

**Selecting an action.** The reason *The Pragmatic Programmer* gives for its interpreter is extension: the language must be extensible, so it should be driven by a table of its parser, «таблицы синтаксического анализатора» (p. 350 of [[pragmatic-programmer]]). Each row holds the command letter, a flag saying whether an argument is needed, and the routine to call (p. 350). The main loop stays simple: it reads a line, finds the command, gets the argument if one is required, and calls the handler (p. 351). The state machine has the same shape: a component is given a transition table and an initial state, and accepting an event is a lookup by state and event, with a `default` row for that state as the fallback (p. 356). See [[finite-state-machine]].

McConnell returns to the form in his tuning chapter (pp. 600-601). A complicated chain of logic, he observes, usually comes down to two steps: classify something, then act on the class (p. 600). His example is an `if` chain whose conditions are compound expressions over three booleans `a`, `b`, `c` (`a && !c || a && b && c`, and so on), each branch assigning a category number; a table indexed by the three inputs replaces it, and he calls that «более модифицируемый и быстродействующий подход» (p. 601). The listing carries the warning that the table definition is hard to understand, so any helpful comment should be used (p. 601). His measured speed-ups, 33% and 50% in two languages (p. 601), are language-specific and not part of this rule; unlike most of that chapter, the change also improves changeability, so this wiki does not treat it as tuning in the sense of [[premature-code-tuning]].

Chapter 19 makes the same recommendation for decisions combining several variables: a decision table instead of `if` or `case` (p. 428).

Two questions decide every table design, in McConnell's terms: how an entry is found (direct, indexed or stair-step access; see [[choose-table-access-scheme]]) and what an entry holds. An entry holds data, or, where the result is an action, code or a reference to a routine; the book warns that each of these makes the table more complex (p. 406). McConnell also counts as a benefit that the table can live in a file read at run time, so rates change without a change to the program (pp. 409, 423). [[over-configuration]] owns the question of when that pays.

## Sign in code

- An `if` or `switch` chain of four or more arms over a single key in which every arm has the same shape: each arm only assigns a constant (twelve months, each assigning a day count), or extracts the same parts and then calls one thing.
- Branches nested over several enumerated or small-integer inputs, where every leaf assigns a constant to the same variable (the rate tree).
- A compound boolean classifier that compares one value against literal lists or ranges and assigns a category.
- An `if`/`else if` chain in which every condition is a compound expression over the same few boolean or small enumerated inputs, the same input appearing negated in one branch and un-negated in another, and every branch only assigning a category or a handler, so finding which branch an input combination reaches means evaluating each condition in turn (pp. 600-601).
- Adding a case means copying an arm and changing only values in it.
- State transitions, however written, are not this page: flags that one loop over a sequence of events sets and tests to track its place in that sequence are [[finite-state-machine]]; code that already holds the mode in one state variable but does not mirror the transition graph is [[state-machine-as-switch-on-state]]; whether a state machine's transitions are held as a table or as a switch is [[state-machine-table-or-switch]]. This page adds only the generic table component of the exercise in *The Pragmatic Programmer*.

This wiki assigns the neighbouring cases as follows. This page owns a branch over a data value chosen at run time, whose arms hold the varying values or calls themselves. Where each arm instead constructs or calls a per-variant unit whose body is a fixed list of fields, [[describe-variants-in-data-not-subclasses]] owns it. A switch on a type tag of an object whose arms call per-kind behaviour of one operation is [[polymorphism-or-type-switch]]. A branch whose key is an object's runtime type or class name is [[avoid-introspection-and-casting]], however many arms. Where the key is a public constant or enum passed in from outside to select behaviour, [[no-public-constants]] owns the branch. Repeated statements with no branch at all, which state a list of facts, are [[program-close-to-the-domain]]'s shape. A single compound condition guarding one action is [[name-complex-conditions]]. An `if`-`else if` chain whose every arm only assigns a category from one input compared with literal lists or ranges is [[drive-repeated-dispatch-from-a-table]]. A chain whose arms do different work, or whose tests combine different inputs, is [[name-complex-conditions]], which names each test with a boolean function (pp. 350-351). A branch whose arms each call one routine and do nothing else is [[drive-repeated-dispatch-from-a-table]] when the key-to-routine map is the whole of the logic; arms that do different work around their calls are [[case-or-if-chain]]. Whether a chain becomes a table is [[drive-repeated-dispatch-from-a-table]]; which access scheme the table uses is [[choose-table-access-scheme]]. The order of arms in a chain whose arms do different work is [[order-branches-by-frequency]]; once a chain is a table, the order of arms is moot. Whether a state machine's transitions are held as a table or as a switch is [[state-machine-table-or-switch]]; a table for repeated dispatch outside a state machine is [[drive-repeated-dispatch-from-a-table]].

## When not to apply

McConnell gives one limit: in simple cases logical expressions are simpler and clearer (p. 404). *The Pragmatic Programmer* states none. The limits below are this wiki's own.

- There are fewer than four arms, the threshold [[program-close-to-the-domain]] shares. This wiki reads McConnell's "simple cases" as this threshold. The table's indirection costs more than the repetition saves.
- The arms differ in shape. A table then grows flags that re-create the control flow in data, which is harder to read than the branches were. This wiki accepts one such column, as in the interpreter table (p. 350 of [[pragmatic-programmer]]), and treats more as this case.
- The key cannot index the table directly and no clean transformation exists. A forced direct table then turns into duplicated rows: see [[choose-table-access-scheme]].
- A reader now has to look in two places, and a debugger steps through one generic line for every case. Where tracing single cases matters more than adding them, keep the explicit form.

## Repair

1. Name the inputs the branches test and list what differs between arms. Those are the table's dimensions and columns.
2. Map each input to a dense index, as McConnell does with enums numbered from 0 to a `_Last` value (p. 409). Where the input does not fit as an index, isolate the conversion: see [[isolate-table-key-computation]].
3. Write one row per case, with a function reference for any behaviour. Fill the table by assignment, from a file, or by computation (p. 409).
4. Replace the branch with one access, or one loop or function that looks up a row and acts on the columns.
5. For a table over several inputs, give it a comment header naming each axis and its values, and check with a test that enumerates every combination that each maps to the result the chain produced. The comment is McConnell's (p. 601); the enumerating test is this wiki's own.
6. Decide what a missing key does: report it, as the interpreter's lookup does (p. 351 of [[pragmatic-programmer]]), or use a default row.

## Before and after

Before: each new command copies an arm.

```
if c == 'L':
    if not hasNumber(line): report("L needs an argument"); continue
    loadRow(number(line))
else if c == 'S':
    if not hasNumber(line): report("S needs an argument"); continue
    saveRow(number(line))
else if c == 'D':
    if not hasNumber(line): report("D needs an argument"); continue
    deleteRow(number(line))
else if c == 'C':
    if not hasNumber(line): report("C needs an argument"); continue
    copyRow(number(line))
else:
    report("unknown command")
```

After: a new command is one row.

```
commands = [
  { key: 'L', run: loadRow   },
  { key: 'S', run: saveRow   },
  { key: 'D', run: deleteRow },
  { key: 'C', run: copyRow   },
]

cmd = find(commands, c)
if cmd is none: report("unknown command"); continue
if not hasNumber(line): report(c + " needs an argument"); continue
cmd.run(number(line))
```

Before: every new factor multiplies the arms.

```
if sex == FEMALE:
    if status == SINGLE:
        if smoker == NO:
            if age < 18: rate = 200
            else if age == 18: rate = 250
            ...
        else:
            if age < 18: rate = 250
            ...
    else if status == MARRIED:
        ...
else:
    ...
```

After: the knowledge is in data, and the logic is one line.

```
rateTable = loadRates()      // [smoker][sex][status][ageKey]
rate = rateTable[smoker][sex][status][keyFromAge(age)]
```

Before: a classifier over three booleans; which category does `a, not b, c` get?

```
if (a and not c) or (a and b and c):
    category = 1
else if (b and not a) or (a and c and not b):
    category = 2
else if c and not a and not b:
    category = 3
else:
    category = 0
```

After: the same mapping as a documented table.

```
# categoryTable[a][b][c]
#              !b!c  !b c   b!c   b c
# !a             0     3     2     2
#  a             1     2     1     1
categoryTable = [[[0, 3], [2, 2]],
                 [[1, 2], [1, 1]]]

category = categoryTable[a][b][c]
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), answers to exercises 4 and 19, pp. 350-351 and 356: the interpreter and state-machine table designs and the extensibility reason. [[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 18, pp. 404-409 and 423: the general rule, the character, month and insurance examples, the two design questions, the run-time file benefit and the "simple cases" limit; ch. 26.1, pp. 600-601: the classify-then-act observation, the three-boolean chain and its table, the comment warning and the speed figures; section 19.1, p. 428: decision tables for conditions over several variables. The third pair reproduces the book's truth table in this wiki's pseudocode. The signs and their threshold of four, the splits with neighbouring pages, the limits other than McConnell's, the repair steps other than the dense-index mapping, the fill options and the missing-key behaviour, and the pseudocode are this wiki's own. As extracted, the listing for exercise 19 in *The Pragmatic Programmer* stores the table passed to its constructor and then reads a constant. This wiki takes from that slip that a table handed to a generic component must be the one actually read. Related: [[dry]], [[program-close-to-the-domain]].
