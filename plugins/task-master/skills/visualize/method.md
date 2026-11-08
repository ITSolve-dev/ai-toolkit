# visualize: method

A question in; one chart that answers it, as a Mermaid file, and a short text reading. The chart is
chosen by the question, not by the occasion. Read the question file first: it names the scope, the
reader, the setup and the obligations met by a fallback. Start from
`wiki/showing-work/which-chart-for-which-plan-question.md`: its tables map questions to charts,
and its "Cannot ask" column says what each chart cannot answer.

## Inputs and output

- **Passed:** the snapshot, its metrics file or files, the question file.
- **Every number in the chart is copied from the metrics**, with its basis; which tasks a bar or
  node holds, their sprints and the sprint dates, come from the snapshot. A series the metrics lack,
  or refuse with a `reason`: refuse the chart, naming the series and that reason.
- **Output:** the chart at `.task-master/visualize-<slug>.mmd`; `findings` holds its path and the
  reading. A refusal writes no file and says why. Publishing goes to `needs_caller`. No changeset.

## The charts

One snapshot is one moment and cannot stand in for history. The "Reads" column is how each chart is
built from this plugin's metrics (not from the base).

| Chart | Answers | Reads |
|---|---|---|
| Iteration burndown | Will this period's work finish? | `series.burndown` (`--sprint`): finish times and estimates, membership as of now |
| Release burndown, line | How far along is the release? | One snapshot per period start, each compared to the first: `comparison.forces.residual.points` per run |
| Release burndown, bars | Why did remaining work move? | `comparison.forces` between two period starts |
| Velocity | How much fits by a date, at what rate? | `velocity.periods`; by count without estimates |
| Parking lot | Which themes are behind? | Not available: the settings keep no theme field; refuse, naming it |
| Feature Gantt | What is planned for which period? | The snapshot's sprint on each task; sprint dates |
| Cumulative flow | Average time? More starting than finishing? | `series.cfd`: every item's transitions |
| Cycle time scatterplot | How long may one item take? Did it change? | `series.scatterplot` |
| Cycle time histogram | What shape is the data, how long the tail? | `series.histogram` |
| Aging view | What is open now, and how old? | `age.items[].work_item_age_days` of started open items; `cycle_time.percentiles` as lines (`wiki/reading-history/work-item-age.md`, How to read it) |

## Process

1. **Map the question to a row** of the which-chart page.
   - A chart named instead of a question: state the question it answers; if the caller's question
     is another, name the chart that answers that one.
   - No row fits: no chart; the question goes to `not_covered`. Never offer the nearest chart.
   - A date for a set of items is a forecast (`schedule`); plan against fact is `review-period`.
2. **Fit the setup and the reader.** Flow has no burndown or velocity: go to the cycle time rows
   (which-chart page, Flow setup). An outside reader gets count or elapsed time, never points
   (`wiki/showing-work/points-or-time-and-count.md`). Periods under two weeks: say an iteration
   burndown is probably not worth drawing (`wiki/showing-work/iteration-burndown.md`).
3. **Check the data; refuse what it cannot support.** Hold the row's "Reads" against the metrics.
   Unmet: refuse, naming the input and the obligation that lacks it, and say which question can
   still be answered. Nothing is approximated: a cumulative chart from column counts is "dubious"
   (`wiki/showing-work/cumulative-flow-diagram.md`, Building it), and a burndown from one snapshot
   is one point. Null `work_item_age_days`: no aging view; the reading may list `days` labelled by
   its `basis`. Few finished items: the scatterplot over the histogram, read dot by dot.
4. **Draw one chart.** Several views at once bury the answer (which-chart page, Failure modes).
   - Open with `%%` comment lines: the question, the snapshot's `taken_at` and `source`, each
     series' basis, and what the chart cannot answer.
   - A cumulative line never falls (cumulative-flow-diagram, Signs that a chart is not a CFD); a dot
     sits at its item's finish date (`wiki/showing-work/cycle-time-scatterplot.md`); a Gantt bar
     spans its whole period and shows no progress.
5. **Name the Mermaid type and what it loses** (Mermaid's limits are not in the base):

   | Chart | Mermaid | Lost |
   |---|---|---|
   | Burndowns, velocity | `xychart-beta`, line or bar | No legend: series are named in the reading; scope change below the axis goes as a table |
   | Cumulative flow | `xychart-beta`, one line per state | Bands unfilled; dates are categories, so list every day |
   | Scatterplot | `xychart-beta`, one bar per item by finish date, percentiles as flat lines | The x axis is order, not time; gaps vanish |
   | Histogram | `xychart-beta`, bars per cycle time band | Percentile lines go in the reading |
   | Aging view | `xychart-beta`, one bar per open item, states as label prefixes | States are labels, not columns |
   | Feature Gantt | `gantt`, a section per period | Nothing the question needs |

   No other diagram type, `pie` included, answers a question here.
6. **Write the reading.** Conclusion first, then the figures behind it, what the chart cannot
   answer, and the Mermaid type with its loss. Read shapes as questions naming the shape, its dates
   and what to check (`wiki/showing-work/reading-a-cfd.md`, The walk and What a finding should
   carry; `wiki/reading-history/reading-a-cycle-time-scatterplot.md`).

## Common pitfalls

- **Don't** choose by the occasion ("for the demo"). **Do** choose by the question.
- **Don't** put a number in the file that the metrics do not hold.
- **Don't** report a shape as a cause or a bottleneck. **Do** report it as a question.
