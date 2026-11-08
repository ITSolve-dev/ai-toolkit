---
title: State machine, event stream or publish-subscribe
category: types-and-state
summary: "A state machine with states counting events plus timestamp fields, or a stream used only to fan out: pick the tool by what must be remembered."
tags: [decision-rule, state-machine, events, publish-subscribe, streams]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Three ways of reacting to events suit different jobs. The book's answer works through several behaviours and shows that the obvious choice can be harder than it looks: a condition that looks like a state machine can be simpler over a stream (pp. 356-357). The book offers these as likely choices and not verdicts. The strategies themselves are mapped on [[event-driven-code]].

## Rule

Decide by what the logic has to remember and by how many receivers there are.

| The behaviour needs | Likely fit | The book's case |
|---|---|---|
| A condition over a window of recent events and their times | Event stream | Three network-interface failures within five minutes |
| Several independent reactions, each following its own sequence | Publish-subscribe delivering to state machines | Motion at the bottom and then the top of the stairs after sunset turns the lights on |
| Notifying several unrelated receivers | Publish-subscribe | Telling accounting systems that an order was fulfilled |
| Waiting for responses to several concurrent requests | Event stream | Three backend requests |

The book's reasoning for the first row is a schedule. Events at minutes 1, 4, 7 and 8 must raise a warning on the fourth event, and the machine must «сбросить себя в исходное состояние» (p. 357). This wiki spells out why that is hard: minutes 1 to 7 span six minutes, so nothing fires, yet minutes 4 to 8 fall inside the window, so a machine that simply clears itself on a failed check has already lost the events it needs. Its state would have to hold the window. A stream's `buffer()` takes `size` and `offset`, yields each group of three, and leaves only a comparison of the first and last timestamps (p. 357).

For the third row the book warns that streams would work, but the notified systems would then have to be designed around streams as well (p. 357).

## Sign in code

- A state machine with states named after a count, such as `one_failure` and `two_failures`, and timestamp fields beside the state.
- Transition code that discards a remembered event and then needs it again.
- A stream whose subscribers do nothing but forward each event to a separate system, with no windowing or joining.

## When not to apply

The book states no limits here. The limits below are this wiki's own.

- The project has no stream library, and adding one would serve one window. A short list of the last N timestamps gives the same result with no dependency, and that is the repair then.
- The condition depends only on the order of distinct kinds of event, with no time window or count. A state machine stays the simpler form. See [[finite-state-machine]].
- The whole set of reactions is one synchronous call chain inside one module. None of the three is needed.

## Repair

1. Write what the logic must remember between events.
2. If that is a recent window, replace counting states with a window of N events, sliding by one. See [[event-stream]].
3. If the machine's job is only delivery, replace it with publish-subscribe, and keep state machines at the receivers that follow a sequence. See [[observer-vs-publish-subscribe]].

## Before and after

Before: on failures at minutes 1, 4, 7 and 8 this never alerts.

```
state = IDLE
on failure(t):
    if state == IDLE: first = t; state = ONE
    else if state == ONE: state = TWO
    else if state == TWO:
        if t - first <= 5 minutes: alert()
        state = IDLE
```

After: the same input alerts on the failure at minute 8.

```
on window of last 3 failures, sliding by 1:
    if window.last.time - window.first.time <= 5 minutes:
        alert()
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), answer to exercise 20, pp. 356-357. The cases, the choices, the schedule and the `buffer()` solution are the book's. The table's general wording, the explanation of why a reset fails, the signs, the limits, the repair and the pseudocode are this wiki's own.
