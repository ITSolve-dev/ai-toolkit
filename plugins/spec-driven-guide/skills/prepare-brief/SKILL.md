---
name: prepare-brief
description: >-
  Turn a raw intent — a ticket, a Slack thread, a half-formed idea — into a brief a design doc or
  decision record can actually be written from. Use this whenever someone asks to write a spec,
  design doc, ADR or technical description and nobody has yet stated, in one sentence, what is
  observably wrong today. Also use when a draft keeps getting rewritten because a new missing fact
  surfaces each round — that is a missing brief, not a writing problem.
---

# Prepare a brief

The brief is an input, not a draft. It exists so the document is written once instead of being
rewritten every time a missing fact surfaces.

## Steps

1. **Read before asking.** The ticket, the thread, the code the change touches. Every answer you
   can obtain by looking is one the user should not have to give — and asking for it burns the
   goodwill you need for the questions only they can answer.

2. **Interview for the gaps.** Ask in clusters rather than one question at a time; a person answers
   a related group in one pass and loses patience with a queue.

   | Cluster | What it must yield |
   |---|---|
   | Problem | What is wrong now, observably, and for whom |
   | Reader and grain | Who acts on this document, and at what level they decide |
   | Settled vs open | Which decisions are already made and by whom; which are genuinely open |
   | Bounds | What is deliberately out of scope; constraints not visible in the code |
   | Success | What would be observably true afterwards |

   When a "what is wrong" question gets answered with a solution, ask what breaks if it is not
   built. That answer is the problem. People arrive holding a fix, and a document written from the
   fix cannot be argued with — it has no criterion for judging the fix.

   The **reader and grain** cluster is the one worth pressing on. It fixes the altitude for every
   sentence of the document, and it is the cheapest thing to get wrong: a doc pitched at the wrong
   reader is not repaired by editing, only by rewriting.

3. **Write the brief.** Short, working notes — the five clusters, plus a list of **what the
   interview did not settle**. That list is why the brief exists: it names exactly what the writing
   skill would otherwise quietly invent.

4. **Show it and stop.** The user confirms the brief before any document is written. Starting the
   doc in the same turn defeats the point — the confirmation is what makes the single pass safe.

## What the brief is not

It is not written to the standard of the document it feeds. A brief may name tools, files and
libraries freely; deciding what of that survives is the writing skill's job. Applying
[`writing-discipline`](${CLAUDE_PLUGIN_ROOT}/skills/writing-discipline/SKILL.md) here strips information the writer still
needs.

## Done when

- Every cluster has an answer, or appears on the unsettled list.
- The problem is stated as something observably wrong, with no solution inside it.
- Reader and grain are one sentence the user has agreed to.
- The user has seen the brief and confirmed it.
