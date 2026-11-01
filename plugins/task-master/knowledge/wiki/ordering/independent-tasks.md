---
title: Independent Tasks
category: ordering
summary: Tasks should not overlap and should be orderable freely; a conditional estimate or a stated precondition is the sign that they cannot be.
tags: [rule, dependencies, invest, decomposition]
sources: [wake-invest, humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
---

# Independent Tasks

Two tasks are independent when neither overlaps the other in concept and either can be done first. Wake's definition:

> Stories are easiest to work with if they are *independent*. That is, we’d like them to not overlap in concept, and we’d like to be able to schedule and implement them in any order.
>
> — [[wake-invest]], L48

## The rule

Cut tasks so that they can be ordered by what matters, with no hidden order among them. Where an order cannot be removed, state it.

Wake concedes that this is a preference and not an absolute: "We can’t always achieve this" (L50). The Humanizing Work authors state a weaker test that can be met: a good story "is sufficiently self-contained that it can be prioritized by something other than technical dependency" (L111). This wiki uses the weaker test, and therefore treats an unstated dependency as the defect and a stated one as acceptable.

## Sign of violation

- **In the task text or estimate:** an estimate that depends on order. Wake's example is "3 points for the first report, then 1 point for each of the others" (L50). The number only holds if the tasks run in one sequence, so the order is real even if nothing says so.
- **In the task text:** two tasks whose acceptance would change the same behaviour. That is the overlap in concept Wake names. This reading of how overlap shows up in text is this wiki's.
- **Across tasks:** a set of tasks of which one absorbs most of the effort, whichever is scheduled first. The authors' case is one story per credit card type, where "the credit card processing infrastructure will be built to support the first story; adding more card types will be relatively trivial" (L267).

## Why

What breaks is ordering. If the order is fixed by construction, the prioritization step has nothing left to decide, and any later reordering silently invalidates the estimates. The authors name exactly that risk: an estimate that loads the first story means "we have to remember to change our estimates if the Product Owner later changes priorities" (L267).

## What to do with a dependency that cannot be removed

The authors give three moves, and in each the dependency stays but is made harmless:

- **Scaffold it.** "Sometimes that means temporarily building some scaffolding so a story can be tested independently, allowing you to do it sooner to get value or reduce risk early in a project." (L111). The cost is that the scaffolding is built and later removed.
- **Defer which one comes first.** Replace one task per item with a task for any one of them and a task for the rest, given one is done. The authors' wording for the second is "…I can pay with all four credit card types (VISA, MC, DC, AMEX) (given one card type already implemented)." (L269), and they accept the result: "The two new stories still aren’t independent, but the dependency is much clearer than it would be with a story for each card type." (L271).
- **Accept it when the pieces are one thing done twice.** A simple interface and then a fancier one: "These, of course, aren’t independent—the second story effectively is the original story if you do it first—but it still can be a useful split." (L257).

## Cost

Independence competes with size. The authors say "As stories get smaller, for example, it becomes harder to make them independent and valuable." (L125), so cutting finer will produce more dependencies, and [[invest]] records when each letter matters more.

## Agent executor note

The rule concerns the structure of the work and does not depend on who executes it, so it survives. Both sources speak from the practice of human teams, and no measurement supports it.
