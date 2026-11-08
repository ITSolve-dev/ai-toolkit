---
title: Refactoring warning signs (code smells)
category: change
summary: "Checklist run on a routine or class to find what to refactor: duplication, long routine or loop, poor cohesion, long parameter list, parallel edits, feature envy, overloaded primitive, tramp data, middle man, public data, subclass using little of its parent, setup/cleanup around a call, speculative code; Fowler's 24 smells (mysterious name, mutable data, loops, lazy element, temporary field, message chains, insider trading, data class, refused bequest, comments...) alongside; each routed to the page that owns it."
tags: [method, refactoring, code-smells, review, checklist]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell lists warning signs, after Fowler's "smells", that show code has degraded in maintenance or was weak from the start and needs refactoring (pp. 553-558). This page is the run-order for that list: read the code against each sign and open the owner page, which holds the limits and the repair. Several signs are stated only for object-oriented code; their pages say so.

## Procedure

Walk the routine or class under review through the list. For each hit, open the owner page before reporting: most signs have a stated case where they are acceptable.

This wiki assigns the neighbouring methods as follows. Choosing *which* units of a codebase to open first, by comparing counts across all of them, is [[metric-outlier-review]]. Reading one routine or class for what to refactor is [[refactoring-warning-signs]]. The scan of the code already in front of the reader, against fixed thresholds, is [[design-warning-signs]].

| Sign (pp. 553-557) | What to look at | Owner |
|---|---|---|
| Code is duplicated | the same fragment edited in parallel in several places | [[dry]] |
| Routine too long | a routine that does not fit on a screen; the book says such routines are rarely needed in object-oriented code (p. 553) | [[routine-length]] |
| Loop too long or too deeply nested | the loop body is a candidate to become its own routine (p. 554) | [[loop-length-and-nesting]] |
| Class has poor cohesion | many unrelated responsibilities | [[class-interface-coherent-abstraction]], [[cohesion]] |
| Class interface is not a consistent abstraction | members added for convenience at the cost of integrity (p. 554) | [[class-interface-coherent-abstraction]] |
| Too many parameters | a long list signals a poor routine abstraction (p. 554) | [[limit-parameter-count]] |
| Parts of a class change independently | two areas of responsibility in one class | [[class-interface-coherent-abstraction]] |
| One change touches many classes | the book's example: a checklist of about 15 classes to edit for each new output type (p. 554) | [[coupling]] |
| Parallel inheritance hierarchies; parallel case statements | a subclass in one tree forces a subclass in another; similar switches edited together | [[polymorphism-or-type-switch]] |
| Related data used together is not a class | the same group of values travels together | [[group-related-data-into-a-structure]] |
| Routine uses more of another class than its own | it belongs in the other class (p. 555) | [[tell-dont-ask]] when it writes back, [[information-expert]] when it only computes |
| Primitive type overloaded | money or temperature as a bare integer | [[replace-primitive-with-class]] |
| Class does too little | a class that no longer earns its name; consider deleting it (p. 555) | [[lazy-element]] for a class with state whose only behaviour is one simple function; [[class-with-only-data-or-only-behaviour]] for a class with no fields created to call one method; [[hide-delegate-or-remove-middle-man]] for a class that mostly forwards |
| Tramp data | data passed through a routine only to be passed on | [[tramp-data]] |
| Middle man does nothing | a class that only forwards calls | [[hide-delegate-or-remove-middle-man]] |
| One class knows too much about another | includes subclasses knowing too much of their parents (p. 555) | [[coupling]], [[train-wreck]], [[inheritance-tax]] |
| Routine has a poor name | the book says fix it now, because it only gets harder later (p. 555) | a vague verb, a number or a repeated receiver: [[routine-names]]; a name that a later change made untrue: [[rename-when-meaning-drifts]] |
| Public data members | blurs interface and implementation (p. 555) | [[uniform-access]] |
| Subclass uses a small fraction of its parent's routines | inherited by accident, not by is-a | [[delegate-to-services]] |
| Comments explain difficult code | «Не документируйте плохой код — перепишите его» (p. 556, quoting Kernighan and Plauger) | [[comment-why-not-how]] |
| Global variables | revisit with fresh eyes; isolate behind access routines (p. 556) | [[global-data]] |
| Setup code before a call, takedown code after | the interface asks the caller to do its work | [[pass-what-the-routine-uses]] |
| Code that seems it might be needed someday | design ahead of requirements | [[replaceable-code-over-forecast]] |

