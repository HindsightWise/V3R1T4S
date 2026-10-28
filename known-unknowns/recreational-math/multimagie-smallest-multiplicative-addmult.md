# Multimagie.com: smaller best-known multiplicative or additive-multiplicative magic squares (orders 7-17)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Christian Boyer's multimagie.com tables list the best known (mostly not proven minimal) multiplicative magic squares (smallest magic product P and/or smallest maximum entry 'Max nb'), pandiagonal multiplicative squares and additive-multiplicative squares for orders 3-17. Examples: 8x8 smallest known Max nb <= 117 and 9x9 <= 153 (Toshihiro Shirakawa, 2013), orders 10-17 products and Max nb (Shirakawa 2013, from his add-mult squares, plus Boyer and Luke Pebody 2005), a 9x9 pandiagonal multiplicative square with Max nb 1365 (Elbert Krison, 2017), and add-mult squares of orders 7 (Sebastien Miquel, 2016), 8-9 (Boyer 2005, after Walter Horner) and 10-17 (Shirakawa 2013). Target: a square of a listed type and order with strictly smaller P, Max nb or S (per the table's criterion) than the best known. Whether a 5x5 or 6x6 add-mult square exists is a live prize enigma, tracked separately and excluded here.

## What counts as a win

Success means an explicit n x n array of DISTINCT positive integers which an independent checker confirms has the type's properties (all rows, columns and both main diagonals with equal product; additionally equal sums for add-mult; all broken diagonals for pandiagonal), and whose criterion value (P, Max nb or S as named on the page) is STRICTLY SMALLER (direction: min) than the best-known value for that type and order on the relevant page among http://www.multimagie.com/English/Multiplicative.htm, Multiplicative6_7.htm, Multiplicative8_9.htm, Multiplicative10_.htm, AddMult10_.htm and SmallestAddMult.htm, re-fetched live immediately before claiming. Objects that would solve an enigma on http://www.multimagie.com/English/Enigmas.htm (e.g. any 5x5 or 6x6 add-mult magic square) are excluded. A literature search (arXiv, OEIS, Shirakawa/Miquel follow-ups) must also find no smaller published example.

## Partial wins

- **p1:** A pandiagonal multiplicative square improving a pandiagonal best-known entry.
- **p2:** An improvement in a secondary criterion (e.g. equal P but smaller MaxNb) where the page tracks both.

## How a win is checked

Python with exact integers: check distinctness, all line products (and sums), compute P, MaxNb, S, compare with the parsed live page. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.multimagie.com/English/Multiplicative.htm>

## Sources

- <http://www.multimagie.com/English/Multiplicative.htm>
- <http://www.multimagie.com/English/Multiplicative6_7.htm>
- <http://www.multimagie.com/English/Multiplicative8_9.htm>
- <http://www.multimagie.com/English/Multiplicative10_.htm>
- <http://www.multimagie.com/English/AddMult10_.htm>
- <http://www.multimagie.com/English/SmallestAddMult.htm>
- <http://www.multimagie.com/English/Problems.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exponent-vector reduction: a multiplicative square is an additive magic 'square' of exponent vectors over the primes used; build additive Latin-square-based magic squares for each prime's exponents and combine (Graeco-Latin products).
- For add-mult, start from Shirakawa/Miquel constructions and run local search (swap/scale moves) minimising MaxNb with CP-SAT feasibility repair.
- Cross-domain import (MIMO / orthogonal space-time codes): orthogonal-design combinatorics (Latin and Graeco-Latin structures used in coding) give systematic exponent layouts.
- Cross-domain import (portfolio optimisation): choosing the multiset of entries with fixed product as a knapsack on log-values; branch-and-bound on log-space with exact integer back-checks.
- Restrict to smooth numbers with small prime support (2,3,5,7,11,13) and enumerate entry multisets with the right prime-exponent totals.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Distinctness is mandatory; repeated entries invalidate the square.
- Semi-magic (rows/columns only) vs magic (plus diagonals) vs pandiagonal are different tables.
- The site is updated rarely and 'best known' may have been improved in print; search the literature before claiming. Fetch the pages over plain http (the https certificate does not verify).
- Do not confuse P (magic product) with MaxNb; the page may track both separately.
- 5x5 and 6x6 add-mult magic squares are live prize enigmas (Enigmas.htm), not table improvements; they are excluded from this target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/multimagie-smallest-multiplicative-addmult.md
```

Already set up? Say `run V3R1T4S on multimagie-smallest-multiplicative-addmult`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `multimagie-smallest-multiplicative-addmult`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
