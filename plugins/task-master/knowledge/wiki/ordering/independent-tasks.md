---
title: Independent Tasks
category: ordering
summary: Tasks should not overlap and should be orderable freely; a conditional estimate or a stated precondition is the sign that they cannot be, and work inside one task that restates another open task is an overlap found late, which can be held as a reserve until the commitment is settled.
tags: [rule, dependencies, invest, decomposition]
sources: [wake-invest, humanizing-work-splitting, montgomery-tracker-smells, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Independent Tasks

Two tasks are independent when neither overlaps the other in concept and either can be done first. Wake's definition:

> Stories are easiest to work with if they are *independent*. That is, we’d like them to not overlap in concept, and we’d like to be able to schedule and implement them in any order.
>
> — [[wake-invest]], L48

## The rule

Cut tasks so that they can be ordered by what matters ([[ordering-by-value-and-urgency]]), with no hidden order among them. Where an order cannot be removed, state it.

Wake concedes that this is a preference and not an absolute: "We can’t always achieve this" (L50). The Humanizing Work authors state a weaker test that can be met: a good story "is sufficiently self-contained that it can be prioritized by something other than technical dependency" (L111). This wiki uses the weaker test, and therefore treats an unstated dependency as the defect and a stated one as acceptable.

## Sign of violation

- **In the task text or estimate:** an estimate that depends on order. Wake's example is "3 points for the first report, then 1 point for each of the others" (L50). The number only holds if the tasks run in one sequence, so the order is real even if nothing says so.
- **In the task text:** two tasks whose acceptance would change the same behaviour. That is the overlap in concept Wake names. This reading of how overlap shows up in text is this wiki's.
- **Across tasks:** a set of tasks of which one absorbs most of the effort, whichever is scheduled first. The authors' case is one story per credit card type, where "the credit card processing infrastructure will be built to support the first story; adding more card types will be relatively trivial" (L267).
- **Across tasks:** a cycle among stated dependencies. The study behind [[montgomery-tracker-smells]] lists this as a smell, "Issues A is linked as a dependency of B, and B is also linked as dependency of A." (L203). Its result is in a lost figure. This one needs no perception behind it, since neither task can start first if the links are right, so it shows that at least one link is wrong or the tasks are one task.

## Why

What breaks is ordering. If the order is fixed by construction, the prioritization step has nothing left to decide, and any later reordering silently invalidates the estimates. The authors name exactly that risk: an estimate that loads the first story means "we have to remember to change our estimates if the Product Owner later changes priorities" (L267).

## What to do with a dependency that cannot be removed

The authors give three moves, and in each the dependency stays but is made harmless:

- **Scaffold it.** "Sometimes that means temporarily building some scaffolding so a story can be tested independently, allowing you to do it sooner to get value or reduce risk early in a project." (L111). The cost is that the scaffolding is built and later removed.
  When to scaffold and when to leave the dependency in place is on [[handling-a-sequence-dependency]].
- **Defer which one comes first.** Replace one task per item with a task for any one of them and a task for the rest, given one is done. The authors' wording for the second is "…I can pay with all four credit card types (VISA, MC, DC, AMEX) (given one card type already implemented)." (L269), and they accept the result: "The two new stories still aren’t independent, but the dependency is much clearer than it would be with a story for each card type." (L271).
- **Accept it when the pieces are one thing done twice.** A simple interface and then a fancier one: "These, of course, aren’t independent—the second story effectively is the original story if you do it first—but it still can be a useful split." (L257).

## An overlap found while cutting

Overlap often surfaces only when work is written out concretely. In the fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961), breaking down the human-versus-human story produces the card "Computer knows when a piece completes a winning pattern" (L5843). A tester notices: "Wait, doesn’t this story encompass another story we wrote? We have one that says _As a player, I want the computer to recognize a winning shape_ ." (L5824). Line references in this section are to that source.

**Sign, in task text:** a task's acceptance, or a piece of its work, restates the title of another open task, in the same or different wording. This can be read before anything reaches a board. The wording is this wiki's.

**What to do.** The analyst does not resolve it on the spot: "We included it by accident, Let’s see if we can commit to the work we just identified. If we can’t, we can remove having the computer recognize winning shapes and let the players decide when a game is over," (L5826). This wiki reads that as a useful move: an accidental inclusion is a named piece that can be dropped if the commitment does not fit, which gives a reserve with no new estimate. It only works if the part is really separable. In the case it was: the story was dropped during the iteration so that its programmer could help on the engine (L6223-L6225), and two people could still play (L6235).

**What it does to counting.** The team says it committed to three stories (L5933), while the velocity sum names four, crediting the absorbed story's 2 points separately (L6169). When that story was dropped its 2 points fell out and velocity was 16 (L6263), while the absorbing story's 3 stood. This wiki reads that as saying an overlap has to be settled by naming which task holds the work, or the same work is counted in two places. See [[planned-velocity]].

**What breaks if it goes unnoticed.** This wiki's reading is that the same work is estimated twice, so release totals are inflated, and it may be done twice. That matters more with an agent, which will not recognise from memory that a sibling task already did the work. The intake form of the same defect is on [[duplicate-reports]].

## Cost

Independence competes with size. The authors say "As stories get smaller, for example, it becomes harder to make them independent and valuable." (L125), so cutting finer will produce more dependencies, and [[invest]] records when each letter matters more.

## Agent executor note

The rule concerns the structure of the work and does not depend on who executes it, so it survives. Both sources speak from the practice of human teams, and no measurement supports it.
