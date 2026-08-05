---
name: review-domain-model
description: >-
  Use to audit existing code against Domain-Driven Design — anemic models, oversized
  aggregates, infrastructure leaking into the domain, an ORM dictating the model, unrelated
  models blended into one context. Trigger on "review my domain model", "is this DDD", "audit
  the domain layer", "why does this model feel wrong", "is my domain anemic".
---

# Review a domain model

An audit, not a redesign. The reading happens in parallel inspectors; only findings come back.

## Steps

1. **Establish the scope** — a directory, a layer, a change set. Confirm it with the user when
   the request is open-ended, before dispatching anything.

2. **Establish the gate.** A missing pattern is a defect only where complexity justifies the
   pattern. The sources are as firm about over-application as under-application, so settle this
   first or the review manufactures work.

3. **Establish priority.** Which part of the scope carries the core of the business. The same
   defect matters more there, and this is the only ranking axis the sources actually supply.

4. **Fan out one inspector per dimension, in parallel.** Dispatch
   `domain-driven-guide:model-inspector` once per dimension, each given the scope, the gate
   result, and its single dimension:

   - behaviour placement — whether the objects that own the rules are the ones enforcing them
   - value modelling — concepts the domain treats as whole values but the code carries as bare
     primitives, and the logic that leaks out of the model as a result
   - consistency boundaries and transactional analysis
   - dependency direction and infrastructure isolation
   - read and write separation
   - language and strategic boundaries
   - integration topology and coupling across boundaries

   Each is decidable from its own evidence, so none waits on another. Adapt the set to what the
   scope actually contains — a single module has no integration topology.

5. **Merge.** Several dimensions can reach one root cause from different evidence: keep the
   finding once, with the strongest evidence behind it. Rank by cost, then by whether it sits
   in the core.

6. **Check for suppressed symptoms.** The sources name remedies that quiet a symptom and leave
   the defect in place. A symptom already suppressed that way is a finding in its own right,
   and usually a worse one.

## Deliver

Findings in the caller's context, most costly first: where, what it costs, and the page that
establishes it. Say plainly which dimensions came back clean, and which you did not run at all
because the gate ruled them out — a dimension that was never inspected is not a clean one.

**Carry the inspectors' page references through to the user.** Merging and de-duplicating is
your job; dropping the citations while you do it is not. A finding that arrives without the
page behind it is an opinion, and the reader has no way to check it — which is the entire
reason this review is worth more than a code smell list.

Fixing is a separate decision. Where a system needs several repairs the sources give an order
for them — surface that order rather than an unsequenced list.
