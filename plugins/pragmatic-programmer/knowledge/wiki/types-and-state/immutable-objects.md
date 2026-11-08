---
title: Immutable objects
category: types-and-state
summary: "A method reassigns a field after construction (a setter, in-place arithmetic like `this.x *= f`) instead of returning a new object, or a method mutates an object it received as an argument; fields not final; a setter whose only caller is the constructor."
tags: [rule, immutability, mutation, remove-setting-method]
paradigm: oop
sources: [elegant-objects, fowler-refactoring]
created: 2026-11-02
updated: 2026-11-07
---

Bugayenko defines an immutable object as one whose state cannot change after it is created: «Объект называется неизменяемым, если его состояние нельзя изменить после создания» (p. 74). All its fields are assigned once, in the constructor, and marked final. A method that would "change" the object returns a new object instead. This wiki notes that the book takes the most radical position on this of any source here: «изменяемые объекты не имеют права на существование» (p. 76). He does not say immutable classes are merely better in some situations (p. 76).

Fowler's *Refactoring* holds a narrower position, in **Remove Setting Method** (2nd ed., ch. 11, PDF pp. 370-373): "Providing a setting method indicates that a field may be changed" (PDF p. 371), so a field that should not change after construction is set only in the constructor and gets no setter. He keeps setters for fields that may change, such as a person's name in his example (PDF p. 372). This wiki uses his position where the project does not follow *Elegant Objects*: see the limits below.

## Rule

Make every class immutable. Assign fields only in the constructor and declare them final. A modifying operation such as `mul(factor)` returns a new instance carrying the new state, and leaves the receiver unchanged (pp. 74-75). The book's example: once `five` is created it can never become `fifty`. If fifty is needed, a new object is created (p. 75).

The reasons the book gives, from least to most important in its own ranking (p. 81):

- **Identity mutability.** A mutated object corrupts a hash container it sits in. See [[mutable-hash-key]] (pp. 78-79).
- **Failure atomicity.** A failure cannot leave the object half-updated. See [[failure-atomicity]] (pp. 79-81).
- **No temporal coupling.** There is no setter order to remember. See [[temporal-coupling]] (pp. 81-83).
- **No side effects through arguments.** A method that receives the object cannot alter it behind the caller's back (pp. 83-84). In the book's example, `print(price)` also calls `price.mul(2)`, and the caller's `five` silently becomes $10. Finding that in a large project can take days, in the book's estimate.
- **No NULL fields.** See [[null-field-hides-another-class]] (pp. 84-86).
- **Thread safety without locks.** In a two-field `mul`, a concurrent caller can see dollars multiplied but cents not, and print $60.20 for $15.10 × 2 × 2. The failure is hard to reproduce (pp. 86-87). Synchronisation fixes it, but the book says making a mutable class thread-safe is not easy, and that «синхронизация всегда снижает производительность» (p. 88). It also raises the risk of deadlock. See [[shared-state-is-incorrect-state]].
- **Smaller objects,** the author's favourite reason. All state arrives through the constructor, so growth shows as a swelling constructor and forces a split. See [[class-size]] and [[keep-objects-small]] (pp. 89-90).

The book also notes that renaming a mutable variable to something vague, like `money` instead of `five`, only hides the confusion. Pushed to its limit, every variable would be called `var` (p. 76).

## Sign in code

- A field without final (or the language's equivalent) that some method other than the constructor assigns.
- A `void` method that updates the receiver's own state, such as `this.dollars *= factor` or `setX(...)`, where a value-returning method would do.
- A method that receives an object as an argument and calls a mutator on it (the `print(price)` → `price.mul(2)` shape, p. 84).
- A setter whose only caller is the class's own constructor, which goes through its accessors even for its own fields (Fowler's first case, PDF p. 371).

This page owns the general sign "a field reassigned after construction". Narrower shapes belong to their own pages:

- setters called at the call site on an object built empty, including Fowler's creation script (`p = new Person(); p.name = ...; p.id = ...`, PDF p. 372): [[temporal-coupling]];
- the mutated object was put into a hash map or set earlier in the code at hand, or its class's equality/hash reads the mutated field and the class is used as a key in the code at hand: [[mutable-hash-key]];
- a method that writes a field of the receiver and can then throw or return before its remaining writes: [[failure-atomicity]];
- a field left null and filled later: A field left null by the constructor and filled by a setter, and code that branches on whether it is null to choose behaviour, is [[null-field-hides-another-class]]. A field left null and filled by a setter with no branch on its nullness is [[immutable-objects]] (class side) or [[temporal-coupling]] (call side).
- a field bound by a rule and exposed to a plain setter or a public write: on an entity under a mutable-entity convention [[class-invariant]], on a value whose state is its identity [[immutable-objects]];
- a class whose public methods are only accessors: [[no-getters-and-setters]], with this page's repair for the setter. On a class whose public methods are only accessors, the setter itself is also reported on [[immutable-objects]];
- a field computable from others and recomputed by a setter: [[stored-derived-data]];
- a holder's setter that writes a field of a nested object only that holder refers to, or copies of one logical record built per holder from one id: [[reference-or-value]];
- a field written by one method only for a later method to read: [[pass-state-dont-hoard-it]];
- mutable state that concurrent code reaches: [[shared-state-is-incorrect-state]];
- a container mutated in place behind a final field, which the book still counts as immutable: [[prefer-constant-objects]];
- A function that writes fields of a plain record or element it received as an argument is [[do-not-mutate-input-data]]; a method that calls a mutator on an object it received, or a class whose fields are reassigned after construction, is [[immutable-objects]].

