# Dimension: acceptance

Which task near or in work states no check of done? Read `README.md`, *Every dimension*, first.

**Reads:** tasks of kind `queued`, `active`, `handed_off`, their title and description;
`missing_acceptance_criteria` (items with `reason`, and the `headings` searched).

## Steps

1. **Take the stage first.** The statement is due before a task enters active work
   (`wiki/task-content/testable-acceptance.md`, Specified Before the Task Starts), and conditions are
   written ahead only for tasks likely to be taken next
   (`wiki/task-content/conditions-of-satisfaction.md`, Signs to check). So the scope is `queued`,
   `active` and `handed_off`. An `active` or `handed_off` task without a check is the stronger
   finding: the agent already works to whatever its reading allows.
2. **Read the flagged tasks, do not trust the flag.** `missing_acceptance_criteria` finds a missing
   heading or description, which is a prompt to look and not the sign: the check may live under
   another heading, in a list, or in the title (`wiki/task-content/empty-fields.md`, The rule;
   `wiki/task-content/testable-acceptance.md`, Sign of violation). A finding needs that nothing in
   the text states what would show the task done.
3. **Read the unflagged tasks for an untestable check.** Under a heading, an outcome that is an
   adjective with no threshold ("fast", "usable", "secure"), or that two readers could disagree
   on, is a finding; so is a graded word in the title with no condition pinning it
   (`wiki/task-content/testable-acceptance.md`, Sign of violation;
   `wiki/task-content/conditions-of-satisfaction.md`, Signs to check). A threshold whose edges are
   not covered is a finding of the same kind.
4. **Propose by cause.** Testable acceptance gives three next steps: clarify the request, ask
   whether it should exist, or draft a check for the requester to confirm
   (`wiki/task-content/testable-acceptance.md`, Sign of violation). Choose by what the text shows;
   a drafted check is marked as a draft, never written into the task as settled. For an `active`
   task, add a question to the person steering: whether the run continues before the check is
   agreed.

## Not a finding

- A `before_start` task without criteria: writing them for the whole backlog is the opposite
  failure (`wiki/task-content/conditions-of-satisfaction.md`, Signs to check).
- A spike whose criteria are questions (`wiki/task-content/testable-acceptance.md`, The rule).
- Many criteria. Criteria that could each be delivered alone are `unit-of-work`'s.
- Criteria edited during the period: editing is not the defect, a stale criterion is
  (`wiki/task-content/testable-acceptance.md`, On a board).
- A check stated outside the expected heading but plainly in the text.
- A missing project-wide definition of done: not a task's criteria
  (`wiki/task-content/testable-acceptance.md`, Sign of violation, last paragraph).
