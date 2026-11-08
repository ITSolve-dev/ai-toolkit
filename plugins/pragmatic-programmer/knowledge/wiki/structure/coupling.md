---
title: Coupling
category: structure
summary: "Concept: a class or routine tied to another so they change together; graded by size (parameter count, public methods), visibility (parameter against hidden global) and flexibility (how easily a new caller can use it); transitive; module-to-module dependencies are taken from the architecture."
tags: [concept, coupling, decoupling, change, grasp]
paradigm: any
sources: [pragmatic-programmer, code-complete, object-oriented-thought-process, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Coupling is a dependency between pieces of code that makes them change together. The book calls it hostile to change: it ties together components that must then move in parallel, so time goes either on tracking down every part that must change or on working out why something broke when only one of the coupled parts was changed (p. 168). Its slogan for the whole topic is «Развязанный код проще изменить» (p. 169).

## Why software wants the opposite of a bridge

The book contrasts a bridge with software. A bridge's rigid joints are what keep its shape, while software that expects change must flex, so a component should be tied to as few others as possible (pp. 168-169). This wiki reads the analogy as naming the cost of rigidity: what makes a structure strong is what stops one part from moving alone.

## Coupling is transitive

«И хуже того, связывание транзитивно.» (p. 169) If A is coupled to B and C, B to M and N, and C to X and Y, then A is coupled to all six. This wiki draws the consequence for review: counting a module's direct imports understates what can break it, because the count that matters is the reachable set.

## What counts as coupling

The book says its list of forms is somewhat artificial, since coupling can arise nearly any time two pieces of code share something (p. 169). The forms it treats are:

- chains of method calls: [[train-wreck]]
- global data, including singletons and external resources: [[global-data]]
- inheritance: [[inheritance-tax]]

Data pipelines also couple, because one function's output format must fit the next function's input, but in the authors' experience this obstructs change far less than a chain of calls does (p. 173). See [[train-wreck]] for the distinction.

## Signs the book names

Two of the book's four signs can be seen in code or in its history (p. 169):

- odd dependencies between unrelated modules or libraries
- a change that looks simple in one module, which spreads through unrelated modules or breaks something elsewhere

The other two are about people (developers afraid to touch code, meetings everyone must attend) and leave no mark in code, so this wiki records them only as a prompt to look for the first two.

This wiki adds a scope note: which modules may depend on which is the project's architecture and is taken as given. This page grades connections between classes and routines inside a module, and reports only a dependency that contradicts that architecture.

## The aim: shy code

The book closes the topic by asking for code that stays «скромным»: code that deals only with what it knows directly (p. 175). Its warning is that a change in coupled code can have side effects in hard-to-find places that surface only a month into production (p. 175).

This wiki reads decoupling as a matter of degree and not a state to reach, since the book itself accepts the format coupling of pipelines. A review finding should therefore name what the sharing costs at that site, and not merely that two things are connected.

## Code Complete's criteria and kinds

*Code Complete* defines coupling as the strength of the connection between a class or routine and other classes or routines, and uses "module" for both, since the idea is the same at both levels (pp. 96-97). The aim is few, direct, visible and flexible connections: «Отношения модулей должны напоминать отношения деловых партнеров, а не сиамских близнецов.» (p. 97) Its scale: `sin(angle)` is loosely coupled; `InitVars(var1, ..., varN)` is tighter, because its callers learn much of how it works from what they pass; two classes depending on how each uses one global are tighter still (p. 97).

The book's three criteria let a reader grade a connection in front of them (pp. 97-98):

- **Size**: the number of connections. A routine with one parameter is more loosely coupled than one with six; a class with four well-defined public methods than one with 37.
- **Visibility**: how prominent the connection is. Data passed in a parameter list is an obvious connection; data passed through a global is disguised and therefore worse; a global connection documented as such is slightly better. Programming, the book says, is not the CIA, and connections should be as loud as advertising (p. 97). See [[global-data]].
- **Flexibility**: how easily the connection can change, in practice how easily a new caller can use the module: «чем проще вызывать модуль из других модулей, тем слабее он сопряжен» (p. 98). The book's worked case is on [[pass-what-the-routine-uses]].

Its kinds, from acceptable to insidious (p. 98):

- **simple data-parameter coupling**: only primitive data passed through parameter lists, normal and acceptable;
- **simple object coupling**: a module instantiates an object, also fine;
- **object-parameter coupling**: object 1 requires object 2 to pass it an object 3, tighter, because object 2 must know object 3;
- **semantic coupling**: one module relies not on a syntactic element of another but on knowledge of its inner workings, the most insidious kind. See [[semantic-coupling]] and [[semantic-encapsulation-violation]].

The book's reason: a well-designed module is an extra layer of abstraction that can be taken as given once written, which lets a programmer think of one thing at a time. When using it requires holding its internals, global data changes and murky behaviour in mind at once, «сила абстракции исчезает» (p. 99). See [[managing-complexity]] and [[information-hiding]].

This wiki reads the two books as complementary: *The Pragmatic Programmer* says why coupling costs (change that spreads, transitively), McConnell gives the scale to grade one connection. A finding cites the criterion that fails at the site. A count of collaborators a routine reaches is [[limit-fan-out]].

## Weisfeld's test: does a change in one class force a change in another

Weisfeld's *The Object-Oriented Thought Process*, pointing to Scott Ambler's *The Object Primer* for more, gives a test rather than a measure: «если изменение, внесенное в один класс, приводит к изменению в другом классе, то эти два класса будут считаться тесно связанными» (p. 111). Maintainability comes from small manageable pieces and less interdependent code (p. 111). If classes are designed correctly, changes go only into an object's implementation, and «Изменений открытого интерфейса следует избегать любой ценой» (p. 111): changing `Cabbie.getName()` means finding, changing and recompiling every call site in every system that uses it, with a high chance of missing one (p. 111).

This wiki reads the test as separating two kinds of dependency. A dependency on a stable public interface is unavoidable and costs only when the interface changes; a dependency on an implementation (fields read directly, call order, undocumented side effects, the concrete subclass) is what the test flags, because the supplier's internal changes then break the client. See [[interface-and-implementation]] and [[semantic-coupling]]. Where a widely used signature must change, this wiki prefers adding the new method beside the old and retiring the old one.

## Larman: where coupling sits, and which coupling hurts

Larman defines coupling as "a measure of how strongly one element is connected to, has knowledge of, or relies on other elements" (17.12, p. 444) and credits Larry Constantine with identifying coupling and cohesion as critical principles in the 1960s (p. 447). He adds four things to the books above:

- **An inventory of where coupling sits in object code** (pp. 445-446). TypeX is coupled to TypeY when it has an attribute referring to a TypeY instance or to TypeY itself, calls on services of a TypeY object, references TypeY in a method by any means (a parameter, a local variable, a returned object), is a direct or indirect subclass of TypeY, or implements TypeY as an interface. This wiki uses the list as the checklist when two placements are compared on [[low-coupling]].
- **Subclassing is the strongest form.** "A subclass is strongly coupled to its superclass" (p. 446). His example is an abstract `PersistentObject` superclass that gives automatic persistence but couples domain classes to a technical service and mixes concerns. See [[inheritance-tax]] and [[delegate-to-services]].
- **Instability, not quantity, is the harm.** "High coupling to stable elements and to pervasive elements is seldom a problem" (p. 446); the problem is coupling to elements unstable in their interface, implementation or mere presence. "You cannot obtain an absolute measure of when coupling is too high" (p. 446), so one judges whether *raising* coupling at a given point will cause problems.
- **Coupling minimised to excess is a defect too.** It yields a few incohesive, bloated active objects doing all the work over many "passive zero-coupled objects that act as simple data repositories" (p. 446). That shape is [[god-class]]. Coupling and cohesion move together: "Bad cohesion usually begets bad coupling, and vice versa" (17.14, p. 464). See [[cohesion]].

This wiki reads Larman's instability point as agreeing with Weisfeld's test above and sharpening it: the dependency the change test flags is the one on something that changes. A dependency on a stable public interface or a pervasive library passes both. The decision rule built on this, comparing two placements, is [[low-coupling]].

## Fowler: insider trading and shotgun surgery

Fowler's *Refactoring* has two smells that are forms of coupling. **Insider Trading**: some exchange of data between modules is needed, but "we need to reduce it to a minimum and keep it all above board"; modules that "whisper to each other by the coffee machine" have to be separated (2nd ed., ch. 3, Insider Trading, PDF p. 96). He extends it to inheritance: "Subclasses are always going to know more about their parents than their parents would like them to know" (PDF p. 96). His repairs are Move Function and Move Field to reduce the need to talk; for common interests, a third module that holds the commonality, or Hide Delegate to make another module the intermediary; and for inheritance, "If it’s time to leave home", Replace Subclass with Delegate or Replace Superclass with Delegate (PDF p. 96). This wiki notes that splitting into modules is the project's architecture; inside a module it applies the same repairs as Move Function and Extract Class.

This wiki routes the code-visible shapes to their owners. Two classes that each read or write the other's fields are [[uniform-access]]; reading and writing back into one object is [[tell-dont-ask]]. A subclass reading a concrete parent's fields is [[inheritance-tax]], and protected fields of an abstract base are [[private-data-not-protected]]. This wiki adds one limit: classes designed as one unit, such as an iterator and its collection or a builder and its product, may share internals inside one module, because the smell is intimacy across a boundary the code itself draws.

**Shotgun surgery**, one change spread as small edits over many classes, is the history-side form of the warning sign "one change touches many classes" in [[refactoring-warning-signs]]. Its code-visible shapes and Fowler's repairs are on [[divergent-change-vs-shotgun-surgery]].

## Related

[[tell-dont-ask]], [[reversibility]], [[orthogonality]], [[event-driven-code]], [[temporal-coupling]], [[limit-fan-out]], [[circular-dependency]], [[cohesion]], [[low-coupling]].

## Source

[[pragmatic-programmer]], Topic 28, Russian edition, pp. 168-175. The reading of the bridge analogy, the review consequence of transitivity, the reading of coupling as a matter of degree and the scope note on dependencies between modules are this wiki's own. Related: [[coupling-hidden-in-language-features]].

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 5, p. 111: the change test after Ambler, avoiding public-interface changes, the `getName` ripple. The quotations were checked against `raw/`. The interface/implementation reading and the add-beside advice are this wiki's own.

[[code-complete]], ch. 5, section 5.3, Russian edition, pp. 96-99: the definition, the three criteria, the kinds and the reason. The reading of the two books as complementary is this wiki's own.

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 17.12, PDF pp. 444-447 (the definition, the inventory of forms, subclass coupling, stable and pervasive elements, no absolute measure, coupling to excess, Constantine), and 17.14, PDF p. 464 (cohesion and coupling together). This wiki's own: using the inventory as a checklist, and the reading of instability as agreeing with Weisfeld's test.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Insider Trading", PDF p. 96, and "Shotgun Surgery", PDF p. 91: the smell, the inheritance extension and the repairs. This wiki's own for that part: the routing to owner pages, the one-unit limit and the note on module splitting.
