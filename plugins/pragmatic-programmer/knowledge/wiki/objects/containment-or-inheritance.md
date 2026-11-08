---
title: Containment or inheritance
category: objects
summary: "Several classes declare the same group of fields with no shared object holding them; a class extends one of its own parts, so the sentence 'every X is a Y' is false (Car extends Engine, Television extends Tuner); also the decision test (share data, behaviour or both; who defines the interface) that an extends clause raised elsewhere is judged by."
tags: [decision-rule, inheritance, containment, composition, is-a, has-a]
paradigm: oop
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-07
---

Containment means one class holds a primitive or another object as a member, the "has-a" relation; inheritance means one class is a more specialised version of another, the "is-a" relation (pp. 139-140). McConnell notes that the literature talks more about inheritance because it is complicated and error-prone, not because it is better (p. 139), and sums up: containment is usually preferable unless you are modelling "is-a" (p. 156). «Ради управления сложностью относитесь к наследованию с подозрением» (p. 146).

## Rule

The book's test, per what the classes share (p. 146):

| Classes share | Use |
|---|---|
| data, not behaviour | a common object contained in each |
| behaviour, not data | a common base class defining the shared methods |
| data and behaviour | a common base class defining both |

And on the interface: use inheritance when you want the base class to define your interface, containment when you want to control the interface yourself (p. 146). Two further cuts:

- «Не наследуйте реализацию только потому, что вы наследуете интерфейс, и не наследуйте интерфейс только для того, чтобы унаследовать реализацию» (p. 142). If you need the implementation and not the interface, contain (p. 142).
- Private inheritance to reach a contained class's protected members is a last resort; in practice it couples parent and child too closely and usually points to a design error to solve otherwise (p. 140).

Weisfeld's *The Object-Oriented Thought Process* names the same two ways of building classes from classes, inheritance and composition (p. 47), and separates them by the relation each models, is-a against has-a (pp. 43, 48). His test is to say the sentence aloud. A circle is a shape, as is a square, so `Circle` and `Square` extend `Shape` (p. 43); a dog is a mammal, as is a cat (p. 47). A TV has a tuner and a screen, a car an engine (pp. 47-48). Of the engine: «мы не можем сказать, что двигатель является экземпляром автомобиля. Это будет просто неправильно звучать» (p. 47). Of the TV: «Телевизор, несомненно, не является тюнером, поэтому здесь нет никаких отношений наследования» (p. 48). The reason on each side: a superclass keeps what several classes share in one place, because duplication is extra work and «может привести к ошибкам и несоответствиям» (p. 41); a part kept as its own object can be reused, as an engine built separately can go into different cars (p. 47). The book also notes that the use of inheritance is constantly debated and that many developers avoid it where they can (p. 21). This wiki reads the sentence test as deciding only between the two relations: a false is-a sentence rules inheritance out, and a true one does not by itself call for a subclass; the table above decides that.

Chapter 7 of the same book adds a second test and a closing position. The **change test**: if a change to `Shape`'s implementation breaks `Circle`, «то Circle в действительности не является конкретизацией Shape» (p. 143); a true specialization feels a parent's change in a natural and expected way (p. 143), which is the encapsulation cost of [[inheritance-weakens-encapsulation]]. His worked misuse is `Window extends Rectangle`: a window «может включать Rectangle (и даже много Rectangle); вместе с тем это ненастоящий Rectangle» (p. 144), so `Window` should hold its menubar, status bar and main view as rectangles rather than inherit from one (p. 144). He refuses the slogan "composition where possible, inheritance only where necessary": the point is that composition «является более подходящей в большем количестве случаев, чем наследование», not that it should be used whenever it can be, and both are to be used, but only in the fitting context (p. 150). He also warns that «злоупотребление композицией» raises complexity (p. 140); how far to decompose is [[base-class-with-one-subclass]]'s trade-off.

When inheriting, decide per method whether it is abstract-overridable (interface only), overridable (interface plus default implementation) or non-overridable (interface plus fixed implementation) (p. 142).

## Sign in code

- Several classes declare the same group of fields (same names, same meaning) with no object holding them. This is the "share data, not behaviour" row with no contained object, and this page owns it.
- A class extends another of which it is made, so the sentence "every <subclass> is a <superclass>" is false for them: a whole extending one of its parts (`Car extends Engine`, `Television extends Tuner`). This page owns that shape, by Weisfeld's sentence test (pp. 47-48). The same shape includes a class extending one thing of which it needs several (`Window extends Rectangle` beside further rectangle fields for its menubar and status bar, p. 144): one parent cannot supply several instances, so the relation is has-a. That reading of the plural is this wiki's.

