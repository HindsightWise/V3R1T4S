# TSP Art (Bosch): a shorter tour for vangogh120K, venus140K, pareja160K, courbet180K or earring200K

🚚 **Optimization benchmarks** · standard · tractability ★★☆☆☆ · compute: laptop-days (120k-200k cities, EUC_2D; checking a tour takes seconds) · open as of 2026-10-30

## The problem

Robert Bosch's TSP Art instances are continuous-line drawings of famous paintings with 100,000 to 200,000 cities and TSPLIB EUC_2D distances. William Cook hosts them, posts the best tours and invites improvements. On 2026-10-29 (page unchanged from 2026-10-28) the records are vangogh120K 6,543,609 and courbet180K 7,888,731 (Kazuma Honda, Yuichi Nagata and Isao Ono, from their 2013 parallel GA-EAX paper, received in 2019), and venus140K 6,810,665, pareja160K 7,619,953 and earring200K 8,171,677 (Nagata, 2011). Emilio Bendotti, Francesco Cavaliere and Matteo Fischetti found 7,888,732 for courbet180K in 2019. No lower bounds are published. The sixth instance, mona-lisa100K, carries a live $1,000 prize and is excluded here. Find a shorter tour for one of the five.

## What counts as a win

A tour in TSPLIB TOUR_SECTION form (cities 1..n, each exactly once) for one of vangogh120K, venus140K, pareja160K, courbet180K or earring200K. A standalone checker computes TSPLIB EUC_2D lengths (each edge int(sqrt(dx^2+dy^2) + 0.5)) on https://www.math.uwaterloo.ca/tsp/data/art/ < name > .tsp. The length must be strictly below the Best Tour value for that instance on https://www.math.uwaterloo.ca/tsp/data/art/index.html, re-fetched immediately before claiming, and below any shorter tour found in a literature search. The checker must first reproduce the posted record tours at https://www.math.uwaterloo.ca/tsp/data/art/tours/ < name > _ < length > .tour (all five verified 2026-10-29). The tour, the checker, the instance sha256 and the page snapshot are saved together. Nothing is sent to Cook by the agent; the write-up goes to the human.

## How a win is checked

Download the .tsp file and the record tour. On 2026-10-29 the EUC_2D checker reproduced vangogh120K 6,543,609, venus140K 6,810,665, pareja160K 7,619,953, courbet180K 7,888,731 and earring200K 8,171,677 exactly. Each check takes a few seconds in Python.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.math.uwaterloo.ca/tsp/data/art/index.html>

## Sources

- <https://www.math.uwaterloo.ca/tsp/data/art/index.html>
- <https://www.math.uwaterloo.ca/tsp/data/art/vangogh120K.tsp>
- <https://www.math.uwaterloo.ca/tsp/data/art/tours/vangogh120K_6543609.tour>
- <https://www.math.uwaterloo.ca/tsp/data/art/tours/courbet180K_7888731.tour>
- <https://www.math.uwaterloo.ca/tsp/data/art/tours/earring200K_8171677.tour>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The records come from parallel GA-EAX with local EAX moves for 100k-city scale (Honda, Nagata and Ono 2013). Start an EAX population from the posted record plus diverse LKH tours, as Nagata did for the 2025 World TSP record.
- Bendotti, Cavaliere and Fischetti improved courbet180K by one unit in 2019 (7,888,733 to 7,888,732, starting from Nagata's 2011 tour; Honda et al.'s 7,888,731 was not yet public), so polishing a record tour with exact re-optimisation of windows (a Concorde or ILP solve on 500-2,000-city corridors with fixed endpoints) can still pay off.
- Art instances have strong local structure (dense dark regions, sparse light regions); allocate search effort by region rather than uniformly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- mona-lisa100K is on the same page but carries a live prize; it is a separate setter challenge and not part of this target.
- No lower bounds are posted, so a matching tour is not a proof of anything; only a strictly shorter tour counts.
- Use the exact file names (the page lists 'vangogh120.tsp' in one place, while the link is vangogh120K.tsp).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/tsp-art-bosch-five-instances.md
```

Already set up? Say `run V3R1T4S on tsp-art-bosch-five-instances`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tsp-art-bosch-five-instances`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
