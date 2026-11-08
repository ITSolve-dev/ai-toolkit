---
title: Replace Type Code with Subclasses
category: objects
summary: "A class with a type-code field (enum, string, number) that also carries fields or methods meaningful only for some codes (a quota only salesmen have, guarded by if type == \"salesman\"), or a constructor validating the code against a list; replace the code with subclasses, of the class itself or, if the type changes at run time or the class is already subclassed, of a separate type object."
tags: [rule, inheritance, type-code, polymorphism, refactoring]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Replace Type Code with Subclasses** turns a field that classifies an object (an enum, symbol, string or number) into a family of subclasses, one per value. In Fowler's 2nd edition it subsumes Extract Subclass and the 1st edition's Replace Type Code with State/Strategy (*Refactoring*, ch. 12, PDF pp. 401-409). Its inverse, for subclasses that no longer earn their keep, is [[subclass-that-differs-only-in-data]].

This wiki assigns the neighbouring cases as follows. A switch on a type code, in one routine or repeated in several, is [[polymorphism-or-type-switch]]; fields or methods meaningful only for some values of a type code, and the choice between subclassing the class itself or a separate type object, are [[replace-type-code-with-subclasses]]. The step-by-step move of switch arms into subclass overrides is [[replace-conditional-with-polymorphism]]. Subclasses made from a type code, each carrying fields or methods of its own kind, are [[replace-type-code-with-subclasses]]; a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]], even inside such a family. A switch whose arms only construct subclasses that override nothing but constants is [[subclass-that-differs-only-in-data]]; any other switch that only chooses which class to instantiate is [[factory-object-for-creation]]. A type code with no subclasses yet, whose value changes during the object's life, is [[replace-type-code-with-subclasses]] (indirect form); subclasses that already exist, where the object must change kind at run time, are [[replace-subclass-with-delegate]].

## Rule

Fowler starts from the plain case: "Most of the time, such a type code is all I need" (PDF p. 402). He names two situations where subclasses pay:

- **Conditional behaviour.** Several functions invoke different behaviour depending on the value of the type code (PDF p. 402). Subclasses let [[replace-conditional-with-polymorphism]] remove those conditionals.
- **Code-specific features.** Fields or methods are valid only for particular values of the type code, such as a sales quota that applies only to salesmen (PDF p. 402). A subclass with [[push-down-method-and-field]] makes the relation explicit, where validation logic would only guard it.

### Direct or indirect inheritance

Fowler sets out a choice, which this page settles by what the code shows:

- **Direct**: subclass the class itself (`Engineer extends Employee`). Fowler: "Using direct subclassing is simpler" (PDF p. 402).
- **Indirect**: give the class a type property whose class has the subclasses (`Employee.type` is an `EmployeeType`, with `Engineer extends EmployeeType`). Use it when either of Fowler's two conditions holds: the class's inheritance is already spent on another variation (his part-time and full-time subclasses, PDF p. 406), or the type is mutable (PDF p. 402). The route is [[replace-primitive-with-class]] on the code, then this refactoring on the new class.

Fowler now reads the old State/Strategy refactoring as this one using indirect inheritance (PDF p. 409).

## Sign in code

- Fields or methods meaningful for only some values of a type-code field, guarded by checks such as `if type == "salesman"`, or simply unset for the other values.
- A validation list of allowed codes in the constructor (Fowler's `validateType`, PDF p. 403) of a class that also has fields or methods used only for some codes.

## When not to apply

- The code is only carried and displayed, or one conditional reads it. Fowler: such a type code is all he needs most of the time (PDF p. 402).
- Direct subclassing cannot be used if the object's type changes during its life, or if the class already has subclasses for a different variation (PDF pp. 402, 406). Use the indirect form.
- This wiki adds, as its own reasoning: if the code comes from outside (Fowler notes it often does, PDF p. 402) and must round-trip unchanged, the subclasses still give back the literal. Fowler's subclasses do this by overriding the `type` getter, or `toString` in the indirect form. The selection point that maps literal to class is then the one place that still switches, and this wiki does not count it as a sign.
- Where the type changes as a control state the object's own methods reassign, the shape is a state machine ([[switch-on-state-vs-state-pattern]]). This limit is this wiki's own.

## Repair

Fowler's mechanics (PDF pp. 402-403):

1. Self-encapsulate the type code field ([[encapsulate-variable]]).
2. Pick one value, create its subclass, and override the type getter to return that literal.
3. Create selector logic from code to subclass. With direct inheritance, use [[factory-function-over-constructor]] and put the selector in the factory. With indirect inheritance it may stay in the constructor (PDF p. 402), or in the setter, as in Fowler's example (PDF p. 408).
4. Test. Repeat for each value, testing after each one.
5. Remove the type code field. Test.
6. Use Push Down Method and [[replace-conditional-with-polymorphism]] on methods that use the type accessors, then remove the accessors ([[remove-dead-code]]).

Fowler adds a check that the new path is really taken: "I then alter the return value of the engineer’s override and test again to ensure the test fails" (PDF p. 404). Once the factory's `switch` throws on an unknown code, the old validation is redundant and goes (PDF p. 405). In the indirect form Fowler keeps the empty `EmployeeType` superclass, because it makes explicit the relationship between the various subclasses and gives a home for shared behaviour such as capitalisation (PDF p. 408).

## Before and after

```
class Employee
  constructor(name, type)
    if type not in ["engineer", "manager", "salesman"] then fail
    this.name = name
    this.type = type
    this.quota = 0                       // used only when type == "salesman"
  quotaAttainment()
    if type != "salesman" then fail
    return sales / quota
  bonus(salary)
    switch type
      "engineer": return salary * 0.10
      "manager":  return salary * 0.15 + teamSize * 100
      "salesman": return sales * 0.05
```

```
function createEmployee(name, type)
  switch type
    "engineer": return new Engineer(name)
    "manager":  return new Manager(name)
    "salesman": return new Salesman(name)
    default:    fail "Employee cannot be of type " + type

class Employee
  constructor(name): this.name = name

class Engineer extends Employee
  bonus(salary): return salary * 0.10
class Manager extends Employee
  bonus(salary): return salary * 0.15 + teamSize * 100
class Salesman extends Employee
  quota
  quotaAttainment(): return sales / quota
  bonus(salary): return sales * 0.05
```

Indirect form, when the type can change:

```
class Employee
  setType(code): this.type = EmployeeType.create(code)
  toString(): return name + " (" + type.capitalizedName() + ")"
  bonus(salary): return type.bonus(this, salary)

class EmployeeType
  capitalizedName(): ...
class Engineer extends EmployeeType
  bonus(employee, salary): return salary * 0.10
class Manager extends EmployeeType
  bonus(employee, salary): return salary * 0.15 + employee.teamSize * 100
class Salesman extends EmployeeType
  bonus(employee, salary): return employee.sales * 0.05
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 12, Replace Type Code with Subclasses, PDF pp. 401-409: the two motivating situations, the direct/indirect criteria, the mechanics, the failing-test check and the kept empty superclass. This wiki's own: the signs as worded, the owner assignments (including the selecting sentences against [[subclass-that-differs-only-in-data]], [[factory-object-for-creation]] and [[replace-subclass-with-delegate]]), the limits about externally sourced codes and control states, and all pseudocode. Fowler's example shows only the type getter and `toString`.
