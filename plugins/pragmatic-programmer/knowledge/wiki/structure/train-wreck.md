---
title: Train wreck (chained method calls)
category: structure
summary: "An expression walks more than two dotted steps, fields or calls alike, through objects returned by other objects, or does the same through a run of temporaries each derived from the last."
tags: [rule, coupling, law-of-demeter, method-chains, protected-variations]
paradigm: oop
sources: [pragmatic-programmer, code-complete, larman-applying-uml-and-patterns]
created: 2026-11-01
updated: 2026-11-07
---

A train wreck is a chain of accesses in which each step reaches through the object returned by the previous one. The code at the head of the chain then depends on every link, so all those methods and properties are coupled together like wagons in a derailment (p. 170). The book's example crosses five levels of abstraction, and the top-level code must implicitly know that one object exposes a collection, that the collection has a find, and that the found object holds a further object with accessors (p. 170).

Larman's *Applying UML and Patterns* gives a third statement, under the name *Don't Talk to Strangers*. It was one of the nine GRASP patterns of his first edition and is now a special case of [[protected-variations]]: "a mechanism to achieve protection from structure changes" (25.4, p. 594). Its aim is "to avoid coupling a client to knowledge of indirect objects and the object connections between objects" (p. 595). Within a method, messages go only to these familiars: `this`; a parameter of the method; an attribute of `this`; an element of a collection that is an attribute of `this`; an object created within the method (pp. 594-595). Any object reached through a familiar's return value is a stranger. His measure is distance: "The farther along a path the program traverses, the more fragile it is" (p. 596), and the Demeter group named the law because they saw object structures change often and code coupled to them break often (p. 596). His examples grade it: `sale.getPayment().getTenderedAmount()` reaches one stranger and is "very slightly fragile", `sale.getPayment().getAccount().getAccountHolder()` is more fragile (p. 595). This wiki notes that his list, like McConnell's, leaves out global variables, and routes his first example, a two-step reach, to [[hide-delegate-or-remove-middle-man]] and his second, with three steps, here.

## Rule

«Не связывайте вызовы методов в цепочку» (p. 172). The working limit the book gives is: «Старайтесь связывать не более двух вызовов методов через точку» (p. 172).

This replaces the Law of Demeter, which the book reports was formulated by Ian Holland in the late 1980s. That law limits a method of class C to calling C's other instance methods, its parameters, methods of objects it creates, and global variables (p. 172). The authors keep its underlying principle but give up the formulation for two reasons: they no longer like global variables, and applying the law is like parsing a document on every method call (p. 172).

*Code Complete* reaches the same rule from coupling. McConnell writes that direct connections are rather dangerous, and indirect ones such as `account.ContactPerson().DaytimeContactInfo().PhoneNumber()` are more dangerous still (p. 146). He states the Law of Demeter (Lieberherr and Holland, 1989) as: object A may call any of its own methods; if it creates object B it may call B's methods, but should not call methods of objects returned by B. So `account.ContactPerson()` is acceptable and `account.ContactPerson().DaytimeContactInfo()` should be avoided (pp. 146-147). He calls this a simplified explanation and points to *The Pragmatic Programmer*, Larman and Page-Jones (p. 147). More generally he asks to minimise a class's collaboration with other classes, including the number of calls on objects returned by other created objects (p. 147); the count of collaborators is owned by [[limit-fan-out]]. This wiki notes that his example has three steps and so meets this page's sign, and that his formulation, unlike the one *The Pragmatic Programmer* reports, says nothing about global variables. His line also falls one step earlier: he rejects a two-step chain, which this page's sign lets pass. This wiki resolves that by shape rather than by choosing a book: with more than two steps [[train-wreck]] owns the sign; a two-step reach (`a.b().c()`) is owned by [[hide-delegate-or-remove-middle-man]], so McConnell's two-step case is reported there, not here.

## Sign in code

Count every step after the receiver in an expression that navigates from one object to objects it holds, field or call alike: more than two is the sign. This wiki counts fields too, because the book's own bad example on p. 173 has only two calls with parentheses beside two field reads.

The same chain split across lines is still the sign. The book is explicit that intermediate variables count (pp. 172-173). The shape is a run of assignments where each right-hand side is a member of the variable assigned on the line before.

This wiki assigns the neighbouring case as follows. A chain of at most two steps that sits on the left of an assignment or inside a loop, or one that walks the links of a single self-referential structure (node.next.previous), is [[explaining-variable]]; a longer chain through objects of different application or third-party types is [[train-wreck]], and naming it locally does not repair it. A client reaches through B's accessor to call C. With more than two steps [[train-wreck]] owns the sign; a two-step reach (`a.b().c()`) is owned by [[hide-delegate-or-remove-middle-man]]. Where that two-step chain sits on the left of an assignment or inside a loop, its naming stays with [[explaining-variable]]. A path of indexing into a plain data structure with no routines of its own is [[replace-direct-data-manipulation-with-adt]]; a chain of steps through objects returned by other objects is [[train-wreck]].

