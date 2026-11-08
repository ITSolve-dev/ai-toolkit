---
title: Speculative generality
category: complexity
summary: "Concept: hooks, parameters, abstract classes or delegation added for a need that nothing has yet (an abstract class with one trivial subclass, an unused or always-constant parameter, a pass-through delegating method or class, a function whose only callers are tests); each shape is routed to the page that owns it."
tags: [concept, speculative-generality, yagni, dead-code]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Beck and Fowler's **Speculative Generality** (they credit the name to Brian Foote) arises when people say "Oh, I think we’ll need the ability to do this kind of thing someday" and add hooks and special cases that are not required (ch. 3, Speculative Generality, PDF p. 94). The result is harder to understand and to maintain. Their verdict: "If all this machinery were being used, it would be worth it. But if it isn’t, it isn’t" (PDF p. 94).

This page holds the idea and routes each shape to its owner, which holds the limits and the repair. This wiki assigns the forward-looking choice, designing for replacement rather than for a forecast, to [[replaceable-code-over-forecast]]. This page names the shapes a wrong forecast leaves behind.

## The shapes and their owners

Fowler lists four shapes, each with its refactoring (PDF pp. 94-95):

| Shape | Fowler's repair | Owner |
|---|---|---|
| An abstract class that is not doing much | Collapse Hierarchy | [[base-class-with-one-subclass]]; an empty class of the pair is [[collapse-hierarchy]] |
| Unnecessary delegation | Inline Function, Inline Class | [[lazy-element]], [[hide-delegate-or-remove-middle-man]] |
| Functions with unused parameters, often added for variations that never came | Change Function Declaration | [[remove-unused-parameters]]; a parameter every caller passes with the same value is [[minimal-but-complete-functionality]] |
| The only users of a function or class are test cases | delete the test, then Remove Dead Code | [[minimal-but-complete-functionality]] |

Fowler puts the last one as a sign: "Speculative generality can be spotted when the only users of a function or class are test cases" (PDF p. 95). This wiki notes that it needs a search for callers, while the other three can be read from the code in front of the reader. The same shapes introduced by a diff under review belong to [[know-when-to-stop]].

## Limits this wiki adds

- An extension point that code outside the repository uses, such as a published library API or a plugin interface, has users that the search will not find.
- A seam that exists so that a collaborator can be substituted in tests is used. The tests are its purpose, and the "only users are tests" sign does not fire on it.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 3, "Speculative Generality", PDF pp. 94-95. The routing to owner pages, the note on which shapes need a caller search, and both limits are this wiki's own.
