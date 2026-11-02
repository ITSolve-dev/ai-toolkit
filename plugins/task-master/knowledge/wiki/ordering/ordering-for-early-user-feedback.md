---
title: Ordering for Early User Feedback
category: ordering
summary: Move forward the features that let real or likely users react, because building the wrong product is the most serious risk and end uncertainty (what to build) is settled only by people who use the result; means uncertainty (how to build it) is settled by trying it in the system, and within one cut the piece whose duration is least known goes ahead of the understood ones once a first slice exists. It applies only if someone can react, and does not mean building the interface alone.
tags: [rule, ordering, prioritization, risk, learning, concept, splitting]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Ordering for Early User Feedback

This rule moves earlier the work that lets users respond to something real. Cohn ([[cohn-agile-estimating-planning]]) calls the risk it answers "the most serious risk facing most projects: the risk of developing the wrong product" (L1855).

## The rule

> This risk can be dramatically reduced by developing early those features that will best allow us to get working software in front of or in the hands of actual users.
>
> — [[cohn-agile-estimating-planning]], L1777

Cohn applies the four [[prioritization-factors]] to user interface work to show it (L1851-L1859).

- **New knowledge:** yes. Building the main components or the navigational model lets the system be shown "to real or likely users in an early form" (L1853), and the reactions become product knowledge.
- **Risk:** it "probably doesn’t eliminate technical risk" unless this kind of interface is new to the team, but it reduces the risk of the wrong product (L1855).
- **Cost:** doing it early is not usually cheaper: "In most cases, this is not the case." (L1857).

So the case rests on learning and risk, not on cost. Cohn's conclusion is to move earlier "those themes that will allow users to provide the most feedback on the usability and functionality of the system" (L1859).

## What it does not mean

> This does not mean that we would work on the user interface in isolation or separate from the functionality that exists beneath the user interface.
>
> — [[cohn-agile-estimating-planning]], L1859

This wiki reads this as the same requirement as a [[vertical-slice]]: what is shown must work. A separate interface task with nothing behind it fails the rule, and the sign is a task that delivers screens and no behaviour ([[component-task-masquerading]]).

## Two positions and when each holds

Cohn sets out a disagreement: common advice does interface design entirely within the iteration of the underlying feature, while others argue that usability improves if designers consider the whole interface upfront (L1851). He resolves it by moving forward the features that carry significant interface and gain the most feedback. He does not choose whole-interface design as a task of its own.

This wiki's reading by setting is as follows. If a person or group can react soon, follow the rule above. If the overall structure of the interface is itself the open question, the first feature shown should be the one that exercises that structure, which is what Cohn means by "the navigational model" (L1853).

## Sign

The signs are this wiki's, and each raises a question. A long run of history in which every finished task is internal and nothing was presented to anyone. Or a project whose open questions about what to build stay open while the tasks that could settle them sit low.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Who can react to the result, and how soon | The person steering |
| Which open questions are about what to build | *End and Means Uncertainty* (below), the tasks' open questions |
| Which item would expose the most to reaction | The tasks' descriptions of what users see |

The move was wrong if the result was shown and nothing changed afterwards: no new, changed or dropped tasks came of it. The test is this wiki's. It means either that the uncertainty was smaller than assumed or that the wrong people saw it.

## Conditions and cost

This wiki notes that the rule requires someone who can react. Where no user is reachable, the feedback does not arrive, and the early move buys nothing this source can name. With a few people, the only reader may be the person steering, whose reaction tests the result less well than a user's would. Early user-facing work may also be redone as reactions come in, and that rework is the price of the knowledge ([[cost-now-versus-cost-later]]).

## Agent executor note

This wiki reads the rule as surviving whole, because the uncertainty lives with users and not with the executor (*End and Means Uncertainty* (below)). It may matter more with an agent, since this wiki expects an agent to build the wrong thing as readily as the right one. That expectation is ours and the source does not test it. See also [[replanning-on-new-knowledge]].

## End and Means Uncertainty

This distinction separates two kinds of ignorance at the start of a project. Cohn ([[cohn-agile-estimating-planning]]) takes the terms from Laufer (1996) and pairs them with the two kinds of knowledge a team builds up (L1748-L1758). The rule that iteration reduces both is on [[replanning-on-new-knowledge]]; this section names the two and says what ordering does with them.

### The two kinds

| | Knowledge | Question | Uncertainty removed |
|---|---|---|---|
| Product | "knowledge about _what_ will be developed" (L1754) | What features go in, and which stay out | End uncertainty |
| Project | "knowledge about how the product will be created" (L1756) | Technologies, the developers' skills, how well the team works together | Means uncertainty |

