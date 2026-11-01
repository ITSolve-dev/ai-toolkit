---
title: Empty Fields
category: task-content
summary: An empty field is a failure only at the stage where the workflow reads it, and only for fields something depends on; practitioners split on missing properties for exactly these reasons, and a filled field does not prove a real value.
tags: [decision-rule, task-content, audit, evidence]
sources: [montgomery-tracker-smells, kubernetes-issue-triage]
created: 2026-11-01
updated: 2026-11-01
---

# Empty Fields

A board audit can flag every blank in a tracker, and most of those flags would be wrong. This rule decides when an empty field counts. The study behind [[montgomery-tracker-smells]] lists "Properties such as assignee, priority, or severity are left blank on issues." (L152) as a smell, and nine of the 15 participants who answered disagreed or said it depends (L518). Two reasons recur, and both can be applied to a board.

The first is the stage. Fields are filled when the workflow reaches them, and P01's note says "no assignee while the ticket is in progress would be considered bad" (L518). The Kubernetes guide treats an empty field as a state: "If an issue lacks a `priority` label, this means it has not been reviewed and prioritized yet." ([[kubernetes-issue-triage]] L226).

The second is the field. P26 said they "differentiate important vs non-important properties", and P05 spoke of "properties nobody cares about that are often missing" (L518).

## The rule

An empty field is a failure when both of these hold.

1. The task has passed the stage at which the project's workflow needs that field.
2. Something depends on the field: a decision, a rule on this board, or a person who reads it.

Any other empty field is not reported. This is this wiki's statement of the two context factors, "workflow stage" and "issue property" (L564-L565). The study does not state a rule.

Examples for a project of this kind. An unrated item before triage is fine ([[triage-procedure]]), and an unrated item that is about to start is not ([[ordering-by-value-and-urgency]]). A missing estimate is fine until something reads it. In the study, 2 of 8 disagreed on missing estimates (L554): P12's team does not estimate at all, because of a very complex code base, and P15 said it depends on the sector. So a project with no size ceiling has no failure there ([[size-ceiling]]).

## How this fits the charter

The charter says a rule about task content can use an omission as its sign, and pages such as [[testable-acceptance]] and [[task-must-justify-itself]] refuse a merely empty field. This page is consistent with both. It gives the condition under which the omission counts, and it treats the field as only one place for a fact. The test for the fact itself is on [[recoverable-versus-task-only-facts]].

## A filled field proves little

The reverse also needs saying. Forcing a field does not give a real value. The authors report that "Users may be unsure about how to fill in certain fields, so they revert to skipping the field or filling in incorrect information." (L442). Fields can also be required before anyone knows the answer, "when the required information is not known at the issue creation time" (L427). And participants also described the opposite trouble, a lack of enforcement that lets a field be misused (L429).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Which field is empty | Board state |
| The task's stage | Board state |
| Where the workflow needs the field | Project configuration |
| Whether anything reads the field | This wiki's rules for the setup ([[board-rules-by-setup]]), and project configuration |

Not reporting was wrong if a decision later went badly for want of that field. Reporting was wrong if the people steering dismiss it as not needed at that stage. These tests are this wiki's.

## What the study does not establish

It gives no list of fields that matter. That depends on the project, by its own account. All of this is what practitioners said, in mostly large companies, and no field's emptiness was measured against an outcome ([[montgomery-tracker-smells]]).

## Agent executor note

Stage and dependence do not depend on the executor, so the rule survives. Which fields matter does change. An assignee field matters to people dividing work and very little to an agent, while the fields an agent acts on are the ones in its brief. The participants' reasons for leaving a field empty, friction and uncertainty when typing, do not apply to a plugin. Its failure runs the other way: it can fill every field with a plausible value, so a filled field written by the plugin should not count as confirmation.
