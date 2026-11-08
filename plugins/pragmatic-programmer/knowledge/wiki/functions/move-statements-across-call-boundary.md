---
title: Move statements across the call boundary
category: functions
summary: "The same statements immediately before or after every call of a function (move them into it), or a parameter that only skips or alters the function's first or last statement for some callers, or a caller that overwrites what the callee's last statement produced right after the call (move that statement out to the callers)."
tags: [rule, refactoring, duplication, function-boundaries]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler pairs two inverse refactorings, Move Statements into Function and Move Statements to Callers. Both put the boundary between caller and callee where the behaviour actually divides. Function boundaries drift as software changes: "what might once have been a cohesive, atomic unit of behavior becomes a mix of two or more different things" (*Refactoring*, 2nd ed., ch. 8, PDF p. 246).

## Rule

- **Into the function:** when the same code runs every time a function is called, move it into the function, so that future changes happen in one place (p. 242). Do this only when the statements are best understood as part of the called function (p. 242).
- **Out to the callers:** when behaviour shared by several callers must now vary in some of them, move the varying part out of the function to its callers (p. 246).

The two directions are reversible: "Should the code vary in the future, I can easily move it (or some of it) out again" (p. 242).

## Sign in code

- Into: every call site of `f` is immediately preceded or followed by the same (or semantically equivalent) statements on the same arguments. In Fowler's example, both callers of `emitPhotoData(photo)` emit the photo title on the line before (p. 243).
- Out: a parameter, usually a boolean, that only skips or alters the function's first or last statement for some callers; or a caller that overwrites or undoes the output of the callee's last statement right after the call. A new requirement alone, such as Fowler's need for one caller to render the location differently (p. 247), is not a sign; it is the occasion to run the move (p. 246).

This wiki assigns the neighbouring cases as follows. The same statements adjacent to every call of one function are [[move-statements-across-call-boundary]]; the same fact restated elsewhere, not tied to a call, is [[dry]]. A flag parameter that selects between unrelated jobs the routine performs inline is [[routine-cohesion]]; a flag that only switches off a trailing or leading line for one caller is [[move-statements-across-call-boundary]].

## When not to apply

- **The statements do not belong to the callee's meaning.** If they "don't make sense as part of the called function, but still should be called with it" (p. 242), extract a new function around the statements *and* the call instead, and leave the callee alone.
- **The boundary needs complete reworking.** Moving statements to the callers suits small shifts. For a full rework Fowler inlines the function and slides and extracts new ones (p. 246).
- **The likeness is a coincidence.** This wiki adds: if the repeated statements state different requirements that happen to match today, see [[coincidental-duplication]]. Fowler states that limit only under Replace Inline Code with Function Call (p. 251).

## Repair

With one caller (or one or two simple ones), cut and paste, then test (pp. 242, 246). With more callers, Fowler uses a safer sequence with a temporary name that is "easy to grep" (p. 248), such as `zznew` or `zztmp`:

- **Into:** slide the statements next to the call if needed ([[slide-statements]]). Extract the statements plus the call at one site into a new function. Convert the other call sites one at a time, testing after each. Inline the original function into the new one, then rename the new one to the original name or a better one (p. 242).
- **Out:** extract everything that stays into a temporary function. If the method is overridden, do the extraction in every subclass so that the remainders are identical, then remove the subclass methods. Inline the original function at each call site, one at a time, testing after each, then rename the extracted function back (p. 246).

## Before and after

```
renderPerson(person):
  out("<p>" + person.name + "</p>")
  out("<p>title: " + person.photo.title + "</p>")
  emitPhotoData(person.photo)

photoDiv(photo):
  out("<div>")
  out("<p>title: " + photo.title + "</p>")
  emitPhotoData(photo)
  out("</div>")

emitPhotoData(photo):
  out("<p>location: " + photo.location + "</p>")
  out("<p>date: " + photo.date + "</p>")
```

```
renderPerson(person):
  out("<p>" + person.name + "</p>")
  emitPhotoData(person.photo)

photoDiv(photo):
  out("<div>")
  emitPhotoData(photo)
  out("</div>")

emitPhotoData(photo):
  out("<p>title: " + photo.title + "</p>")
  out("<p>location: " + photo.location + "</p>")
  out("<p>date: " + photo.date + "</p>")
```

The reverse direction starts from the "after": once one caller needs a different location line, the location statement moves back out to both callers, and the varying caller changes its copy.

## Source

Fowler, *Refactoring*, 2nd ed., ch. 8, Move Statements into Function (PDF pp. 242-245) and Move Statements to Callers (pp. 245-250) ([[fowler-refactoring]]). This wiki's own parts are the pseudocode pair, the "out" sign as worded (the flag parameter and the caller that overwrites the callee's output), the assignment against neighbouring pages, and the link to coincidental duplication as a limit.