Cohn's premise is that "The flip side of acquiring knowledge is reducing uncertainty." (L1758). This wiki reads the "new knowledge" among the [[prioritization-factors]] accordingly: it is not a separate benefit but uncertainty being removed, which is why that factor sits close to risk (L1781).

### Two views of removing it

Cohn contrasts them in a figure (L1775; his text at L1762-L1777 calls it Figure 8.1, while the caption says 9.1).

- **Waterfall** tries to eliminate end uncertainty before work begins, then reduces means uncertainty as work proceeds. Cohn calls complete upfront elimination "unachievable" (L1762).
- **Agile** reduces both at once, by building parts, showing them, collecting feedback and adjusting the plan (L1764-L1768).

His agile curve is deliberately not a straight line. It favours reducing end uncertainty early:

> End uncertainty does not need to be eliminated at the outset (as hoped for in the traditional view) and it cannot be. However, one of the greatest risks to most projects is the risk of building the wrong product.
>
> — [[cohn-agile-estimating-planning]], L1777

The rule he draws from this is the one at the top of this page.

### How the plugin uses it

This use is this wiki's. Asked why an item should come early for its knowledge, the plugin first asks which kind is meant, because each has a different owner and test. End uncertainty is settled by people who will use the result, and means uncertainty by trying the thing in the system. Unknown ends are a task-content problem first ([[underspecified-task]]), and one question to the requester may settle them more cheaply than building. Unknown means are a matter of cutting ([[choosing-between-splits]], [[spike-as-last-resort]]).

### Agent executor note

The charter asks what survives, and the answer differs by kind. The transfer here is ours.

- **End uncertainty survives whole.** It lives with users and does not depend on who builds.
- **Means uncertainty survives in part.** Knowledge about the technology in this system still has to be gained. Knowledge about "the skills of the developers" and "how well the team functions together" (L1756) is about people, and it does not transfer to an agent.
- **What is learned does not keep itself.** On Cohn's team, project knowledge stays in the people. With an agent it stays only if written where the next task can read it ([[conversation-moves-into-the-task]]). So an item moved forward for means knowledge has paid off only if its finding was recorded.

## Uncertain Piece Goes Earlier

When a task is cut, the order of its pieces is a separate decision. In Cohn's search screen example, the order was set by uncertainty and not by what a user would want next:

> These iterations were prioritized this way because there was a lot of uncertainty about how long it would take to develop the data display grid. Removing that uncertainty in the second iteration was deemed better than leaving it until the third.
>
> — [[cohn-agile-estimating-planning]], L2629

Cohn gives the piece left for last as the one the team understood: "Since the team had already achieved a solid understanding of what was necessary to create the query builder, they considered that work to be low risk." (L2629).

This is a single example, and Cohn draws no guideline from it: the guideline at the end of that passage concerns cutting by operations (L2631). The rule below is this wiki's generalization. It agrees with "most risky" in the Complicated row of [[how-far-to-split-up-front]], and it reads the grid's uncertainty as uncertainty about means (*End and Means Uncertainty* (above)).

### The rule

Among the pieces of one cut, once a first [[vertical-slice]] exists, place the piece with the least known duration ahead of the pieces that are understood.

The first clause comes from the order Cohn actually used: the grid was the second piece and not the first, and a first iteration with a working query path came before it (L2627). The grid's uncertainty was about how long it would take. This wiki reads uncertainty about what the work is as a different matter, which goes to [[spike-as-last-resort]] or [[choosing-between-splits]].

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Uncertainty of each piece | The estimator's statement; whether similar work was finished before, from board history |
| Dependencies among the pieces | The cut itself, per [[sequence-versus-wait]] |
| Value of each piece | The purpose in the request, or the person steering |

The order was wrong if the piece marked uncertain took about what was expected, while a piece left for later because it was understood took much longer. It was also wrong if a valuable piece slipped past a date to make room for an uncertain one that could have waited. Both tests are this wiki's.

### Trade-off

The order can delay what is most useful. In this example the remaining search fields waited a further iteration. Cost of delay can outweigh the uncertainty, and [[ordering-by-value-and-urgency]] decides that comparison. This wiki reads the rule as a tie-breaker inside one cut and not as a general order for the board.

### Agent executor note

The example is a human team's judgement with no measurement. This wiki reads the reasoning as surviving an agent executing, since a late surprise costs the plan whoever does the work. What changes is the source of the uncertainty: a human team's unknowns are not necessarily an agent's, so "the team had already achieved a solid understanding" (L2629) cannot be carried across and has to be read from the project's own finished work.
