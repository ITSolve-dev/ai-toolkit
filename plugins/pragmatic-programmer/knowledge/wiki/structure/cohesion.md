---
title: Cohesion
category: structure
summary: "How closely all routines of a class, or all parts of a routine, serve one central purpose; low cohesion shows as members a reader cannot relate to the class's name, as one class serving several unrelated functional areas, or as one area carried alone by a class with hundreds of methods. Larman's High Cohesion grades the degrees and names when lower cohesion is accepted."
tags: [concept, cohesion, focus, abstraction, grasp]
paradigm: any
sources: [code-complete, larman-applying-uml-and-patterns]
created: 2026-11-06
updated: 2026-11-07
---

*Code Complete* defines cohesion as how well all the routines of a class, or all the code of a routine, support a central purpose, that is, how focused the class is (p. 102). The concept comes from structured design and is usually discussed with [[coupling]] (p. 102). The aim is as high cohesion as possible; the reason given is memory: the more closely the code serves its purpose, the easier it is to remember everything it does (p. 102).

## Routine level and class level

The book says striving for cohesion at the routine level has long been a useful heuristic, while at the class level it is largely subsumed by the broader heuristic of defining consistent [[abstraction|abstractions]]; at the routine level the two heuristics are on a more equal footing (p. 102). The book ranks cohesion among the less useful heuristics of the chapter, behind the eight core ones (pp. 102, 105).

This wiki reads that ranking as advice for review: at the class level, a finding is better stated as "this member does not belong to the abstraction the class presents" than as "low cohesion", because the former names what to move. The rule that carries it is [[class-interface-coherent-abstraction]].

## Larman's High Cohesion

Larman defines (functional) cohesion as "a measure of how strongly related and focused the responsibilities of an element are" (17.14, p. 461), and earlier, informally, as how functionally related the operations of an element are and how much work it is doing (17.8, p. 433). He presents High Cohesion as a GRASP principle that, like [[low-coupling]], is *evaluative*: "Assign a responsibility so that cohesion remains high. Use this to evaluate alternatives" (p. 461). A class with low cohesion does many unrelated things or does too much work; it is then hard to comprehend, hard to reuse, hard to maintain, and "delicate; constantly affected by change" (p. 461).

### A scale of degrees

Larman grades cohesion with four scenarios (17.14, p. 463):

1. **Very low.** One class is solely responsible for very different functional areas. His example is an `RDB-RPC-Interface` that does both database access and remote calls; split it into a family of database classes and a family of RPC classes.
2. **Low.** One class carries a complex task in a single area alone. His example is an `RDBInterface` whose methods are all related but number in the hundreds; split it into a family of lightweight classes that share the work.
3. **High.** Moderate responsibilities in one area, collaborating with other classes, such as an `RDBInterface` that works with a dozen related classes.
4. **Moderate.** Lightweight, sole responsibilities in a few areas related to the class concept but not to each other, such as a `Company` that knows its employees and its finances, with few public methods and little code.

Larman's rule of thumb: a highly cohesive class has a relatively small number of methods, with highly related functionality, and does not do too much work; it collaborates when the task is large (pp. 463-464).

This wiki reads the scale as the criterion between two kinds of split: unrelated areas (scenario 1) split by area, while one area done alone (scenario 2) splits into collaborators sharing the work. This wiki also reads scenario 4 as tolerated, not a defect to repair; the book orders no split for it. In review, the finding for scenario 1 is stated on [[class-interface-coherent-abstraction]], which owns the sign of methods serving unrelated purposes or touching disjoint halves of the fields. A routine that does several jobs is [[routine-cohesion]].

### Trend, not single assignment

Larman warns against judging one assignment in isolation. One Payment creation in Register is acceptable, but fifty system operations all done in Register make it bloated: "The point is not that this single Payment creation task in itself makes the Register incohesive" (17.14, p. 462). What matters is the trend. The class that receives many requests and does their work is [[controller]]. A coordinator whose method computes the details itself (rolling, moving, scoring) instead of sending messages to the objects holding that state is Larman's low-cohesion `MonopolyGame` (17.8, Figure 17.11, p. 434); this wiki routes that shape to [[controller]] when the coordinator receives system operations, and to [[god-class]] otherwise.

### Cohesion and coupling move together

"Bad cohesion usually begets bad coupling, and vice versa" (17.14, p. 464). Larman's example is a GUI widget class that paints itself, saves to a database and invokes remote services: incohesive, and coupled to many unrelated elements. He also says a 2,000-line low-cohesion class probably collaborates with many others, so bad cohesion and bad coupling "often go hand-in-hand" (17.8, p. 433). This wiki reads the converse as a limit on splitting: breaking a class apart so that the pieces must constantly exchange each other's data trades cohesion for coupling; when the method groups share most of their fields, keep them together. See [[low-coupling]].

Size alone is not the sign. Larman counts both the amount of code and how related it is (17.8, p. 433). This wiki reads that as: a large class whose methods all serve one responsibility over shared fields is scenario 2 at worst, not scenario 1. The line count is [[class-size]]. Larman's low-cohesion scenario 2, one functional area carried alone by a class with hundreds of related methods, is reported on [[class-size]] or [[fewer-than-five-public-methods]] under those pages' own conditions, and not on its own; [[cohesion]] supplies the split into collaborators sharing the work.

### When lower cohesion is accepted

Larman names two cases (17.14, pp. 464-465):

- **One maintainer's skill.** All embedded SQL is gathered into one `RDBOperations` class so that the one or two SQL experts on the project can work on it in one place, although good design would spread it across ten mapper classes. He adds that such grouping may also make maintenance worse.
- **Remote objects.** Because remote calls are expensive, fewer and larger, less cohesive server objects with coarse-grained operations are sometimes preferred: one `setData` in place of `setName`, `setSalary` and `setHireDate`. This wiki notes that the remote boundary belongs to the architecture, which is given; the case applies only to the interface of a class that sits on such a boundary.

A single facade [[controller]] over only a few system operations is cohesive in its role (17.8, p. 432).

## Related

[[class-size]], [[orthogonality]], [[information-hiding]], [[coupling]], [[low-coupling]], [[responsibility-driven-design]]. The routine-level rule, with the kinds of weak cohesion and their signs, is [[routine-cohesion]].

## Source

[[code-complete]], section 5.3, Russian edition, p. 102. The review reading, and the sign of low cohesion in the summary (members a reader cannot relate to the class's name), are this wiki's own.

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 17.8, PDF pp. 432-434 (the informal definition, the `Big` class, the `MonopolyGame` contrast, the facade allowance, bad cohesion and coupling together); 17.14, PDF pp. 461-465 (the definition, the problems, the Register example, the four degrees, the rule of thumb, the two contraindications). This wiki's own: reading the scale as the criterion between the two kinds of split, treating scenario 4 as tolerated, the routing of the scenario-1, scenario-2 and coordinator shapes to owner pages, the limit on splitting that raises coupling, the size note, and the architecture note on remote objects.
