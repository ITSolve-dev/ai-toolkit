---
title: Independent Estimates
category: sizing
summary: Estimators commit before seeing each other's numbers, and a spread is treated as evidence of a differing assumption to surface, not as noise to average; what remains of planning poker once its meeting script is removed.
tags: [rule, estimation, planning-poker, divergence]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Independent Estimates

Independent estimating means each estimator commits to a number before seeing anyone else's, and a difference between them is treated as information. It is the mechanism inside planning poker (Grenning 2002, cited at [[cohn-agile-estimating-planning]] L1310), which Cohn calls the best way he has found for agile teams to estimate. This wiki keeps the mechanism. The deck, moderator and sand timer are a meeting script and are out of scope. This rule detects: a spread is the sign that estimators do not share an assumption.

## The rule

Collect estimates before anyone sees another's. Where they differ, find out what the high and low estimators assumed. Re-estimate after that, and stop when the numbers are close enough.

## The steps that carry the mechanism

**Commit first.** "Cards are not shown until each estimator has made a selection." (L1318). All are then revealed together (L1318). Cohn gives no reason for the privacy in this chapter. This wiki's reading is that a number seen first anchors the next one.

**Read the spread.** "It is very likely at this point that the estimates will differ significantly. This is actually good news. If estimates differ, the high and low estimators explain their estimates." (L1320). Cohn states the aim as "Instead, you want to learn what they were thinking about." (L1320).

His example shows what a spread contains. The high estimator raises testing cost and adds: "Also, I’m not sure if our standard compression algorithm will work and we may need to write one that is more memory efficient." (L1322). The low estimator proposes a simpler storage choice and concedes: "Also, I didn’t think about having more data—maybe that will be a problem." (L1328). This wiki reads the spread as two facts about the work, one a design option and one a requirement nobody had written down.

**Stop on reasonableness.** "It rarely takes more than three rounds but continue the process as long as estimates are moving closer together." (L1332). Exact agreement is not needed: "It isn’t necessary that everyone in the room turn over a card with exactly the same estimate written down." (L1332). With 5, 5, 5 and 3, he asks the low estimator if 5 is acceptable, because "Again, the point is not absolute precision but reasonableness." (L1332). This wiki reads the stopping condition as: the estimates have stopped moving, or the remaining difference is one step with no objection.

## Why it works

These claims are Cohn's reports of studies this wiki has not read (L1362-L1368):

- Several expert opinions from all disciplines, per [[who-estimates]].
- Justification. "This has been found to improve the accuracy of the estimate, especially on items with large amounts of uncertainty (Hagafors 1983)." (L1366).
- Missing information. "Being asked to justify estimates has also been shown to result in estimates that better compensate for missing information (Brenner 1996). This is important on an agile project because the user stories being estimated are often intentionally vague." (L1366).
- Averaging. "studies have shown that averaging individual estimates leads to better results (Höst and Wohlin 1998) as do group discussions of estimates (Jørgensen and Moløkken 2002)." (L1368), and "Group discussion is the basis of planning poker and those discussions lead to an averaging of sorts of the individual estimates." (L1368).

This wiki notes that a bare arithmetic average discards the thing the spread was for. The averaging evidence supports a better number. It says nothing about the assumption, and in Cohn's example the assumption is what changed the work.

## What the plugin does with a spread

The assumption goes into the task. This wiki reads a spread resolved in conversation as leaving the task as vague as it was, and that is what [[conversation-moves-into-the-task]] and [[fact-stranded-outside-the-task]] are about. The source says only that notes can be taken for later programming and testing (L1330). Making them part of the task is ours, for an executor that cannot ask. An assumption that cannot be settled yet goes to [[unknowns-surfaced-by-estimating]].

## Signs

- Estimates more than one step apart with no recorded reason.
- An estimate that changed sharply after a discussion, with the task text unchanged. The decision behind the change is in nobody's reach.

Both signs are this wiki's, and a large spread is not itself a defect: Cohn calls it good news. What the sign raises is the question of what the difference was.

## Trade-off

This wiki notes that the rule needs at least two estimators, which is a real cost for a very small project, and each round costs attention. The limit on that discussion is on [[estimating-effort-by-purpose]].

## Agent executor note

The mechanism was built for people, and two of its parts rest on that: justifying oneself to colleagues and being anchored by them. No source here tests either with an agent.

This wiki's suggestion, untested, is that the rule still applies to a person and an agent. If the plugin shows a proposed estimate before the person forms a view, the proposal is the first card turned over. Where the estimate matters, ask for the person's number first, or show the agent's reasoning for the number and read the difference as a spread. Whether two agent runs disagree in a way that reveals assumptions is unknown. Identical answers from one model would not be independent opinions.
