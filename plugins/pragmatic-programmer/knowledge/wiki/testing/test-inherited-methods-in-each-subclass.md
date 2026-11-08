---
title: Test inherited methods in each subclass
category: testing
summary: "A concrete subclass that adds state or overrides a method its inherited methods call, whose tests exercise only its own new methods while the inherited ones are tested only on the parent instance."
tags: [rule, testing, inheritance, test-coverage]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Inheritance saves rewriting code, not testing it. Weisfeld notes that `bark()` and `pant()` are written and tested once in `Dog`, then adds that «тот факт, что вам не нужно переписывать код, не означает, что вы не должны его протестировать» (p. 134). His reason: «Каждое новое отношение наследования создает контекст для использования унаследованных методов. Стратегия полного тестирования должна учитывать каждый из таких контекстов» (p. 134).

The same holds in the other direction. A change to a concrete parent reaches every subclass ([[inheritance-weakens-encapsulation]]); the book warns the ripple can make testing a nightmare and asks that classes depending on a changed class be retested (p. 142). This wiki reads that as running the subclasses' tests after a parent change.

## Rule

Run the tests of inherited behaviour against every concrete subclass, not only against the parent (p. 134).

## Sign in code

- A concrete subclass that adds fields or overrides a method that inherited methods call, whose test suite exercises only its own new methods; the inherited methods are tested only on a parent instance.
- The parent's tests construct the parent directly, and no test runs them against an instance of such a subclass.

Both signs are this wiki's own statement of the book's rule.

## When not to apply

- The subclass adds no state and overrides nothing the inherited methods call. The context is then the same, and the book itself calls a break here unlikely (p. 134). The book's main text already relaxes re-testing when nothing new is added (p. 134), while its side box asks for it always; this wiki follows the main text here.
- The parent method is abstract. Nothing is inherited to re-test; each subclass's own implementation is tested directly. This limit is this wiki's own.

## Repair

Write the inherited behaviour's tests once, parameterized over the instance under test (or as an abstract test that each subclass's test extends), and run them for every concrete subclass. This repair is this wiki's own.

## Before and after

```
test dog_pants
  d = new Dog()
  assert d.pant() is panting

test retriever_retrieves
  r = new GoldenRetriever()      // overrides breathRate(), which pant() uses
  assert r.retrieve() ...
```

```
for each make in [Dog, GoldenRetriever, LhasaApso]
  test pants(make)
    d = make()
    assert d.pant() is panting

test retriever_retrieves
  r = new GoldenRetriever()
  assert r.retrieve() ...
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 7, pp. 134, 142, via [[object-oriented-thought-process]]. The rule and its reason are the book's; the quotations were checked against `raw/`. This wiki's own: both signs, both limits (the first follows the main text of p. 134 over its box), the reading of p. 142 as running subclass tests, the parameterized repair and the pseudocode.

Related: [[test-the-contract]], [[liskov-substitution-principle]].
