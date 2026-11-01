---
title: Board Misuse Corrupts Flow Data
category: reading-history
summary: Flow data can be no better than the use of the board that produced it. Late updates, uncaptured blockers and random moves leave history that must be repaired or thrown away.
tags: [failure-mode, board-history, data-quality, flow-metrics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Board Misuse Corrupts Flow Data

This failure occurs when a board is not used consistently, so its history cannot support flow metrics however carefully it is extracted. The source's statement is flat: "Your data is only as good as your use of your Agile tracking tool" ([[vacanti-actionable-agile-metrics]] L3834). It holds for both electronic systems and physical boards (L3830).

## Observable signs

The source names three:

> If work items are not updated in a timely manner, or blockers not captured properly, or items are moved back and forth randomly, then that lack of attention to process policies will be reflected in your data.
>
> — [[vacanti-actionable-agile-metrics]], L3836

This wiki reads those as the following marks in board history, each of which raises a question to check (see [[smell-is-not-a-finding]]):

- **Late updates:** several states traversed by one item on the same day, or many items moved at one moment.
- **Uncaptured blockers:** an item idle in an active state for a long stretch with no blocked marker recorded.
- **Random moves:** repeated back-and-forth transitions that match no rework reason. See [[backward-movement]].

## What it costs

"no data extraction scheme will make up for abusing either your electronic or physical board" (L3836). Once the data is bad, the choice left is unpleasant: "try to fix the data or discard it altogether" (L3836). This wiki reads the second consequence as a reset of the sample: discarded history means [[how-much-flow-data]] starts again from zero.

## The rule

The prevention is upstream of the data. The source calls it "a much better strategy to make sure all team members use your Agile tracking tool in an agreed upon matter" (L3836-L3842). The agreement covers what is moved when, and what a blocker looks like on the board.

## Agent executor note

The mechanism in the source is human lapse: people forgetting to update. This wiki's reading is that it only partly survives. An agent moving its own tasks timestamps them as it goes, so lateness on the executor's side should shrink. Lateness moves to the steps a person owns, such as review and acceptance, where a batch of approvals in one sitting produces the same false dates. Board-level automation can also add its own moves. The same signs apply, though they now point at the person's steps.

## See also

[[capturing-flow-data]], [[flow-metrics]], [[waiting-versus-blocked]], [[verifying-tool-flow-analytics]]
