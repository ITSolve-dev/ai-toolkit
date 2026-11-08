---
title: Keep objects small
category: objects
summary: "A class stores more than four fields (Elegant Objects conventions) or more than about seven (elsewhere, after Code Complete), its constructor takes more than five parameters, fields share a prefix that names a missing child object (cardNumber, cardExpiry on a payment, often with logic interpreting them), or a Builder exists to assemble it."
tags: [rule, object-size, encapsulation, constructors, cohesion, object-identity, data-members]
paradigm: oop
sources: [elegant-objects, code-complete, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-02
updated: 2026-11-07
---

*Elegant Objects* sets a hard ceiling on what an object holds. In section 2.1 the cap is four encapsulated objects, «Четыре, не более» (p. 46); in an earlier reader discussion the author puts the ideal at one to four properties, «Определенно не больше пяти» (p. 26). A constructor with more than five parameters marks a badly designed class: «Любой класс с более чем пятью параметрами в конструкторе спроектирован плохо» (p. 34). The book rejects the Builder pattern as a cover for objects above that size.

## Rule

A class encapsulates no more than four objects (fields). If it needs more, the book says the class needs refactoring, without exception (p. 44). A class with too many constructor parameters is simply too big; split it into parts (p. 34).

The book's reasoning:

- **State is identity.** The set of objects a class encapsulates is the object's state, and that state is its identity. Two `Cash(29, 95, "USD")` objects should be equal, because an object is an aggregate of its parts and is nothing without them; a book is an aggregate of pages, a cover and an ISBN (pp. 44-45). The book counts reference identity separate from state, Java's `==` and default `equals()`, as a flaw of the language (pp. 44-45), and advises avoiding `==` on objects and always overriding `equals()` (p. 47). This wiki's limit: the book's "state is identity" assumes immutable objects, its own design in section 2.6 ([[immutable-objects]]). Overriding equality on a mutable object breaks it as a key in hashed collections once a field changes; see [[mutable-hash-key]]. Override equality only where the state does not change.
- **Identity is a set of coordinates.** A person is found by name and date of birth, a car by maker, model and year. More than four coordinates is, in the book's words, against common sense (p. 46).
- **A richer real-world thing is a tree, not a wide class.** A reader objected that two cars of the same maker, model and year are still different cars. The answer: a real car needs more attributes, but they are grouped into other objects. The car encapsulates a type and a VIN, and the type encapsulates maker, model and year (p. 46).
- **Size drives complexity.** The cap serves the book's broader claim that objects must be small, because size drives complexity and complexity drives maintenance cost (pp. 42-44).

The number itself has no grounding, and the author says so: «Я взял это число из головы, у меня нет никаких научных доказательств.» (p. 44).

*Code Complete* sets a looser number. McConnell advises being wary of classes with more than about seven data members (p. 140). The reason he gives is that a person can hold 7±2 discrete items in mind while doing other tasks (Miller, 1956); with more than seven, consider splitting the class into smaller ones (Riel, 1996). Lean to the upper bound when the members are primitives such as integers and strings, and to the lower when they are complex objects (p. 140).

Larman's *Applying UML and Patterns* argues for the small child object even when it is tiny. In his payment design he weighs whether `CreditCard`, `DriversLicense` and `Check` deserve classes of their own, notes the "first impulse" to "eliminate such fine-grained classes", and answers that "it is usually a more profitable strategy to use them; they often end up providing useful behavior and being reusable" (35.8, PDF pp. 810-811). His payoff: "the CreditCard is a natural Expert on telling you its credit company type (Visa, MasterCard, and so on)", worked out from the number's leading digit (p. 811), so the logic that interprets the fields gets one obvious home ([[information-expert]]).

On Builder, the book's position is that it does not solve the problem but masks it (p. 34). Its purpose is to help construct larger objects, and since large objects are the problem, the author calls using it a very bad idea (p. 26); in Chapter 2 he repeats that Builder exists to pass many parameters to a constructor and that the cure is to split the complex object into simpler ones (p. 61). The Builder statements in Chapter 1 come from the reader discussions printed after sections 1.1 and 1.2. A reader described the book's overloaded constructors as telescoping constructors, fine for a few parameters, and proposed Builder for five or more at the cost of more code and classes (p. 33). The reply on p. 34 is the author's answer.

Fowler and Beck's **Large Class** smell starts from the same count: "When a class is trying to do too much, it often shows up as too many fields. When a class has too many fields, duplicated code cannot be far behind" (*Refactoring*, 2nd ed., ch. 3, Large Class, PDF p. 96). They set no number. Their clues are the shared prefix: "common prefixes or suffixes for some subset of the variables in a class suggest the opportunity for a component" (PDF p. 96), as with `depositAmount` and `depositCurrency`, and fields that are not all used all of the time (PDF p. 96). They add a clue that lies outside the class: "The clients of such a class are often the best clue for splitting up the class" (PDF p. 97), when each client uses a different subset of its features. This wiki notes that the client clue needs a look at callers, so it confirms a split rather than raising it.

The catalogue entry **Extract Class** (ch. 7, PDF pp. 208-212) explains how such classes arise: they grow by small additions, each seemingly not worth a separate class, until the class "becomes too complicated. Soon, your class is as crisp as a microwaved duck" (PDF p. 209). Fowler's tests for where to split: a subset of the data and methods "seem to go together"; subsets of data "usually change together or are particularly dependent on each other"; and the question of what would happen if a piece of data or a method were removed: "What other fields and methods would become nonsense?" (PDF p. 209). A later sign is subtyping that affects only a few features, or features that need subtyping in different directions (PDF p. 209). The inverse, folding a class that no longer pulls its weight back into its user, is [[lazy-element]].

## Sign in code

- A class declares more than four instance fields in a project that follows *Elegant Objects* conventions, or more than about seven elsewhere (fewer when the fields are objects, up to nine when they are primitives).
- A constructor, primary or the one that receives every field, takes more than five parameters.
- A separate Builder class, or a chain of `with...` calls ending in `build()`.
- Constructors differ only in which subset of optional fields they set.
- Subclasses that override only the methods using one group of the class's fields, the subtyping sign of Fowler's Extract Class (PDF p. 209).
- Fields whose names share a prefix (`makerName`, `makerCountry`), or two or more fields that are always passed together, as consecutive arguments, to the same call or constructor (`street`, `city`, `zip`). These are a child object waiting to be named. Logic that interprets such a group (a card type from the number's prefix, an expiry check) sitting in the enclosing class or a utility strengthens the sign; this wiki takes that form from Larman's payment case.

This page owns the size of what an object holds. A class with more fields than the threshold of [[keep-objects-small]] for its setting (four, or about seven) or a constructor with more than five parameters belongs to [[keep-objects-small]]; a class over the line limit with fewer belongs to [[class-size]]. A class with no fields at all that reaches for static calls is on [[global-data]]. The count of public methods is a separate measure, on [[fewer-than-five-public-methods]] (section 3.1). A group of fields repeated across several classes is [[containment-or-inheritance]]; a group inside one class, shown by a shared prefix or by being passed together, is [[keep-objects-small]]. A long parameter list on an ordinary method, rather than a constructor, is [[limit-parameter-count]]. The number of collaborators a routine calls, or a class's method bodies reach beyond its fields, is [[limit-fan-out]].

## When not to apply

The book allows no exceptions to the ceiling. This wiki states these limits on its own:

- **The two sources set different numbers.** *Elegant Objects* says four fields, *Code Complete* about seven with the 7±2 adjustment. This wiki resolves it per setting: a project that follows *Elegant Objects* conventions uses four; elsewhere the threshold is about seven, about five when the fields are objects and nine when primitives (p. 140); below it, a split is a question, not a finding. In both settings a split is warranted only where the fields form groups used by different methods, which is what [[class-interface-coherent-abstraction]] tests.

- **The figures are arbitrary, by the author's own admission.** This wiki treats the count as a prompt to look for groups of fields that change together, or that together form one coordinate of the object. The repair applies only where such groups exist and have a name a reader would recognise. If no field belongs with any other, the class may simply be wide, and splitting only adds indirection.
- **A record whose shape is fixed from outside**, such as a row of an external table, a message of a wire format, a serialization DTO at the boundary or a configuration file, has as many fields as that format has. Splitting it invents a structure the format does not have. Common practice uses a Builder there, and for such data this wiki does not count the Builder as a sign. The domain object built from such a record is where this rule applies.
- **The grouped fields are only carried through and never interpreted**, and no rule attaches to them. A child class would hold data and no behaviour ([[class-with-only-data-or-only-behaviour]]). Larman's word is "usually", not "always"; this limit is this wiki's reading of it.
- **A cluster used by exactly one method** of the class. This limit is this wiki's own: the split adds a class and a link and removes little.
- **A project convention or framework** that requires flat entities, such as an ORM mapping, overrides the rule at the persistence boundary. A convention that uses Builder for objects with many optional settings, for example clients of external services, overrides this page for those classes.

## Repair

1. Group the fields that are always used together, validated together, or that together are one coordinate of the object, such as street, city and postcode.
2. Make each group an object with its own name under [[name-classes-for-what-they-are]], give it those fields, and move into it the behaviour that touched only the group.
3. Replace the fields in the original class with one field of each new type. Repeat until every class is at or below its setting's threshold.
4. Remove the Builder once the constructor takes the group objects, few enough to pass directly.

Fowler's Extract Class mechanics (PDF pp. 209-212): decide the split; create the new class, and rename the old one if its name no longer fits; create an instance of the new class in the old one's constructor; move fields one at a time, then methods, starting with those that are called rather than calling, testing after each move; review both interfaces and rename what fits poorly (he drops "office" once `officeAreaCode` and `officeNumber` live in `TelephoneNumber`); decide whether to expose the new class, and if so consider making it a value object. To reallocate features between two classes he sometimes inlines one into the other first and then extracts the new split (ch. 7, "Inline Class", PDF p. 213); the large intermediate class is then a step, not a finding.

For too many fields, Fowler and Beck use Extract Class on each group, or Extract Superclass or Replace Type Code with Subclasses where the component fits inheritance; each client's subset of features is a candidate class (PDF pp. 96-97). Their remedy for too much code, removing redundancy inside the class, is on [[class-size]].

## Before and after

```
class Car
  constructor(maker, model, year, vin, plate)
    ...five assignments...

Car.builder().maker(m).model(d).year(y).vin(v).plate(p).build()
```

```
class Car
  constructor(type: CarType, vin: Vin, plate: Plate)
    this.type = type
    this.vin = vin
    this.plate = plate

class CarType
  constructor(maker, model, year)
    ...three assignments...

Car(CarType(m, d, y), Vin(v), Plate(p))
```

The prefix case, with logic interpreting the group (Larman's credit card):

```
class CreditPayment
  field amount
  field cardNumber
  field cardExpiry

  method authorizerName()
    if cardNumber.startsWith("4") then return "visa"
    if cardNumber.startsWith("5") then return "mastercard"
```

```
class CreditCard
  field number
  field expiry
  method companyType()
    if number.startsWith("4") then return VISA
    if number.startsWith("5") then return MASTERCARD

class CreditPayment
  field amount
  field card: CreditCard
```

## Source

[[elegant-objects]]: the reader discussion on p. 26 (one to four properties, no more than five; Builder) and pp. 33-34 (telescoping constructors, the five-parameter ceiling, Builder as a mask); section 2.1, pp. 42-45 (size and complexity, state as identity, reference identity as a flaw of the language, the four-object cap and the admission that the number is arbitrary); section 2.1, p. 46 (coordinates, the car tree); p. 47 (avoid `==`, override `equals()`); p. 61 (against Builder). The car tree is the book's own example; the `plate` field, added to push the count past four, is this wiki's. This wiki's own: the signs as worded, the boundary with [[class-size]], [[global-data]], method counts and method parameter lists, every limit (including the one on value equality for mutable objects), the repair steps and the pseudocode.

[[code-complete]], Russian edition, p. 140 (about seven data members, the 7±2 adjustment for primitives and objects, Miller and Riel). This wiki's own: the per-setting resolution of the two thresholds and the split condition.

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.8 "Fine-Grained Classes?", PDF pp. 810-811: the case for fine-grained classes and the CreditCard as expert on its company type. This wiki's own: reading it as support for the prefix sign, the interpreting-logic form of the sign, the carried-through limit and the credit card pseudocode.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Large Class", PDF pp. 96-97: too many fields and the duplication that follows, the prefix and suffix clue, fields not always used, the client clue and the repairs for too many fields. This wiki's own for that part: reading the client clue as confirmation rather than a sign, and routing the too-much-code remedy to [[class-size]]. Ch. 7, "Extract Class", PDF pp. 208-212, and "Inline Class", p. 213: how classes grow, the tests for where to split, the subtyping sign, the mechanics and inline-then-extract. This wiki's own for that part: the subclass sign as worded and the one-method limit.
