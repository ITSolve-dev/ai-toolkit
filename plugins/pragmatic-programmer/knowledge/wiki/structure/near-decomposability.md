---
title: "Near-decomposability: fewer links between parts than within them"
category: structure
summary: "Concept: Simon's near-decomposability as Weisfeld uses it to justify composition, fewer links between parts than within them; parts of a class that read each other's fields or call each other back and forth have their boundary in the wrong place, and the coupling and cohesion rules apply it."
tags: [concept, composition, coupling, cohesion, complexity]
paradigm: any
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Weisfeld bases the case for composition on Herbert Simon's 1962 paper *The Architecture of Complexity*, which states four properties of stable complex systems (pp. 182-183):

1. They are hierarchies of simpler subsystems, each made of simpler subsystems. The book notes that this underlies functional decomposition in procedural design, and that object-oriented design extends it to composition, building complex objects from simpler parts.
2. They are *nearly decomposable*: you can identify the parts and tell interactions between parts from interactions within them. The Russian translation names the property «почти не поддаются декомпозиции», the opposite of Simon's term; the book's own gloss carries the original meaning. «В стабильных системах меньше связей между их частями, чем внутри их частей» (p. 182).
3. They are built from subsystems of only a few kinds, arranged in different combinations.
4. They nearly always evolve from simple working systems, building on proven designs rather than starting from scratch.

The book gives three practical gains from composition. People hold only about seven chunks in short-term memory, so we name a whole ("a car") instead of listing its parts (pp. 181-182). Interchangeable parts mean reuse (p. 182). Parts can be built, and above all tested and maintained, independently (p. 182). The stereo example ties these together: in a modular system a broken component is unplugged, repaired and tested alone while the rest keeps working (pp. 183-184).

## How this wiki applies it inside a module

The book states the property for systems and devices. Applying it to classes and functions inside a module is this wiki's transfer:

- A class composed of parts is well divided when most calls and field accesses happen inside each part, and the parts talk through a few narrow calls.
- Two supposed parts that read each other's fields or call each other back and forth are one part split in the wrong place, or two parts with a misplaced boundary. This wiki's repair is to move the boundary, not to add indirection. A method that uses more of another class than its own is [[tell-dont-ask]]; one class that knows too much about another is [[coupling]]. That two parts always change together is read from the change log, not from the code.
- This wiki reads the "few kinds of parts" property as a cost: a class built from many one-off kinds of collaborators is harder to understand than one built from a few kinds reused.

This concept explains why the coupling and cohesion rules hold. A finding on a specific shape belongs to the rule page that owns it: two domains held in one class is [[class-interface-coherent-abstraction]], links between classes are graded on [[coupling]], and the parts of one routine are [[routine-cohesion]]. Splitting a system into modules or services is architecture and outside this base.

## Limits

The property is a tendency of stable systems, not a count to reach. The book itself warns that design rules are not rigid (p. 187) and that convenience can justify an integrated unit, as the TV/VCR case on [[class-interface-coherent-abstraction]] records. This wiki does not read Simon's fourth property, growing from simple working systems, as a rule against rewriting.

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 9, via [[object-oriented-thought-process]]: seven chunks (pp. 181-182), interchangeability and reuse, independent building, testing and maintenance (p. 182), Simon's four properties (pp. 182-183), the stereo as integrated against modular (pp. 183-184), design rules not rigid (p. 187). The quotation was checked against `raw/`; the remark on the translated term is this wiki's. This wiki's own: the transfer from systems to classes inside a module, the three readings in code and the routing to owner pages.

Related: [[aggregation-vs-association]], [[cohesion]], [[coupling]].
