---
title: Business rules are metadata
category: structure
summary: "The same condition naming concrete roles, departments or limits repeats at two or more sites: the policy is hard-coded instead of held as data read by one mechanism."
tags: [rule, policy, duplication, configuration]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A business rule says who may do what, and under which limit, today. *The Pragmatic Programmer* separates such a rule from the requirement that carries it: the requirement describes a general capability, and the current rule is one value of that capability. Code that hard-codes the value has to be edited whenever the value moves.

## Rule

Thomas and Hunt take a statement that only direct managers and HR staff may view an employee's record (p. 302). Read as the requirement, it leads a developer to code and check that condition explicitly at every data access. Restated as: records may be accessed only by authorised users, it leads to an access-control system whose metadata holds the current rule. The authors then state the consequence: «И если бизнес-правила изменятся (а это неизбежно), то обновить придется только метаданные такой системы.» (p. 302).

Their general form is that business rules are metadata: «Реализуйте общий случай, приняв во внимание сведения о бизнес-правилах в качестве примера того, что должно поддерживаться в системе.» (p. 302).

The book separates the two in its passage on over-specification: a requirement must «зафиксировать исходные семантические инварианты и задокументировать конкретные или текущие нормы практики выполнения работ в виде набора правил» (p. 305). This wiki reads that as the line between the two: an invariant stays in the code, a current practice goes into the rule set. The same line runs through [[semantic-invariant]].

## Sign in code

The source gives a wording test, not a sign in code. The signs below are this wiki's own.

- One condition naming concrete parties or limits (role names, department names, plan names, amounts) appears at two or more sites.
- A diff that adds one role or tier edits the same list of literals in several functions.

The first sign alone is duplication, which step 2 of the repair removes. The second shows the rule varying, and only that justifies moving it into data.

A condition at a single site is not a sign. Calling it a violation would need knowledge that the rule varies, and the code in hand does not show that.

This wiki assigns the neighbouring cases as follows. A branch on an environment or a customer name is [[parameterize-with-external-configuration]]. Any other repeated check is [[dry]].

## When not to apply

The source states no limit and calls change of such rules inevitable (p. 302). The limits here are this wiki's own.

- The condition sits at one site and nothing in front of the reader shows it varying. A mechanism serving one rule is abstraction that does not pay for itself; a named function is enough. See [[know-when-to-stop]].
- The condition is a semantic invariant, not a current practice. A date range whose start precedes its end is a fact about the data, and moving it into configuration lets someone switch off what keeps the data meaningful. See [[semantic-invariant]] and [[design-by-contract]].
- The rule cannot be expressed as data without inventing a small language. Metadata then becomes a program with no types, tests or debugger, which costs more than the code it replaced. See [[over-configuration]].

## Repair

1. Name the decision and give it one function, such as `allows(actor, action, subject)`.
2. Replace every inline copy of the condition with a call to it. This step alone removes the duplication; stop here if nothing shows the rule varying.
3. Move the concrete parties and limits out of the function into data that it reads.
4. Test the mechanism with sample rules, and check the shipped rule set separately, because a compiler no longer checks it.

The trade-off, which is this wiki's own statement: the rule is no longer readable at the call site, and an error in the data fails at run time. The rule data therefore needs review and tests like code.

## Before and after

Before:

```
function approve_refund(actor, refund):
    if actor.role == "supervisor" or actor.department == "finance":
        mark_approved(refund)
    else:
        deny()

function cancel_refund(actor, refund):
    if actor.role == "supervisor" or actor.department == "finance":
        mark_cancelled(refund)
    else:
        deny()
```

After step 2, which removes the duplication:

```
function may_manage_refunds(actor):
    return actor.role == "supervisor" or actor.department == "finance"

function approve_refund(actor, refund):
    require(may_manage_refunds(actor))
    mark_approved(refund)

function cancel_refund(actor, refund):
    require(may_manage_refunds(actor))
    mark_cancelled(refund)
```

After step 3, once a diff shows the parties changing:

```
policy = load("refund-policy")   // data: which parties may take which action

function approve_refund(actor, refund):
    require(policy.allows(actor, "refund.approve", refund))
    mark_approved(refund)

function cancel_refund(actor, refund):
    require(policy.allows(actor, "refund.cancel", refund))
    mark_cancelled(refund)
```

## Source

[[pragmatic-programmer]]: Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, p. 302 (requirement versus rule, the access-control example, the general statement) and p. 305 (invariants versus current practice).

This wiki's own: all of `## Sign in code`, all of `## When not to apply`, the numbered repair and its trade-off, the reading of invariant versus practice as the discriminating line, and the pseudocode. The authors' example is a wording exercise on a requirement; moving it onto code that already exists is our transfer.
