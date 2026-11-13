---
title: Should We Include Waiting or Blocked Items in WIP Limits?
category: work-states
summary: A Kanban Maturity Model answer to whether stopped work counts toward WIP limits; blocked items stay and count, items waiting on outsiders may be parked, and a parked item past its time becomes blocked.
tags: [summary, work-states, wip, kanban]
sources: [radzikowska-waiting-blocked]
created: 2026-11-01
updated: 2026-11-02
---

# Should We Include Waiting or Blocked Items in WIP Limits?

This is a short "Kanban Evergreen" article from the David J. Anderson School of Management site, djaa.com. The raw file's `authors` field is empty and the text names no author. "Radzikowska" in the slug comes from how the source was recorded at scouting and cannot be confirmed from the file.

The article answers a poll question from the Kanban Maturity Model (KMM): "Let’s examine what we can learn about this case from the Kanban Maturity Model." (L26). It also advertises the school's classes (L30, L78).

## Thesis

The article gives a conditional yes. Blocked items stay where they are and count toward the column's limit (L34). Items waiting on an external group may go to a parking lot, with the time tracked, and become blocked when the agreed time expires (L44-L53). The parking lot can have its own limit (L57-L63). Limits on stopped work cause stress, so the source recommends them only at higher organizational maturity (L69-L76).

## Extraction caveat

- The poll results are missing. L21 introduces them and nothing follows.
- The three types of blocker are missing. L30 says "we identify and recognize three types of blockers or waiting items", and no list follows. This wiki does not reconstruct them, so the two-way test on [[waiting-versus-blocked]] may be coarser than the source's.
- The passages at L32-L34, L44-L53 and L57-L63 end in footnote marks that lead to KMM practice entries, which suggests they are the model's text and not the article writer's, but the raw file does not mark them as quotations. This wiki attributes them to the source and treats them as the KMM's position.
- The footnotes in the raw file are all numbered "1." (L82-L88). They match the markers (1) to (4) in order: XP 3.0, VZ 3.9, LW 4.1, and Overreaching.

## What this wiki took from it

- What separates waiting from blocked: [[waiting-versus-blocked]].
- Blocked work stays in place and counts: [[blocked-work-counts-against-wip]].
- Parking external waits, tracking the time, and the expiry rule: [[parking-lot]].
- How to set a first limit on the parking lot: [[parking-lot]].
- The external wait as one side of the sequence-or-wait distinction: [[sequence-versus-wait]].

## What this wiki dropped, and why

- **The poll** (L19-L24). "Most participants" is a claim about opinion with no figures, and the results did not survive extraction.
- **The escalation policy** (L38-L40) as a procedure. Agreeing a documented policy across stakeholders and organizational roles belongs to a larger organization. The distinction it rests on, between what can be resolved locally and what cannot, is kept on [[waiting-versus-blocked]].
- **Service Delivery Reviews and Operations Reviews** (L59, L63). They are meetings.
- **Maturity levels as a gate** (L74-L76). The argument depends on human resistance and on an organizational self-assessment that a board does not show. It is kept as a stated cost on [[blocked-work-counts-against-wip]] and not as a rule.
- **Spawning a peer ticket as a variant** (L48). It describes a way of drawing the dependency, with no sign and no reason to prefer it.

## How to read it

Read it as one methodology's position, stated by practice rather than demonstrated. It reports no measurement, and the mechanisms it offers for limits are human ones: tension, stress and resistance. The criteria for what counts as waiting and what counts as blocked do not depend on people, and they are the most durable part.
