---
title: Temporal coupling
category: structure
summary: "A comment says 'call X before Y' across objects or where the callee holds no state to check it, a sleep waits for a result, a flag makes callers take turns over work that shares nothing, independent backend calls run one after another, or an object built empty is completed by setters before use: the code depends on order in time and nothing states it."
tags: [rule, coupling, concurrency, ordering]
paradigm: any
sources: [pragmatic-programmer, elegant-objects]
created: 2026-11-01
updated: 2026-11-06
---

Temporal coupling is a dependency on time rather than on a name or a type. The book's definition is that the code constrains the sequence of the actions the task requires (pp. 213-214). This wiki reads the target as an order the task does not itself demand, because the book's worked example separates real dependencies from the written order (p. 216). The book treats time as a design element with two aspects, concurrency (things happen at the same moment) and ordering (their relative position in time) (p. 215).

## Rule

The book's position is that code should not depend on tick coming before tock if it is to stay flexible, and that calling several backend services strictly one after another is a way to lose customers (p. 214). Its examples of the coupling are a method A that must always be called before B, a report that can only be produced one at a time, and a button click after which the user must wait for a redraw (p. 215). Of this linear habit the book says: «Такой подход негибок и не очень реалистичен.» (p. 215)

The book's prescription is to allow for concurrency and to think about decoupling any time or order dependency. It claims the result is a system that is easier to reason about and potentially faster and more reliable (p. 215).

*Elegant Objects* names a narrower form of the same dependency at the call site: an object instantiated as an empty skeleton and then initialised by setters, so the lines that build it and the lines that use it must stay in one sequence that nothing enforces (pp. 81-83). Its rule is not to separate instantiation from initialisation: an object gets all of its state in one constructor call, so it cannot be used before it is complete (p. 83). If the setter lines are reordered by mistake, «логика поломается, но код все же скомпилируется» (p. 82). The reader has to keep the order in mind and the compiler does not help; with many objects, or with fifty lines between the setters, nobody can see that the order matters (p. 83). With a full constructor, the remaining lines cannot be swapped without a compile error. The book ties the pattern to JavaBeans, JPA and JAXB, which it describes as a bag of data with procedures attached: create the bag, inject data, then command it (p. 82). It lists the absence of this coupling among the benefits of [[immutable-objects]].

This wiki reads the damage as follows: the order lives only in the heads of the callers, so a new caller, or the same caller moved to a concurrent path, breaks it with no error at the point of the mistake.

## Sign in code

The constructs below are this wiki's own; the book gives examples of behaviour, not code shapes.

- A comment or docstring saying a call must come after another call.
- A fixed `sleep` or delay before reading a result something else produces.
- A module-level `busy` flag or lock around work that touches no shared mutable data, so callers wait for nothing but each other.
- Consecutive blocking calls to external services where the later call uses nothing returned by the earlier one.
- A no-argument constructor followed, at the call site, by two or more `setX(...)` calls on the same object before its first real use, or a use of the object placed between or before those setters. This sign is the shape *Elegant Objects* shows (pp. 81-82).

A call whose argument is the result of the previous call is not this sign. That is an ordinary data dependency, stated in the code.

This wiki assigns the neighbouring cases as follows. An order of destruction or ownership between two objects stated only in a comment is [[rewrite-tricky-code]]; an order of calls or of reading a result is [[temporal-coupling]]. An object built with a no-argument constructor and completed by setters before its first use belongs to [[temporal-coupling]]; an object already in use whose setter carries an intermediate result to a later method belongs to [[pass-state-dont-hoard-it]]. The class-side shape, a field reassigned after construction, belongs to [[immutable-objects]], with the null-field case as follows. A field left null by the constructor and filled by a setter, and code that branches on whether it is null to choose behaviour, is [[null-field-hides-another-class]]. A field left null and filled by a setter with no branch on its nullness is [[immutable-objects]] (class side) or [[temporal-coupling]] (call side). A second method that reads a field that only carries a result between steps is [[pass-state-dont-hoard-it]], which owns that sign, because a parameter removes the order. This page owns order imposed by timing, waiting or turn-taking, or stated only in a comment. Where a field carries a result between the ordered calls, [[pass-state-dont-hoard-it]] owns the finding even when a comment states the order. [[temporal-coupling]] owns an order stated in a comment only where no such field exists. A delay whose comment blames a dependency is [[select-isnt-broken]], which owns it and comes first, because a completion signal assumes a cause nobody has checked. A delay beside a run of overlapping calls is [[remove-calls-you-cannot-justify]]. A delay with no visible result being waited for is a question under [[comment-why-not-how]]. A precondition on a value or on the object's state stated only in a comment, and a public `initialize` the class declares as required before its other methods, are [[semantic-interface-to-programmatic]]. An order between calls on one object, stated only in a comment, where that object's own state could tell whether the first call happened, is [[semantic-interface-to-programmatic]]; an order across objects, or one the callee holds no state for, is [[temporal-coupling]]. A caller that skips a documented call because it knows another call makes it is [[semantic-encapsulation-violation]]. A comment in a class that demands particular values or a call order from callers and gives an internal or subclass quirk as the reason is [[semantic-encapsulation-violation]].