This wiki assigns the neighbouring cases as follows. An existing `extends` clause is classified by its callers on [[choose-an-alternative-to-inheritance]], which uses this page's table as its decision criterion. A class that inherits from a container and so exposes its operations (`Stack` extending `List`) is [[mixed-abstraction-levels-in-interface]]. A subclass reading a concrete parent's fields is [[inheritance-tax]]. An `extends` clause whose is-a sentence is false because the subclass is a whole and the parent one of its parts is [[containment-or-inheritance]]; one where the sentence is true, or where the parent is a framework class, is classified on [[choose-an-alternative-to-inheritance]] and [[delegate-to-services]]. Repeated helper methods across siblings are [[mixins-share-functionality]]. Classes with no superclass of the project's own that repeat the same fields and a method over them, where every instance of each class would be a valid instance of one shared parent, are [[extract-superclass]]. A subclass whose fields identify one instance while its parent describes the kind is [[replace-superclass-with-delegate]]. A group of fields repeated across several classes is [[containment-or-inheritance]]; a group inside one class, shown by a shared prefix or by being passed together, is [[keep-objects-small]].

## When not to apply

- Where the classes also share behaviour over those fields and each is a true subtype by [[liskov-substitution-principle]], the book's table picks a common base class (p. 146).
- The books disagree on the base-class rows. This wiki resolves it per setting: in a project following *Elegant Objects* conventions the base class's shared methods are final ([[final-or-abstract]]); where the classes are not substitutable for one another, [[delegate-to-services]] applies instead of the base-class rows.
- This wiki adds: the shared field names may be a chance likeness, as when two classes both have `name` meaning different things. The group must mean the same thing in each class; see [[coincidental-duplication]].
- Shared behaviour across unrelated classes may also be served by [[mixins-share-functionality]] or [[multiple-inheritance-only-for-mixins]]; the table does not consider them. This remark is this wiki's.
- The sentence test needs names that mean what they say. Where class names are technical (`BaseHandler`, `AbstractProcessor`), the sentence cannot be judged from the code, and the clause goes to [[choose-an-alternative-to-inheritance]]. This limit is this wiki's own.

## Repair

Extract the repeated fields into a class of their own, give each former owner one member of that type, and move into it the behaviour that touched only those fields.

For a whole that extends its part: replace the inheritance with a field holding the part, and have the whole delegate to it the operations it needs, exposing on its own interface only what its users require.

## Before and after

```
class Invoice  { street, city, zip, total }
class Shipment { street, city, zip, weight }
class Customer { street, city, zip, name }
```

```
class Address  { street, city, zip }
class Invoice  { address: Address, total }
class Shipment { address: Address, weight }
class Customer { address: Address, name }
```

A whole that extends its part:

```
class Engine
  start()
  rpm()

class Car extends Engine
  drive()
    start()
```

```
class Engine
  start()
  rpm()

class Car
  private engine
  constructor(engine)
    this.engine = engine
  drive()
    engine.start()
```

## Source

- [[code-complete]], pp. 139-140 (containment, private inheritance), p. 142 (kinds of inherited methods, inherit only what you want), p. 146 (the table and the interface test), p. 156 (key points).
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 1: p. 21 (the inheritance debate), p. 41 (the duplication argument for superclasses), p. 43 and p. 47 (is-a, shapes, mammals), pp. 47-48 (has-a, the car and engine, the TV and tuner, two ways to build classes). The quotations were checked against `raw/`. This wiki's own for that part: the reading of the sentence test as deciding only between the two relations, the whole-extends-part sign, the technical-names limit, the repair and the `Car` pseudocode. Ch. 7: p. 140 (overuse of composition), p. 143 (the change test), p. 144 (`Window` and `Rectangle`), p. 150 (the closing position); the quotations were checked against `raw/`. This wiki's own for that part: the plural-instances reading.
- This wiki's own: the sign, the owner assignments, the reading of the table as a limit on this sign, the per-setting resolution against *Elegant Objects*, the chance-likeness and mixin limits, the repair wording and the pseudocode.
