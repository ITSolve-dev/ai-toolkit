---
title: Factory function over a constructor
category: objects
summary: "Call sites outside any factory pass a constructor a literal type code (new Employee(name, 'E')), or replace or wrap the object right after constructing it depending on arguments or environment (if remote: s = Proxy(s)); wrap creation in a named factory function."
tags: [rule, factory-function, constructors, creation, type-code]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Replace Constructor with Factory Function**, formerly Replace Constructor with Factory Method, puts a plain function in front of a constructor (*Refactoring*, 2nd ed., ch. 11, PDF pp. 373-376).

This wiki assigns the neighbouring cases as follows. A call site that invokes a constructor where a named factory function would lift a constructor's limits is [[factory-function-over-constructor]]; a domain class that branches on configuration or type to decide which concrete class to instantiate is [[factory-object-for-creation]]. Where the factory function is the one place that maps a type code to subclasses, the shape is [[replace-type-code-with-subclasses]]'s, and this page supplies its first step. A literal code passed to a constructor that only stores it is [[factory-function-over-constructor]]; a literal passed to a routine whose body branches on it is [[semantic-coupling]].

## Rule

Fowler lists the constructor's awkward limitations (PDF p. 374): in Java it must return an instance of the class it was called on, so it cannot return a subclass or proxy depending on the environment or the parameters; its name is fixed, so no clearer name can be used; and it often needs a special operator such as `new`, so it is awkward where a normal function is expected. A factory function has none of these limits (PDF p. 374): it will likely call the constructor, but can substitute something else.

## Sign in code

- A constructor called with a literal code that picks a kind, at a call site outside the factory functions (`new Employee(doc.leadEngineer, 'E')`). Fowler: "it’s generally a bad smell to pass a code as a literal string" (PDF p. 376).
- Code right after a constructor call that replaces or wraps the new object depending on arguments or environment (`s = new Staff(…); if remote: s = Proxy(s)`), or callers that tell variants apart only by constructor arguments.

## When not to apply

- The source gives none. This wiki adds: a constructor with one variant, called with data rather than a literal code, and with no need to substitute the class gains nothing from a wrapper; the indirection is the shape [[speculative-generality]] describes.
- In languages where the constructor is already an ordinary function that may return any value, the limits Fowler names may not exist; that is decided at work time from the language. This limit is this wiki's own.
- Where the project follows *Elegant Objects*, secondary constructors take this role instead of free functions ([[one-primary-constructor]]). This limit is this wiki's own reading.

## Repair

Fowler's mechanics (PDF p. 374): create a factory function whose body calls the constructor; replace each constructor call with it, testing after each; limit the constructor's visibility as far as possible. Where callers pass a literal code, create a factory per kind that embeds the code in its name (`createEngineer(name)`, PDF p. 376). This wiki notes that this is the same repair as for flag arguments in [[semantic-coupling]].

## Before and after

```
lead = new Staff(doc.leadName, "ENG")
hire = new Staff(doc.name, doc.staffType)
```

```
function createStaff(name, typeCode)
    return new Staff(name, typeCode)
function createEngineer(name)
    return new Staff(name, "ENG")

lead = createEngineer(doc.leadName)
hire = createStaff(doc.name, doc.staffType)
```

## Source

- [[fowler-refactoring]], ch. 11, Replace Constructor with Factory Function, PDF pp. 373-376: the constructor's limits, the mechanics, the literal type code smell, the per-kind factory.
- This wiki's own: the wording of both signs, the call-site qualifier and the second sign itself (the book gives the constructor's limits, not a shape in code), all three limits (the source gives none), the owner assignments, the link to flag arguments, and the pseudocode pair, after the book's employee example.
