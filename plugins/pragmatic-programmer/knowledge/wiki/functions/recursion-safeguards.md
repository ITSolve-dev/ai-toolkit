---
title: Recursion must provably stop and stay within one routine
category: functions
summary: "A recursive routine with no base-case test reached before the self-call, with no visited-set on a graph or grid walk, or recursing through a cycle of routines (A calls B calls A)."
tags: [rule, recursion, termination, stack]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Recursion here means a routine that solves a small part of a problem and calls itself on the smaller pieces of the rest (p. 385 of [[code-complete]]). McConnell's tips on recursion (pp. 387-388) fit into one rule: every recursive routine needs a path out that the reader can see, a guard against looping on structures with cycles, and a depth the stack can hold. Whether to recurse at all is decided on [[recursion-or-iteration]].

## Rule

- **Make sure the recursion stops.** The routine must contain a non-recursive path, usually a test that ends further recursion once it is no longer needed (p. 387).
- **Record what has been visited** when the structure can lead back to itself. This comes from the maze example, not from the listed tips: there a remembered position prevents «бесконечную рекурсию, которая может возникнуть в результате замкнутого пути» (p. 387).
- **Use a safety counter** where no such simple test is possible. The counter must not be created anew on each call. Keep it in an object field or pass it in as a parameter, and stop once it exceeds a limit (pp. 387-388). The loop form of the device is [[safety-counter]].
- **Keep recursion within one routine.** Cyclic recursion, where A calls B, B calls C and C calls A, is dangerous «потому что ее сложно обнаружить» (p. 388). Redesign it so that one routine recurses. If that is impossible, use a safety counter as insurance (p. 388).
- **Watch the stack.** Set the safety counter's limit low enough to prevent stack overflow, and keep large locals out of recursive frames (p. 388).

## Sign in code

- A routine calls itself and none of its branches returns without making the call. Or the stopping test comes after the recursive call instead of before it.
- A recursive walk over a graph, grid or linked structure that can contain a cycle carries no visited set and no marking.
- A call graph cycle across routines: A calls B, B calls A, through any number of steps.
- A safety counter that is a local variable initialised inside the routine, so it restarts on every call and never reaches its limit.
- Large buffers or arrays declared as locals in a routine whose depth depends on the input.

## When not to apply

- Where the recursion is structurally bounded, for example by descent over a finite tree that cannot share nodes, or by an index range that shrinks on every call as in quicksort, the base-case test is the whole safeguard. A safety counter adds nothing there. The book asks for a counter only where a simple test is impossible (p. 387).
- Mutually recursive routines that a grammar or a state machine requires by its nature, such as a recursive-descent parser. This wiki adds this limit: the book admits the cyclic case and asks for a safety counter (p. 388), but does not name such designs.
- This wiki also notes that where the language or runtime guarantees tail-call elimination, the stack-depth concern does not apply to tail calls. The book does not discuss this.

## Repair

Add the missing base case before the recursive call. Add a visited set where the structure can contain cycles. Pass a depth or safety counter as a parameter with a limit sized to the stack. Fold a cycle of routines into one recursive routine with helpers that do not recurse.

## Before and after

```
findPath(maze, pos):
    if isExit(maze, pos): return true
    for each neighbour n of pos:
        if findPath(maze, n): return true
    return false
```

```
findPath(maze, pos, visited):
    if pos in visited: return false
    if isExit(maze, pos): return true
    add pos to visited
    for each neighbour n of pos:
        if findPath(maze, n, visited): return true
    return false
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 17.2, pp. 385-388, and the checklist on p. 403: [[code-complete]]. The tips and the visited-set device of the maze example are the book's. The signs, the limits for structurally bounded recursion, for parsers and for tail calls, and the pseudocode are this wiki's own.
