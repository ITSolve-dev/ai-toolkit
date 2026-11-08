---
title: Write replaceable code instead of forecasting
category: change
summary: "Code justified by a future need: a comment or name citing later extension on a hook, a parameter or a one-entry registry. With no stated need, a one-occupant pattern role belongs to do-not-force-a-design-pattern, and any other single-implementation layer to know-when-to-stop where a change adds it and minimal-but-complete-functionality in code as it stands."
tags: [rule, reversibility, speculative-design, speculative-generality, protected-variations, yagni, flexibility-mechanism]
paradigm: any
sources: [pragmatic-programmer, code-complete, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

The book's image is a driver outrunning the headlights: how far ahead we can see is limited, and what lies beyond is guesswork (pp. 163-165). The tip is «Избегайте предсказания будущего» (p. 166). The neighbouring pages are [[easier-to-change]], which gives the value behind this rule, and [[know-when-to-stop]], which this wiki uses to judge what a change adds past its need, where this page judges a design justified by a forecast. The way of working that follows from the same limit is [[small-steps-with-feedback]].

## Rule

Design for maintenance only as far as you can actually see (p. 165). The more a design has to predict, the greater the risk of being wrong, so instead of spending effort on an uncertain future, write replaceable code: «Старайтесь облегчить отказ от непригодного кода и его замену более пригодным кодом.» (p. 165). The book adds that replaceability also helps cohesion, coupling and DRY (p. 165).

*Code Complete* reaches the same rule from the other end: it lists code that seems it might be needed someday as a reason to refactor (pp. 557-558), opening with «Программисты очень плохо угадывают, какая функциональность» will be needed later (p. 557). To prepare for future requirements, make the code needed now clear and straightforward, so future programmers know what it does and does not do and can change it quickly and correctly; the book reports this as the experts' unanimous view (Fowler, 1999; Beck, 2000; p. 558). Its four reasons (pp. 557-558):

- Requirements for code designed ahead are not developed, so the programmer will likely guess wrong and the code will be thrown away.
- Even a close guess misses details that break its design assumptions, so the design is thrown away too.
- Later programmers assume the speculative code was written, tested and reviewed as carefully as the rest, and build on it only to find it does not work.
- The extra code adds complexity, testing and defect fixing, slowing the project.

Larman's *Applying UML and Patterns* gives the test that separates a forecast from a need, in the terms of [[protected-variations]] (25.4, pp. 596-597). A **variation point** is variation "in the existing, current system or requirements, such as the multiple tax calculator interfaces that must be supported". An **evolution point** is, in his words, one of the "Speculative points of variation that may arise in the future", points "not present in the existing requirements" (pp. 596-597). Protection at the first pays; at the second "the cost of engineering protection at evolution points can be higher than reworking a simple design" (p. 597). Earlier he puts the same bar on polymorphism: the variation should be "definitely motivated by an immediate or very probable variability", and "Be realistic about the true likelihood of variability before investing in increased flexibility" (25.1, p. 584). He reports two failures: an architect's scripting language and interpreter, added for flexibility and later removed because it "simply wasn't needed", and his own "generalize-itis" of writing superclasses of the classes he really needed, "for that future situation when it would really pay off", a situation that "never came" (p. 597). His summary: "Novice developers tend toward brittle designs, intermediate developers tend toward overly fancy and flexible, generalized ones (in ways that never get used)" (p. 597). This wiki reads the variation point as the "requirement already in hand" of the first limit below, and the evolution point as the forecast this page reports.

Fowler's *Refactoring* gives the test that decides when a forecast may still justify a mechanism (2nd ed., ch. 2, "Refactoring, Architecture, and Yagni", PDF pp. 74-76). A function written with general applicability in view invites a dozen parameters that could be added. Fowler calls these flexibility mechanisms and says they are "not a free lunch": they complicate the function for the one case it serves now, a missed parameter is harder to add among the others, and he often gets them wrong, so that "most of the time my flexibility mechanisms actually slow down my ability to react to change" (PDF p. 75). His alternative is to build software that solves only the currently understood needs, designed excellently for them, and refactor as needs change. Mechanisms that do not increase complexity, such as small well-named functions, are fine; "any flexibility that complicates the software has to prove itself before I include it". If callers do not pass different values for a parameter, it is not added; Parameterize Function adds it later (PDF p. 75). The decision test: "Only if I can see that it would be substantially harder to refactor later do I consider adding a flexibility mechanism now" (PDF p. 75). He insists this does not abolish architectural thinking; it rests on refactoring, without which it is not credible (PDF p. 75), and on [[self-testing-code]] (PDF p. 76).

**A disagreement inside Larman, resolved.** In the same chapter he also advises: given an abstract superclass C1, consider making an interface I1 that corresponds to the public method signatures of C1, so that "even if there is no immediate motivation" there is "a flexible evolution point for unknown future cases" (25.1, p. 584). That protects an evolution point, which his own contraindication warns against. This wiki resolves it per setting. The interface is justified where a hierarchy already exists, so a variation point is real, and the language allows single inheritance only, so a new variant might be unable to subclass C1; Larman's reason is that without the interface "any new polymorphic solution must be a subclass of AC, which is very limiting" (p. 584). It is also justified where the type is handed to code outside the module that cannot be changed with it ([[public-methods-implement-interfaces]]). Otherwise, with one implementation and code the team can change freely, the interface is left out: extracting it later is a mechanical refactoring.

## Sign in code

The book names no sign, so every item here is this wiki's own.

The sign is a stated forecast: a comment or name justifies code by a later need, such as `for future formats`, `extensible` or `in case we need`. It usually sits on a parameter or hook nothing uses, or on an interface and a registry with one entry.

[[know-when-to-stop]] counts those same constructs. The stated need selects the page: with one, the argument to answer is the forecast, and this page applies; with none, the count decides. A named pattern role (factory, strategy, observer, visitor) with one occupant is [[do-not-force-a-design-pattern]], in a diff or in code as it stands; any other single-implementation layer is [[know-when-to-stop]] where a change adds it and [[minimal-but-complete-functionality]] in code as it stands. A configuration key belongs to [[over-configuration]]. Existing code that no caller reaches apart from tests written only for it, with no forecast stated, is [[minimal-but-complete-functionality]]; this wiki reads *Code Complete*'s third reason as why it matters. The shapes a wrong forecast leaves behind, with no forecast stated, are routed by [[speculative-generality]]. Placing an interface boundary around code already being written, so a likely change stays inside one class, is [[anticipate-likely-changes]] and adds no code; a hook, parameter or registry added for a change that has not come is [[replaceable-code-over-forecast]].

This wiki reads the interpreter Larman reports (p. 597) as the same sign at a larger size: an embedded rule or script interpreter whose scripts all encode fixed behaviour, justified by flexibility to come. This wiki assigns it here when the justification is stated, and to [[know-when-to-stop]] when it is not.

This sign raises the question without settling it. Whether a variation is "very probable" in Larman's sense cannot be read from code either, so a reviewer reporting the sign asks for the requirement that motivates the variation rather than declaring it absent. A verdict needs what the code does not show: every call site, and whether the second case is already a requirement. Lacking those, report the construct and what must be checked, and do not call it a violation.

## When not to apply

- The book accepts designing for future maintenance as far as you can see ahead (p. 165). A requirement already in hand is not a forecast.
- This wiki adds a seam that pays today, such as one a test uses to replace a dependency.
- Larman's variation point: two or more implementations exist, or a requirement names them, like his several tax calculators (25.4, p. 596). Protection there is the point of [[protected-variations]].
- An interface beside an existing hierarchy in a single-inheritance language, under the resolution above (25.1, p. 584).
- This wiki adds decisions that are expensive to reverse, such as a stored data format or a published interface. There replaceability is unavailable, so some forward thought is justified; see the version-marker finding on [[anticipate-likely-changes]]. Fowler's test reaches the same place: a mechanism is considered only where adding it later by refactoring would be substantially harder (PDF p. 75); this wiki reads that as cases where callers cannot be changed with the code ([[parallel-change]]).
- Fowler: a mechanism that adds no complexity, such as extracting a small well-named function, needs no justification (PDF p. 75).
- This wiki's reading of Fowler's statement that this rests on refactoring: where the code has no tests and no safe automated refactoring is available, "refactor later" is not a real option, and the cost comparison has to count that.

## Repair

Delete the unused hook, inline the single implementation and drop the parameter. Keep the code behind a small surface, so a later change replaces it rather than extending it. Larman's stance is the same: the simple, "brittle" design is reworked "as necessary in response to the true change pressures" (25.4, p. 597). This wiki adds that the abstraction returns when the second variant arrives; Fowler names the refactoring that brings a parameter back, Parameterize Function (PDF p. 75).

## Before and after

```
# before
# Extensible so that other formats can be added later
interface Exporter:
    method export(report, options)

registry = { "csv": CsvExporter() }

function export_report(report, format = "csv", options = {}):
    return registry[format].export(report, options)
```

```
# after
function export_report_csv(report):
    return to_csv_rows(report.lines)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 163-166 for the rule, its reasoning and the first limit. McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]], section 24.2, pp. 557-558, citing Fowler (1999) and Beck (2000), for the second statement of the rule and its four reasons. Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 25.1, PDF p. 584 (the bar of very probable variability, the interface guideline) and 25.4, PDF pp. 596-597 (variation and evolution points, the cost comparison, the interpreter and superclass anecdotes, the novice and intermediate remark, rework under true change pressure). This wiki's own for that part: the reading of the two kinds of point against this page's sign and limits, the resolution of the interface guideline against the contraindication, the assignment of the interpreter sign, the split with [[do-not-force-a-design-pattern]], and the return of the abstraction with the second variant. Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 2, "Refactoring, Architecture, and Yagni", PDF pp. 74-76: flexibility mechanisms and their cost, building for current needs, the bar of proving itself, the refactor-later decision test and its dependence on refactoring. This wiki's own for that part: the reading of "substantially harder" as callers outside the change, and the no-tests limit. The signs, the other limits, the repair, the example and the assignments against [[minimal-but-complete-functionality]] and [[anticipate-likely-changes]] are this wiki's own.
