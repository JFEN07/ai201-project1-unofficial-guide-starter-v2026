# The Unofficial Guide

My name is Julian Fennema, and I'm tackling the `city_guides` corpus.

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This is a system that allows users to search for the consensus of documents
for specific questions. This system will use the city_guides corpus, which 
consists of the towns within a region and what they offer/support in terms 
of places to eat, stay, transportation, sightseeing, accessibility and more.
This system is designed to answer questions like what time of year is best 
visit the region or what is the most common source of confusion when it 
comes to traveling by bus.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

For my strategy, within config.py, the chunk size was increased to 1400 as the city_guides corpus consists of large documents that average 2,068 characters each. For the overlap, its size was slightly lowered to 100 to avoid large paragraphs from seeping across chunks, but allow for paragraph headings and endings to transfer through.

**Chunk size: 1400 **
**Overlap: 100 **

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.

**Brightwater** is level along the river and through the centre. The mill museum
is step-free. The station is a 15-minute walk from campus on flat ground, or the
shuttle meets the four busiest arrivals.

## Mixed

**Pellew Sands** has a two-mile seafront that is flat the whole way, and
everything of interest is on it or one street back. The land train runs the
length of the promenade hourly between Easter and September. The beach itself is
hard sand and manageable at low tide.

**Givens Mill** is one flat street along the river. The mill tour involves
stairs and the machinery floor is not accessible; the tearoom and riverside are.
```

**Chunk 2** — source: `guide_corry_vale.md#1` — produced by: `chunker.py::split_documents`

```
## What to see

The valley itself is the attraction. The footpath network is dense and well 
marked, and a circuit taking in three of the four villages is about nine miles 
with 500 metres of ascent. The chapel in the second village is 12th century 
and always unlocked.

## Where to stay

Perhaps thirty beds in the entire valley, spread across two pubs and a handful of 
farmhouse rooms. In summer these are booked months ahead. Camping is permitted on 
two marked fields and nowhere else.

## When to go

May to September. Outside those months the pub in the third village closes, 
the farm shop reduces its hours, and several footpaths become genuinely boggy 
rather than merely wet. The road is not gritted above the second village and is 
impassable in snow.

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```

**Chunk 3** — source: `guide_givens_mill.md#0` — produced by: `chunker.py::split_documents`

```
# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds 
flour commercially. It is the sort of place people visit for an afternoon and then 
talk about for longer than the visit lasted.

## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, 
taking 30 minutes. Driving is 20 minutes. The village car park holds about forty 
cars and is full by 11am on summer Saturdays.

## Getting around

Everything is on one street along the river. The mill is at one end and the church 
at the other, eight minutes apart. The riverside path continues in both directions 
for as far as you want to walk.

## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread 
made from the flour ground twenty metres away and is the reason most people come. One 
pub, food served lunchtimes and Thursday to Saturday evenings.

## What to see

The mill runs tours on the hour from 11 to 3 and the machinery is operating during 
them, which is loud and much more impressive than a static exhibit. The church has a 
Saxon doorway. The river walk downstream reaches Brightwater in about three hours.

## Where to stay

Nothing in the village itself. The nearest rooms are in Brightwater, which is close 
enough that this is not really a problem — most people come for a half day.
```

**Chunk 4** — source: `guide_kestrelford.md#1` — produced by: `chunker.py::split_documents`

```
## Where to stay

Two inns on the square and a handful of rooms above the pubs. Booking ahead matters 
between May and September and not at all otherwise. There is no accommodation of any 
kind within four miles of the town in either direction.

## When to go

Late spring and early autumn. The Saturday market runs year-round but is much 
reduced from November to February. August is busy with walkers. The single-track 
approach road is genuinely difficult in snow and the town can be cut off for a day 
or two most winters.

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```

**Chunk 5** — source: `guide_regional_transport.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region

## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.

## Buses

Three operators run in the region and they do not accept each other's tickets,
which is the single most common source of confusion for visitors. Services
concentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford service is hourly on weekdays, two-hourly on Saturdays, and
does not run on Sundays. The Halden Bay coast service runs four times daily
year-round.

## Driving

Roads are good between the towns and poor on the approaches to both Kestrelford
and Halden Bay. The Kestrelford approach is single-track with passing places
for the final eight minutes. The Halden Bay coast road is cut into the cliff
and is slow rather than difficult.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question: "How do the city guides describe Thornby Wells to people getting around the region with limited mobility?" **

**Answer: According to `guide_accessibility.md`, Thornby Wells is described as the easiest town in the region, being flat, compact, and having everything within three minutes of everything else. It notes that the pump room and gardens are level throughout, parking is free for two hours anywhere in town, and the station is central. **

```
Sources retrieved: guide_accessibility.md, guide_thornby_wells.md, guide_walking.md
```

**My relevance cutoff: 0.75 **

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| 1. Which towns in the city guides are considered good or reliable options for tourists to go during the winter season? | Yes | 0.4749 |
| 2. What market in what town is considered the best in the region? | Yes | 0.5237 |
| 3. What week do the city guides argue as the best to visit Brightwater? | Yes | 0.3947 |
| 4. How do the city guides describe Thornby Wells to people getting around the region with limited mobility? | Yes | 0.4348 |
| 5. What do the city guides say the most common source of confusion from the three bus operators is? | Yes | 0.7043 |
| 6. What is the capital of Mongolia? | No | 0.8886 |
| 7. How do I change the oil in a diesel engine? | No | 0.9075 |
| 8. Who won the 1994 World Cup? | No | 1.0349 |
| 9. What is the recommended dosage of ibuprofen for a headache? | No | 0.8335 |
| 10. How do I write a for loop in Rust? | No | 0.8746 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1. When I asked Claude to build the chunking function from my corpus details and preferences, it allowed paragraphs without headers to appear in two chunks. I edited the body function and lowered the overlap size.**

**2. When I asked ChatGPT for additional examples for generating questions and expectations, it suggested referencing 
the exact document source in the question. Instead, I had my questions either include from the corpora ("city guides") 
or be a general question covering the entire corpora with no mention of it.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4 of 5 | 4 of 5 | 4 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 4 of 5 | 4 of 5 | 4 of 5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks begin and end with complete sentences | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. One source document named contains 'expects' phrase | 5 of 5 | 4 of 5 | 4 of 5 | 4 of 5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

```
Run log — before

