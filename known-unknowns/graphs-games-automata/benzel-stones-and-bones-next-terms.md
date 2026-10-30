# Stones-and-bones tilings of benzels (Propp's Problems 15-18): the next terms of A364416 and A364417, or of the weighted A364418 and A364438

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (transfer matrix on the triangular grid) · open as of 2026-10-30

## The problem

Benzels are hexagon-like regions of hexagonal cells, introduced by James Propp. A stones-and-bones tiling covers one with stones (three mutually adjacent hexagons, Conway-Lagarias T_2) and bones (three collinear hexagons, L_3). Propp's 'Trimer covers in the triangular grid: twenty mostly open problems' (arXiv:2206.06472, v4 Jan 2024) poses enumeration problems, and he entered the sequences in OEIS. A364416 counts all stones-and-bones tilings of the (n,2n-4)-benzel (Problem 15), known to n = 20 (a(20) = 87817595880192684). A364417 does the same for the (n,2n-3)-benzel (Problem 16), known to n = 19. Propp extended both in Apr 2024. No formulas are known; Propp conjectures 2-adic continuity. Weighting each stone by 3 gives A364418 and A364438 (Problems 17-18), with b-files to n = 17. Propp's Benzel Tilings Site lists Problems 14-20 as open but Problems 9 and 11 as solved (Byun, Ciucu and Lee). So A364481 and A364483 follow from proven formulas and are not part of this target. All re-fetched 2026-10-30.

## What counts as a win

The exact next term A364416(21) or A364417(20), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, and the same code must reproduce every published term of A364416 and A364417.

## Partial wins

- **p1:** The next term of A364418 (n = 18) or A364438 (n = 18), the stone-weight-3 sums, with the code reproducing all published terms of both, under the same two-run rule.
- **p2:** Five or more new consecutive terms of A364416 or A364417 beyond the published range, under the same two-run rule.

## How a win is checked

Skeptic: check the claimant's code against all published terms of A364416-A364418 and A364438 (small benzels can also be checked by an independent exact-cover count). Then rerun the new term modulo a fresh prime or with exact integers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A364416>

## Sources

- <https://arxiv.org/abs/2206.06472>
- <http://jamespropp.org/benzels.html>
- <https://oeis.org/A364416>
- <https://oeis.org/A364417>
- <https://oeis.org/A364418>
- <https://oeis.org/A364438>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The (a,b)-benzel coordinates must follow Propp's paper exactly (cells whose barycentric centres satisfy -(a-1) <= j-i, k-j, i-k <= b-1); reproduce every published term before trusting new ones.
- Offsets: all four sequences start at n = 3.
- A364481 and A364483 (one bone orientation forbidden) are solved by formula and do not count here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/benzel-stones-and-bones-next-terms.md
```

Already set up? Say `run V3R1T4S on benzel-stones-and-bones-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `benzel-stones-and-bones-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
