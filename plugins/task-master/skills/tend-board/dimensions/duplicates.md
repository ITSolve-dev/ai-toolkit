# Dimension: duplicates

## What it looks for

- Two open tasks one change would finish.
- A task closed as a duplicate whose text holds a fact the original lacks (a failing case, an
  environment, a trace).
- A task closed as a duplicate with no reference to its original.

**Scope:** every task in the snapshot, open and finished: titles, descriptions, and `links` of the
tool's type for `duplicates` as the question names it. No type named: links are not read, and the
reference check is `not_covered`. Only the scope the skill read is searched; say that an original
outside it cannot be found.

## Read

- `wiki/intake/duplicate-reports.md` — the whole page decides this dimension:
  - The discriminating test: one change closes both; shared wording is not the test.
  - Kinds of duplicate: what each kind needs carried, and that an intentional resubmission means
    the original has stalled.
  - Sign of violation: the three board-state signs above, and that a missing reference is a
    missing record, not harm.
  - The rule: the order of the proposals (carry, link, close).

You cannot confirm from files that one change closes both, so every pair is a question with the
reason you think so. Name the newer task, with the older as the candidate original.

## Not a finding

- Two tasks on the same feature or file that need different changes.
- A parent and its subtasks, or tasks linked `blocks` or `relates`.
- A closed accidental resubmission with nothing to carry.
- A closed task with no duplicate link, close reason or note naming an original.
- An empty `links` list in a composed snapshot (README, step 5).

A duplicate link whose states contradict (both open, or the original closed while the duplicate
stays open) is reported here, not under `link-contradictions`.

## Finding shape

The common shape (README), with the kind of duplicate from the page's table. Propose in the page's
order: `comment` on the original carrying what is new, `link` with relation `duplicates`, `close`
with `decide` and reason `duplicate`. Where the tool's help names a side effect of the link (it also
closes a task), repeat it in the link's `why`.
