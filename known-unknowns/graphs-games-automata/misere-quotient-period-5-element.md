# Impartial misere quotients: exhibit an element of period 5 (or 8, or any period other than 1, 2, 3, 4, 6)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (quotient computations over many small game trees or heap rules; enumeration of the quotients of order 20 for p1) · open as of 2026-10-30

## The problem

Plambeck and Siegel's misere quotient of a set A of impartial games (closed under options and sums) identifies two games G and H when G + X and H + X have the same misere outcome for every X in A. The quotient Q is a commutative monoid with a P-portion. An element x has period p if p is the least positive integer with x^(n+p) = x^n for some n. Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem E12, from Plambeck and Siegel) says that quotients with elements of periods 1, 2, 3, 4, 6 and infinity have been found. It conjectures that every period occurs and asks for a quotient with a period-5 element, then period 8 and so on. It also asks for the smallest quotient with a period-4 (or 3 or 6) element, and for Siegel's classification of quotients to be extended beyond order 18. Siegel (arXiv:math/0703070, 2007) counted the quotients of orders 2, 4, ..., 18 as 1, 0, 1, 1, 1, 6, 9, 50, 211. Plambeck and Siegel (arXiv:math/0609825, Section A.6) gave a period-6 generator in the order-200 quotient of *(2#210)(2#30)3#21 and a period-4 element in the quotient of *(2#1)(2#0)4310, of order 120, the smallest then known with a period above 2. Simon Rubinstein-Salzedo and Stephen Zhou (arXiv:2603.18244, March 2026) showed that partizan misere quotients can have any finite cardinality except 3 and note that impartial ones have even cardinality. No 2026 arXiv math.CO title reports a new period.

## What counts as a win

CONFIRMED: an explicit impartial game G (a finite game tree in a documented notation, or a heap game with stated rules) and the misere quotient Q of its closure, in which some element x has a period p not in {1, 2, 3, 4, 6}, with p shown to be minimal from the table. Q is given as a presentation with its P-portion and multiplication table (or a finite rewriting system), computed by two independent programs (for example Siegel's MisereSolver and one written by the claimant). The example must not be published at verification time (Games of No Chance volumes, Siegel's Combinatorial Game Theory (AMS, 2013), arXiv).

## Partial wins

- **p1:** The number of non-isomorphic misère quotients of order 20, from two independent enumerations that both reproduce Siegel's counts 1, 0, 1, 1, 1, 6, 9, 50, 211 for orders 2 to 18. The count must not be published at verification time (check Siegel's Combinatorial Game Theory, AMS, 2013, and arXiv first).
- **p2:** A misère quotient that contains an element of period 4 (or 3 or 6) and has order strictly smaller than the smallest one published at verification time (order 120 in arXiv:math/0609825; check Siegel's 2013 book first), computed by two independent programs.

## How a win is checked

Recompute the quotient of the claimed game's closure with an independent implementation of the Plambeck-Siegel algorithm (outcomes of sums, indistinguishability, reduced bipartite monoid) and check that it is a valid misere quotient. Then compute powers of the claimed element until they repeat and confirm the cycle length. For p1, rerun the enumeration with separate code and compare the counts of isomorphism classes and their representatives.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Sources

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>
- <https://arxiv.org/abs/math/0609825>
- <https://arxiv.org/abs/math/0703070>
- <https://arxiv.org/abs/2603.18244>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The period-3 and period-6 elements came from games built by adjoining small options to nimbers (*(2#...)...). A structured search over game trees of the form *(a#b)(c#d)... with a MisereSolver-style engine, filtering for torsion in the quotient, is cheap per tree.
- Search heap games too: quaternary codes with 3-4 digits give quotients of moderate size quickly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Partizan misere quotients (arXiv:2603.18244) are a different object; this target is about impartial ones.
- Infinite quotients are common, and a computation that never stabilises is not evidence of anything.
- Plambeck's cash prizes (Dawson's Chess, .3102, .3122, .3123, .3312) are separate setter challenges and are not part of this target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/misere-quotient-period-5-element.md
```

Already set up? Say `run V3R1T4S on misere-quotient-period-5-element`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `misere-quotient-period-5-element`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
