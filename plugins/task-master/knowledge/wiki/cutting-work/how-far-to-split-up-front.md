---
title: How Far to Split Up Front
category: cutting-work
summary: Decide whether to enumerate all the pieces of a large request or cut only one or two, by whether starting the work will teach you what the work is.
tags: [decision-rule, decomposition, splitting, cynefin]
sources: [humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-02
---

# How Far to Split Up Front

Before cutting a large request, decide how much of it to cut now. The Humanizing Work authors answer this with Dave Snowden's Cynefin model. The raw file names the domains and links to the authors' overview of them, but does not define them, so this wiki does not rely on the domain definitions. It relies on the operational test the authors give for the case that matters:

> The most important nuance is in the complex domain, where starting the work will teach you about the work. In this situation, it doesn’t make sense to try to find all the small stories that add up to the original, big one. Instead, it’s more productive to find one or two you can start right away in order to learn.
>
> — [[humanizing-work-splitting]], L344

## The choices

| Case | What to do | Line |
|---|---|---|
| Obvious | "Just build it. Or, if it’s too big, find all the stories, and do the most valuable ones first." | L338 |
| Complicated | "Find all the stories, and do the most valuable and/or most risky ones first." | L339 |
| Complex | "Don’t try to find all the stories. Find one or two that will provide some value and teach you something about the problem and solution, build those and use what you learn to find the rest." | L340 |
| Chaotic | "Put out the fire; splitting stories probably isn’t important right now." | L341 |
| Disordered | "Figure out which domain you’re in before splitting so you don’t take the wrong approach." | L342 |

For a request that is neither obvious nor on fire, the working question is the one test: will starting teach us what the work is? If yes, cut one or two slices using [[choosing-between-splits]]. If no, enumerate.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Whether the outcome depends on people's preferences or behaviour | The request, using the authors' guidance at L315 |
| Whether it needs a new integration or external dependency | The request and the repository |
| Whether similar work has been done | Finished tasks on the board |

The inputs above are this wiki's translation of the test into things that can be read, and so is their combination: treat the request as complex if either of the first two holds and similar work has not been done, and otherwise enumerate. The authors give no combination, and L315 is their guidance for finding the core complexity, not their Cynefin test, so the result informs a judgement that the person steering confirms. The choice was wrong in one of two directions. If everything was enumerated and the task list was then substantially rewritten after the first tasks finished, the work was complex and the list was false precision. If one slice was cut and the tasks found afterwards matched what could have been listed at the start, the caution bought nothing.

## Trade-off

The cost of the complex choice is that there is no complete list to project a date from. The authors accept that cost:

> Some are uncomfortable with this approach, wanting all the stories enumerated and sized to be able to project time over the backlog. But if you’re really in the complex domain, this only gives you the illusion of predictability—the actual stories are likely to change as you get into the work.
>
> — [[humanizing-work-splitting]], L346

This wiki reads that as a reason for the plugin to state its uncertainty and not to fill out a list it expects to change. A coarse list written only to see the shape of the work is a different thing, on [[initial-task-inventory]]. When a large task has to be cut at all is on [[size-ceiling]].

## Agent executor note

The evidence is coaching experience with human teams, with no measurement. The test survives an agent executing, because the work is what teaches. The learning still has to reach whoever steers: an agent's finished slice teaches the project only once someone reads the result and revises the remaining tasks.
