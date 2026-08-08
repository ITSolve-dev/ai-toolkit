---
title: Pruning a document
category: reviewing
summary: Four line-by-line checks that remove load without removing obligation — duplication, material the environment already holds, lost relevance, and instructions the reader would follow anyway.
tags: [method, review, pruning, symptom]
sources: [web-page-writing-for-agents]
created: 2026-08-08
updated: 2026-08-08
---

The only pass in this wiki that is run sentence by sentence rather than against a document as a
whole. Four checks, from [[writing-for-agents-reference]], L96-L99. Each removes text without
touching what the document commits to, which is what separates the pass from
[[the-changeability-test]] and from the cut [[minimal-is-not-short]] forbids.

## 1. Single source of truth

"Keep each meaning in a **single source of truth**: one authoritative place, so changing the
behaviour is a one-place edit" (L96). **Duplication** — the same meaning in more than one place —
"costs maintenance and tokens, and inflates a meaning's prominence on the ladder past its real
rank".

That last cost is the one a reviewer misses. A statement repeated in three sections reads as more
important than it is, and the inflation is invisible from any one of the three.

The source distinguishes it from the deliberate repetition in [[leading-words]]: a leading word
"repeats a token on purpose, never the meaning" (L96).

## 2. The environment is a source of truth too

> The **environment** is a source of truth too — `package.json` scripts, config files, the
> directory layout, `--help` output — and a document that restates it is a **cache**: a copy of a
> lookup, earning its load only when the lookup is expensive. Cache what the agent cannot find by
> looking: the unwritten convention, the reason behind a choice, the gotcha no config confesses.
>
> — L97

This wiki reads the second sentence as the most useful positive statement any of its sources makes.
Every other source here says what to *remove*; this one says what is left when everything
retrievable has been removed — convention, reason, and the trap that is not written down anywhere.
Those three are precisely the things that cannot go stale against a repository, because no
artifact in the repository states them.

It is also [[the-changeability-test]] arriving from a fifth direction. Parnas argues from what
changes over time; this argues from what is discoverable now. The two select the same content for
different reasons, and the second is cheaper to run — a reviewer can check whether a fact is in a
config file, and cannot check whether it will change.

## 3. Relevance

"Check every line for **relevance**: does it still bear on what the document does?" A line loses it
"by never bearing on the task (mere exposition, or a branch that should be disclosed) or by going
stale as the behaviour or world it describes changes" (L98).

Left unrun, the pass has a named consequence: **sediment** — "stale layers that settle because
adding feels safe and removing feels risky, until you must core down through them to find what is
still live" (L98). This wiki notes that sediment is what makes a document *look* comprehensive
while being unusable, and that it is produced by the same instinct that produces the enumeration in
[[canonical-examples-not-edge-cases]].

## 4. No-ops

"An instruction the model already obeys by default pays load to say nothing" (L99). The test —
does it change behaviour versus the default? — is stated as **model-relative, not reader-relative**:
"two people disagreeing about a no-op disagree about the default, and settle it by running the
document, not by debate".

Two consequences the source draws:

- **Delete the whole sentence rather than trim words from it.** A sentence that changes nothing is
  not improved by being shorter.
- **The test grades leading words too.** "A word too weak to beat the default (*be thorough* when
  the agent is already thorough-ish) is a no-op, and the fix is a stronger word (*relentless*), not
  a different technique."

## Running it

The pass is mechanical and belongs late, after the checks that can change what the document says.
Its output is a list of deletions, each with the check that found it — which makes it the one
review pass whose findings need no ranking ([[ranking-findings]]), since every finding is the same
severity and the same repair.

Its honest limit: check 4 cannot be settled from the text. The source says so, and names the
settlement — run the document. A review that has not run it reports a suspected no-op rather than a
confirmed one.

Related: [[sprawl]], the failure that remains after this pass has removed everything it can;
[[the-use-test]], which finds the opposite defect — what the document never said at all.
