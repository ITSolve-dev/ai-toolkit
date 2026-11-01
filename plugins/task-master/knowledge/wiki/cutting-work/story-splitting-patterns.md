---
title: Story Splitting Patterns
category: cutting-work
summary: The three-step procedure and nine patterns for cutting a too-big task into thin vertical slices, each pattern with the trigger that selects it.
tags: [method, decomposition, splitting]
sources: [humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
---

# Story Splitting Patterns

This is the Humanizing Work procedure for cutting a task that is too big. Run it on a request or a task before it reaches a board. The authors' example stories were lost in extraction ([[humanizing-work-splitting]]), so this page keeps the triggers and the moves and does not reconstruct the examples.

## The procedure

1. **Make the input a real increment of value.** The authors say to start by checking the input against [[invest]], "(other than small)" (L183). If it fails on value, go to [[component-task-masquerading]] and combine it.
2. **Ask whether it is too big.** That is the question [[size-ceiling]] answers. If it is too big, apply the patterns in the table below.
3. **Choose among the possible splits**, using [[choosing-between-splits]].

## The patterns

The authors number the patterns, and the spike comes last by design. All line references are to [[humanizing-work-splitting]].

| # | Pattern | Trigger | Move | Lines |
|---|---|---|---|---|
| 1 | Workflow steps | The task hides a multi-step process | Build the simple end-to-end case first, then add the middle steps and special cases | L193-L209 |
| 2 | Operations | The word "manage", or several operations under one name | One task per operation | L215 |
| 3 | Business rule variations | A general phrase hides several rules of similar weight | One task per rule | L225-L231 |
| 4 | Variations in data | Complexity comes from kinds of data | Build the simplest version and add variations as they appear; list them up front when they are already known | L235-L253 |
| 5 | Data entry methods | Complexity is in the interface and not in the function | Simplest possible interface first, the richer one second | L257 |
| 6 | Major effort | Most of the work goes into whichever part comes first | One task for any one of them, and one task for the rest, given one is done | L265-L271 |
| 7 | Simple/complex | The task grows as it is discussed | Capture the simplest version, and move every variation into its own task | L275-L285 |
| 8 | Defer performance | Much of the effort is in making it fast, secure or scalable | "Make it work", then "make it fast" | L289-L297 |
| 9 | Break out a spike | The implementation is poorly understood | See [[spike-as-last-resort]] | L301-L309 |

## Points the table cannot carry

**Pattern 1 has a wrong way.** The natural cut, one task per step, is what the authors warn against:

> Either way, the most obvious split—one step at a time from beginning to end—is the wrong way to go.
>
> — [[humanizing-work-splitting]], L209

The authors' reason is that "the biggest value often comes from the beginning and end. The middle steps add incremental value, but don’t stand alone." (L195). When the whole workflow matters, their alternative is "a thin slice through the whole workflow" (L207). The sign in a cut is a list of tasks named after successive steps of one process.

**Pattern 8 has a trap.** The authors warn: "It’s easy to get in a habit of calling stories done that aren’t really done, accumulating debt you’ll pay for later." (L297). This wiki reads that as a reason to give both halves their own acceptance check, following the authors' "(in under 5 seconds)" (L293), per [[testable-acceptance]].

**Patterns 5 and 6 leave a dependency in place.** The authors say so at L257 and L271, and that is accepted. [[independent-tasks]] records why it is acceptable.

**Pattern 7's trigger is a meeting.** The authors place it "in a planning meeting" (L275), with the signs “what about x?” and “have you considered y?”. The plugin runs no meetings, so this wiki moves the trigger to text: a request or a clarification thread that keeps adding "what about" items.

## Agent executor note

The patterns come from coaching human Scrum teams, with no measurement. They survive an agent executing because their triggers lie in the work and their purpose lies with whoever reviews it. Only pattern 7's setting depends on people talking in a room.

## Related

The patterns share one underlying move, which [[find-core-complexity]] describes and which can be used directly.
