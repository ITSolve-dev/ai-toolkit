---
name: write-design-doc
description: >-
  Write a design doc arguing that a design is right, at a level that survives the implementation
  changing underneath it. Use when the problem is already stated and settled and someone needs the
  design written up — if nobody has yet said what is observably wrong today, run prepare-brief
  first. Use it also to rewrite a doc that drifted into an implementation manual. For one decision
  rather than a design, use write-decision-record.
---

# Write a design doc

A design doc argues that a design is the right one. Its load-bearing content is the trade-offs, not
the description of what will be built — a document describing the same design without the argument
is a different genre, and a less useful one, because nobody can disagree with it.

Apply [`writing-discipline`](${CLAUDE_PLUGIN_ROOT}/skills/writing-discipline/SKILL.md) throughout. This skill adds only what
the genre owes on top of it.

## Steps

1. **Get the brief.** Without one, run [`prepare-brief`](${CLAUDE_PLUGIN_ROOT}/skills/prepare-brief/SKILL.md) first. Writing
   from an unconfirmed problem statement is what produces the rewrite cycle.

   Read `.claude/spec-driven-guide.md` for where design docs live and what language they are
   written in. Where it is absent, run [`init`](${CLAUDE_PLUGIN_ROOT}/skills/init/SKILL.md) or ask — do not guess a path, a
   document filed somewhere nobody looks is the same as one not written.

2. **Fix the reader and the grain, in writing, before prose.** One sentence, shown to the user and
   agreed. Everything downstream is judged against it — which detail is mechanism, which is
   commitment, how coarse a decision may be stated. Skipping this makes every later
   "too much detail?" question unanswerable.

3. **Propose the outline and get it approved.** Shape it by rule 7 of the discipline — two anchors,
   then descending importance. Show it as a list of section titles with one line each on what that
   section will claim. This is the cheapest place to be wrong, which is why the gate is here rather
   than after a draft exists.

4. **Write one section, show it, wait.** Per section: draft it, run the discipline checks against
   it, then show it and stop. The approval gate is the point of the skill — a whole draft delivered
   at once gets reviewed as a whole and its altitude errors survive.

   Collect open questions as they arise rather than at the end; the moment you notice one is when
   you know why it matters.

5. **Close.** Assemble, then re-read for defects that exist only between sections — a term used two
   ways, a decision stated in one section and contradicted in another, a section whose reader is
   different from the one fixed in step 2. Then run [`review-doc`](${CLAUDE_PLUGIN_ROOT}/skills/review-doc/SKILL.md).

## What the genre owes

- **Context is background, not argument.** Objective facts about the world as it is. A context
  section that argues for the chosen solution has absorbed the design section, and the reader loses
  the ability to check the argument against neutral ground.
- **Non-goals do most of the bounding.** What the design deliberately does not attempt, and why —
  this is what stops the document being judged against work it never claimed.
- **Alternatives considered, with why each was rejected.** Their absence reads as a design that was
  defaulted into rather than chosen. A rejected option with no stated reason will be proposed again
  within the year.

## Length

The document runs as long as the argument needs. When it runs far past what the reader can hold,
the usual cause is that the subject was too large rather than the writing verbose — say so, and
propose the split, rather than compressing an over-large subject into a shorter document that
states the same things less clearly.

## Done when

- Reader and grain are stated and every section sits at that grain.
- Each section was approved before the next was written.
- Non-goals and rejected alternatives are present, each with its reason.
- No passage names a tool, library, framework or file path that could be swapped without changing
  what the document promises.
