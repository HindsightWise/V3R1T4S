# Odd-graceful tree conjecture (Gnanajothi): extend the verification past 12 vertices, or a tree that is not odd-graceful

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

A graph with q edges is odd-graceful (Gnanajothi 1991) if its vertices get distinct labels from {0,1,...,2q-1} so that the edge differences |f(u)-f(v)| are exactly the odd numbers 1, 3, ..., 2q-1. Every graph with an alpha-labeling is odd-graceful and no graph with an odd cycle is. R. B. Gnanajothi conjectured that every tree is odd-graceful and proved it for trees of order up to 10; Christian Barrientos extended this to trees of order up to 12 (unpublished, cited in DS6) and proved it for caterpillar forests and trees of diameter at most five. Gallian's Dynamic Survey DS6 (28th ed., 30 Oct 2025, Section 3.6) still gives order 12 as the bound. The next orders are tiny: 1,301 trees on 13 vertices, 19,320 on 16, 823,065 on 20 and 5,623,756 on 22 (OEIS A000055). Credit: Gnanajothi; Barrientos; Gallian.

## What counts as a win

Success means EITHER (a) a certificate that every tree on at most 22 vertices is odd-graceful: for each n in 13..22, a file giving every unlabeled tree on n vertices (as from nauty gentreeg) with an odd-graceful labeling, where an independent checker regenerates the trees, confirms the counts equal A000055(n), matches every tree by canonical form, and checks the labels are distinct in [0, 2n-3] with edge differences exactly {1, 3, ..., 2n-3}; OR (b) a tree with no odd-graceful labeling, certified by two independent exhaustive methods. Before claiming, re-check the latest DS6 edition and the literature for a higher verification bound.

## Partial wins

- **p1:** Certificate (as in (a)) that every tree on at most 16 vertices is odd-graceful.
- **p2:** Certificate that every tree on at most 20 vertices is odd-graceful.

## How a win is checked

Regenerate trees with gentreeg, compare counts with A000055, match certificate entries by canonical form, check each labeling's range, injectivity and the set of edge differences. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS6/pdf/>
- <https://oeis.org/A000055>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Trees with an alpha-labeling are odd-graceful (double the labels on one side and shift), so start from alpha-labelings and search directly only for the rest. Brinkmann, Crevals, Melot, Rylands and Steffen (DMTCS 14, 2012, https://dmtcs.episciences.org/569/pdf) computed the alpha-deficit of every tree up to 26 vertices and give the number of trees with nonzero deficit for each order (Appendix A: counts, not lists). That residue, which you must regenerate yourself, is the only part needing a direct search.
- Backtracking by largest odd difference first, as for graceful labelings.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Labels range over {0..2q-1}; edge differences must be exactly the q odd numbers below 2q.
- Barrientos's order-12 result is unpublished; DS6 is the source of the bound, and a later extension may exist, so search before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/odd-graceful-trees-beyond-12.md
```

Already set up? Say `run V3R1T4S on odd-graceful-trees-beyond-12`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `odd-graceful-trees-beyond-12`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
