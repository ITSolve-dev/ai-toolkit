---
title: Group states that share an outgoing transition
category: types-and-state
summary: "The same transition (same condition, same action, same target state, e.g. `if estop: close(); state = FAULT`) copied into the case arms of several states of one state machine: write it once as a group transition."
tags: [rule, state-machine, automata-based-programming, duplication]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

**State grouping** is a feature of the transition-diagram notation (Polikarpova and Shalyto, p. 69). Suppose several states of one automaton have the same outgoing transition: the same condition, the same output action and the same target state. Those states can then be framed as a group, and the identical arcs replaced by one **group transition**. The source sets the scope of the device: it applies where a set of states is «логически объединен общим поведением, однако выделять эти состояния в отдельный автомат нецелесообразно» (p. 69).

This wiki reads the duplicated transition as a case of duplicated knowledge ([[dry]]).

## Rule

Write a transition shared by several states once, attached to the group, rather than once per state. Choose grouping when the states share behaviour but do not form a sub-machine of their own. Choose a separate automaton when they do (p. 69); this wiki adds that it may be nested or called ([[called-vs-nested-state-machines]]).

## Sign in code

This wiki's own translation: in a `switch` over the state, two or more case arms contain the same branch, the same condition leading to the same action and the same next state, e.g. `if emergency_stop: close_valve(); state = FAULT`. A change to the shared reaction must be made in every arm. If one arm is missed, that state behaves differently without anyone having decided so.

This wiki assigns the shape as follows: a transition identical in condition, action and target across several states of one machine is this page; the same text in two machines is [[dry]]; overlapping guards inside one state are [[transition-conditions-consistent-and-complete]]. An identical transition (condition, action, target) in several states is [[state-grouping-for-shared-transitions]]; a guard on an 'is pressed' flag set and cleared around the machine is [[event-driven-vs-polled-state-machine]].

## When not to apply

- The branches only look alike. The condition, the action or the target differs in one arm, or is expected to differ for a reason in the domain. Then they are separate transitions that happen to be similar ([[coincidental-duplication]]). The source's criterion is identity of all three: condition, output action and target (p. 69).
- The grouped states have enough shared internal behaviour to be a sub-machine. The source then prefers a separate automaton over a group (p. 69); this wiki adds that it may be nested or called.
- The shared branch has to take priority over a state's own branches, or yield to them. Hoisting it then changes the order of evaluation, so the order has to be stated ([[transition-conditions-consistent-and-complete]]). This last limit is this wiki's own.

## Repair

Name the group (as a set, a predicate over the state, or a superstate) and check the shared transition once, before or after the per-state dispatch. Decide explicitly whether the group transition outranks the states' own transitions.

## Before and after

```
// before: the same emergency reaction copied into three states
switch state:
    case OPENING: if estop: close(); state = FAULT; else if opened: state = OPEN
    case OPEN:    if estop: close(); state = FAULT; else if cmd_close: state = CLOSING
    case CLOSING: if estop: close(); state = FAULT; else if closed: state = CLOSED
```

```
// after: one group transition, checked first (it outranks the states' own arcs)
MOVING_OR_OPEN = {OPENING, OPEN, CLOSING}
if state in MOVING_OR_OPEN and estop:
    close(); state = FAULT
else switch state:
    case OPENING: if opened: state = OPEN
    case OPEN:    if cmd_close: state = CLOSING
    case CLOSING: if closed: state = CLOSED
```

## Source

- Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]). State grouping and the group transition, the identity criterion (condition, output action, target), and the choice between a group and a separate automaton: p. 69.
- This wiki's own: the reading as duplicated knowledge, the sign in code and its assignment, the limit on priority, the note that the separate automaton may be nested or called, the repair as code and the pseudocode. The source describes grouping as diagram notation.
