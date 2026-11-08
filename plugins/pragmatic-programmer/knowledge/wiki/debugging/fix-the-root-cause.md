---
title: Fix the root cause, not the symptom
category: debugging
summary: "A guard, clamp, default or catch is added at the line where a failure surfaced, or a branch keyed on one input value (a client id, a magic argument) overwrites a computed result, while the code that produces the bad value stays unchanged."
tags: [rule, debugging, root-cause, special-case]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

The place where a failure shows and the place where it is caused are often different. A patch at the first place removes the evidence and leaves the defect.

## Rule

The book warns against short-sightedness in debugging and against the urge to fix only the visible symptom, since the real fault may be several steps away from what you observe and may be tied to other faults (p. 126). «Старайтесь всегда обнаружить корневую причину возникшего затруднения, а не только его конкретное внешнее проявление» (p. 126). Its illustration is a wrong value: finding that `interest_rate` holds 4.5 instead of 0.045 is the start, and the work is finding why it became wrong (p. 128).

*Code Complete* states the same rule and aims it at one shape, the special case written for the input on which the bug was seen. Fix the problem, not its symptoms: symptoms must go too, but the main aim is to remove the cause, and without understanding the problem fully a change removes symptoms and makes the code worse (p. 540). McConnell's two illustrations: after `x = Compute(y)`, an `if (y = 17)` that sets x to a constant because Compute fails for 17 (p. 528); and a summing loop followed by `if (client == 45) sum[45] += 3.45`, then `else if (client == 37 && numClaims == 0) sum[37] = 0.0` (pp. 540-541). He gives three reasons (pp. 541-542): such fixes mostly will not work, because the problems look very much like initialisation defects, which are unpredictable by definition, so a sum off by 3.45 today may be off by 10,000.02 tomorrow, or be right (p. 541); the code becomes hard to maintain, since «Если для исправления ошибок создаются частные случаи, они становятся самой заметной особенностью кода» (p. 541), and new special cases pile up while old ones are never removed; and faking data in code is a job better done by hand on the printout.

## Sign in code

- A diff adds a null check, range clamp, fallback default, `catch` or retry at the failing line, and does not touch the function that produced the value.
- A comment beside a guard says it was added after a report, with no statement of where the bad value comes from.
- After a computation, a fix adds one branch that compares an input to a literal identifying one case (an id, a record number, one argument value) and overwrites or adjusts the result with another literal, with no rule connecting the two. This sign is this wiki's statement of *Code Complete*'s examples (pp. 528, 540-541); the book's two-branch form on p. 541 is the shape of [[rewrite-a-method-you-do-not-understand]].

The discriminating criterion is this wiki's own: a guard is a repair when the contract of the function admits that value at that point, and it is a symptom patch when the contract does not admit it and the guard absorbs it silently.

This wiki assigns the two neighbouring shapes by what the code does to the value. This page owns a guard that absorbs the value by returning, defaulting or catching. A number that is corrected and passed on, such as a rate divided by 100 when it looks too large, belongs to [[fix-the-model-not-the-offset]]. A guard a fix adds at the failing line, absorbing the value by returning, defaulting or catching, and a single input-keyed correction of a computed result added by a fix, are [[fix-the-root-cause]]. Two or more input-keyed corrections accreted in one method on its own computed result are [[rewrite-a-method-you-do-not-understand]].

This wiki also selects by the diff. A guard that a fix adds at the failing line, with the producer unchanged, is this page's. The same construct in standing code is [[crash-early]] for a dropped failure and [[caller-owns-the-precondition]] for a clamp or default at a routine's entry. A retry or delay whose comment blames a dependency is [[select-isnt-broken]]. A departure from the region's way of handling errors, in a diff that fixes no reported failure, is [[first-do-no-harm]].

## When not to apply

The book states no limit. The following limits are this wiki's own.

- The value crosses a boundary from a system you cannot change. Validating at that boundary is the fix at the origin available to you.
- A production incident needs mitigation before diagnosis. The patch is then temporary, and it should say so and point to the open cause.
- The contract does allow the value, so handling it where it arrives is correct.
- The special treatment of one input is a stated requirement for that case (a contract term for one customer). It is then not a fix, and it belongs in named data or configuration rather than a literal id in the computation.

## Repair

1. Observe the wrong value and walk the call stack back to where it was first wrong, per [[debugging-procedure]].
2. Change the producer so that it can no longer create the value.
3. Remove the guard at the surface if the contract no longer admits the value. Where bad data must never travel further, fail early instead of absorbing it: see [[crash-early]].
4. Look for other consumers that had absorbed the same value, per [[after-a-surprising-bug]].
5. For a special case keyed on one input: remove it, reproduce the wrong result again ([[stabilize-the-error]]), change the computation so that every input gets the right result, and add a test pinning the case.

## Before and after

```
// before: the symptom is patched where the crash appeared
function sendInvoice(invoice):
    if invoice.customer is null:    // added after the report
        return
    mail(invoice.customer.address, render(invoice))
```

```
// after: the importer created the bad invoice, and it now refuses the row
function importInvoice(row):
    customer = findCustomer(row.customerId)
    require customer exists
    return Invoice(customer, row.lines)

function sendInvoice(invoice):
    mail(invoice.customer.address, render(invoice))
```

A special case patched after a computation, *Code Complete*'s shape:

```
// before: the case where the wrong total was reported is patched
function totalClaims(client):
    for i in 0 .. claimCount(client) - 1:
        sum[client] = sum[client] + claimAmount(client, i)
    if client == 45:
        sum[45] = sum[45] + 3.45
    return sum[client]
```

```
// after: the accumulator starts from a known value for every client
function totalClaims(client):
    total = 0
    for i in 0 .. claimCount(client) - 1:
        total = total + claimAmount(client, i)
    return total
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], p. 126 and p. 128. The rule and the 4.5 versus 0.045 value are the book's. The signs and their assignments against [[fix-the-model-not-the-offset]] and the other neighbouring pages, the discriminating criterion, the limits, the repair and the pseudocode are this wiki's own.

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], p. 528 and section 23.3, pp. 540-542. The rule, the `y = 17` and `client == 45` illustrations, the initialisation reading and the three reasons are that book's, paraphrased except where quoted; the quotation was transcribed from the extracted text with line-break hyphens joined. The third sign and its assignment against [[rewrite-a-method-you-do-not-understand]], the requirement limit, repair step 5 and the second pair are this wiki's own; the pair only echoes the book's shape.
