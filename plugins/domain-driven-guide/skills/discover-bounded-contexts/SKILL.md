---
name: discover-bounded-contexts
description: >-
  Use when deciding where to split a system, a monolith, or a fresh domain into bounded
  contexts — finding the boundaries, classifying subdomains as core/supporting/generic, and
  drawing a context map with an integration pattern per relationship. Trigger on "where do we
  split this", "how many services", "bounded context", "context map", "is this one domain or
  two", "should these be separate".
---

# Discover bounded contexts

The boundary is linguistic, not technical. You are looking for where the same word stops
meaning the same thing.

## Steps

1. **Establish which situation you are in** — a deliberate assessment ahead of building, or a
   boundary being discovered inside a system that already exists. The sources prescribe
   different entry paths for the two, and everything after this follows from the answer.

2. **Check that the investment is warranted.** These patterns are justified by complexity, and
   the sources are explicit that applying them to a simple domain makes it worse. Settle this
   before drawing anything.

3. **Collect the language** — the terms actually in use, and who uses them. The signal you are
   hunting is one word carrying different meanings to different speakers, usually subtly rather
   than obviously. The inverse signal is the identical concept appearing in two places, which
   normally means a modelling error rather than two contexts.

4. **Try the thin boundary first.** Where terminology is merely fuzzy, separate with a module
   and stop. Promote to a context only when the language demands it — a boundary drawn on a
   hunch buys integration machinery forever.

5. **Delegate the heavy pass.** Dispatch `domain-driven-guide:domain-modeler` with the language
   inventory, the scope, and the situation from step 1. It fetches the criteria from the base
   and returns the boundaries, each subdomain classified, and every relationship labelled with
   its integration pattern and direction.

6. **Settle the classification with the user.** Which subdomain is core is a business judgement,
   not a technical one, and it governs where effort goes afterwards. Do not infer it — but when
   there is nobody to ask, state the most likely reading, mark it unconfirmed, and continue
   rather than returning questions and nothing else.

## Deliver

Map what exists now before anything you intend to build — the present is what the map is for.

**Pass the agent's work through — its citations and its diagram — instead of restating it.**
Every decision reaches the user with the page it rests on. Summarising the citations away in
the last step destroys the one thing that separates this from a confident guess, and redrawing
the diagram yourself spends the context the delegation was meant to save.

Decisions, then the map as a Mermaid `graph`: one node per context annotated with its subdomain
kind, one edge per relationship pointing upstream → downstream and labelled with the pattern.
Nothing beyond that. The sources are emphatic that a context map earns its keep by staying
cheap enough that people keep using it, and that it is not an architecture or topology diagram.
