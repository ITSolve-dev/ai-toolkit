---
title: Extract a routine to name a step, however small
category: functions
summary: "An inline loop or pair of order-dependent statements whose result has a nameable meaning (find the leaf, pop the stack) sits in the middle of a longer routine, or one intent comment heads far more than ten lines; move it into a routine named for that meaning."
tags: [rule, extract-routine, abstraction, boolean-test, complexity, comments]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell lists reasons to create a routine (*Code Complete*, pp. 160-163). The first is the one he ranks highest: «Самая важная причина создания метода — снижение сложности программы.» (p. 160). The routine hides information, so that once it is written its details can be forgotten. Code size, maintenance and defect count matter too, but rank below that.

## Rule

When a fragment computes something that can be named, put it in a routine with that name, even when the fragment is two or three lines. The book's reasons that bear on a single fragment (pp. 160-161):

- **Deep nesting.** Deeply nested inner loops or conditionals are one sign that a routine should be split. The nested part becomes its own routine.
- **An understandable intermediate abstraction.** Eight lines that walk a list to its last node and read its name become `leafName = GetLeafName(node)`. The name documents the purpose, and the routine is simple enough that the name is all the documentation it needs.
- **Hiding a sequence.** Two lines that read the top of a stack and then decrement `stackTop` go into `PopStack()`, so that the assumption about their order is not spread through the system.
- **Simplifying a complex boolean test.** Its details are rarely needed to follow the program's path. A routine hides them, and its descriptive name characterises the test. Isolating the test also pushes the author to make its inside readable.
- **A single place to optimise or port.** Non-portable code and performance work are isolated in one routine rather than spread out.

The book addresses directly the objection that an operation is too simple to deserve a routine. It calls the reluctance one of the main mental barriers to effective routines: «небольшие методы могут быть чрезвычайно полезны» (p. 162). The second reason it gives is that «простые операции имеют свойство усложняться с течением времени» (p. 162). Its conversion from device units to points later needed a guard against division by zero. With the routine, that guard was 3 lines in one place. Without it, it would have been 30 lines across ten call sites (pp. 162-163).

Chapter 9 gives a calibration for code written from pseudocode: «Каждый комментарий обычно разворачивается в 2–10 строк кода.» (p. 222). When the code under one pseudocode line grows well beyond that, McConnell gives two repairs: turn the block into a new routine, named from the pseudocode, and apply the [[pseudocode-programming-process]] to it; or apply the process recursively, splitting the one pseudocode line into several and coding each (p. 222). The comment is then already the name, so if the process was applied properly the name is easy to find (p. 222). In his worked example he marks the command-line branch as a good candidate for its own routine (p. 221).

Fowler's catalogue entry for Extract Function gives the same test in other words (*Refactoring*, 2nd ed., ch. 6, PDF pp. 122-123). He sets aside two common guidelines, that a function should fit on a screen and that code used once should stay inline, and keeps one criterion, the separation between intention and implementation: "If you have to spend effort looking at a fragment of code and figuring out what it’s doing, then you should extract it into a function and name the function after the “what.”" (PDF p. 122). He reports that, applied this way, any function of more than about half a dozen lines starts to smell to him, and one-line functions are normal (PDF p. 123). His example is a Smalltalk `highlight` whose whole body calls `reverse`: the name is longer than the body and the function stays, "because there was a big distance between the intention of the code and its implementation" (PDF p. 123). A comment heading the block is "often a good hint for the name of the function" (PDF p. 123). He dismisses the cost of the call: it is very rare now for it to matter, and optimising compilers often work better with short functions (PDF p. 123). This wiki reads that as: only a hot path a profiler has measured makes the call cost a reason to keep a fragment inline, and that exception comes from [[premature-code-tuning]], not from this page.

The chapter's key points rank the purpose: making the program intellectually manageable comes first, and shortening the code matters much less than readability, reliability and ease of change (p. 181).

## Sign in code

- A loop or block inside a longer routine that exists only to compute one value later used under a different name (a loop that walks to the last node and then sets `leafName`).
- Two or three statements that must run together in a fixed order, written inline in a longer routine (read the top element, then decrement the index).
- One comment stating one intent, followed by a long run of code before the next comment at the same level: more than about ten lines, in this wiki's reading of the book's 2-10 calibration, often with its own nested branches or locals used nowhere else in the routine.

