---
title: Uniform access
category: objects
summary: "Code outside a class reads or writes an object's fields directly (public fields, or fields reached past the object's methods), so turning a stored value into a computed one would change every call site and the class cannot know or control the change."
tags: [rule, encapsulation, accessors, interfaces, information-hiding]
paradigm: oop
sources: [pragmatic-programmer, code-complete, object-oriented-thought-process]
created: 2026-11-01
updated: 2026-11-07
---

Uniform access means that callers use one notation for a module's services, whether a service is stored or computed. The book reaches it from [[stored-derived-data]]: the line class could add a cache because callers went through methods.

## Rule

The book's premise: «всякий раз, когда модуль раскрывает структуру данных, весь использующий ее код привязывается к реализации этого модуля» (p. 66). It therefore tells the reader to use accessor functions for reading and writing object properties wherever possible, which makes it easier to add functionality later (p. 66). The authors link this to Meyer's Uniform Access Principle from *Object-Oriented Software Construction*: all services of a module should be available through a uniform notation that does not reveal whether they are implemented through storage or through computation (p. 67).

*Code Complete* states the same rule from the class side: do not make data members public. Exposing them breaks encapsulation and limits control over the abstraction. McConnell cites Arthur Riel: a `Point` class exposing `float x, y, z` breaks encapsulation, because client code can do anything with the data and the class may not even learn that it changed (Riel, 1996). A `Point` with `GetX()`/`SetX()` and so on encapsulates well: you cannot tell whether the data is stored as floats, as doubles converted to float, or «хранит их на Луне и получает через спутник» (p. 136). He adds that encapsulation is a stronger concept than abstraction: abstraction lets you ignore details, encapsulation prevents you from knowing them even if you want to, and in his experience you have either both or neither (p. 135). See [[abstraction]].

Weisfeld's *The Object-Oriented Thought Process* makes the same rule the core of data hiding: «Для того чтобы скрытие данных произошло, все атрибуты должны быть объявлены как private», and «Объявление атрибута как public нарушает концепцию скрытия данных» (p. 37). Access to an attribute is controlled by the object that holds it, and «никакие другие объекты не должны напрямую изменять значения атрибутов этого объекта» (p. 35). His reason is the control argument rather than the representation one. When access is controlled, a wrong value can have been written in only one place, so a defect does not require tracing every fragment of code that might have changed the attribute (p. 37). His chapter 4 example is a defect traced to a `name` attribute that something overwrites with garbage: were `name` public, «вам пришлось бы просмотреть весь возможный код» to find the writer (p. 94). He names security, testing and maintenance as what gains, and adds that sensitive data such as passwords should not be read or written by uncontrolled code (p. 37). In chapter 10, explaining the `-` and `+` marks of a class diagram, he repeats the rule without exception: his book's approach declares attributes private «во всех ситуациях» (p. 197). A `+companyAge:int` is shown as an attribute that «любой класс сможет инспектировать или модифицировать» (p. 198). This wiki reads that as the control argument in notation. The book's remark there that Java's default access is `protected` (p. 199) is not carried over: the access it describes, limited to classes of one package, is package access, and the language detail is outside this wiki anyway. This wiki reads the two arguments together: an accessor protects the stored-or-computed choice, and routing every write through the owner keeps the set of possible writers to one class.

## Sign in code

- Code outside a class reads or assigns a field of that class's object directly, and the object has methods of its own, so it is not a plain record.
- A class (not a plain record) declares fields as public, and code outside the class assigns them.
- The same field name is accessed in many call sites, in a language or style where a field and a computed member are written differently.

