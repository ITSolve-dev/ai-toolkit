---
title: "MADR — Markdown Any Decision Records"
category: decision-records
summary: The template that closes Nygard's gaps — explicit options with their pros and cons, a justification forced into the outcome sentence, and a section for how compliance will be confirmed.
tags: [summary, decision-record, template]
sources: [madr]
created: 2026-08-06
updated: 2026-08-06
---

A decision-record template maintained by the ADR organisation, now at version 4. It keeps
[[decision-record]]'s shape and adds the parts the original left implicit. Dual-licensed MIT or
CC0, so its text can be quoted and adapted freely (L252).

## What it adds over the original

- **Considered Options**, and a *Pros and Cons of the Options* section beneath — the explicit
  alternatives Nygard's format leaves to surface inside Context. See
  [[alternatives-considered]].
- **A forced justification.** The outcome is written as a sentence with a because-clause built into
  it: `Chosen option: "{title of option 1}", because {justification…}` (L209). See
  [[every-argument-carries-a-because]].
- **Confirmation** — how compliance with the decision will be checked. See [[confirmation]].
- **Decision Drivers** — the forces, named as a list, optional.

## Its disagreement with Nygard, stated openly

MADR deliberately widens the entry gate:

> Do not take the term "architecture" too seriously or interpret it too strongly. As the examples
> illustrate, any decisions that might have an impact on the architecture somehow are architectural
> decisions. […] There are debates about what is an architecturally-significant decision and which
> decisions are not architecturally significant. Since we believe that any (important) decision
> should be captured in a structured way, we offer the MADR template to capture any decision.
>
> — L94-L98

The renaming from "Architectural" to "Any" Decision Records in version 3 (L84) made the position
explicit before version 4 partially reverted the name while keeping the scope. This is a real
disagreement with [[architecturally-significant]], and both positions are recorded there.

## Scaling the form to the decision

MADR is "a template allowing to craft short, medium-sized, and large decision records", with "no
formal definition of short, medium-sized, and large decision records" (L264). Its worked example is
given twice: a compact version listing only context, options and outcome (L271-L282), then the same
decision expanded with pros and cons, consequences, confirmation and links (L288-L354). The source
calls the first "a very short and dense version" and describes the move to the second as unpacking
the decision (L266).

**Unpacking is the operation, and it is one-way.** Start at the size the decision warrants; expand
a section when the short form leaves a reader unable to act. A record padded to the long form
because the template has the headings produces the empty sections the template's own optional
markers are there to prevent — nearly every element is annotated "This is an optional element. Feel
free to remove."

## How to read it

**Authoritative on:** the structure of a decision record and the grammar inside it. It is
maintained, versioned, and its own decisions are published as MADRs, so the template is
demonstrated as well as described.

**A template, not an argument.** It states what the sections are and rarely why. The reasoning
mostly lives in the linked articles rather than the page itself, so this source supplies checkable
structure while [[documenting-architecture-decisions]] supplies the motivation.

**Out of scope here:** the bulk of the captured page. Installation via package manager, markdown
linting, filename patterns, folder organisation, the tooling decisions and the licensing decision
(L104-L257, L359-L558) are doc tooling, which the charter excludes. The MADR project's own
decisions were read as worked examples of the format, not for their content — with one exception:
its founding record justifies keeping decision records at all by citing a paper on making implicit
assumptions explicit, *"A rational design process: How and why to fake it"* (L397; the source gives
the title and a DOI, and names no author).
