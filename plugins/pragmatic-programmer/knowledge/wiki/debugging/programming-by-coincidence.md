---
title: Programming by coincidence
category: debugging
summary: "Concept: code whose author cannot say why it works; owns a change kept because it made a run pass, with no stated cause, and names the owners of the boundary, offset and leftover-call shapes."
tags: [concept, assumptions, understanding, false-confidence]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

Programming by coincidence is writing code whose success its author cannot explain, then treating that success as evidence the code is right. Thomas and Hunt set it against programming deliberately. The failure it predicts is specific: code that was never understood when it worked cannot be diagnosed when it stops.

## What it is

The book's case is a programmer, Fred, who types a little code, tries it, finds it seems to work, and repeats this for weeks until the program stops working and hours of effort do not bring it back (p. 246). The book's explanation is that he cannot find why it fails because he never established why it worked. Limited testing showed success by chance, and that success gave him false confidence. Its summary of the mechanism: if you do not know why the program works, «вы не знаете причин, по которым она может отказать» (p. 250).

The book's minefield image (pp. 245-246) makes the logical point. A soldier probes the ground, finds nothing, concludes the field is safe, and is killed. Probing that found nothing was not evidence of safety.

## The forms it takes

- **Accidents of implementation.** Code depends on how something happens to be written now: undocumented behaviour, boundary conditions, call order. See [[rely-only-on-documented-behaviour]] and [[remove-calls-you-cannot-justify]].
- **Lack of precision.** A wrong result is patched by an adjustment that happens to give the right number. See [[fix-the-model-not-the-offset]].
- **False patterns.** People see regularity and cause where there is only coincidence.
- **Accidents of context.** Code relies on surroundings nothing guarantees. See [[do-not-rely-on-unguaranteed-context]].
- **Implicit assumptions.** Beliefs held in the head, rarely written down, and often disputed between developers (p. 249). See [[assert-the-impossible]].

## False patterns in failure evidence

The book gives two diagnostic examples (p. 249). An error appearing in a log every 1000 requests may be a hard race condition or just an old bug. Tests that pass on one machine and fail on the server may reveal a difference between the environments, or may be chance. Its instruction is «не допускайте, а убеждайтесь» (p. 249); see [[prove-dont-assume]].

The book also warns that testing is particularly exposed to false causation and accidental consequences: it is easy to assume X causes Y (p. 249). This wiki reads that as a limit on any report that says a change fixed a failure. The report needs a stated mechanism, because a passing run after the change is what coincidence also looks like.

## The test that separates understanding from luck

Can you explain the code in detail to a less experienced programmer? The book says that if you cannot, you are probably relying on coincidence (p. 250). McConnell sets the same test at the line. His wording: «Нужно знать роль каждой строки своей программы.» (*Code Complete*, Russian edition, p. 223). He holds that nothing counts as correct merely because it appears to work, that code you cannot explain the working of probably does not work, and that a working method you do not understand should be studied, discussed and tried in alternatives until you do (p. 223). Where the behaviour stays unexplained, he prefers rewriting the method to patching it; see [[rewrite-a-method-you-do-not-understand]]. This wiki adds that the test applies to a line as well as a program: for a line under review, ask what would change if it were deleted.

This wiki assigns the neighbouring shapes as follows. A change kept because it made a run pass, with no stated cause, is [[programming-by-coincidence]]. A loop bound flipped or nudged by 1 until a test passes is [[check-loop-boundaries-by-hand]]; a lone unexplained ±1 or scale factor applied to a value is [[fix-the-model-not-the-offset]]; a run of near-synonymous calls left in because the result finally looked right is [[remove-calls-you-cannot-justify]]. For a change kept with no stated cause, the repair is to state the mechanism by which it fixes the failure, or to remove it and reproduce the failure again ([[stabilize-the-error]]).

## Compiling to see what happens

McConnell describes the same failure in chapter 33 under the name of intellectual carelessness: not quite understanding one's program and «просто компилируете ее, чтобы увидеть, будет ли она работать» (*Code Complete*, p. 807). His example is running the program to decide whether a condition should use `<` or `<=`. He argues that whether the program then works does not matter, because its author does not understand it well enough to say why it works (p. 807). His reason ties this to testing: «тестирование может указать только на наличие, но не на отсутствие ошибок» (p. 807), and a program one does not understand cannot be tested thoroughly. He calls compiling a program to see what happens a warning sign (p. 808, paraphrased): it may mean a return to design is needed, or that coding began without a clear grasp of what was being done. His instruction is to make sure the program is understood before compiling it (p. 808).

The book also files this under the first kind of laziness, which the book says hardly ever pays: compiling a class to see whether it works instead of checking it in one's head (pp. 810-811). As a replacement habit it suggests writing a class in pseudocode before coding it, or reading code carefully before compiling it (p. 814); see [[pseudocode-programming-process]].

This wiki reads McConnell's `<` versus `<=` case as the line-level form of the explanation test above. For a boundary in a loop or comparison, the author should be able to say which element is included and why, without a run. A loop bound flipped or nudged by 1 until a test passes is [[check-loop-boundaries-by-hand]]. This wiki also keeps a limit. Experimenting with a small throwaway program to learn how a language feature behaves is what McConnell recommends elsewhere in the same chapter (p. 803), and it is not coincidence, because the experiment answers a stated question and its result is understood before production code depends on it.

## Programming deliberately

The parts of the book's list (pp. 250-251) that bear on code:

- Do not build on an application you do not understand, or a technology you only half understand.
- Rely on established facts. Where you do not know whether something is reliable, assume the worst.
- Document your assumptions.
- Test assumptions as well as code, by experiment and by assertion.
- Do not let existing code dictate future code. Code that no longer fits can be replaced ([[refactor-early-and-often]]), on the assumption that replacing it costs less than keeping it (p. 251).

## Limits

The book gives two limits. Where relying on documented behaviour is impossible for some reason, «следует задокументировать свое допущение» (p. 248), so undocumented behaviour may be used if the assumption is written down. On replacing code, a footnote warns «Здесь можно зайти слишком далеко», with a developer who rewrote all the code handed to him because he had naming conventions of his own (p. 251).

This wiki adds a third: nobody understands every layer below them, so the demand is to rely only on what a layer promises, not to read all of it. This wiki counts understanding the contract as enough, and counts relying on what the contract does not state as coincidence unless the assumption is written down.

## Source

[[pragmatic-programmer]], Topic 38, pp. 245-251. McConnell's role-of-every-line demand and the study-until-understood advice: [[code-complete]], p. 223. Compiling to see what happens: [[code-complete]], ch. 33.4, pp. 807-808; ch. 33.7, pp. 810-811; ch. 33.9, p. 814; ch. 33.3, p. 803 for experiments. The line-level form of the explanation test, the reading of fix reports, the third limit, the reading of the `<` versus `<=` case and its distinction from an experiment, the assignment of code shapes to this page and its neighbours, and the repair for a change kept with no stated cause are this wiki's own. The ch. 33 quotations were transcribed from the extracted text and should be checked against the page image. Related: [[do-not-silence-warnings]].
