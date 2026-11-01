---
title: Ordering by One Factor
category: ordering
summary: An order driven by value alone meets its derailing risk late, an order driven by risk alone builds what is later thrown away, and an order that counts time but not money overvalues features; each leaves a trace in board history.
tags: [failure-mode, ordering, prioritization, risk]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Ordering by One Factor

This defect is an order that lets one input of the [[prioritization-factors]] decide. Cohn ([[cohn-agile-estimating-planning]]) describes the first two forms as the drawbacks of two opposite approaches (L1793). The signs are this wiki's derivation from those consequences. A sign raises a question, because either trace can have another cause ([[smell-is-not-a-finding]]).

## Value to the exclusion of risk

> a team that focuses on value to the exclusion of risk may develop a significant amount of an application before hitting a risk that jeopardizes the delivery of the product.
>
> — [[cohn-agile-estimating-planning]], L1793

**Sign:** finished work is mostly easy, high-value items, while the items with an unproven dependency are still open late in the period. Or a late item blocks or invalidates work already done.

**Check:** was the risky item's position decided, or was it merely never reached?

## Risk to the exclusion of value

> The risk-driven team accepts the chance that work they perform will turn out to be unneeded or of low value. They may develop infrastructural support for features that turn out unnecessary as the product owner refines her vision of the project based on what she learns from users as the project progresses.
>
> — [[cohn-agile-estimating-planning]], L1793

**Sign:** finished infrastructure has no feature using it, or features it was built for were later dropped or closed. Tasks that exist only to support other work outlive what they supported.

**Check:** was the supporting work tied to a feature that was still wanted when it was finished?

## Time without money

> Themes often seem worthwhile when viewed only in terms of the time they will take.
>
> — [[cohn-agile-estimating-planning]], L1740

This wiki reads this as a third form: a size is compared with a benefit without ever being turned into the same terms, so the comparison feels cheaper than it is. Cohn's remedy is [[cost-per-story-point]].

**Sign:** an item was included on its size and benefit alone, and a higher-valued item was then left out for lack of capacity.

**Check:** what would the same capacity have bought instead?

## Why it happens

Cohn says money makes the first two factors dominate discussions (L1720). This wiki adds that an order can therefore look reasoned while two of its inputs were never asked for. This wiki's remedy is [[combining-prioritization-factors]], and [[risk-value-quadrants]] for the first two forms. Ordering for the builders' convenience is a different fault, on [[order-by-value-not-convenience]].

## Agent executor note

The consequences concern work products, so this wiki reads them as surviving. Risk to the exclusion of value may be the likelier form with an agent, since this wiki expects supporting work to look cheap when an agent does it, but the source says nothing on this. Cheap construction would not remove the later cost of work nobody uses, because that cost is in [[cost-now-versus-cost-later]].