## When not to apply

- The order is real. The book's own worked example keeps its true dependencies: an ingredient goes in before the blender runs (pp. 216-217). The target is assumed order, not order the problem demands.
- The order is already enforced by shape, such as B taking a value only A can produce. This limit is this wiki's own.
- An explicit state machine that rejects an out-of-order call states the order instead of hiding it, as in [[finite-state-machine]]. This limit is this wiki's own.
- Running independent calls together has a price: the moment two steps overlap, the hazards of [[shared-state-is-incorrect-state]] apply to anything they touch. The book says finding the opportunity is the easy part and implementing it reliably is the hard part (p. 219). If the sequence is fast enough and nothing else runs alongside it, this wiki would leave a sequential call alone.
- A framework the project depends on instantiates objects through a no-argument constructor and setters (bean-style persistence or serialisation). The setter shape is then imposed from outside, and the book's only remedy is avoiding such frameworks (p. 82). This limit is this wiki's own.
- A builder object, which collects values through setters and then produces a complete object in one call, is not the setter sign, because the product cannot be seen half-built. The book does not discuss builders on these pages; this reading is this wiki's own, and whether the builder itself is needed is [[keep-objects-small]].

## Repair

The book's step is to find what is actually ordered, with [[find-what-can-run-concurrently]]. The specific repairs here are this wiki's own:

1. Turn the hidden order into data: the first step returns a value and the second takes it as a parameter, so a wrong order no longer compiles or no longer makes sense. See [[pass-state-dont-hoard-it]].
2. If two calls are always made together, merge them into one operation.
3. Start independent calls together and join on their results.
4. Replace a timed wait with a completion signal or a returned result.
5. For an object completed by setters, move every required value into the constructor: compute the values first, construct the object in one statement, then use it. The full constructor is the repair of *Elegant Objects* (p. 83); secondary constructors for optional values come from [[one-primary-constructor]].

## Before and after

```
start_export(job)
sleep(30)                         // hopes the export has finished
file = read_export(job)

customer = fetch_customer(id)     // blocks
offers = fetch_offers(region)     // uses nothing from the call above
```

```
file = start_export(job).wait()   // returns when the export has finished

(customer, offers) = join(fetch_customer(id), fetch_offers(region))
```

The setter form, before:

```
price = new Cash()
price.setDollars(29)
print(price)          // $29.00, the cents were not set yet
price.setCents(95)
```

After:

```
dollars = computeDollars()
cents = computeCents()
price = new Cash(dollars, cents)
print(price)          // $29.95, and there is no order to get wrong
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: the definition and examples, pp. 213-215; the limit that true dependencies stay, pp. 216-217; implementation being the hard part, p. 219.

This wiki's own: every item under `## Sign in code`, the assignment of the neighbouring cases, the limits marked as its own, the reading of the damage, the numbered repairs and the pseudocode. The book states the goal of decoupling but not these code-level steps. The definition on pp. 213-214 is reported as printed, and its reading as an order the task does not demand is this wiki's own.

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), see [[elegant-objects]], section 2.6, pp. 81-83: the setter form, its rule, the reasoning and the link to bean frameworks. This wiki's own for that part: the setter sign as worded, the split with [[pass-state-dont-hoard-it]], [[immutable-objects]] and [[null-field-hides-another-class]], the framework and builder limits, and the pseudocode.
