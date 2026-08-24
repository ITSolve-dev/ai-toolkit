---
title: Genre blur
category: structure
summary: Two genres in one file do not each get half — they collapse into something that serves neither, and the pairs that collapse are predictable from what they have in common.
tags: [failure-mode, genre, structure, symptom]
sources: [web-page-diataxis]
created: 2026-08-24
updated: 2026-08-24
---

> Crossing or blurring the boundaries described in the map is at the heart of a vast number of
> problems in documentation.
>
> — [[diataxis]], L258

The source's subject is end-user documentation and its four kinds. This wiki takes two claims from
it that hold of any genre pair, and applies them to its own genres — the argument document, the
decision record, the instruction written for an agent.

## Blur is directional, not random

> there is a kind of natural affinity between each of the different forms of documentation and its
> neighbours on the map, and a natural tendency to blur the distinctions (that can be seen
> repeatedly in examples of documentation).
>
> — L1108

The source then tabulates which pairs blur and what each pair shares (L1110-L1114). Four rows, four
shared properties: the pair that both guide action, the pair that both serve applying a skill, the
pair that both carry propositional knowledge, and the pair that both serve acquiring a skill.

**This wiki reads the shared property as the affinity itself** — that is our inference from the
table's shape, not a sentence the source writes. Two genres drift together along whatever axis they
already agree on.

This wiki reads that as the usable half. A reviewer does not need the source's taxonomy to apply it
— they need to ask what the two genres in front of them have in common, because that is where the
seam will fail. A design doc and an implementation plan both describe future work, so the plan
creeps in through the design section rather than announcing itself. A decision record and a design
doc both argue, so the record grows an alternatives discussion the size of a design doc.

## The cost is that neither need is met

> In the worst case there is a complete or partial collapse of tutorials and how-to guides into
> each other, making it impossible to meet the needs served by either.
>
> — L1118

The last clause is the finding worth keeping, and it is not what a reader expects: a document serving
two purposes reads as though it serves each of them partly, and the source states the outcome is
that neither is met.

**The mechanism under that outcome is this wiki's, not the source's.** Diátaxis reports the collapse
and does not explain it. This wiki's reading: the two sets of obligations are not additive, so
satisfying one displaces the other rather than diluting it. That reading is what makes the finding
usable on a genre pair Diátaxis never discusses — and it is an inference, so a case where a document
does serve two genres adequately would refute it rather than the source.

That is why [[splitting-a-document]] is a repair and not a tidy-up.

## It compounds

> Writing style and content make their way into inappropriate places. It also causes structural
> problems, which make it even more difficult to maintain the discipline of appropriate writing.
>
> — L1116

The loop the source names: blur produces structure that reflects the blur, and that structure then
makes the next correct placement harder. This wiki notes the consequence for timing — the defect
gets cheaper to fix the earlier it is caught, which is an argument for checking genre at the outline
stage rather than at review, and the same argument [[sprawl]] makes about placement.

## The symptom

**A section whose obligations come from a different genre than the document's.** Take one section
and ask what would make it good. Where the answer is a standard the rest of the document is not
held to — completeness for a section inside an argument, an argument inside a reference — that
section belongs to another genre.

**A heading that would be at home in a different document type.** "Steps", "Files to modify",
"Rollout" inside a design doc; "Alternatives considered" at length inside a decision record.

The test that resolves which genre a passage actually is: [[the-two-axis-test]].
