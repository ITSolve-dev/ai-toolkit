---
title: Review a routine against the routine checklist
category: functions
summary: "Procedure for auditing one routine: reason for existing, cohesion, name, coupling, length, then each parameter's use, order, mode, count and documented assumptions, then every return path; worked on a routine with eleven parameters and a dozen defects."
tags: [method, checklist, routine-design, parameters, review]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* closes chapter 7 with a checklist for judging the quality of a routine (pp. 180-181). It opens the chapter with a deliberately bad routine, `HandleStuff()`, and the author's own list of its defects (pp. 158-159). This page turns the two into a procedure and points each step at the page that owns the finding.

## Procedure

Run the steps in order. The earlier steps can make the later ones moot: a routine that must be rewritten for coincidental cohesion does not need its parameters reordered.

1. **Reason to exist.** Is there a sufficient reason for the routine? Have the parts that deserve their own routines been moved out? See [[extract-routine-to-name-a-step]].
2. **Cohesion.** Does it do one thing and do it well? See [[routine-cohesion]].
3. **Name.** Is a procedure named verb + object, and is a function named for its return value? Does the name describe everything the routine does? Is there a convention for common operations? See [[routine-names]] and [[one-name-per-concept]].
4. **Coupling.** Are the routine's connections to others few, intimate, visible and flexible? The book's opening example reads and changes globals. See [[global-data]] and [[coupling]].
5. **Length.** Is the length set by its role and logic rather than by a coding standard? See [[routine-length]].
6. **Parameters**, one by one:
   - Does the list as a whole form a consistent interface abstraction? See [[pass-what-the-routine-uses]].
   - Is the order sensible, and does it match similar routines? See [[parameter-order]].
   - Are the interface's assumptions documented? See [[state-the-contract]].
   - Are there seven parameters or fewer? See [[limit-parameter-count]].
   - Is every input used, and every output used? See [[remove-unused-parameters]].
   - Are inputs kept out of service as working variables? See [[do-not-reuse-parameters-as-working-variables]].
   - At the call sites, can adjacent arguments of one type be swapped unnoticed? See [[match-arguments-to-parameters]].
7. **Return.** If it is a function, does it return a correct value in every case? See [[every-path-sets-the-return-value]] and [[function-or-procedure]].

The book's opening list also covers defences against bad input and magic numbers (p. 159). Those belong to the error-handling and naming pages, such as [[caller-owns-the-precondition]], [[barricade]] and [[named-constants-over-literals]].

## Worked example

The book's `HandleStuff()` takes 11 parameters and asks the reader to find at least 10 defects (p. 158). Its own list, mapped to the steps above (pp. 158-159):

| Defect the book lists | Step |
|---|---|
| The name says nothing about what the routine does | 3 |
| No documentation | 6 (assumptions) |
| Poor, inconsistent layout | out of this wiki's scope (formatting) |
| The input `inputRec` is changed | 6 (working variables) |
| Reads and writes global variables | 4 |
| No single purpose: it initialises, writes to a database and computes | 2 |
| No defence against bad data: a zero quarter divides by zero | outside this method; see [[caller-owns-the-precondition]] |
| Magic numbers 100, 4.0, 12, 2 and 3 | outside this method; see [[named-constants-over-literals]] |
| `screenX` and `screenY` unused | 6 (use) |
| `prevColor` passed by reference but never assigned | 6 (use, mode) |
| 11 parameters, laid out unreadably | 6 (count) |
| Parameters poorly ordered and undocumented | 6 (order, assumptions) |

The book says that routines with coincidental cohesion usually have to be redesigned and reimplemented (p. 166). For `HandleStuff()`, step 2 therefore decides the outcome before step 6 is reached. This wiki's reading is that the parameter findings matter only for whatever routines replace it.

## When the procedure ends with no change

A routine that passes each step needs no rewrite, and the review says so. The checklist has no step that is always failed. The book itself allows long routines (100-200 lines) and flag dispatchers that only call other routines; see the limits on [[routine-length]] and [[routine-cohesion]].

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition: the opening example and its defect list, pp. 158-159; the redesign of coincidental cohesion, p. 166; the checklist, pp. 180-181 ([[code-complete]]).
- The ordering of the checklist into a procedure, the call-site step, the mapping to wiki pages, and the note on ending with no change are this wiki's own.

Related: [[pseudocode-programming-process]], whose polish step runs a shorter form of the same check on a routine just written.
