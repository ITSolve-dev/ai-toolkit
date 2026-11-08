---
title: Top-down and bottom-up design
category: structure
summary: "Decomposition (general to specific) vs composition (specific to general); decomposition stops when the next level would be easier to code than to decompose, and a solution that still looks slightly tricky needs another level."
tags: [concept, decomposition, composition, design-heuristics, iteration]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Top-down design** starts at a high level of abstraction, for example base classes or other general elements, and adds detail step by step: derived classes, collaborators, specifics. **Bottom-up design** starts from concrete objects and responsibilities and builds general groupings and base classes from them (p. 108). McConnell treats the first as a strategy of *decomposition* and the second as one of *composition*. In his account they are complementary, not competing (pp. 109-110). This page applies both to classes and routines inside a module; how an application is split into subsystems or packages is its architecture, which this wiki takes as given.

## Why top-down works, and what it buys

Top-down rests on the limit of what a person can hold in mind at one time. Splitting a general class step by step into more specialized ones means the designer never deals with too many details at once (p. 108). The book names two strengths:

- **Simplicity.** People, and programmers especially, are good at cutting something large into smaller parts.
- **Deferring construction details.** Changes to details such as file structure or report format often ripple through the whole system. Top-down design shows early that such details should be hidden in classes low in the hierarchy (p. 110). This wiki reads this as an application of [[information-hiding]]: the volatile detail goes to the bottom, where a change to it stays local.

The failure mode: low-level complexity sometimes breaks through to the top and complicates the system in a way that could have been avoided (p. 110).

## Why bottom-up works, and what it buys

Bottom-up is the way in when top-down is too abstract to start. Ask what the system has to *do*: format this report, compute its data, center its headings, show it on screen, print it. Then assign those concrete responsibilities to classes (p. 109). Low-level factors, such as how the hardware has to be driven, sometimes dictate the main attributes of a design anyway (p. 109). The book's steps:

1. Ask what the system must do.
2. From that, identify concrete objects and their responsibilities.
3. Find common objects and group them by composition or inheritance, whichever fits (see [[choose-an-alternative-to-inheritance]]). The book also names grouping into subsystems or packages here; this wiki takes that grouping as the project's architecture, given rather than chosen on this page.
4. Go up a level, or return to the top and try top-down again (p. 109).

The book names two strengths:

- Bottom-up identifies **utility functionality early**, which leads to a compact, well-factored design.
- It allows reuse of fragments of a similar system built before (p. 110).

It names two weaknesses:

- It is hard to use on its own. Most people find combining small concepts into a large one harder than splitting a large one, the problem of parts left over in the box.
- Sometimes the pieces you started with cannot be assembled into the program at all: «Никто не сможет собрать самолет из кирпичей» (p. 110).

Bottom-up starts with the hard parts, and McConnell sees an advantage in that: knowing them early lets the high-level classes be designed better, «если к этому моменту сложность не потопит всю систему» (p. 110).

## When to stop decomposing

The book gives a stopping criterion that this wiki finds checkable against a design or a draft:

- Continue until coding the next level would be easier than decomposing it: «пока вам не покажется, что вместо декомпозиции следующего уровня его было бы проще закодировать» (p. 109).
- Continue until the design is so obvious and simple it is almost annoying. If anything is unclear, decompose further.
- «Если сейчас решение кажется вам хоть чуть-чуть хитрым, для любого, кто будет работать над ним позднее, оно станет головоломкой» (p. 109).

In the book's checklist this becomes: has the design been taken to the point where its implementation seems obvious (p. 119)?

This wiki reads the criterion as a counterweight in both directions. A unit whose body still holds several unnamed steps, or clever code, has not been decomposed far enough; such code is routed by [[design-warning-signs]]. Decomposing past the point where coding is easier yields wrappers that do not pay for themselves (see [[know-when-to-stop]]). The second half of that reading is ours; the book states only the first.

## Iteration is part of the method

Decomposition is iterative in two ways. A designer goes down several levels, and a designer also tries several *different* decompositions (other inheritance trees, other groupings of objects; the book also names subsystem splits, which this wiki leaves to the architecture), compares them and keeps the better one (p. 109). McConnell argues the second attempt is nearly always better than the first (p. 108). Some tension between high-level and low-level concerns is healthy, he says, and yields a more stable structure than pure top-down or pure bottom-up (p. 107). He also points to refactoring as the safe way to try alternatives in code (p. 108, cross-reference to ch. 24; see [[refactoring]]).

## Related

[[design-heuristics]].

## Source

[[code-complete]], ch. 5.4, Russian edition, pp. 107-110, 119. The link to information hiding, the reading of the stopping criterion as also warning against over-decomposition, the routing to [[design-warning-signs]], and the treatment of subsystem and package grouping as given architecture are this wiki's own.
