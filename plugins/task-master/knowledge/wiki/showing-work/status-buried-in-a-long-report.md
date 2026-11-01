---
title: Status Buried in a Long Report
category: showing-work
summary: The news that a plan is off track is technically reported but sits where nobody reads it; the sender is responsible for the message being understood, not merely sent.
tags: [failure-mode, visualization, reporting, status]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Status Buried in a Long Report

Status is buried when a report contains the important fact but its reader does not come away knowing it. Cohn places the responsibility on the sender.

> They need to not only hear the message, but also understand it.
>
> — [[cohn-agile-estimating-planning]], L4587

> if the news that a project is behind is “clearly” shown on page 32 of a 40-page weekly status report, it’s quite likely that no one knows it
>
> — [[cohn-agile-estimating-planning]], L4587

## Observable signs

The signs below are this wiki's reading of Cohn's example.

- The conclusion (behind, on track, at risk) is not in the opening lines.
- The reader has to compute the conclusion from the data shown.
- The report grows every period, while the plan's status gets no more visible.

## What to do instead

Cohn's instruction for a project manager reporting a slip is to "do it in such a manner that no one can fail to understand" (L4587). His reason for favouring big, visible charts is that "with no more than a handful of big, visible charts hanging in the team’s workspace it is likely that everyone on the project team will understand the significance of each" (L4587). The number is a qualitative "handful", not a measured limit.

This wiki reads the rule for generated output this way: the first line states the conclusion, the figures that support it follow, and detail comes last or is omitted. A forecast states its range in that first line; see [[stating-plan-uncertainty]].

## Trade-off

A leading verdict hides nuance and has to be right. This wiki separates the two cases: "the plan needs 30 more points than the range allows" is arithmetic and can lead, while a suspected cause is a question to raise, as [[smell-is-not-a-finding]] requires.

## Agent executor note

The mechanism here depends on a human reader rather than a human executor, so this wiki reads it as surviving: the person steering an agent is that reader, and an agent's long report buries a result in the same way. Cohn's wall chart assumes a shared workspace, which a few people working remotely may not have, so the transferable part is the short, unmissable statement and not the wall.

See also [[which-chart-for-which-plan-question]].
