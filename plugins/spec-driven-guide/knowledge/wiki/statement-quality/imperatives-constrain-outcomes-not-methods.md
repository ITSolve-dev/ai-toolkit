---
title: Imperatives constrain outcomes, not methods
category: statement-quality
summary: A binding statement is legitimate only where it is required for things to work together or to prevent harm — never to impose a method the outcome does not depend on.
tags: [rule, obligation-language, criterion, symptom]
sources: [web-page-rfc-2119-key-words-for-use-in-rfcs-to-indicate-requirement-levels-rfc-editor]
created: 2026-08-06
updated: 2026-08-06
---

[[rfc-2119-requirement-levels]] does not stop at defining the levels. Its sixth section restricts
when any of them may be used, and this is the load-bearing rule for anyone deciding what a document
may demand:

> Imperatives of the type defined in this memo must be used with care and sparingly. In particular,
> they MUST only be used where it is actually required for interoperation or to limit behavior
> which has potential for causing harm (e.g., limiting retransmisssions)  For example, they must
> not be used to try to impose a particular method on implementors where the method is not required
> for interoperability.
>
> — L75-L82

Two admissible grounds, and one named misuse.

**Admissible:** the constraint is required for things to work together, or it prevents harm.

**Inadmissible:** imposing a method that the outcome does not depend on.

## Why this is the same rule as information hiding, arriving from elsewhere

The IETF reached it from interoperability; Parnas reached it from cost of change; the design-doc
practice reached it from documents going stale. All three arrive at: **state the commitment, not
the means of meeting it.**

The convergence is worth noting because the three give different reasons, and a rule with three
independent justifications is more robust than one with a single elegant argument. See
[[information-hiding]] for the volatility argument and
[[abstract-interface-vs-representation]] for where the line falls in practice.

What RFC 2119 adds that the others do not is a second admissible ground — **harm**. A constraint on
method is legitimate where the method itself is dangerous, even if the outcome could be reached
another way. This is a real exception rather than a hedge, and documents that omit it end up unable
to say the one prescriptive thing they needed to.

## The symptom, and the two questions that find it

A binding statement that names *how*.

For each imperative in a document, ask:

1. **Would something fail to work together if this were free?** If yes, the imperative is earned.
2. **If not, is the prescribed method itself the hazard?** If yes, it is earned on the harm ground.

If neither, the statement is an imperative about method with no obligation under it — the same
defect as [[over-specification]], stated in the vocabulary of requirements rather than of
interfaces. Parnas's diagnostic applies unchanged: **name a valid implementation the statement
excludes**. If one exists and would have served, the imperative is costing something and buying
nothing.

## The caution about strength

The section opens with "care and sparingly", and this bounds the rule's own application. A document
that has established which of its statements bind, and finds nearly all of them binding, has
probably not applied the test — [[obligation-language]] notes uniform force as its own symptom.
