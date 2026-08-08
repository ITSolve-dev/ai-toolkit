# Synthesis

## One rule, two reasons, three arrivals

Nine sources feed this wiki: software modularity from 1972, an internet standard from 1997, a
documentation-practice essay, an architecture-diagramming model, three treatments of decision
records, a process document, and model-vendor guidance from 2025. They share no lineage and cite
each other barely. Several arrive at the same rule:

> State the commitment. Do not state the means of meeting it.

**One reason, reached three times at three scales — all of them volatility.**

- **Parnas**, at the scale of a module: a revealed decision must be revised everywhere it was
  revealed ([[information-hiding]]).
- **Design-doc practice**, at the scale of a document: pasted definitions and schemas "quickly get
  out of date", so their presence makes the document wrong rather than detailed
  ([[what-a-design-doc-omits]]).
- **C4**, at the scale of a level: deployment is excluded because it "will likely vary across
  different environments" ([[defining-a-level]]).

These are not independent derivations. This wiki says so on the pages themselves — the design-doc
rule is "[[the-changeability-test]] arriving from practice rather than from theory", and C4's
exclusion is the same criterion applied across environments rather than across time. Their value is
that one argument is confirmed at three scales, which is a different and more useful fact than
three arguments agreeing.

**One genuinely independent reason.** RFC 2119 reaches the rule from interoperation and harm: an
imperative is earned only where things must work together, or where the prescribed method is itself
hazardous ([[imperatives-constrain-outcomes-not-methods]]). Nothing about volatility enters, and
the harm ground has no counterpart in the other three.

Each supplies a different test, and in practice the tests disagree about borderline cases. That
disagreement is where the judgement lives. The rule, its two grounds and all four tests are held
together in [[state-the-commitment-not-the-means]]; where the tests collide, the collision is
usually about grain rather than about the rule — [[resolving-a-scale-conflict]].

## The failure has two sides, and the tradition only sees one

Nearly every source here warns against saying too much. Only one warns against saying too little,
and it comes from outside the tradition: [[the-right-altitude-for-an-agent]] names both extremes —
brittle hardcoded logic at one end, "vague, high-level guidance that […] falsely assumes shared
context" at the other.

This asymmetry is a real gap in the older material, and it is the failure this wiki's own users are
most likely to commit, because every rule they will read here points the same direction.
[[minimal-is-not-short]] is the counterweight, and it is one page against many.

## The line is drawn higher than "avoid detail"

The single most useful finding: **Parnas puts operation names, parameter counts and types on the
side a description may state.** Storage formats and table organisation go on the side it must hide
([[abstract-interface-vs-representation]]).

So the discriminator is not concreteness. Both sides are equally concrete. It is **what a reader is
forced to depend on**: a commitment the subject intends to keep, or a decision it intends to
revisit.

The line moves with the subject rather than staying fixed — a document about a system commits at a
coarser grain than one about a component — which is why the level must be declared before the line
can be located ([[defining-a-level]]), and why [[mixed-levels-of-abstraction]] is a defect rather
than a stylistic complaint.

## Rigour attaches to claimed status, not to writing

The sources' standards — verifiable statements, complete consequences, arguments carrying their
reasons — would forbid the most valuable thing a person can write early: an unfinished thought.
[[timely-rather-than-polished]] takes the opposite position and explains why it must be stated
aloud: "there is a tendency to view a written statement as ipso facto authoritative".

The reconciliation is [[state-marks-authority]]. A document declares how settled it is, and the
standards apply according to that declaration. Without the declaration, the choice is between
publishing tentative work that will be mistaken for a decision and not writing it at all.

## What is missing, and how that biases the above

**No source on altitude proper.** The direct treatment of goal levels was not obtained; what stands
in for it is C4's structural hierarchy and one vendor post. The wiki's own central concept is its
least-sourced.

**The reviewing group is one page.** Everything the wiki says about checking a document is inferred
from pages written about producing one. The checks at the foot of each failure-mode page are this
wiki's synthesis, not a source's claim, and none has been validated against a real document.

**No source on requirement quality.** The enumerated rule catalogues were identified and not
obtained, so everything here about phrasing rests on [[rfc-2119-requirement-levels]] alone — three
pages defining five words — plus one page inferred from a diagramming model
([[imprecise-terminology]]).

**Nothing on preparing a document before writing it.** No source addresses turning an unformed
request into something a document can be written from.

Each gap tilts the same way: the wiki is strongest on *what to leave out of a finished document*
and weakest on *how to get to one, and how to check it afterwards*.