## Fowler's smells

Fowler and Beck's chapter on smells, in the second edition of *Refactoring*, gives the *when* of refactoring: a recognisable structure that suggests, and sometimes screams for, a refactoring (ch. 3, PDF p. 85). They refuse to give a threshold: "no set of metrics rivals informed human intuition", so the reader develops a sense of how many fields or lines are too many (PDF pp. 85-86). This wiki reads that refusal as a limit on every owner page: a smell names a shape to point at, and acting on it stays a judgement. Several smells carry an explicit strength in the source, such as a refused bequest that is usually too faint to clean, mutable data harmless within a couple of lines, and global data whose harm grows with the dose, so a hit is a reason to look, and the code can still be fine as it is.

| Smell (ch. 3, PDF pp. 86-99) | Owner |
|---|---|
| Mysterious Name | a vague verb, a number or a repeated receiver: [[routine-names]]; a name that a later change made untrue: [[rename-when-meaning-drifts]] |
| Duplicated Code | [[dry]] |
| Long Function | [[routine-length]], which routes each place to look to its owner |
| Long Parameter List | [[limit-parameter-count]] |
| Global Data | [[global-data]] |
| Mutable Data | [[mutable-data]], which routes each shape |
| Divergent Change; Shotgun Surgery | [[divergent-change-vs-shotgun-surgery]] |
| Feature Envy | [[information-expert]], or [[tell-dont-ask]] when it writes back |
| Data Clumps | [[group-related-data-into-a-structure]] |
| Primitive Obsession | [[replace-primitive-with-class]] |
| Repeated Switches | [[polymorphism-or-type-switch]] |
| Loops | [[replace-loop-with-pipeline]] |
| Lazy Element | [[lazy-element]] |
| Speculative Generality | [[speculative-generality]], which routes each shape |
| Temporary Field | [[null-field-hides-another-class]], or [[pass-state-dont-hoard-it]] for fields that only carry results within one algorithm |
| Message Chains; Middle Man | [[hide-delegate-or-remove-middle-man]], and [[train-wreck]] for chains longer than two steps |
| Insider Trading | [[coupling]], which routes each shape |
| Large Class | [[keep-objects-small]] for fields, [[class-size]] for lines |
| Alternative Classes with Different Interfaces | [[alternative-classes-with-different-interfaces]] |
| Data Class | [[no-getters-and-setters]] |
| Refused Bequest | [[delegate-to-services]] |
| Comments | [[self-documenting-code]], which routes each comment shape |

Some smells pull in opposite directions, and the source resolves them by setting: message chains against middle man, divergent change against shotgun surgery, and lazy element against long function. Each pair's owner states the condition that selects one side.

## Limits of the list

- Some signs are read from history, not from the code in front of the reader: the signs that parts of a class change independently and that one change touches many classes need the change log. This wiki notes that, under its charter, an inspector reports them only when that history is in hand, or when the parallel shape is itself visible (two switches over the same codes, two mirrored hierarchies).
- The book says of case statements and of tramp data that they are not bad in themselves (pp. 554-555). This wiki reads a hit as a question, not a finding.
- This wiki does not treat the list as complete. McConnell says so of his list of specific refactorings (p. 559), not of these signs.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 24.2 and its checklist, pp. 553-558, after Fowler (1999), with p. 559 for the remark on the list of specific refactorings. The routing to owner pages, the split against [[design-warning-signs]] and [[metric-outlier-review]], the note on history-dependent signs and the reading of the list as incomplete are this wiki's own.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3 "Bad Smells in Code", PDF pp. 85-99: smells as the when of refactoring, the refusal of metrics, and the smells in the table. This wiki's own for that part: reading the refusal as a limit on every owner page, and the routing.
