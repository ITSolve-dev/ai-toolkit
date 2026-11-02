---
title: Estimation Scale
category: sizing
summary: Estimates sit on a small predefined non-linear scale, kept for near-term work within about one order of magnitude, because gaps must grow with uncertainty; a step is a bucket, an estimate moves only by a step, and a value between steps, or a split reconciled to its original by arithmetic, is false precision.
tags: [rule, estimation, scale, false-precision]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Estimation Scale

An estimation scale is the fixed set of values an estimate may take. Cohn's position is that the set should be predefined, non-linear, and for near-term work span about one order of magnitude. This rule both chooses and detects: it chooses the scale at project setup, and it catches values that do not belong on it. It applies to [[story-points]] and to [[ideal-days]] alike.

## The rule

Fix the values before estimating starts. Give every estimate one of them. Treat each value as a bucket, not a measurement.

## Which scales

Cohn reports success with two ([[cohn-agile-estimating-planning]] L1226, L1228):

- 1, 2, 3, 5, 8, which he calls the Fibonacci sequence
- 1, 2, 4, 8, where each number doubles the last

Of the two he writes: "Either sequence works well although my slight personal preference is for the first." (L1230). This wiki takes that as saying the choice between them carries no weight, and the fact that only one is used on a project carries the weight.

Larger numbers such as 10, 20, 30, 50, 100 are "fine since these are also within a single order of magnitude", with a recommendation: "I still recommend that you pre-identify the numbers you will use within that range." (L1244). Steps for distant work are on [[estimating-by-horizon]].

## Why

**One order of magnitude.** "Studies have shown that we are best at estimating things that fall within one order of magnitude (Miranda 2001; Saaty 1996)." (L1222). This wiki has not read the cited studies, and the claim is held on Cohn's report of them. It is also the reason behind the 1–10 preference left open on [[story-points]].

**Non-linear gaps.** "These non-linear sequences work well because they reflect the greater uncertainty associated with estimates for larger units of work." (L1230). The case study in Chapter 23 repeats it: "And we need to remember that estimates of very large features are likely to be less accurate. That’s why the ranges get bigger." (L5363). This wiki reads the gaps as a statement of what the estimator knows, which is why a step that looks exact at the top of the scale would misrepresent it.

## Bucket, not measurement

Cohn writes: "Each of these numbers should be thought of as a bucket into which items of the appropriate size are poured." (L1232). His image is sand and not water: a story the slightest bit bigger than other fives can go in the five bucket. His limit is that "A story you think is a 7, however, clearly would not fit in the five-point bucket." (L1232). This wiki reads that as: a small excess may round down, and a clear excess moves up a step.

The fictional case study in Chapter 23 (L4961) runs the image on a scale ending as "0, 1, 2, 3, 5, 8, 13, 20, 40, and 100" (L5525). Those values are the book's convention, and the chapter gives no measurement for them. Asked whether to make up a 16 between 13 and 20, the coach answers:

> If this story is a 16, it won’t fit in a bucket that holds 13. We don’t want to make up new values because it starts to look too precise. We don’t know if this is a 13 or a 16 or a 19. It’s important to remember that these are estimates, not guarantees.
>
> — [[cohn-agile-estimating-planning]], L5435

The chapter then shows the tolerance at the boundary. A story judged 2 to 3 times an 8 comes to 16 to 24, which overflows a 20, and the programmer asks whether that forces a 40. The coach says no: "They’re buckets, but think of the contents as sand, not water. You can overfill it a tiny bit at the top." (L5439). It becomes a 20 (L5443-L5445). This wiki reads the deciding fact as the programmer's own: a 40 would misstate the comparison, since "It’s not five times as big as the medium engine." (L5437).

## The top of the scale records size

The large steps exist to say that a task is large and not to schedule it.

> Considering the stories that we’ve estimated so far, any story we estimate at 100 story points is not going to fit into a single iteration. It’s going to be too big. The same is probably true of the rest of the numbers I just passed out.
>
> — [[cohn-agile-estimating-planning]], L5363

