---
title: Bug Allocation
category: periods
summary: Bugs enter a period as estimated work inside an amount the owner chooses; a new bug that must go in now is estimated and an equal amount of unstarted work comes out.
tags: [rule, iterations, commitment, bugs, intake]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Bug Allocation

This rule handles bugs inside an iteration as ordinary planned work with a budget. Cohn offers it for teams "faced with a large number of legacy bugs" while "bugs continue to come in at a rapid rate" ([[cohn-agile-estimating-planning]] L4494). It has two parts.

**The allocation.** The product owner decides the share of the period, and the bugs are then chosen to fit:

> The product owner selects how much of an iteration should be directed toward bug fixing rather than new feature development.
>
> — [[cohn-agile-estimating-planning]], L4498

His example is a row such as "Fix ten ‘high’ bugs", where the product owner selects the ten, developers write an estimated card for each, and those cards are worked "in the same way they work on other task cards" (L4496). He says "The team could allocate 40 hours to bug fixing or they could allocate 100 hours." (L4498). Those figures illustrate a free choice and are not a benchmark: no team size or iteration length comes with them.

**The swap.** A bug found mid-period that the team considers high priority goes in by displacement: "The developers are asked to estimate it and then remove an equivalent amount of work from the To Do column of the task board." (L4496).

This wiki notes that the removal comes from To Do, so the swap touches only unstarted work and leaves what is in progress alone.

This page concerns bugs that are not part of the current period's own work. A defect found in that work finishes with it, and a later one is ranked like any other item ([[defect-inside-or-outside-the-iteration]]). This wiki reads the swap as the route for a later defect ranked high enough to enter now.

## The rule

1. Before a period, whoever owns the scope sets how much of it goes to bugs. The bugs that fit are selected and estimated like any other task.
2. During a period, a bug that must go in now is sized, and an equal amount of unstarted work comes out.

## Inputs, where each is read from, and what would show the choice wrong

The table and the failure conditions are this wiki's.

| Input | Read from |
|---|---|
| Share for bugs | Stated by whoever owns scope; the size of the selected bug tasks shows it |
| Which bugs | Open bugs, ordered per [[ordering-by-value-and-urgency]] |
| Whether a new bug goes in now | [[interrupting-started-work]] and [[urgent-versus-important]] |
| What comes out | Unstarted tasks in the selection, lowest order first |

The share was wrong if open bugs keep growing across periods despite it, or if it goes unused while bugs stay open.

## Sign of violation

- **In board history:** a task added during a period with its total of remaining work rising and nothing removed.
- **In board history:** a started task pulled back to make room, where the swap should have taken unstarted work.
- **In board state:** bugs worked in a period that were never selected or sized, so the amount going to bugs cannot be read.

Cohn describes the practice. These signs are this wiki's. A rise alone also fits a corrected estimate ([[overrun-triggers-a-recut]]), so the sign raises a question.

## Why

What breaks without it, in Cohn's framing, is that bugs stay fixed "someday" (L4494) while the backlog grows. This wiki reads the allocation as moving the rate of fixing from an accident to a decision, and the swap as keeping a period's total honest ([[filling-a-period]]).

## Cost

Feature work is displaced openly and by a known amount. The swap also assumes a bug can be sized before it is fixed, which is often not so before it has been reproduced ([[reproduce-before-accepting]]). A size guessed there makes the swap a guess too.

## Agent executor note

Cohn's mechanism does not depend on human memory or pace and survives. The product owner and the team are often one person when a few people steer an agent, so the joint selection he describes has no second party ([[mid-period-change]]). The plugin can propose the swap and show what would come out, and the people steering decide.

## Which holds under which setup

The resolution is this wiki's.

- **Iteration setup with a goal:** two tests apply and they differ. Cohn's swap keeps the amount of work level, and [[mid-period-change]] protects the goal. The goal check goes first, so the swap takes out work that does not serve the goal. If everything left serves it, the bug waits or the case goes to [[interrupting-started-work]].
- **Iteration setup with no goal:** the swap alone applies.
- **Flow setup:** there is no period total to preserve. The bug waits for capacity under [[wip-control]], or it uses an exception declared in advance. A share for bugs can still be kept as a ratio of what is pulled, which no source here states.
