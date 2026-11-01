---
title: End and Means Uncertainty
category: ordering
summary: What is unknown about a product divides into what to build (end) and how to build it (means); doing the work reduces both, and Cohn favours reducing end uncertainty early, since building the wrong product is among the largest risks.
tags: [concept, ordering, prioritization, learning, risk]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# End and Means Uncertainty

This distinction separates two kinds of ignorance at the start of a project. Cohn ([[cohn-agile-estimating-planning]]) takes the terms from Laufer (1996) and pairs them with the two kinds of knowledge a team builds up (L1748-L1758). The rule that iteration reduces both is on [[iterating-reduces-uncertainty]]; this page names the two and says what ordering does with them.

## The two kinds

| | Knowledge | Question | Uncertainty removed |
|---|---|---|---|
| Product | "knowledge about _what_ will be developed" (L1754) | What features go in, and which stay out | End uncertainty |
| Project | "knowledge about how the product will be created" (L1756) | Technologies, the developers' skills, how well the team works together | Means uncertainty |

Cohn's premise is that "The flip side of acquiring knowledge is reducing uncertainty." (L1758). This wiki reads the "new knowledge" among the [[prioritization-factors]] accordingly: it is not a separate benefit but uncertainty being removed, which is why that factor sits close to risk (L1781).

## Two views of removing it

Cohn contrasts them in a figure (L1775; his text at L1762-L1777 calls it Figure 8.1, while the caption says 9.1).

- **Waterfall** tries to eliminate end uncertainty before work begins, then reduces means uncertainty as work proceeds. Cohn calls complete upfront elimination "unachievable" (L1762).
- **Agile** reduces both at once, by building parts, showing them, collecting feedback and adjusting the plan (L1764-L1768).

His agile curve is deliberately not a straight line. It favours reducing end uncertainty early:

> End uncertainty does not need to be eliminated at the outset (as hoped for in the traditional view) and it cannot be. However, one of the greatest risks to most projects is the risk of building the wrong product.
>
> — [[cohn-agile-estimating-planning]], L1777

The rule he draws from this is [[ordering-for-early-user-feedback]].

## How the plugin uses it

This use is this wiki's. Asked why an item should come early for its knowledge, the plugin first asks which kind is meant, because each has a different owner and test. End uncertainty is settled by people who will use the result, and means uncertainty by trying the thing in the system. Unknown ends are a task-content problem first ([[underspecified-task]]), and one question to the requester may settle them more cheaply than building. Unknown means are a matter of cutting ([[find-core-complexity]], [[spike-as-last-resort]]).

## Agent executor note

The charter asks what survives, and the answer differs by kind. The transfer here is ours.

- **End uncertainty survives whole.** It lives with users and does not depend on who builds.
- **Means uncertainty survives in part.** Knowledge about the technology in this system still has to be gained. Knowledge about "the skills of the developers" and "how well the team functions together" (L1756) is about people, and it does not transfer to an agent.
- **What is learned does not keep itself.** On Cohn's team, project knowledge stays in the people. With an agent it stays only if written where the next task can read it ([[fact-stranded-outside-the-task]]). So an item moved forward for means knowledge has paid off only if its finding was recorded.
