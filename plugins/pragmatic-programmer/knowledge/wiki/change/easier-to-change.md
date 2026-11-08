---
title: Easier to change (ETC)
category: change
summary: "Choosing between two workable shapes for code, with no rule deciding it: prefer the one that is cheaper to change later, and if unsure make the piece replaceable."
tags: [concept, change, design-values, design-quality, reversibility]
paradigm: any
sources: [pragmatic-programmer, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

ETC (Easier to Change) is the value Thomas and Hunt place under every other design principle: a design is good to the degree that it is easier to change than the alternative. The book states it as a tip, «Удачное проектное решение легче изменить, чем неудачное» (p. 58), and argues from the idea that a well-designed thing adapts to the people who use it, which for code means adapting to change.

## The reduction

The authors claim that every design principle they know is a special case of ETC (p. 58). Their three examples:

- Lower coupling separates concerns so that each is easier to change.
- Single responsibility means a change in requirements lands in one module.
- Good naming matters because code has to be read before it can be changed.

This wiki reads the reduction as a tool for an unforeseen case: when a principle seems to apply but its application makes the code harder to change, the principle is being followed past its purpose.

## A value, not a rule

The book says explicitly that ETC is a value, something that helps choose between courses, and not a rule (pp. 58-59). It should nudge decisions after a period of conscious reinforcement. The authors suggest asking, for about a week, whether what was just done made the whole system easier or harder to change, at each file save, test or bug fix (p. 59). The question they give is «Облегчило или же затруднило изменение всей системы в целом то, что я только что сделал?» (p. 59).

This wiki keeps ETC as a concept for that reason. It has no sign in code of its own: nearly any code can be called hard to change. Its use on a page is as the reasoning under a rule, while the sign comes from rules such as [[dry]], [[orthogonality]] or [[global-data]].

## Why the feedback loop depends on it

The section on agility returns to the claim and gives it a reason: «грамотное проектирование дает нечто, что изменить легче, чем при неграмотном проектировании» (p. 318). The argument comes from the feedback loop (see [[small-steps-with-feedback]]). You make a change, then discover that you do not like it, and step three of the recipe says to fix what you broke. For the loop to work, «такое исправление должно быть как можно более безболезненным» (p. 318). «В противном случае возникнет искушение оставить все как есть, без исправления.» (p. 318). The authors then point to [[software-entropy]] for what follows from leaving it (p. 318).

The closing step of the argument: «Если внести изменения нетрудно, то можно, не колеблясь, вносить соответствующие коррективы на каждом уровне.» (p. 318).

This wiki reads the argument as running from a human tendency, not from an abstract virtue of clean code. Costly repair leads to skipped repair, and skipped repair leads to accumulated damage. Good design here is what keeps the loop running.

## Fowler: ease of change as the test of good code

Fowler's *Refactoring* reaches the same value from the other side, as the criterion for judging a refactoring. He answers the argument over what good code looks like by naming a test beyond taste: "the true test of good code is how easy it is to change it" (2nd ed., ch. 1, PDF p. 55). Code should be obvious, so that someone who needs a change can "find the code to be changed easily and to make the change quickly without introducing any errors" (PDF p. 55).

- **Length is not the measure.** After [[split-phase]] his example grew from 44 to 70 lines, and again after [[replace-conditional-with-polymorphism]]. Fowler accepts this because the extra code separates the calculations from the layout and lets the HTML version reuse them: "Brevity is the soul of wit, but clarity is the soul of evolvable software" (PDF pp. 42-43). This wiki reads that as follows: a reviewer does not count added wrapper functions against a change by themselves; the question is whether a likely change now touches fewer places.
- **Structure is judged against the expected changes.** Fowler justifies grouping per-type calculations in subclasses with "If most of the changes will be to this code" (PDF p. 53). This wiki reads that as: where the expected changes lie elsewhere, the same structure is cost without benefit.
- **The camping rule and its balance.** Fowler states it: "Always leave the code base healthier than when you found it" (PDF p. 43). He pairs it with a limit: he always has to balance the refactorings he could do against adding new features, and "It will never be perfect, but it should be better" (PDF p. 43). This wiki reads the limit as: improving the code you touch is the goal, not finishing every refactoring that is possible. The occasions are on [[when-to-refactor]]; the same idea from the side of decay is [[broken-windows]].

## When the easier path is not visible

The authors name an assumption inside ETC: that a person can tell which of several paths will be easier to change later. Common sense usually can, but sometimes there is no hint (p. 59). They give two moves for that case:

1. Fall back on replaceability: «попытаться сделать заменяемым фрагмент кода, который вы пишете» (p. 59). Whatever happens, the fragment will not become a roadblock. The authors stress that this is no extreme measure, only keeping code decoupled and cohesive.
2. Treat it as training. Record the options and the guess about future change in an engineering log, and leave a tag in the source. When the code later has to change, compare the guess with what happened (p. 59).

## Failure modes

This wiki adds a warning the source does not state: replaceability read as a licence for speculative extension points produces abstraction that does not pay for itself. The book glosses the move as keeping code decoupled and cohesive (p. 59), and this wiki reads that as not licensing extension points. The book does not rule out layers as such: it asks for third-party APIs to be hidden behind them (p. 81), see [[hide-third-party-apis]]. See also [[replaceable-code-over-forecast]]. This wiki's test for telling the two apart: a design is easier to change when a likely edit touches fewer places, not when it has more extension points.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 8, pp. 58-60, Topic 11, p. 81, and Topic 48, p. 318, for the reasoning from the feedback loop, via [[pragmatic-programmer]]. This wiki's own: the reading of the reduction as a test for over-applied principles, the statement that ETC has no sign of its own, the reading of the feedback-loop argument as resting on a human tendency, and the warning and test under *Failure modes*.

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, PDF pp. 42-43 ("Status: Separated into Two Files"), p. 53 and pp. 54-55 ("Final Thoughts"): the criterion, the line counts, the clarity remark, the expected-changes justification and the camping rule with its balance. This wiki's own for that part: the reviewer reading of added length, the reading of expected changes, and the reading of the balance.
