---
title: Keep each case arm short
category: functions
summary: "A case or switch arm holding many lines of its own logic (a loop, a nested if, more than about five lines) so the labels of the branch cannot be seen together: move the arm's body into a routine named for the action and call it."
tags: [rule, conditionals, switch, extract-function, readability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A `case` statement is readable when its structure can be seen at a glance: the labels and what each one does. McConnell asks for the code in each case to be short, and for complicated actions to go into a routine (pp. 353-354).

## Rule

Keep the actions of each case simple. Short arms make the structure of the `case` statement clear. If the actions for a case are complicated, write a routine and call it from the case rather than putting the code into the case itself (pp. 353-354). The checklist asks whether the actions for each case are simple, with calls to routines as needed (p. 358).

## Sign in code

- A `switch` arm that holds a loop, a nested `if` of its own, or more lines than fit beside the other labels (this wiki uses about five lines as the point to look), so that the labels of the `switch` cannot be seen on one screen.
- Arms of very uneven length, where one arm hides the rest.

This wiki assigns the neighbouring cases as follows. A long arm of a `case` or `switch` is this page; a long unnamed block elsewhere in a routine is [[extract-routine-to-name-a-step]], which supplies the extraction both use. Arms that are the same few lines with different data are [[drive-repeated-dispatch-from-a-table]]. A switch over an object's type code is [[polymorphism-or-type-switch]] first, because extracting its long arms into routines yields that page's sign. In a state machine's step function, a case arm that computes over the controlled data inline is [[separate-control-object-from-state-logic]]; a long arm elsewhere is [[keep-case-arms-short]].

## When not to apply

The book states no limits. This wiki's own:

- An arm of two or three statements that read as one action is already simple; extracting it adds a name and a jump without adding meaning.
- If every arm is the same few lines with different data, extraction is the wrong repair; [[drive-repeated-dispatch-from-a-table]] owns that shape.

## Repair

1. For each long arm, name the action it performs.
2. Move its body into a routine with that name, passing what it needs.
3. Leave one call (and the `break`, where the language needs it) in the arm.

Arms that share and modify many local variables are hard to extract without a long argument list. That is a sign the enclosing routine needs splitting differently ([[routine-cohesion]]), not a reason to leave the long arm.

## Before and after

```
switch event:
    case SAVE:
        if not dirty: return
        for each buffer in openBuffers:
            if buffer.modified:
                write(buffer)
                buffer.modified = false
        status("saved")
    case QUIT:
        close()
    default:
        internalError("unexpected event")
```

```
switch event:
    case SAVE: saveModifiedBuffers()
    case QUIT: close()
    default:   internalError("unexpected event")
```

The arms end on their own in this pseudocode, with no fall-through.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.2, pp. 353-354; checklist, p. 358. The line threshold, the assignment against the neighbouring pages, the limits, the reading of shared locals as a cohesion problem and the pseudocode are this wiki's own.
