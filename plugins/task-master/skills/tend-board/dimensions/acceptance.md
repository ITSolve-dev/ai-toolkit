# Dimension: acceptance

## What it looks for

A task near or in work whose text states no check of done, or a check nobody could test.

**Scope:** tasks of kind `queued`, `active`, `handed_off`: title and description. The metrics'
`missing_acceptance_criteria` lists tasks with no matching heading (`reason`, `headings`): a prompt
to read the task, never the sign itself.

## Read

- `wiki/task-content/testable-acceptance.md` — The rule, Sign of violation, On a board, and
  *Specified Before the Task Starts*: what counts as a testable check, the three diagnoses and
  their next steps, why a check due before active work makes an `active` or `handed_off` task the
  stronger finding.
- `wiki/task-content/conditions-of-satisfaction.md`, Signs to check — why only tasks likely to be
  taken next are in scope, and the graded-word-in-a-title sign; threshold edges not covered.
- `wiki/task-content/empty-fields.md`, The rule — why an empty field or missing heading is not the
  sign: the check may live in another heading, a list or the title.

## Not a finding

- A `before_start` task without criteria: writing them for the whole backlog is the opposite
  failure (conditions-of-satisfaction, Signs to check).
- A spike whose criteria are questions (testable-acceptance, The rule).
- Many criteria; criteria that could each ship alone are `unit-of-work`'s.
- Criteria edited during the period: a stale criterion is the defect, not an edit
  (testable-acceptance, On a board).
- A check stated outside the expected heading but plainly in the text.
- A missing project-wide definition of done: not a task's criteria.

## Finding shape

The common shape (README), with the stage: `queued`, or `active`/`handed_off` as the stronger case.
Propose by the diagnosis testable-acceptance gives (clarify, question whether it should exist, or
draft a check): a `comment` asking, or a drafted check marked as a draft for the requester to
confirm, never written into the task as settled. For an `active` task add a question to the person
steering: does the run continue before the check is agreed?
