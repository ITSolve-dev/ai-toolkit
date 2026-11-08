---
title: Isolate unsafe memory operations behind wrappers
category: errors
summary: "In code that manages memory by hand, raw allocation and release calls or link-field updates (p->next = ...) appear at many sites with no wrapper or owning routine that checks, poisons and nulls; a loop frees a node and then reads its next; a pointer is declared far from its allocation."
tags: [rule, pointers, memory, defensive-programming, dog-tag, wrappers]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* (section 13.2) calls pointers one of the most error-prone areas of programming and traces many security problems, buffer overflows especially, to their misuse (p. 314). A pointer error is usually a pointer aimed at the wrong place: «Ошибка в указателе — чаще всего результат того, что он указывает не туда, куда должен.» (p. 316) Writing through it corrupts memory, and the symptom may be a crash, a wrong result elsewhere, or nothing at all until much later. For that reason, the book says, the costly part of fixing such an error is finding its cause (p. 316). Its strategy has two parts: avoid making the errors, and make them show as early as possible after they are coded (p. 316).

This page applies only where code manages memory by hand. The language-specific advice from the same section (references against pointers, smart pointers, rules of C syntax) is left out under this wiki's scope.

## Rule

«Изолируйте операции с указателями в методах или классах» (p. 316): write `NextLink()`, `InsertLink()`, `DeleteLink()` once, rather than handling the list by hand wherever it is used. Then centralise the safety checks in wrappers around allocation and release, which the book calls `SAFE_NEW` and `SAFE_DELETE` (pp. 322-323). Prefer a technique that needs no pointers at all whenever a reasonable one exists (p. 323).

The checks the book gathers into the wrappers (pp. 316-322):

- declare a pointer and give it its value in the same statement;
- release memory in the scope that allocated it: in the same block, in a matching routine, or in the destructor of the object whose constructor allocated it;
- before use, check that the pointer falls in a plausible address range and that what it points to has a plausible value;
- a **dog tag**: an extra field set to a known value on allocation, checked on use and on release, and changed on release so that a second release is caught. A tag at the start of the block catches double release, and one at the end catches writes past the block. The more often the tag is checked, the closer to its source the corruption is detected;
- explicit redundancy: two copies of a field that must agree;
- before releasing, fill the block with garbage so that a dangling pointer reads obviously wrong data, then set the pointer to null so that a write through it fails at once;
- assert that the pointer is not null before releasing it, and keep a list of allocated pointers so that releasing one that was never allocated is caught;
- when freeing a linked list, hold the pointer to the next node before freeing the current one;
- reserve a "parachute" of memory at start-up that is large enough to save work and shut down cleanly, and release it when memory runs out (p. 321).

The book's closing chapter gives the reason for nulling under a general rule: «Программируйте так, чтобы ошибки было трудно не заметить.» (p. 829). It cites Glenford Myers, who studied defect corrections and found that the most common cause of poor error detection was simple inattention: the errors were visible in the test output and the programmers did not notice them (Myers, 1978b; p. 829). A freed pointer may still point at a valid area of memory, so a mistaken use can appear to work; set to null, it points at an invalid address, and the mistake produces loud problems instead of silent ones (p. 829). The same paragraph's advice on compiler warnings is on [[do-not-silence-warnings]].

The book notes that some of these techniques are redundant or conflicting: a list of valid pointers makes dog tags unnecessary, for example. Wrappers keep the program to one consistent strategy, and they let the debug build stop on an error while the production build logs it and continues (pp. 322-323).

## Sign in code

- Raw allocation and release calls appear at many sites, outside any wrapper or owning class.
- Link fields of a list are updated directly at several call sites rather than by list routines.
- A pointer is declared at one place and allocated many lines later.
- A released pointer variable stays in scope with its old value.
- A loop frees a list node and then reads that node's `next`.

This wiki assigns the neighbouring cases as follows. A resource acquired in one routine and released in another, including memory a routine allocates for its caller to free, is [[finish-what-you-start]]. Freed memory left with its last valid contents in a debug build is [[offensive-programming]], which owns the difference between builds. Counting allocations against releases to find a suspected leak is the procedure [[resource-balance-check]]. This page owns raw memory and link operations spread through the code with no wrapper, and the checks such a wrapper makes.

## When not to apply

This wiki's own limits:

- In code where memory is managed automatically, or owned by a scope-bound handle, most of this list is done by the runtime. Only isolating link manipulation in routines still applies.
- The garbage fill, the dog tag and the pointer list cost time and memory. The book treats switching them between debug and production builds as part of the design (pp. 322-323), so their absence from a release build is not a finding by itself; see [[switchable-debug-aids]].
- Arena, pool or region allocators release in bulk by design; the per-pointer pairing, pointer list and nulling checks do not apply to memory they own.

## Repair

1. Put each data structure's link manipulation into routines of its own.
2. Route every allocation and release through one pair of wrappers that apply one chosen set of the checks above.
3. Pair each allocation with its release in the same scope or the same object's lifetime.
4. Replace pointers with a safer technique where one is reasonable.

## Before and after

```
node = allocate(Node)
...
while node != none
    release(node)
    node = node.next            // reads freed memory
```

```
function safe_release(ref p)
    assert p != none
    assert allocated.contains(p)
    fill(p, GARBAGE)
    allocated.remove(p)
    release(p)
    p = none

node = safe_allocate(Node)
while node != none
    following = node.next
    safe_release(node)
    node = following
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 13.2, pp. 314-323, and the chapter checklist, pp. 335-336: the error-prone nature of pointers, the two-part strategy, isolation in routines, each listed check, dog tags, the parachute, the wrapper pair with its debug and production behaviour, and the preference for non-pointer techniques. Section 34.7, p. 829: making errors hard to miss, the Myers finding and the null-after-free reasoning; the quotation was transcribed from the extracted text and should be checked against the page image. This wiki's own: the signs as worded, the assignment against the neighbouring pages, the limits and the pseudocode. Related: [[explaining-variable]] for naming the participants of a pointer chain, [[crash-early]] and [[assert-the-impossible]].