Produced by: `run_eval.py::main`
Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
Corpus: `city_guides` (index variant `default`)
top-k: 4 · relevance cutoff: 0.75
Runs per question: 3, caching off
When: 2026-09-23 20:57
```

**Criterion 1**: 4 of 5 retrieved chunks include one that contains the answer (MET)
```
| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Which towns in the city guides are considered good or reliable options for tourists to go during the winter season? | pass | pass | pass |
| What market in what town is considered the best in the region? | pass | pass | pass |
| What week do the city guides argue as the best to visit Brightwater? | pass | pass | pass |
| How do the city guides describe Thornby Wells to people getting around the region with limited mobility? | fail | fail | fail |
| What do the city guides say the most common source of confusion from the three bus operators is? | pass | pass | pass |
```

**Criterion 2**: 5 of 5 answers should name a source document (MISSED) Only 4 of 5 produced a source, below is the fail.
```
### Which towns in the city guides are considered good or reliable options for tourists to go during the winter season? — run 1

- Best distance: 0.4749 (passed the gate)
- Sources retrieved: guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_thornby_wells.md

Based on the provided documents, Thornby Wells is described as the region's most reliable winter destination after Marchwood, and Marchwood is noted as working well in winter because almost everything is indoors and nothing closes seasonally. 

Sources: `guide_thornby_wells.md` and `guide_marchwood.md`.
```

**Criterion 3**: The relevance gate stops 4 of 5 out-of-corpus questions (MET)
```
## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.75. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.889 | refused |
| How do I change the oil in a diesel engine? | 0.907 | refused |
| Who won the 1994 World Cup? | 1.035 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.833 | refused |
| How do I write a for loop in Rust? | 0.875 | refused |

```

**Criterion 4**: 4 of 5 sampled chunks will begin and end with complete sentences (MET)
```
run_eval.py doesn't produce the 5 sample chunks for each question, but the five sample chunks generated by chunker.py all satisfy criterion 4 and all the answers produced are complete sentences as well.
```

**Criterion 5**: 5 of 5 of the answers will produce one source containing the expects phrase (MISSED) Only 4 of 5 produced a source with the expects phrase, below is the fail. Expects: "straightforward, easiest"; guide_accessibility.md contains the words straightforward and easiest, but not the exact phrase in expects.
```
### How do the city guides describe Thornby Wells to people getting around the region with limited mobility? — run 1

- Best distance: 0.4348 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_thornby_wells.md, guide_walking.md

According to **guide_accessibility.md** and **guide_walking.md**, Thornby Wells is described as the easiest town in the region for limited mobility. It is flat and compact with level streets and formal gardens, and everything is within three minutes of everything else.
```


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | 4 of 5 Retrieved chunks contain the answer | MET | For all three runs, the respective chunks contained the answers for questions 1, 2, 3, and 5, only failing to correctly answer question 4 on all three runs, arguably because of the expects phrase I chose. |
| 2 | (5 of 5) Every answer names a source | MISSED | This was a fail because in the first run, the answer to question 1 failed to name the source in the answer, resulting in 4 of 5 answers fulfilling the criterion, and in the second and third runs the source wasn't included in the answers for question 5, also resulting in 4 of 5 answers fulfilling the criterion, but failing to reach the 5 of 5 threshold across runs. |
| 3 | Gate stops 4 of 5 out-of-corpus questions | MET | The results showed that all 5 out-of-corpus questions were refused as they exceeded the 0.75 threshold cutoff, successfully fulfilling the criterion of the gate stopping at least 4 of 5 out-of-corpus questions from being answered. |
| 4 | 4 of 5 Sampled chunks begin and end with complete sentences | MET | All 5 sampled chunks used to answer the questions across all three runs were either headed by a header or properly began at the beginning of a sentence and ended at the end of a sentence. This also shows my chunker.py function is working successfully. |
| 5 | (5 of 5) One source document named by answer contains 'expects' phrase | MISSED | This criterion failed as it is an extension of the second criterion and somewhat of the first criterion where it was already determined that only 4 of 5 answers contained a source for all three runs and 4 of 5 retrieved chunks contained the answer, although the source could differ from the chunk. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
