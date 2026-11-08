---
title: Class size
category: complexity
summary: "A class body longer than the book's limit for its language, about 250 lines in Java or 100 in Ruby, counting comments and blank lines."
tags: [rule, class-size, simplicity]
paradigm: oop
sources: [elegant-objects, fowler-refactoring]
created: 2026-11-02
updated: 2026-11-07
---

Bugayenko treats maintainability as the main virtue and simplicity as what produces it, with the number of lines as simplicity's usual measure: the shorter a class, the easier it is to see what it does, where it is weak and how to rework it (p. 89). He presents this as the strongest argument for [[immutable-objects]].

## Rule

Keep classes small. The book gives a number for Java: «максимальный размер класса не должен превышать 250 строк кода» (p. 89), counting comments and blank lines. Anything larger calls for immediate refactoring. For Ruby the book suggests 100 lines (p. 89). It applies the limit to test code as well as production code (p. 90). It adds that the exact number matters less than being small, and that 5,000-line classes, which it has seen even in OpenJDK, are inexcusable (p. 90).

The mechanism the book offers is that immutability keeps classes small. All state arrives through the constructor, so each new capability adds a constructor argument. A constructor with ten arguments looks so bad that the author splits the class: «Вы никогда не напишете неизменяемый класс размером 2000 строк кода» (p. 90).

In section 3.1 the author demotes the line limit: «В разделе 2.6 я уже предложил ограничивать размер класса 250 строками, но это не самый важный показатель» (p. 115). He makes the number of public methods the main measure, and says a class with one public method and 20 private ones is not very large (p. 115). See [[fewer-than-five-public-methods]].

## Sign in code

- A class body over the book's threshold for its language: 250 lines for Java, 100 for Ruby, counting everything.

A class with more fields than the threshold of [[keep-objects-small]] for its setting (four, or about seven) or a constructor with more than five parameters belongs to [[keep-objects-small]]; a class over the line limit with fewer belongs to [[class-size]]. A class over the line limit with five or more public methods is [[fewer-than-five-public-methods]]. A class over the line limit with fewer is [[class-size]], and this wiki reports it only where its private methods fall into groups over disjoint fields. Larman's low-cohesion scenario 2, one functional area carried alone by a class with hundreds of related methods, is reported on [[class-size]] or [[fewer-than-five-public-methods]] under those pages' own conditions, and not on its own; [[cohesion]] supplies the split into collaborators sharing the work.

## When not to apply

- The thresholds are the author's, stated for Java and Ruby only. This wiki records them as he states them and does not carry them over to other languages. For another language, the project's own limit decides.
- This wiki's own limit: generated code, and data tables kept as code, have no design to refactor, and their length is not this sign.
- Line count is a proxy. A class just under the limit that mixes several responsibilities is still a problem, but that finding belongs to a cohesion page, not here. This reading is this wiki's own.

## Repair

1. Find the groups of methods that use the same few fields, or that serve one caller's purpose.
2. Make each group a class of its own, under [[name-classes-for-what-they-are]], and let the original compose them.
3. Make the class immutable first where it is not (see [[immutable-objects]]): with all state in the constructor, the groups become visible there.

Where the class is long because its methods repeat each other, Fowler and Beck remove that redundancy first: five hundred-line methods with much code in common may become five ten-line methods plus ten two-line methods extracted from them (*Refactoring*, 2nd ed., ch. 3, Large Class, PDF p. 97). They call a class with too much code "a prime breeding ground for duplicated code, chaos, and death" (PDF p. 97).

## Before and after

```
class Report                      // 900 lines
  constructor(source, layout)
  method rows() ...               // 200 lines of querying and paging
  method pdf() ...                // 350 lines of page layout
  method csv() ...                // 150 lines of escaping and quoting
  method cached() ...             // 200 lines of cache bookkeeping
```

```
class Report                      // 60 lines
  constructor(rows: Rows)

class PdfReport                   // 220 lines
  constructor(report: Report, layout: Layout)

class CsvReport                   // 120 lines
  constructor(report: Report)

class CachedRows                  // 140 lines
  constructor(origin: Rows)
```

The line counts are read as Java, the language of the book's limit.

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 2.6, pp. 89-90, and section 3.1, p. 115, for the demotion of the line limit; see [[elegant-objects]]. The quotation on p. 115 was checked against the page image. This wiki's own: the limits on other languages and generated code, the redirect to cohesion, the split with [[keep-objects-small]] and [[fewer-than-five-public-methods]], the private-method grouping test, the routing of Larman's scenario 2 from [[cohesion]], the repair steps and the pseudocode.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Large Class", PDF p. 97: a class with too much code and the remedy of removing redundancy inside it. This wiki's own for that part: placing that remedy here rather than on [[keep-objects-small]].