This wiki assigns the neighbouring cases as follows. This page owns a bare read or write of a field. A read, a decision and a write back to the same object is [[tell-dont-ask]], where an accessor is no repair. A field bound by a rule is [[class-invariant]]. A direct write that undoes the effect of a public operation with no counterpart is [[provide-opposite-operations]]; any other bare write of a field is [[uniform-access]]. Fields of a structure with no routines of its own written from several call sites: [[replace-direct-data-manipulation-with-adt]]. Direct access beside access routines that already exist, or routines named in the implementation's terms: [[access-routines-at-domain-level]]. An object with methods of its own whose field is read or written outside it: [[uniform-access]]. A public field read or written outside its class is [[uniform-access]]'s sign; [[encapsulate-variable]] is its repair procedure.

## When not to apply

The Pragmatic Programmer says only «там, где это возможно» (p. 66), and *Code Complete* states no limit. The following limits are this wiki's own:

- Inside the class that owns the field there is nothing to shield. Between classes of one module the representation argument weakens, since every caller can change in one edit, but Weisfeld's control argument (p. 37) still holds for writes, so a write is reported and a read of an immutable field is not.
- An immutable public field, or a constant, cannot be overwritten, so Weisfeld's debugging argument (p. 94) does not hold for it; the representation argument still does where the value might later be computed.
- Where one notation already covers stored and computed members, a hand-written accessor adds nothing, and the sign does not arise. Such properties weaken the representation argument but not the control argument: every client can still set every value.
- Plain immutable records, whose shape is itself the contract, do not hide a representation. A plain data record or value with no invariant and no behaviour, such as a message or DTO, is data, not an [[abstract-data-type]]; public fields there hide nothing worth hiding, and making it immutable is the stronger protection. The page is marked `oop` for this reason.
- **Getters and setters are not the goal in themselves.** This wiki reads McConnell's point as access going through the class, which keeps the representation free to change. A trivial `get`/`set` per field still lets every client set every value, so it encapsulates the representation but not the class's control over its state. Whether a class should have accessors at all is [[no-getters-and-setters]]; this page owns only the bare field access. This reading is this wiki's own resolution between *Code Complete* (p. 136) and *Elegant Objects*.

This wiki adds a warning: an accessor for every field meets the letter of this rule and still exposes the shape. The rule protects the choice between stored and computed, not the object's encapsulation as a whole. That wider concern is [[tell-dont-ask]].

## Repair

Make the field private and route reads and writes through functions named for what they give the caller. Replace outside writes with operations named for the intent (`moveBy(dx, dy)` rather than `setX`), and add plain accessors only where callers need the value. Then change all external uses. A stored value can now become computed, or a computed value cached, without callers changing.

## Before and after

Before:

```
# in several callers; User has methods of its own
print user.display_name
```

After:

```
class User
    private display_name

    function display_name()
        return this.display_name

# in several callers
print user.display_name()
```

If the name is later assembled from a first and a last name, only `display_name()` changes.

A public field written from outside:

```
class Point
  public x; public y
  distanceTo(other)
...
point.x = point.x + dx
```

```
class Point
  private x; private y
  distanceTo(other)
  moveBy(dx, dy)
...
point.moveBy(dx, 0)
```

## Related

- [[minimize-member-accessibility]]
- [[replace-direct-data-manipulation-with-adt]]
- [[semantic-encapsulation-violation]]
- [[information-hiding]]

## Source

- *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 9, pp. 66-67, via [[pragmatic-programmer]], citing Meyer.
- [[code-complete]], ch. 6.2, Russian edition, pp. 135-136, citing Riel (1996): public data members, the `Point` example, encapsulation as stronger than abstraction. Merged here from the former page on public data members.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: p. 35 (no other object changes an object's attributes), p. 37 (all attributes private, the public attribute as a violation, one place of change, security, testing, passwords), p. 94 (the overwritten `name`), pp. 197-198 (private in all situations, what `+` permits). The quotations were checked against `raw/`. This wiki's own for that part: the reading of the two arguments together and the immutable-field limit.
- This wiki's own: the signs, all limits (including the getter resolution and the properties note), the warning about accessors for every field, the preference for intent-named operations over setters (the book shows plain accessors), the owner assignments, and the pseudocode.
