---
title: Fault, error, failure
category: errors
summary: "Concept: three terms for one misbehaviour, each a different place to act: the fault is the cause in the code or configuration (fixed in source), the error is its manifestation in the running system (detected or not), the failure is the service that is not delivered (handled by a fallback); a handler that swallows a failure turns a detected error back into an undetected one."
tags: [concept, terminology, exceptions]
paradigm: any
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Larman uses three terms when he introduces failure handling in his case study (35.3, p. 790):

- **Fault**: "the ultimate origin or cause of misbehavior". Example: a programmer misspelled a database name.
- **Error**: "a manifestation of the fault in the running system. Errors are detected (or not)." Example: the naming service signals an error when asked for the misspelled database.
- **Failure**: "a denial of service caused by an error." Example: the product subsystem cannot provide product information.

## Why the distinction matters in code

This wiki reads the terms as three places to act:

- A fault is fixed in the source or the configuration. No handler repairs it.
- An error is where code can detect the problem: a check, an assertion, an exception thrown at the point of detection ([[crash-early]], [[assert-the-impossible]]). An error nobody detects becomes a failure further away, where the cause is harder to see.
- A failure is what the caller and the user see. The handling Larman describes for that level is a fallback, such as a local cache or asking the cashier to type the price, together with an exception named for the denied service ([[exception-at-the-interface-abstraction]], [[name-exceptions-after-the-problem-not-the-thrower]]). The wider set of options is [[fault-tolerance-techniques]].

This wiki adds a reading of its own: a handler that catches a failure and goes on silently turns a detected error back into an undetected one.

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.3, PDF p. 790: the definitions and examples. The fallbacks are from the same section's case study (35.2-35.3, PDF pp. 784-791).
- This wiki's own: the reading of the terms as places to act, the links to neighbouring pages, and the remark on silent handlers.
