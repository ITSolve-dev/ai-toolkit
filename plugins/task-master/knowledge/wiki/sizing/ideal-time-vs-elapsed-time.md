---
title: Ideal Time Versus Elapsed Time
category: sizing
summary: Ideal time is how long work takes stripped of everything around it; elapsed time is what passes on the calendar. Ideal time is much easier to predict, and the gap between them is overhead, not work.
tags: [concept, estimation, ideal-time, elapsed-time, overhead]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Ideal Time Versus Elapsed Time

**Ideal time** is how long a piece of work takes with everything around it removed. **Elapsed time** is how long passes on a clock or calendar until it is done. Cohn's illustration is American football: four fifteen-minute quarters make a sixty-minute game that takes around three hours to sit through, and both answers are correct ([[cohn-agile-estimating-planning]] L1080).

> Ideal time is the amount of time that something takes when stripped of all peripheral activities.
>
> — [[cohn-agile-estimating-planning]], L1080

> Elapsed time, on the other hand, is the amount of time that passes on a clock (or perhaps a calendar).
>
> — [[cohn-agile-estimating-planning]], L1080

## Each answers a different question

The officials need ideal time to know when the game is over. Someone asked how long they will be gone needs elapsed time, and answering "sixty minutes" does them no good (L1082). This wiki reads the discriminating question as who is asking and for what: how much work this is calls for ideal time, and when it will be finished calls for elapsed time. Neither value can stand in for the other without a conversion. For software that conversion is [[velocity]], as [[ideal-days]] explains.

## Why ideal time is easier to predict

> It is almost always far easier and accurate to predict the duration of an event in ideal time than in elapsed time.
>
> — [[cohn-agile-estimating-planning]], L1084

Cohn's reasoning is that ideal time depends on few inputs. A quick answer of 60 minutes is available off the cuff, and historical overtime figures refine it (his illustrative result is 62.3 minutes). Elapsed time depends on many inputs. Games ran from 2½ hours to over four, driven by injuries, playing style, penalties, televised timeouts and weather, and matching the off-the-cuff ideal estimate would mean weighing each of them (L1084-L1092). Those figures illustrate the argument and are not measurements of software work.

## What fills the gap in software

On a software project the gap comes from "the natural overhead we experience every day" (L1100). Table 5.1 lists its sources: supporting the current release, training, sick time, email, meetings, reviews and walk-throughs, demonstrations, interviewing, personnel issues, task switching, phone calls, bug fixing in current releases, special projects and management reviews (L1104-L1113).

Cohn cites a figure for interruptions: "managers are able to work an average of only five minutes between interruptions (Hobbs 1987)" (L1117). The measured population is managers. The figure of one interruption every fifteen minutes for a developer is Cohn's supposition of a third of that rate, not a measurement (L1117).

Cohn adds that multitasking widens the gap further: "A software developer who is told to multitask loses a great deal of efficiency while switching between two (or more) tasks." (L1121). This chapter gives no magnitude for that loss. Cohn's study of it is on [[multitasking]].

## The assumptions behind an ideal estimate

An ideal estimate holds under three stated assumptions (L1123-L1129):

- the story being estimated is the only thing you'll work on
- everything you need will be on hand when you start
- there will be no interruptions

These are counterfactual: Cohn asks the estimator to assume them, not to make them true. This wiki notes that the second resembles the plugin's working test for a task, "once started, it can be finished without waiting" ([[unit-of-work]]). The resemblance is not a grounding: that test comes from the plugin's design and has no source, and Cohn's line is an estimating assumption, not a criterion for cutting work.

## Agent executor note

This wiki reads the distinction as surviving, with the contents of the gap changing. The mechanism here is a person's day: most of Table 5.1 (sick time, email, training, interviewing, phone calls) does not apply to an agent, though it still applies to the person steering. The transfer here is ours and unsourced: for agent-executed work the expected remaining gap is waiting on that person, such as a presented result sitting unreviewed, rather than interruption during execution. Time in state read from board history would show whether that holds, and the [[flow-metrics]] count that time; logged hours are not needed and are out of scope.

This wiki does not carry the interruption figures above over to agent-executed work at all.

Related: [[ideal-estimate-read-as-deadline]], [[size-versus-duration]].
