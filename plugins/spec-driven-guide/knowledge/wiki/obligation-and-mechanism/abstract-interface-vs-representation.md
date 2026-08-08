---
title: Abstract interface versus representation
category: obligation-and-mechanism
summary: Parnas puts operation names, parameter counts and types on the side a description may state, and storage formats and table organisation on the side it must hide.
tags: [concept, criterion, information-hiding, boundary]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

Where exactly does the line fall between what a description may state and what it must withhold?
Parnas answers by contrasting the two boundaries in his worked example, and the answer is sharper
than "avoid detail".

> In the first modularization the interfaces between the modules are the fairly complex formats
> and table organizations described above. […] In the second modularization the interfaces are
> more abstract; they consist primarily in the function names and the numbers and types of the
> parameters.
>
> — [[parnas-criteria-for-decomposing-systems]], L188-L199

So the line runs between:

| May be stated (the abstract interface) | Must be hidden (the representation) |
|---|---|
| The operations that exist | How data is laid out |
| What each operation is called | How it is stored, packed, indexed |
| How many parameters it takes, and of what types | Which table organisation carries it |
| What must be called before what has a defined value | When the work is actually performed |
| What is guaranteed about the result | How the guarantee is produced |

## Why the line falls there

Both sides are equally concrete; concreteness is not the discriminator. The discriminator is
**what a reader is forced to depend on**. A caller that knows an operation's name and parameters
depends on a commitment the module intends to keep. A caller that knows the storage format depends
on a decision the module intends to revisit — and Parnas's changeability trace shows exactly that
decision changing and propagating everywhere it was revealed
([[the-changeability-test]]).

The paper makes the same point from the cost side: complex-format interfaces "represent design
decisions which cannot be taken lightly", must be designed jointly across teams, and hold up
independent work; abstract interfaces "are relatively simple decisions and the independent
development of modules should begin much earlier" (L188-L199).

## Applied to a document

This is the answer to the recurring question of whether naming an operation in a document is a
leak. By Parnas's line it is not: the operation, its parameters and its types are the commitment
itself, and a document that omits them has withheld its obligation rather than its mechanism.

What *is* a leak is the layer beneath — the storage layout, the internal decomposition, the
tooling that realises the operation, the order in which the work is actually done. See
[[information-hiding]] for the criterion and [[over-specification]] for the failure mode that
arises when a description crosses this line while believing it has not.

One caution against reading the table too literally. Parnas is describing an interface between
program modules, where the operation *is* the commitment. A document whose subject is larger — a
system rather than a component — has its commitments at a correspondingly larger grain, and
naming component-level operations there states something the subject does not commit to.
The line is stable; what sits on each side of it moves with the subject.

**This page and [[what-a-design-doc-omits]] will return opposite verdicts on the same passage** —
one saying an interface is the obligation, the other saying not to import interface definitions.
Do not apply either alone to such a passage. [[resolving-a-scale-conflict]] separates the two
questions they are answering and resolves both.
