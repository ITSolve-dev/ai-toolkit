---
title: Story Splitting Patterns
category: cutting-work
summary: The three-step procedure and nine patterns for cutting a too-big task into thin vertical slices, each pattern with the trigger that selects it, and Cohn's guidelines with the worked examples the first source lost; data boundaries, exceptional conditions, operations and CRUD, cross-cutting concerns, nonfunctional targets and mixed priority, plus cuts by case of the domain and by rising capability, which buy order and not reduced size, and Vacanti and Seele's cuts by acceptance criterion, customer and assumption. A cut that defers a cross-cutting concern or a nonfunctional target is allowed only if the first version says what it omits, the second exists, and the first is not released alone.
tags: [method, decomposition, splitting, rule, nonfunctional]
sources: [humanizing-work-splitting, kanban-playbook-right-sizing, cohn-agile-estimating-planning, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
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

Cohn gives no order among them. He calls data boundaries "One of the best ways" (L2597), and nothing in the chapter measures any of this: the evidence is his own projects and clients. Exceptional conditions has no guideline sentence of its own: it sits inside the section on data boundaries, and the row is this wiki's. The two cross-cutting rows carry a cost that has its own page, *Deferred Concern Slice* (below).

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

Cohn's example for operations is not CRUD. The search screen was cut into part of the criteria fields with the query builder, then the results grid, then the remaining fields, across three iterations (L2627-L2629). This wiki reads that as: an operation here means a separable piece of behaviour, and CRUD is the common case. The order of those pieces was a decision of its own, on [[ordering-for-early-user-feedback]].

CRUD is also not a formula. The coach's task became add, edit and delete, and Cohn notes that "These stories very closely correspond to the Create, Update, and Delete portions of CRUD." (L2643). Read got no task, and it is not among what the coach was found to want (L2633). This wiki takes from that: the list of tasks comes from what was asked for, not from the four letters.

### Mixed priority: the test

The login example lists three conditions of satisfaction: valid access, lockout after three failed passwords, and an email on lockout (L2683-L2687). The test is what the product owner would ship without:

> She might, however, be willing to release the product without a retry time-out mechanism or without sending an email about the access attempt.
>
> — [[cohn-agile-estimating-planning]], L2689

This wiki reads the question as applicable to a task's acceptance criteria directly: for each criterion, would the person steering accept a release without it? Differing answers mark the cut.

### Worked example: cutting by a case of the domain

The fictional case study in Chapter 23 (L4961) shows a task that looked indivisible. Its figures belong to the fiction. A first game engine is estimated at 20, which the coach calls too big, asking "is there a way to split this story up? Maybe have an even weaker engine the first time?" (L5385). The programmer answers "I don’t see any good ways" (L5387). His one idea is an engine that only attacks, "ignoring the human’s moves", and he rejects it himself (L5387), and the chapter does not give his reason. The opening comes from someone who does not program:

> What if a first engine only recognized rings? […] We could take away bridges and forks—just for now. Allan, couldn’t you write an engine that played offensively and defensively but that only tried to make—and block— rings?
>
> — [[cohn-agile-estimating-planning]], L5389

The result is one story per winning shape, at 8, 5 and 8 (L5401-L5403). This wiki reads the example as a method, which the chapter does not state:

1. Ask what the task must recognize or handle, and list the cases. Here the game has three winning shapes.
2. Take one case and keep the whole behaviour for it. The ring engine still attacks and defends. The rejected idea cut a behaviour and not a case.
3. Add the remaining cases as tasks of their own.

This wiki maps that onto patterns 3 and 4. The sign that it applies, in task text, is a task that names one capability over several parallel cases of its domain. The failure mode is that the cases may not be equal: if the first builds what all the others reuse, the pieces are not independent and their estimates are order-bound ([[independent-tasks]]). The chapter's 8, 5 and 8 carry no such statement.

### Worked example: cutting by rising capability

A large capability can also be cut into steps that each add behaviour to the one before, starting with the unobstructed case and adding opposition, defence and judgement later. The chapter's programmer plans to "first have a move engine that will be smart enough to play six hexagons in a row to make a ring." with no opponent, and then: "Next I’ll write it so that it tries to make a ring even if an opponent tries to block the ring. Then I’ll switch to the defensive side of rings." (L5730).

The bridges story takes the same shape (L5867-L5880): find a path corner to corner, form it around obstacles, know when to give up, block another player, then choose between a bridge and a ring. The hardest judgement comes last and is the largest card, at 16 hours.

The chapter presents this as one programmer's plan at the level below this wiki's task ([[unit-of-work]]). Naming it as a method and using it at the level of a task are this wiki's steps. Stated that way:

1. State the simplest situation in which the capability does something observable.
2. Add one complication at a time: an obstacle, an opponent, a failure, a choice.
3. Attach a check to each step, and test each step against [[size-ceiling]].

This wiki reads it as pattern 1's simple case first, and it differs from the wrong way warned of under pattern 1: each step here leaves something that works, where a cut by process step does not. The sign of a bad result is a step that adds no behaviour a check can see. The case's first card, "Code state management classes" (L5754), is of that kind. This wiki reads it as tolerable there only because the commitment sits on the story ([[commitment-over-a-period]]), so the card is an internal measure. On a board where the task is itself the unit delivered, the same text is a [[component-task-masquerading]] signal.

Test work runs beside each step in the case: "If Allan can give me code after each of the tasks he identified, I can define and automate tests right along with him. Any bugs I find he’ll hear about while the code is fresh in his mind." (L5746). This wiki notes that the stated reason, code fresh in a mind, is a human memory mechanism and does not survive an agent executing. What survives is that a step is cheap to check. Whether test work belongs inside the step for a single executor is an open question this source does not answer.

### Pulling a capability out to open an earlier result

A second kind of cut pulls something shared out of several tasks. Recognizing a winning shape sat inside the engine stories, and the programmer proposes taking it out: "if we pull it out we could do it separately and that would let us write a human vs. human version of the game really quickly while we get the move engine working." (L5463). It becomes a 2-point task, and the engine stories keep their estimates: asked whether they fall, he says "Not really" (L5469).

### What such cuts buy

This wiki reads these cuts together: none of them made the work smaller. The first raised the total from 20 to 21, and the pull-out added 2 with nothing removed. What they bought was order, meaning that a playable result could arrive earlier and that weaker slices could be dropped or postponed. The chapter bears that out, since the pulled-out story is the one dropped at the end of the first iteration (L6223), and two people could still play (L6235). So a cut judged by whether the total fell will look like a failure, and [[estimation-scale]] says why totals are not reconciled. Which cut to prefer is on [[choosing-between-splits]], and the deliberate order of the pieces on [[ordering-for-early-user-feedback]].

### What the guidelines forbid and when they start

Two guidelines in the same chapter say what not to do: do not cut by layer or activity ([[component-task-masquerading]], [[vertical-slice]]), and do not refill a task once it is sized ([[related-changes-temptation]]). [[size-ceiling]] holds the triggers for cutting at all, and [[combining-small-tasks]] the opposite move.

## Vacanti and Seele's cuts

[[flow-metrics-scrum-teams]] offers three cuts for an item found too large, and all line references in this section are to it. Its evidence is that the authors and others have used them (L1230), and it adds that several can apply to one item. The test it holds them to is "faster feedback" (L1230).

| Cut | Trigger | Move | Lines |
|---|---|---|---|
| By acceptance criterion | Several criteria could each be delivered alone | One task per criterion | L1234-L1254 |
| By customer | The text names a whole population or "the customer" | One task per concrete group | L1258-L1280 |
| By assumption | The value rests on claims nobody has checked | One task per assumption, each inside the SLE | L1284-L1316 |

**By acceptance criterion.** The aim is "closer and closer to a 1:1 ratio of acceptance criteria to the PBI" (L1234), with a limit: "This does not mean that every bug, story, experiment, feature or initiative should have only one acceptance criteria." (L1234). The book's example is a paper-review item whose five criteria could each be delivered without the others (L1240-L1254). This wiki reads the sign in text as the one on [[compound-task-text-signs]], with the same limit.

**By customer.** The example is "Enable secure login for employees." (L1262), cut by place of work, country, department or role (L1266-L1274). The book's claim is that a generic customer "increases the size of the work" (L1258), and it adds "Not all customers are equal" (L1280). This wiki reads that as an order as well as a cut, so the narrow group that matters most comes first ([[choosing-between-splits]]). It has no number in the table above. This wiki's sign in text is a plural population with no narrowing, which is the Kanban Playbook's question "For which users?" ([[kanban-playbook-right-sizing]] L45) turned into a cut.

**By assumption.** The question is "what are all the assumptions we’re making about the value of this thing?" (L1286), and each assumption becomes a separately delivered piece. The effort for each "should comfortable fit within your SLE" (L1304). This wiki separates it from a spike by the kind of unknown: a spike asks how to build something, and this asks whether it is worth building ([[ordering-for-early-user-feedback]], [[spike-as-last-resort]]). Like a spike, the task's acceptance is a question answered. That distinction is ours.

This wiki notes the limit for an agent. The book's ladder of evidence runs through conversations, observation, paper prototypes and a Wizard of Oz experiment (L1306-L1312), which are people's work. The plugin can propose the question and cut the task, and a person has to run most of it.

## Agent executor note

The patterns come from coaching human Scrum teams and the guidelines from human teams in two-week iterations, with no measurement behind either. They survive an agent executing because their triggers lie in the work and their purpose lies with whoever reviews it. Only pattern 7's setting depends on people talking in a room, and several of Cohn's triggers surface the same way ("The team talks to the coaches/users", [[cohn-agile-estimating-planning]] L2633). This wiki moves those to the request's text and to clarifying questions, the same transfer it makes for pattern 7, because the plugin runs no meetings.

The case study's detail that the shape idea came from a non-programmer is a remark about a group's mix of views and does not transfer. What does transfer, in this wiki's reading, is that whoever sees the domain's cases can propose a cut the implementer did not, which is a reason for the plugin to read a design document's domain terms when cutting.

## Related

The patterns share one underlying move, which [[choosing-between-splits]] describes and which can be used directly.

The Kanban Playbook's four moves overlap with these, and it adds no new pattern ([[kanban-playbook-right-sizing]] L35-L49). This mapping is this wiki's. Generic terms and plurals point toward patterns 3 and 4. Solving a smaller problem first is pattern 7 and [[choosing-between-splits]]. Its conjunctions and its splitting by acceptance criteria are signs for finding a split rather than patterns, and they are on [[compound-task-text-signs]].

## Deferred Concern Slice

A deferred concern slice is a version of a task built without one of the qualities it will finally need: security, logging, error handling, or a performance or resource target. It is the one cut in *Story Splitting Patterns* (above) that deliberately produces something that should not ship alone. Cohn recommends it with that cost stated.

### The rule

Cut a concern away only if the first version says what it leaves out and a second task carries the concern. This wording is this wiki's, built from Cohn's two guidelines and his marking.

Cohn states the two forms separately:

> Consider removing cross-cutting concerns (such as security, logging, error handling, and so on) and creating two versions of the story: one with and one without support for the cross-cutting concern.
>
> — [[cohn-agile-estimating-planning]], L2665

> Considering splitting a large story by separating the functional and nonfunctional aspects into separate stories.
>
> — [[cohn-agile-estimating-planning]], L2671

Cohn also gives the marking: "The version would clearly note that it is not secure." (L2657). The nonfunctional form extends beyond speed, to a feature that "must consume less than a defined amount of memory, be drawn with fewer than a number of shapes, or use a critical resource for less than a defined amount of time" (L2673).

### When it applies

The concern has to be what makes the task too big. In the login example the password rules were small one by one: "None of this may be particularly time-consuming, but in aggregate it may make the story a little too big to fit in an iteration." (L2657). In the stock chart example, "caching would be a significant part of the effort" (L2669), so it became its own task in the next iteration.

This wiki reads the condition as a limit: a task that fits gets no such cut, since the cut exists only to reach a size. [[size-ceiling]] decides that.

### Observable signs

The signs are this wiki's reading of Cohn's marking and of his two-versions wording.

- **In task text:** a task's result omits a concern the request names, and the task does not say so.
- **On the board:** the first version is present and the second is not, so the omission is recorded nowhere that anyone will schedule.
- **In board history:** a release includes the first version while the second is still open. A sign raises a question, and the check is whether anyone decided that on purpose.

### Cost

Cohn is direct: "You probably would not choose to release the product with only the first story supported, but there may be value in splittng the stories in this way." (L2657). The search example shows how far the first version can go: "Their solution was to ignore this security restriction and in the first iteration on this feature users could see the entire result set." (L2653). That passage does not say whether this version ever reached real users, and this wiki reads it as acceptable only if it did not.

This wiki therefore reads the first version as possibly a [[vertical-slice]] and still not finished work. The Humanizing Work trap on pattern 8 of *Story Splitting Patterns* (above) is the same risk, and the same remedy applies: each half gets its own acceptance check, per [[testable-acceptance]]. A deferred concern is also a sequence between two tasks and not a wait, per [[sequence-versus-wait]].

The chapter does not discuss the cost of adding a concern later to code built without it. Its own citation points the other way, Kernighan and Plauger's "Make it work then make it faster." (L2669), and it is given second-hand with no measurement.

### Agent executor note

The evidence is Cohn's own projects, with no measurement. The rule survives an agent executing, and this wiki expects the marking to matter more with one: a person who built the insecure version remembers it, and an agent working the next task knows only what the task says, as [[recoverable-versus-task-only-facts]] sets out. The omission has to be written where the next executor will read it.
