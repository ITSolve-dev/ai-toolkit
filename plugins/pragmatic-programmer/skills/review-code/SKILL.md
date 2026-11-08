---
name: review-code
description: >-
  Report-only review of code, a diff, a branch or a module against this plugin's base of
  code-quality rules, with a cited page behind each finding and, when a ticket or spec exists, a
  separate check that the change does what it asked. Use when someone wants a rule-backed review,
  asks "is this code good", "does this do what the ticket asked", or wants a check before merging.
  To change the code use improve-code; for whether tests can catch bugs use check-tests; for domain
  modelling use domain-driven-guide's review-domain-model.
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Grep, Glob
---

# Review code

Parallel inspectors, one per base group, do the reading; only findings come back. Each sees the
code, the conventions and the spec, never your reasoning, so it cannot simply confirm it.

Base root: `${CLAUDE_PLUGIN_ROOT}/knowledge`, absolute by the time you hand it on.

**If an inspector reports a failed read, say so before any finding**: its group was not reviewed,
and an audit without the base reads like one with it. Interactively, approve the prompt;
headlessly, pass the plugin directory with `--add-dir`.

## Steps

1. **Scope** — a diff, files, a module. Confirm an open-ended or large scope, or split it: every
   inspector reads all of it. Take the paradigm and conventions from
   `.claude/pragmatic-programmer.md`; without it, collect the convention files you find
   (`CLAUDE.md`, `CONTRIBUTING`, linter and formatter configs) or note there are none. Find the spec
   the user named or the change cites. No spec is normal; do not reconstruct one.

2. **Pick the groups**, the folders under `wiki/`. Run one only when you can name a construct in
   scope its pages judge, and give that reason in the opening line; run `structure` when the scope
   spans more than one unit. A single-function change needs two to four.

3. **Dispatch in parallel**, one `pragmatic-programmer:inspector` per group in one message. Each
   brief: the group, the absolute base root, the scope, the paradigm, the conventions (paths), the
   spec if any. For a diff or branch, pass the diff text or paths with changed line ranges: the
   inspector cannot run git. Pass no reasoning of yours about the code.
   - `NEEDS_INFO`: answer from step 1, else ask the user (headless: list it under not checked).
     Continue the same inspector with SendMessage; a new one loses what it read.
   - `BLOCKED`, or no report: the group goes under not checked with the reason; do not redo it.
   - If inspectors cannot be dispatched, say in the opening line that the review is not
     independent, then run each group yourself: grep `^summary:` inside `wiki/<group>`, open only
     the pages the code calls for, report only signs you can quote, from pages you opened.

4. **Merge.** Where two groups reach one fragment, open both pages for the owner statement and keep
   the owner's finding. If neither names one, report one finding citing both, say the base does not
   decide, and mark your choice `model opinion`. A finding citing a page outside that inspector's
   pages-opened list is marked `model opinion`. A declined item is dropped if its group ran and
   reported on those lines; otherwise it goes under not checked, group named. No second round.

5. **Spec axis**, when a spec exists: walk each item against the scope — done, done differently,
   not done, unverified. Fold in the inspectors' spec departures; list behaviour no item asks for.

## Report

Open with one line: the scope, the groups run and why, whether the structure holds, whether the
review was independent.

- **Spec axis** — the walk from step 5.
- **Standards axis** — structure first, then by severity. Each: `file:line`, the sign quoted, the
  move, the page, severity, and a flag where a project convention explains the code — reported, not
  called a defect.

Your own observations go in a separate `model opinion` list, never among the standards findings.

Never rank across the axes: a perfect implementation of the wrong thing and a messy one of the right
thing are different news.

**No findings is a valid result**, given per group with what was checked; a padded finding invites
a needless change.

Close with what was not checked: groups dropped and why, blocked groups, uncovered declined items,
unanswered questions, unverified spec items.
