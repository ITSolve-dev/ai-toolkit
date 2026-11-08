---
name: improve-code
description: >-
  Delegate improving existing code without changing its behaviour to the plugin's craftsman:
  refactoring, untangling, simplifying, restructuring code inside a module, then an independent
  check against the base of rules. "No changes needed" is an expected answer. Use when the user asks
  to refactor, clean up, simplify, restructure or make code easier to change, or says code "feels
  wrong" and wants it fixed rather than only reviewed. For new behaviour use write-code; for a fault
  use debug-code.
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Grep, Glob, Bash(git stash create:*), Bash(git status:*), Bash(git diff:*), Bash(git hash-object:*)
---

# Improve code

Behaviour stays; the shape gets better, or the skill says why it already holds. An edit made to show
effort costs review time and risks behaviour for nothing.

**If any agent reports a denied read of the base, say so before any result.** Work done without the
base reads exactly like work done with it. Interactively the fix is approving the prompt;
headlessly, `--add-dir` with the plugin directory.

**One writer per checkout.** Never run two `craftsman` at once, and do not edit files yourself while
one works: parallel writers edit the same files and break each other's checks. Designers and
inspectors only read, so they may run in parallel with each other, never while the craftsman works.

**Headless, with nobody to ask:** answer under the most likely reading and mark it assumed in brief
and report. Never assume scope: stop with the question.

## Steps

1. **Read the project config** `.claude/pragmatic-programmer.md` if present: languages, paradigm,
   check commands, where the conventions live. Pass the paths, not copies of the conventions.

2. **Frame the work.** Turn the request into goals, each a named weakness in the code in scope; if
   the user named none, the craftsman finds them. Scope has no default: if the request does not
   bound it, ask, together with any goal the code does not bear out and whether tests are in scope.

3. **Structure first.** A goal is structural when it crosses units inside a module: splitting
   classes, moving responsibilities between them, the direction of dependencies between them.
   Extracting a function inside one file is a detail. A goal that needs a different module split or
   module architecture is out of scope: report it, do not design it. For a structural goal, design
   before writing: invoke the `design-code` skill on it, because one designer left alone returns the
   average design and "keep the current structure" must be among the options. If that wins, drop the
   goal, say why, and go on with the detail goals, or report "no changes needed" if none remain.
   When the chosen design moves code across files, show it to the user and wait; on a rejection,
   keep the current structure. Headless: keep the current structure and report the design as
   proposed.

4. **Build the brief** in plain text: mode `improve`; task; problem; goals; context, including the
   chosen design if any; scope; constraints. It also asks the craftsman to:

   - per weakness, make at most two attempts, undo one that does not remove it, and after two
     attempts in a row with no gain stop and report the remaining weaknesses as not done;
   - on a structural weakness found mid-run, return `NEEDS_INFO` naming it instead of restructuring
     without a design (then run step 3 on it and continue the same craftsman with the result);
   - when the change spans several files, add the new contract beside the old, move implementations
     and callers, remove the old last, so checks pass after each phase; run and report them per
     phase. Tests that pin current behaviour, if in scope, come first.

5. **Record a baseline**, so the later diff holds only the craftsman's changes: `git stash create`
   (a commit when the tree is dirty, otherwise use `HEAD`; changes nothing),
   `git status --porcelain --untracked-files=all`, and `git hash-object` of each untracked file in
   scope. Not a git repository, or a git command fails: say so, skip the baseline, and give
   inspectors the files in scope in full, marked whole files, not a diff. Dispatch
   `pragmatic-programmer:craftsman`.

6. **`NEEDS_INFO`:** ask the user and continue the same agent with the answers (SendMessage); if it
   cannot be continued, dispatch a new one with the brief plus the answers, and say so. A
   `NEEDS_INFO` naming a change of module split or module shape is out of scope: report it, and
   continue only with a scope that keeps the architecture. **`BLOCKED`:** relay the reason, list the
   files changed since the baseline without reverting them, and stop. Suggest no command to discard
   the changes; how to undo them is the user's call.

7. **Independent check, after `DONE` with edits.** Take the diff against the baseline (same
   `git status` form), plus in full: files untracked now and not before, and untracked files
   whose hash changed, marked "pre-existing, earlier content not kept". Dispatch
   `pragmatic-programmer:inspector` in parallel, one per dimension (the folders under `wiki/`) that
   the diff actually gives work to, not every one it could touch. Give each the absolute base root
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

- Status, and each weakness: removed, or not and why.
- If no edits: why the code holds, with pages. That is a full answer, not a failure.
- **Spec axis:** where the result departs from the goals or changed behaviour.
- **Standards axis:** inspector findings, structure first, each with its page; declined ones with
  the reason.
- The design chosen and the ones rejected, if step 3 ran.
- Conflicts with conventions; checks with command and output or `NOT_RUN`; "behaviour unverified" if
  nothing could verify it; dimensions not checked; issues outside the diff; assumed answers;
  unproven facts.

Do not commit; accepting the change is the user's call.
