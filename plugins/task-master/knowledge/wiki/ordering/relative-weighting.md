---
title: Relative Weighting
category: ordering
summary: Wiegers's method scores each feature 1-9 on benefit if present and penalty if absent, adds them, and divides its share of total value by its share of total cost; the percentages do not change the order, the score omits urgency, learning and risk, and it rewards cheapness.
tags: [method, ordering, prioritization, value, estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Relative Weighting

Relative weighting, from Karl Wiegers (1999), turns judgements of value and an estimate of cost into one number per feature. Like the [[kano-questionnaire]] it looks at both presence and absence of a feature. The difference: "Rather than use questionnaires, this approach relies on expert judgment." ([[cohn-agile-estimating-planning]] L2510). The source has the team do this "Collaboratively, but led by the product owner" (L2510). Running that session is out of scope here; the calculation and its limits are what this page keeps.

## Procedure

1. **Score each feature 1-9 twice:** for "the benefits it will bring if implemented as well as the penalty that will be incurred if it is not implemented" (L2510). "As with estimates of story points and ideal time, the estimates of benefits and penalties are relative." (L2510). This wiki reads that as a reason to score the list together, since a score has no meaning outside its comparisons.
2. **Total Value** = benefit + penalty. "If you wish, you could weight the benefits and penalties." (L2527): doubling the benefit before adding counts it as twice as important.
3. **Value %** = the feature's total value over the sum of all total values (L2529).
4. **Cost %** = the feature's estimate, in story points or ideal days, over the sum of all estimates (L2531).
5. **Priority** = Value % / Cost %. "Higher numbers represent higher priorities because they will create more value for the effort invested in them." (L2533).

| Feature | Benefit | Penalty | Total value | Value % | Estimate | Cost % | Priority |
|---|---|---|---|---|---|---|---|
| Graph event times | 8 | 6 | 14 | 42 | 32 | 53 | 0.79 |
| Can upload photos | 9 | 2 | 11 | 33 | 21 | 34 | 0.97 |
| Post autobiographical profile | 3 | 5 | 8 | 25 | 8 | 13 | 1.92 |
| Total | 20 | 13 | 33 | 100 | 61 | 100 | |

(Table 11.2, L2514-L2519.) The source's conclusion: "Because of its high value to cost ratio, posting autobiographical profiles is the highest priority feature in this analysis." (L2533).

## What the arithmetic actually does

This section is this wiki's derivation and is not in the source.

Priority is (V / sum of V) / (C / sum of C), which equals (V / C) times (sum of C / sum of V). The second factor is the same for every feature on the list, so **the percentages do not change the order.** The order is simply total value per point of estimate: 14/32 = 0.44, 11/21 = 0.52, 8/8 = 1.00, the same order as the table.

Three things follow:

- A plan can skip steps 3 and 4 and compare V / C directly.
- A priority above 1 means a feature takes a larger share of the value than of the cost. It is a statement about this list, and adding a feature rescales every figure, so scores from two lists cannot be compared.
- The figures look more exact than their inputs. Raising Graph event times from a total of 14 to 17 puts it above Can upload photos (17/32 = 0.53 against 11/21 = 0.52), and three points across two judgement scales is well within disagreement. This wiki reads a small gap in Priority as a tie and sends it to [[incomparable-tasks]].

## What the score leaves out

The source's summary calls the result "a single value representing the priority of a feature" (L2561). The same summary lists four factors for prioritizing: learning, risk removed, financial value and cost (L2547-L2555), which are the [[prioritization-factors]]. This wiki reads relative weighting as covering value and cost only, so its number is an input to an order and not the order. It can supply the first sort on [[combining-prioritization-factors]], and the moves for learning and risk still follow.

- **Urgency is absent.** Nothing in the score says what waiting does. Total value is therefore not cost of delay, and the result should not be read as the division on [[cost-of-delay-over-duration]]. The two look alike as a value over a duration, and they differ by that term. Penalty is not urgency either: see [[relative-penalty]].
- **Learning and risk are absent.** A feature that would remove a large risk scores no better for it.
- **Dependencies are absent.** A high score cannot start before its prerequisite ([[sequence-versus-wait]]).
- **Hard constraints are absent.** A must-have can lose on ratio: see [[kano-or-relative-weighting]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Relative benefit | The people steering; the source's experts. The request and stated purpose inform it ([[task-must-justify-itself]]) |
| Relative penalty | The same, asked as what happens if this is never done |
| Estimate | The task, on the project's own scale ([[size-ceiling]]) |
| The list being compared | The set of tasks actually competing for the period or release |

The source gives no tests of the score, so these are this wiki's.

- **Benefit was overrated** if the feature shipped and the gain named at scoring time did not appear.
- **Penalty was underrated** if a low-ranked feature's absence caused a loss.
- **The estimate was wrong** if the task overran ([[overrun-triggers-a-recut]]); the rank rested on a false input and should be recomputed.
- **The ratio starved a large feature** if the same large feature stays at the bottom through repeated rankings while its value goes.

## Cost

- The ratio favours small work: the profile has the lowest value on the list and ranks first. The trade-off is the one on [[cost-of-delay-over-duration]], and the same remedy applies, since a starving large feature is a prompt to cut it.
- It needs two judgements per feature and an estimate for each, and with a few people there may be only one judge, so the check that a group gives is lost ([[ordering-by-value-and-urgency]], Cost).
- It adds two ordinal judgements and divides by an estimate, as if all were measurements. The book does not raise this; the objection is ours.
- Numbers invite [[priority-inflation]] as words do.

## Defects in the source's text

The source says Priority "is calculated by dividing the Priority % by the Cost %" (L2533). The table's arithmetic shows it is Value % over Cost % (42/53 = 0.79), and this page uses that. The Value % of 25 for the profile is rounded so that the column reaches 100: 8/33 is 24%, which would give 1.85 and the same order.

The prose says "uploading photos is probably an exciter" (L2523), while Table 11.1 classes the same feature must-have at 54.3% ([[kano-questionnaire]]). This wiki reads the two tables as separate illustrations and not as one data set.

## Agent executor note

The plugin can lay out the table and do the division, and that is the useful part: the scores are task-only facts ([[recoverable-versus-task-only-facts]]) and belong to the person steering. The cost column inherits what the estimate measures. If the scarce thing with an agent is the attention of the people steering, as [[cost-of-delay-over-duration]] reads it, the estimate should be what the task costs them, not a run's duration. That is unmeasured.