The cards passed out are 13, 20, 40 and 100 (L5359). This wiki reads the claim as made about this team's scale, since it is relative to the stories estimated so far, and not as a universal ceiling. The choice of ceiling is on [[size-ceiling]], and the timing of the cut on [[when-to-split-a-task]].

## Failure mode: false precision

> Do not, for example, allow one story to be estimated at 66 story points or ideal days and another story to be estimated at 67. That is a false level of precision and we cannot discern a 1.5% difference in size.
>
> — [[cohn-agile-estimating-planning]], L1244

Cohn adds that one-point gaps between 1, 2 and 3 are acceptable because they are much larger as percentages (L1244), so this wiki reads what is forbidden as a small relative difference and not a small absolute one.

**Sign:** an estimate field holds a value off the project's scale, or two estimates differ by a few percent. A sign raises a question, per [[smell-is-not-a-finding]]: it may be a logged duration in the wrong field. The related smell of several scales on one project is on [[montgomery-tracker-smells]].

The case study adds two signs that a field check would miss.

- **In an estimate's history:** a change smaller than the gap between steps. Lowering an 8 to a 7 is refused: "That makes the numbers look too precise. If we want to lower it to a 5, we can. Otherwise, let’s leave it as an 8." (L5471).
- **Across a split:** a piece's estimate adjusted so that the pieces total the original. Three pieces of a 20 came to 21, and the product manager proposed taking a point off (L5407-L5409). The coach refused: "The sum of the estimates doesn’t need to equal the estimate of the larger story." (L5417). The stated reason is that the original was never that exact and that breaking a story up shows more of what is involved (L5411-L5417). The same holds for a split at a period's end, on [[all-or-nothing-counting]].

The rule discards real information, and the chapter accepts that. The programmer's 7 reported a small effect of moving work out of a story (L5469), and the step rule drops it, because the alternative is numbers that imply knowledge nobody has. That reading of the trade-off is this wiki's.

## Whether to include 0

Cohn offers 0 as an option with two reasons (L1234). First, "if we want to keep all features within a 10x range, assigning non-zero values to tiny features will limit the size of largest features". Second, "if the work truly is closer to 0 than 1, the team may not want the completion of the feature to contribute to its velocity calculations": one point earned for trivial work must be repaid next iteration by a velocity drop or by non-trivial work (L1234, L1240).

The case study adds a third reason, that work must be remembered and is still not worth counting, on [[handling-a-sequence-dependency]].

Cohn's cost is that zero is not free in aggregate. Everyone must understand that "13 × 0 ≠ 0" and that "there’s a limit to the number of free lunches they can get in a single iteration" (L1242). He also offers a way out: "An alternative to using 0 is to group very small stories together and estimate them as a single unit." (L1242).

This wiki adds a sign that the source does not state: a period holding many zero-point tasks has work its [[velocity]] does not show. Chapter 6 gives no way to choose between 0 and grouping, so this wiki treats either as a setup choice to hold to.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The project's scale | Project setup |
| The task's size relative to others | [[triangulation]] against estimated tasks |
| How near the task is | Its place in the order, on [[estimating-by-horizon]] |

The source names no test for a bad scale. This wiki's reading is that a scale is wrong when nearly all tasks land on one step, since it then separates nothing, when near-term tasks keep landing above its top, since the ceiling is doing no cutting, or when tasks on one step live for widely different times in board history with no difference in what they contained.

## Agent executor note

This wiki reads "we cannot discern" as a claim about human perception. A model will return 67 as easily as 5 and no source here says it can discern the difference either. The transfer is ours: the rule matters more with an agent estimator, because nothing in the act of producing a number resists false precision, so the plugin restricts its output to the project's steps and does not reconcile a parent with its pieces. A model produces a neat total as readily as a 17. A step's meaning still has to come from tasks on this project, per [[triangulation]].

## Related

The step above which a task is cut is [[size-ceiling]]. What a point means is on [[story-points]]. A missing estimate is judged on [[empty-fields]]. Stating uncertainty in a date is a separate matter, on [[forecast-range-and-probability]].
