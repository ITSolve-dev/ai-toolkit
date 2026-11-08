---
title: Abstract data type
category: objects
summary: "Data plus the operations on it, named in problem terms; the idea a class is supposed to implement, and the test for a class that is only a container of loosely related data and methods."
tags: [concept, abstraction, encapsulation, class-design, information-hiding]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

An **abstract data type (ADT)** is a set of data together with the operations performed on it. The operations describe the data to the rest of the program and let the rest of the program change it. McConnell treats the ADT as the concept beneath the class: a class is an ADT that also supports inheritance and polymorphism (p. 129). The "data" can be anything with operations: a window, a file, a table of insurance rates (p. 122).

## Why it matters

McConnell's argument is that without a clear grasp of ADTs, programmers write classes that are classes in name only, «удобными контейнерами» holding sets of poorly matched data and methods (p. 122). The ADT idea lets code work with real-world entities instead of low-level implementation entities: add a cell to a spreadsheet rather than insert a node into a linked list (p. 122).

He lists these benefits (pp. 123-124):

- **Implementation details hidden:** a change of data type is made in one place.
- **Changes contained:** new operations, such as strikethrough fonts, touch one piece of code.
- **A more informative interface:** `size = 16` does not say whether the unit is pixels or points. An ADT interface can be defined in points, in pixels, or with both clearly separated.
- **Easier optimisation:** a few well-defined routines to speed up, instead of code scattered across the program.
- **Easier verification:** a call such as `SetBoldOn()` can go wrong in one way, a wrong method name. A raw `attribute = attribute or 0x02` can go wrong in four: wrong structure, wrong field, wrong operator, wrong constant.
- **Readability:** McConnell cites Woodfield, Dunsmore and Shen (1981). Students answering questions about a program split into eight ADT routines scored 30% higher than those answering about one split into eight functional-style routines.
- **Data use confined:** the structure is neither passed into every routine nor made global. Only the ADT's own routines touch it.

## Principles from the chapter

- Represent common low-level types (stack, list, queue) as ADTs named for what they hold. Ask what the stack represents: if it holds employees, treat it as a set of employees. «Используйте как можно более высокий уровень абстракции» (p. 126). See [[replace-direct-data-manipulation-with-adt]].
- ADTs layer. The OS gives a first level of file abstraction and a high-level language gives a second. A data-structure ADT, such as stack operations, can carry a problem-domain ADT on top (pp. 126-127).
- Even trivial things qualify. A flashlight with only on and off is still worth an ADT, because it limits the effects of changing `TurnLightOn()` and reduces the data passed around (p. 127).
- Name the ADT independently of its storage medium: see [[storage-independent-names]].
- Without classes the same discipline still applies, with explicit instance handling: see [[adt-instances-without-classes]].

This wiki narrows the book's advice to wrap even simple elements (p. 127) with a limit McConnell does not state: an ADT pays for itself only when the operations it hides are performed from more than one place, or carry a rule or a unit the raw data does not show. A record read in one place with no invariant is not made clearer by wrapping it.

## Related

- [[abstraction]]
- [[class-interface-coherent-abstraction]]: a class should implement exactly one ADT.
- [[mixed-abstraction-levels-in-interface]]
- [[semantic-encapsulation-violation]]

## Source

[[code-complete]], ch. 6.1, Russian edition, pp. 121-129. The limit in the last paragraph of the principles section is this wiki's own reasoning.
