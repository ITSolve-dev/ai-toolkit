---
title: Risk-Value Quadrants
category: ordering
summary: Sort features by risk and value into four quadrants; high-value high-risk first, high-value low-risk second, low-value low-risk last, and low-value high-risk avoided; value decides, risk breaks the tie, and positions change over time.
tags: [decision-rule, ordering, prioritization, risk]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Risk-Value Quadrants

This rule settles the "classic struggle" (L1791) between building what could derail a project and building what pays soonest. Cohn ([[cohn-agile-estimating-planning]]) refuses both extremes: "The solution, of course, is to give neither risk nor value total supremacy when prioritizing." (L1795).

## What counts as a risk

Cohn defines a risk as "anything that has not yet happened but might and that would jeopardize or limit the success of the project" (L1781). He lists schedule risk, cost risk and functionality risk, and also divides risks into technological and business (L1783-L1791). His signs of a high-risk feature are reliance on "unproven technologies, integration with unproven sub-contractors, technical innovation (such as the development of a new algorithm)" (L1795).

## The sequence

| Value | Risk | Cohn's label | Why |
|---|---|---|---|
| High | High | Do first | "These features deliver the most value and working on them eliminates significant risks." (L1806) |
| High | Low | Do second | Equal value and less risk, so they "can therefore be done later in the schedule" (L1806) |
| Low | Low | Do last | "they will have less impact on the total value of the product if they are dropped and because they are low risk" (L1815) |
| Low | High | Avoid | "There is no reason to take on a high degree of risk for a feature of limited value." (L1817) |

The quadrant labels are from Figure 9.3 (L1811). The rule in a sentence is his: "use the guideline to work first on high-value features but use risk as a tie-breaker." (L1806).

This wiki notes what the table implies. Value is the primary sort and risk only separates items within a value band. Risk is not a reason to raise a low-value item, and its direction flips with value: it pulls a high-value item forward and pushes a low-value one out. Cohn's instruction for the last row is "Try to defer low-value, high-risk items right out of the project." (L1817). The test for the middling case is on [[combining-prioritization-factors]].

## Positions change

"Be aware that a feature’s risk and value profile changes over time." (L1817). Cohn's example has a slip: he places a low-value, low-risk feature in the Avoid quadrant, which Figure 9.3 gives to low-value, high-risk items (L1811, L1817). This wiki reads the point as surviving the slip: a feature set aside today can become the next thing to do once everything above it is finished. So a rating expires, as a [[cost-of-delay]] rating does.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Value band | The person steering, or [[ordering-by-value-and-urgency]] |
| Named risk: what might happen and what it would stop | The task's text, the design it came from, or the person steering |
| Whether doing the work settles the risk | The task: does it exercise the unproven thing? |
| Date of the rating | Board history |

This wiki adds that a risk band needs a named event, because a bare sense that something is hard gives nothing to check later. The tests below are this wiki's, since the source states none.

- **Risk was overrated** if a high-risk item finished with no surprises and nothing that depended on the outcome changed.
- **Risk was underrated** if a low-risk item stalled, or changed the plan for other work.
- **Avoid was wrong** if a deferred item proved necessary and its risk arrived late in the work.

## Cost

Doing high-risk work first means accepting what Cohn says of a risk-driven team: "work they perform will turn out to be unneeded or of low value" (L1793). This wiki notes that restricting that to high-value items reduces the exposure and does not remove it, since the value rating may itself be wrong. The ordering also leaves the easy, high-value wins until second, so visible progress can come later.

## Agent executor note

This wiki reads the rule as concerning results, so it survives. What changes is the reading of risk. This wiki reads "unproven technologies" (L1795) in Cohn's setting as partly meaning unproven for these people. With an agent, this wiki reads the question as whether the thing has been shown to work in this system, not whether anyone present has done it before. That transfer is ours, and the source does not test it.
