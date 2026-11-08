---
title: Test environment matches production
category: testing
summary: "Production code branches on a test flag, an integration test runs on a different storage engine from production, or a test relies on a path, timezone or locale that exists only on one machine."
tags: [rule, test-environment, test-doubles, integration]
paradigm: any
sources: [pragmatic-programmer, object-oriented-thought-process]
created: 2026-11-01
updated: 2026-11-06
---

A passing test says the code works where the test ran. Each difference between that place and production is a condition the code never faced.

## Rule

Thomas and Hunt ask for testing for real, which means that «среда тестирования должна как можно более точно соответствовать среде эксплуатации, поскольку любые расхождения служат местом для размножения программных ошибок» (p. 333). This wiki borrows an illustration from p. 337, where the book argues against manual procedures and compares developer machines with each other, not with production: developers set up the same IDE by hand from long instructions, each machine ended up slightly different, the same code behaved slightly differently, and a bug could appear on one computer and not on the others.

## Sign in code

- Production code that branches on a test flag or on a check for running under test. This page owns that branch, including a field or parameter of a production class whose only purpose is to make it return canned data; Weisfeld's advice to build testing into the class (p. 113) is resolved on [[test-scaffolding]]. A branch on a deployed environment or a customer is [[parameterize-with-external-configuration]].
- An integration-level test whose configuration names a different storage engine or driver from the production configuration.
- A test that depends on a value present on one machine: an absolute path, the default timezone, the default locale. See [[do-not-rely-on-unguaranteed-context]].

## When not to apply

The book says as closely as possible, not identically. The rest of this section is this wiki's reading.

- Unit tests replace collaborators on purpose. Isolation is what they are for, so a substitute in a unit test is not a violation. The rule bites at the levels that check collaboration. See [[test-levels]].
- A real dependency may be unaffordable or unsafe to call from tests: a payment provider, specialised hardware. A substitute kept faithful to the provider's contract is the available choice.
- Real engines would make the suite slow enough that people stop running it. Keep many fast tests with substitutes and a smaller set against the real engine. The rule then holds for the smaller set.
- A difference with no bearing on what the test checks is harmless. A pure calculation does not need a production database behind it.

## Repair

1. Remove test flags from production code. Pass the collaborator that differs in from the edge.
2. At integration level, run against the same engine as production.
3. Set timezone, locale and paths explicitly in the test's setup.

## Before and after

Before:

```
function save(order):
    if config.test_mode:
        memory_store.put(order)
    else:
        database.insert(order)
```

After:

```
function save(order, store):
    store.insert(order)

test "order round trip, integration level":
    store = connect(same_engine_as_production)
    save(order, store)
    assert store.find(order.id) == order
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), see [[pragmatic-programmer]]: the rule on p. 333 and the client story on p. 337.

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], p. 113: the advice to build testing into the class. Counting a canned-data field under this page's sign is this wiki's own.

This wiki's own: the use of the client story as an illustration of this rule, all of `## Sign in code`, `## Repair` and the pseudocode, and all limits in `## When not to apply` apart from the book's wording of as closely as possible.
