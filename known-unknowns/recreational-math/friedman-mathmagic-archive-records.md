# Erich Friedman's Math Magic archive: beat a best-known entry on a monthly-problem page (non-packing categories)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Math Magic (1998-2020 monthly unsolved problems, archive at erich-friedman.github.io/mathmagic) keeps per-problem tables of best-known answers for each n (tilings, reptiles, numbers, digits, matrices, graphs, chess, games). Many were updated years after posting; the index's latest per-entry update is 3/25/23. Its 'Unsolved Problems from Math Magic' page lists 34 open questions with credited later progress (e.g. #8 proven in 2026 by Alec Kriebel, #19 found by Bryce Herdt, #20 proved by Vamshi Jandhyala, #33 disproved by Konstantin Kopp). Many still open items could be refuted or advanced by a single finite construction, e.g. #2: do any of 7 length-9 disconnected linear polyominoes tile a rectangle; #5: products of powers using 1..2n exactly once for n >= 2; #7: another shape with partridge number 4. Distinct from the bank's friedman-packing-records (the Packing Center). Target: a construction strictly improving a listed best-known value for some n on a Math Magic page, or a finite witness settling an item on unsolved.html.

## What counts as a win

Success means an explicit object (tiling coordinates, number, matrix, sequence) for one problem page linked from https://erich-friedman.github.io/mathmagic/index.html (excluding problems in the index's Packing category and anything under erich-friedman.github.io/packing, which friedman-packing-records covers) and one n, which (1) satisfies that page's stated rules as verified by an independent exact checker, and (2) is STRICTLY better in the page's own direction than the best entry for that n on the page re-fetched live immediately before claiming (or fills an n the table marks as unknown/blank within the range the page tabulates); OR an explicit finite witness that settles a question still listed as open on https://erich-friedman.github.io/mathmagic/unsolved.html re-fetched live (not one the page already credits as solved). The object must not appear in later literature found by searching the problem name. Emailing Friedman is NOT part of success.

## Partial wins

- **p1:** Extend a page's table to a new n just beyond the largest tabulated n with a verified construction plus a reproducible exhaustive-search log showing it is optimal for that n.
- **p2:** Unsolved #5: a verified solution for every n up to a bound beyond any n shown on the December 2000 page, with the search code.
- **p3:** Unsolved #2: a SAT/DLX-certified proof that one of the 7 disconnected polyominoes cannot tile any rectangle up to a stated size bound (bounded result, clearly labelled).

## How a win is checked

Write a per-page exact checker (integer coordinates / exact arithmetic), re-run it on the claimed object, fetch the live page and parse the table row for n, compare in the page's direction. Literature search on the problem title.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://erich-friedman.github.io/mathmagic/index.html>

## Sources

- <https://erich-friedman.github.io/mathmagic/index.html>
- <https://erich-friedman.github.io/mathmagic/unsolved.html>
- <https://erich-friedman.github.io/mathmagic/archivetile.html>
- <https://erich-friedman.github.io/mathmagic/archivenumber.html>
- <https://erich-friedman.github.io/mathmagic/archivedigit.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Triage: crawl every monthly page, extract tables with 'best known'/'?' cells, and rank by last-updated date (stale pages from 1999-2010 with blank cells are the softest).
- Exact cover / DLX and SAT (Kissat with cardinality encodings) for tiling and digit-arrangement problems; CP-SAT for matrix problems.
- Cross-domain import (VLSI floorplanning): rectangle-packing and tiling pages map directly onto floorplanning B*-tree / sequence-pair representations with simulated annealing.
- Cross-domain import (protein folding Monte Carlo): pull-move and replica-exchange Monte Carlo from HP-lattice protein folding for polyomino/polyform-shape optimisation pages.
- Number pages: meet-in-the-middle and modular sieving (as in sums-of-cubes searches) for digit/number records.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Each page has idiosyncratic rules (e.g. 'distinct', 'non-trivial', reflections allowed?); misreading them is the commonest false record.
- Updates to the pages are sporadic (latest index update 3/25/23, though unsolved.html credits a 2026 result); improvements may exist in later literature or OEIS but not on the page. Search before claiming.
- Direction varies per page; a 'larger' value is not always better.
- Do not overlap the Packing Center target (friedman-packing-records): packing pages under erich-friedman.github.io/packing and Math Magic problems in the Packing category are excluded here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/friedman-mathmagic-archive-records.md
```

Already set up? Say `run V3R1T4S on friedman-mathmagic-archive-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `friedman-mathmagic-archive-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
