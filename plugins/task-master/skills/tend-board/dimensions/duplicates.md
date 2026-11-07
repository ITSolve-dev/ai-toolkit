# Dimension: duplicates

Which tasks are one defect or one change, and which duplicate closings lost a fact or a
reference? Read `README.md`, *Every dimension*, first.

**Reads:** every task in the snapshot, open and finished: titles, descriptions, `links` of type
`duplicates` and `duplicated-by`. Only the scope the skill read is searched; an original outside it
is not found, and the result says so.

## Steps

1. **Test by defect, not by wording.** Two tasks are duplicates if one change would close both.
   Similar wording or similar behaviour is not the test, and reports that look different can be the
   same (`wiki/intake/duplicate-reports.md`, The discriminating test). Without the repository you
   cannot confirm that one change closes both, so every pair is a question, with the reason you
   think so.
   *Wrong if:* a pair rests on shared words alone.
2. **Two open tasks that one change would finish**: finding on the newer, naming the older as the
   candidate original (`wiki/intake/duplicate-reports.md`, Sign of violation). Name the kind from
   the page's table: an accidental resubmission needs nothing carried; another reporter or several
   failures need each new fact carried; an intentional resubmission also says the original has
   stalled (Kinds of duplicate).
3. **A closed duplicate holding a fact the original lacks** (a failing case, an environment, a
   trace): finding; propose carrying it to the original as a comment
   (`wiki/intake/duplicate-reports.md`, The rule, step 3).
4. **A task closed as a duplicate with no reference to its original**: finding, at the strength the
   page gives it: a missing record, not harm (`wiki/intake/duplicate-reports.md`, Sign of violation,
   last item). Without a `duplicates` link, a closing reason or a note naming it in the text, you
   cannot tell a task was closed as a duplicate; then there is no finding.
5. **Propose** in the page's order: carry what is new, link to the original, close the duplicate
   (`wiki/intake/duplicate-reports.md`, The rule). Closing is the person's decision. Note in the
   changeset that on some boards a duplicate link moves or closes the task by itself, so the
   `board` skill must show it before applying.

## Not a finding

- Two tasks on the same feature or file that need different changes.
- A parent and its subtasks, or tasks linked as `blocks` or `relates`: related is not the same.
- A closed accidental resubmission with nothing to carry.
- An empty `links` list: in a composed snapshot it may mean the links were not read
  (`not_covered`), not that there are none.
- A pair whose `duplicates` link contradicts states (both open, or the original closed while the
  duplicate stays open): report here as step 2 or 3, not under `link-contradictions`.
