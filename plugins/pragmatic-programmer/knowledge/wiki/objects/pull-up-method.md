---
title: Pull Up Method and Pull Up Field
category: objects
summary: "Two or more sibling subclasses each define a method or field that their superclass does not declare, with the same body or the same use, possibly under different names (annualCost / totalAnnualCost): make the copies identical, then keep one copy on the superclass."
tags: [rule, inheritance, duplication, refactoring, pull-up]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Pull Up Method** moves a method that several subclasses each define, with the same behaviour, into their common superclass. **Pull Up Field** does the same for a field. Fowler presents them as a pair in *Refactoring* (2nd ed., ch. 12). The inverses are [[push-down-method-and-field]].

This wiki assigns the neighbouring cases as follows. Identical or near-identical overrides of a method the superclass already declares are [[shared-behavior-in-superclass-varying-step-polymorphic]]; identical methods or fields that sibling subclasses each define and the superclass does not declare are [[pull-up-method]]. Classes with no superclass of the project's own that repeat the same fields and a method over them, where every instance of each class would be a valid instance of one shared parent, are [[extract-superclass]]; repeated method bodies on classes whose instances would not be valid instances of one parent, or repeated without shared fields, are [[mixins-share-functionality]].

## Rule

When sibling subclasses hold duplicate methods or fields, make the copies identical and keep one copy, on the superclass. Fowler's reason is the general one against duplication: "Whenever there is duplication, there is risk that an alteration to one copy will not be made to the other" (PDF p. 390). He says pulling up a field cuts duplication twice: "I remove the duplicate data declaration and I can then move behavior that uses the field from the subclasses to the superclass" (PDF p. 394).

Fowler gives these points on judging and ordering the work:

- Identical bodies point to a copy and paste. That is the easy case.
- Methods that differ only in values are parameterized first ([[parameterize-function]]), then pulled up as a separate step (PDF p. 390).
- Duplicate fields do not always have similar names: "The only way I can tell what is going on is by looking at the fields and examining how they are used" (PDF p. 394).
- If the body uses features that exist only on the subclasses, pull those features up first (PDF p. 391).
- Methods with the same overall flow but different details call for Form Template Method rather than Pull Up Method (PDF p. 391).
- In a language that declares fields only by assigning them, pulling up a field comes down to [[pull-up-constructor-body]] (PDF p. 394).

## Sign in code

- Two or more classes with a common superclass each define a method with the same body that the superclass does not declare, possibly under different names (Fowler's `annualCost` and `totalAnnualCost`, PDF pp. 391-392).
- Two or more sibling classes declare a field that is assigned and read in the same way, whatever it is called.

This wiki adds, as its own reading: the sign is a relation between siblings that a reader sees by putting the two classes side by side. A shared name with different bodies is not this sign.

## When not to apply

- The bodies look alike but use the fields differently. Fowler requires that the users of a field be inspected "to ensure they are used in the same way" (PDF p. 394). A chance likeness is not duplicated knowledge ([[coincidental-duplication]]).
- The methods share a skeleton but differ in steps. That case belongs to Form Template Method (PDF p. 391), which this wiki holds on [[shared-behavior-in-superclass-varying-step-polymorphic]].
- This wiki adds, as its own reasoning: if only one subclass or a minority of them would use the pulled-up member, pulling it up creates the shape that [[push-down-method-and-field]] removes.
- This wiki adds: where the project prefers composition to inheritance, the shared method goes to a collaborator both subclasses hold ([[choose-an-alternative-to-inheritance]]).

## Repair

Fowler's mechanics (PDF p. 391):

1. Inspect the methods to check they are identical. If they do the same thing but differ, refactor them until their bodies are identical.
2. Check that every call and field reference in the body can be reached from the superclass.
3. If the signatures differ, use [[change-function-declaration]] to get the one wanted on the superclass.
4. Create the method in the superclass and copy one body into it. Run static checks.
5. Delete one subclass method and test. Repeat until all are gone.

For a field (PDF p. 394): check that every user uses it the same way, rename the fields if the names differ, create the field on the superclass (accessible to subclasses), delete the subclass fields, and test.

Fowler also suggests a check that the tests alone may miss: "I usually find it valuable to look for the differences—often, they show up behavior that I forgot to test for" (PDF p. 390).

If the pulled-up body calls a member that each subclass supplies but the superclass does not declare, Fowler marks the duty on the superclass. In a static language that is an abstract method; in a dynamic one it is a trap method that throws a "subclass responsibility" error (PDF pp. 392-393), which tells future subclasses what they must provide.

## Before and after

```
class Party

class Employee extends Party
  monthlyCost(): ...
  annualCost(): return monthlyCost() * 12

class Department extends Party
  monthlyCost(): ...
  totalAnnualCost(): return monthlyCost() * 12
```

```
class Party
  annualCost(): return monthlyCost() * 12
  abstract monthlyCost()        // or a trap: throw SubclassResponsibility

class Employee extends Party
  monthlyCost(): ...

class Department extends Party
  monthlyCost(): ...
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 12, Pull Up Method, PDF pp. 389-393, and Pull Up Field, PDF p. 394: the motivation, the ordering points, the mechanics, the look-for-differences check and the subclass-responsibility trap. This wiki's own: the sign as worded, the owner assignments, the minority-use and composition limits, and the pseudocode.
