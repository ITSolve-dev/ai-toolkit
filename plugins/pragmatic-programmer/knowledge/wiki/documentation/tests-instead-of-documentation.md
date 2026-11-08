---
title: Tests instead of documentation
category: documentation
summary: "A doc comment on a class or method declaration carries the meaning its names lack (`Helper.saveAndCheck`, `convert(int, boolean)`): rename until the comment is redundant, and let a unit test show the use."
tags: [rule, documentation, unit-tests, naming]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-03
---

Bugayenko grants that a reader needs supporting information about a class or method. He argues that the need for prose documentation is itself a symptom of poor design, and that the information should come from clean code and from unit tests instead (section 2.7, pp. 93-96).

## Rule

Do not document code. Make it cleaner: «не документируйте код — делайте его чище» (p. 95). The book's test is whether the code reads by itself. `jeff.giveRaise(new Cash("$5,000"))` followed by `if (jeff.performance() < 3.5) jeff.fire()` needs no comment (p. 94). A class `Helper` with `saveAndCheck(float)`, `extract(String)` and `convert(int, boolean)` cannot be understood without one: «Плохо спроектированные классы вынуждают писать для них документацию» (p. 94). The book contrasts it with `WebPage` having `content()` and `update(String)` (p. 95).

The positive half of the rule is the unit test. The book holds that a unit test is conceptually part of the class, as much as its methods, name and interfaces: «Юнит-тест — часть класса, а не самостоятельная сущность» (p. 95). It regrets that the separate test class (`CashTest` for `Cash`) lets a class exist with no test at all. The better the test, the less documentation the class needs: «Юнит-тест и есть документация» (p. 95). The book adds that a test, unlike prose, does not depend on the reader's command of English.

The section opens with a reader-centred premise. Write as if the reader knows the domain, language, patterns and algorithms less well than you do, and write simple code rather than show off (p. 94).

## Sign in code

- A doc comment on a class or method declaration whose name says nothing about what it does (`Helper`, `saveAndCheck`, `convert(int, boolean)`), the comment standing in for the missing meaning.
- A boolean flag parameter whose effect can only be learned from the comment on the method.

An exported routine with no doc comment, or one whose doc comment states a contract the names and types cannot, belongs to [[documentation-in-the-source]]. A comment, above a declaration or inside a body, that restates steps, numbers or names the body already holds belongs to [[comment-why-not-how]]; a doc comment that says what a vaguely named class or method is for, without restating its body, belongs to [[tests-instead-of-documentation]]. A vague name with no comment beside it is judged by the naming pages: [[name-classes-for-what-they-are]] for a class, [[builder-and-manipulator-names]] or [[name-by-role]] for a method. A class arriving with no unit test is [[test-early-often-automatically]]. A method like `saveAndCheck` that saves and also returns a status is [[command-query-separation]].

## When not to apply

- **The disagreement with *The Pragmatic Programmer*.** That book asks for a doc comment on every module and exported function ([[documentation-in-the-source]]); this book says not to document code (p. 95). This wiki resolves it per setting. Where the comment explains what a vaguely named thing does, this page applies: rename, and the comment goes. Where the names already say what the thing does and the comment states what they cannot (a precondition, a failure mode) on an export whose callers will not read its tests, such as a published library, [[documentation-in-the-source]] applies and the comment stays. The book's argument concerns classes read by the people who maintain them.
- Comments that record why a non-obvious choice was made, and that no test can express (an external constraint, a rejected alternative), are not covered by this sign. This page fires on comments that explain what code does because the names fail to. See [[comment-why-not-how]]. This limit is this wiki's own.
- The book's own examples include things a reader may legitimately not know, such as how an algorithm works, what MD5 is, or a regular expression (p. 94). This wiki notes that the book does not say whether such knowledge belongs in a test, a better name or a comment: section 2.7 (pp. 93-96) leaves it open.

## Repair

1. Rename the class and its methods after what they are or return, by the naming pages the book cites (sections 1.1 and 2.4: [[name-classes-for-what-they-are]], [[builder-and-manipulator-names]]).
2. Split a class like `Helper` into ones that each have a clear purpose.
3. Replace a boolean flag with two methods or two classes.
4. Write a unit test that shows each public method in use.
5. Delete the comment that the names and the test now make redundant.

## Before and after

```
// Saves the value and checks it against the limit; returns the status code.
// If extra is true, converts using the legacy scale.
class Helper
  method saveAndCheck(x)
  method convert(value, extra)
```

```
class Reading
  constructor(value)
  method save()              // manipulator: stores the reading
  method withinLimit(limit)

class LegacyScale
  constructor(reading)
  method value()

test "reading above the limit is reported as outside it"
  assert not new Reading(12).withinLimit(10)
```

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 2.7, pp. 93-96. The quotations on p. 95 were checked against the page image. The book cites Beck's *Test-Driven Development by Example* for unit testing (p. 95). See [[elegant-objects]]. This wiki's own: the signs as worded, the boolean-flag sign, the ownership split with [[documentation-in-the-source]], [[comment-why-not-how]], the naming pages, [[test-early-often-automatically]] and [[command-query-separation]], the per-setting resolution of the disagreement with *The Pragmatic Programmer*, the limit on comments that explain why, the shape of the repair and the pseudocode.
