---
title: Build an independent checking tool
category: testing
summary: "Use when outputs of a complex calculation are checked by hand, or a failure cannot be placed in the data or in the program: write a separate one-case program that recomputes a result, or a validator for the input data, independent of the main system's code."
tags: [method, testing, test-oracle, data-validation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell argues that most medium and large projects need tools unique to the project (p. 705). Two of his examples are testing methods in their own right: a stand-alone program that recomputes a single result, used to check the main system, and a validator for input data, used to tell whether a failure lies in the data or in the code (p. 706).

## Two shapes

**One-case oracle.** An insurance company built a large system to compute rate increases. The system was complex and the accuracy requirements were high, so hundreds of computed rates had to be checked, at several minutes each by hand. The company wrote a separate tool that computes one rate in seconds, and checked the main program's rates against it far faster than by hand (p. 706).

**Data validator.** At Microsoft, both the font files and the software rendering them were new, so a defect could sit in either. The developers wrote utilities that checked the data files for errors, which made it easier to tell whether an error came from the data files or from the software (p. 706).

```
// main system: batch, optimised, many interacting parts
rates = RateEngine.computeAll(policies)

// independent oracle: one policy, straightforward, written separately
for p in samplePolicies:
    assert rates[p.id] == SimpleRate.compute(p)

// validator: rule out the input before blaming the program
for f in fontFiles:
    FontFileChecker.validate(f)   // reports malformed data, not rendering bugs
```

## Why it works

This wiki reads the oracle's value as **independence**. A check that reuses the main system's code reproduces its mistakes; a separate one-case computation, written without the batch machinery, can disagree with it, and only a check that can disagree can catch anything. This is the same point [[test-code-is-defect-prone]] makes about expected values computed by an independent route, and [[property-based-testing]] makes about round-trip oracles. The validator narrows the search during debugging: once the input is known good, the program is the remaining suspect, which is the narrowing of [[debugging-procedure]].

## Trade-offs and limits

- The tool is code too, and can be wrong. This wiki adds that an oracle sharing the main system's misreading of the specification agrees with it, and so passes the wrong answer; the source does not say this.
- It costs time up front. The source's advice is to plan for it: «Планируя проект, необходимо подумать об инструментах, которые могут понадобиться, и выделить время для их создания» (p. 706).
- Where a small direct check, or an expected value [[test-values-checkable-by-hand]], already pins the behaviour, a separate tool adds nothing. This limit is this wiki's own.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, section 30.5, pp. 705-706 ([[code-complete]]): project-specific tools, and the font and insurance examples. The quotation was transcribed from the extracted text with line-break hyphens joined. This wiki's own: the pseudocode, the independence reading and its links, and the limits other than the planning advice.
