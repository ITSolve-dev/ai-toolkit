---
title: Predictability
category: reading-history
summary: How accurately a process answers "When will it be done?"; Vacanti scores it by that accuracy and not by adherence to a practice, widens it to a system behaving as expected, and treats it as the result of policies a project sets, written or not.
tags: [concept, predictability, retrospective-analysis, flow]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Predictability

In Vacanti's usage, predictability is how accurately a process answers one question. He calls “When will it be done?” the first thing customers ask and, "for the most part, it is the only thing they are interested in until you deliver" ([[vacanti-actionable-agile-metrics]] L384-L386).

> Whether your process is predictable or not is judged by the accuracy of your answer.
>
> — [[vacanti-actionable-agile-metrics]], L394

This wiki reads that as a definition that can be scored: compare the answer given with when the item finished. It follows that a project which never records its answers has nothing to score. [[stating-plan-uncertainty]] covers what a stated answer has to carry so that it can be compared afterwards.

## What it is not

**It is not adherence to a practice.** The source's case is Bennet Vallet, who ran mature Agile teams following established practice: "In his mind he was doing everything right, so he reasonably believed that predictability would inevitably follow. Yet he constantly struggled to accurately answer the most important questions that his customers were asking." (L398). This wiki reads that as agreeing with [[plan-conformance-as-success]]: following the procedure and getting the outcome are separate facts, and only the second is scored.

**It is not a standing property.** Vallet's remark is that predictability is a verb and not a noun, and the author extends it: "It is that you “do” predictability. Predictability is proactive and not reactive." (L524). The practical content is in the next sentence: "The actions you take today have the biggest impact on your predictability tomorrow." (L524). This wiki reads that as saying a forecast depends on what the project does after giving it, such as starting more work.

**It is not only a forecast.** Chapter 3 widens the Chapter 1 definition: "The bigger part of predictability is operating a system that behaves in a way that we expect it to." (L1100). The author says a process that conforms, or mostly conforms, to the assumptions of [[littles-law]] gives data that can be trusted, and is then "probabilistically predictable" (L1088-L1094). This wiki reads the two definitions as complementary: an answer can be scored only after the fact, while conformance can be checked during the work ([[littles-law-assumptions]]).

## What produces it

The source places the cause in policy and not in circumstance:

> Amongst other things you start new work at a faster rate than you finish old work, you work on too many items at the same time, you ignore systemic dependencies and impediments, and you expedite requests that do not need to be expedited.
>
> — [[vacanti-actionable-agile-metrics]], L232

The author says these policies exist "Whether explicit or not" (L232). This wiki reads that as an instruction for review: the policy in force is the one board history shows, which can differ from the one the project declared. [[signs-of-poor-flow]] gives the reading, and [[process-policies-from-littles-law]] gives the policies stated positively.

The author also describes a loop: the metrics "will immediately reflect policies you have in place", that data suggests a policy change, and the change appears in the next data (L242). The mechanism is observable, but this part of the book reports no worked instance of it.

## Cost

The author names the cost directly. "It will mean saying no to customer requests to start new work immediately. It will mean placing much less emphasis on upfront estimation and planning." (L234).

## Accuracy against usefulness

Vacanti's test scores the answer. [[good-plan-test]] records Cohn's opposite emphasis, that a plan is good if stakeholders find it "sufficiently reliable that they can use it as the basis for making decisions" ([[cohn-agile-estimating-planning]] L469), so a plan can be wrong and still good.

The resolution is this wiki's, and it turns on what is being scored. Vacanti asks the reader to count "how many times you have been wrong" (L394), which scores a process across its answers, so one miss says little. Cohn scores one plan against the decisions it fed, so one miss matters only through those decisions. Read a single plan with [[good-plan-test]], and read a run of answers here. An answer given as a probability is scored the way [[service-level-expectation]] scores an SLE: by the share of items that finished within the stated time.

## Against estimation

The source's strongest claim is conditional: "If you can get to a process that has stable, predictable flow, then the act of estimating and planning—the act of making predictions—becomes trivial." (L522). The condition carries the claim. A project with no history, or with unstable flow, gets nothing from it.

This disagrees with the estimating position elsewhere in this base, and the resolution is this wiki's. The sentence is about estimates used as predictions. Estimating also finds unknowns ([[unknowns-surfaced-by-estimating]]) and gives a size at which a task is cut ([[size-ceiling]]), and stable flow replaces neither. So under a stable flow, stop producing a date by adding up estimates and keep the sizing where the project uses it. Without stable flow, the route from size to date on [[size-versus-duration]] stands unchanged. Which unit the answer is stated in is on [[points-or-time-and-count]].

## Agent executor note

The definition does not depend on the executor: the answer and the finish can be compared under any arrangement. The policies listed are set by whoever decides what starts, which here means the people steering, so they survive too. Whether an agent's run durations are stable enough for the conditional claim above to apply is not shown by this source, whose setting is human teams at Siemens Health Services. This wiki treats that as open.
