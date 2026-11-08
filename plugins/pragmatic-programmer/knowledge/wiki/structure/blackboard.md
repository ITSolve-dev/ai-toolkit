---
title: Blackboard
category: structure
summary: "A coordinator with branches over which inputs have arrived so far, such as `if a and b and not c`, holding the handling of every input and rule in one function: facts arrive in any order and the sequence is hard-coded anyway."
tags: [rule, concurrency, coordination, decoupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A blackboard is a shared place where independent contributors post facts and watch for facts, with no knowledge of each other. The book calls it a form of passive concurrency, in which the contributors are independent processes, agents or actors. Some post facts, others take them, combine or process them, and post further results (p. 234).

## Rule

The book's tip is to use blackboards to coordinate workflow: «Пользуйтесь классными досками для координации потока выполнения» (p. 236). Its detective analogy gives the properties: no contributor needs to know the others exist; contributors can differ in training and experience; they can come and go; and nothing restricts what goes on the board (p. 234).

The book's case is loan processing. Answers can arrive in any order, gathered by different people in different places or by other systems; some can only start once others are confirmed; and a new fact can raise new questions and rules (pp. 235-236). A workflow system would have to enumerate every combination, and when regulations or procedures change the hard-coded logic may need rewriting (p. 236). With a blackboard and a rules engine encapsulating the legal requirements, «Порядок поступления данных не имеет особого значения» (p. 236): a posted fact triggers the matching rules, and their results go back on the board, triggering others (p. 236).

## Sign in code

These shapes are this wiki's own.

- A coordinator function with branches over which inputs have arrived so far, such as `if a and b and not c`.
- One central function holds the branches for every input and rule.

This wiki assigns the neighbouring case as follows. A record of nullable fields and status flags whose own methods test them in combination is [[replace-flags-with-explicit-states]]; one tested by functions outside its owner is [[status-variable-as-enumeration]]; one whose inputs can arrive in any order, or where a fact raises new work, is [[blackboard]].

## When not to apply

- The order is fixed and the inputs are few. This wiki would then keep a plain sequence.
- All inputs are needed and nothing new arises from them. This wiki would then use a join that waits for all of them; a board earns its place when facts generate more work.
- This wiki adds that a board is itself shared state. It stays safe only if contributors add facts rather than edit them, and reach it only through its own API. See [[shared-state-is-incorrect-state]].
- This page covers coordination inside one application. Contributors that are separate systems, as in the book's loan case, fall under system architecture and outside this wiki's scope.

## Repair

The outline is the book's (p. 236); the steps are this wiki's own wording.

1. Turn each input into a named fact that any source can post, in any order.
2. Turn each branch of the coordinator into a rule stating which facts it needs.
3. Have rules post their outcomes as facts, so that follow-up rules fire without being called.
4. Delete the coordinator and the per-input flags.

## Trade-offs

- The cost is the same as for actors: the approach is harder to reason about because it works mostly indirectly (p. 236). The book asks for good tooling to follow messages and facts through the system, see [[trace-id-across-messages]], and suggests a central repository of message formats and APIs, especially if it can generate code and documentation (pp. 236-237).
- The book notes that the original systems found little use, in its view partly because the need for that kind of concurrent collaborative processing never developed (p. 235).

## Before and after

```
function on_answer(claim, kind, value):
    claim[kind] = value
    if claim.identity and claim.police_report and not claim.reviewed:
        if claim.police_report.disputed:
            request_statement(claim)
        claim.reviewed = true
    if claim.identity and claim.estimate and claim.policy:
        start_payment(claim)
```

```
board.when(["identity", "police_report"], review_report)
board.when(["identity", "estimate", "policy"], start_payment)

function review_report(facts):
    if facts.police_report.disputed:
        board.post("statement_needed", facts.identity)

// any source, any order
board.post("police_report", report)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: properties, p. 234; history, pp. 234-235; the loan case and the tip, pp. 235-236; the costs, pp. 236-237.

This wiki's own: `## Sign in code`, the limits it marks as its own, the limit to one application, and the worded steps. The insurance example and the pseudocode are this wiki's own. Related: [[actor-model]], [[temporal-coupling]], [[observer-vs-publish-subscribe]].
