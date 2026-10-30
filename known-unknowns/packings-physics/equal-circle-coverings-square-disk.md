# Thinnest coverings by n equal circles: cover the unit square (Nurmela-Ostergard table, n <= 30) or a disk (Tan, n = 21..25) with smaller circles

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Find n equal circles of the smallest radius r that together cover a given region. Square: Nurmela and Ostergard ('Covering a square with up to 30 equal circles', HUT TCS Research Report A62, June 2000) list the best known r(n) for the unit square to 20 digits, n = 1..30, e.g. r(10) = 0.21823351279308384300, r(30) = 0.12203686881944873607. Erich Friedman's 'Circles Covering Squares' page (unit circles, side s = 1/r) shows n <= 12 with the same values, credits Nagy (1974), Melissen (1997), Melissen-Schuur (1997), Tarnai-Gaspar (1995) and Nurmela-Ostergard (2000), and marks n = 3, 4, 5, 7 proved. Disk: Friedman's 'Circles Covering Circles' (unit circles covering the largest circle of radius R) lists n <= 25, found by Melissen (1997) and Jeremy Tan (2018), with proofs credited to Bezdek, G. Fejes Toth and, for n = 11..20, VoxEquinox (2026). The values for n = 21..25 (3.804+, 3.948+, 4.000+, 4.076+, sqrt6+sqrt3) are unproved. Equilateral triangle: Friedman's 'Circles Covering Triangles' shows n <= 9 (Melissen, Schuur 1997), and Nurmela (Experiment. Math. 9 (2000)) extends this to 36. Friedman's polygon-covering pages (squares or triangles covering squares, circles or triangles) were updated 25-Sep-2026 with records by A. Mukhamedov and Ryan Chi (Sep 2026), T. Green, D. Cantrell, M. Morandi and D. Paterson.

## What counts as a win

Success means n circle centres (rational) and a radius r for one region and n such that the union of the closed disks covers the region, certified by interval arithmetic (see verification), and r is STRICTLY SMALLER (direction: min) than the bar. Square, any n in 6..30 except 7: bar = the Nurmela-Ostergard A62 value for that n, or anything smaller published later, with margin r <= bar - 1e-10. Disk (unit radius R = 1 equivalently: n unit circles covering a circle of radius R* strictly larger), n in 21..25: R* must be at least Friedman's displayed truncated value + 0.001, since the page shows only 3 decimals with '+' and Tan's exact values are not posted, and must beat any later source. Cells marked proved on the live pages cannot be won.

## Partial wins

- **p1:** Triangle: n unit circles covering an equilateral triangle of side strictly larger, by at least 0.001 over the displayed value, than Friedman's live 'Circles Covering Triangles' value for n = 7 or 8 (Schuur 1997), certified as in the main criterion, and strictly larger than Nurmela's value for that n (Experiment. Math. 9 (2000) 241-250). If the verifier cannot obtain Nurmela 2000, the claim stays PROMISING until someone checks it.
- **p2:** A polygon-covering record: n unit squares or unit equilateral triangles covering a square, circle or triangle strictly larger than the value on the live Friedman page (squcosqu, sqcovcir, squcotri, tricosqu, tricovcir, tricovtri) for a listed n, beating the displayed value by at least one unit in its last shown decimal, with covering certified by exact or interval arithmetic.

## How a win is checked

Covering certificate: the closed region K is covered by disks D_i iff every 'critical point' is covered, where the critical points are the corners of K, every intersection of a circle with the boundary of K, and every pairwise circle intersection point lying in K. Each must lie in some other closed disk, and the cells must be non-empty. Run this in interval arithmetic at 50 digits with circles of the claimed r. Cross-check by adaptive quadtree subdivision: every box must sit inside some disk, proved by an interval test of the farthest corner. Compare r with the A62 value (from www.tcs.hut.fi/old/reports/A62.ps.gz) or with the live Friedman page, after converting between unit-square r and unit-circle s = 1/r.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://erich-friedman.github.io/packing/circovsqu/>

## Sources

- <https://erich-friedman.github.io/packing/circovsqu/>
- <https://erich-friedman.github.io/packing/circovcir/>
- <https://erich-friedman.github.io/packing/circovtri/>
- <http://www.tcs.hut.fi/old/reports/A62abstract.html>
- <http://www.tcs.hut.fi/old/reports/A62.ps.gz>
- <https://erich-friedman.github.io/packing/sqcovcir/>
- <https://erich-friedman.github.io/packing/squcosqu/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Coverings are rigid 'bar frameworks' (equidistant graphs): optimise r by minimising the uncovered area with BFGS from random starts, as Nurmela-Ostergard did, then polish the structure with Newton's method on the active critical points.
- For the disk, n = 21..25, start from hexagonal patches with one or two rotated outer rings.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Friedman's covering pages for circles (2005 and 2019 stamps) lag the literature: the square page stops at n = 12 and the triangle page at n = 9, while Nurmela-Ostergard (square, n <= 30) and Nurmela (triangle, n <= 36) go further. Always compare with the literature tables.
- Normalisation: A62 gives r for the unit square; Friedman gives the side s for unit circles (s = 1/r). The disk page fixes unit circles and maximises R.
- Grid sampling does not prove coverage: tiny uncovered slivers near triple points are typical. Use the critical-point plus interval certificate.
- Friedman's covering pages are part of his Packing Center; the bank entry friedman-packing-records covers packings only (its criterion requires disjoint interiors), not coverings.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/equal-circle-coverings-square-disk.md
```

Already set up? Say `run V3R1T4S on equal-circle-coverings-square-disk`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `equal-circle-coverings-square-disk`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
