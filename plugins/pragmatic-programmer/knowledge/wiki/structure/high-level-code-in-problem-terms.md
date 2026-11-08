---
title: High-level code in problem terms
category: structure
summary: "A routine at the top of a call chain (entry point, use case, handler) that names file modes, record layouts, byte offsets, stack or queue operations, or a one-letter index for a domain thing, often with a comment translating that variable into the domain."
tags: [rule, abstraction-levels, information-hiding, naming]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell names working at the highest possible level of abstraction as a specific way to fight complexity, and he means working in terms of the programming problem rather than of its computer solution (p. 825). «Высокоуровневый код должен описывать решаемую проблему.» (p. 825)

## Rule

In the book's terms, high-level code should be full of descriptive class names and method calls that state what is being done. It should not hold details of files, stacks, queues, arrays and characters, or variables named `i`, `j` and `k` (p. 825). At the top level the program should not know that employee data is stored as records in a file, and the reader should not need a comment explaining that `i` indexes the employee file and is later reused for client accounts. «Вместо этого вы должны видеть две переменные с выразительными именами, такими как employeeIndex и clientIndex.» (p. 825)

Terms of the implementation are unavoidable somewhere, but they can be kept apart from the parts written in terms of the problem (p. 825). The book sketches five levels (fig. 34-1, pp. 826-827):

| Level | Contents |
|---|---|
| 0 | operations of the OS and machine instructions |
| 1 | the language's own structures and libraries |
| 2 | low-level structures of the implementation: stacks, queues, lists, trees, files, sorting and searching |
| 3 | low-level primitives of the problem domain: its vocabulary as building blocks, often the level of business objects or services |
| 4 | high-level code of the problem domain, partly readable by non-programmers and depending more on the level-3 tools than on the language |

The book says many programmers never rise above level 1, and that a program written entirely at level 2 holds too many details to win the battle with complexity (p. 826). At level 4, implementation details should sit two levels below, so that changes of hardware or OS do not touch it at all. A program changes in the user's terms, so a change in the problem domain then lands on level 4, and a new version is built from the level-3 blocks (p. 827). The book notes that other layerings, such as a three-tier architecture, cut across these levels (p. 827). Which architecture a project uses is out of this wiki's scope and is taken as given.

Even without such an architecture, the book lists techniques for working in problem terms (p. 827): classes for structures that mean something in the domain, hidden low-level data types and their implementation, named constants for the meaning of string and numeric literals, intermediate results assigned to named variables, and boolean functions that explain complex boolean tests.

## Sign in code

A routine at the top of a call chain (an entry point, a use case, a handler) contains any of these:

- a detail of storage or transport: an open mode, a seek, a byte offset, a record layout or field positions;
- an operation on a data structure named as such: a push or pop, an index into an array, a poll of a queue;
- a one-letter index standing for a domain thing;
- a comment translating such a variable into the domain ("i is the employee record here").

This wiki assigns the neighbouring cases as follows. This page owns the mix of abstraction levels inside one high-level routine. Callers walking a shared structure directly, or mixing direct access with access routines on the same data, are [[access-routines-at-domain-level]]. A class's public interface mixing domain operations with container operations is [[mixed-abstraction-levels-in-interface]]. A one-letter index reused for two things, outside a top-level routine, is [[loop-index-names]]. A bare literal whose meaning is domain knowledge is [[named-constants-over-literals]]. The same call sequence repeated four or more times with only literals changing is [[program-close-to-the-domain]]. Detail reached through module-level state is [[global-data]].

## When not to apply

The limits are this wiki's own except where a page is cited.

- The routine is itself at level 2 or 3. In a file reader, a parser or a collection class, files, indices and stacks are the problem, and naming them is correct.
- A small script with one level. When the whole program is twenty lines, an extra layer of domain primitives costs more than it hides.
- A very primitive environment, where the book admits the tools may force a programmer to bend the preferred approach (p. 823); see [[program-into-the-language]].
- Modelling the business domain itself, such as which aggregates and contexts exist, is out of this wiki's scope and belongs to `domain-driven-guide`. This page covers only how a routine's text reads.

## Repair

1. Name the domain operation each low-level fragment performs, then extract it into a function or a method of a level-3 abstraction.
2. Replace a reused one-letter index with two variables named for their roles.
3. Replace a domain literal with a named constant.
4. Move storage details (file, record, mode) behind a level-3 class, so that the top-level routine no longer knows where the data lives.
5. Turn a complex boolean test into a named boolean function.

## Before and after

```
function payroll_run():
    f = open("emp.dat", READ_ONLY)
    i = 0
    while not eof(f):
        rec = read_record(f, 128)        // i: employee record index
        if rec[3] == 2 and rec[7] > 0:   // status 2 = active
            stack.push(rec)
        i = i + 1
    i = 0                                // i now indexes client accounts
    while not stack.empty():
        e = stack.pop()
        accounts[i].credit(e[7])
        i = i + 1
```

```
function payroll_run():
    for employee in employees.active_with_pay_due():
        payroll.pay(employee)
```

In the "after", the file mode, the record width, the field positions and the stack live inside `employees` and `payroll`, both level-3 abstractions, where they are at the right level. If `accounts` in the "before" were a shared structure with access routines of its own, the indexing would also be a sign of [[access-routines-at-domain-level]]; here it stands for the routine's own local data.

## Source

[[code-complete]], ch. 34.6, pp. 825-827; p. 823 for primitive environments. The book's parts: the rule, the employee and client index example, the five levels, and the list of low-level techniques. This wiki's own parts: the signs, the assignments against neighbouring pages, the limits except the one for primitive environments, the repair steps, and the pseudocode. The quotations were transcribed from the extracted text and should be checked against the page image.
