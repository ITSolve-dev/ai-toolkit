---
title: Aggregation versus association
category: objects
summary: "Concept: telling a part a class owns (aggregation: made inside or handed over once, not handed out, ends with the whole) from a collaborator it only uses (association: passed in, shared, outlives the link); the finding is code whose creation, exposure or lifetime handling contradicts the relation chosen."
tags: [concept, composition, aggregation, association, ownership, lifetime]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Weisfeld treats inheritance (is-a) and composition (has-a) as the two basic ways of building classes from classes (pp. 180-181); choosing between them is [[containment-or-inheritance]]. With inheritance the result is conceptually one class: an `Employee` does not send messages to a `Person`, because it *is* one. Composition is interaction between distinct objects (p. 180). The book places association inside composition, admitting other texts do the reverse (p. 184), and splits composition in two.

## The two kinds

- **Aggregation**: a complex object made of other objects, where you normally see only the whole. A television is seen as one television, not as an «агрегацию микрочипов, экрана, тюнера» (p. 185); you buy the car, not its spark plugs.
- **Association**: one object needs another to perform a service it cannot perform itself, and both the whole and the parts are visible. The system unit asks the separate mouse, keyboard and monitor for their services (p. 186): «Ассоциация используется, когда одному объекту нужно, чтобы другой объект оказал ему услугу» (p. 186).

The book's sharpest example is about **lifetime**. An `Employee` holds an `Address` and a `Spouse`. Address may be read as part of the employee; Spouse is an association, because if the employee is fired the `Spouse` stays in the system and only the link breaks (p. 187). In the `Dog` example, `Head` is a part (aggregation, one), while `Owner` is not part of the dog and supplies a service, `walkDog` (association, one or more) (pp. 191-193).

## The criterion as this wiki applies it

The book draws the line conceptually and gives no code for it. This wiki reads it as three questions about the code in front of the reader:

1. **Who creates the other object?** A part is created by the whole, or handed to it once and kept by nobody else. An associate is created elsewhere and passed in.
2. **Who else holds it?** A part is not handed out for others to keep and mutate. An associate is shared by design.
3. **Does it outlive the holder?** A part ends with its whole; an associate survives the end of the link, like the book's Spouse.

Mixed answers are the finding: a part the whole creates and also returns for callers to mutate, or a class that resets or releases an object it only borrowed. What to do with each mismatch belongs to the page that owns the shape: a part returned for callers to mutate is [[class-invariant]] where a rule binds it and [[iterator]] for a collection, copying a part when the whole is copied is [[prefer-deep-copy]], who frees nested parts is [[ownership-of-nested-structures]], how many associates there are and whether one may be absent is [[association-cardinality-in-field-types]].

## Limits

The book stresses that the line is often blurred and that one object can play both roles: the system unit is associated with the mouse and is at the same time an aggregation of chips and boards (p. 186). There is no single right answer, because design is not an exact science (p. 187), and attaching `Head` to `Dog` rather than to `Mammal` was a modelling choice made because `Dog` was the centre of the example (p. 193). This wiki therefore never reports the label chosen; it reports only a mismatch between that relation and how the code creates, exposes and ends the object.

## The same split in chapter 10

Chapter 10 restates the two kinds as UML notation (pp. 201-204). Composition is what one reaches for when the is-a relationship does not fit and inheritance is the wrong choice (p. 201). In aggregation one class is a component of another, as a tire is part of a car. Aggregation levels can nest without a theoretical limit, and each level can be a different aggregation: `Stereo` in `Car`, `Radio` in `Stereo`, `Tuner` in `Radio` (p. 202). In association the classes serve each other, neither is part of the other, and in most cases one can say which is the server and which the client (p. 202). A plain association line records only that the relationship exists, not which way the service runs (p. 203).

The chapter's computer example confirms the limit above. `Monitor`, `Scanner`, `Keyboard` and `Mouse` are drawn as associated with `Computer`, yet the author adds that the monitor «технически является частью Computer» and could be drawn as aggregation, while `Computer` is itself an aggregation of motherboard, memory and other parts (p. 204). The book gives no test for choosing. The `Cabbie` constructor in the same chapter builds its own `Cab` from a serial number (p. 196). This wiki reads that as question 1 above answered for a part: the whole creates it and does not hand it out.

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 9, via [[object-oriented-thought-process]]: is-a against has-a and inheritance as one conceptual class (pp. 180-181), association within composition (p. 184), aggregation (p. 185), association and its boxed definition, mixed roles (p. 186), Address and Spouse (p. 187), Dog, Head and Owner (pp. 191-193). The quotations were checked against `raw/`. This wiki's own: the three code questions, the reading that a mismatch and not the label is the finding, and the routing of mismatches to their owner pages. Ch. 10, pp. 196, 201-204: composition when is-a fails, the two kinds as notation, nesting levels, the plain association line, the computer example and the monitor remark; the quotation was checked against `raw/`. This wiki's own for that part: reading the `Cabbie` constructor as aggregation.
