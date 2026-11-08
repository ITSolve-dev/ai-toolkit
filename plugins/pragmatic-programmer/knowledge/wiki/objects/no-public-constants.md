---
title: "Share functionality, not data: no public constants"
category: objects
summary: "A public static constant, an enum value or a Constants holder class is read by unrelated classes that each wrap it in their own code, or is passed into a general class to select its behaviour (`.method(HttpMethods.POST)`); replace it with a small class that owns that behaviour."
tags: [rule, constants, enums, coupling, cohesion, duplication]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-07
---

*Elegant Objects* (section 2.5) rejects public static final fields as a way for objects to share data: «Объекты не должны ничего использовать совместно» (p. 65). Duplication of a constant between classes is real, but the book's cure is a class that shares the *behaviour* the constant serves. It concludes its argument with its strongest phrasing: «публичные константы в ООП — чистейшее зло» (p. 72).

## Rule

Do not remove duplication by moving a value into a public constant. Instead, «Объекты не должны совместно использовать данные.» (p. 68). Create a small class that encapsulates what the users do with the value, and let them use that class.

The book's first case: `Records.write()` and `Rows.print()` both end lines with a private constant `EOL = "\r\n"`. A private constant used inside one class is fine (p. 65). The two classes are unrelated, so the duplicated constant is duplicated code. A `Constants.EOL` holder is no better than a C `#define`, and is arguably worse, because a public class is visible to every class while a macro is visible only where its header is included (p. 66). Moving `EOL` into `Constants` solves duplication and creates two problems:

- **Coupling.** `Records.write()`, `Rows.print()` and `Constants.EOL` are now hard-wired together. Changing the value changes both users' behaviour in ways nobody can foresee, because the constant does not know how it is used. One user may be ending printed lines, another may be ending lines of an HTTP message, where the protocol forbids a change (p. 67).
- **Loss of cohesion.** The constant knows nothing about its purpose. Each user has to write code around it to give it meaning, which is not what records or rows are for (p. 68).

The repair class, `EOLString`, wraps a string and appends the line end. Both users now use `new EOLString(...)`. The coupling to `EOLString` is acceptable because it «является сцеплением посредством контракта» (p. 70): its behaviour can change behind the contract. The book's example makes it throw on a platform where that line end is wrong, which a public literal could not do (p. 70).

The book's second case is a constant that selects behaviour. Instead of `new HttpRequest().method(HttpMethods.POST)`, write `new PostRequest(new HttpRequest())`. `PostRequest` knows how to configure the request, and the caller no longer needs to know what POST means at the protocol level (p. 72). The book applies the same rule to Java enums: «Перечисления ничем не отличаются от публичных констант» (p. 72).

The book accepts the cost in full. Yes, a class for every public constant. Yes, hundreds of micro-classes instead of hundreds of literals. Its argument is that more distinct words make a text easier to read: «Чем больше мелких классов, тем чище код, при условии, что они не дублируют друг друга.» (p. 71). One overloaded `File` reads worse than `TextFile`, `JPGFile` or `TempFile` (p. 71). Asked in the comments how depending on a constant differs from depending on a public class, the author answers that the class removes duplicated functionality, not just duplicated data (p. 73). Asked about the new object created on each use, he accepts that cost too: «В общем случае я отдаю предпочтение сопровождаемости (чистому коду), а не скорости» (p. 73).

## Sign in code

- A class whose body is only public static final fields (`Constants`, `Config`, `Keys`).
- A public static constant referenced from classes in unrelated parts of the code, each of which wraps the value in its own code (formatting, appending, comparing).
- A public constant or an enum value passed as a mode or selector argument into a general class, or compared in a branch, to decide what to do; the general class switches on it internally.
- The same literal declared as a private constant in two unrelated classes. This is the duplication that tempts the holder class, and its repair is the same.

This page owns a shared constant and what its users do with it. A literal that should vary between deployments is [[parameterize-with-external-configuration]]. The same fact written twice without a constant is [[dry]]. The same literal declared as a constant in two unrelated classes, where the temptation is a shared public constant, is [[no-public-constants]]. A chain of branches over a key, all of one shape, is [[drive-repeated-dispatch-from-a-table]]. Where the key is a public constant or enum passed in from outside to select behaviour, [[no-public-constants]] owns the branch. A switch on a type tag of an object whose arms call per-kind behaviour of one operation is [[polymorphism-or-type-switch]]. A public constant or enum read by classes that each wrap it, or passed in to select behaviour, is [[no-public-constants]]. A mutable or run-time-loaded static value is [[global-data]]. An argument the callee branches on is [[no-public-constants]] when it is a public enum or constant shared across classes, whatever the call site writes; otherwise, written as a literal at the call site it is [[semantic-coupling]], and flowing in as data its type is [[enum-instead-of-codes-and-flags]]. An argument the callee stores, filters on or passes on is [[enum-instead-of-codes-and-flags]].

