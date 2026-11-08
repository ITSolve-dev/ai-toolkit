---
title: Self-documenting code
category: documentation
summary: "Concept: code whose meaning a reader recovers only from a comment, or not at all (one-letter counters, a flag array named for a criterion rather than what it holds, loops whose ends cannot be seen) is repaired by names and structure, not by more comments."
tags: [concept, comments, naming, readability, documentation]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

**Self-documenting code** is McConnell's name for code that documents itself through programming style rather than through comments. He says the main contribution to documentation at the level of the source comes from good style, not from comments. He lists sound program structure, simple and plain approaches, good names for variables and routines, named constants in place of literals, clear layout, and minimal complexity of control flow and data structures (p. 761). Comments come after that: when the code is written well, «комментарии — всего лишь глазурь на пирожном читабельности» (p. 763).

The book also explains why documentation inside the code is worth more than external documentation. It sits closest to the code, so when the code changes it stays correct more often than any other kind (p. 761). This wiki reads that as the reason to put as much meaning as possible into the parts of the code that change anyway, its names and structure. An edit cannot leave those behind the way it leaves a comment or a separate document. The wider argument that the code is the one description that stays current is [[source-code-as-the-authoritative-description]].

## The book's example

Section 32.2 opens with a routine that has no comments and is still badly documented, because its names say nothing and its layout is rough (p. 762). It fills an array `meetsCriteria`, clears entries in nested loops over `i` and `j`, and prints the numbers that "meet criteria". The rewrite uses `primeCandidate`, `isPrime`, `factor` and `factorableNumber` and indents the bodies. Then a first glance shows that the routine has to do with prime numbers, and a second shows that it finds the primes from 1 to `num`. Of the first version the book says that after a couple of looks a reader still cannot tell where the loops end (pp. 762-763). Neither version has a comment, so the difference is style alone (p. 763). `factorableNumber` exists only to explain the operation, which the book's margin note ties to adding explanatory variables (p. 762).

This wiki notes something the book does not. In the edition read, the rewritten outer loop runs `factor < (num / 2)` where the original ran `i <= num / 2`, so for `num = 4` the rewrite no longer marks 4 as composite. A rename for readability is meant to leave behaviour alone. A changed bound slipped in alongside it is exactly what a reviewer of a "rename only" change should look for (see [[refactoring]]). The pseudocode below keeps the original bound.

```
// before
for i = 2 to num: flags[i] = true
for i = 2 to num / 2:
    j = i + i
    while j <= num:
        flags[j] = false
        j = j + i
for i = 1 to num:
    if flags[i]: print(i, "meets criteria")
```

```
// after
for candidate = 2 to num: is_prime[candidate] = true
for factor = 2 to num / 2:
    multiple = factor + factor
    while multiple <= num:
        is_prime[multiple] = false
        multiple = multiple + factor
for candidate = 1 to num:
    if is_prime[candidate]: print(candidate, "is prime")
```

## What the book's checklist asks

The chapter's checklist for self-documenting code (pp. 763-764) points to rules this wiki keeps on other pages. Grouped by where they show:

- **Classes:** the interface forms a consistent abstraction, the class name states its main purpose, and the class can be used as a black box. See [[class-interface-coherent-abstraction]].
- **Routines:** the name describes exactly what the routine does, each routine does one well-defined job, and parts worth extracting have been extracted. See [[routine-names]], [[routine-cohesion]] and [[extract-routine-to-name-a-step]].
- **Data names:** loop counters carry names more informative than `i`, `j`, `k`; well-named enumerations replace home-made flags and booleans; named constants replace magic numbers and magic strings; each variable serves only the purpose its name states. See [[loop-index-names]], [[enum-instead-of-codes-and-flags]], [[name-describes-what-the-variable-represents]] and [[named-constants-over-literals]].
- **Data organisation:** extra variables explain the code, references to a variable are grouped, and complex data is reached through access routines. See [[keep-variable-live-time-short]] and [[access-routines-at-domain-level]].
- **Control:** the nominal path is obvious, the normal case follows the `if` rather than the `else`, each loop does one job, nesting is minimal, and boolean expressions are simplified with extra boolean variables, boolean functions and decision tables. See [[nominal-path-first]], [[tame-deep-nesting]] and [[name-complex-conditions]].
- **Layout:** the formatting shows the logical structure. See [[layout-must-tell-the-same-story-as-the-logic]].
- **Design:** the code is simple and avoids clever tricks, implementation details are hidden as far as possible, and the program is written in terms of the problem domain rather than in computer-science or language structures. See [[rewrite-tricky-code]] and [[high-level-code-in-problem-terms]].

## Where comments still come in

The book does not conclude that comments are unnecessary. When code needs an explanation, it says the better move is almost always to improve the code and then add a summary or intent comment (p. 769); see [[comment-kinds]]. This wiki takes that order as the boundary between this concept and [[comment-why-not-how]]. A comment that restates or explains what better names and structure could carry shows that self-documentation failed. A comment heading a block whose result has a nameable meaning is [[extract-routine-to-name-a-step]]; a comment that restates steps, numbers or names the body already holds is [[comment-why-not-how]]. A comment that says what the code is for, or holds a fact the code cannot hold, is the comment self-documenting code still needs.

## Fowler: comments as deodorant

Fowler and Beck reach the same order from the smell side. Comments are not a bad smell, "indeed they are a sweet smell", but they are listed because "comments are often used as a deodorant" (*Refactoring*, 2nd ed., ch. 3, Comments, PDF p. 98): thickly commented code often has its comments because the code is bad, and after refactoring the comments often turn out to be superfluous (PDF pp. 98-99). Their rule: "When you feel the need to write a comment, first try to refactor the code so that any comment becomes superfluous" (PDF p. 99).

They pair three comment shapes with repairs (PDF p. 99), which this wiki routes to the owners:

- A comment explaining what a block of code does: Extract Function, named after the comment. A comment heading a block whose result has a nameable meaning is [[extract-routine-to-name-a-step]]; a comment that restates steps, numbers or names the body already holds is [[comment-why-not-how]].
- A comment explaining what an already extracted function does: Change Function Declaration, to rename it. A comment, above a declaration or inside a body, that restates steps, numbers or names the body already holds belongs to [[comment-why-not-how]]; a doc comment that says what a vaguely named class or method is for, without restating its body, belongs to [[tests-instead-of-documentation]]. A name shape listed on [[routine-names]] (a vague verb, numbered siblings) is that page's.
- A comment stating rules about the required state of the system: Introduce Assertion. The owner is [[assert-the-impossible]].

They also name the comments that stay: a comment that marks uncertainty ("A good time to use a comment is when you don’t know what to do") and one that explains why something was done, which helps future modifiers, "especially forgetful ones" (PDF p. 99). This wiki reads those as the same boundary as above: the reason-giving comment is what [[comment-why-not-how]] asks for.

## Source

[[code-complete]], ch. 32, section 32.2 (pp. 761-764). The book's parts: the claim that style is the main contribution to documentation in the code, the reason internal documentation stays correct longer, the prime-sieve pair and its reading, the role of `factorableNumber`, and the checklist. This wiki's own parts: the note on the changed loop bound, the reading of why names outlive comments, the mapping of checklist items to other pages, the boundary with [[comment-why-not-how]], and the pseudocode. The quotation on p. 763 was rejoined across a line break of the raw extraction and should be checked against the page image.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Comments", PDF pp. 98-99: comments as deodorant, the rule, the three shapes and their repairs, and the comments that stay. This wiki's own for that part: the routing of each shape to its owner page.
