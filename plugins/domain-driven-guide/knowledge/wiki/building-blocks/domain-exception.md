---
title: Domain Exception
category: building-blocks
summary: Using named exceptions, drawn from the ubiquitous language, to express domain concepts such as 'out of stock' as first-class outcomes of the model.
tags: [pattern, domain-exception, error-modeling, ubiquitous-language, building-blocks, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

A **domain exception** is an exception that names and expresses a business concept, not merely a technical failure. *Architecture Patterns with Python* presents it as its domain-modeling chapter's final building block: "exceptions can be used to express domain concepts too" (raw L999). Errors, like [[entity]]s and [[value-object]]s, are part of the model.

## The motivating concept

Conversations with domain experts surfaced a real business outcome: an order sometimes cannot be allocated because the item is *out of stock*. That possibility is captured directly as a named exception rather than a boolean, a `None`, or a generic error — "we can capture that by using a *domain exception*" (raw L1000..1002):

```python
class OutOfStock(Exception):
    pass

def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(
            b for b in sorted(batches) if b.can_allocate(line)
        )
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")
```

The [[domain-service]] `allocate` translates the mechanical failure to find a suitable batch (`StopIteration`) into the meaningful domain event `OutOfStock`, carrying the offending SKU.

## Named in the ubiquitous language

The key discipline is naming. "We take care in naming our exceptions in the ubiquitous language, just as we do our entities, value objects, and services" (raw L1011). `OutOfStock` is a phrase the business uses; a generic `AllocationError` or `ValueError` would discard that shared meaning. This ties domain exceptions to the [[ubiquitous-language]] as firmly as any other building block.

## Trade-offs and failure modes

- **Gain:** callers handle a business outcome explicitly (`pytest.raises(OutOfStock)`), and the exception name documents a real domain rule at the point it is violated.
- **Generic exceptions leak intent.** Reusing `ValueError`/`Exception` for a domain condition forces callers to string-match or guess, and hides the business rule from readers and experts.
- **Off-language naming.** An exception named after implementation mechanics (e.g. `NoBatchFound`) rather than the business concept (`OutOfStock`) breaks the ubiquitous-language contract.

> **A modeling choice, not a rule.** Whether a domain outcome is an exception at all is itself a modeling decision. On its own [[domain-service]] the same book models a *failed authentication* as a returned `null` rather than an exception, because failing to authenticate "is not an exceptional error, just a normal possibility of this domain." Out-of-stock, by contrast, is worth signalling loudly — the point is that the choice belongs to the domain, not to convenience.

Domain exceptions are raised by [[domain-service]]s and [[entity]] behavior within the [[domain-model]] and named per the [[ubiquitous-language]].

## Related

- [[domain-service]] — where the allocation exception is raised.
- [[ubiquitous-language]] — the vocabulary the exception name must come from.
- [[domain-model]] · [[entity]] · [[value-object]] — the other building blocks errors sit alongside.
- [[web-page-cosmic-python-book]] — source summary.
