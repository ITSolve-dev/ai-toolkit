---
title: The Conversation Moves Into the Task
category: task-content
summary: What a human team settles by talking during development has to be settled before an agent starts and written into the task; a text that points at a conversation or at memory is the sign it was not.
tags: [rule, task-content, agents, readiness, invest]
sources: [wake-invest, ambig-swe, humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-01
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

The signs are this wiki's. Neither source states them.

## When to do it

The rule does not ask for detail early. Wake says the notes are not needed for ordering: "Over time, the card may acquire notes, test ideas, and so on, but we don’t need these to prioritize or schedule stories." ([[wake-invest]] L54). The Humanizing Work authors describe the same movement: "as the collaboration happens and you capture more detail, the story becomes less negotiable" ([[humanizing-work-splitting]] L113). This wiki reads the two together with the staging on [[invest]]: a task far from starting stays thin and open, and it closes as it approaches the start. The deadline for closing it is the moment an agent would take it.

## Cost

The person steering pays in writing time, before the work. The Ambig-SWE authors note of interactive workflows that "these workflows can burden users, highlighting the need to minimize intervention to essential cases" ([[ambig-swe]] L250). Where a decision cannot be made in advance because the work itself will reveal it, the answer is a smaller first slice and not a longer task ([[how-far-to-split-up-front]]).

## Agent executor note

This page exists because the human mechanism does not survive. Wake's card works for a person who can ask. For an agent, the card is the whole brief.
