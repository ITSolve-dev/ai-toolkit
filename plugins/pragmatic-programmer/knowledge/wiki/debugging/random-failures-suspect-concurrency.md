---
title: "Random failures: suspect concurrency"
category: debugging
summary: "Failures that appear at arbitrary places, between runs, with symptoms that contradict the state on disk, often after work became concurrent: look for what the failing code shares, including process-wide state."
tags: [method, debugging, concurrency, intermittent-failures]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A way to narrow down failures that move around. The book's tip reads: «Случайные отказы часто вызваны осложнениями, возникающими в связи с параллельностью» (p. 225). It is a specialised branch of [[debugging-procedure]] for the case where the failure will not stay in one place.

## The case

The authors changed their toolchain to do more work in threads. The build then failed in odd ways and at arbitrary places. What the failures had in common was that files or directories could not be found although they were exactly where they should be. The authors traced this to two places in their code that temporarily changed the current directory. «В нераспараллеленной версии кода обратное восстановление каталога было вполне приемлемым» (p. 225), but in the threaded version one thread changed the directory while another ran assuming the original one (p. 225).

## Procedure

The book gives the case and the tip. This procedure is this wiki's own generalisation of how that case was solved.

1. Collect several failures and ask what they share, instead of chasing each site. In the book's case the common symptom pointed to the cause; the failing locations did not.
2. Look for a contradiction between the error and the actual state, such as a file reported missing that is present. It suggests the code saw a different view from the one inspected afterwards.
3. Ask whether something recently became concurrent.
4. List what the failing code depends on beyond its own locals, including process-wide state: current directory, environment, shared files, connections, caches.
5. Search for temporary changes that are set and then restored. They are invisible sequentially and visible to everyone else when concurrent.
6. Test the suspicion by forcing one worker. If the failures go away the suspicion is supported, not proven, since timing changed too.
7. Fix by removing the sharing, as in [[shared-state-is-incorrect-state]], not by adding a retry or a delay. See [[fix-the-root-cause]].

## Limits

The book says often, not always. This wiki adds that randomness also comes from time, from unordered collections, from uninitialised data and from the network. This wiki also holds that a failure surviving step 6 rules out only sharing inside the process. The book counts files, databases and external services among shared resources too (p. 225), so check what the code shares with other processes before looking elsewhere.

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: the case, the tip and the list of shared resources, p. 225.

This wiki's own: the numbered procedure, the alternative sources of randomness and what a failure surviving step 6 does and does not rule out.

Related: where an intermittent failure on identical input comes from state the code never set rather than from timing, [[perturb-state-to-expose-uninitialized-data]] makes it reproducible.
