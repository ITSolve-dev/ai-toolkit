---
title: "Replace Conditional with Polymorphism: the mechanics"
category: objects
summary: "Procedure for turning the same switch on a type code (play.type, kind) in several functions into a class hierarchy: host class, move the functions in, factory with the one remaining switch, then move one case at a time into subclass overrides, leaving a throwing tombstone and a default in the superclass."
tags: [method, refactoring, polymorphism, conditional, factory]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Replace Conditional with Polymorphism** turns a conditional that selects behaviour by a type code into a class hierarchy, where each subclass carries the behaviour for one case and the language's dispatch does the selecting. Fowler applies it in chapter 1 when the code has to support more kinds of play, "each with its own charging and volume credits calculations" (PDF p. 43).

This wiki assigns the sign as follows. The same type code switched on in several functions is [[polymorphism-or-type-switch]], which owns the sign; [[replace-conditional-with-polymorphism]] is the procedure for the repair. Whether the hierarchy is worth it, and where a switch stays, is decided there.

## Why Fowler does it

His reasoning: "conditional logic like this tends to decay as further modifications are made unless it's reinforced by more structural elements of the programming language" (PDF p. 43). His criterion for when it pays is the number of functions sharing the dispatch: "The more functions there are that depend on the same type of polymorphism, the more useful this approach becomes" (PDF p. 54). In the example, conditionals in two functions (`amountFor`, `volumeCreditsFor`) were reduced to one switch in a creation function. He also ties the structure to where change is expected: "If most of the changes will be to this code, it will be helpful to have it clearly separated like this" (PDF p. 53).

## Procedure

Fowler's sequence (PDF pp. 45-52), each step followed by compile-test-commit ([[refactor-in-small-tested-steps]]):

1. Create a host class for the varying behaviour (`PerformanceCalculator`) and construct it where the conditional functions are called.
2. Move the data the calculations need into it (Change Function Declaration to pass `play`), even data that does not vary, because "that consistency will make the code clearer" (PDF p. 46).
3. Move each conditional function into the class with [[move-function]].
4. Replace Type Code with Subclasses: replace the constructor call with a factory function that switches on the type code once and returns the right subclass.
5. Move one case at a time into an overriding method in its subclass. While the move is in progress Fowler makes the moved case in the superclass throw, so a dispatch error shows at once; it stays only for a couple more minutes (PDF p. 51).
6. When every case has moved, replace the superclass method with one that throws `'subclass responsibility'`: "it's kinder to my future self to leave a tombstone" (PDF p. 51).
7. Where most cases share one behaviour and only some vary, keep the common case in the superclass as a default and override it only in the variants, calling the superclass version where the variant extends it (volume credits: comedy adds a bonus to the default).

Chapter 10's catalogue entry adds details to the same mechanics (PDF pp. 303-316). While moving legs one at a time, Fowler replaces each moved leg in the superclass switch with a throw: "I put in the throw because I'm paranoid." (p. 306). Where the language needs no common type for dispatch, he still keeps the superclass "as it helps explain the way the classes are related in the domain" (pp. 308-309). For a base case with variants, the varying part of a superclass method is extracted into its own method first and only that is overridden, rather than copying the whole method down (pp. 314-315). A method introduced only for a subclass to override can itself hide what varies (p. 316); where its name joins two quantities with "And", Fowler splits it before naming (p. 315), which [[routine-names]] owns. The sign and the decision are on [[polymorphism-or-type-switch]].

The factory in the example is partly a language constraint: Fowler notes that constructors in his language cannot return subclasses (PDF p. 49). This wiki does not carry that reason over; the single creation switch stands on its own as the intended result on [[polymorphism-or-type-switch]].

## Example

```
function amountFor(perf, play)
    switch play.type
        case "tragedy": ...
        case "comedy":  ...
        default: fail("unknown type")

function creditsFor(perf, play)
    result = max(perf.audience - 30, 0)
    if play.type == "comedy"
        result += floor(perf.audience / 5)
    return result
```

```
function createCalculator(perf, play)
    switch play.type
        case "tragedy": return new TragedyCalculator(perf, play)
        case "comedy":  return new ComedyCalculator(perf, play)
        default: fail("unknown type")

class Calculator
    amount(): fail("subclass responsibility")
    credits(): return max(perf.audience - 30, 0)

class TragedyCalculator extends Calculator
    amount(): ...

class ComedyCalculator extends Calculator
    amount(): ...
    credits(): return super.credits() + floor(perf.audience / 5)
```

After the change only one switch on `play.type` remains, in the factory. Adding a kind of play means writing a subclass and adding one case to the factory (PDF p. 53).

## Trade-offs

The code grows again (PDF p. 53). Fowler also weighs whether the first phase of [[split-phase]] should return the calculator objects themselves instead of copying their results into plain data. He makes that choice depend on "who is using the downstream data structure" and in the example keeps plain data to hide the decision to use a polymorphic calculator (PDF p. 54).

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Reorganizing the Calculations by Type" through "Status: Creating the Data with the Polymorphic Calculator", PDF pp. 43-54; catalogued as Replace Conditional with Polymorphism (272), with Replace Type Code with Subclasses (362) and Replace Constructor with Factory Function (334). The decay argument, the usefulness criterion, the steps, the default-in-superclass move and the tombstone are Fowler's. This wiki's own: the assignment of the sign to [[polymorphism-or-type-switch]], the decision not to carry over the language reason for the factory, and the pseudocode.

Fowler, *Refactoring*, 2nd ed., ch. 10, "Replace Conditional with Polymorphism", PDF pp. 303-316, via [[fowler-refactoring]]: the paranoid throw, the kept superclass, the extraction of the varying part and the "And" name.
