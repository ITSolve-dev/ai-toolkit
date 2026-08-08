# Synthesis

## One rule, two reasons, three arrivals

Eleven sources feed this wiki: software modularity from 1972, an internet standard from 1997, a
documentation-practice essay, an architecture-diagramming model, three treatments of decision
records, a process document, model-vendor guidance from 2025, and two working documents from a
practitioner's agent toolkit. They share no lineage and cite each other barely. Several arrive at
the same rule:

> State the commitment. Do not state the means of meeting it.

**One reason, reached three times at three scales — all of them volatility.**

- **Parnas**, at the scale of a module: a revealed decision must be revised everywhere it was
  revealed ([[information-hiding]]).
- **Design-doc practice**, at the scale of a document: pasted definitions and schemas "quickly get
  out of date", so their presence makes the document wrong rather than detailed
  ([[what-a-design-doc-omits]]).
- **C4**, at the scale of a level: deployment is excluded because it "will likely vary across
  different environments" ([[defining-a-level]]).

A fourth arrival changes the *ground* rather than the scale. Practitioner guidance for agent-read
documents treats the surrounding environment — config files, directory layout, `--help` output — as
a competing source of truth, and a document restating it as "a **cache**: a copy of a lookup"
([[pruning-a-document]]). The criterion becomes **discoverability now** rather than **volatility
later**, and it selects nearly the same content. It is the cheaper of the two to run: a reviewer can
check whether a fact is in a config file, and cannot check whether it will change.

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

Nearly every source here warns against saying too much. Only the agent-reader material warns against
saying too little: [[the-right-altitude-for-an-agent]] names both extremes — brittle hardcoded logic
at one end, "vague, high-level guidance that […] falsely assumes shared context" at the other.

This asymmetry is a real gap in the older material, and it is the failure this wiki's own users are
most likely to commit, because every rule they will read here points the same direction.
[[minimal-is-not-short]] is the counterweight, and it now names the ceiling standing opposite it so
that neither is applied alone.

**The two sides are not symmetrical, and the difference is in the repair.** Saying too much is fixed
by deleting — the passage fails a test and goes. Saying too little is fixed by writing. Between them
sits a third case the wiki was missing until [[sprawl]]: a document too long **while every line in
it is live**, where deletion is the wrong repair and relocation is the right one
([[the-information-hierarchy]]). A reviewer who knows only the first two repairs will reach for
deletion there and remove obligations while believing they are cutting verbosity.

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

**The reviewing group is almost all inference.** [[pruning-a-document]] is the one page there with a
source behind it; everything else the wiki says about checking a document is inferred from pages
written about producing one. The checks at the foot of each failure-mode page are this wiki's
synthesis, not a source's claim, and none has been validated against a real document.

**No source on requirement quality.** The enumerated rule catalogues were identified and not
obtained. Phrasing therefore rests on [[rfc-2119-requirement-levels]] — three pages defining five
words — plus [[imprecise-terminology]] inferred from a diagramming model, and
[[completion-criteria]] and [[leading-words]] taken from a source about agent-read documents rather
than about requirements. Nothing here comes from the literature that studies the question directly.

**Nothing on preparing a document before writing it.** No source addresses turning an unformed
request into something a document can be written from.

Each gap tilts the same way: the wiki is strongest on *what to leave out of a finished document*
and weakest on *how to get to one, and how to check it afterwards*.
