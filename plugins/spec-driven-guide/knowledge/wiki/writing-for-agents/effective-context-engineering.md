---
title: "Effective context engineering for AI agents (Anthropic)"
category: writing-for-agents
summary: Vendor guidance on writing instructions a model will act on — it names the altitude problem directly and gives both failure modes bounding it.
tags: [summary, agent-reader, altitude]
sources: [web-page-effective-context-engineering-for-ai-agents]
created: 2026-08-06
updated: 2026-08-06
---

An Anthropic engineering post on assembling what a model sees at inference time. Most of it
concerns runtime mechanics; one section concerns writing, and that section is unusually direct
about the problem this wiki exists for.

## What it supplies

- [[the-right-altitude-for-an-agent]] — the altitude question named as such, with the failure mode
  at each end.
- [[minimal-is-not-short]] — the corrective that stops the altitude rule collapsing into brevity.
- [[canonical-examples-not-edge-cases]] — what examples are for and how they are misused.
- [[attention-budget]] — why economy is load-bearing for this reader specifically, rather than a
  matter of taste.

## Its governing principle

> Given that LLMs are constrained by a finite attention budget, *good* context engineering means
> finding the *smallest possible* set of high-signal tokens that maximize the likelihood of some
> desired outcome.
>
> — L41

The rest of the writing guidance follows from that constraint rather than from a theory of good
prose, which is what makes it a different argument from the ones reached in
[[information-hiding]] or [[what-a-design-doc-omits]] — same conclusions, an unrelated reason.

## Its method for getting there

Empirical, and stated as a procedure: "start by testing a minimal prompt with the best model
available to see how it performs on your task, and then add clear instructions and examples to
improve performance based on failure modes found during initial testing" (L47).

The rule governs **what triggers a change**, not what form the change takes: an observed failure
earns an edit, a hypothetical one does not. It says nothing about whether the edit should be a new
rule or a better example — and that second question is where the edge-case list comes from. See
[[canonical-examples-not-edge-cases]], which answers it: the edit should be an example that
demonstrates the pattern, not another entry. Growth per incident is the correct *trigger* and the
wrong *shape*.

## One transferable test, from an adjacent topic

Discussing tool sets rather than prose, the post states an ambiguity test worth keeping: "If a
human engineer can't definitively say which tool should be used in a given situation, an AI agent
can't be expected to do better" (L53).

Generalised: **a choice a knowledgeable human cannot make confidently from the text is one the
agent will make arbitrarily.** That is a usable check on any instruction that presents alternatives,
and it converts "is this ambiguous?" into a question with an observable answer.

## How to read it

**Authoritative on:** how instructions written for a model reader should be pitched. It is the
model vendor writing about its own models, and the altitude framing is stated more plainly here
than in any of this wiki's other sources.

**Narrow.** Only the section on composing context is in scope — L29 through L57, covering the
attention constraint, system-prompt altitude and examples. Everything from L59 onward — agentic
search, compaction, note-taking, sub-agent architectures — is runtime architecture, excluded by the
charter. The tool-design passages at L49-L53 sit inside the in-scope stretch and are likewise
excluded, except for the single ambiguity test quoted above, which is about text rather than tools.

**Perishable in its specifics.** The post itself notes that "the exact formatting of prompts is
likely becoming less important as models become more capable" (L45). Treat concrete formatting
advice as dated on arrival; the altitude reasoning is what survives.
