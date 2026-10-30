# Polyomino number theory: the next count of free polyominoes tiled by n copies of a tetromino (I: A397019, T: A397020, L: A397021, S: A397022)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (hash-sharded canonical enumeration on disk: about 2-3e10 shapes for I, T or S and about 2e11 for L, so hundreds of GB of disk) · open as of 2026-10-30

## The problem

An n-fold multiple of a polyomino P is a polyomino that n copies of P can tile (Cibulis, Liu and Wainwright, Polyomino Number Theory I, Crux Math. 2002; Golomb 1981). In June 2026 Haoyang Xu entered four sequences counting the free n-fold multiples of the tetrominoes, up to rotation and reflection: A397019 (I-tetromino) to n = 8, A397020 (T) to n = 7 (a(7) = 733980532), A397021 (L) to n = 6 and A397022 (S) to n = 7. He computed them with a parallel hash-sharded on-disk method. All four carry 'more' and were re-fetched 2026-10-30. At the last published step the counts grew by about 27x (I), 40x (T and S) and 87x (L). The next terms are therefore about 2-3e10 free shapes for I, T and S and about 2e11 for L, each to be enumerated and deduplicated. The sibling tromino sequences A397720 and A397723 (Jul 2026) are not part of this target.

## What counts as a win

One new exact term: A397019(9), A397020(8), A397021(7) or A397022(8), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly and differ in canonical form or enumeration order. For example, one run can use lexicographically minimal sorted cells and the other a different canonical encoding with a different shard key. Or one run can grow shapes by adding a piece to every (n-1)-fold multiple and the other by removing a piece from candidate shapes. The same code must reproduce every published term of that sequence.

## Partial wins

- **p1:** An independent program that reproduces every published term of all four sequences, with code and run times published.

## How a win is checked

Skeptic: run the Python program in A397020 (it works to n = 5) against the claimant's code, check that the claimant's shape counts at each step reproduce the published terms, and rerun the new term with a different sharding.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A397020>

## Sources

- <https://oeis.org/A397020>
- <https://oeis.org/A397019>
- <https://oeis.org/A397021>
- <https://oeis.org/A397022>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A shape counts once however many tilings it has; deduplicate by free canonical form.
- These are brand-new sequences and the author may extend them soon; re-fetch right before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/tetromino-multiples-next-terms.md
```

Already set up? Say `run V3R1T4S on tetromino-multiples-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tetromino-multiples-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