When one of those shapes is present, that page carries the finding, and this page is cited only when none of them applies, apart from that setter. A container behind a final field that falls outside prefer-constant-objects' sign is no finding of this page; the book counts it as immutable (pp. 163-165).

## When not to apply

- **Lazy initialisation and caching.** The book concedes that, in Java and similar languages, a field loaded on first use cannot be final. Every way of combining lazy loading with immutability is a workaround, a cache built on a framework or a static map (pp. 77-78). This wiki reads that as a limit: where the cost of repeated loading is real, a mutable cache field is the accepted exception. The book points to its own cache example in section 1.3 (see [[constructors-without-code]]) for code that does not aim at pure immutability.
- **Frameworks that require bean setters.** JavaBeans, JPA, JAXB and similar standards build objects empty and fill them through setters. The book's answer is to keep away from them (p. 82). This wiki reads that as a limit: where the project's persistence or serialisation layer is built on such a framework, the project's convention governs the classes that layer maps, and the rule applies to the rest.
- **Models that are naturally mutable.** Vaccari objected in the comments that simulators and games are modelled naturally with mutable objects, and that code should stay close to the mental model. The author answers that both can be built from immutable objects, and that the mental model is what he wants to change (p. 93). This wiki resolves the dispute per setting: in a simulation or game loop where the team models the domain as state changing over time, the project's convention wins. Elsewhere the default is immutable.
- **The disagreement with *The Pragmatic Programmer*.** That book protects mutable state with invariants and mutators that keep them ([[class-invariant]]); this book rejects mutable objects outright (p. 76). This wiki resolves it per setting. For a value whose state is its identity (money, dates, ranges, identifiers, anything compared by value, used as a key or shared between threads), [[immutable-objects]] applies. For an entity in a codebase whose convention models entities as mutable objects behind guarded mutators, a mutator that keeps a stated invariant is judged by [[class-invariant]], and [[immutable-objects]] does not fire on it alone. Under that convention Fowler's narrower rule still applies to the declaration: a setter whose only callers are the class's constructor, or the setter lines right after construction, is reported here for the setter; the call-site sequence stays [[temporal-coupling]]'s.
- **A shared reference object.** Fowler's own stop: if a setter call cannot be replaced by creating a new object because it updates a shared reference object, abandon the refactoring (PDF p. 372); see [[reference-or-value]].
- **Allocation cost.** Creating a new object on every operation costs time. The book trades that cost for maintainability (p. 73, on a related case). This wiki's own limit is that the rule yields on a measured hot path, and not on a guess.
- **Immutable does not mean constant.** Asked how to build a tree that gains children at runtime, the author answers: «Неизменяемый объект — не значит константный» (p. 91). This wiki reads that as saying the object's own fields stay fixed while what it represents may change, for example by delegating to storage. Section 3.4 returns to the point in detail; see [[immutable-versus-constant-object]] and [[prefer-constant-objects]].

## Repair

1. Make every field final and assign it in the constructor.
2. Turn each mutator into a method that returns a new instance built from the current fields plus the change.
3. At call sites, bind the result: `fifty = five.mul(10)` instead of `five.mul(10)`.
4. If a class needs a field that some callers leave unset, split the class. Do not keep the field mutable.

For a single field that should not change, Fowler's mechanics (PDF pp. 371-372): if the constructor does not take the value, add it as a parameter ([[change-function-declaration]]) and call the setter from the constructor, adding the values of several setters at once if several go; remove each setter call outside the constructor, using the constructor argument instead, testing after each; inline the setter into the constructor and make the field immutable where the language allows.

## Before and after

```
class Cash
  field dollars
  method mul(factor)
    this.dollars = this.dollars * factor

five = new Cash(5)
five.mul(10)
print(five)        // prints $50: "five" no longer means five
```

```
class Cash
  final field dollars
  constructor(dollars)
    this.dollars = dollars
  method mul(factor)
    return new Cash(this.dollars * factor)

five = new Cash(5)
fifty = five.mul(10)
print(fifty)       // $50, and five is still $5
```

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 2.6, pp. 74-91, and the comments on p. 93; see [[elegant-objects]]. The book defers its answers to the counter-arguments to section 3.4 (p. 90). This wiki's own: the signs as worded, the ownership split, the reading of "not constant", the mutable cache field as an accepted exception, the limits on frameworks, games, the disagreement with [[class-invariant]] and hot paths, the remark on how radical the book's position is, and the pseudocode. The book states only the lazy-loading concession and its own replies to the objections. The quotation from p. 91 was checked against the page image.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 11, "Remove Setting Method", PDF pp. 370-373: the rule, the two cases, the shared-reference stop and the mechanics. This wiki's own for that part: the comparison with *Elegant Objects*, the use of his rule under a mutable-entity convention, the constructor-only-setter sign as worded, and assigning the creation script to [[temporal-coupling]].
