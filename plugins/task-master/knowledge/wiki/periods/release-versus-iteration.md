---
title: Release Versus Iteration
category: periods
summary: An iteration is a timebox; a release is a set of related functionality built across iterations. What ends the unit, a date or a content set, separates them.
tags: [decision-rule, iterations, release, period-versus-milestone]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Release Versus Iteration

A release and an iteration are both spans of work, but they are defined differently. An iteration is defined by time. A release is defined by a body of related functionality, delivered across one or more iterations.

> A release comprises one or more (usually more) iterations that build upon each other to complete a set of related functionality.
>
> — [[cohn-agile-estimating-planning]], L776

Cohn's reason a release exists at all is that one iteration is too short for a result users would want: "a single iteration does not usually provide sufficient time to complete enough new functionality to satisfy user or customer desires" (L776).

## The test

This wiki states the discriminating question as: what ends this unit? If the end is a date and the content gives way, it is a period, handled as a [[timeboxed-iteration]]. If the end is a coherent set of functionality, it is a release, which is Cohn's closest equivalent of a milestone. Cohn does not phrase the test this way; the phrasing is this wiki's, drawn from the definitions at L764 and L776. It is the same test as "A period versus a milestone" on [[commitment-over-a-period]], which asks which of the two gives way when they collide.

A release can still carry a date. Whether its date or its content yields is settled through [[conditions-of-satisfaction]], not by its definition: Cohn says the product owner "may, for example, be equally satisfied with a release in five months that includes one set of user stories as with a release a month later" (L857).

## Numbers, with their conditions

- "While iterations are most commonly one to four weeks, a release is typically two to six months." (L776).
- The summary and the discussion of Figure 3.2 give three to six months for a release plan (L872, L896). The chapter is inconsistent between these; neither figure is derived.
- Worked case: an investment management system, one release for mutual and money market funds, six two-week iterations, roughly three months; a second release for stocks and bonds, four more two-week iterations (L776).
- "Releases may occur at varying intervals." (L776). This wiki reads that as iteration length tending to be regular while release length does not need to be.

These figures describe human teams. This wiki reads the shape as surviving a few people steering an agent, and the month counts as not surviving it.

## Signs to check

Cohn gives none. This wiki reads these as questions.

- A period on the board has a target set of features and its end date moved to fit them. It is being run as a release while named as an iteration.
- A release has no coherent statement of what it completes, only a date. It is then a long period, and it cannot use Cohn's definition.

Related: [[planning-horizons]], [[fixed-date-variable-scope]], [[potentially-shippable-increment]].