This wiki assigns the neighbouring case as follows. A fragment repeated verbatim at several call sites is [[dry]], which owns it; a fragment that is not repeated is [[extract-routine-to-name-a-step]]. A comment heading a block whose result has a nameable meaning is [[extract-routine-to-name-a-step]]; a comment that restates steps, numbers or names the body already holds is [[comment-why-not-how]]. This page decides by whether the fragment can be named. A compound condition in an `if`, `else if` or `while` is [[name-complex-conditions]], which owns it whether the repair is a variable or a function. Fowler's leg extraction belongs to [[name-complex-conditions]] when it accompanies naming the condition: the legs of an `if`/`else` whose condition is being named are extracted in the same pass; a leg that is long on its own, under a simple condition, is [[extract-routine-to-name-a-step]]. A long arm of a `case` or `switch` is [[keep-case-arms-short]]. Loops nested more than three deep, or a loop body too long to see at once, are [[loop-length-and-nesting]], and `if`/`switch` nesting is [[tame-deep-nesting]]; this page supplies the extraction their repairs use. A function whose name says *what* where its body says *how* is an explanation and stays, however short; a function whose name only restates its body is [[lazy-element]]. Where extracting a fragment would need most of the routine's locals as parameters or results, the temps are removed first ([[replace-temp-with-query]]); where they still tangle, [[function-or-command-object]] owns the choice of a command object; where the routine is to stay whole, the intent comment is split into finer steps ([[extract-routine-to-name-a-step]]).

The procedure for carrying out the extraction (which locals become parameters, which the return value) is [[extract-function]].

## When not to apply

- **Not to shrink other routines.** The book rejects routine size as a reason in itself. Some tasks are better done in one large routine (p. 161; see [[routine-length]]).
- **No name exists.** Fowler states this limit: "If I can’t come up with a more meaningful name, that’s a sign that I shouldn’t extract the code" (ch. 6, PDF p. 123). This wiki adds the reasoning: if the only available name restates the code (`AddOneAndCompare`), the fragment is not a step of the problem, and extracting it moves the reader's attention without reducing it. Fowler adds that it is fine to extract, find the function is not helping, and inline it back (PDF pp. 123-124; [[inline-function]]).
- **A flat, uniform sequence.** The 2-10 range is the book's description of what usually happens, not a limit. This wiki lets a block that is long only because it is one uniform run (a table of assignments, a list of field copies) with one intent stay inline.
- **Extraction would need many of the routine's locals.** A block that cannot move without passing many locals in and out trades a long block for a long parameter list ([[limit-parameter-count]]). Remove the temps first ([[replace-temp-with-query]]); if they still tangle, a command object is weighed on [[function-or-command-object]]. Where the routine is to stay whole, this wiki reads the book's second repair, splitting the comment into finer steps, as the one to use.
- **A test that is the program's path.** The book's reason applies to booleans whose details do not affect the reader's understanding of the flow. This wiki judges that when the condition *is* the business rule being read (a single `if total > limit`), a named routine adds a hop.

## Repair

1. Name what the fragment produces or decides.
2. Move the fragment into a routine with that name, passing in what it reads and returning what it produces.
3. Replace the fragment with the call.
4. For a boolean, name the routine as a question (`IsEligible`, `HasExpired`).
5. Where a comment headed the fragment, take the routine's name from it, then delete the comment if it only restates the name ([[comment-why-not-how]]). Where extraction does not fit, replace the one comment with several finer intent comments and redistribute the code under them (p. 222).

## Before and after

```
routine ShipOrder(order)
    if order.ready
        node = order.route
        while node.next != none
            node = node.next
        destination = node.stop
        send order to destination
```

```
routine ShipOrder(order)
    if order.ready
        send order to FinalStop(order.route)

routine FinalStop(route)
    node = route
    while node.next != none
        node = node.next
    return node.stop
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.1, pp. 160-163, and the key points on p. 181 ([[code-complete]]). The reasons, the leaf-name, `PopStack` and device-units examples, and the limit about routine size are the book's.
- Same book, chapter 9, pp. 221-222: the 2-10 calibration and the two repairs for a block that outgrows its comment.
- The signs (including the ten-line threshold), the no-name, flat-sequence, many-locals and program's-path limits, the splits with [[dry]], [[name-complex-conditions]], [[loop-length-and-nesting]] and [[tame-deep-nesting]], and the pseudocode are this wiki's own.

- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 6, "Extract Function", motivation, PDF pp. 122-123: the intention-versus-implementation test, the two guidelines set aside, the half-dozen-lines remark, the `highlight` example, the comment as a hint for the name, the call cost, the no-better-name limit and inlining back an extraction that does not help. This wiki's own for that part: the reading of the call cost as an exception only for a measured hot path.

Related: [[routine-cohesion]], [[temporal-coupling]], [[routine-names]].
