---
title: Separate Size from Duration
category: sizing
summary: Estimate how big the work is first, in a unit that cannot be read as time, and obtain how long it takes from a measured rate, so that a wrong rate does not invalidate the size estimates; a size given in hours, or a date with no size and rate behind it, shows the two have been confused.
tags: [rule, estimation, duration, story-points, velocity, forecast]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Separate Size from Duration

The rule is to estimate the size of work and to obtain its duration separately, from a rate, rather than estimating elapsed time directly. Cohn opens Part II with it:

> Agile teams separate estimates of size from estimates of duration.
>
> — [[cohn-agile-estimating-planning]], L914

## The worked distinction

Cohn contrasts two routes to the same job, moving a pile of dirt (L914-L918):

- **Direct:** look at the pile and the tools and say five hours. This "bypassed any estimate of size" (L914).
- **Through size:** 300 cubic feet of dirt, 6 cubic feet per wheelbarrow load, so 50 trips; each trip takes 3 + 2 + 1 = 6 minutes, so 300 minutes, or 5 hours.

This wiki notes that both routes reach five hours in this constructed example, so it shows the structure of the estimate and not that the indirect route is more accurate. Cohn adds that size alone does not answer the question either: "an estimate of size alone is not useful in this case" (L916). The size has to be converted with a rate. For software, that rate is [[velocity]] and the conversion is [[velocity-range-forecast]].

Chapter 22 repeats the structure with a novel the reader may not open. To say how long it takes, you first guess 600 pages, then a rate of one page per minute, and only then arrive at 600 minutes, or ten hours (L4849). The duration is an output of two separate guesses, and either can be corrected alone.

## Separate units

Cohn calls mixing the two up "A common planning flaw (on traditional as well as many agile teams)" (L4847). His later statement of the rule is about units:

> The best way to maintain a clear distinction between an estimate of size and one of duration is to use separate units that cannot be confused. Estimating size in story points and translating size into duration using velocity is an excellent way of doing this.
>
> — [[cohn-agile-estimating-planning]], L4915

The process is two estimates and one derivation: size in story points, a rate called velocity, and duration as their combination (L4853). Cohn's reason for the unit is that "Because story points are abstract and notional they are pure estimates of size." (L4853).

## Duration does not follow from size

Size and duration are related, but duration also depends on who does the work and how many are doing it, so a single number cannot state both. Cohn's illustration:

> A four-person team may take six months (24 person-months). An eight-person team may reduce that to four calendar months but 32 person-months, even though the project is of the same size in both cases.
>
> — [[cohn-agile-estimating-planning]], L4847

These figures are invented to make the point, and nothing was measured. This wiki reads the example as showing a further thing the source does not state: person-months are not a size either, since the same project costs 24 in one setup and 32 in another.

## What breaks when it is ignored

Cohn's reason appears in the painting example. Room estimates stay valid when the true dimensions turn out larger than assumed, because only the rate of progress changes (L1037). He concludes:

> estimating in story points completely separates the _estimation of effort_ from the _estimation of duration_ . Of course effort and schedule are related, but separating them allows each to be estimated independently. In fact you are no longer even estimating the duration of a project; you are computing it or deriving it.
>
> — [[cohn-agile-estimating-planning]], L1039

This wiki reads the consequence this way: a duration estimated directly carries both the size belief and the rate belief in one number, so when the rate proves wrong, every estimate has to be redone. With the two apart, one measured number changes and the rest stand. See [[velocity-self-correction]].

## Sign of a violation

These signs are this wiki's derivation; the chapter states none. Each raises a question to check.

- A task carries an estimate in hours or days and no size. Ideal days are the exception, because they are stated as a size; see [[ideal-days]].
- Some tasks on a project are in points and others in time.
- A planned date exists with no size total or rate behind it.
- After a slow iteration, the task estimates are rewritten across the board and the rate is left alone. See [[re-estimate-when-relative-size-changes]].
- Estimates of unstarted tasks all shift at once when only the executor or team changed, which suggests the numbers were durations.

## Trade-offs

The rule requires a rate, and a rate takes completed work to measure. Before any exists, velocity has to be estimated, which Cohn calls difficult and defers to Chapter 16 (L1023-L1029). Size also inherits the looseness of [[story-points]]: this wiki notes that Cohn uses "size" and "effort" interchangeably across Chapter 4 (L953-L955, L1039), so the separation is from duration only, and not a claim that size is one clean quantity.

## Agent executor note

The transfer here is this wiki's, not Cohn's. The separation is structural and does not depend on who executes: it holds wherever a rate can be read from board history. It may matter more with an agent, since the rate is what shifts when the executor changes, and sizes kept apart from the rate would survive that change. Changing the model or the way results are reviewed changes the rate and leaves size alone, so sizes stay usable where a duration estimate would have gone stale, though [[filling-a-period]] warns that older rates then become a poor guide. The chapter gives no evidence on that point.

Cohn's stated reason, that programmers "of different skill and experience levels" take different amounts of time (L4847), is a human one, and the team-size figures rest on human coordination and do not transfer. No source here says whether points stay comparable when an agent assigns them ([[size-ceiling]]).

## Related

[[forecast-range-and-probability]] covers how a derived duration should be stated. [[filling-a-period]] uses the rate to select work.
