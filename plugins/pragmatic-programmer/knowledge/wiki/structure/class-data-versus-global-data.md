---
title: Class data versus global data
category: structure
summary: "Fields shared by dozens of methods of one large class behave like global data; fields of a small class whose few methods all know each other do not."
tags: [decision-rule, global-state, class-size, encapsulation, information-hiding]
paradigm: oop
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

This test decides when a class's fields carry the hazards of [[global-data]]. McConnell raises it as a barrier to [[information-hiding]]: a careful programmer may treat class data as global data and avoid it for that reason (p. 92).

## Rule

The book names the two defects of global data: routines touching it do not know that other routines touch it too, or they know but not what the others do with it (p. 92). Class data has neither defect, because direct access is limited to a few methods of the same class, which know both that the others use the data and which they are (p. 92). The condition is the book's: this assumes small, well-designed classes. «Если программа использует огромные классы, включающие десятки методов, различие между данными класса и глобальными данными стирается» (p. 92), and class data takes on many of the defects of globals.

## Sign in code

- A class with dozens of methods, several of which write the same field, where no single reader can name every writer without a search.

A split of the fields into groups used by disjoint methods is owned by [[class-interface-coherent-abstraction]] at any method count. Dozens of methods of one class writing the same field are [[class-data-versus-global-data]].

## When not to apply

- A small class whose methods all fit in view: its fields are what the book calls far safer than globals (p. 92). Avoiding them by passing state through parameters adds nothing.
- Immutable fields set once in construction: neither of the book's two defects can arise from them. This wiki's addition.

What size counts as "dozens" is the book's word; this page takes no threshold of its own, and defers to [[class-size]] for when to split.

## Repair

Split the class so that each field has a small group of methods that own it; each new class then regains the property the book attributes to class data.

## Before and after

```
class ReportEngine           -- 40 methods
    currentRow
    function loadData() ... currentRow = 0
    function formatHeader() ... currentRow = 3
    function writeBody() ... uses currentRow
    function exportTotals() ... currentRow = currentRow + 1
    ...
```

```
class RowCursor
    private row = 0
    function next() ... row = row + 1
    function current() ... return row

class ReportEngine
    function writeBody(cursor: RowCursor) ...
```

## Source

[[code-complete]], section 5.3, Russian edition, p. 92. The two defects, the safety of class data and its condition are the book's; the signs, the immutability limit, the split with [[class-interface-coherent-abstraction]] and the repair are this wiki's own.
