---
title: Name an ADT independently of its storage
category: naming
summary: "A class or accessor is named after where its data lives (`RateFile.Read()`, `customerDb`, `cacheMap`) rather than what the data is; the name breaks when the storage changes."
tags: [rule, naming, abstraction, information-hiding]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

## Rule

Give classes and accessors names that do not depend on how the data is stored, and refer to the [[abstract-data-type]] rather than to the medium. McConnell's example is an insurance rate table large enough to live on disk. Calling it a rate file, with `RateFile.Read()`, says more about it than it should. If the program later keeps the table in memory, code that treats it as a file becomes incorrect and confusing. The name should be `rateTable.Read()`, or just `rates.Read()` (p. 127).

## Sign in code

- A type or accessor name contains a storage or transport word (`File`, `Disk`, `Db`, `Cache`, `Http`, `Json`) while its callers only want the domain data. `Table` names a data structure, as in the book's `rateTable`, and is not a storage word.
- The name already lies: the type called `...File` reads from memory or from a service.

## When not to apply

- The class's job is the storage mechanism itself: a file reader, a database gateway, a cache. Then the medium is the abstraction, and naming it is accurate. This limit is this wiki's own.
- Code at the persistence boundary, such as an adapter or repository implementation, may name its medium. The name the rest of the program sees should not.

## Repair

Rename the type and its accessors after the data's meaning. If the storage choice matters to some callers, keep a storage-named class behind the domain-named one.

## Before and after

```
// before
rate = RateFile.read(age, plan)
```

```
// after
rate = rates.lookup(age, plan)   // file, memory or service: hidden
```

## Related

- [[abstract-data-type]]
- [[mixed-abstraction-levels-in-interface]]
- [[information-hiding]]

## Source

[[code-complete]], ch. 6.1, Russian edition, p. 127. The list of storage words in the sign, the second sign ("the name already lies"), the limits and the storage-named class behind the domain-named one in Repair are this wiki's own reasoning.
