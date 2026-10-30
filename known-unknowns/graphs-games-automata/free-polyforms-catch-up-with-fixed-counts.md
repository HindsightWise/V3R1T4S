# Free polyominoes, polyhexes and polyiamonds: close the gap to the fixed counts (A000105 beyond n = 59, A000228 beyond 36, A000577 beyond 52)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-days (symmetric-animal transfer matrices or enumeration of half-animals; big-integer or multi-prime arithmetic) · open as of 2026-10-30

## The problem

Three classic polyform tables have free counts (up to rotation and reflection) that lag far behind the fixed counts (up to translation). Polyominoes: fixed A001168 is known to n = 70 (b-file by Gill Barequet and Gil Ben-Shachar, ALENEX 2024; n <= 56 Iwan Jensen), but free A000105 stops at n = 59 (Toshihiro Shirakawa, arXiv 2510.22446, 2025; terms to 50 also John Mason). Polyhexes: fixed A001207 is known to n = 46 (Voege and Guttmann 2003, b-file by Vaclav Kotesovec) but free A000228 stops at n = 36 (John Mason and Robert A. Russell). Polyiamonds: fixed A001420 is known to n = 75 (Guttmann's 2009 book table, b-file by Kotesovec) but free A000577 stops at n = 52 (John Mason). By Burnside, free = (fixed + symmetric corrections)/|G|, and only the counts of animals with a nontrivial symmetry are missing; those grow roughly like the square root of the fixed counts. For polyominoes we checked (2026-10-30) that the identity fixed = 8 asym + 4(axial + diagonal + C2) + 2(two-axes + two-diagonals + C4) + D8 reproduces A000105 exactly for n = 20, 40, 59 from the b-files, and that at n = 60 every class count is already published (A006746 to 60, A006748 to 66, A056877 to 81, A056878 to 87, A144553 to 95, A142886 to 203) except the exactly-C2 class A006747 (to 59, Mason/Shirakawa). So A000105(60) follows from one new number: the count of fixed polyominoes of 60 cells invariant under a half-turn. All OEIS pages checked live 2026-10-30, no pending drafts.

## What counts as a win

Success means the exact value of the first unknown term of A000105 (n = 60 as of 2026-10-30), A000228 (n = 37) or A000577 (n = 53), with the N re-read from the live b-file immediately before claiming. The value must come with every published symmetry-class count it relies on and every new class count it introduces (for A000105(60): the half-turn-invariant count and the resulting A006747(60), A006749(60)). It must satisfy the Burnside identity exactly against the published fixed count (A001168, A001207 or A001420). The same code must reproduce all published free terms and class terms for at least the 15 largest published n. A new class count must also be confirmed by a second, independent method (a different algorithm or decomposition) that agrees exactly.

## Partial wins

- **p1:** The next unknown term of a published polyomino symmetry-class sequence other than A006747/A006749: A006746 (axial, b-file to 60), A006748 (diagonal, to 66), A056877 (two axes, to 81), A056878 (two diagonals, to 87), A144553 (C4, to 95) or A142886 (D8, to 203). The index is re-read from the live b-file. The same reproduction and two-method rules apply. A006747(60) is not a partial: it determines A000105(60), which is the full win.
- **p2:** The next unknown term of any published polyhex or polyiamond symmetry-class sequence that the free count A000228 or A000577 needs, at the first n beyond the free table. The same reproduction and two-method rules apply.

## How a win is checked

Skeptic (< 1 hour): recompute the Burnside identity from the claimant's class counts and the published fixed count, and check divisibility (the result must be an exact integer). Rerun the claimant's symmetric-class program for small n against the OEIS class sequences, and for the new n modulo one fresh prime if it uses modular arithmetic. Optional: an independent half-animal enumerator for n up to 40.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A000105>

## Sources

- <https://oeis.org/A000105>
- <https://oeis.org/A001168>
- <https://oeis.org/A006747>
- <https://arxiv.org/abs/2510.22446>
- <https://oeis.org/A000228>
- <https://oeis.org/A001207>
- <https://oeis.org/A000577>
- <https://oeis.org/A001420>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- A half-turn-symmetric polyomino of 2m or 2m+1 cells is determined by a 'half' attached to its centre (cell, edge midpoint or vertex). Count the halves with a Jensen-style transfer matrix on a half-plane with a twisted (glued) boundary row, as Barequet, Moffie, Ribo and Rote did for twisted cylinders.
- Redelmeier-type enumeration restricted to symmetric animals grows like lambda^(n/2), about 4^30 at n = 60: large but within reach for a multithreaded counter, and a second method for cross-checking.
- Use the published fixed counts as a free consistency test: a wrong class count almost always breaks integrality of the Burnside quotient.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A006747 counts polyominoes with exactly the C2 symmetry. A program that counts all half-turn-invariant polyominoes must subtract the two-axes, two-diagonals, C4 and D8 classes, each with the right weight.
- Polyhex and polyiamond free counts use the 12-element dihedral group of the hexagonal or triangular lattice. Polyiamonds have cell-centred symmetries for both triangle orientations. Reproduce the small published class counts before trusting the code.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/free-polyforms-catch-up-with-fixed-counts.md
```

Already set up? Say `run V3R1T4S on free-polyforms-catch-up-with-fixed-counts`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `free-polyforms-catch-up-with-fixed-counts`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
