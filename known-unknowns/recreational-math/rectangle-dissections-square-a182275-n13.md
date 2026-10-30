# Ways to divide an n x n square into integer-sided rectangles: the next term A182275(13) (known to n = 12 since Butler 2014)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (column transfer matrix with Fibonacci-many states) · open as of 2026-10-30

## The problem

A182275(n) is the number of ways to divide an n x n square into rectangles with integer sides. It is the main diagonal of the array A116694 (Helena Verrill 2006; b-file of antidiagonals 1..20 by Alois P. Heinz) and of the triangle A333476 (Peter Kagey; Heinz's b-file gives rows 0..12, i.e. every rectangle up to 12 x 12). Klarner and Magliveras (1988) and Smith and Verrill (2006) treated fixed widths. Blanco, Dougherty-Bliss, Ter-Saakov and Zeilberger (arXiv:2606.05439, June 2026) revisited fixed-width counts but did not extend the diagonal. Matthew C. Russell entered the sequence in 2012 and Steve Butler added a(11)-a(12) in Mar 2014. a(12) = 5.96e49 is the last term (re-fetched 2026-10-30; entry unchanged since 2023). A column transfer matrix works here. Along the current grid line, its state records which unit segments are crossed by a still-open rectangle (with that rectangle's exact extent) and which are edges (merged into runs). That gives Fibonacci-many states, F(2n+1). An unoptimised Python version reproduces a(1)..a(9) in about 15 seconds (rerun by the skeptic), so a(13), and probably a(14), are laptop computations with a cell-by-cell sweep.

## What counts as a win

The exact integer A182275(13) (dissections of the 13 x 13 square), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, using different decompositions (for example a column sweep vs a cell-by-cell broken profile, or a different state encoding). The same code must reproduce every published term a(0)..a(12) and every entry of the A116694 b-file.

## Partial wins

- **p1:** The exact number of dissections of the 13 x 12 rectangle into integer-sided rectangles (A116694(13,12), not in the A116694 or A333476 b-files), under the same two-run rule, with the code reproducing A182275(0..12).
- **p2:** A182275(14), after a(13) has been established, under the same two-run rule.

## How a win is checked

Skeptic (minutes to an hour): write an independent transfer-matrix program (the state description above is enough) and check it against the b-file for n <= 10. Then rerun the claimant's code for n = 13 with exact big integers or a fresh prime set.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A182275>

## Sources

- <https://oeis.org/A182275>
- <https://oeis.org/A116694>
- <https://oeis.org/A333476>
- <https://arxiv.org/abs/2606.05439>
- <https://doi.org/10.1016/S0195-6698(88)80062-3>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Processing cell by cell removes the exponential fan-out of whole-column transitions; exact Python integers are fine at this size (a(13) has about 60 digits).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Offset 0 (a(0) = 1); a(12) is the 12 x 12 square.
- Dissections are counted as distinct, not up to symmetry. Do not confuse this with A045846 (squares only), which is a separate bank entry.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/rectangle-dissections-square-a182275-n13.md
```

Already set up? Say `run V3R1T4S on rectangle-dissections-square-a182275-n13`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rectangle-dissections-square-a182275-n13`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
