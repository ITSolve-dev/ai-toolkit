# Overview

This wiki is about writing documents that drive development — how to state what something must do
and why, at a level that survives the implementation changing underneath it.

It is organised by **the question a writer arrives with**. The complete catalogue, generated from
the pages themselves, is in [[index]]; this page is the map and says which pages carry weight.

## The groups

**obligation-and-mechanism — what to keep and what to leave out.** The centre.
[[state-the-commitment-not-the-means]] holds the rule several sources converge on and the tests
each supplies; [[information-hiding]] is Parnas's method for reaching it;
[[abstract-interface-vs-representation]] draws the line and [[the-changeability-test]] is how you
apply it to a specific text. [[resolving-a-scale-conflict]] handles the case where two rules here
disagree about the same passage — read it before applying either alone.
[[when-a-snippet-beats-prose]] is the one stated exception — the schema or state machine that is a
commitment rather than an implementation. [[parnas-criteria-for-decomposing-systems]] is the source
summary, and it is where the transfer from modules to prose is argued rather than assumed.

**altitude — how high to write and how to stay there.** [[defining-a-level]] fixes what a level is
and makes the audience the discriminator. [[what-a-design-doc-omits]] sets the ceiling for one
genre, [[degree-of-constraint]] its shape. [[the-c4-model]] is the source summary; the wiki takes
its reasoning about levels and none of its diagramming.

**document-types — which document this is.** [[design-doc]] and [[oxide-rfd-process]] are the two
genres treated in depth, with entry tests in [[when-to-write-a-design-doc]] and section rules in
[[non-goals]] and [[alternatives-considered]]. [[state-marks-authority]] and
[[timely-rather-than-polished]] cover documents that are not finished; read them together, neither
is safe alone. [[splitting-a-document]] handles a file carrying two genres.
[[design-docs-at-google]] and [[skills-for-real-engineers-formats]] are the source summaries.

**decision-records — how to record a decision so it outlives the document that made it.**
[[decision-record]] and [[madr-template]] give the two standard forms;
[[architecturally-significant]] is the entry test and records the disagreement about whether there
should be one. The checkable rules are [[consequences-include-the-negative]],
[[every-argument-carries-a-because]] and [[confirmation]]; [[superseding-not-editing]] governs
reversal and [[decision-log]] the collection. [[a-record-can-be-one-paragraph]] is the dissenting
position on how much of that a record owes, and carries the sharpest entry gate here.
[[documenting-architecture-decisions]] is the source summary.

**statement-quality — how to phrase something so it can be checked.** [[obligation-language]] for
force, [[imperatives-constrain-outcomes-not-methods]] for when force is earned,
[[imprecise-terminology]] for the words that make a claim unfalsifiable. [[completion-criteria]]
grades the bound a statement sets, which varies independently of its force; [[leading-words]] is the
one lever that shortens a statement and sharpens it at the same time, and carries the rule against
steering by prohibition. [[rfc-2119-requirement-levels]] is the source summary and is candid about
how little it covers.

**writing-for-agents — how to write for a reader that will not ask.**
[[the-right-altitude-for-an-agent]] names both failure modes, which no other group here does.
[[minimal-is-not-short]] is the floor under every cutting rule in this wiki and [[sprawl]] the
ceiling opposite it — read them together, either alone misleads.
[[canonical-examples-not-edge-cases]] and [[attention-budget]] are the genre's own constraints.
[[the-information-hierarchy]] decides where a piece of material sits, [[context-pointer]] how it is
reached, and [[the-two-loads]] which budget the choice spends.
[[effective-context-engineering]] and [[writing-for-agents-reference]] are the source summaries.

**failure-modes — what goes wrong.** [[over-specification]],
[[processing-order-is-not-a-structure]], [[implementation-manual]],
[[mixed-levels-of-abstraction]], [[comprehensible-only-as-a-whole]]. Each names a symptom; note
that the check sits in the middle of each page, not at the end, and that
[[comprehensible-only-as-a-whole]] carries a restriction that must be respected or it fires on
sound documents.

**reviewing — how to check a document or a set.** [[the-use-test]] is the primary method and the
only one that finds what was never written. [[unresolvable-references]] and
[[a-problem-with-no-decision]] are the cheap textual checks; [[consistency-across-a-set]] covers
defects that exist only between files; [[ranking-findings]] decides what order to report them in.
[[pruning-a-document]] is the sentence-by-sentence pass and the only page here with a source behind
it — the other five are this wiki's own work and say so.

## Where to start

**The central argument.** [[state-the-commitment-not-the-means]] → [[information-hiding]] →
[[abstract-interface-vs-representation]] → [[the-changeability-test]]. The source and its
worked evidence are in [[parnas-criteria-for-decomposing-systems]].

**Writing a document now.** [[defining-a-level]] to fix the level, then the genre page —
[[design-doc]] or [[decision-record]] — then [[what-a-design-doc-omits]] for the ceiling and
[[minimal-is-not-short]] for the floor.

**Checking a document you have.** [[ranking-findings]] first, so the pass produces something
usable, then [[the-use-test]], then the textual checks in `reviewing/` and the symptoms in
`failure-modes/`.

**One question, fast.** *Is this passage too much detail?* → [[the-changeability-test]]. *Two rules
disagree about it?* → [[resolving-a-scale-conflict]].

The position all of this adds up to, and an honest account of what is missing, is in
[[synthesis]].
