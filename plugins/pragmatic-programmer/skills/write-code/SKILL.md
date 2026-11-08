---
name: write-code
description: >-
  Delegate writing new code or changing behaviour to the plugin's craftsman, then have the result
  checked independently against the task and the base of rules. Use when the user asks to
  implement, add, build or change a feature, function, endpoint or module and wants the work
  delegated or checked against the base, or when a bounded part of a larger task can be handed off.
  Not for small edits the main agent can make directly. For better code with the same behaviour use
  improve-code; for an unknown fault use debug-code.
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Grep, Glob, Bash(git stash create:*), Bash(git status:*), Bash(git diff:*), Bash(git hash-object:*)
---

# Write code

The craftsman writes from a brief in a clean context; inspectors then read only the diff and the
brief, so the check does not inherit the author's reasoning.

**If any agent reports a denied read of the base, say so before any result.** Work done without the
base reads exactly like work done with it. Interactively the fix is approving the prompt;
headlessly, `--add-dir` with the plugin directory.

**One writer per checkout.** Never run two `craftsman` at once, and do not edit files yourself while
one works: parallel writers edit the same files and break each other's checks. When tests are in
scope the craftsman writes them; do not write tests first in this context.

**Headless, with nobody to ask:** answer under the most likely reading and mark it assumed in brief
and report. Never assume scope: stop with the question.

## Steps

1. **Read the project config** `.claude/pragmatic-programmer.md` if present: languages, paradigm,
   check commands, where the conventions live. Pass the paths, not copies of the conventions.

2. **Build the brief** in plain text: mode `write`; task; problem; goals; context the work needs;
   scope (files or area the craftsman may change, whether tests are in it); constraints. Scope has
   no default: if the request does not bound it, ask the user. Ask too about behaviour the request
   leaves open, or about a public signature the change must break; an answer guessed into the brief
   reads as the user's. The brief overrides the config. If the task needs a new composition across
   several units, run `design-code` first and put the chosen design in the brief's context.

   When tests are in scope, the brief asks the craftsman to propose the public seams it will test
   and return them as `NEEDS_INFO` before writing tests, unless the user named the interface to
   test, and to name, for each test, the break it catches.

3. **Record a baseline**, so the later diff holds only the craftsman's changes: `git stash create`
   (a commit when the tree is dirty, otherwise use `HEAD`; changes nothing),
   `git status --porcelain --untracked-files=all`, and `git hash-object` of each untracked file in
   scope. Not a git repository, or a git command fails: say so, skip the baseline, and give
   inspectors the files in scope in full, marked whole files, not a diff. Dispatch
   `pragmatic-programmer:craftsman`.

4. **`NEEDS_INFO`:** ask the user and continue the same agent with the answers (SendMessage); if it
   cannot be continued, dispatch a new one with the brief plus the answers, and say so. A
   `NEEDS_INFO` naming a change of module split or module shape is out of scope: report it, and
   continue only with a scope that keeps the architecture. **`BLOCKED`:** relay the reason, list the
   files changed since the baseline without reverting them, and stop. Suggest no command to discard
   the changes; how to undo them is the user's call.

5. **Independent check, after `DONE`.** Take the diff against the baseline (same `git status` form),
   plus in full: files untracked now and not before, and untracked files whose hash changed, marked
   "pre-existing, earlier content not kept". Dispatch `pragmatic-programmer:inspector` in parallel,
   one per dimension (the folders under `wiki/`) that the diff actually gives work to, not every one
   it could touch. Give each the absolute base root `${CLAUDE_PLUGIN_ROOT}/knowledge`, the
   repository path, the diff, the brief, the convention paths and its dimension; name generated
   files and files over a few hundred lines, do not inline them. Never pass the craftsman's report
   or reasoning. Findings count only on lines the diff adds or changes; issues in surrounding code
   go under outside the diff. An inspector's `NEEDS_INFO`: answer from the brief, else ask the user,
   and continue the same inspector. An inspector `BLOCKED` leaves its dimension not checked, never
   clean, and gets no round.

6. **Rounds.** Return to the same craftsman (SendMessage) only findings with a page, severity `high`
   or `medium` and no conflict flag, to fix or decline each with a reason. Low, `model opinion`,
   conflict-flagged and structural findings go straight to the report. A round is one return and one
   re-inspection, on the new diff, by the dimensions that raised them. At most two; what the last
   re-inspection still raises goes in the report, unfixed.

## Report

Relay, do not restate; keep every page citation.

- Status, and what was done against each task item.
- **Spec axis:** where the code departs from the brief.
- **Standards axis:** findings against the base, structure first, each with its page; declined
  findings with the craftsman's reason.
- Conflicts with project conventions.
- Each check with its command and output, or `NOT_RUN`; any "behaviour unverified" warning.
- Dimensions not checked, issues outside the diff, assumed answers, unproven facts, and what was not
  done.

No findings is a valid result: say which dimensions were checked and came back clean. Do not commit;
accepting the change is the user's call.
