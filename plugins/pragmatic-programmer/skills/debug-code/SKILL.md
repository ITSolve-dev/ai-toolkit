---
name: debug-code
description: >-
  Delegate finding and fixing a fault whose cause is unknown to the plugin's craftsman, which works
  from a failing command, ranked hypotheses and probes, and leaves a regression test behind. Use
  when the user reports a bug, a failing or flaky test, a crash, wrong output or a regression and
  the cause is not yet established; a confident guess by the user is not an established cause. If
  the cause is proven and only the change is wanted, use write-code.
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Grep, Glob, Bash(git stash create:*), Bash(git status:*), Bash(git diff:*), Bash(git hash-object:*)
---

# Debug code

The craftsman sees only the brief, so guesses already made in this conversation do not steer it.
Pass facts about the fault as facts. A theory, the user's or yours, goes in as one hypothesis to
rank, never as the cause, and the report says whether it held. This replaces any other debugging
procedure for this fault: collect facts here, do not investigate or hypothesise in this context, and
do not write the regression test here either.

**If any agent reports a denied read of the base, say so before any result.** Work done without the
base reads exactly like work done with it. Interactively the fix is approving the prompt;
headlessly, `--add-dir` with the plugin directory.

**One writer per checkout.** Never run two `craftsman` at once, and do not edit files yourself while
one works: parallel writers edit the same files and break each other's checks.

**Headless, with nobody to ask:** answer under the most likely reading and mark it assumed in brief
and report. Never assume scope: stop with the question.

## Steps

1. **Read the project config** `.claude/pragmatic-programmer.md` if present: languages, paradigm,
   check commands, where the conventions live. Pass the paths, not copies of the conventions.

2. **Collect the facts:** the symptom, expected versus actual, the input and the command or steps
   that show it, when it started, what changed. Ask the user for what is missing and cheap to get;
   an expected behaviour nobody stated is a question now, not a round trip later.

3. **Build the brief** in plain text: mode `debug`; task; problem (the symptom); goals; context (the
   facts); constraints; scope: reading is unbounded; edits are limited to the files or modules the
   facts or the user name, plus a regression test unless the user excludes it. A fix that needs
   another file returns `NEEDS_INFO` naming it; widening needs the user's yes. The brief adds to the
   craftsman's debug procedure:

   - shrink the repro before theorising;
   - tag every probe with `pp-probe`; undo each failed fix before the next; before returning, leave
     no probe and no failed fix in the tree;
   - leave a regression test at a seam that fails before the fix and passes after; if no seam
     reaches the fault, report the missing seam as a structural finding instead;
   - in the three-failed-fixes limit, a fix that breaks another check counts;
   - if it does not reproduce: when the evidence shows the code right under the stated conditions,
     return `DONE` with "no fault found" and that evidence, no regression test; otherwise return
     `BLOCKED` with what was tried.

4. **Record a baseline**, so the later diff holds only the craftsman's changes: `git stash create`
   (a commit when the tree is dirty, otherwise use `HEAD`; changes nothing),
   `git status --porcelain --untracked-files=all`, and `git hash-object` of each untracked file in
   scope. Not a git repository, or a git command fails: say so, skip the baseline, and give
   inspectors the files in scope in full, marked whole files, not a diff. Dispatch
   `pragmatic-programmer:craftsman`.

5. **After any return,** Grep for `pp-probe` the files changed since the baseline, including
   untracked files new or with a changed hash (without a baseline, the scope); any hit goes first in
   the report.

6. **`NEEDS_INFO`:** ask the user and continue the same agent with the answers (SendMessage); if it
   cannot be continued, dispatch a new one with the brief plus the answers, and say so. A
   `NEEDS_INFO` naming a change of module split or module shape is out of scope: report it, and
   continue only with a scope that keeps the architecture. **`BLOCKED`:** relay the reason, list the
   files changed since the baseline without reverting them. Suggest no command to discard the
   changes; how to undo them is the user's call. Then:
   - three failed fixes: put the structural question to the user; continue the same agent only with
     the user's answer, never with "try again";
   - no repro: relay what was tried, ask the user for the conditions under which it fails, and
     continue the same agent with them;
   - denied access or a check it cannot fix: relay and stop.

7. **Independent check, after `DONE` with a fix.** Take the diff against the baseline (same
   `git status` form), plus in full: files untracked now and not before, and untracked files
   whose hash changed, marked "pre-existing, earlier content not kept". Dispatch one
   `pragmatic-programmer:inspector` with dimension `testing`. Give it the absolute base root
   `${CLAUDE_PLUGIN_ROOT}/knowledge`, the repository path, the diff, the brief, the convention paths
   and its dimension; name generated files and files over a few hundred lines, do not inline them.
   Never pass the craftsman's report or reasoning. Findings count only on lines the diff adds or
   changes; issues in surrounding code go under outside the diff. An inspector's `NEEDS_INFO`:
   answer from the brief, else ask the user, and continue the same inspector. An inspector `BLOCKED`
   leaves its dimension not checked, never clean, and gets no round.

8. **Rounds.** Return to the same craftsman (SendMessage) only findings with a page, severity `high`
   or `medium` and no conflict flag, to fix or decline each with a reason. Low, `model opinion`,
   conflict-flagged and structural findings go straight to the report. A round is one return and one
   re-inspection, on the new diff, by the dimensions that raised them. At most two; what the last
   re-inspection still raises goes in the report, unfixed.

## Report

Relay, do not restate; keep every page citation.

- Any probe left in the tree, first.
- Status; the cause, and the evidence that it is the cause, or "no fault found" with the evidence.
- Whether the user's theory, if any, held.
- The repro command, failing before and passing after.
- Hypotheses ruled out and by which probe.
- The fix, and the regression test with the break it catches, or the missing seam as a structural
  finding.
- **Standards axis:** inspector findings, each with its page; declined ones with the reason.
- Checks with command and output or `NOT_RUN`; dimensions not checked; issues outside the diff;
  assumed answers; unproven facts; what was not done.

Do not commit; accepting the change is the user's call.
