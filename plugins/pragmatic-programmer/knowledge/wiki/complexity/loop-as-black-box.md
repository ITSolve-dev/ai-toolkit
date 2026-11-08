---
title: Loop as a black box
category: complexity
summary: "Concept: whether a reader can tell when a loop ends from its header alone, or must read the body for breaks, index assignments and flags; the idea the loop rules rest on, and which page owns each way of breaking it."
tags: [concept, loops, control-flow, readability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell lists what typically goes wrong with a loop: wrong or missing initialization, accumulators not initialized, wrong nesting, wrong termination, an index not incremented or incremented wrongly, and an array indexed wrongly through the loop index (p. 365). He answers all of them with two principles. Minimize the number of factors that affect the loop. Treat its body like a routine, keeping as much control as possible outside it. «Думайте о цикле, как о черном ящике» (p. 365): the surrounding code knows the control conditions, not the contents.

## What it means

A loop is a black box when its header states every condition under which it runs. McConnell's example is a `while` over two conditions: from the header alone the reader knows the loop ends when the file is exhausted or no more data is available (p. 365). Every construct that changes control from inside the body breaks the box: an assignment to the index, a `break`, a `continue`, a flag set deep in a branch. McConnell says this explicitly about `break`: it rules out treating the loop as a black box and forces the reader to look inside to understand its control (pp. 373-374). His cross-reference on p. 365 adds that even the single exit of a `while (true)` loop lies inside the box.

## How it shapes the rules

The loop rules in this wiki apply this idea to particular shapes:

- [[for-or-while]]: a `for` with its index changed from inside claims to be a closed box and is not.
- [[loop-header-holds-only-control]]: the header is the outside of the box, so only control goes there.
- [[initialize-close-to-first-use]] and [[loop-housekeeping-at-one-end]]: initialization and housekeeping are control, kept where they can be seen together.
- [[break-and-continue]]: each exit inside the body is a hole in the box, accepted only where it buys more clarity than it costs.
- [[loop-with-exit-in-the-middle]]: the one sanctioned trade, where a single internal exit removes duplicated code.
- [[do-not-use-loop-index-after-loop]]: the index's final value is a detail of the box's inside, so code outside must not read it.
- [[loop-length-and-nesting]]: a box too big to see at once cannot be checked even when it is closed.

This wiki reads the trade-off this way. The black box costs flags and extra conditions in the header. Past a point those cost more clarity than a well-placed `break` saves, and McConnell concedes this on p. 372 (see [[break-and-continue]]).

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 16.2, p. 365 and pp. 372-374. The mapping onto the individual rule pages and the statement of the trade-off are this wiki's own.
