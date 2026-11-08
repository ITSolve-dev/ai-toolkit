---
title: Finite state machine as a transition table
category: types-and-state
summary: "A loop over messages, events or characters sets and tests several boolean flags to track where it is in a sequence; legal orderings are implicit in nested conditionals."
tags: [rule, state-machines, events, transition-table]
paradigm: any
sources: [pragmatic-programmer, automata-based-programming]
created: 2026-11-01
updated: 2026-11-06
---

A finite state machine is, in the book's words, «всего лишь спецификацией порядка обработки событий» (p. 177). It consists of a set of states, one of them current. For each state it lists the events that matter there, and for each of those events it gives the next state (p. 177).

The authors say state machines are not hard to use, and that developers are set against them, probably believing that they are too complicated, that they apply only to hardware, or that they need an obscure library. One of the authors reports writing one nearly every week, often in a couple of lines (p. 177).

## Rule

Where the meaning of an event depends on what came before it, write the allowed orderings down as data, in a transition table, and drive it with a small loop. «КА примечательны тем, что их можно выразить исключительно как данные.» (p. 178)

In the table, rows are states, columns are events, and the cell is the next state (p. 178). The loop looks up the cell for the current state and event, and any pair with no entry goes to an error state (p. 178). This is why the form pays, in this wiki's reading: an illegal ordering needs no separate check, because it is simply absent from the table.

A pure machine is a parser of an event stream whose only output is its final state. It gains output by attaching actions to transitions, so a cell holds the next state and an action name, and the loop dispatches on that name before going round again (pp. 179-180). The book's other variations (p. 180):

- a default transition for events a state does not name
- functions or function pointers in the table in place of action names
- wrapping the machine in its own class

The same move on non-sequential cases is [[drive-repeated-dispatch-from-a-table]].

## Sign in code

This sign is this wiki's own, since the book names none.

A loop reads a sequence of events, messages or characters, and its branches both test and assign state held outside the loop body: two or more boolean flags such as `in_string`, `escaped`, `seen_header`. Legal orderings can be recovered only by reading nested conditionals.

This wiki assigns the neighbouring cases as follows. A record of nullable fields and status flags whose own methods test them in combination is [[replace-flags-with-explicit-states]]; one tested by functions outside its owner is [[status-variable-as-enumeration]]; one whose inputs can arrive in any order, or where a fact raises new work, is [[blackboard]]. Code that already holds the mode in one state variable but does not mirror the transition graph is [[state-machine-as-switch-on-state]]. Whether a state machine's transitions are held as a table or as a switch is [[state-machine-table-or-switch]]. [[drive-repeated-dispatch-from-a-table]] owns a branch on a key with no state behind it. A single status boolean or enum read by functions outside its owner, with no loop or sequence behind it, is [[status-variable-as-enumeration]]. Flags held as fields of one entity and tested in combination by several of its own input handlers to choose a reaction are [[replace-flags-with-explicit-states]]; flags that one loop over a sequence of events sets and tests to track its place in that sequence are [[finite-state-machine]].

## When not to apply

- The book says state machines do not solve every event-handling problem (p. 181). See [[event-driven-code]] for the alternatives.
- A machine is the harder tool when events must be combined over time. The book's answer to exercise 20 takes three failures within five minutes: with events at minutes 1, 4, 7 and 8, the alert belongs on the fourth, so a machine would have to reset itself, and event streams are the likely choice (pp. 356-357). That shape belongs to [[event-stream]], and [[state-machine-or-event-stream-or-pubsub]] holds the decision.
- *Automata-Based Programming* recommends the opposite form: a switch on the state with one guarded branch per transition, keeping tables for automata changed at run time (pp. 79-80 of that book; [[state-machine-as-switch-on-state]]). Its table is indexed by the full input vector and grows exponentially with the inputs (p. 79), while this book's is indexed by state and event type. This wiki resolves it per setting: where every transition is keyed by the state and an event type alone and its action is a name, the table of [[finite-state-machine]] is the shorter form; where transitions are guarded by conditions over several inputs, or carry priorities, or where each event reaches the machine through its own handler or event method (*Automata-Based Programming*, pp. 88-89), the switch with one guarded branch per arc of [[state-machine-as-switch-on-state]] is the form. A project convention on state-machine form overrides both.
- This wiki adds that a single flag with one transition does not earn a table, since a conditional reads better. Nor does the rule apply where order does not matter and each event is handled alike.

## Repair

1. List the states the flags were encoding, and name them.
2. List the event types the loop distinguishes.
3. Write the table, with an entry only for legal pairs.
4. Replace the conditionals with one lookup, sending missing entries to an error state.
5. Move side effects into named actions attached to transitions.

For a workflow that stretches over many interactions, such as signing up a user through several steps, the book recommends keeping the state in external storage and using it to drive the machine (p. 180).

Trade-off, as this wiki states it: the table separates the ordering from the code that runs, so a reader follows one more indirection to learn what an action does.

## Before and after

```
// before: legal order is scattered through flags
greeted = false
authed = false
closed = false
failed = false
while not closed and not failed:
    msg = nextMessage()
    if msg.type == HELLO:
        if greeted: failed = true
        greeted = true
    else if msg.type == AUTH:
        if not greeted or authed: failed = true
        authed = true
    else if msg.type == DATA:
        if not authed: failed = true
        store(msg)
    else if msg.type == BYE:
        if not authed: failed = true
        closed = true
    else:
        failed = true
```

```
// after: legal order is the table, and anything else is an error
TRANSITIONS = {
    start:   { HELLO: (greeted, ignore) },
    greeted: { AUTH:  (open, ignore) },
    open:    { DATA:  (open, store), BYE: (done, ignore) },
}
state = start
while state is not done and state is not error:
    msg = nextMessage()
    (state, action) = TRANSITIONS[state][msg.type] or (error, ignore)
    run(action, msg)
```

## Source

[[pragmatic-programmer]], Topic 29, Russian edition, pp. 177-181: the definition, the table form, the lookup loop with its error default, actions, variations, external state, and the note that machines do not solve everything; pp. 356-357 for the answer to exercise 20. This wiki's own: the rule's condition that an event's meaning depends on what came before it, the sign, the assignment of neighbouring cases (the status-flag record, a held state variable, table or switch), the reading of why a missing entry is valuable, the assignment against [[replace-flags-with-explicit-states]], the resolution against [[automata-based-programming]] (whose claims, including the event-handler setting of pp. 88-89, are cited to that book's pages), the third limit, the repair steps, the trade-off and the example. A sentence on p. 177 as printed reads «Ни одно из этих мнений неверно», literally that none of these views is wrong; the sentence before it says state machines are not hard to use, and this page takes that as the authors' position. A sentence on p. 180 as printed says transitions must be handled at the same time; its own signup example describes the opposite, and this page follows the example.
