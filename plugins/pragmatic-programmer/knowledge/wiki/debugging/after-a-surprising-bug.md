---
title: After a surprising bug
category: debugging
summary: "Use once a defect is fixed but nothing else moved: the fix was not rerun against the diagnosis tests, no test now catches it, bad data still travels layers before failing, and the same defect may sit elsewhere."
tags: [method, debugging, prevention, regression-test, similar-defects, search]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

Fixing a surprising defect is half the job. The book adds that you must also establish why it was not caught earlier (p. 133). This method runs after the fix, while the cause is fresh.

## Steps

1. **Find out why it was not caught.** Decide whether unit or other tests should change so that they would detect this defect (p. 133).
2. **Move detection closer to the origin.** If bad data travelled through a couple of levels before causing the failure, see whether better parameter checks in those routines would expose it earlier (p. 133). The book points to crashing early and to assertions here: see [[crash-early]] and [[assert-the-impossible]].
3. **Look for the same defect elsewhere.** Check whether other places in the code may show the same fault, and fix them now (p. 133).
4. **Make a recurrence visible.** «Убедитесь, что чтобы ни случилось, если это произойдет вновь, вы будете об этом знать» (p. 133).
5. **If the fix took long, find out why.** Ask what would make it easier next time, for instance better test hooks or a log file analyser (p. 133).

## Code Complete's version

McConnell ends both his procedure (step 5, p. 530) and his rules for fixing with work that starts after the code is changed, and he does not restrict it to surprising defects:

1. **Check the fix.** Check it yourself, have someone else check it, or walk through it together. Rerun the same triangulation tests used for the diagnosis and see whether every aspect of the problem is gone; if only part was solved, you will find out (p. 542).
2. **Check the whole program for side effects.** The book names automated regression testing as the easiest and most effective way (p. 542).
3. **Add a unit test that exposes the defect,** so that it cannot return unnoticed (p. 542). See [[find-bugs-once]]; for a test that must fail on the unfixed code, [[failing-test-before-the-fix]].
4. **Look for similar defects.** «Дефекты часто появляются группами» (p. 542). The book adds a test of understanding: «Если вы не можете сообразить, как искать похожие дефекты, значит, вы еще не полностью понимаете проблему» (p. 543).
5. **Learn from the defect.** The book's questions (p. 527): how and why did you make it, how could you have found it faster, how could you have prevented it, does the code hold other errors like it, and can they be fixed before they cause trouble. Reading the code to find the defect is also a chance to judge its readability and refactor it (p. 527).

The book reports that new defects are found more often in classes that had problems before than in classes that were error-free (p. 535). This wiki reads that as a reason to record where a defect was fixed, so the next search starts there.

## What to look for in step 3

The following is this wiki's own elaboration. Search for the shape of the fault and not the text of the fix: the same call with the same argument order, the same assumed unit, the same copied block. A defect that came from a false assumption usually recurs wherever that assumption was made, which ties this step to [[prove-dont-assume]]. A copied block with the defect in several places is also a sign of [[dry]].

*Code Complete* names the tool for this search. Multi-file search, McConnell says, can look for every occurrence of a class or routine name, and once you have found a defect in your code you can use such a tool to look for similar defects in other files (p. 696). It can match an exact string, a case-insensitive one, or a regular expression, which he singles out as especially powerful because it matches complex patterns; his example looks for arrays indexed by magic numbers, `[`, any spaces, one or more digits, any spaces, `]`, as `grep "\[ *[0-9]+ *\]" *.cpp`, and he notes the criterion can be tightened for precision (p. 696). This wiki turns that into steps: state the defect's shape in code rather than its location (a call whose result goes unchecked, a literal used as an index, a resource opened with no matching close); write the shape as a search; run it over the whole codebase, not just the module where the bug surfaced; and read each hit as a suspect to fix or rule out, not as a confirmed defect.

```
// the defect just fixed
price = table[3]           // 3 meant "discount column"; the layout changed

// shape -> search:  \[ *[0-9]+ *\]
total = table[3] * qty     // same stale assumption: fix
row   = grid[0]            // first element: rule out
```

A text search has a limit this wiki adds: it finds only siblings that share a lexical shape. The same misunderstanding written in other syntax, through other names or behind an abstraction does not match, so an empty result does not show the class of defect is gone. Start with a narrow pattern and widen it, since a broad one buries the real hits. A literal used as an index is itself [[named-constants-over-literals]].

## Limits

The book attaches these steps to surprising defects and to slow fixes (p. 133). A routine fix with an obvious cause does not need all of them, in this wiki's reading, beyond the test required by [[failing-test-before-the-fix]]. *Code Complete* asks for its first three steps after every fix (p. 542); this wiki resolves the two by keeping those three, which cost one test run and one test, for every fix, and the search for similar defects and the review of why it was slow for surprising or slow ones.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], pp. 133-134. Steps 1 to 5 are the book's, set out as a list. The book's closing advice to discuss the problem with the team is left out as team process. The guidance on what to look for in step 3 and the reading of the limits are this wiki's own.

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], pp. 527, 530, 535 and 542-543, and section 30.2, p. 696, for multi-file search and the magic-number pattern. The five steps, the questions and the finding about error-prone classes are that book's, paraphrased except where quoted; quotations were transcribed from the extracted text with line-break hyphens joined. The reading about recording where a defect was fixed, the resolution of the limits between the two books, the steps built on the multi-file search, its pseudocode and the lexical limit are this wiki's own.
