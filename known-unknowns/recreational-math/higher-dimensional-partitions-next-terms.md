# Solid and higher-dimensional partitions: the next term of A000293 (solid, n = 73) or A000334 (4D, n = 41), or of the 5- to 8-dimensional counts

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster for A000293(73); laptop-hours to laptop-days for the 6- to 8-dimensional partials · open as of 2026-10-30

## The problem

The number of d-dimensional partitions of n has no known generating function for d >= 3: MacMahon's guess A000294 fails for solid partitions (Atkin, Bratley, McDonald and McKay 1967; Knuth 1970). Solid partitions A000293 are known to n = 72. The Solid Partitions Project at IIT Madras (Suresh Govindarajan and Srivatsan Balakrishnan, with Intel India support) finished p3(72) = 3464274974065172792 on 3 Jan 2013 and has been paused since; the b-file 0..72 is Govindarajan's. Other OEIS ranges: 4D A000334 to n = 40 (Govindarajan), 5D A000390 to n = 30, 6D A000416 to n = 21, 7D A000427 to n = 20 and 8D A179855 to n = 17. These OEIS ranges for 6D-8D are stale. Govindarajan's 'Notes on higher-dimensional partitions' (JCTA 2013, arXiv:1203.4419) lists d <= 10 up to n = 23 (Table 1), and its F-matrix (Table 4) determines partitions of every n <= 25 in every dimension. His b-file for A119271, the triangle of partitions of n whose Ferrers diagram spans exactly m axes, now gives full rows n = 1..26. The sum p_d(n) = sum_m C(d+1,m) A119271(n,m) reproduces A000293, A000334 and A000390 at n = 26 (auditor check, 2026-10-30). So every dimension is determined for n <= 26, and in dimensions 6 and up the first unpublished value is n = 27. Balakrishnan-Govindarajan-Prabhakar (2011) and Destainville-Govindarajan (2015) studied the asymptotics, and Mondal (arXiv:2609.03034, Sep 2026) estimated them for d = 3..6 by Monte Carlo without adding exact terms. All re-fetched 2026-10-30.

## What counts as a win

The exact next term A000293(73) or A000334(41), not in the DATA or b-file when re-fetched immediately before claiming. It must come from two independent runs that agree, using different algorithms or branch decompositions. The same code must reproduce every published term of that sequence and of at least one other dimension.

## Partial wins

- **p1:** A new exact count in a lower-cost dimension: A000390(31) (5D), or p_d(27) for some d in 6..8 (6D, 7D or 8D partitions of 27; every n <= 26 is already determined by row 26 of the A119271 b-file). The code must reproduce all published terms of that dimension, Govindarajan's Table 1 values for n <= 23 and the values for n = 24..26 derived from A119271, under the same two-run rule.
- **p2:** The full row n = 27 of A119271: the partitions of 27 whose Ferrers diagram spans exactly m axes, for every m. Then p_d(27) = sum_m C(d+1,m) A119271(27,m) gives partitions of 27 in every dimension. The values derived for d = 3, 4, 5 must equal the published A000293(27), A000334(27) and A000390(27), under the same two-run rule.

## How a win is checked

Skeptic: check the code against the b-files for small n in two dimensions. Rerun the claimed term with an independent generator, for example a Bratley-McKay or Knuth-style generator vs the proper-partition binomial transform. For a cluster run, recompute a random sample of branches.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A000293/b000293.txt>

## Sources

- <https://oeis.org/A000293>
- <https://oeis.org/A000334>
- <https://oeis.org/A000390>
- <https://oeis.org/A000416>
- <https://oeis.org/A000427>
- <https://oeis.org/A179855>
- <https://oeis.org/A119271>
- <https://arxiv.org/abs/1203.4419>
- <http://boltzmann.wikidot.com/solid-partitions>
- <https://arxiv.org/abs/1105.6231>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The binomial relation over A119271 turns one enumeration into terms for every dimension at once. Govindarajan's 2013 triangles (A, C, F matrices) already halve the data needed; extending them from row 26 to row 27 is the natural route for the higher dimensions.
- Since p_3 is known to 72, p_4 to 40 and p_5 to 30, A119271(n,m) for m <= 6 is already determined well beyond n = 27. Only the m >= 7 entries are new: p_6(27) needs just A119271(27,7), p_7(27) adds m = 8 and p_8(27) adds m = 9.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Offsets: A000293 starts at n = 0, the others at n = 1.
- A Monte Carlo estimate is never a term; only exact counts count.
- OEIS sequence entries lag for d >= 6: a value missing from A000416, A000427 or A179855 may already follow from the A119271 b-file (full rows to n = 26) or Govindarajan's 2013 tables. Check those before claiming.
- Index convention: column m of A119271 counts Ferrers diagrams spanning exactly m axes (exactly (m-1)-dimensional partitions), and d-dimensional partitions use C(d+1,m), not C(d,m). Check the transform against A000293(26) = 120256653 before trusting it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/higher-dimensional-partitions-next-terms.md
```

Already set up? Say `run V3R1T4S on higher-dimensional-partitions-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `higher-dimensional-partitions-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
