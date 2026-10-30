# Partitions of the n x n grid into connected pieces (polyomino tilings of the square): the next term A145835(13), or the symmetric count A291807(13) as a partial win

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-days (frontier DP with connectivity states, modular arithmetic) · open as of 2026-10-30

## The problem

A145835(n) counts compositions of the n x n grid graph, i.e. partitions of an n x n square into orthogonally connected regions; these are all tilings of the square by polyominoes of any shape. Brian Kell defined it in 2008, after Knopfmacher and Mays (Graph compositions I, 2001). Frank Simon computed a(7)-a(10) (2011 and his 2012 TU Dresden thesis) and John F. Rudge a(11)-a(12) in Apr 2026 with a Python program (github johnrudge/oeis); a(12) = 4.12e66. Rudge also took two related sequences to n = 12: the free count up to rotation and reflection, A291806 (John Mason's sequence; a(5) by Christian Sievers 2026), and the symmetric count A291807. The rectangular table A110476 has a b-file of 220 terms (Walter Trump; the first 40 by Hugo van der Sanden). All re-fetched 2026-10-30: there is no term for n = 13.

## What counts as a win

The exact integer A145835(13), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, using different primes or exact integers and a different sweep order or state encoding. The same code must reproduce a(1)..a(12) and the A110476 b-file entries with m, n <= 12.

## Partial wins

- **p1:** A291807(13) (symmetric polyomino tilings of the 13 x 13 square), together with the counts of tilings fixed by each symmetry of the square, with the code reproducing A291807(1..12), under the same two-run rule.
- **p2:** The exact number of partitions of the 12 x 13 rectangle into orthogonally connected regions (A110476(12,13), not in Trump's b-file), under the same two-run rule, with the code reproducing A145835(1..12).

## How a win is checked

Skeptic: run Rudge's published program or an independent frontier DP for n <= 9 and compare with the b-files, then rerun the claimant's code for n = 13 modulo one fresh prime. A291806(13) follows from A145835(13) and the symmetric counts by Burnside's lemma, which the skeptic recomputes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A145835>

## Sources

- <https://oeis.org/A145835>
- <https://oeis.org/A291806>
- <https://oeis.org/A291807>
- <https://oeis.org/A110476>
- <https://github.com/johnrudge/oeis>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Frontier state: give each of the n boundary cells a block label (a non-crossing set partition of frontier cells into regions) and record which regions may still be closed. Canonical relabelling keeps the state count near the Motzkin-like count.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rudge extended the sequence six months ago; check the history page and his repository before claiming.
- Do not mix up A145835 (all partitions), A291806 (up to symmetry) and A291807 (symmetric ones).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/grid-compositions-polyomino-tilings-a145835-n13.md
```

Already set up? Say `run V3R1T4S on grid-compositions-polyomino-tilings-a145835-n13`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `grid-compositions-polyomino-tilings-a145835-n13`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
