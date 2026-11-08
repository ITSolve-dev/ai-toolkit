---
title: Name the intermediate object
category: complexity
summary: "A chain of two dereferences or field hops (p->next->previous), or a longer one along a single self-referential structure (node.next.previous.next), sits on the left of an assignment or inside a loop whose iterations do not change it, so the reader must reconstruct an unnamed participant; assign it to a variable named for its role."
tags: [rule, readability, naming, expressions, loops, loop-invariant]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

*Code Complete* gives two pieces of advice on pointers that hold in general (section 13.2): use an extra variable to name each object an operation involves, and assign a complicated access expression to a well-named variable. The book's line on such expressions: «Подобные выражения заставляют разбираться в коде, а не читать его.» (Russian edition, p. 320)

## Rule

When an operation involves an object that is only reachable through a chain, give that object its own variable named for its role in the operation.

The book's first example inserts a node into a doubly linked list (pp. 318-319). Three objects are involved: the current node, the node that follows it, and the node being inserted. The original names only two, so the reader has to keep in mind that `currentNode->next` is the third, and the line `currentNode->next->previous = insertNode` is the one the book marks as needlessly complicated. The rewrite introduces `followingNode` and renames the others `startNode` and `newMiddleNode`. It costs one line and reads directly.

The second example multiplies inside a loop by `rates->discounts->factors->net`. Assigning it once to `quantityDiscount` before the loop makes the purpose visible and may also speed the loop up. The book adds that any speed gain should be measured before anyone relies on it (p. 320). By this wiki's count that chain also meets [[train-wreck]]; the hoist names the value, and the reach is train-wreck's finding.

Chapter 26 returns to the same example among the tuning techniques, under minimizing the work done inside loops: if an expression or part of one can be computed outside the loop and its result used inside, do so. McConnell calls it a good practice that sometimes improves readability, and the named `quantityDiscount` shows what the loop multiplies by, which was not obvious before (p. 606). His measured gains were modest outside one language (13-19%, and 43% in Java), and he concludes that during initial coding you may use whichever form reads better and leave speed for later (p. 607). This wiki reads that as: hoisting an invariant chain is a naming move first and a speed move second, and by McConnell's own definition of tuning (p. 596) it is standard practice, so it needs no measurement. See [[premature-code-tuning]] for the shapes that do.

The book also warns against reusing one variable for different purposes, which it says matters most for pointer variables (p. 318); that sign is [[one-variable-one-purpose]].

## Sign in code

- A chain of two dereferences or field hops (`a.b.c`, `p->next->previous`), or a longer one along a single self-referential structure, appears on the left of an assignment, or inside a loop body while its value does not change between iterations.
- An operation's comment names a participant ("after current", "the following node") that no variable names.

This wiki assigns neighbouring cases as follows. A chain of at most two steps that sits on the left of an assignment or inside a loop, or one that walks the links of a single self-referential structure (node.next.previous), is [[explaining-variable]]; a longer chain through objects of different application or third-party types is [[train-wreck]], and naming it locally does not repair it. A compound boolean condition is [[name-complex-conditions]]. One variable reassigned for a second role is [[one-variable-one-purpose]]. A step of a routine that deserves a name of its own is [[extract-routine-to-name-a-step]]. An identical non-trivial expression written two or more times, such as `rate / 12` in a formula, is [[name-repeated-subexpression]]; this page owns field and dereference chains. A single expression that combines several sub-calculations, none written twice, is [[extract-variable]]; an identical subexpression written two or more times is [[name-repeated-subexpression]]; a chain of field hops or dereferences is [[explaining-variable]].

A local assigned once from a lookup or expression on values every fragment already has, inside a function about to be split, is [[replace-temp-with-query]]; a variable naming the participant of a dereference chain in a function that stays whole is [[explaining-variable]].

## When not to apply

This wiki's own limits: a single hop (`order.total`) needs no name. A chain read once, in a line that already says what it is, gains nothing from a variable. If the intermediate value can change between its assignment and its use, as in a loop that modifies the structure, hoisting it changes behaviour.

Two more limits of this wiki's own for the loop case: if the chain has side effects or reads state that the loop body or a called routine changes, it is not invariant, and establishing that needs a look at what the body calls. If the loop may run zero times and evaluating the chain can fail (a dereference valid only when there are elements), hoisting it introduces a failure the loop form never reached; keep it inside or guard it.

## Repair

Introduce a local variable for each unnamed participant, named for its role in this operation (`following`, `quantity_discount`), assign it once before use, and write the operation in terms of the named variables. Give each role its own variable rather than reusing one.

## Before and after

```
function insert_after(current, inserted)
    inserted.next = current.next
    inserted.previous = current
    if current.next != none
        current.next.previous = inserted
    current.next = inserted
```

```
function insert_between(start, new_middle)
    following = start.next
    new_middle.next = following
    new_middle.previous = start
    if following != none
        following.previous = new_middle
    start.next = new_middle
```

## Source

McConnell, *Code Complete*, 2nd edition, Russian edition, via [[code-complete]], section 13.2, pp. 318-320: extra pointer variables for clarity, the `InsertLink` pair, simplifying complicated pointer expressions, and the `quantityDiscount` example with its caution about measuring speed. The book also advises drawing a picture of the links (p. 320). Section 26.2, pp. 606-607: the same example as a loop optimization, the readability remark and the measured gains. The quotation of p. 320 is transcribed from `raw/` and needs the page-image check. This wiki's own: the generalisation beyond pointers, the reading of the chapter 26 technique as a naming move, the side-effect and zero-iteration limits, the signs, the split with neighbouring pages (including the step count shared with [[train-wreck]] and the reading of the `rates` chain as meeting it), the limits and the pseudocode.
