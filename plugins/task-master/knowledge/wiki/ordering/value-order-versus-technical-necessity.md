---
title: Value Order Versus Technical Necessity
category: ordering
summary: The product owner orders by value but takes advice on sequencing; a value-ordered list cut at capacity must still be checked for low-ranked stories that are necessary, and those move up.
tags: [rule, prioritization, dependencies, release-planning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Value Order Versus Technical Necessity

An order by value is not yet a buildable release. Cohn states the division of labour in one sentence and then shows why it matters.

> A good product owner will accept ultimate responsibility for prioritizing, but will listen to advice from the development team, especially about sequencing.
>
> — [[cohn-agile-estimating-planning]], L2824

## The case in the source

In SwimStats the list is sorted "in descending order of how valuable she thinks each will be" (L2939), and the owner draws the line after the eighth story at 46 of 48 points. Then:

> However, the developers point out that the story prioritized as the lowest by the product owner is necessary
>
> — [[cohn-agile-estimating-planning]], L2941

That story is "As a system administrator, I can configure permissions and user groups." (L2941). It enters the release, an 8-point story is dropped to pay for it, and in the final plan it sits second, directly before the login-and-permissions story (L2943, L2955-L2965).

The source does not say why it was necessary. This wiki infers a dependency from its placement in Table 13.2: a story about seeing only permitted data needs permissions to be configurable.

## The rule

This wiki states what the example shows: after cutting a value-ordered list at capacity, walk the stories above the line and ask what each needs to work. A needed story below the line moves up, and enough is dropped to stay within capacity. The value order still decides what gets dropped, and the owner still makes that call: in the source she chooses which story to give up (L2943). Staying under the line is itself a choice, since Cohn notes that "Some teams may allow for 49 points under these circumstances." (L2941).

**Inputs.** The value order comes from the owner. Necessity comes from whoever knows the system, and in a task it should be readable as a stated dependency ([[sequence-versus-wait]], [[independent-tasks]]).

**Later fact that shows it wrong.** A story in the release turns out to be blocked by one outside it, or a story included as necessary turns out not to have been needed by anything that shipped.

## Sign of a violation

This sign is this wiki's. On the board, a story inside the release depends on a story outside it, or a story near the top of the release waits on one that sorts below it. The sign only works where dependencies are recorded, so its absence is not proof.

## What breaks when it is ignored

The release reaches its date with stories that cannot function, because a date-driven cut removed what they stood on. This is most exposed on a [[date-driven-vs-feature-driven|date-driven]] release, where the line falls wherever the capacity puts it ([[fitting-stories-into-a-release]]).

## Trade-off

The order stops being a pure expression of value. In the example, the swimmers' comparison with national records is lost to a story the owner had ranked lowest, and the release shrinks from 46 points of chosen value to 41 points that work together (L2939-L2943).

## Under an agent

This wiki's reading is that the check survives and matters more, since an agent given a story without its prerequisite may build around the absence by guessing rather than stop and raise it. The advising role the source gives developers falls to whoever steers, or to the plugin reading stated dependencies.

## Related

What a move out of the assumed order costs is on [[natural-order-of-work]]. The general case against dependencies is on [[minimize-feature-dependencies]]. The same division of labour for risk and learning is on [[combining-prioritization-factors]].