## When not to apply

- The book's stated exception: the rule does not apply when what is chained is unlikely to change at all (p. 173). It warns that in an application almost anything can change, and that anything in a third-party library should be treated as volatile, especially if its maintainers change the API between releases. Libraries that ship with the language are likely to be stable, so chains over those are acceptable (p. 173).
- Larman gives the same exception from the other side: "it is not always necessary to protect against this; it depends on the instability of the object structure" (25.4, p. 596). Connections in standard libraries are relatively stable, mature systems are more stable, and new systems in early iterations are not; of his one-stranger example he says "Realistically, this is unlikely to be a problem" (p. 595). This wiki reads his "early iterations" as a reason the check by origin below counts the application's own types as volatile.
- This wiki turns that forecast into something readable: check where the chained types come from. Types from the language's standard library are outside the rule, while types from the application or a third-party package are inside it.
- Pipelines are not train wrecks. In a pipeline, data is transformed and passed from one function to the next, and nothing relies on hidden implementation details. A pipeline still couples through the data format passing between stages, but in the authors' experience this obstructs change much less (p. 173). See [[programs-transform-data]] and [[transformation-pipeline-over-method-chain]].
- The discriminating question, as this wiki puts it: does each step operate on a value it was handed, or does it step inside an object to reach something that object holds?
- This wiki also excludes a fluent interface whose every call returns the same object, because the chain then traverses no structure. The book does not discuss that shape by name. Its answer to exercise 23 warns about a neighbouring one: a chain of the application's own methods binds each returned object to the calling code, and a new step has no obvious home (p. 358). This wiki therefore keeps the exclusion to a builder that assembles one value, and does not extend it to a chain that does the application's work.
- A chain ending at a top-level concept can be accepted: [[tell-dont-ask]] gives the book's reasoning on why `customer.findOrder(id)` may stay public.

## Repair

Give the nearest object a method that does what the caller wanted, and repeat until the caller takes at most two steps. The book does this step by step in its discount example (p. 171), and [[tell-dont-ask]] holds the procedure. Larman's repair is the same: add an operation to the familiar that returns what the caller ultimately wants and hides how it was obtained, such as `sale.getAccountHolderOfPayment()` (25.4, p. 596). He names its cost: "Strictly obeying this law ... requires adding new public operations" (p. 596). This wiki reads that cost as a reason to prefer moving the behaviour the caller needed onto the familiar over adding a pass-through getter for every path; [[hide-delegate-or-remove-middle-man]] owns the choice when the familiar starts to fill with forwards.

Introducing temporaries is not a repair. The book counts that form as the same bad style (p. 173).

## Before and after

```
// before: the chain
temperature = fleet.vehicles.first().engine().temperature

// before: the same chain, spread out; still a violation
vehicles = fleet.vehicles
lead = vehicles.first()
engine = lead.engine()
temperature = engine.temperature
```

```
// after: the caller no longer knows how a fleet or a vehicle is built
temperature = fleet.leadVehicle().engineTemperature()
```

```
// not a violation: standard collection operations passing a value along
short_names = words.filter(isShort).map(lowercase).sorted()
```

## Source

[[pragmatic-programmer]], Topic 28, Russian edition, pp. 170-173: the rule, the Law of Demeter history, the treatment of temporaries, the exception and the pipeline distinction; p. 358 for the answer to exercise 23. This wiki's own: counting fields as steps, the split with [[explaining-variable]] and [[hide-delegate-or-remove-middle-man]], the check by origin of types, the discriminating question, the fluent interface limit, and the examples. The limit of two calls is given as the Russian edition states it.

[[code-complete]], Russian edition, pp. 146-147: the `account.ContactPerson()` example, McConnell's statement of the Law of Demeter, and the collaboration minimisation list. This wiki's own: the comparison of the two formulations, the routing of his two-step case to [[hide-delegate-or-remove-middle-man]], and the owner link to [[limit-fan-out]]. *Code Complete* gives no limits for this rule; the limits above are from *The Pragmatic Programmer* or this wiki's.

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 25.4 "Structure-Hiding Designs", PDF pp. 594-596: Don't Talk to Strangers as a special case of Protected Variations, the five familiars, the Register examples, fragility by distance, the stability limit and the repair with its cost. This wiki's own for that part: the routing of his two examples by step count, the note on globals, the reading of "early iterations" against the origin check, and the preference for moving behaviour.

Related: [[coupling]], [[protected-variations]].
