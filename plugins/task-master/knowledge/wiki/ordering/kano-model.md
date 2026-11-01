---
title: Kano Model
category: ordering
summary: Kano's model sorts features by how satisfaction responds to them; threshold features only prevent dissatisfaction, linear features pay in proportion, and exciters please when present and cost nothing when absent. It yields a category and not an order, a linear feature can carry a mandatory floor, one importance scale cannot see the reaction to absence, and categories decay over time.
tags: [concept, ordering, prioritization, value, kano]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Kano Model

The Kano model sorts the features of a product by how customer satisfaction responds to them. It originates with Noriaki Kano (1984), and Cohn uses it to decide "how to prioritize work for a new product release" ([[cohn-agile-estimating-planning]] L2384). The model says what kind of thing a feature is. The order that follows is on [[ordering-by-kano-category]], and the way to measure a category instead of guessing it is on [[kano-questionnaire]].

## The three categories

| Category | Other names | When present | When absent | Line |
|---|---|---|---|---|
| Threshold | Must-have, basic | Adds little: "Improving the performance or amount of a threshold feature will have little impact on customer satisfaction." | The feature "must be present in the product for it to be successful" | L2392 |
| Linear | Performance, one-dimensional | "customer satisfaction is correlated linearly with the quantity of the feature" | Less of it, less satisfaction | L2394 |
| Exciter | Delighter, unknown need | Great satisfaction, and even a partial implementation raises it sharply | "the lack of an exciter or delighter will not decrease customer satisfaction below neutral" | L2396, L2400 |

Two further limits come with these. For a threshold feature, "no matter how much of a must-have feature is added, customer satisfaction never rises above the mid-point." (L2398). For a linear feature, "product price is often related to linear attributes" (L2394). Exciters are called unknown needs because "customers or users do not know they need these features until they see them" (L2396). This wiki reads that as the reason a request rarely names one.

## What separates them

This wiki reads the three categories as one discriminating test: an asymmetry between presence and absence.

- Absence hurts and presence does not help: threshold.
- Presence helps and absence does not hurt: exciter.
- Both directions move satisfaction: linear.

The consequence is that a single rating of value cannot separate a threshold feature from an exciter, since both can be called valuable and they call for opposite handling. The fictional case study in Chapter 23 (L4961) states the mechanism when a product manager asks why a 1-to-5 importance rating would not do:

> A single scale like that just tells us how strongly a user values a feature. It doesn’t tell us how strongly the user would react to the absence of the feature. I wouldn’t prioritize wheels very highly if you asked me about features on a car but I’d be mad if you took them away.
>
> — [[cohn-agile-estimating-planning]], L5634-L5638

This wiki reads that as saying importance and reaction to absence are two different measurements, and a feature can be low on one and high on the other. That is the reason [[relative-penalty]] scores absence separately, and why the Killer band of [[ordering-by-value-and-urgency]] names both what doing a thing gains and what not doing it loses.

## The categories in the case study

The chapter uses the model without naming it and points to Chapter 11 for the method (L5943). Its names are mandatory, linear and exciter, and it adds what the table above leaves out. The speakers are characters.

**Mandatory is the cost of entry.** Some features are so obvious that the analyst does not ask about them: "Supporting them is really the cost of entry." (L5992).

**Linear does not mean optional.** An artist objects that art cannot be optional, and the analyst separates a floor from a slope: "I didn’t say these are optional, Rose," then "There is a certain baseline we can’t fall below" and "These are linear because the more of them the better." (L6050). This wiki reads that as the discriminating criterion: a linear feature can carry a mandatory minimum, so the category does not license dropping it whole.

**Few exciters is an unfinished search.** "Remember that exciters are unexpected features." and "Every product should have at least one or two exciters" (L5984). A survey showing few of them is read as a reason for open-ended interviews, and not as a dull product (L5984). This wiki reads that as following from an exciter being an unknown need: a list built from what is already asked for has little chance of holding one.

**Indifferent is a fourth outcome.** "it just means that the person didn’t have a strong preference either way" (L5972). What the chapter does with such features is on [[ordering-by-kano-category]].

## Categories decay

> Keep in mind that features tend to migrate down the Kano diagram over time. A short time ago, wireless Internet access in a hotel room was a delighter. Now it’s a linear feature well on its way to becoming a threshold feature.
>
> — [[cohn-agile-estimating-planning]], L2419

This wiki reads that as saying a category carries a date, like any rating ([[ordering-by-value-and-urgency]], step 5). The direction runs one way in the source's example: exciter, then linear, then threshold. This wiki takes the observable sign to be users beginning to object to the absence of something recorded as an exciter. A category kept from an earlier release should be asked again before it decides anything, and the source gives no figure for how fast this happens.

## What the model is applied to

The source classifies features and themes ([[theme]], L2423), and all its examples are things a user meets in the product. This wiki's reading is that a technical task has no category of its own. It takes the category of the theme it serves, through its stated purpose ([[task-must-justify-itself]]). A task that serves no theme cannot be classified, and goes to [[incomparable-tasks]].

A category also belongs to a population and not to the feature alone: this wiki reads the two-peak rows on [[kano-questionnaire]] as meaning the same feature can be a must-have for one group of users and an exciter for another.

## Setting

The source's setting is a product with customers, a market and releases, and the example is a website with prospective users. A project with no users outside the people steering it has no satisfaction curve to read, so the model tells it little. That limit is this wiki's.

## Agent executor note

The model concerns the reaction of users, not the executor, so it survives an agent executing. A category is a task-only fact in the sense of [[recoverable-versus-task-only-facts]]: the repository cannot show how users would feel. The plugin can propose a category and a person confirms it.
