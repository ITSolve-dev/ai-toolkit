# Dimension: link-contradictions

## What it looks for

- **Parent finished, child open:** a `finished` task with an unfinished subtask, or the reverse view.
- **Finished before its blocker:** a `finished` task blocked by an unfinished one; or an open task
  marked blocked whose every blocker is finished.
- **Started while blocked:** an `active` task blocked by an unfinished one, with no blocked marker.

**Scope:** `kind`, `parent`, `subtasks`, `markers`, and `links` of the question's types for
`blocks` (either direction) and `relates`; a relation with no type: `not_covered`. A link the tool
records in one direction only is listed once per pair.

## Read

- `wiki/moving-work/what-may-move.md`, Sign of violation — the linked-states sign: it shows a move
  ignored a relation, not which task is wrong; two of ten practitioners disagreed, so apply the
  smell check strictly. The base states it for parent and subtask; the blocking cases extend it
  (mark them not from the base).

## Not a finding

- A `relates` link in any states; any `duplicates` link (`duplicates` owns them).
- A cancelled parent with open children the process document keeps on purpose.
- An empty `links`, `subtasks` or null `parent` in a composed snapshot (README, step 5).

## Finding shape

One per pair, in the README's shape. Return a question per pair carrying both options (close the
child or reopen the parent; drop a stale link or mark the stop). Never choose; propose no op.