## When not to apply

The book admits no exception: public constants «не должны использоваться никогда» (p. 72). It concedes that for a primitive constant with transparent meaning, such as EOL, the coupling is small (p. 68), and still replaces it. It notes that standard libraries are full of public constants and says not to add them to your own code (p. 72). A private constant used inside one class is outside the rule (p. 65).

The items below are this wiki's resolution, not the book's:

- **A constant the project must pass to a library's API** is outside the rule; the library fixed it.
- **The book and common practice disagree on enums and named constants**, which are standard in most codebases. This wiki resolves it per setting. A constant or enum that merely names a value and is never used to select behaviour, such as a closed set of labels serialised to a wire format, carries no logic to encapsulate. The rule applies when the constant selects behaviour that callers would otherwise have to know about, or when its users each wrap it in their own code. An argument the callee branches on is [[no-public-constants]] when it is a public enum or constant shared across classes, whatever the call site writes; otherwise, written as a literal at the call site it is [[semantic-coupling]], and flowing in as data its type is [[enum-instead-of-codes-and-flags]]. An argument the callee stores, filters on or passes on is [[enum-instead-of-codes-and-flags]].
- **A value whose meaning is the value**, fixed by an outside specification (a protocol code, a header name, a unit factor such as pi). No behaviour to encapsulate surrounds it, and wrapping it adds a class that only returns the literal.
- **A project convention** for constants, enums or configuration keys overrides the rule. Where the codebase has none, the book's rule decides.
- **Cost when followed:** many micro-classes, and an allocation per use. The book's own condition is that the classes must not duplicate each other. On a measured hot path the allocation may decide otherwise.

## Repair

1. Look at what every user of the constant does with it. That shared operation, or the behaviour the constant selects, is the class to create.
2. Give it a constructor taking what the users supply, and a method that does the operation. For a selector, the class is usually a decorator of the general class that applies that behaviour.
3. Replace each use of the constant with that class: callers choose the class instead of passing the constant.
4. Delete the constant once no caller uses it.

## Before and after

```
class Constants
  public static EOL = "\r\n"

class Records
  write(out)
    for rec in this.all
      out.write(rec.text())
      out.write(Constants.EOL)

class Rows
  print(pnt)
    for row in this.fetch()
      pnt.print("{ " + row + " }" + Constants.EOL)
```

```
class EOLString
  origin: String
  EOLString(origin)
  text(): String
    return origin + "\r\n"

class Records
  write(out)
    for rec in this.all
      out.write(new EOLString(rec.text()))

class Rows
  print(pnt)
    for row in this.fetch()
      pnt.print(new EOLString("{ " + row + " }"))
```

A constant that selects behaviour, before:

```
class HttpMethods
  public static final POST = "POST"

body = new HttpRequest().method(HttpMethods.POST).fetch()
```

After:

```
class PostRequest
  final field origin
  constructor(origin)
  method fetch()
    return this.origin.method("POST").fetch()

body = new PostRequest(new HttpRequest()).fetch()
```

## Source

[[elegant-objects]], section 2.5: the rule and private constants, p. 65. `Records`, `Rows` and `Constants` compared to `#define`, p. 66. Coupling and the HTTP example, p. 67. Loss of cohesion, the primitive-constant concession and «Объекты не должны совместно использовать данные.», p. 68. `EOLString`, p. 69. Coupling through a contract and the platform check, p. 70. Micro-classes and the word analogy, p. 71. `PostRequest`, enums, «чистейшее зло», «не должны использоваться никогда» and the standard libraries, p. 72; the quotations of pp. 68 and 72 were checked against the page images. The reader comments on functionality against data and on speed, p. 73. This wiki's own: the holder-class, selector and duplicated-private-literal signs as worded, the splits with [[parameterize-with-external-configuration]], [[dry]], [[drive-repeated-dispatch-from-a-table]], [[polymorphism-or-type-switch]], [[global-data]] and [[enum-instead-of-codes-and-flags]], the library, label-versus-selector, outside-spec, convention and hot-path limits, the repair procedure and the pseudocode. Related: [[public-methods-implement-interfaces]].
