---
title: Assert what cannot happen
category: errors
summary: "A comment claims a run-time fact (never null, always sorted, can't happen) with no check beside it, an impossible branch is empty, a multi-way branch over a closed set has no default arm, a file operation has no failure path because it cannot fail, logic relies on a + 1 > a, a field set by program logic is silently mishandled outside a sub-range (a negative discount rate) and checked nowhere, or a hand-written algorithm's result goes unchecked."
tags: [rule, assertions, defensive-code, assumptions]
paradigm: any
sources: [pragmatic-programmer, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

The belief behind this rule is the one the book calls a mantra every programmer picks up: «Это никогда не может случиться» (p. 152). The tip is «Пользуйтесь утверждениями, чтобы предотвратить невозможное» (p. 152).

## Rule

Whenever you catch yourself thinking that something could never happen, add code to check it, most simply with an assertion (p. 152). Check a parameter or result that must not be null (p. 152). Check an algorithm by asserting its outcome, as in testing that the output of a custom sort is sorted (p. 153). In Java, the book says, an assertion can and should carry a descriptive string (p. 153), and this wiki asks the same of any assertion. Every multi-way branch carries a default arm for the impossible case (p. 149).

The book returns to this under [[programming-by-coincidence]]: state your assumptions, and test them as well as the code, by writing an assertion for each (p. 250). It spells out why both outcomes pay: «Если ваше утверждение окажется верным, значит, вы улучшили документирование своего кода. А если оно окажется неверным, то можете считать себя везунчиком» (p. 250). Where you do not know whether something can be relied on, its instruction is «допустите самое худшее» (p. 250).

Fowler's *Refactoring* catalogues the same move as **Introduce Assertion** (2nd ed., ch. 10, PDF pp. 338-341). Code often works only if some condition holds, and "Such assumptions are often not stated but can only be deduced by looking through an algorithm. Sometimes, the assumptions are stated with a comment. A better technique is to make the assumption explicit by writing an assertion." (p. 339). He defines an assertion as "a conditional statement that is assumed to be always true. Failure of an assertion indicates a programmer error." (p. 339). Two constraints follow: "Assertion failures should never be checked by other parts of the system", and the program should function "equally correctly if they are all removed" (p. 339), so adding one always preserves behaviour. He values assertions as much for telling the reader what the program assumes as for catching bugs; self-testing code reduces their value for debugging, "as steadily narrowing unit tests often do the job better, but I still like assertions for communication" (p. 339), and he is inclined to leave one in once the bug it chased is fixed (p. 339).

He also limits them: "There is a real danger of overusing assertions. I don't use assertions to check everything that I think is true, but only to check things that need to be true." (p. 341). This wiki resolves that against *The Pragmatic Programmer*, which asks for a check whenever one thinks something could never happen (p. 152), by the code: where the lines below rely on the condition (their arithmetic, an index, a call that assumes it), assert it; a belief that nothing below depends on adds noise and maintenance.

The book observes that assumptions are rarely documented and are often disputed between developers (p. 249). This wiki adds that a checked assumption cannot go on being disputed, and that it fails at the point where it is false, not later and elsewhere.

This wiki asks one question before the assertion is written: by what path could the case happen? The answer decides between handling it and asserting it, by the test on [[assertion-or-error-handling]]. The book's answer to exercise 16 lists such paths, from different layers:

- **Calendar and time.** September 1752 had only 19 days in Britain's calendar change, as the editor's note explains, and leap minutes can have 61 or 62 seconds (pp. 355-356).
- **Environment.** A directory can have been removed by another process, read permission can be missing, and a disk can be unmounted (p. 355).
- **Operators.** Where variable types are left open, overloading of `+`, `=` or `!=` can behave unexpectedly (p. 355).
- **Aliasing.** Two names can denote one variable, so the second assignment overwrites the first (p. 355).
- **Concurrency.** A badly written parallel program can update a variable before the addition runs (p. 355).
- **Numeric range.** Depending on the language, overflow can leave `a + 1` negative (p. 356).

## Sign in code

- A comment or name records the belief: `never null here`, `cannot be empty`, `always sorted`, `caller holds the lock`, `unreachable`. This page owns that sign on any line, and [[prove-dont-assume]] sends it here.
- A branch labelled as impossible or `should not happen` is empty: no statement runs in it, so nothing was checked. This page owns that shape. Where a statement runs and the work carries on, the shape belongs to [[crash-early]]. A branch that the types or the control flow of the routine prove unreachable is [[remove-dead-code]]; a branch that is impossible only because of an assumption about run-time values is [[assert-the-impossible]].
- A multi-way branch over a fixed set of values has no default arm. [[default-branch-catches-the-unexpected]] owns that shape: it owns whether a multi-way branch over a closed set has a final `else` or `default` reserved for the unexpected, including a missing one.
- A hand-written algorithm has a cheap test of its result, and none is present.
- A directory or file operation has no failure path, on the ground that the path was just checked, that it is the current directory, or that closing cannot fail. This page owns that shape, and [[crash-early]] sends it here.
- A comparison's logic relies on `a + 1 > a` over a fixed-width integer.
- A value set by program logic (a field, a setter argument) that a later calculation silently mishandles outside a sub-range (a negative discount rate turning into a surcharge), with no check at the setter or at the use, so the assumption is deducible only by reading the algorithm. This wording is this wiki's, after Fowler's discount example (pp. 339-340).
- The same asserted condition written out in several places. Fowler: "Duplication is a particular problem, as it's common to tweak these kinds of conditions." (p. 341).
- Two reads of a shared variable in one expression assume that nothing changes it between them.

## When not to apply

- The condition can occur in a correct program: use real handling, see [[assertion-or-error-handling]].
- This wiki adds that where a compiler already checks that a branch is exhaustive, a default arm can switch that check off. Keep the compiler's check.
- This wiki also excludes conditions a type already makes impossible, since the check would be dead code.
- This wiki does not apply the aliasing and concurrency paths to local variables that nothing else can reach.
- The check is too costly to keep: see [[leave-assertions-on]], which limits the exception to that one check.
- Nothing below the point relies on the condition. Fowler checks only "things that need to be true" (p. 341); see the resolution above.

## Repair

Name the path by which the case could happen. If it can happen in operation, handle it: give the file operation a failure path, see [[assertion-or-error-handling]]. If it could only follow from a bug in this program, turn the comment into a check, with a message naming the value and place, and keep as a comment only the wording the check cannot carry. Keep the condition free of effects ([[assertion-side-effects]]), and let a failure stop the work ([[crash-early]]). Where you cannot tell whether the assumption holds, write the code for the worst case.

Fowler's placement rule: prefer the point where the bad value enters. If the assertion fails at the point of use, "my first puzzle is how it got into the field in the first place" (p. 340), so an assertion on the setter catches the error at its source, such as an errant minus sign in input data (p. 340). If an expression form leaves no place for a statement (a ternary), restructure it into an `if` first (p. 340). Remove duplication among asserted conditions, usually by extracting a function (p. 341).

## Before and after

Only a bug in this program can release a slot twice, so the belief becomes an assertion.

```
# before
function release_slot(pool, slot):
    # slot came from this pool, so it is always busy here
    pool.busy[slot] = false
    pool.free.push(slot)
```

```
# after
function release_slot(pool, slot):
    assert pool.busy[slot], "slot " + slot + " released twice in release_slot"
    pool.busy[slot] = false
    pool.free.push(slot)
```

A directory can vanish in operation, so this belief becomes handling.

```
# before
names = list_directory(work_dir)   # work_dir always exists
for name in names:
    process(name)
```

```
# after
result = list_directory(work_dir)
if result is failure:
    report("cannot read " + work_dir, result.reason)
    return
for name in result.names:
    process(name)
```

Fowler's case, with the assertion moved to where the value enters:

```
# before: the assumption lives only in the arithmetic
method applyDiscount(amount)
  if rate == null then return amount
  return amount - rate * amount

method set_rate(value)
  this.rate = value
```

```
# after
method set_rate(value)
  assert value == null or value >= 0, "discount rate must not be negative: " + value
  this.rate = value

method applyDiscount(amount)
  if rate == null then return amount
  return amount - rate * amount
```

Fowler's own listing starts from a conditional expression, which leaves no place for a statement, and rewrites it as an `if` before adding the assertion (p. 340).

If `rate` came from parsed user input rather than from program logic, this "after" would be wrong: that check is ordinary validation with its own error path ([[assertion-or-error-handling]]).

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 149, 152-153 for the rule, pp. 249-250 for assumptions and their payoff, and the answer to exercise 16, pp. 355-356, for the failure paths. The note that the 1752 calendar change was a British one is the Russian edition's editor's. The signs, the limits marked as this wiki's, the question of the path, the extension of the descriptive string beyond Java, the repair and the examples are this wiki's own.

Fowler, *Refactoring*, 2nd ed., ch. 10, "Introduce Assertion", PDF pp. 338-341, via [[fowler-refactoring]]: unstated assumptions, the definition, removability, no checking of failures, communication over bug-finding, tests reducing the debugging value, the setter placement, the ternary, overuse, duplication and the discount example. This wiki's own for that part: the resolution of overuse against *The Pragmatic Programmer*, the partial-domain sign as worded and the pseudocode; the raw extraction drops the minus sign in Fowler's listing, so the pseudocode restores it.
