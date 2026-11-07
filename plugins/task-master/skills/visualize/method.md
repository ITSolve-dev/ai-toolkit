# visualize: method

A question in; one chart that answers it, as a Mermaid file, and a short text reading. The chart is
chosen by the question, not by the occasion. Read the question file first: it names the scope, the
reader, the setup and the capabilities that are not `native`. Open a cited page when a case is
borderline. "This wiki's reading" means the base marks the rule as its own, not a source's.

## Inputs and output

- **Passed:** the snapshot, its metrics file, the question file.
- **Every value in the chart is copied from the metrics file**, with its basis. A series the chart
  needs and the metrics lack: refuse and name the series and what produces it.
- **Output:** the chart at `.task-master/visualize-<slug>.mmd`, and after `status` the reading
  (step 6). A refusal writes no file and says why. Publishing goes to `needs_caller`: the plugin
  has no means of publishing. `changeset` stays empty.

## The charts

What each needs beyond the snapshot taken now. "History" means `history = "native"`; one snapshot
is one moment and cannot stand in for it.

| Chart | Answers | Needs |
|---|---|---|
| Iteration burndown | Will this period's work finish? | History: remaining size per day of the period |
| Release burndown, line | How far along is the release? | History, or one snapshot per period start; estimates |
| Release burndown, bars | Why did remaining work move? | History, to separate scope change from completion and re-estimation |
| Velocity | How much fits by a date, at what rate? | Estimates and finish times per closed period; by count without estimates |
| Parking lot | Which themes are behind? | The snapshot; the field that names a theme, from the caller or process document |
| Feature Gantt | What is planned for which period? | The snapshot's sprint on each task; sprint dates |
| Cumulative flow | How long do items take on average? Is more starting than finishing? | History: each item's entry date into each state |
| Cycle time scatterplot | How long may one item take? Did it change over time? | History: start and finish per finished item |
| Cycle time histogram | What shape is the data, how long the tail? | As the scatterplot |
| Aging view | What is open now, and how old? | Age per open item, and percentile lines from finished items |

Rows and questions follow `wiki/showing-work/which-chart-for-which-plan-question.md`; the aging view
is `wiki/reading-history/work-item-age.md`, How to read it. What each chart cannot answer is that
page's "Cannot ask" column. The "Needs" column is this method's reading of how each chart is built.

## Steps

1. **Map the question to a row.** Find the question on the page's plan or cycle time tables. A
   chart named instead of a question: state the question it answers; if the caller's question is
   another, name the chart that answers that one. No row fits: no chart, and the question goes to
   `not_covered`; the nearest chart is not offered in its place. A date for a set of items is a
   forecast, not a chart: it belongs to `schedule`. A plan-against-fact table belongs to
   `review-period`. *Output:* the row, or why none. *Wrong if:* the choice follows the occasion
   ("for the demo") rather than the question.

2. **Fit the setup and the reader.** Flow: no burndown or velocity exists; the question goes to the
   cycle time rows (`wiki/showing-work/which-chart-for-which-plan-question.md`, Flow setup). A reader
   outside the project gets count or elapsed time, never points
   (`wiki/showing-work/points-or-time-and-count.md`, The rule). Periods under two weeks: an iteration
   burndown is probably not worth drawing, and the reading says so
   (`wiki/showing-work/iteration-burndown.md`). *Wrong if:* points reach an outside reader.

3. **Check the data; refuse what it cannot support.** Hold the row's "Needs" against the question
   file and the snapshot header. Unmet: refuse, naming the input and the capability that lacks it,
   and say which question can still be answered from what there is. Nothing is approximated: a
   cumulative chart built from counts of what sits in each column is "dubious"
   (`wiki/showing-work/cumulative-flow-diagram.md`, Building it), and a burndown from one snapshot is
   one point. Age without history runs from creation: no aging view is drawn on it, and the reading
   may list those ages labelled "since created" (this method's own rule). Few finished items: the
   scatterplot over the histogram, read dot by dot (which-chart page, Which holds under which setup).
   *Wrong if:* a chart is drawn whose series the metrics do not hold.

4. **Draw one chart.** One question, one chart: several views at once bury the answer (which-chart
   page, Failure modes). Open with `%%` comment lines: the question, the snapshot's `taken_at` and
   `source`, each series' basis, and what the chart cannot answer. Construction rules: a cumulative
   line never falls (`wiki/showing-work/cumulative-flow-diagram.md`, Signs that a chart is not a
   CFD); a dot sits at its item's finish date (`wiki/showing-work/cycle-time-scatterplot.md`); a
   Gantt bar spans its whole period and shows no progress (which-chart page, plan table). *Wrong
   if:* the file holds a number not in the metrics.

5. **Name the Mermaid type and what it loses** (this method's own table; Mermaid's limits are not
   in the base):

   | Chart | Mermaid | Lost |
   |---|---|---|
   | Burndowns, velocity | `xychart-beta`, line or bar | No legend: series are named in the reading. The bar form's scope change below the axis cannot be drawn, so it goes as a table |
   | Cumulative flow | `xychart-beta`, one line per state | Bands are unfilled; read the gaps between lines. Dates are categories, so every day must be listed for even spacing |
   | Scatterplot | `xychart-beta`, one bar per item by finish date, percentiles as flat lines | No scatter type: the x axis is order, not time; gaps between dates vanish and stacked items stand side by side |
   | Histogram | `xychart-beta`, bars per cycle time band | Percentile lines cannot be vertical; they go in the reading |
   | Aging view | `xychart-beta`, one bar per open item, states as label prefixes in workflow order | States are labels, not columns |
   | Feature Gantt | `gantt`, a section per period | Nothing the question needs |
   | Parking lot | `flowchart`, one node per theme with its counts | Layout; a colour only with its stated test |

   A diagram type the table does not name, `pie` among them, answers no question here.

6. **Write the reading.** Conclusion first, then the figures behind it, then what the chart cannot
   answer, then the Mermaid type and its loss. A cumulative chart's shapes are read as questions,
   each naming the shape, its dates and what to check (`wiki/showing-work/reading-a-cfd.md`, The walk
   and What a finding should carry); likewise a scatterplot's
   (`wiki/reading-history/reading-a-cycle-time-scatterplot.md`). *Wrong if:* a shape is reported as
   a cause or a bottleneck.

## Notes

- The chart shows the board at `taken_at`; it is not kept in version control, because the state
  lives on the board (the plugin's design).
- Like `review-period`, this method has not been run on a real board's history; on invented data it
  checks only that the steps execute.
