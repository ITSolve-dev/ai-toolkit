---
title: Decompose a requirement into transformations
category: functions
summary: "Procedure for a function that tangles several conversions: name input and output, list the stages with sample data, split any stage too big to write directly, then compose."
tags: [method, transformation, top-down, decomposition]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A top-down procedure for turning a requirement into a chain of functions. It starts from what goes in and what must come out, not from which classes to create. The book calls this top-down design (p. 189). Run it when writing a new function, or against an existing long function to find where it should split. The second use is this wiki's extension. The book shows only new code.

## Procedure

1. **Name the input and the output of the whole requirement.** This gives one function that stands for the entire program (p. 189).
2. **List the stages between them, with a sample of the data at each stage.** The book writes this as a table of stage, conversion and example data (pp. 189-191). The sample is what shows a stage is real: if you cannot write down what the data looks like after a step, the step is not yet defined. That last point is this wiki's reading of why the tables carry samples.
3. **Treat each stage as a smaller requirement.** Where a stage is too big to write directly, decompose it the same way. The transformations nest (p. 190, p. 198).
4. **Stop when each step can be written directly.** The book stops at the point where implementing each one is easy (p. 190).
5. **Compose the top-level function.** Its body is the stages in order and nothing else (p. 192).

## Worked shape

The book's anagram finder takes a string of letters and returns the dictionary words those letters make, grouped by length. It has four stages: all combinations of three or more letters, the signature of each combination, the dictionary words matching any signature, and the words grouped by length (p. 189). The first stage alone splits into four: into characters, into all subsets, keep the long enough ones, back into strings (p. 190).

The finished shape, in this wiki's pseudocode:

```
function words_from(letters):
    return letters
        then combinations_of_three_or_more
        then signatures_of
        then dictionary_matches
        then grouped_by_length
```

## Checks while running it

These three checks are this wiki's own and do not come from the book:

- Each stage's output must have the shape of the next stage's input. A mismatch means a stage is missing, or a stage is doing two things.
- A stage may take extra parameters that do not flow through the chain. The book's search stage takes the pattern this way (p. 195, p. 197). A long run of parameters passed through several stages untouched suggests the stages are in the wrong order.
- A stage name should say what it produces. If the name needs "and", split it.

## Testing a requirement against the method

Exercise 21 asks the reader to state, as one top-level transformation, three things that do not look like pipelines at first: adding taxes to an order, loading configuration from a named file, and a user logging in (p. 198). The book's answers are one line each: an order becomes a final order, a file name becomes a configuration structure, and credentials become a session (pp. 357-358). The authors remark that ordinary code would likely define one function for shipping cost and another for tax, where the transformational view sees an order turned into a new kind of order (p. 357). This wiki reads that as the book's claim that the method reaches beyond batch work.

Failure shows up as a chain that works only when nothing goes wrong. Once a stage can fail, go to [[wrap-values-between-transformations]]. The idea behind the method is [[programs-transform-data]]. How to write the resulting stages is [[transformation-pipeline-over-method-chain]].

## Splitting an arrow that hides several jobs

Where one stage does several jobs, replace it with one stage per job. The book's answer to exercise 22 splits a single validate and convert step over a form field into string to integer, a lower-bound check, an upper-bound check, and a result of either a value or a reason for the error (p. 358).

The split has a stated dependency: «При этом предполагается наличие конвейера для обработки ошибок» (p. 358). This wiki reads that as a precondition of the method: without such plumbing, every stage has to test its predecessor's result, and the pipeline's shape is lost. See [[handle-errors-in-stages-or-in-the-pipeline]].

This wiki reads two gains from the split. Each check becomes separately testable and replaceable. And the final shape of the data has a name of its own, so a function that needs a final order cannot be handed a basic one, provided the types are distinct.

## Limits

These limits are this wiki's own; the book states none here.

- A stage that has to change shared state does not fit a plain arrow. Put the effect at the end of the chain rather than hiding it in the middle.
- Splitting has a floor. Two checks that always change together and have one error reason can stay one stage.
- Passing data through a chain makes its format a coupling between stages. See [[coupling-hidden-in-language-features]].

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 30, pp. 189-192, 195, 197-198, pp. 357-358 for the answer to exercise 21, and p. 358 for the answer to exercise 22. The use on existing functions, the listed checks, the reading of exercise 21, the reading of the error-handling dependency, the listed gains and the limits are this wiki's own. The pseudocode is this wiki's.
