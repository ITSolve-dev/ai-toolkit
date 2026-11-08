---
title: Name builders with nouns, manipulators with verbs
category: naming
summary: "A method that returns a value is named with a verb (load, read, add, get, cook...), a void method is named with a noun, or a boolean query is named isX/exists; rename to a noun, a verb or an adjective."
tags: [rule, method-names, getters, boolean-names]
paradigm: oop
sources: [elegant-objects, code-complete]
created: 2026-11-02
updated: 2026-11-07
---

*Elegant Objects* (section 2.4) ties a method's name to what it does with the result. A **builder** returns a new object and is named with a noun. A **manipulator** changes the entity the object represents, returns `void` and is named with a verb. The rule that no method may be both is [[command-query-separation]].

## Rule

- **Builders are nouns.** Examples: `pow(base, power)`, `speed()`, `employee(id)`. A noun may carry an adjective, as in `parsedCell(x, y)`, a cell whose content was transformed (pp. 54-55).
- **Manipulators are verbs.** Examples: `save(content)`, `put(key, value)`, `remove(emp)`. A verb may carry an adverb, as in `quicklyPrint(id)` (p. 55).
- **Booleans are the exception: adjectives.** Examples: `empty()`, `readable()`, `negative()`. Read the name with a silent "is" in front to check it, but do not write the prefix. Where the adjective does not read, rephrase: `equals` becomes `equalTo`, `exists` becomes `present` (p. 63). The exception exists because conditions are written without `== true`, so `if (name.empty())` reads as "if the name is empty" while a noun such as `emptiness()` would not (p. 64).
- **No `get` prefix.** `get` is a verb, but a getter returns something and is therefore a builder (p. 56). The book's fuller case against getters comes in a later section.
- **`with` names under the Builder pattern** (`withTitle`) are accepted as shorthand for the noun phrase `bookWithTitle`: they are builders, so their names count as nouns (pp. 60-61). The book then rejects the pattern itself: it breeds large objects that are harder to maintain, the many constructor arguments it serves are a problem of their own, and a complex object should be split into simpler ones instead (p. 61).

The reasoning: a verb on a method that returns something tells the object how to do its work. The book's image is a cafe. You ask for a brownie or a coffee, not for the cafe to bake or brew it. `Bakery.cookBrownie()` and `brewCupOfCoffee(flavor)` are procedures in methods' clothing, the same as C functions `cook_brownie()` (pp. 57-58). A badly named method invites its users to treat the object as «мешок с данными и набором процедур» (p. 58). With `sum(x, y)` instead of `add(x, y)`, the caller asks for a result that obeys a contract and leaves to the object how it is produced (p. 59). This is the method-level form of [[object-as-representative]].

The book's own summary on p. 64 says manipulators get *adjectives*. This contradicts the section it summarises (pp. 55, 59-60), and this wiki reads it as a misprint for verbs.

## Sign in code

- A method that returns a value and is named with an imperative verb, such as `load(url)`, `read(file)`, `add(x, y)`, `getX()`, `cookBrownie()` or `calculateTotal()`.
- A `void` method named with a noun.
- A boolean method named `isX`, `hasX` or with a verb (`exists`).

A method whose name's part of speech does not match whether it returns belongs to [[builder-and-manipulator-names]]. A method that returns a value and is named with a verb belongs to [[builder-and-manipulator-names]], whose repair names what comes back by its role; a method that returns nothing and is named for its mechanism belongs to [[name-by-role]]. A returning method named with a noun for its mechanism belongs to [[name-by-role]] unless it is a general-purpose utility. A method that mutates and returns a value describing that mutation (a count, a flag, a previous value), or a method named for its action that also returns a result it computed (an item found), belongs to [[command-query-separation]]; a method whose name promises a read or a result and which also writes as a side job belongs to [[rename-when-meaning-drifts]]. On a class whose public methods are only accessors over its fields, [[no-getters-and-setters]] owns the finding and its repair 1 comes first. [[builder-and-manipulator-names]] takes a get-prefixed name only on a class that has behaviour of its own. A class name is [[name-classes-for-what-they-are]].

## When not to apply

The source gives no limits. This wiki resolves the conflict with common practice by setting:

- **Where a framework reflects on names** (bean introspection, serializers, templating, or ORMs keyed on `get`/`is`), the framework's convention wins for the methods it reads. The book's rule applies to the objects you design that no such tool reads.
- **Language idioms and the project's naming convention** are decided at work time, per this wiki's Scope. If a codebase uses `isEmpty` consistently, a lone `empty()` is the worse choice; see [[follow-local-naming-culture]].
- **Methods inherited from the platform** (`equals`, `toString`) cannot be renamed.
- **The other source disagrees.** *Code Complete* names a function for what it returns but accepts an `Is` form as such a name: `printer.IsReady()` (p. 168); it agrees with this page that a procedure is named for its action (p. 168). This wiki resolves it per setting: in a project that follows *Elegant Objects* conventions, this page's renames apply; elsewhere a returning method named `isX` or `getX` that names its result is not a finding, and only a verb that names an action rather than the result (`load`) is; a vague verb (`process`, `handle`) is [[routine-names]] whatever the return. Other defects of routine names are [[routine-names]].
- A verb name on a returning method that also writes: if the value describes the write, or the name is the action and the value a result it computed, [[command-query-separation]]; if the name promises a read and the write is a side job, [[rename-when-meaning-drifts]]. Renaming to a noun alone hides either.

## Repair

1. Decide whether the method returns or changes.
2. A returning method gets the noun that names the result it returns (`stream`, `content`, `sum`, `brownie`, `total`).
3. A boolean gets an adjective that reads after "is".
4. A changing method gets a verb and a `void` return.
5. If no single noun or verb fits, the method does two things: see [[command-query-separation]].

## Before and after

```
load(url): InputStream
read(file): String
add(x, y): int
isEmpty(): boolean
exists(): boolean
```

```
stream(url): InputStream
content(file): String
sum(x, y): int
empty(): boolean
present(): boolean
```

## Source

[[elegant-objects]], section 2.4: builders and manipulators, pp. 54-55. Against `get`, p. 56. The cafe argument and the renames `load`/`read`/`add` to `stream`/`content`/`sum`, pp. 57-59. `with` names, pp. 60-61. Boolean adjectives and `equalTo`/`present`, p. 63. Why booleans are the exception, and the summary with its misprint, p. 64. This wiki's own: the `calculateTotal`, `hasX` and void-noun signs, the misprint reading, the division of method names with [[name-by-role]], [[command-query-separation]], [[rename-when-meaning-drifts]] and [[no-getters-and-setters]], and all of *When not to apply*. The rejection of the Builder pattern is the book's (p. 61).

[[code-complete]], Russian edition, section 7.3, p. 168: function and procedure naming, the `IsReady()` example. This wiki's own: the per-setting resolution between the two books and the split with [[routine-names]] on vague verbs.
