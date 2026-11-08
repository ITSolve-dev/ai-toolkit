---
title: "Low Coupling: choose the placement that adds no dependency on unstable elements"
category: structure
summary: "Of two workable placements for one responsibility, the chosen one adds a field, parameter, local, return type, superclass or implemented interface naming a class the other placement would not need (a reference kept only for one method); or an interface or adapter stands in front of a stable, pervasive dependency with no named reason to vary (a one-occupant pattern role is do-not-force-a-design-pattern, any other single-implementation layer is know-when-to-stop where a change adds it and minimal-but-complete-functionality in code as it stands)."
tags: [decision-rule, coupling, grasp, responsibilities, evaluation]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

**Low Coupling** is Larman's GRASP principle for choosing between alternative placements of a responsibility: prefer the one that keeps coupling low. It weighs candidates that [[information-expert]] and [[creator]] produce; it does not produce candidates itself. Larman calls Low Coupling "one of the cardinal goals in building software" (17.8, p. 428). The general concept, with Larman's inventory of where coupling sits, is on [[coupling]].

## Rule

"Assign responsibilities so that (unnecessary) coupling remains low. Use this principle to evaluate alternatives" (17.8, p. 428); 17.12 restates it as "Assign a responsibility so that coupling remains low" (p. 444). It is an *evaluative* principle: all other things being equal, prefer the design whose coupling is lower than the alternatives' (p. 428).

Larman's reason is that low coupling "tends to reduce the time, effort, and defects in modifying software" (17.8, p. 429). A highly coupled class is forced to change when the classes it depends on change, is harder to understand in isolation, and is harder to reuse (17.12, p. 444). It also explains why Expert works: Expert guides the choice toward low coupling (17.8, p. 429).

Larman's two worked comparisons:

- **Who creates the Payment** (17.12, pp. 444-445). Register creating it adds a Register-to-Payment dependency. Sale creating it adds none, because Sale must know Payment anyway, so the second design is preferred.
- **Who knows the balance** (18.4, p. 491). Sale and Payment are both partial experts. Giving `getBalance` to Payment would require Payment to gain a reference to Sale, raising overall coupling; Sale already holds the Payment it created, so the balance goes on Sale.

The same guideline appears for choosing a creator: "Choose an alternative with good cohesion, coupling, and stability in the presence of likely future changes" (18.4, p. 489).

## Sign in code

The sign is relative: it exists only when two placements of one responsibility are compared. This wiki generalises Larman's comparisons into a procedure:

1. Name the types the responsibility touches.
2. For each candidate placement, list the classes that must reference each type, using the forms on [[coupling]]: a field, a call, a parameter, a local, a returned object, a superclass, an implemented interface.
3. The placement that makes a class reference a type it did not reference before is the higher-coupling one.

Concrete forms in a diff, as this wiki reads them:

- **Too much coupling.** A new field or constructor parameter introduced solely so that one computation can live in a class holding a minority of its inputs, while another class already references all the parties (`Payment.sale`, kept only for `balance()`). A new import or parameter of a type the class did not depend on, added for one operation.
- **Coupling fought where it does not matter.** An interface, adapter or indirection in front of a dependency that is stable and pervasive, such as the standard library, with several callers and no named reason to vary. With one implementation and one caller, the owner is set by the assignment below. Larman: "if we put effort into 'future proofing' or lowering the coupling when we have no realistic motivation, this is not time well spent" (17.12, p. 446).

This wiki assigns the neighbouring cases as follows. A named pattern role (factory, strategy, observer, visitor) with one occupant is [[do-not-force-a-design-pattern]], in a diff or in code as it stands; any other single-implementation layer is [[know-when-to-stop]] where a change adds it and [[minimal-but-complete-functionality]] in code as it stands. For either, this page supplies Larman's reason that coupling to a stable element was not worth removing. A class that names a type only to construct it and hand it on is [[creator]]. A computation from another class's data alone is [[information-expert]]; one that mixes the computing class's own data with another's, where either class could hold it, is compared on [[low-coupling]]. This page supplies Expert's reason. One class holding all the logic over many passive data classes, which Larman calls coupling minimised to excess, is [[god-class]]. This page owns the comparison of whole alternatives: which of two classes should hold an operation, and whether a new dependency is needed.

## When not to apply

- **Coupling to stable and pervasive elements.** "High coupling to stable elements and to pervasive elements is seldom a problem" (17.12, p. 446). Larman's example is the standard Java libraries.
- **No absolute threshold.** "You cannot obtain an absolute measure of when coupling is too high" (p. 446). What matters is judging whether *raising* coupling at a given point will cause problems. This page therefore compares alternatives and does not count dependencies against a limit.
- **Not alone.** Larman says coupling "can't be considered in isolation from other patterns such as Expert and High Cohesion" (p. 446). When the lower-coupling placement lowers cohesion, [[cohesion]] has a say. Folding two collaborating classes into one removes the coupling between them and leaves one unfocused class; this wiki compares both and does not minimise coupling alone.
- **Some coupling is required.** No coupling at all goes against objects collaborating through messages (p. 446).
- **The future-evolution argument needs a known requirement.** Larman's stability clause (p. 489) weighs likely changes. This wiki reads it as usable in review only when the coming change is stated in the brief or the requirements; a forecast alone is [[replaceable-code-over-forecast]].

## Repair

Larman's guidance is "Pick Your Battles": "It is not high coupling per se that is the problem; it is high coupling to elements that are unstable in some dimension, such as their interface, implementation, or mere presence" (17.12, p. 446). Spend decoupling effort at points of realistic instability; his example is several third-party tax calculators with differing interfaces (pp. 446-447). Larman also says classes that are generic and likely to be reused should have especially low coupling (p. 446).

Elsewhere, move the responsibility to the candidate that already references the needed types, and remove the reference that existed only to serve it. Replace inheritance from a technical base class with delegation (see [[delegate-to-services]]). Remove an indirection that guards a stable dependency.

## Before and after

```
class Payment
    amountTendered
    sale                        // added only for balance()
    balance()
        return amountTendered - sale.total()
```

```
class Sale
    payment                     // Sale created it and holds it already
    balance()
        return payment.amount() - total()

class Payment
    amountTendered
    amount()
        return amountTendered
```

After the change only Sale knows both types, and Payment depends on nothing.

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 17.8, PDF pp. 427-429 (the definition, the rule, the reason, the link to Expert); 17.12, PDF pp. 444-447 (the problems of high coupling, the Register/Payment comparison, stable elements, no absolute measure, not in isolation, coupling to excess, Pick Your Battles, the tax calculators); 18.4, PDF pp. 489 and 491 (the stability guideline, the balance comparison).
- This wiki's own: the counting procedure as a general method, the diff forms as worded here, the owner split with [[creator]], [[information-expert]] and [[god-class]], the cohesion trade-off as phrased, the reading of the stability clause, and the pseudocode.
