---
title: The Conversation Moves Into the Task
category: task-content
summary: What a human team settles by talking during development has to be settled before an agent starts and written into the task; a text that points at a conversation or at memory is the sign it was not. Its failure afterwards is a fact stranded outside the task: a decision known and recorded in a comment or chat, contradicting the task's text or fields, which practitioners called problematic with no one disagreeing.
tags: [rule, task-content, agents, readiness, invest, failure-mode, evidence]
sources: [wake-invest, ambig-swe, humanizing-work-splitting, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-02
---

# The Conversation Moves Into the Task

Whatever a human team would settle by talking during development has to be settled before an agent starts, and written into the task. This page is a connection between sources and no source states it. Wake's account of a story assumes a conversation, and Ambig-SWE shows that an agent does not reliably start one. The rule is this wiki's conclusion from the two.

## What the human case assumes

Wake's story is deliberately incomplete, because the rest is expected later:

> Story descriptions can be small too (and putting them on an index card helps make that happen). Alistair Cockburn described the cards as tokens promising a future conversation. Remember, the details can be elaborated through conversations with the customer.
>
> — [[wake-invest]], L72

This wiki reads a card as an IOU, and the same reading applies to Wake's Negotiable letter ([[invest]]): "details will be co-created by the customer and programmer during development" ([[wake-invest]] L54). The card is safe to leave thin only because someone will collect on it.

## What changes with an agent

The study behind [[ambig-swe]] gives two findings. Both hold for its six models on stripped issues with a simulated user, with the conditions recorded on that page.

- **The agent does not call in the IOU.** "Without compulsory interaction, the model defaults to non-interactive behavior for most issues, as seen in the Hidden setting." ([[ambig-swe]] L148). See [[agent-silence-is-not-completeness]].
- **Even compulsory clarification does not catch up with a complete task.** The authors report: "The performance gap between the Interaction and Full settings is also significant across all models, highlighting the unrealized potential." ([[ambig-swe]] L155).

This wiki reads the second finding as the strongest reason for the rule: of the two ways to give an agent the information, having it in the task beat obtaining it during the run for every model tested.

## The rule

Before an agent starts, every decision the task depends on is either made and written down, or explicitly left to the executor. A later conversation is not a place to put a decision.

## Sign of violation

- **In task text:** the text refers to a conversation or to memory it does not contain: "as discussed", "TBD", "details to follow", "the usual way", "handle edge cases appropriately". These words exist in the text, so this sign does not rest on a missing field.
- **In board history:** a task reworked after completion over a decision the text left open.
- **In the task's comments or elsewhere:** the decision was made and never reached the text (*Fact Stranded Outside the Task* (below)).

The signs are this wiki's. Neither source states them.

## When to do it

The rule does not ask for detail early. Wake says the notes are not needed for ordering: "Over time, the card may acquire notes, test ideas, and so on, but we don’t need these to prioritize or schedule stories." ([[wake-invest]] L54). The Humanizing Work authors describe the same movement: "as the collaboration happens and you capture more detail, the story becomes less negotiable" ([[humanizing-work-splitting]] L113). This wiki reads the two together with the staging on [[invest]]: a task far from starting stays thin and open, and it closes as it approaches the start. The deadline for closing it is the moment an agent would take it.

## Cost

The person steering pays in writing time, before the work. The Ambig-SWE authors note of interactive workflows that "these workflows can burden users, highlighting the need to minimize intervention to essential cases" ([[ambig-swe]] L250). Where a decision cannot be made in advance because the work itself will reveal it, the answer is a smaller first slice and not a longer task ([[how-far-to-split-up-front]]).

## Agent executor note

This page exists because the human mechanism does not survive. Wake's card works for a person who can ask. For an agent, the card is the whole brief.

## Fact Stranded Outside the Task

A fact is stranded when it is known and written down, and the task does not show it. It breaks the question of what a task must carry: the task is out of date and it does not look out of date. The smell's definition gives the plain case: "In the comments, someone has referenced a property and the value it should be, but not updated it in the property. For example, “This ticket is now closed”, but the status of the ticket remains open." ([[montgomery-tracker-smells]] L179).

This is the one smell the discussion reports as unrefuted (L765):

> The smell “properties discussed in the comments but not updated in the issue” was declared as problematic by 12 participants and not refuted by any participant. This smell is particularly problematic because it describes when information is known (and often reported somewhere), but is not recorded in the issue. Therefore, there is a known inconsistency, but it will be unknown to people who only have the information in the issue.
>
> — [[montgomery-tracker-smells]], L765

The study also shows a wider form of the same failure. Ten participants described information spread across systems, as in P20's note "multiple sources of truth: Slack, Jira, etc." (L472). And among the causes of missing information is that it may be "stored inside other communication tools such as Mattermost" (P19, L443). The study also lists the link version of the smell, a known link mentioned in comments but not documented (S2.4, L190), with no result in the text.

### Sign

- **In a task's comments:** a comment states a status, a value or a decision that the task's fields or text do not show.
- **In task text:** it points at another place for a decision: a chat, a call, a thread. This overlaps with the sign at the top of this page.
- **In board history:** a task's result followed a decision that appears only in a comment.

These wordings are this wiki's, from L179 and L765.

### What this sign does not establish

- That the task is misleading anyone in this project. A team may read comments as a matter of course. The study says some teams put everything in the description instead, and "no comments means everything is well" for another (L520).
- How often it happens. Twelve people called it a problem in an interview, which is a perception.
- That the fact should have been copied. A link to a decision record is not stranded. Writing decisions down at length is `spec-driven-guide` work, and the point here is only that the task must show the result.

### Remedy

Move the fact into the task, or update the field. The authors' account of the reasons includes "laziness, assumption of responsibility on someone else, and reliance on external tools for discussion" (L765), and this wiki keeps the third, which is a matter of where work happens. Their proposed tool, which would detect keywords in a comment, is out of scope.

### Agent executor note

This failure gets worse with an agent, and the mechanism is the one the authors name. The authors' "people who only have the information in the issue" (L765) describes an agent's normal position, while a person on the team has usually seen the chat. An agent given a task and not its comments works from a stale brief. An agent that does read comments still has to weigh them against the text, and nobody here tests how well it does. So the plugin should treat a comment that contradicts a task as something to resolve before the task starts. The agent case is this wiki's reading. The study has no agent in it.
