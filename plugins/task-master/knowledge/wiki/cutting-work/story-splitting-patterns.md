---
title: Story Splitting Patterns
category: cutting-work
summary: The three-step procedure and nine patterns for cutting a too-big task into thin vertical slices, each pattern with the trigger that selects it, and Cohn's guidelines with the worked examples the first source lost; data boundaries, exceptional conditions, operations and CRUD, cross-cutting concerns, nonfunctional targets and mixed priority.
tags: [method, decomposition, splitting]
sources: [humanizing-work-splitting, kanban-playbook-right-sizing, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Story Splitting Patterns

This is the Humanizing Work procedure for cutting a task that is too big. Run it on a request or a task before it reaches a board. The authors' example stories were lost in extraction ([[humanizing-work-splitting]]), so this page keeps the triggers and the moves and does not reconstruct the examples. Cohn's guidelines, further down, have their examples intact.

## The procedure

1. **Make the input a real increment of value.** The authors say to start by checking the input against [[invest]], "(other than small)" (L183). If it fails on value, go to [[component-task-masquerading]] and combine it.
2. **Ask whether it is too big.** That is the question [[size-ceiling]] answers. If it is too big, apply the patterns in the table below.
3. **Choose among the possible splits**, using [[choosing-between-splits]].

## The patterns

The authors number the patterns, and the spike comes last by design. All line references are to [[humanizing-work-splitting]].

| # | Pattern | Trigger | Move | Lines |
|---|---|---|---|---|
| 1 | Workflow steps | The task hides a multi-step process | Build the simple end-to-end case first, then add the middle steps and special cases | L193-L209 |
| 2 | Operations | The word "manage", or several operations under one name | One task per operation | L215 |
| 3 | Business rule variations | A general phrase hides several rules of similar weight | One task per rule | L225-L231 |
| 4 | Variations in data | Complexity comes from kinds of data | Build the simplest version and add variations as they appear; list them up front when they are already known | L235-L253 |
| 5 | Data entry methods | Complexity is in the interface and not in the function | Simplest possible interface first, the richer one second | L257 |
| 6 | Major effort | Most of the work goes into whichever part comes first | One task for any one of them, and one task for the rest, given one is done | L265-L271 |
| 7 | Simple/complex | The task grows as it is discussed | Capture the simplest version, and move every variation into its own task | L275-L285 |
| 8 | Defer performance | Much of the effort is in making it fast, secure or scalable | "Make it work", then "make it fast" | L289-L297 |
| 9 | Break out a spike | The implementation is poorly understood | See [[spike-as-last-resort]] | L301-L309 |

## Points the table cannot carry

**Pattern 1 has a wrong way.** The natural cut, one task per step, is what the authors warn against:

> Either way, the most obvious split—one step at a time from beginning to end—is the wrong way to go.
>
> — [[humanizing-work-splitting]], L209

The authors' reason is that "the biggest value often comes from the beginning and end. The middle steps add incremental value, but don’t stand alone." (L195). When the whole workflow matters, their alternative is "a thin slice through the whole workflow" (L207). The sign in a cut is a list of tasks named after successive steps of one process.

**Pattern 8 has a trap.** The authors warn: "It’s easy to get in a habit of calling stories done that aren’t really done, accumulating debt you’ll pay for later." (L297). This wiki reads that as a reason to give both halves their own acceptance check, following the authors' "(in under 5 seconds)" (L293), per [[testable-acceptance]].

**Patterns 5 and 6 leave a dependency in place.** The authors say so at L257 and L271, and that is accepted. [[independent-tasks]] records why it is acceptable.

**Pattern 7's trigger is a meeting.** The authors place it "in a planning meeting" (L275), with the signs “what about x?” and “have you considered y?”. The plugin runs no meetings, so this wiki moves the trigger to text: a request or a clarification thread that keeps adding "what about" items.

## Cohn's guidelines

Cohn's chapter on splitting offers guidelines for a task too big to fit its iteration, each drawn from an example ([[cohn-agile-estimating-planning]] L2579). His examples are intact, which matters here because the Humanizing Work examples were lost in extraction. Cohn's "story" is this wiki's task. His "task" is a step one level below that, which is why [[component-task-masquerading]] applies to it. His "product owner" is the person steering. All line references from here to the agent note are to [[cohn-agile-estimating-planning]].

| Guideline | Trigger | Move | Example | Lines |
|---|---|---|---|---|
| Data boundaries | One task covers many fields, kinds or levels of detail of data | One task per type or level of data | Balance sheet entry; U.S. and international fax numbers | L2597-L2613 |
| Exceptional conditions | Discussion adds an exception to the main path | Main task tolerates the case, a second task handles it | Loan overpayment refund over ¤2 | L2615-L2621 |
| Operations | One task covers several operations, or the parts of one operation | One task per operation | Complex search screen | L2625-L2631 |
| CRUD | A word such as "manage" hides create, edit and delete | One task per operation actually wanted | "As a coach, I can manage the swimmers on my team." | L2633-L2645 |
| Cross-cutting concerns | Security, logging or error handling adds the size | Two versions, without and with the concern | Privileged screens; login | L2649-L2665 |
| Functional and nonfunctional | A performance or resource target adds the size | Separate the target into its own task | Stock chart caching | L2669-L2673 |
| Mixed priority | Conditions of satisfaction differ in priority | Cut along the difference | Login, lockout, alert email | L2677-L2691 |

Cohn gives no order among them. He calls data boundaries "One of the best ways" (L2597), and nothing in the chapter measures any of this: the evidence is his own projects and clients. Exceptional conditions has no guideline sentence of its own: it sits inside the section on data boundaries, and the row is this wiki's. The two cross-cutting rows carry a cost that has its own page, [[deferred-concern-slice]].

This wiki maps them onto the numbered patterns above. Data boundaries is pattern 4, CRUD and operations are pattern 2, functional and nonfunctional is pattern 8, and exceptional conditions is closest to pattern 7. Cross-cutting concerns widens pattern 8 from making a thing fast or secure to logging and error handling. Mixed priority has no number: it is the first test of [[choosing-between-splits]] used as a way to find a cut.

### Worked example: cutting by data

The balance sheet task started as "As a user I can enter my balance sheet information." (L2597). The team cut it in order of depth:

1. Summary data: the form and two fields, "very small (almost too small)" (L2599).
2. Categorized data, which brought two dozen input fields (L2599, L2605).
3. Validation, with the rules agreed: positive and negative amounts allowed, decimals rounded to the nearest dollar (L2605).
4. Detailed loans, up to 100 of them (L2607).
5. The same for real estate, cash and the rest: "The loan story was used as a pattern for many other user stories that were split from the original" (L2607).

The result was that "the team created about a dozen user stories from the initial one" (L2609), each well inside a two-week iteration. This wiki draws two points from it. The first of a family was the largest piece and the rest followed it, which is pattern 6, major effort. And the bound of 100 loans was "discussed, agreed to, and noted as a condition of satisfaction on the story card" (L2607), so a split that sets a limit has to write it into the task, per [[conversation-moves-into-the-task]].

### The main path keeps what it must tolerate

In the loan example the first task reads "As a borrower, I want to pay off my loan. Note: Allow overpayments." (L2617). This wiki reads the note as the part that makes the cut safe: removing an exception from a task does not mean the main path may fail on it, so the task says what it has to accept until the second task arrives.

### Operations is wider than CRUD

Cohn's example for operations is not CRUD. The search screen was cut into part of the criteria fields with the query builder, then the results grid, then the remaining fields, across three iterations (L2627-L2629). This wiki reads that as: an operation here means a separable piece of behaviour, and CRUD is the common case. The order of those pieces was a decision of its own, on [[uncertain-piece-goes-earlier]].

CRUD is also not a formula. The coach's task became add, edit and delete, and Cohn notes that "These stories very closely correspond to the Create, Update, and Delete portions of CRUD." (L2643). Read got no task, and it is not among what the coach was found to want (L2633). This wiki takes from that: the list of tasks comes from what was asked for, not from the four letters.

### Mixed priority: the test

The login example lists three conditions of satisfaction: valid access, lockout after three failed passwords, and an email on lockout (L2683-L2687). The test is what the product owner would ship without:

> She might, however, be willing to release the product without a retry time-out mechanism or without sending an email about the access attempt.
>
> — [[cohn-agile-estimating-planning]], L2689

This wiki reads the question as applicable to a task's acceptance criteria directly: for each criterion, would the person steering accept a release without it? Differing answers mark the cut.

### What the guidelines forbid and when they start

Two guidelines in the same chapter say what not to do: do not cut by layer or activity ([[component-task-masquerading]], [[vertical-slice]]), and do not refill a task once it is sized ([[related-changes-temptation]]). [[when-to-split-a-task]] holds the triggers for cutting at all, and [[combining-small-tasks]] the opposite move.

## Agent executor note

The patterns come from coaching human Scrum teams and the guidelines from human teams in two-week iterations, with no measurement behind either. They survive an agent executing because their triggers lie in the work and their purpose lies with whoever reviews it. Only pattern 7's setting depends on people talking in a room, and several of Cohn's triggers surface the same way ("The team talks to the coaches/users", [[cohn-agile-estimating-planning]] L2633). This wiki moves those to the request's text and to clarifying questions, the same transfer it makes for pattern 7, because the plugin runs no meetings.

## Related

The patterns share one underlying move, which [[find-core-complexity]] describes and which can be used directly.

The Kanban Playbook's four moves overlap with these, and it adds no new pattern ([[kanban-playbook-right-sizing]] L35-L49). This mapping is this wiki's. Generic terms and plurals point toward patterns 3 and 4. Solving a smaller problem first is pattern 7 and [[find-core-complexity]]. Its conjunctions and its splitting by acceptance criteria are signs for finding a split rather than patterns, and they are on [[compound-task-text-signs]].
