# Fixed polyominoes: the exact count of 71-cell polyominoes (next term of OEIS A001168 after Barequet and Ben-Shachar's n = 70)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (Jensen's transfer-matrix method; states and run time grow about 2^(n/2) per width, with n = 70 needing a large parallel run) · open as of 2026-10-30

## The problem

A001168 counts polyominoes up to translation. Iwan Jensen's transfer-matrix algorithm (2001, 2003 cluster version) gave terms to n = 56. Gill Barequet and Gil Ben-Shachar ('Counting Polyominoes, Revisited', ALENEX 2024) pushed this to n = 70. Vuong Bui (arXiv 2211.14909) quotes a(69) and a(70), and the b-file (0..70) is theirs. The count is the primary input for series analysis of Klarner's constant (about 4.0626) and for the free-polyomino table. The OEIS page was checked live 2026-10-30 (last edit 2026-10-19, links only; no pending draft): a(71) is not listed.

## What counts as a win

Success means the exact integer a(71) of A001168, or the next unknown term if the live b-file, re-fetched immediately before claiming, has grown. It must come from two runs that agree exactly. The runs must differ in modulus set or arithmetic AND in decomposition (for example different width splits, or row vs column sweeps). The same code must reproduce every published term for n <= 70 exactly. Sanity check: a(71)/a(70) must lie strictly between a(70)/a(69) = 4.00512... and 4.0626.

## Partial wins

- **p1:** An independent reproduction of a(57)..a(70) by a program written from scratch (not Jensen's or Barequet and Ben-Shachar's code) that agrees exactly with the b-file, with source and run logs. It must also give a(71) modulo at least one 61-bit prime, computed by two different decompositions that agree.

## How a win is checked

Skeptic: rerun the claimant's program for n <= 50 and compare with the b-file; rerun the n = 71 computation modulo one fresh prime for a subset of width classes and compare residues; check ratio consistency.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A001168>

## Sources

- <https://oeis.org/A001168>
- <https://oeis.org/A001168/b001168.txt>
- <https://arxiv.org/abs/2211.14909>
- <https://arxiv.org/abs/cond-mat/0007239>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Fixed (A001168), one-sided and free (A000105) counts differ; this target is fixed counts only.
- Width-split runs must cover every bounding-box shape exactly once (Jensen counts width <= length and doubles the non-square cases); off-by-one in the square case is a classic error.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/fixed-polyominoes-a001168-n71.md
```

Already set up? Say `run V3R1T4S on fixed-polyominoes-a001168-n71`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fixed-polyominoes-a001168-n71`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
