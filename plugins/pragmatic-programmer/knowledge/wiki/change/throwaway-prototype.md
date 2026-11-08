---
title: Keep prototype code throwaway
category: change
summary: "A prototype's own code has grown past the minimum its design question needed (error handling, configuration, layers, its own tests), or states no question at all; prototype code reached from the production path is tracer-code-vs-prototype."
tags: [rule, prototyping, spike, design-question]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

In McConnell's sense, experimental prototyping means writing the absolutely minimal amount of code, meant to be thrown away, that answers one specific design question: «написание абсолютно минимального объема подлежащего выбрасыванию кода, нужного для ответа на отдельный вопрос проектирования» (p. 111). It deals with the "wickedness" of design, where a design problem cannot be fully defined until it is at least partly solved. Examples are whether a database layout meets a throughput requirement, or whether a subsystem design survives the choice of GUI library (pp. 110-111).

## Rule

The book gives three conditions for a prototype to work:

- **The question is specific.** "Will this database organization work?" gives a prototype no direction. "Will it support 1000 transactions per second under conditions X, Y and Z?" does (p. 111).
- **The code is the absolute minimum.** To answer the throughput question you need only an approximation of the problem space: the number of tables, the number of rows. Tables and columns named `Table1`, `Column1`, filled with dummy data, are enough (p. 111).
- **The code is treated as throwaway from the start.** McConnell observes that people cannot write minimal code if they think it will end up in the system. They start implementing the system instead (p. 111). He suggests two safeguards. One is to build the prototype in a different technology from the product. The other, when the technology is the same, is to start the names of prototype classes and packages with `prototype`, so a programmer thinks twice before extending them (p. 111, citing Stephens, 2003).

Used with discipline, prototyping fights the messiness of design. Without discipline, «оно делает проектирование еще более грязным» (p. 111).

## Sign in code

- A prototype directory has grown error handling, configuration, abstraction layers or tests of its own. That code is far more than its single question needed, so the prototype is being built as the system.
- No question stated: a prototype file or directory whose header or README does not say what it was written to find out.
- A directory or class in the product's tree, imported by nothing in the product, whose content has a prototype's shape (`Table1`/`Column1` names, dummy rows, one timing loop) but no `prototype`, `spike` or `poc` name.

This wiki assigns the neighbouring case as follows. Prototype code read on its own belongs to this page; prototype code reached from the production path (an import of a spike folder, `Table1`-style placeholders or canned rows in shipped code) belongs to [[tracer-code-vs-prototype]], which owns that sign.

## When not to apply

- **Evolutionary prototypes.** McConnell notes that "prototyping" means different things to different people (p. 111). This rule covers only code written to answer a design question. Code deliberately started as the first increment of the product is ordinary production code and is judged as such; see [[tracer-code]].
- **The answer has been taken, and the code rewritten.** A production module that re-implements what a prototype measured is the intended outcome, not a violation, even if it looks similar.
- **Benchmarks and experiments kept on purpose** as a regression check, in a clearly separate tooling or bench location not imported by the product.

## Repair

1. State the question the prototype answers, with its numbers and conditions, at the top of the prototype.
2. Cut the prototype to what that question needs. Anything beyond it is the start of an implementation and belongs in the product, written properly.
3. If prototype and product share a technology, put the prototype under a `prototype` name or location so that extending it is visibly a choice.
4. Once the answer is recorded, delete or archive the prototype.

## Before and after

```
// before: the throughput spike is turning into the storage layer
prototype_db/
  writer       // retries, connection pool, config loader
  schema       // migrations for Table1, Table2
  writer_test  // 40 tests
  // no file says what question this answers
```

```
// after: the spike states its question and holds only what answers it
prototype_db/
  README       // question: can layout L take 1000 tx/s under X, Y, Z? answer: yes, 1350 tx/s
  load_test    // Table1/Column1, dummy rows, one timing loop
```

## Source

[[code-complete]], ch. 5.4, "Experimental prototyping", Russian edition, pp. 110-111. The book states the three conditions, the `Table1`/`Column1` example and the `prototype` prefix. The signs in code, the owner assignment against [[tracer-code-vs-prototype]], the limits (evolutionary prototypes, kept benchmarks), the repair steps and the pseudocode are this wiki's own. Related: [[prototype-when-code-resists]], [[architecture-prototype-questions]].
