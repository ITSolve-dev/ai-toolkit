---
title: Rely only on documented behaviour
category: errors
summary: "A caller passes a value outside a routine's stated input, or depends on an order, format or side result the routine never promised."
tags: [rule, contracts, coupling, assumptions]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A caller that depends on what a routine happens to do, rather than what it promises, is coupled to an implementation detail that its author is free to change. The book calls this an accident of implementation: the code works only because the routine is written as it is at the moment. It is one form of [[programming-by-coincidence]].

## Rule

Call a routine for what its contract states. The book's wording is «следует полагаться на документированное поведение», and where that is impossible for some reason, «следует задокументировать свое допущение» (p. 248).

The reasoning is the book's own example. A routine is called with bad data and returns some answer, and the caller builds on that answer. Its author never considered that case. If the routine is then corrected, the caller can break (pp. 246-247). The same holds for calls made in the wrong order or context (p. 247). Undocumented behaviour may also change in the next release of a library (p. 247).

## Sign in code

- A caller uses a result obtained from an argument outside the routine's stated range or type.
- A caller reads a property of a result that the routine's documentation does not state: the first element of an unordered result, the wording of an error message, a field of an internal structure.
- A call reads state that only an earlier call on the same object sets, and neither the routine's documentation nor a comment says that order is required. Where the project owns the routine and that state sits in a field that only carries a result between steps, [[pass-state-dont-hoard-it]] owns the shape, because a parameter removes the order and documenting would keep it. This page keeps a routine the project cannot change, and a field that outlives the steps, such as a connection, where repair 2 states the order.

Judging these needs the routine's contract in view. From the call alone a reader cannot tell a promise from an accident, and the page gives no verdict until that contract has been read. Where the routine has no documentation at all, this wiki reports only a visible reliance of the shapes above, and not the absence alone.

## When not to apply

- Nothing else is available. The book allows the reliance if the assumption is written down (p. 248).
- The caller and the routine are owned together and always change in one step. The cost of the rule is then low, and so is its benefit; making the behaviour a stated contract is still cheap.
- A characterisation test pins existing behaviour on purpose before a change. Depending on the accident is its job.

## Repair

1. Replace the reliance with a call that states what is needed, if the routine offers one.
2. If you own the routine and the behaviour is really needed, make it part of the contract: document it and test it. On the callee's side the book recommends modularisation, hiding implementation behind small, well-documented interfaces, and a clear contract (p. 247; see [[design-by-contract]]).
3. If you own neither, write the assumption at the call, and preferably check it there ([[assert-the-impossible]]).

## Before and after

```
// before: the store's contract says nothing about order
rows = store.query(filter)
latest = rows[0]
```

```
// after: the order is requested, so it is promised
rows = store.query(filter, orderBy: "created", descending: true)
latest = rows[0]
```

Where the routine offers no such option:

```
rows = store.query(filter)
assert isSortedDescending(rows, "created")   // assumption: vendor returns newest first
latest = rows[0]
```

## Source

[[pragmatic-programmer]], Topic 38, pp. 246-248, for the rule, its reasoning, and the repair on the callee's side. The signs, the second and third limits, repair step 1, the documenting and testing in step 2, the check in step 3 and the example are this wiki's own.
