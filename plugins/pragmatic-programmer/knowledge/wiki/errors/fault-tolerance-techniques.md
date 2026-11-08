---
title: Fault-tolerance techniques
category: errors
summary: "Concept: the options for keeping a computation working after a fault (retry from a known-good state, auxiliary code, voting among implementations, substitute values, degraded mode, shutdown, restart) and what each costs in code."
tags: [concept, fault-tolerance, recovery, robustness]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Fault tolerance*, as McConnell defines it, is the set of properties that make a system more reliable by detecting errors, recovering where it can, and containing the bad effects where it cannot (p. 47). He asks the architecture to state the expected level of fault tolerance (p. 47), and illustrates the options with a system that computes a square root (pp. 47-48):

- **Back up and retry.** On failure, return to a state known to be correct and continue from there.
- **Auxiliary code.** Keep backup code that runs when the main code fails, for example another square-root method when the first answer looks wrong.
- **Voting.** Three classes compute the root in different ways and the system compares the results, taking the mean, the median or the most probable of the three, depending on the kind of fault tolerance chosen.
- **Substitute value.** Replace the wrong value with a made-up one that keeps the rest of the system working.

Other approaches he names (p. 48): moving to partial operation or reduced functionality when an error is detected, shutting down, and restarting automatically. He notes that the examples are simplified and that fault tolerance is a field of its own, outside his book (p. 48).

## How this wiki uses it

The level of fault tolerance is set by the system's architecture (p. 47); this wiki takes it as given and uses the list only for what each option costs in the code that implements it. This wiki reads the list as a menu of recovery options, each with a cost in code. The trade-offs below are this wiki's own, not the book's:

- **Back up and retry** needs a state known to be correct and a way back to it, such as a checkpoint, a transaction or immutable inputs. Without one, a retry repeats side effects. See [[failure-atomicity]].
- **Voting** costs several independent implementations, and helps only if they fail independently.
- **A substitute value** hides a fault from the rest of the system. It is a deliberate choice of availability over correctness; when nobody records that choice, it becomes a silent wrong answer, which [[crash-early]] warns against for failures only a bug can produce.
- **Degraded mode** needs the system to know which functions it can still offer, which means a state for it; see [[finite-state-machine]].

Whichever option is chosen, this wiki places it inside the system's one error-handling strategy ([[consistent-error-handling-strategy]]) and its level inside the agreed robustness of the parts ([[uniform-robustness-level]]). Where in the call chain recovery may happen is [[recover-only-at-entry-points]].

## Source

[[code-complete]], ch. 3, section 3.5 («Отказоустойчивость»), Russian edition, pp. 47-48: the definition and the options. Taking the level as given, the trade-offs and the placement under *How this wiki uses it* are this wiki's own.
