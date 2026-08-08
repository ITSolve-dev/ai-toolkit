---
title: Over-specification
category: failure-modes
summary: Stating a constraint the obligation does not require — every statement is true, and the description is still defective because it excludes implementations that would have served.
tags: [failure-mode, information-hiding, symptom]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

**Over-specification** is a description that constrains more than its obligation requires. Nothing
in it is false, nothing is obviously mechanism, and it still narrows the set of acceptable
implementations for no return. It is the failure mode that survives a careful reading, because
careful reading checks whether statements are *true* and this defect is about whether they are
*needed*.

Parnas caught it in his own work and did not soften the verdict.

## The worked case

His circular-shift module hides how the shifts are stored or computed — the obvious leak, correctly
avoided. But its definition also fixes the **order** in which shifts appear: shifts of line *i*
before those of line *j*, and within a line, the original first, then successive one-word rotations
(L113-L127).

Reviewing it, he finds the order was never required. Three statements would have sufficed: that
the named shifts all exist, that none appears twice, and that a function recovers the original line
from a shift.

> By prescribing the order for the shifts we have given more information than necessary and so
> unnecessarily restricted the class of systems that we can build without changing the definitions.
> For example, we have not allowed for a system in which the circular shifts were produced in
> alphabetical order, *ALPH* is empty, and *ITH* simply returns its argument as a value. Our
> failure to do this in constructing the systems with the second decomposition must clearly be
> classified as a design error.
>
> — [[parnas-criteria-for-decomposing-systems]], L215-L232

Note what makes the diagnosis stick: he does not argue that the ordering is inelegant. He
**names a specific system the statement wrongly excludes** — one where alphabetisation collapses to
nothing because the shifts arrive sorted. The excluded system is the evidence.

## The symptom, and how to check for it

The symptom is a statement that no obligation depends on. It cannot be found by asking "is this too
detailed"; it is found by asking, of each constraint:

1. **What would break if this were not stated?** If the honest answer is "nothing that was
   promised", the constraint is over-specification.
2. **Can I name a valid alternative this excludes?** If yes, the statement has a cost, and the cost
   is now concrete rather than theoretical. If no such alternative exists, the constraint may be
   restating something already forced.

The second question is the one that makes the finding reportable — an over-specification claim
without a named excluded alternative is an opinion.

## Why it is worth hunting

Over-specification does not announce itself. Unlike a leaked storage format, it survives review by
people who agree with the criterion in [[information-hiding]], because the constraint is usually
true of the implementation the author had in mind. It is caught either by the deliberate
enumeration in [[the-changeability-test]], or by the two questions above — never by reading for
tone.

Related: [[abstract-interface-vs-representation]] governs which *kinds* of statement belong;
over-specification is what remains once that line is respected and the description still says too
much.
