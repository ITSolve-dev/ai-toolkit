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

The source then tabulates which pairs blur and what each pair shares (L1110-L1114): the ones that
both guide action, the ones that both serve applying a skill, the ones that both carry propositional
knowledge. **The shared property is the affinity.** Two genres drift together along whatever axis
they already agree on.

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

The last clause is the finding worth keeping, and it is not what a reader expects. A document
serving two purposes reads as though it serves each of them partly. The source says the opposite:
the collapse makes it *impossible* to meet either — the two sets of obligations are not additive,
and satisfying one displaces the other rather than diluting it.

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
